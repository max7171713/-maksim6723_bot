train_gen = ImageDataGenerator
train_respil = ImageDataGenerator(rescale=1./255)
valide_gen = ImageDataGenerator(rescale=1./255)
train_gen = train_respil.flow_from_directori(train_dir,target_size,batch_size,class_mode)