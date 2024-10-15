# SNMP MIB module (CIOMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIOMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:15 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adaptec_ObjectIdentity = ObjectIdentity
adaptec = _Adaptec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795)
)
_Storagemanagement_ObjectIdentity = ObjectIdentity
storagemanagement = _Storagemanagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2)
)
_Cio2_ObjectIdentity = ObjectIdentity
cio2 = _Cio2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12)
)
_MibRevision_ObjectIdentity = ObjectIdentity
mibRevision = _MibRevision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 1)
)
_RevMajor_Type = Integer32
_RevMajor_Object = MibScalar
revMajor = _RevMajor_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 1, 1),
    _RevMajor_Type()
)
revMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revMajor.setStatus("mandatory")
_RevMinor_Type = Integer32
_RevMinor_Object = MibScalar
revMinor = _RevMinor_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 1, 2),
    _RevMinor_Type()
)
revMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revMinor.setStatus("mandatory")
_StorageDevice_ObjectIdentity = ObjectIdentity
storageDevice = _StorageDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2)
)
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("mandatory")
_DevEntry_Object = MibTableRow
devEntry = _DevEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1)
)
devEntry.setIndexNames(
    (0, "CIOMIB", "devIndex"),
)
if mibBuilder.loadTexts:
    devEntry.setStatus("mandatory")
_DevIndex_Type = Integer32
_DevIndex_Object = MibTableColumn
devIndex = _DevIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 1),
    _DevIndex_Type()
)
devIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIndex.setStatus("mandatory")


class _DevType_Type(Integer32):
    """Custom type devType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("cartridgeRigidDiskDrive", 10),
          ("compactDiskDrive", 8),
          ("digitalVersatileDiskDrive", 15),
          ("digitalVersatileDiskRAMDrive", 16),
          ("flashDisk", 9),
          ("flexibleDisketteDrive", 4),
          ("magnetoOpticalDrive", 7),
          ("mediaChanger", 14),
          ("opticalFloppyDrive", 11),
          ("opticalWriteOnceReadManyDrive", 6),
          ("other", 1),
          ("rigidDiskDrive", 3),
          ("solidState", 13),
          ("tapeDrive", 12),
          ("unknown", 2))
    )


_DevType_Type.__name__ = "Integer32"
_DevType_Object = MibTableColumn
devType = _DevType_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 2),
    _DevType_Type()
)
devType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devType.setStatus("mandatory")


class _DevTypeDescr_Type(DisplayString):
    """Custom type devTypeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevTypeDescr_Type.__name__ = "DisplayString"
_DevTypeDescr_Object = MibTableColumn
devTypeDescr = _DevTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 3),
    _DevTypeDescr_Type()
)
devTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTypeDescr.setStatus("mandatory")


class _DevSubIdentifier_Type(DisplayString):
    """Custom type devSubIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevSubIdentifier_Type.__name__ = "DisplayString"
_DevSubIdentifier_Object = MibTableColumn
devSubIdentifier = _DevSubIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 4),
    _DevSubIdentifier_Type()
)
devSubIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSubIdentifier.setStatus("mandatory")
_DevMediaBlockSize_Type = Integer32
_DevMediaBlockSize_Object = MibTableColumn
devMediaBlockSize = _DevMediaBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 5),
    _DevMediaBlockSize_Type()
)
devMediaBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devMediaBlockSize.setStatus("mandatory")
_DevFormattedMediaCapacity_Type = Integer32
_DevFormattedMediaCapacity_Object = MibTableColumn
devFormattedMediaCapacity = _DevFormattedMediaCapacity_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 6),
    _DevFormattedMediaCapacity_Type()
)
devFormattedMediaCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFormattedMediaCapacity.setStatus("mandatory")


class _DevRemovableDevice_Type(Integer32):
    """Custom type devRemovableDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_DevRemovableDevice_Type.__name__ = "Integer32"
_DevRemovableDevice_Object = MibTableColumn
devRemovableDevice = _DevRemovableDevice_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 7),
    _DevRemovableDevice_Type()
)
devRemovableDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devRemovableDevice.setStatus("mandatory")


class _DevLoaded_Type(Integer32):
    """Custom type devLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_DevLoaded_Type.__name__ = "Integer32"
_DevLoaded_Object = MibTableColumn
devLoaded = _DevLoaded_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 8),
    _DevLoaded_Type()
)
devLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devLoaded.setStatus("mandatory")


class _DevRemovableMedia_Type(Integer32):
    """Custom type devRemovableMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_DevRemovableMedia_Type.__name__ = "Integer32"
_DevRemovableMedia_Object = MibTableColumn
devRemovableMedia = _DevRemovableMedia_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 9),
    _DevRemovableMedia_Type()
)
devRemovableMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devRemovableMedia.setStatus("mandatory")


class _DevMediaLoaded_Type(Integer32):
    """Custom type devMediaLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_DevMediaLoaded_Type.__name__ = "Integer32"
_DevMediaLoaded_Object = MibTableColumn
devMediaLoaded = _DevMediaLoaded_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 10),
    _DevMediaLoaded_Type()
)
devMediaLoaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devMediaLoaded.setStatus("mandatory")


class _DevCompression_Type(Integer32):
    """Custom type devCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_DevCompression_Type.__name__ = "Integer32"
_DevCompression_Object = MibTableColumn
devCompression = _DevCompression_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 11),
    _DevCompression_Type()
)
devCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCompression.setStatus("mandatory")


class _DevEncryption_Type(Integer32):
    """Custom type devEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_DevEncryption_Type.__name__ = "Integer32"
_DevEncryption_Object = MibTableColumn
devEncryption = _DevEncryption_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 2, 1, 1, 12),
    _DevEncryption_Type()
)
devEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devEncryption.setStatus("mandatory")
_StorageController_ObjectIdentity = ObjectIdentity
storageController = _StorageController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 3)
)
_CtlrTable_Object = MibTable
ctlrTable = _CtlrTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 3, 1)
)
if mibBuilder.loadTexts:
    ctlrTable.setStatus("mandatory")
_CtlrEntry_Object = MibTableRow
ctlrEntry = _CtlrEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 3, 1, 1)
)
ctlrEntry.setIndexNames(
    (0, "CIOMIB", "ctlrIndex"),
)
if mibBuilder.loadTexts:
    ctlrEntry.setStatus("mandatory")
_CtlrIndex_Type = Integer32
_CtlrIndex_Object = MibTableColumn
ctlrIndex = _CtlrIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 3, 1, 1, 1),
    _CtlrIndex_Type()
)
ctlrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlrIndex.setStatus("mandatory")


class _CtlrDescription_Type(DisplayString):
    """Custom type ctlrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtlrDescription_Type.__name__ = "DisplayString"
_CtlrDescription_Object = MibTableColumn
ctlrDescription = _CtlrDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 3, 1, 1, 2),
    _CtlrDescription_Type()
)
ctlrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlrDescription.setStatus("mandatory")


class _CtlrProtectionManagement_Type(Integer32):
    """Custom type ctlrProtectionManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("protected", 4),
          ("protectedThroughSCSI3SCC", 5),
          ("protectedThroughSCSI3SCC2", 6),
          ("unknown", 2),
          ("unprotected", 3))
    )


_CtlrProtectionManagement_Type.__name__ = "Integer32"
_CtlrProtectionManagement_Object = MibTableColumn
ctlrProtectionManagement = _CtlrProtectionManagement_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 3, 1, 1, 3),
    _CtlrProtectionManagement_Type()
)
ctlrProtectionManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlrProtectionManagement.setStatus("mandatory")


class _CtlrBusMaster_Type(Integer32):
    """Custom type ctlrBusMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("unknown", 2))
    )


_CtlrBusMaster_Type.__name__ = "Integer32"
_CtlrBusMaster_Object = MibTableColumn
ctlrBusMaster = _CtlrBusMaster_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 3, 1, 1, 4),
    _CtlrBusMaster_Type()
)
ctlrBusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlrBusMaster.setStatus("mandatory")
_CtlrSecondsSinceLastPowerUp_Type = Integer32
_CtlrSecondsSinceLastPowerUp_Object = MibTableColumn
ctlrSecondsSinceLastPowerUp = _CtlrSecondsSinceLastPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 3, 1, 1, 5),
    _CtlrSecondsSinceLastPowerUp_Type()
)
ctlrSecondsSinceLastPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlrSecondsSinceLastPowerUp.setStatus("mandatory")
_Enclosure_ObjectIdentity = ObjectIdentity
enclosure = _Enclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 4)
)
_EnclTable_Object = MibTable
enclTable = _EnclTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 4, 1)
)
if mibBuilder.loadTexts:
    enclTable.setStatus("mandatory")
