# SNMP MIB module (ADAPTECSCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADAPTECSCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:44 2024
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



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adaptec_ObjectIdentity = ObjectIdentity
adaptec = _Adaptec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2)
)
_Scsi_ObjectIdentity = ObjectIdentity
scsi = _Scsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 6)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "ADAPTECSCSI-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDisplaystring
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("vAnErrorOccurredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vTheVerificationIsNotSupported", 2),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TOperationGroup_Object = MibTable
tOperationGroup = _TOperationGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    tOperationGroup.setStatus("mandatory")
_EOperationGroup_Object = MibTableRow
eOperationGroup = _EOperationGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 2, 1)
)
eOperationGroup.setIndexNames(
    (0, "ADAPTECSCSI-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eOperationGroup.setStatus("mandatory")
_A2PollDevices_Type = DmiInteger
_A2PollDevices_Object = MibTableColumn
a2PollDevices = _A2PollDevices_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 2, 1, 1),
    _A2PollDevices_Type()
)
a2PollDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2PollDevices.setStatus("mandatory")
_A2ScanDevices_Type = DmiInteger
_A2ScanDevices_Object = MibTableColumn
a2ScanDevices = _A2ScanDevices_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 2, 1, 2),
    _A2ScanDevices_Type()
)
a2ScanDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2ScanDevices.setStatus("mandatory")


class _A2IndicationControl_Type(Integer32):
    """Custom type a2IndicationControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A2IndicationControl_Type.__name__ = "Integer32"
_A2IndicationControl_Object = MibTableColumn
a2IndicationControl = _A2IndicationControl_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 2, 1, 3),
    _A2IndicationControl_Type()
)
a2IndicationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2IndicationControl.setStatus("mandatory")
_THostAdapterGroup_Object = MibTable
tHostAdapterGroup = _THostAdapterGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 3)
)
if mibBuilder.loadTexts:
    tHostAdapterGroup.setStatus("mandatory")
_EHostAdapterGroup_Object = MibTableRow
eHostAdapterGroup = _EHostAdapterGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 3, 1)
)
eHostAdapterGroup.setIndexNames(
    (0, "ADAPTECSCSI-MIB", "DmiComponentIndex"),
    (0, "ADAPTECSCSI-MIB", "a3HostAdapterIndex"),
)
if mibBuilder.loadTexts:
    eHostAdapterGroup.setStatus("mandatory")
_A3HostAdapterIndex_Type = DmiInteger
_A3HostAdapterIndex_Object = MibTableColumn
a3HostAdapterIndex = _A3HostAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 3, 1, 1),
    _A3HostAdapterIndex_Type()
)
a3HostAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3HostAdapterIndex.setStatus("mandatory")
_A3HostAdapterDescription_Type = DmiDisplaystring
_A3HostAdapterDescription_Object = MibTableColumn
a3HostAdapterDescription = _A3HostAdapterDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 3, 1, 2),
    _A3HostAdapterDescription_Type()
)
a3HostAdapterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3HostAdapterDescription.setStatus("mandatory")
_A3HostAdapterVersion_Type = DmiDisplaystring
_A3HostAdapterVersion_Object = MibTableColumn
a3HostAdapterVersion = _A3HostAdapterVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 3, 1, 3),
    _A3HostAdapterVersion_Type()
)
a3HostAdapterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3HostAdapterVersion.setStatus("mandatory")
_A3ChannelCount_Type = DmiInteger
_A3ChannelCount_Object = MibTableColumn
a3ChannelCount = _A3ChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 3, 1, 4),
    _A3ChannelCount_Type()
)
a3ChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ChannelCount.setStatus("mandatory")
_A3Errorcontrolid_Type = DmiDisplaystring
_A3Errorcontrolid_Object = MibTableColumn
a3Errorcontrolid = _A3Errorcontrolid_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 3, 1, 5),
    _A3Errorcontrolid_Type()
)
a3Errorcontrolid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Errorcontrolid.setStatus("mandatory")


class _A3EventStatus_Type(Integer32):
    """Custom type a3EventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vChanged", 1),
          ("vDiscovered", 0),
          ("vFailed", 2),
          ("vRecovered", 3))
    )


