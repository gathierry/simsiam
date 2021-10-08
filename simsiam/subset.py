import os
import torchvision.datasets as datasets


class ImageFolderSubset(datasets.ImageFolder):
    def __init__(self, subset_txt, **kwargs):
        super().__init__(**kwargs)
        if subset_txt is not None:
            with open(subset_txt, 'r') as fid:
                subset = set([line.strip() for line in fid.readlines()])

            subset_samples = []
            for sample in self.samples:
                if os.path.basename(sample[0]) in subset:
                    subset_samples.append(sample)

            self.samples = subset_samples
            self.targets = [s[1] for s in subset_samples]