_EnclEntry_Object = MibTableRow
enclEntry = _EnclEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 4, 1, 1)
)
enclEntry.setIndexNames(
    (0, "CIOMIB", "enclIndex"),
)
if mibBuilder.loadTexts:
    enclEntry.setStatus("mandatory")
_EnclIndex_Type = Integer32
_EnclIndex_Object = MibTableColumn
enclIndex = _EnclIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 4, 1, 1, 1),
    _EnclIndex_Type()
)
enclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclIndex.setStatus("mandatory")


class _EnclType_Type(Integer32):
    """Custom type enclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aemi", 6),
          ("decfault", 3),
          ("other", 1),
          ("safte", 4),
          ("ses", 5),
          ("unknown", 2))
    )


_EnclType_Type.__name__ = "Integer32"
_EnclType_Object = MibTableColumn
enclType = _EnclType_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 4, 1, 1, 2),
    _EnclType_Type()
)
enclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclType.setStatus("mandatory")


class _EnclDescription_Type(DisplayString):
    """Custom type enclDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EnclDescription_Type.__name__ = "DisplayString"
_EnclDescription_Object = MibTableColumn
enclDescription = _EnclDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 4, 1, 1, 3),
    _EnclDescription_Type()
)
enclDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclDescription.setStatus("mandatory")
_BusPort_ObjectIdentity = ObjectIdentity
busPort = _BusPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5)
)
_BusPortTable_Object = MibTable
busPortTable = _BusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1)
)
if mibBuilder.loadTexts:
    busPortTable.setStatus("mandatory")
_BusPortEntry_Object = MibTableRow
busPortEntry = _BusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1)
)
busPortEntry.setIndexNames(
    (0, "CIOMIB", "portIndex"),
)
if mibBuilder.loadTexts:
    busPortEntry.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")


class _PortProtocol_Type(Integer32):
    """Custom type portProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("ata-atapi", 6),
          ("diagnostic", 19),
          ("eisa", 3),
          ("escon", 18),
          ("fddi", 34),
          ("flexibleDiskette", 7),
          ("hippi", 22),
          ("i2c", 20),
          ("ieee488", 26),
          ("ieee802-3-100BaseVG", 32),
          ("ieee802-3-10Base2", 29),
          ("ieee802-3-10Base5", 28),
          ("ieee802-3-10Broad36", 31),
          ("ieee802-3-1Base5", 30),
          ("ieee802-5-Tokenring", 33),
          ("interface1496", 8),
          ("ipi", 25),
          ("isa", 4),
          ("mca", 35),
          ("multibus", 23),
          ("other", 1),
          ("parallelPort", 17),
          ("pci", 5),
          ("pcmcia", 15),
          ("power", 21),
          ("rs232", 27),
          ("scsiFibreChannel", 10),
          ("scsiParallel", 9),
          ("scsiSerialBusProtocol", 11),
          ("scsiSerialBusProtocol2", 12),
          ("scsiSerialStorageArchitecture", 13),
          ("universalSerialBus", 16),
          ("unknown", 2),
          ("vesa", 14),
          ("vme", 24))
    )


_PortProtocol_Type.__name__ = "Integer32"
_PortProtocol_Object = MibTableColumn
portProtocol = _PortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 2),
    _PortProtocol_Type()
)
portProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portProtocol.setStatus("mandatory")


class _PortProtocolDescription_Type(DisplayString):
    """Custom type portProtocolDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortProtocolDescription_Type.__name__ = "DisplayString"
_PortProtocolDescription_Object = MibTableColumn
portProtocolDescription = _PortProtocolDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 3),
    _PortProtocolDescription_Type()
)
portProtocolDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portProtocolDescription.setStatus("mandatory")


class _PortSignalCharacteristics_Type(Integer32):
    """Custom type portSignalCharacteristics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("differential", 4),
          ("lowVoltageDifferential", 5),
          ("optical", 6),
          ("other", 1),
          ("singleEnded", 3),
          ("unknown", 2))
    )


_PortSignalCharacteristics_Type.__name__ = "Integer32"
_PortSignalCharacteristics_Object = MibTableColumn
portSignalCharacteristics = _PortSignalCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 4),
    _PortSignalCharacteristics_Type()
)
portSignalCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSignalCharacteristics.setStatus("mandatory")


class _PortAddressDescriptor_Type(DisplayString):
    """Custom type portAddressDescriptor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortAddressDescriptor_Type.__name__ = "DisplayString"
_PortAddressDescriptor_Object = MibTableColumn
portAddressDescriptor = _PortAddressDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 5),
    _PortAddressDescriptor_Type()
)
portAddressDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAddressDescriptor.setStatus("mandatory")


class _PortIsochronous_Type(Integer32):
    """Custom type portIsochronous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PortIsochronous_Type.__name__ = "Integer32"
_PortIsochronous_Object = MibTableColumn
portIsochronous = _PortIsochronous_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 6),
    _PortIsochronous_Type()
)
portIsochronous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIsochronous.setStatus("mandatory")
_PortMaximumWidth_Type = Integer32
_PortMaximumWidth_Object = MibTableColumn
portMaximumWidth = _PortMaximumWidth_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 7),
    _PortMaximumWidth_Type()
)
portMaximumWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMaximumWidth.setStatus("mandatory")
_PortMaximumTransferRate_Type = Integer32
_PortMaximumTransferRate_Object = MibTableColumn
portMaximumTransferRate = _PortMaximumTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 8),
    _PortMaximumTransferRate_Type()
)
portMaximumTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMaximumTransferRate.setStatus("mandatory")
_PortMaximumAttachments_Type = Integer32
_PortMaximumAttachments_Object = MibTableColumn
portMaximumAttachments = _PortMaximumAttachments_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 9),
    _PortMaximumAttachments_Type()
)
portMaximumAttachments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMaximumAttachments.setStatus("mandatory")


class _PortConnectorType_Type(Integer32):
    """Custom type portConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("appleAUI", 33),
          ("ata-2-5inch-44pin", 18),
          ("ata-3-5inch-40pin", 17),
          ("aui", 24),
          ("bnc", 28),
          ("eisaSlot", 36),
          ("fiberMIC", 32),
          ("floppyDiskette3-5inch", 41),
          ("floppyDiskette5-25inch", 40),
          ("gbicSocket", 43),
          ("hssdc-6pin", 42),
          ("ieee488", 23),
          ("isaSlot", 35),
          ("none", 3),
          ("other", 1),
          ("pc-CardSlot", 39),
          ("pciSlot", 34),
          ("pcmciaSlot", 38),
          ("rs232-25pin", 21),
          ("rs422", 22),
          ("scsi-A-HighDensityShielded-50pin", 4),
          ("scsi-A-HighDensityUnshielded-50pin", 5),
          ("scsi-A-LowDensityShielded-50pin", 6),
          ("scsi-A-LowDensityUnshielded-50pin", 7),
          ("scsi-FibreChannel-BNC", 16),
          ("scsi-FibreChannel-DB9-Copper", 12),
          ("scsi-FibreChannel-Fibre", 13),
          ("scsi-FibreChannel-SCA-II-20pin", 15),
          ("scsi-FibreChannel-SCA-II-40pin", 14),
          ("scsi-P-HighDensityShielded-68pin", 8),
          ("scsi-P-HighDensityUnshielded-68pin", 9),
          ("scsi-SCA-I-80pin", 10),
          ("scsi-SCA-II-80pin", 11),
          ("scsi-VHDCIshielded-68pin", 45),
          ("serial-25pin", 20),
          ("serial-9pin", 19),
          ("stp-DB9", 31),
          ("stp-RJ11", 29),
          ("stp-RJ45", 30),
          ("thirteenNinetyFour-6pin", 44),
          ("unknown", 2),
          ("upt-Category3", 25),
          ("upt-Category4", 26),
          ("upt-Category5", 27),
          ("vesaSlot", 37))
    )


_PortConnectorType_Type.__name__ = "Integer32"
_PortConnectorType_Object = MibTableColumn
portConnectorType = _PortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 10),
    _PortConnectorType_Type()
)
portConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConnectorType.setStatus("mandatory")


class _PortConnectorTypeDescription_Type(DisplayString):
    """Custom type portConnectorTypeDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortConnectorTypeDescription_Type.__name__ = "DisplayString"
_PortConnectorTypeDescription_Object = MibTableColumn
portConnectorTypeDescription = _PortConnectorTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 11),
    _PortConnectorTypeDescription_Type()
)
portConnectorTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConnectorTypeDescription.setStatus("mandatory")


class _PortConnectorGender_Type(Integer32):
    """Custom type portConnectorGender based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("female", 3),
          ("male", 4),
          ("other", 1),
          ("unknown", 2))
    )