_A3EventStatus_Type.__name__ = "Integer32"
_A3EventStatus_Object = MibTableColumn
a3EventStatus = _A3EventStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 3, 1, 6),
    _A3EventStatus_Type()
)
a3EventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3EventStatus.setStatus("mandatory")
_TLogicalUnitGroup_Object = MibTable
tLogicalUnitGroup = _TLogicalUnitGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 4)
)
if mibBuilder.loadTexts:
    tLogicalUnitGroup.setStatus("mandatory")
_ELogicalUnitGroup_Object = MibTableRow
eLogicalUnitGroup = _ELogicalUnitGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 4, 1)
)
eLogicalUnitGroup.setIndexNames(
    (0, "ADAPTECSCSI-MIB", "DmiComponentIndex"),
    (0, "ADAPTECSCSI-MIB", "a4HostAdapterIndex"),
    (0, "ADAPTECSCSI-MIB", "a4ScsiId"),
    (0, "ADAPTECSCSI-MIB", "a4LogicalUnitId"),
)
if mibBuilder.loadTexts:
    eLogicalUnitGroup.setStatus("mandatory")
_A4HostAdapterIndex_Type = DmiInteger
_A4HostAdapterIndex_Object = MibTableColumn
a4HostAdapterIndex = _A4HostAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 4, 1, 1),
    _A4HostAdapterIndex_Type()
)
a4HostAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4HostAdapterIndex.setStatus("mandatory")
_A4ScsiId_Type = DmiInteger
_A4ScsiId_Object = MibTableColumn
a4ScsiId = _A4ScsiId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 4, 1, 2),
    _A4ScsiId_Type()
)
a4ScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4ScsiId.setStatus("mandatory")
_A4LogicalUnitId_Type = DmiInteger
_A4LogicalUnitId_Object = MibTableColumn
a4LogicalUnitId = _A4LogicalUnitId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 4, 1, 3),
    _A4LogicalUnitId_Type()
)
a4LogicalUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4LogicalUnitId.setStatus("mandatory")


class _A4LogicalUnitType_Type(Integer32):
    """Custom type a4LogicalUnitType based on Integer32"""
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
        *(("vCdrom", 6),
          ("vComdevice", 10),
          ("vDirectaccess", 1),
          ("vHostadapter", 11),
          ("vJukebox", 9),
          ("vOpticalmemory", 8),
          ("vOther", 12),
          ("vPrinter", 3),
          ("vProcessor", 4),
          ("vScanner", 7),
          ("vTape", 2),
          ("vWriteonce", 5))
    )


_A4LogicalUnitType_Type.__name__ = "Integer32"
_A4LogicalUnitType_Object = MibTableColumn
a4LogicalUnitType = _A4LogicalUnitType_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 4, 1, 4),
    _A4LogicalUnitType_Type()
)
a4LogicalUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4LogicalUnitType.setStatus("mandatory")
_A4LogicalUnitDescription_Type = DmiDisplaystring
_A4LogicalUnitDescription_Object = MibTableColumn
a4LogicalUnitDescription = _A4LogicalUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 4, 1, 5),
    _A4LogicalUnitDescription_Type()
)
a4LogicalUnitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4LogicalUnitDescription.setStatus("mandatory")
_A4Errorcontrolid_Type = DmiDisplaystring
_A4Errorcontrolid_Object = MibTableColumn
a4Errorcontrolid = _A4Errorcontrolid_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 4, 1, 6),
    _A4Errorcontrolid_Type()
)
a4Errorcontrolid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Errorcontrolid.setStatus("mandatory")