_PortConnectorGender_Type.__name__ = "Integer32"
_PortConnectorGender_Object = MibTableColumn
portConnectorGender = _PortConnectorGender_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 5, 1, 1, 12),
    _PortConnectorGender_Type()
)
portConnectorGender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConnectorGender.setStatus("mandatory")
_AggregatePhysicalExtent_ObjectIdentity = ObjectIdentity
aggregatePhysicalExtent = _AggregatePhysicalExtent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 6)
)
_AggregatePExtentTable_Object = MibTable
aggregatePExtentTable = _AggregatePExtentTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 6, 1)
)
if mibBuilder.loadTexts:
    aggregatePExtentTable.setStatus("mandatory")
_AggregatePExtentEntry_Object = MibTableRow
aggregatePExtentEntry = _AggregatePExtentEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 6, 1, 1)
)
aggregatePExtentEntry.setIndexNames(
    (0, "CIOMIB", "aggPExtentIndex"),
)
if mibBuilder.loadTexts:
    aggregatePExtentEntry.setStatus("mandatory")
_AggPExtentIndex_Type = Integer32
_AggPExtentIndex_Object = MibTableColumn
aggPExtentIndex = _AggPExtentIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 6, 1, 1, 1),
    _AggPExtentIndex_Type()
)
aggPExtentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggPExtentIndex.setStatus("mandatory")
_AggPExtentBlocks_Type = Integer32
_AggPExtentBlocks_Object = MibTableColumn
aggPExtentBlocks = _AggPExtentBlocks_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 6, 1, 1, 2),
    _AggPExtentBlocks_Type()
)
aggPExtentBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggPExtentBlocks.setStatus("mandatory")
_AggPExtentCheckDataBlocks_Type = Integer32
_AggPExtentCheckDataBlocks_Object = MibTableColumn
aggPExtentCheckDataBlocks = _AggPExtentCheckDataBlocks_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 6, 1, 1, 3),
    _AggPExtentCheckDataBlocks_Type()
)
aggPExtentCheckDataBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggPExtentCheckDataBlocks.setStatus("mandatory")
_AggregateProtectedSpace_ObjectIdentity = ObjectIdentity
aggregateProtectedSpace = _AggregateProtectedSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 7)
)
_AggregatePsExtentTable_Object = MibTable
aggregatePsExtentTable = _AggregatePsExtentTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 7, 1)
)
if mibBuilder.loadTexts:
    aggregatePsExtentTable.setStatus("mandatory")
_AggregatePsExtentEntry_Object = MibTableRow
aggregatePsExtentEntry = _AggregatePsExtentEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 7, 1, 1)
)
aggregatePsExtentEntry.setIndexNames(
    (0, "CIOMIB", "aggPsExtentIndex"),
)
if mibBuilder.loadTexts:
    aggregatePsExtentEntry.setStatus("mandatory")
_AggPsExtentIndex_Type = Integer32
_AggPsExtentIndex_Object = MibTableColumn
aggPsExtentIndex = _AggPsExtentIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 7, 1, 1, 1),
    _AggPsExtentIndex_Type()
)
aggPsExtentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggPsExtentIndex.setStatus("mandatory")
_AggPsExtentBlocks_Type = Integer32
_AggPsExtentBlocks_Object = MibTableColumn
aggPsExtentBlocks = _AggPsExtentBlocks_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 7, 1, 1, 2),
    _AggPsExtentBlocks_Type()
)
aggPsExtentBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggPsExtentBlocks.setStatus("mandatory")
_VolumeSet_ObjectIdentity = ObjectIdentity
volumeSet = _VolumeSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 8)
)
_VolumeSetTable_Object = MibTable
volumeSetTable = _VolumeSetTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 8, 1)
)
if mibBuilder.loadTexts:
    volumeSetTable.setStatus("mandatory")
_VolumeSetEntry_Object = MibTableRow
volumeSetEntry = _VolumeSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 8, 1, 1)
)
volumeSetEntry.setIndexNames(
    (0, "CIOMIB", "volIndex"),
)
if mibBuilder.loadTexts:
    volumeSetEntry.setStatus("mandatory")
_VolIndex_Type = Integer32
_VolIndex_Object = MibTableColumn
volIndex = _VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 8, 1, 1, 1),
    _VolIndex_Type()
)
volIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volIndex.setStatus("mandatory")


class _VolName_Type(DisplayString):
    """Custom type volName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VolName_Type.__name__ = "DisplayString"
_VolName_Object = MibTableColumn
volName = _VolName_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 8, 1, 1, 2),
    _VolName_Type()
)
volName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volName.setStatus("mandatory")
_VolCapacity_Type = Integer32
_VolCapacity_Object = MibTableColumn
volCapacity = _VolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 8, 1, 1, 3),
    _VolCapacity_Type()
)
volCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCapacity.setStatus("mandatory")
_VolPSExtentStripeLength_Type = Integer32
_VolPSExtentStripeLength_Object = MibTableColumn
volPSExtentStripeLength = _VolPSExtentStripeLength_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 8, 1, 1, 4),
    _VolPSExtentStripeLength_Type()
)
volPSExtentStripeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volPSExtentStripeLength.setStatus("mandatory")
_VolPSExtentInterleaveDepth_Type = Integer32
_VolPSExtentInterleaveDepth_Object = MibTableColumn
volPSExtentInterleaveDepth = _VolPSExtentInterleaveDepth_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 8, 1, 1, 5),
    _VolPSExtentInterleaveDepth_Type()
)
volPSExtentInterleaveDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volPSExtentInterleaveDepth.setStatus("mandatory")
_RedundancyGroup_ObjectIdentity = ObjectIdentity
redundancyGroup = _RedundancyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9)
)
_RedundancyGroupTable_Object = MibTable
redundancyGroupTable = _RedundancyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9, 1)
)
if mibBuilder.loadTexts:
    redundancyGroupTable.setStatus("mandatory")
_RedundancyGroupEntry_Object = MibTableRow
redundancyGroupEntry = _RedundancyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9, 1, 1)
)
redundancyGroupEntry.setIndexNames(
    (0, "CIOMIB", "redundancyIndex"),
)
if mibBuilder.loadTexts:
    redundancyGroupEntry.setStatus("mandatory")
_RedundancyIndex_Type = Integer32
_RedundancyIndex_Object = MibTableColumn
redundancyIndex = _RedundancyIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9, 1, 1, 1),
    _RedundancyIndex_Type()
)
redundancyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyIndex.setStatus("mandatory")


class _RedundancyType_Type(Integer32):
    """Custom type redundancyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("copy", 3),
          ("none", 8),
          ("other", 1),
          ("p-q", 5),
          ("p-s", 7),
          ("s", 6),
          ("unknown", 2),
          ("xor", 4))
    )


_RedundancyType_Type.__name__ = "Integer32"
_RedundancyType_Object = MibTableColumn
redundancyType = _RedundancyType_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9, 1, 1, 2),
    _RedundancyType_Type()
)
redundancyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyType.setStatus("mandatory")
_WorldWideIds_ObjectIdentity = ObjectIdentity
worldWideIds = _WorldWideIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 10)
)
_WorldWideIdTable_Object = MibTable
worldWideIdTable = _WorldWideIdTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 10, 1)
)
if mibBuilder.loadTexts:
    worldWideIdTable.setStatus("mandatory")
_WorldWideIdEntry_Object = MibTableRow
worldWideIdEntry = _WorldWideIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 10, 1, 1)
)
worldWideIdEntry.setIndexNames(
    (0, "CIOMIB", "worldWideIdIndex"),
)
if mibBuilder.loadTexts:
    worldWideIdEntry.setStatus("mandatory")
_WorldWideIdIndex_Type = Integer32
_WorldWideIdIndex_Object = MibTableColumn
worldWideIdIndex = _WorldWideIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 10, 1, 1, 1),
    _WorldWideIdIndex_Type()
)
worldWideIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worldWideIdIndex.setStatus("mandatory")


class _WorldWideIdType_Type(Integer32):
    """Custom type worldWideIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("binary", 7),
          ("fc-PH64bitNameIdentifier", 6),
          ("ieeeExtendedUniqueIdentifier64bit", 5),
          ("lanMACAddress", 9),
          ("none", 3),
          ("other", 1),
          ("unicode", 8),
          ("unknown", 2),
          ("vendorProductSerial", 4),
          ("wanAccessAddress", 10))
    )


_WorldWideIdType_Type.__name__ = "Integer32"
_WorldWideIdType_Object = MibTableColumn
worldWideIdType = _WorldWideIdType_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 10, 1, 1, 2),
    _WorldWideIdType_Type()
)
worldWideIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worldWideIdType.setStatus("mandatory")


class _WorldWideId_Type(DisplayString):
    """Custom type worldWideId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WorldWideId_Type.__name__ = "DisplayString"
_WorldWideId_Object = MibTableColumn
worldWideId = _WorldWideId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 10, 1, 1, 3),
    _WorldWideId_Type()
)
worldWideId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    worldWideId.setStatus("mandatory")
_Associations_ObjectIdentity = ObjectIdentity
associations = _Associations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 11)
)
_AssociationTable_Object = MibTable
associationTable = _AssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 11, 1)
)
if mibBuilder.loadTexts:
    associationTable.setStatus("mandatory")
_AssociationEntry_Object = MibTableRow
associationEntry = _AssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 11, 1, 1)
)
associationEntry.setIndexNames(
    (0, "CIOMIB", "associationIndex"),
)
if mibBuilder.loadTexts:
    associationEntry.setStatus("mandatory")
_AssociationIndex_Type = Integer32
_AssociationIndex_Object = MibTableColumn
associationIndex = _AssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 11, 1, 1, 1),
    _AssociationIndex_Type()
)
associationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associationIndex.setStatus("mandatory")


class _AssociationType_Type(DisplayString):
    """Custom type associationType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AssociationType_Type.__name__ = "DisplayString"
_AssociationType_Object = MibTableColumn
associationType = _AssociationType_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 11, 1, 1, 2),
    _AssociationType_Type()
)
associationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associationType.setStatus("mandatory")
_AssociationObject1_Type = ObjectIdentifier
_AssociationObject1_Object = MibTableColumn
associationObject1 = _AssociationObject1_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 11, 1, 1, 3),
    _AssociationObject1_Type()
)
associationObject1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associationObject1.setStatus("mandatory")
_AssociationObject2_Type = ObjectIdentifier
_AssociationObject2_Object = MibTableColumn
associationObject2 = _AssociationObject2_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 11, 1, 1, 4),
    _AssociationObject2_Type()
)
associationObject2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    associationObject2.setStatus("mandatory")
_BusPortAssociations_ObjectIdentity = ObjectIdentity
busPortAssociations = _BusPortAssociations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 12)
)
_BusPortAssociationTable_Object = MibTable
busPortAssociationTable = _BusPortAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 12, 1)
)
if mibBuilder.loadTexts:
    busPortAssociationTable.setStatus("mandatory")
_BusPortAssociationEntry_Object = MibTableRow
busPortAssociationEntry = _BusPortAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 12, 1, 1)
)
busPortAssociationEntry.setIndexNames(
    (0, "CIOMIB", "busPortAssociationIndex"),
)
if mibBuilder.loadTexts:
    busPortAssociationEntry.setStatus("mandatory")
_BusPortAssociationIndex_Type = Integer32
_BusPortAssociationIndex_Object = MibTableColumn
busPortAssociationIndex = _BusPortAssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 12, 1, 1, 1),
    _BusPortAssociationIndex_Type()
)
busPortAssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busPortAssociationIndex.setStatus("mandatory")
_BusPortAssociationNegotiatedSpeed_Type = Integer32
_BusPortAssociationNegotiatedSpeed_Object = MibTableColumn
busPortAssociationNegotiatedSpeed = _BusPortAssociationNegotiatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 12, 1, 1, 2),
    _BusPortAssociationNegotiatedSpeed_Type()
)
busPortAssociationNegotiatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busPortAssociationNegotiatedSpeed.setStatus("mandatory")
_BusPortAssociationNegotiatedWidth_Type = Integer32
_BusPortAssociationNegotiatedWidth_Object = MibTableColumn
busPortAssociationNegotiatedWidth = _BusPortAssociationNegotiatedWidth_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 12, 1, 1, 3),
    _BusPortAssociationNegotiatedWidth_Type()
)
busPortAssociationNegotiatedWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busPortAssociationNegotiatedWidth.setStatus("mandatory")
_ComponentSpareAssociations_ObjectIdentity = ObjectIdentity
componentSpareAssociations = _ComponentSpareAssociations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 13)
)
_ComponentSpareAssociationTable_Object = MibTable
componentSpareAssociationTable = _ComponentSpareAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 13, 1)
)
if mibBuilder.loadTexts:
    componentSpareAssociationTable.setStatus("mandatory")
_ComponentSpareAssociationEntry_Object = MibTableRow
componentSpareAssociationEntry = _ComponentSpareAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 13, 1, 1)
)
componentSpareAssociationEntry.setIndexNames(
    (0, "CIOMIB", "componentSpareAssociationIndex"),
)
if mibBuilder.loadTexts:
    componentSpareAssociationEntry.setStatus("mandatory")
_ComponentSpareAssociationIndex_Type = Integer32
_ComponentSpareAssociationIndex_Object = MibTableColumn
componentSpareAssociationIndex = _ComponentSpareAssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 13, 1, 1, 1),
    _ComponentSpareAssociationIndex_Type()
)
componentSpareAssociationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentSpareAssociationIndex.setStatus("mandatory")


class _ComponentSpareFunctioningState_Type(Integer32):
    """Custom type componentSpareFunctioningState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("activeStandby", 4),
          ("activeStandbyLoadBalances", 5),
          ("inactiveStandby", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ComponentSpareFunctioningState_Type.__name__ = "Integer32"
_ComponentSpareFunctioningState_Object = MibTableColumn
componentSpareFunctioningState = _ComponentSpareFunctioningState_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 13, 1, 1, 2),
    _ComponentSpareFunctioningState_Type()
)
componentSpareFunctioningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentSpareFunctioningState.setStatus("mandatory")
_OverallObjectStatus_ObjectIdentity = ObjectIdentity
overallObjectStatus = _OverallObjectStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 14)
)


class _OverallStatus_Type(Integer32):
    """Custom type overallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("okay", 1),
          ("other", 5),
          ("unknown", 4),
          ("warning", 2))
    )


_OverallStatus_Type.__name__ = "Integer32"
_OverallStatus_Object = MibScalar
overallStatus = _OverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 14, 1),
    _OverallStatus_Type()
)
overallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overallStatus.setStatus("mandatory")
_OperationalStates_ObjectIdentity = ObjectIdentity
operationalStates = _OperationalStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15)
)
_OperationalStateTable_Object = MibTable
operationalStateTable = _OperationalStateTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1)
)
if mibBuilder.loadTexts:
    operationalStateTable.setStatus("mandatory")
_OperationalStateEntry_Object = MibTableRow
operationalStateEntry = _OperationalStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1)
)
operationalStateEntry.setIndexNames(
    (0, "CIOMIB", "operationalStateIndex"),
)
if mibBuilder.loadTexts:
    operationalStateEntry.setStatus("mandatory")
_OperationalStateIndex_Type = Integer32
_OperationalStateIndex_Object = MibTableColumn
operationalStateIndex = _OperationalStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 1),
    _OperationalStateIndex_Type()
)
operationalStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalStateIndex.setStatus("mandatory")
_OperationalDeviceGroupIndex_Type = Integer32
_OperationalDeviceGroupIndex_Object = MibTableColumn
operationalDeviceGroupIndex = _OperationalDeviceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 2),
    _OperationalDeviceGroupIndex_Type()
)
operationalDeviceGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalDeviceGroupIndex.setStatus("mandatory")


class _OperationalStatus_Type(Integer32):
    """Custom type operationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("enabled", 3),
          ("notApplicable", 5),
          ("other", 1),
          ("unknown", 2))
    )


_OperationalStatus_Type.__name__ = "Integer32"
_OperationalStatus_Object = MibTableColumn
operationalStatus = _OperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 3),
    _OperationalStatus_Type()
)
operationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalStatus.setStatus("mandatory")


class _OperationalUsageState_Type(Integer32):
    """Custom type operationalUsageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("busy", 5),
          ("idle", 3),
          ("notApplicable", 6),
          ("other", 1),
          ("unknown", 2))
    )


_OperationalUsageState_Type.__name__ = "Integer32"
_OperationalUsageState_Object = MibTableColumn
operationalUsageState = _OperationalUsageState_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 4),
    _OperationalUsageState_Type()
)
operationalUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalUsageState.setStatus("mandatory")


class _OperationalAvailabilityStatus_Type(Integer32):
    """Custom type operationalAvailabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 10),
          ("inTest", 5),
          ("installError", 12),
          ("notApplicable", 6),
          ("notInstalled", 11),
          ("offDuty", 9),
          ("offLine", 8),
          ("other", 1),
          ("powerOff", 7),
          ("powerSave", 13),
          ("running", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_OperationalAvailabilityStatus_Type.__name__ = "Integer32"
_OperationalAvailabilityStatus_Object = MibTableColumn
operationalAvailabilityStatus = _OperationalAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 5),
    _OperationalAvailabilityStatus_Type()
)
operationalAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalAvailabilityStatus.setStatus("mandatory")