class _A4EventStatus_Type(Integer32):
    """Custom type a4EventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vChanged", 1),
          ("vDiscovered", 0),
          ("vFailed", 2),
          ("vRecovered", 3))
    )


_A4EventStatus_Type.__name__ = "Integer32"
_A4EventStatus_Object = MibTableColumn
a4EventStatus = _A4EventStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 4, 1, 7),
    _A4EventStatus_Type()
)
a4EventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4EventStatus.setStatus("mandatory")
_TErrorcontrol_Object = MibTable
tErrorcontrol = _TErrorcontrol_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 5)
)
if mibBuilder.loadTexts:
    tErrorcontrol.setStatus("mandatory")
_EErrorcontrol_Object = MibTableRow
eErrorcontrol = _EErrorcontrol_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 5, 1)
)
eErrorcontrol.setIndexNames(
    (0, "ADAPTECSCSI-MIB", "DmiComponentIndex"),
    (0, "ADAPTECSCSI-MIB", "a5Selfid"),
)
if mibBuilder.loadTexts:
    eErrorcontrol.setStatus("mandatory")
_A5Selfid_Type = DmiInteger
_A5Selfid_Object = MibTableColumn
a5Selfid = _A5Selfid_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 5, 1, 1),
    _A5Selfid_Type()
)
a5Selfid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Selfid.setStatus("mandatory")
_A5Fatalcount_Type = DmiCounter
_A5Fatalcount_Object = MibTableColumn
a5Fatalcount = _A5Fatalcount_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 5, 1, 2),
    _A5Fatalcount_Type()
)
a5Fatalcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Fatalcount.setStatus("mandatory")
_A5Majorcount_Type = DmiCounter
_A5Majorcount_Object = MibTableColumn
a5Majorcount = _A5Majorcount_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 5, 1, 3),
    _A5Majorcount_Type()
)
a5Majorcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Majorcount.setStatus("mandatory")
_A5Warningcount_Type = DmiCounter
_A5Warningcount_Object = MibTableColumn
a5Warningcount = _A5Warningcount_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 5, 1, 4),
    _A5Warningcount_Type()
)
a5Warningcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Warningcount.setStatus("mandatory")


class _A5Errstatus_Type(Integer32):
    """Custom type a5Errstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vFatal", 3),
          ("vMajor", 2),
          ("vOk", 0),
          ("vWarning", 1))
    )


_A5Errstatus_Type.__name__ = "Integer32"
_A5Errstatus_Object = MibTableColumn
a5Errstatus = _A5Errstatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 5, 1, 5),
    _A5Errstatus_Type()
)
a5Errstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Errstatus.setStatus("mandatory")


class _A5Errstatustype_Type(Integer32):
    """Custom type a5Errstatustype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vDiagnosticTest", 2),
          ("vPost", 0),
          ("vRuntime", 1))
    )


_A5Errstatustype_Type.__name__ = "Integer32"
_A5Errstatustype_Object = MibTableColumn
a5Errstatustype = _A5Errstatustype_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 5, 1, 6),
    _A5Errstatustype_Type()
)
a5Errstatustype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Errstatustype.setStatus("mandatory")


class _A5Indicationcontrol_Type(Integer32):
    """Custom type a5Indicationcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vOff", 0),
          ("vOn", 1))
    )


_A5Indicationcontrol_Type.__name__ = "Integer32"
_A5Indicationcontrol_Object = MibTableColumn
a5Indicationcontrol = _A5Indicationcontrol_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 5, 1, 7),
    _A5Indicationcontrol_Type()
)
a5Indicationcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a5Indicationcontrol.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "ADAPTECSCSI-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99MibName_Type = DmiDisplaystring
_A99MibName_Object = MibTableColumn
a99MibName = _A99MibName_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 99, 1, 1),
    _A99MibName_Type()
)
a99MibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibName.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTrap_Type = DmiInteger
_A99DisableTrap_Object = MibTableColumn
a99DisableTrap = _A99DisableTrap_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 99, 1, 3),
    _A99DisableTrap_Type()
)
a99DisableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a99DisableTrap.setStatus("mandatory")
_TTrapGroup_Object = MibTable
tTrapGroup = _TTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999)
)
if mibBuilder.loadTexts:
    tTrapGroup.setStatus("mandatory")