class _OperationalAdministrativeStatus_Type(Integer32):
    """Custom type operationalAdministrativeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("locked", 3),
          ("notApplicable", 5),
          ("other", 1),
          ("shuttingDown", 6),
          ("unknown", 2),
          ("unlocked", 4))
    )


_OperationalAdministrativeStatus_Type.__name__ = "Integer32"
_OperationalAdministrativeStatus_Object = MibTableColumn
operationalAdministrativeStatus = _OperationalAdministrativeStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 6),
    _OperationalAdministrativeStatus_Type()
)
operationalAdministrativeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalAdministrativeStatus.setStatus("mandatory")
_OperationalFatalErrorCount_Type = Integer32
_OperationalFatalErrorCount_Object = MibTableColumn
operationalFatalErrorCount = _OperationalFatalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 7),
    _OperationalFatalErrorCount_Type()
)
operationalFatalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalFatalErrorCount.setStatus("mandatory")
_OperationalMajorErrorCount_Type = Integer32
_OperationalMajorErrorCount_Object = MibTableColumn
operationalMajorErrorCount = _OperationalMajorErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 8),
    _OperationalMajorErrorCount_Type()
)
operationalMajorErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalMajorErrorCount.setStatus("mandatory")
_OperationalWarningErrorCount_Type = Integer32
_OperationalWarningErrorCount_Object = MibTableColumn
operationalWarningErrorCount = _OperationalWarningErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 9),
    _OperationalWarningErrorCount_Type()
)
operationalWarningErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalWarningErrorCount.setStatus("mandatory")


class _OperationalCurrentErrorStatus_Type(Integer32):
    """Custom type operationalCurrentErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("noncritical", 4),
          ("nonrecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_OperationalCurrentErrorStatus_Type.__name__ = "Integer32"
_OperationalCurrentErrorStatus_Object = MibTableColumn
operationalCurrentErrorStatus = _OperationalCurrentErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 10),
    _OperationalCurrentErrorStatus_Type()
)
operationalCurrentErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalCurrentErrorStatus.setStatus("mandatory")


class _OperationalPredictedFailureStatus_Type(Integer32):
    """Custom type operationalPredictedFailureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deviceFailurePredicted", 5),
          ("mediaFailurePredicted", 6),
          ("noFailurePredicted", 4),
          ("notSupported", 3),
          ("other", 1),
          ("unknown", 2))
    )


_OperationalPredictedFailureStatus_Type.__name__ = "Integer32"
_OperationalPredictedFailureStatus_Object = MibTableColumn
operationalPredictedFailureStatus = _OperationalPredictedFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 15, 1, 1, 11),
    _OperationalPredictedFailureStatus_Type()
)
operationalPredictedFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalPredictedFailureStatus.setStatus("mandatory")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16)
)
_StatisticsTable_Object = MibTable
statisticsTable = _StatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1)
)
if mibBuilder.loadTexts:
    statisticsTable.setStatus("mandatory")
_StatisticsEntry_Object = MibTableRow
statisticsEntry = _StatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1)
)
statisticsEntry.setIndexNames(
    (0, "CIOMIB", "statisticsIndex"),
)
if mibBuilder.loadTexts:
    statisticsEntry.setStatus("mandatory")
_StatisticsIndex_Type = Integer32
_StatisticsIndex_Object = MibTableColumn
statisticsIndex = _StatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 1),
    _StatisticsIndex_Type()
)
statisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsIndex.setStatus("mandatory")
_StatisticsBlocksRead_Type = Integer32
_StatisticsBlocksRead_Object = MibTableColumn
statisticsBlocksRead = _StatisticsBlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 2),
    _StatisticsBlocksRead_Type()
)
statisticsBlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsBlocksRead.setStatus("mandatory")
_StatisticsBlocksWritten_Type = Integer32
_StatisticsBlocksWritten_Object = MibTableColumn
statisticsBlocksWritten = _StatisticsBlocksWritten_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 3),
    _StatisticsBlocksWritten_Type()
)
statisticsBlocksWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsBlocksWritten.setStatus("mandatory")
_StatisticsReadCommands_Type = Integer32
_StatisticsReadCommands_Object = MibTableColumn
statisticsReadCommands = _StatisticsReadCommands_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 4),
    _StatisticsReadCommands_Type()
)
statisticsReadCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadCommands.setStatus("mandatory")
_StatisticsWriteCommands_Type = Integer32
_StatisticsWriteCommands_Object = MibTableColumn
statisticsWriteCommands = _StatisticsWriteCommands_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 5),
    _StatisticsWriteCommands_Type()
)
statisticsWriteCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteCommands.setStatus("mandatory")
_StatisticsReadBucket0_Type = Integer32
_StatisticsReadBucket0_Object = MibTableColumn
statisticsReadBucket0 = _StatisticsReadBucket0_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 6),
    _StatisticsReadBucket0_Type()
)
statisticsReadBucket0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket0.setStatus("mandatory")
_StatisticsReadBucket1_Type = Integer32
_StatisticsReadBucket1_Object = MibTableColumn
statisticsReadBucket1 = _StatisticsReadBucket1_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 7),
    _StatisticsReadBucket1_Type()
)
statisticsReadBucket1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket1.setStatus("mandatory")
_StatisticsReadBucket2_Type = Integer32
_StatisticsReadBucket2_Object = MibTableColumn
statisticsReadBucket2 = _StatisticsReadBucket2_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 8),
    _StatisticsReadBucket2_Type()
)
statisticsReadBucket2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket2.setStatus("mandatory")
_StatisticsReadBucket3_Type = Integer32
_StatisticsReadBucket3_Object = MibTableColumn
statisticsReadBucket3 = _StatisticsReadBucket3_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 9),
    _StatisticsReadBucket3_Type()
)
statisticsReadBucket3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket3.setStatus("mandatory")
_StatisticsReadBucket4_Type = Integer32
_StatisticsReadBucket4_Object = MibTableColumn
statisticsReadBucket4 = _StatisticsReadBucket4_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 10),
    _StatisticsReadBucket4_Type()
)
statisticsReadBucket4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket4.setStatus("mandatory")
_StatisticsReadBucket5_Type = Integer32
_StatisticsReadBucket5_Object = MibTableColumn
statisticsReadBucket5 = _StatisticsReadBucket5_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 11),
    _StatisticsReadBucket5_Type()
)
statisticsReadBucket5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket5.setStatus("mandatory")
_StatisticsReadBucket6_Type = Integer32
_StatisticsReadBucket6_Object = MibTableColumn
statisticsReadBucket6 = _StatisticsReadBucket6_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 12),
    _StatisticsReadBucket6_Type()
)
statisticsReadBucket6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket6.setStatus("mandatory")
_StatisticsReadBucket7_Type = Integer32
_StatisticsReadBucket7_Object = MibTableColumn
statisticsReadBucket7 = _StatisticsReadBucket7_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 13),
    _StatisticsReadBucket7_Type()
)
statisticsReadBucket7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket7.setStatus("mandatory")
_StatisticsReadBucket8_Type = Integer32
_StatisticsReadBucket8_Object = MibTableColumn
statisticsReadBucket8 = _StatisticsReadBucket8_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 14),
    _StatisticsReadBucket8_Type()
)
statisticsReadBucket8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket8.setStatus("mandatory")
_StatisticsReadBucket9_Type = Integer32
_StatisticsReadBucket9_Object = MibTableColumn
statisticsReadBucket9 = _StatisticsReadBucket9_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 15),
    _StatisticsReadBucket9_Type()
)
statisticsReadBucket9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket9.setStatus("mandatory")
_StatisticsReadBucket10_Type = Integer32
_StatisticsReadBucket10_Object = MibTableColumn
statisticsReadBucket10 = _StatisticsReadBucket10_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 16),
    _StatisticsReadBucket10_Type()
)
statisticsReadBucket10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket10.setStatus("mandatory")
_StatisticsReadBucket11_Type = Integer32
_StatisticsReadBucket11_Object = MibTableColumn
statisticsReadBucket11 = _StatisticsReadBucket11_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 17),
    _StatisticsReadBucket11_Type()
)
statisticsReadBucket11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket11.setStatus("mandatory")
_StatisticsReadBucket12_Type = Integer32
_StatisticsReadBucket12_Object = MibTableColumn
statisticsReadBucket12 = _StatisticsReadBucket12_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 18),
    _StatisticsReadBucket12_Type()
)
statisticsReadBucket12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsReadBucket12.setStatus("mandatory")
_StatisticsWriteBucket0_Type = Integer32
_StatisticsWriteBucket0_Object = MibTableColumn
statisticsWriteBucket0 = _StatisticsWriteBucket0_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 19),
    _StatisticsWriteBucket0_Type()
)
statisticsWriteBucket0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket0.setStatus("mandatory")
_StatisticsWriteBucket1_Type = Integer32
_StatisticsWriteBucket1_Object = MibTableColumn
statisticsWriteBucket1 = _StatisticsWriteBucket1_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 20),
    _StatisticsWriteBucket1_Type()
)
statisticsWriteBucket1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket1.setStatus("mandatory")
_StatisticsWriteBucket2_Type = Integer32
_StatisticsWriteBucket2_Object = MibTableColumn
statisticsWriteBucket2 = _StatisticsWriteBucket2_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 21),
    _StatisticsWriteBucket2_Type()
)
statisticsWriteBucket2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket2.setStatus("mandatory")
_StatisticsWriteBucket3_Type = Integer32
_StatisticsWriteBucket3_Object = MibTableColumn
statisticsWriteBucket3 = _StatisticsWriteBucket3_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 22),
    _StatisticsWriteBucket3_Type()
)
statisticsWriteBucket3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket3.setStatus("mandatory")
_StatisticsWriteBucket4_Type = Integer32
_StatisticsWriteBucket4_Object = MibTableColumn
statisticsWriteBucket4 = _StatisticsWriteBucket4_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 23),
    _StatisticsWriteBucket4_Type()
)
statisticsWriteBucket4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket4.setStatus("mandatory")
_StatisticsWriteBucket5_Type = Integer32
_StatisticsWriteBucket5_Object = MibTableColumn
statisticsWriteBucket5 = _StatisticsWriteBucket5_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 24),
    _StatisticsWriteBucket5_Type()
)
statisticsWriteBucket5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket5.setStatus("mandatory")
_StatisticsWriteBucket6_Type = Integer32
_StatisticsWriteBucket6_Object = MibTableColumn
statisticsWriteBucket6 = _StatisticsWriteBucket6_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 25),
    _StatisticsWriteBucket6_Type()
)
statisticsWriteBucket6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket6.setStatus("mandatory")
_StatisticsWriteBucket7_Type = Integer32
_StatisticsWriteBucket7_Object = MibTableColumn
statisticsWriteBucket7 = _StatisticsWriteBucket7_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 26),
    _StatisticsWriteBucket7_Type()
)
statisticsWriteBucket7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket7.setStatus("mandatory")
_StatisticsWriteBucket8_Type = Integer32
_StatisticsWriteBucket8_Object = MibTableColumn
statisticsWriteBucket8 = _StatisticsWriteBucket8_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 27),
    _StatisticsWriteBucket8_Type()
)
statisticsWriteBucket8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket8.setStatus("mandatory")
_StatisticsWriteBucket9_Type = Integer32
_StatisticsWriteBucket9_Object = MibTableColumn
statisticsWriteBucket9 = _StatisticsWriteBucket9_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 28),
    _StatisticsWriteBucket9_Type()
)
statisticsWriteBucket9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket9.setStatus("mandatory")
_StatisticsWriteBucket10_Type = Integer32
_StatisticsWriteBucket10_Object = MibTableColumn
statisticsWriteBucket10 = _StatisticsWriteBucket10_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 29),
    _StatisticsWriteBucket10_Type()
)
statisticsWriteBucket10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket10.setStatus("mandatory")
_StatisticsWriteBucket11_Type = Integer32
_StatisticsWriteBucket11_Object = MibTableColumn
statisticsWriteBucket11 = _StatisticsWriteBucket11_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 30),
    _StatisticsWriteBucket11_Type()
)
statisticsWriteBucket11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket11.setStatus("mandatory")
_StatisticsWriteBucket12_Type = Integer32
_StatisticsWriteBucket12_Object = MibTableColumn
statisticsWriteBucket12 = _StatisticsWriteBucket12_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 16, 1, 1, 31),
    _StatisticsWriteBucket12_Type()
)
statisticsWriteBucket12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statisticsWriteBucket12.setStatus("mandatory")
_TrapLogCount_ObjectIdentity = ObjectIdentity
trapLogCount = _TrapLogCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 17)
)
_TrapLogNumEntries_Type = Integer32
_TrapLogNumEntries_Object = MibScalar
trapLogNumEntries = _TrapLogNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 17, 1),
    _TrapLogNumEntries_Type()
)
trapLogNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogNumEntries.setStatus("mandatory")
_TrapLog_ObjectIdentity = ObjectIdentity
trapLog = _TrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 18)
)
_TrapLogTable_Object = MibTable
trapLogTable = _TrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 18, 1)
)
if mibBuilder.loadTexts:
    trapLogTable.setStatus("mandatory")
_TrapLogEntry_Object = MibTableRow
trapLogEntry = _TrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 18, 1, 1)
)
trapLogEntry.setIndexNames(
    (0, "CIOMIB", "trapLogIndex"),
)
if mibBuilder.loadTexts:
    trapLogEntry.setStatus("mandatory")
_TrapLogIndex_Type = Integer32
_TrapLogIndex_Object = MibTableColumn
trapLogIndex = _TrapLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 18, 1, 1, 1),
    _TrapLogIndex_Type()
)
trapLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogIndex.setStatus("mandatory")


class _TrapLogString_Type(DisplayString):
    """Custom type trapLogString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapLogString_Type.__name__ = "DisplayString"
_TrapLogString_Object = MibTableColumn
trapLogString = _TrapLogString_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 18, 1, 1, 2),
    _TrapLogString_Type()
)
trapLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogString.setStatus("mandatory")
_TrapLogTimeStamp_Type = Integer32
_TrapLogTimeStamp_Object = MibTableColumn
trapLogTimeStamp = _TrapLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 18, 1, 1, 3),
    _TrapLogTimeStamp_Type()
)
trapLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogTimeStamp.setStatus("mandatory")
_CycTraps_ObjectIdentity = ObjectIdentity
cycTraps = _CycTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000)
)


class _CycSeverity_Type(Integer32):
    """Custom type cycSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("informational", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_CycSeverity_Type.__name__ = "Integer32"
_CycSeverity_Object = MibScalar
cycSeverity = _CycSeverity_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9001),
    _CycSeverity_Type()
)
cycSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycSeverity.setStatus("mandatory")
_CycObject_Type = ObjectIdentifier
_CycObject_Object = MibScalar
cycObject = _CycObject_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9002),
    _CycObject_Type()
)
cycObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycObject.setStatus("mandatory")


class _CycPhysicalObjectState_Type(Integer32):
    """Custom type cycPhysicalObjectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("batteryChangedGoodToLow", 13),
          ("batteryChangedGoodToReconditioning", 16),
          ("batteryChangedLowToGood", 14),
          ("batteryChangedLowToReconditioning", 15),
          ("batteryChangedReconditioningToGood", 18),
          ("batteryChangedReconditioningToLow", 17),
          ("batteryCurrentTooHigh", 33),
          ("batteryDead", 30),
          ("batteryFailedCharge", 31),
          ("batteryMissing", 36),
          ("batteryOkay", 29),
          ("batteryOvercharged", 32),
          ("batteryReconditionCompleted", 19),
          ("batteryReconditionScheduled", 11),
          ("batteryReconditionStarted", 20),
          ("batteryShortCircuit", 37),
          ("batteryTemperatureTooHigh", 34),
          ("batteryVoltageTooLow", 35),
          ("cacheOff", 9),
          ("cacheOn", 8),
          ("cacheParametersChanged", 7),
          ("changed", 4),
          ("deleted", 10),
          ("failed", 2),
          ("initializeAbortedByUser", 24),
          ("initializeCompleted", 22),
          ("initializeFailed", 23),
          ("initializeStarted", 21),
          ("newlyDiscovered", 1),
          ("recovered", 3),
          ("scheduledBatteryReconditionDeleted", 12),
          ("selfMonitoringEnabled", 6),
          ("selfMonitoringWarning", 5),
          ("verifyAbortedByUser", 28),
          ("verifyCompleted", 26),
          ("verifyFailed", 27),
          ("verifyStarted", 25))
    )


_CycPhysicalObjectState_Type.__name__ = "Integer32"
_CycPhysicalObjectState_Object = MibScalar
cycPhysicalObjectState = _CycPhysicalObjectState_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9003),
    _CycPhysicalObjectState_Type()
)
cycPhysicalObjectState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycPhysicalObjectState.setStatus("mandatory")