_ETrapGroup_Object = MibTableRow
eTrapGroup = _ETrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1)
)
eTrapGroup.setIndexNames(
    (0, "ADAPTECSCSI-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eTrapGroup.setStatus("mandatory")
_A9999ErrorTime_Type = DisplayString
_A9999ErrorTime_Object = MibTableColumn
a9999ErrorTime = _A9999ErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 1),
    _A9999ErrorTime_Type()
)
a9999ErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorTime.setStatus("mandatory")
_A9999ErrorStatus_Type = DmiInteger
_A9999ErrorStatus_Object = MibTableColumn
a9999ErrorStatus = _A9999ErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 2),
    _A9999ErrorStatus_Type()
)
a9999ErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorStatus.setStatus("mandatory")
_A9999ErrorGroupId_Type = DmiInteger
_A9999ErrorGroupId_Object = MibTableColumn
a9999ErrorGroupId = _A9999ErrorGroupId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 3),
    _A9999ErrorGroupId_Type()
)
a9999ErrorGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorGroupId.setStatus("mandatory")
_A9999ErrorInstanceId_Type = DmiInteger
_A9999ErrorInstanceId_Object = MibTableColumn
a9999ErrorInstanceId = _A9999ErrorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 4),
    _A9999ErrorInstanceId_Type()
)
a9999ErrorInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ErrorInstanceId.setStatus("mandatory")
_A9999ComponentId_Type = DmiInteger
_A9999ComponentId_Object = MibTableColumn
a9999ComponentId = _A9999ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 5),
    _A9999ComponentId_Type()
)
a9999ComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ComponentId.setStatus("mandatory")
_A9999GroupId_Type = DmiInteger
_A9999GroupId_Object = MibTableColumn
a9999GroupId = _A9999GroupId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 6),
    _A9999GroupId_Type()
)
a9999GroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999GroupId.setStatus("mandatory")
_A9999InstanceId_Type = DmiInteger
_A9999InstanceId_Object = MibTableColumn
a9999InstanceId = _A9999InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 7),
    _A9999InstanceId_Type()
)
a9999InstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999InstanceId.setStatus("mandatory")
_A9999VendorCode1_Type = DmiInteger
_A9999VendorCode1_Object = MibTableColumn
a9999VendorCode1 = _A9999VendorCode1_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 8),
    _A9999VendorCode1_Type()
)
a9999VendorCode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode1.setStatus("mandatory")
_A9999VendorCode2_Type = DmiInteger
_A9999VendorCode2_Object = MibTableColumn
a9999VendorCode2 = _A9999VendorCode2_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 9),
    _A9999VendorCode2_Type()
)
a9999VendorCode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorCode2.setStatus("mandatory")
_A9999VendorText_Type = OctetString
_A9999VendorText_Object = MibTableColumn
a9999VendorText = _A9999VendorText_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 10),
    _A9999VendorText_Type()
)
a9999VendorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999VendorText.setStatus("mandatory")
_A9999ParentGroupId_Type = DmiInteger
_A9999ParentGroupId_Object = MibTableColumn
a9999ParentGroupId = _A9999ParentGroupId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 11),
    _A9999ParentGroupId_Type()
)
a9999ParentGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentGroupId.setStatus("mandatory")
_A9999ParentInstanceId_Type = DmiInteger
_A9999ParentInstanceId_Object = MibTableColumn
a9999ParentInstanceId = _A9999ParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 12),
    _A9999ParentInstanceId_Type()
)
a9999ParentInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999ParentInstanceId.setStatus("mandatory")

# Managed Objects groups


# Notification objects