class _CycVolumeSetState_Type(Integer32):
    """Custom type cycVolumeSetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("arrayAdded", 25),
          ("arrayDeleted", 26),
          ("badBlockRepaired", 2),
          ("cacheAllocationFailed", 24),
          ("cacheFlushFailed", 23),
          ("cacheOff", 22),
          ("cacheOn", 21),
          ("cacheParametersChanged", 20),
          ("criticalState", 6),
          ("dedicatedSpareAdded", 13),
          ("dedicatedSpareDeleted", 12),
          ("dedicatedSpareUsed", 16),
          ("lastSpareDeleted", 19),
          ("lastSpareUsed", 18),
          ("memberMissing", 11),
          ("nameChanged", 28),
          ("offline", 3),
          ("offlineMemberFailed", 4),
          ("online", 5),
          ("poolSpareAdded", 15),
          ("poolSpareDeleted", 14),
          ("poolSpareUsed", 17),
          ("protectionDisabled", 7),
          ("protectionEnabled", 8),
          ("scsiAddressesChangedForMembers", 27),
          ("selfMonitoringEnabled", 10),
          ("selfMonitoringWarning", 9),
          ("unsafeShutdown", 1))
    )


_CycVolumeSetState_Type.__name__ = "Integer32"
_CycVolumeSetState_Object = MibScalar
cycVolumeSetState = _CycVolumeSetState_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9004),
    _CycVolumeSetState_Type()
)
cycVolumeSetState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycVolumeSetState.setStatus("mandatory")


class _CycVolumeSetActivity_Type(Integer32):
    """Custom type cycVolumeSetActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("expansion", 12),
          ("initialize", 2),
          ("migration", 11),
          ("mirrorBreak", 9),
          ("mirrorCreate", 10),
          ("reconstruct", 1),
          ("scheduledInitialize", 6),
          ("scheduledReconstruct", 5),
          ("scheduledSpareTest", 8),
          ("scheduledVerify", 7),
          ("spareTest", 4),
          ("verify", 3))
    )


_CycVolumeSetActivity_Type.__name__ = "Integer32"
_CycVolumeSetActivity_Object = MibScalar
cycVolumeSetActivity = _CycVolumeSetActivity_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9005),
    _CycVolumeSetActivity_Type()
)
cycVolumeSetActivity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycVolumeSetActivity.setStatus("mandatory")


class _CycVolumeSetActivityState_Type(Integer32):
    """Custom type cycVolumeSetActivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 21),
          ("abortedByOperator", 7),
          ("abortedByOperatorWithMiscompares", 8),
          ("abortedDueToIOError", 5),
          ("abortedDueToIOErrorWithMiscompares", 6),
          ("abortedNoMemory", 15),
          ("completed", 3),
          ("completedWithMiscompares", 4),
          ("deleted", 10),
          ("failed", 9),
          ("failedToStart", 14),
          ("modified", 13),
          ("priorityChanged", 11),
          ("restarted", 16),
          ("resumed", 18),
          ("running", 20),
          ("scheduled", 12),
          ("started", 1),
          ("startedAutofix", 2),
          ("stopped", 19),
          ("suspended", 17))
    )


_CycVolumeSetActivityState_Type.__name__ = "Integer32"
_CycVolumeSetActivityState_Object = MibScalar
cycVolumeSetActivityState = _CycVolumeSetActivityState_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9006),
    _CycVolumeSetActivityState_Type()
)
cycVolumeSetActivityState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycVolumeSetActivityState.setStatus("mandatory")


class _CycSpareState_Type(Integer32):
    """Custom type cycSpareState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notFunctional", 2),
          ("ok", 1))
    )


_CycSpareState_Type.__name__ = "Integer32"
_CycSpareState_Object = MibScalar
cycSpareState = _CycSpareState_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9007),
    _CycSpareState_Type()
)
cycSpareState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycSpareState.setStatus("mandatory")


class _CycEnclosureComponent_Type(Integer32):
    """Custom type cycEnclosureComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cabinet", 1),
          ("deviceInSlot", 7),
          ("door", 4),
          ("fan", 2),
          ("powerSupply", 3),
          ("speaker", 5),
          ("temperatureSensor", 6))
    )


_CycEnclosureComponent_Type.__name__ = "Integer32"
_CycEnclosureComponent_Object = MibScalar
cycEnclosureComponent = _CycEnclosureComponent_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9008),
    _CycEnclosureComponent_Type()
)
cycEnclosureComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycEnclosureComponent.setStatus("mandatory")
_CycEnclosureComponentNumber_Type = Integer32
_CycEnclosureComponentNumber_Object = MibScalar
cycEnclosureComponentNumber = _CycEnclosureComponentNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9009),
    _CycEnclosureComponentNumber_Type()
)
cycEnclosureComponentNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycEnclosureComponentNumber.setStatus("mandatory")


class _CycEnclosureComponentState_Type(Integer32):
    """Custom type cycEnclosureComponentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("decreaseToHalfCapacityFailed", 20),
          ("found", 1),
          ("inNormalRange", 17),
          ("increaseToMaximumCapacityFailed", 21),
          ("inserted", 6),
          ("locked", 14),
          ("malfunctioning", 4),
          ("malfunctioningAndOff", 11),
          ("malfunctioningButOn", 10),
          ("notPresent", 12),
          ("notResponding", 2),
          ("operational", 3),
          ("operationalAndOff", 9),
          ("operationalAndOn", 8),
          ("outOfNormalRange", 16),
          ("present", 13),
          ("removed", 5),
          ("runningAtHalfCapacity", 18),
          ("runningAtMaximumCapacity", 19),
          ("unknownState", 7),
          ("unlocked", 15))
    )


_CycEnclosureComponentState_Type.__name__ = "Integer32"
_CycEnclosureComponentState_Object = MibScalar
cycEnclosureComponentState = _CycEnclosureComponentState_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 9000, 9010),
    _CycEnclosureComponentState_Type()
)
cycEnclosureComponentState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cycEnclosureComponentState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cycStorageControllerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 0, 101)
)
cycStorageControllerStateChange.setObjects(
      *(("CIOMIB", "cycSeverity"),
        ("CIOMIB", "cycObject"),
        ("CIOMIB", "cycPhysicalObjectState"))
)
if mibBuilder.loadTexts:
    cycStorageControllerStateChange.setStatus(
        ""
    )

cycBusPortStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 0, 102)
)
cycBusPortStateChange.setObjects(
      *(("CIOMIB", "cycSeverity"),
        ("CIOMIB", "cycObject"),
        ("CIOMIB", "cycPhysicalObjectState"))
)
if mibBuilder.loadTexts:
    cycBusPortStateChange.setStatus(
        ""
    )

cycStorageDeviceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 0, 103)
)
cycStorageDeviceStateChange.setObjects(
      *(("CIOMIB", "cycSeverity"),
        ("CIOMIB", "cycObject"),
        ("CIOMIB", "cycPhysicalObjectState"))
)
if mibBuilder.loadTexts:
    cycStorageDeviceStateChange.setStatus(
        ""
    )

cycVolumeSetStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 0, 104)
)
cycVolumeSetStateChange.setObjects(
      *(("CIOMIB", "cycSeverity"),
        ("CIOMIB", "cycObject"),
        ("CIOMIB", "cycVolumeSetState"))
)
if mibBuilder.loadTexts:
    cycVolumeSetStateChange.setStatus(
        ""
    )

cycVolumeSetActivityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 0, 105)
)
cycVolumeSetActivityChange.setObjects(
      *(("CIOMIB", "cycSeverity"),
        ("CIOMIB", "cycObject"),
        ("CIOMIB", "cycVolumeSetActivity"),
        ("CIOMIB", "cycVolumeSetActivityState"))
)
if mibBuilder.loadTexts:
    cycVolumeSetActivityChange.setStatus(
        ""
    )

cycSpareStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 0, 106)
)
cycSpareStateChange.setObjects(
      *(("CIOMIB", "cycSeverity"),
        ("CIOMIB", "cycObject"),
        ("CIOMIB", "cycSpareState"))
)
if mibBuilder.loadTexts:
    cycSpareStateChange.setStatus(
        ""
    )

cycEnclosureStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 12, 0, 107)
)
cycEnclosureStateChange.setObjects(
      *(("CIOMIB", "cycSeverity"),
        ("CIOMIB", "cycObject"),
        ("CIOMIB", "cycEnclosureComponent"),
        ("CIOMIB", "cycEnclosureComponentNumber"),
        ("CIOMIB", "cycEnclosureComponentState"))
)
if mibBuilder.loadTexts:
    cycEnclosureStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIOMIB",
    **{"adaptec": adaptec,
       "storagemanagement": storagemanagement,
       "cio2": cio2,
       "cycStorageControllerStateChange": cycStorageControllerStateChange,
       "cycBusPortStateChange": cycBusPortStateChange,
       "cycStorageDeviceStateChange": cycStorageDeviceStateChange,
       "cycVolumeSetStateChange": cycVolumeSetStateChange,
       "cycVolumeSetActivityChange": cycVolumeSetActivityChange,
       "cycSpareStateChange": cycSpareStateChange,
       "cycEnclosureStateChange": cycEnclosureStateChange,
       "mibRevision": mibRevision,
       "revMajor": revMajor,
       "revMinor": revMinor,
       "storageDevice": storageDevice,
       "deviceTable": deviceTable,
       "devEntry": devEntry,
       "devIndex": devIndex,
       "devType": devType,
       "devTypeDescr": devTypeDescr,
       "devSubIdentifier": devSubIdentifier,
       "devMediaBlockSize": devMediaBlockSize,
       "devFormattedMediaCapacity": devFormattedMediaCapacity,
       "devRemovableDevice": devRemovableDevice,
       "devLoaded": devLoaded,
       "devRemovableMedia": devRemovableMedia,
       "devMediaLoaded": devMediaLoaded,
       "devCompression": devCompression,
       "devEncryption": devEncryption,
       "storageController": storageController,
       "ctlrTable": ctlrTable,
       "ctlrEntry": ctlrEntry,
       "ctlrIndex": ctlrIndex,
       "ctlrDescription": ctlrDescription,
       "ctlrProtectionManagement": ctlrProtectionManagement,
       "ctlrBusMaster": ctlrBusMaster,
       "ctlrSecondsSinceLastPowerUp": ctlrSecondsSinceLastPowerUp,
       "enclosure": enclosure,
       "enclTable": enclTable,
       "enclEntry": enclEntry,
       "enclIndex": enclIndex,
       "enclType": enclType,
       "enclDescription": enclDescription,
       "busPort": busPort,
       "busPortTable": busPortTable,
       "busPortEntry": busPortEntry,
       "portIndex": portIndex,
       "portProtocol": portProtocol,
       "portProtocolDescription": portProtocolDescription,
       "portSignalCharacteristics": portSignalCharacteristics,
       "portAddressDescriptor": portAddressDescriptor,
       "portIsochronous": portIsochronous,
       "portMaximumWidth": portMaximumWidth,
       "portMaximumTransferRate": portMaximumTransferRate,
       "portMaximumAttachments": portMaximumAttachments,
       "portConnectorType": portConnectorType,
       "portConnectorTypeDescription": portConnectorTypeDescription,
       "portConnectorGender": portConnectorGender,
       "aggregatePhysicalExtent": aggregatePhysicalExtent,
       "aggregatePExtentTable": aggregatePExtentTable,
       "aggregatePExtentEntry": aggregatePExtentEntry,
       "aggPExtentIndex": aggPExtentIndex,
       "aggPExtentBlocks": aggPExtentBlocks,
       "aggPExtentCheckDataBlocks": aggPExtentCheckDataBlocks,
       "aggregateProtectedSpace": aggregateProtectedSpace,
       "aggregatePsExtentTable": aggregatePsExtentTable,
       "aggregatePsExtentEntry": aggregatePsExtentEntry,
       "aggPsExtentIndex": aggPsExtentIndex,
       "aggPsExtentBlocks": aggPsExtentBlocks,
       "volumeSet": volumeSet,
       "volumeSetTable": volumeSetTable,
       "volumeSetEntry": volumeSetEntry,
       "volIndex": volIndex,
       "volName": volName,
       "volCapacity": volCapacity,
       "volPSExtentStripeLength": volPSExtentStripeLength,
       "volPSExtentInterleaveDepth": volPSExtentInterleaveDepth,
       "redundancyGroup": redundancyGroup,
       "redundancyGroupTable": redundancyGroupTable,
       "redundancyGroupEntry": redundancyGroupEntry,
       "redundancyIndex": redundancyIndex,
       "redundancyType": redundancyType,
       "worldWideIds": worldWideIds,
       "worldWideIdTable": worldWideIdTable,
       "worldWideIdEntry": worldWideIdEntry,
       "worldWideIdIndex": worldWideIdIndex,
       "worldWideIdType": worldWideIdType,
       "worldWideId": worldWideId,
       "associations": associations,
       "associationTable": associationTable,
       "associationEntry": associationEntry,
       "associationIndex": associationIndex,
       "associationType": associationType,
       "associationObject1": associationObject1,
       "associationObject2": associationObject2,
       "busPortAssociations": busPortAssociations,
       "busPortAssociationTable": busPortAssociationTable,
       "busPortAssociationEntry": busPortAssociationEntry,
       "busPortAssociationIndex": busPortAssociationIndex,
       "busPortAssociationNegotiatedSpeed": busPortAssociationNegotiatedSpeed,
       "busPortAssociationNegotiatedWidth": busPortAssociationNegotiatedWidth,
       "componentSpareAssociations": componentSpareAssociations,
       "componentSpareAssociationTable": componentSpareAssociationTable,
       "componentSpareAssociationEntry": componentSpareAssociationEntry,
       "componentSpareAssociationIndex": componentSpareAssociationIndex,
       "componentSpareFunctioningState": componentSpareFunctioningState,
       "overallObjectStatus": overallObjectStatus,
       "overallStatus": overallStatus,
       "operationalStates": operationalStates,
       "operationalStateTable": operationalStateTable,
       "operationalStateEntry": operationalStateEntry,
       "operationalStateIndex": operationalStateIndex,
       "operationalDeviceGroupIndex": operationalDeviceGroupIndex,
       "operationalStatus": operationalStatus,
       "operationalUsageState": operationalUsageState,
       "operationalAvailabilityStatus": operationalAvailabilityStatus,
       "operationalAdministrativeStatus": operationalAdministrativeStatus,
       "operationalFatalErrorCount": operationalFatalErrorCount,
       "operationalMajorErrorCount": operationalMajorErrorCount,
       "operationalWarningErrorCount": operationalWarningErrorCount,
       "operationalCurrentErrorStatus": operationalCurrentErrorStatus,
       "operationalPredictedFailureStatus": operationalPredictedFailureStatus,
       "statistics": statistics,
       "statisticsTable": statisticsTable,
       "statisticsEntry": statisticsEntry,
       "statisticsIndex": statisticsIndex,
       "statisticsBlocksRead": statisticsBlocksRead,
       "statisticsBlocksWritten": statisticsBlocksWritten,
       "statisticsReadCommands": statisticsReadCommands,
       "statisticsWriteCommands": statisticsWriteCommands,
       "statisticsReadBucket0": statisticsReadBucket0,
       "statisticsReadBucket1": statisticsReadBucket1,
       "statisticsReadBucket2": statisticsReadBucket2,
       "statisticsReadBucket3": statisticsReadBucket3,
       "statisticsReadBucket4": statisticsReadBucket4,
       "statisticsReadBucket5": statisticsReadBucket5,
       "statisticsReadBucket6": statisticsReadBucket6,
       "statisticsReadBucket7": statisticsReadBucket7,
       "statisticsReadBucket8": statisticsReadBucket8,
       "statisticsReadBucket9": statisticsReadBucket9,
       "statisticsReadBucket10": statisticsReadBucket10,
       "statisticsReadBucket11": statisticsReadBucket11,
       "statisticsReadBucket12": statisticsReadBucket12,
       "statisticsWriteBucket0": statisticsWriteBucket0,
       "statisticsWriteBucket1": statisticsWriteBucket1,
       "statisticsWriteBucket2": statisticsWriteBucket2,
       "statisticsWriteBucket3": statisticsWriteBucket3,
       "statisticsWriteBucket4": statisticsWriteBucket4,
       "statisticsWriteBucket5": statisticsWriteBucket5,
       "statisticsWriteBucket6": statisticsWriteBucket6,
       "statisticsWriteBucket7": statisticsWriteBucket7,
       "statisticsWriteBucket8": statisticsWriteBucket8,
       "statisticsWriteBucket9": statisticsWriteBucket9,
       "statisticsWriteBucket10": statisticsWriteBucket10,
       "statisticsWriteBucket11": statisticsWriteBucket11,
       "statisticsWriteBucket12": statisticsWriteBucket12,
       "trapLogCount": trapLogCount,
       "trapLogNumEntries": trapLogNumEntries,
       "trapLog": trapLog,
       "trapLogTable": trapLogTable,
       "trapLogEntry": trapLogEntry,
       "trapLogIndex": trapLogIndex,
       "trapLogString": trapLogString,
       "trapLogTimeStamp": trapLogTimeStamp,
       "cycTraps": cycTraps,
       "cycSeverity": cycSeverity,
       "cycObject": cycObject,
       "cycPhysicalObjectState": cycPhysicalObjectState,
       "cycVolumeSetState": cycVolumeSetState,
       "cycVolumeSetActivity": cycVolumeSetActivity,
       "cycVolumeSetActivityState": cycVolumeSetActivityState,
       "cycSpareState": cycSpareState,
       "cycEnclosureComponent": cycEnclosureComponent,
       "cycEnclosureComponentNumber": cycEnclosureComponentNumber,
       "cycEnclosureComponentState": cycEnclosureComponentState}
)