AdaptecEventError = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 2, 6, 1, 9999, 1, 0, 1)
)
AdaptecEventError.setObjects(
      *(("ADAPTECSCSI-MIB", "a9999ErrorTime"),
        ("ADAPTECSCSI-MIB", "a9999ErrorStatus"),
        ("ADAPTECSCSI-MIB", "a9999ErrorGroupId"),
        ("ADAPTECSCSI-MIB", "a9999ErrorInstanceId"),
        ("ADAPTECSCSI-MIB", "a9999ComponentId"),
        ("ADAPTECSCSI-MIB", "a9999GroupId"),
        ("ADAPTECSCSI-MIB", "a9999InstanceId"),
        ("ADAPTECSCSI-MIB", "a9999VendorCode1"),
        ("ADAPTECSCSI-MIB", "a9999VendorCode2"),
        ("ADAPTECSCSI-MIB", "a9999VendorText"),
        ("ADAPTECSCSI-MIB", "a9999ParentGroupId"),
        ("ADAPTECSCSI-MIB", "a9999ParentInstanceId"))
)
if mibBuilder.loadTexts:
    AdaptecEventError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADAPTECSCSI-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiInteger": DmiInteger,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiComponentIndex": DmiComponentIndex,
       "adaptec": adaptec,
       "products": products,
       "scsi": scsi,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tOperationGroup": tOperationGroup,
       "eOperationGroup": eOperationGroup,
       "a2PollDevices": a2PollDevices,
       "a2ScanDevices": a2ScanDevices,
       "a2IndicationControl": a2IndicationControl,
       "tHostAdapterGroup": tHostAdapterGroup,
       "eHostAdapterGroup": eHostAdapterGroup,
       "a3HostAdapterIndex": a3HostAdapterIndex,
       "a3HostAdapterDescription": a3HostAdapterDescription,
       "a3HostAdapterVersion": a3HostAdapterVersion,
       "a3ChannelCount": a3ChannelCount,
       "a3Errorcontrolid": a3Errorcontrolid,
       "a3EventStatus": a3EventStatus,
       "tLogicalUnitGroup": tLogicalUnitGroup,
       "eLogicalUnitGroup": eLogicalUnitGroup,
       "a4HostAdapterIndex": a4HostAdapterIndex,
       "a4ScsiId": a4ScsiId,
       "a4LogicalUnitId": a4LogicalUnitId,
       "a4LogicalUnitType": a4LogicalUnitType,
       "a4LogicalUnitDescription": a4LogicalUnitDescription,
       "a4Errorcontrolid": a4Errorcontrolid,
       "a4EventStatus": a4EventStatus,
       "tErrorcontrol": tErrorcontrol,
       "eErrorcontrol": eErrorcontrol,
       "a5Selfid": a5Selfid,
       "a5Fatalcount": a5Fatalcount,
       "a5Majorcount": a5Majorcount,
       "a5Warningcount": a5Warningcount,
       "a5Errstatus": a5Errstatus,
       "a5Errstatustype": a5Errstatustype,
       "a5Indicationcontrol": a5Indicationcontrol,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99MibName": a99MibName,
       "a99MibOid": a99MibOid,
       "a99DisableTrap": a99DisableTrap,
       "tTrapGroup": tTrapGroup,
       "eTrapGroup": eTrapGroup,
       "AdaptecEventError": AdaptecEventError,
       "a9999ErrorTime": a9999ErrorTime,
       "a9999ErrorStatus": a9999ErrorStatus,
       "a9999ErrorGroupId": a9999ErrorGroupId,
       "a9999ErrorInstanceId": a9999ErrorInstanceId,
       "a9999ComponentId": a9999ComponentId,
       "a9999GroupId": a9999GroupId,
       "a9999InstanceId": a9999InstanceId,
       "a9999VendorCode1": a9999VendorCode1,
       "a9999VendorCode2": a9999VendorCode2,
       "a9999VendorText": a9999VendorText,
       "a9999ParentGroupId": a9999ParentGroupId,
       "a9999ParentInstanceId": a9999ParentInstanceId}
)
