# SNMP MIB module (V2H124-24-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/V2H124-24-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:59 2024
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

(BridgeId,
 Timeout,
 dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

v2h124_24MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30)
)
v2h124_24MIB.setRevisions(
        ("2004-01-21 20:31",
         "2003-12-12 17:04",
         "2003-07-25 19:59",
         "2003-07-18 21:42",
         "2003-12-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ValidStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )



# MIB Managed Objects in the order of their OIDs

_V2h124_24MIBObjects_ObjectIdentity = ObjectIdentity
v2h124_24MIBObjects = _V2h124_24MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1)
)
_SwitchMgt_ObjectIdentity = ObjectIdentity
switchMgt = _SwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1)
)


class _SwitchManagementVlan_Type(Integer32):
    """Custom type switchManagementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwitchManagementVlan_Type.__name__ = "Integer32"
_SwitchManagementVlan_Object = MibScalar
switchManagementVlan = _SwitchManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 1),
    _SwitchManagementVlan_Type()
)
switchManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchManagementVlan.setStatus("current")
_V2h124switchNumber_Type = Integer32
_V2h124switchNumber_Object = MibScalar
v2h124switchNumber = _V2h124switchNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 2),
    _V2h124switchNumber_Type()
)
v2h124switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124switchNumber.setStatus("current")
_V2h124switchInfoTable_Object = MibTable
v2h124switchInfoTable = _V2h124switchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3)
)
if mibBuilder.loadTexts:
    v2h124switchInfoTable.setStatus("current")
_V2h124switchInfoEntry_Object = MibTableRow
v2h124switchInfoEntry = _V2h124switchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1)
)
v2h124switchInfoEntry.setIndexNames(
    (0, "V2H124-24-MIB", "v2h124swUnitIndex"),
)
if mibBuilder.loadTexts:
    v2h124switchInfoEntry.setStatus("current")
_V2h124swUnitIndex_Type = Integer32
_V2h124swUnitIndex_Object = MibTableColumn
v2h124swUnitIndex = _V2h124swUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 1),
    _V2h124swUnitIndex_Type()
)
v2h124swUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v2h124swUnitIndex.setStatus("current")


class _V2h124swHardwareVer_Type(DisplayString):
    """Custom type v2h124swHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V2h124swHardwareVer_Type.__name__ = "DisplayString"
_V2h124swHardwareVer_Object = MibTableColumn
v2h124swHardwareVer = _V2h124swHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 2),
    _V2h124swHardwareVer_Type()
)
v2h124swHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swHardwareVer.setStatus("current")


class _V2h124swMicrocodeVer_Type(DisplayString):
    """Custom type v2h124swMicrocodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V2h124swMicrocodeVer_Type.__name__ = "DisplayString"
_V2h124swMicrocodeVer_Object = MibTableColumn
v2h124swMicrocodeVer = _V2h124swMicrocodeVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 3),
    _V2h124swMicrocodeVer_Type()
)
v2h124swMicrocodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swMicrocodeVer.setStatus("current")


class _V2h124swLoaderVer_Type(DisplayString):
    """Custom type v2h124swLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V2h124swLoaderVer_Type.__name__ = "DisplayString"
_V2h124swLoaderVer_Object = MibTableColumn
v2h124swLoaderVer = _V2h124swLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 4),
    _V2h124swLoaderVer_Type()
)
v2h124swLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swLoaderVer.setStatus("current")


class _V2h124swBootRomVer_Type(DisplayString):
    """Custom type v2h124swBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V2h124swBootRomVer_Type.__name__ = "DisplayString"
_V2h124swBootRomVer_Object = MibTableColumn
v2h124swBootRomVer = _V2h124swBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 5),
    _V2h124swBootRomVer_Type()
)
v2h124swBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swBootRomVer.setStatus("current")


class _V2h124swOpCodeVer_Type(DisplayString):
    """Custom type v2h124swOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_V2h124swOpCodeVer_Type.__name__ = "DisplayString"
_V2h124swOpCodeVer_Object = MibTableColumn
v2h124swOpCodeVer = _V2h124swOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 6),
    _V2h124swOpCodeVer_Type()
)
v2h124swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swOpCodeVer.setStatus("current")
_V2h124swPortNumber_Type = Integer32
_V2h124swPortNumber_Object = MibTableColumn
v2h124swPortNumber = _V2h124swPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 7),
    _V2h124swPortNumber_Type()
)
v2h124swPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swPortNumber.setStatus("current")


class _V2h124swPowerStatus_Type(Integer32):
    """Custom type v2h124swPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalAndRedundantPower", 3),
          ("internalPower", 1),
          ("redundantPower", 2))
    )


_V2h124swPowerStatus_Type.__name__ = "Integer32"
_V2h124swPowerStatus_Object = MibTableColumn
v2h124swPowerStatus = _V2h124swPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 8),
    _V2h124swPowerStatus_Type()
)
v2h124swPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swPowerStatus.setStatus("current")


class _V2h124swRoleInSystem_Type(Integer32):
    """Custom type v2h124swRoleInSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupMaster", 2),
          ("master", 1),
          ("slave", 3))
    )


_V2h124swRoleInSystem_Type.__name__ = "Integer32"
_V2h124swRoleInSystem_Object = MibTableColumn
v2h124swRoleInSystem = _V2h124swRoleInSystem_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 9),
    _V2h124swRoleInSystem_Type()
)
v2h124swRoleInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swRoleInSystem.setStatus("current")


class _V2h124swSerialNumber_Type(DisplayString):
    """Custom type v2h124swSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_V2h124swSerialNumber_Type.__name__ = "DisplayString"
_V2h124swSerialNumber_Object = MibTableColumn
v2h124swSerialNumber = _V2h124swSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 10),
    _V2h124swSerialNumber_Type()
)
v2h124swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swSerialNumber.setStatus("current")


class _V2h124swExpansionSlot1_Type(Integer32):
    """Custom type v2h124swExpansionSlot1 based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("comboStackingSfp", 15),
          ("hundredBaseFxMtrjMmf", 5),
          ("hundredBaseFxScMmf", 3),
          ("hundredBaseFxScSmf", 4),
          ("notPresent", 1),
          ("other", 2),
          ("stackingModule", 11),
          ("tenHundredBaseFxMtrj4port", 14),
          ("tenHundredBaseT", 16),
          ("tenHundredBaseT4port", 13),
          ("thousandBaseLxScSmf", 9),
          ("thousandBaseSfp", 12),
          ("thousandBaseSxMtrjMmf", 7),
          ("thousandBaseSxScMmf", 6),
          ("thousandBaseT", 10),
          ("thousandBaseXGbic", 8))
    )


_V2h124swExpansionSlot1_Type.__name__ = "Integer32"
_V2h124swExpansionSlot1_Object = MibTableColumn
v2h124swExpansionSlot1 = _V2h124swExpansionSlot1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 11),
    _V2h124swExpansionSlot1_Type()
)
v2h124swExpansionSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swExpansionSlot1.setStatus("current")


class _V2h124swExpansionSlot2_Type(Integer32):
    """Custom type v2h124swExpansionSlot2 based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("comboStackingSfp", 15),
          ("hundredBaseFxMtrjMmf", 5),
          ("hundredBaseFxScMmf", 3),
          ("hundredBaseFxScSmf", 4),
          ("notPresent", 1),
          ("other", 2),
          ("stackingModule", 11),
          ("tenHundredBaseFxMtrj4port", 14),
          ("tenHundredBaseT", 16),
          ("tenHundredBaseT4port", 13),
          ("thousandBaseLxScSmf", 9),
          ("thousandBaseSfp", 12),
          ("thousandBaseSxMtrjMmf", 7),
          ("thousandBaseSxScMmf", 6),
          ("thousandBaseT", 10),
          ("thousandBaseXGbic", 8))
    )


_V2h124swExpansionSlot2_Type.__name__ = "Integer32"
_V2h124swExpansionSlot2_Object = MibTableColumn
v2h124swExpansionSlot2 = _V2h124swExpansionSlot2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 12),
    _V2h124swExpansionSlot2_Type()
)
v2h124swExpansionSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swExpansionSlot2.setStatus("current")


class _V2h124swServiceTag_Type(DisplayString):
    """Custom type v2h124swServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_V2h124swServiceTag_Type.__name__ = "DisplayString"
_V2h124swServiceTag_Object = MibTableColumn
v2h124swServiceTag = _V2h124swServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 3, 1, 13),
    _V2h124swServiceTag_Type()
)
v2h124swServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v2h124swServiceTag.setStatus("current")


class _SwitchOperState_Type(Integer32):
    """Custom type switchOperState based on Integer32"""
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


_SwitchOperState_Type.__name__ = "Integer32"
_SwitchOperState_Object = MibScalar
switchOperState = _SwitchOperState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 4),
    _SwitchOperState_Type()
)
switchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOperState.setStatus("current")
_SwitchProductId_ObjectIdentity = ObjectIdentity
switchProductId = _SwitchProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 5)
)


class _SwProdName_Type(DisplayString):
    """Custom type swProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdName_Type.__name__ = "DisplayString"
_SwProdName_Object = MibScalar
swProdName = _SwProdName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 5, 1),
    _SwProdName_Type()
)
swProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdName.setStatus("current")


class _SwProdManufacturer_Type(DisplayString):
    """Custom type swProdManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdManufacturer_Type.__name__ = "DisplayString"
_SwProdManufacturer_Object = MibScalar
swProdManufacturer = _SwProdManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 5, 2),
    _SwProdManufacturer_Type()
)
swProdManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdManufacturer.setStatus("current")


class _SwProdDescription_Type(DisplayString):
    """Custom type swProdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdDescription_Type.__name__ = "DisplayString"
_SwProdDescription_Object = MibScalar
swProdDescription = _SwProdDescription_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 5, 3),
    _SwProdDescription_Type()
)
swProdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdDescription.setStatus("current")


class _SwProdVersion_Type(DisplayString):
    """Custom type swProdVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdVersion_Type.__name__ = "DisplayString"
_SwProdVersion_Object = MibScalar
swProdVersion = _SwProdVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 5, 4),
    _SwProdVersion_Type()
)
swProdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdVersion.setStatus("current")


class _SwProdUrl_Type(DisplayString):
    """Custom type swProdUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdUrl_Type.__name__ = "DisplayString"
_SwProdUrl_Object = MibScalar
swProdUrl = _SwProdUrl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 5, 5),
    _SwProdUrl_Type()
)
swProdUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdUrl.setStatus("current")
_SwIdentifier_Type = Integer32
_SwIdentifier_Object = MibScalar
swIdentifier = _SwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 5, 6),
    _SwIdentifier_Type()
)
swIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIdentifier.setStatus("current")


class _SwChassisServiceTag_Type(DisplayString):
    """Custom type swChassisServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwChassisServiceTag_Type.__name__ = "DisplayString"
_SwChassisServiceTag_Object = MibScalar
swChassisServiceTag = _SwChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 5, 7),
    _SwChassisServiceTag_Type()
)
swChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swChassisServiceTag.setStatus("current")
_SwitchIndivPowerTable_Object = MibTable
switchIndivPowerTable = _SwitchIndivPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 6)
)
if mibBuilder.loadTexts:
    switchIndivPowerTable.setStatus("current")
_SwitchIndivPowerEntry_Object = MibTableRow
switchIndivPowerEntry = _SwitchIndivPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 6, 1)
)
switchIndivPowerEntry.setIndexNames(
    (0, "V2H124-24-MIB", "swIndivPowerUnitIndex"),
    (0, "V2H124-24-MIB", "swIndivPowerIndex"),
)
if mibBuilder.loadTexts:
    switchIndivPowerEntry.setStatus("current")
_SwIndivPowerUnitIndex_Type = Integer32
_SwIndivPowerUnitIndex_Object = MibTableColumn
swIndivPowerUnitIndex = _SwIndivPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 6, 1, 1),
    _SwIndivPowerUnitIndex_Type()
)
swIndivPowerUnitIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swIndivPowerUnitIndex.setStatus("current")


class _SwIndivPowerIndex_Type(Integer32):
    """Custom type swIndivPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalPower", 2),
          ("internalPower", 1))
    )


_SwIndivPowerIndex_Type.__name__ = "Integer32"
_SwIndivPowerIndex_Object = MibTableColumn
swIndivPowerIndex = _SwIndivPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 6, 1, 2),
    _SwIndivPowerIndex_Type()
)
swIndivPowerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swIndivPowerIndex.setStatus("current")


class _SwIndivPowerStatus_Type(Integer32):
    """Custom type swIndivPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("notPresent", 1),
          ("red", 3))
    )


_SwIndivPowerStatus_Type.__name__ = "Integer32"
_SwIndivPowerStatus_Object = MibTableColumn
swIndivPowerStatus = _SwIndivPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 1, 6, 1, 3),
    _SwIndivPowerStatus_Type()
)
swIndivPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivPowerStatus.setStatus("current")
_PortMgt_ObjectIdentity = ObjectIdentity
portMgt = _PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1)
)
portEntry.setIndexNames(
    (0, "V2H124-24-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("hundredBaseFX", 3),
          ("hundredBaseFxScMultiMode", 10),
          ("hundredBaseFxScSingleMode", 9),
          ("hundredBaseTX", 2),
          ("other", 1),
          ("thousandBaseGBIC", 7),
          ("thousandBaseLX", 5),
          ("thousandBaseSX", 4),
          ("thousandBaseSfp", 8),
          ("thousandBaseT", 6))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortSpeedDpxCfg_Type(Integer32):
    """Custom type portSpeedDpxCfg based on Integer32"""
    defaultValue = 2

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
        *(("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6),
          ("reserved", 1))
    )


_PortSpeedDpxCfg_Type.__name__ = "Integer32"
_PortSpeedDpxCfg_Object = MibTableColumn
portSpeedDpxCfg = _PortSpeedDpxCfg_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 4),
    _PortSpeedDpxCfg_Type()
)
portSpeedDpxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedDpxCfg.setStatus("current")


class _PortFlowCtrlCfg_Type(Integer32):
    """Custom type portFlowCtrlCfg based on Integer32"""
    defaultValue = 1

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
        *(("backPressure", 3),
          ("disabled", 2),
          ("dot3xFlowControl", 4),
          ("enabled", 1))
    )


_PortFlowCtrlCfg_Type.__name__ = "Integer32"
_PortFlowCtrlCfg_Object = MibTableColumn
portFlowCtrlCfg = _PortFlowCtrlCfg_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 5),
    _PortFlowCtrlCfg_Type()
)
portFlowCtrlCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowCtrlCfg.setStatus("current")


class _PortCapabilities_Type(Bits):
    """Custom type portCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("portCap1000full", 5),
          ("portCap1000half", 4),
          ("portCap100full", 3),
          ("portCap100half", 2),
          ("portCap10full", 1),
          ("portCap10half", 0),
          ("portCapFlowCtrl", 15),
          ("portCapSym", 14),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("reserved9", 9))
    )

_PortCapabilities_Type.__name__ = "Bits"
_PortCapabilities_Object = MibTableColumn
portCapabilities = _PortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")
_PortAutonegotiation_Type = EnabledStatus
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 7),
    _PortAutonegotiation_Type()
)
portAutonegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutonegotiation.setStatus("current")


class _PortSpeedDpxStatus_Type(Integer32):
    """Custom type portSpeedDpxStatus based on Integer32"""
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
        *(("error", 1),
          ("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6))
    )


_PortSpeedDpxStatus_Type.__name__ = "Integer32"
_PortSpeedDpxStatus_Object = MibTableColumn
portSpeedDpxStatus = _PortSpeedDpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 8),
    _PortSpeedDpxStatus_Type()
)
portSpeedDpxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeedDpxStatus.setStatus("current")


class _PortFlowCtrlStatus_Type(Integer32):
    """Custom type portFlowCtrlStatus based on Integer32"""
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
        *(("backPressure", 2),
          ("dot3xFlowControl", 3),
          ("error", 1),
          ("none", 4))
    )


_PortFlowCtrlStatus_Type.__name__ = "Integer32"
_PortFlowCtrlStatus_Object = MibTableColumn
portFlowCtrlStatus = _PortFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_PortTrunkIndex_Type = Integer32
_PortTrunkIndex_Object = MibTableColumn
portTrunkIndex = _PortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 2, 1, 1, 10),
    _PortTrunkIndex_Type()
)
portTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkIndex.setStatus("current")
_TrunkMgt_ObjectIdentity = ObjectIdentity
trunkMgt = _TrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 3)
)
_TrunkMaxId_Type = Integer32
_TrunkMaxId_Object = MibScalar
trunkMaxId = _TrunkMaxId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 3, 1),
    _TrunkMaxId_Type()
)
trunkMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMaxId.setStatus("current")
_TrunkValidNumber_Type = Integer32
_TrunkValidNumber_Object = MibScalar
trunkValidNumber = _TrunkValidNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 3, 2),
    _TrunkValidNumber_Type()
)
trunkValidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkValidNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 3, 3, 1)
)
trunkEntry.setIndexNames(
    (0, "V2H124-24-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 3, 3, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 3, 3, 1, 2),
    _TrunkPorts_Type()
)
trunkPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkPorts.setStatus("current")


class _TrunkCreation_Type(Integer32):
    """Custom type trunkCreation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 2),
          ("static", 1))
    )


_TrunkCreation_Type.__name__ = "Integer32"
_TrunkCreation_Object = MibTableColumn
trunkCreation = _TrunkCreation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 3, 3, 1, 3),
    _TrunkCreation_Type()
)
trunkCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCreation.setStatus("current")
_TrunkStatus_Type = ValidStatus
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 3, 3, 1, 4),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_LacpMgt_ObjectIdentity = ObjectIdentity
lacpMgt = _LacpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 4)
)
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 4, 1, 1)
)
lacpPortEntry.setIndexNames(
    (0, "V2H124-24-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")
_LacpPortIndex_Type = Integer32
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 4, 1, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")
_LacpPortStatus_Type = EnabledStatus
_LacpPortStatus_Object = MibTableColumn
lacpPortStatus = _LacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 4, 1, 1, 2),
    _LacpPortStatus_Type()
)
lacpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortStatus.setStatus("current")
_StaMgt_ObjectIdentity = ObjectIdentity
staMgt = _StaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5)
)


class _StaSystemStatus_Type(EnabledStatus):
    """Custom type staSystemStatus based on EnabledStatus"""


_StaSystemStatus_Object = MibScalar
staSystemStatus = _StaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 1),
    _StaSystemStatus_Type()
)
staSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemStatus.setStatus("current")
_StaPortTable_Object = MibTable
staPortTable = _StaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 2)
)
if mibBuilder.loadTexts:
    staPortTable.setStatus("current")
_StaPortEntry_Object = MibTableRow
staPortEntry = _StaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    staPortEntry.setStatus("current")
_StaPortFastForward_Type = EnabledStatus
_StaPortFastForward_Object = MibTableColumn
staPortFastForward = _StaPortFastForward_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 2, 1, 2),
    _StaPortFastForward_Type()
)
staPortFastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortFastForward.setStatus("current")
_StaPortProtocolMigration_Type = TruthValue
_StaPortProtocolMigration_Object = MibTableColumn
staPortProtocolMigration = _StaPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 2, 1, 3),
    _StaPortProtocolMigration_Type()
)
staPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortProtocolMigration.setStatus("current")
_StaPortAdminEdgePort_Type = TruthValue
_StaPortAdminEdgePort_Object = MibTableColumn
staPortAdminEdgePort = _StaPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 2, 1, 4),
    _StaPortAdminEdgePort_Type()
)
staPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminEdgePort.setStatus("current")
_StaPortOperEdgePort_Type = TruthValue
_StaPortOperEdgePort_Object = MibTableColumn
staPortOperEdgePort = _StaPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 2, 1, 5),
    _StaPortOperEdgePort_Type()
)
staPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperEdgePort.setStatus("current")


class _StaPortAdminPointToPoint_Type(Integer32):
    """Custom type staPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_StaPortAdminPointToPoint_Type.__name__ = "Integer32"
_StaPortAdminPointToPoint_Object = MibTableColumn
staPortAdminPointToPoint = _StaPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 2, 1, 6),
    _StaPortAdminPointToPoint_Type()
)
staPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminPointToPoint.setStatus("current")
_StaPortOperPointToPoint_Type = TruthValue
_StaPortOperPointToPoint_Object = MibTableColumn
staPortOperPointToPoint = _StaPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 2, 1, 7),
    _StaPortOperPointToPoint_Type()
)
staPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperPointToPoint.setStatus("current")


class _StaPortLongPathCost_Type(Integer32):
    """Custom type staPortLongPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StaPortLongPathCost_Type.__name__ = "Integer32"
_StaPortLongPathCost_Object = MibTableColumn
staPortLongPathCost = _StaPortLongPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 2, 1, 8),
    _StaPortLongPathCost_Type()
)
staPortLongPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortLongPathCost.setStatus("current")


class _StaProtocolType_Type(Integer32):
    """Custom type staProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stp", 1))
    )


_StaProtocolType_Type.__name__ = "Integer32"
_StaProtocolType_Object = MibScalar
staProtocolType = _StaProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 3),
    _StaProtocolType_Type()
)
staProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staProtocolType.setStatus("current")


class _StaTxHoldCount_Type(Integer32):
    """Custom type staTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StaTxHoldCount_Type.__name__ = "Integer32"
_StaTxHoldCount_Object = MibScalar
staTxHoldCount = _StaTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 4),
    _StaTxHoldCount_Type()
)
staTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staTxHoldCount.setStatus("current")


class _StaPathCostMethod_Type(Integer32):
    """Custom type staPathCostMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_StaPathCostMethod_Type.__name__ = "Integer32"
_StaPathCostMethod_Object = MibScalar
staPathCostMethod = _StaPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 5),
    _StaPathCostMethod_Type()
)
staPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPathCostMethod.setStatus("current")
_XstMgt_ObjectIdentity = ObjectIdentity
xstMgt = _XstMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6)
)
_XstInstanceCfgTable_Object = MibTable
xstInstanceCfgTable = _XstInstanceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    xstInstanceCfgTable.setStatus("current")
_XstInstanceCfgEntry_Object = MibTableRow
xstInstanceCfgEntry = _XstInstanceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1)
)
xstInstanceCfgEntry.setIndexNames(
    (0, "V2H124-24-MIB", "xstInstanceCfgIndex"),
)
if mibBuilder.loadTexts:
    xstInstanceCfgEntry.setStatus("current")


class _XstInstanceCfgIndex_Type(Integer32):
    """Custom type xstInstanceCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_XstInstanceCfgIndex_Type.__name__ = "Integer32"
_XstInstanceCfgIndex_Object = MibTableColumn
xstInstanceCfgIndex = _XstInstanceCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 1),
    _XstInstanceCfgIndex_Type()
)
xstInstanceCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstanceCfgIndex.setStatus("current")


class _XstInstanceCfgPriority_Type(Integer32):
    """Custom type xstInstanceCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_XstInstanceCfgPriority_Type.__name__ = "Integer32"
_XstInstanceCfgPriority_Object = MibTableColumn
xstInstanceCfgPriority = _XstInstanceCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 2),
    _XstInstanceCfgPriority_Type()
)
xstInstanceCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstanceCfgPriority.setStatus("current")
_XstInstanceCfgTimeSinceTopologyChange_Type = Integer32
_XstInstanceCfgTimeSinceTopologyChange_Object = MibTableColumn
xstInstanceCfgTimeSinceTopologyChange = _XstInstanceCfgTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 3),
    _XstInstanceCfgTimeSinceTopologyChange_Type()
)
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTimeSinceTopologyChange.setStatus("current")
_XstInstanceCfgTopChanges_Type = Integer32
_XstInstanceCfgTopChanges_Object = MibTableColumn
xstInstanceCfgTopChanges = _XstInstanceCfgTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 4),
    _XstInstanceCfgTopChanges_Type()
)
xstInstanceCfgTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTopChanges.setStatus("current")
_XstInstanceCfgDesignatedRoot_Type = BridgeId
_XstInstanceCfgDesignatedRoot_Object = MibTableColumn
xstInstanceCfgDesignatedRoot = _XstInstanceCfgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 5),
    _XstInstanceCfgDesignatedRoot_Type()
)
xstInstanceCfgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgDesignatedRoot.setStatus("current")
_XstInstanceCfgRootCost_Type = Integer32
_XstInstanceCfgRootCost_Object = MibTableColumn
xstInstanceCfgRootCost = _XstInstanceCfgRootCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 6),
    _XstInstanceCfgRootCost_Type()
)
xstInstanceCfgRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootCost.setStatus("current")
_XstInstanceCfgRootPort_Type = Integer32
_XstInstanceCfgRootPort_Object = MibTableColumn
xstInstanceCfgRootPort = _XstInstanceCfgRootPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 7),
    _XstInstanceCfgRootPort_Type()
)
xstInstanceCfgRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootPort.setStatus("current")
_XstInstanceCfgMaxAge_Type = Timeout
_XstInstanceCfgMaxAge_Object = MibTableColumn
xstInstanceCfgMaxAge = _XstInstanceCfgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 8),
    _XstInstanceCfgMaxAge_Type()
)
xstInstanceCfgMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgMaxAge.setStatus("current")
_XstInstanceCfgHelloTime_Type = Timeout
_XstInstanceCfgHelloTime_Object = MibTableColumn
xstInstanceCfgHelloTime = _XstInstanceCfgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 9),
    _XstInstanceCfgHelloTime_Type()
)
xstInstanceCfgHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHelloTime.setStatus("current")
_XstInstanceCfgHoldTime_Type = Timeout
_XstInstanceCfgHoldTime_Object = MibTableColumn
xstInstanceCfgHoldTime = _XstInstanceCfgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 10),
    _XstInstanceCfgHoldTime_Type()
)
xstInstanceCfgHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHoldTime.setStatus("current")
_XstInstanceCfgForwardDelay_Type = Timeout
_XstInstanceCfgForwardDelay_Object = MibTableColumn
xstInstanceCfgForwardDelay = _XstInstanceCfgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 11),
    _XstInstanceCfgForwardDelay_Type()
)
xstInstanceCfgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgForwardDelay.setStatus("current")
_XstInstanceCfgBridgeMaxAge_Type = Timeout
_XstInstanceCfgBridgeMaxAge_Object = MibTableColumn
xstInstanceCfgBridgeMaxAge = _XstInstanceCfgBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 12),
    _XstInstanceCfgBridgeMaxAge_Type()
)
xstInstanceCfgBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeMaxAge.setStatus("current")
_XstInstanceCfgBridgeHelloTime_Type = Timeout
_XstInstanceCfgBridgeHelloTime_Object = MibTableColumn
xstInstanceCfgBridgeHelloTime = _XstInstanceCfgBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 13),
    _XstInstanceCfgBridgeHelloTime_Type()
)
xstInstanceCfgBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeHelloTime.setStatus("current")
_XstInstanceCfgBridgeForwardDelay_Type = Timeout
_XstInstanceCfgBridgeForwardDelay_Object = MibTableColumn
xstInstanceCfgBridgeForwardDelay = _XstInstanceCfgBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 14),
    _XstInstanceCfgBridgeForwardDelay_Type()
)
xstInstanceCfgBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeForwardDelay.setStatus("current")
_XstInstanceCfgTxHoldCount_Type = Integer32
_XstInstanceCfgTxHoldCount_Object = MibTableColumn
xstInstanceCfgTxHoldCount = _XstInstanceCfgTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 15),
    _XstInstanceCfgTxHoldCount_Type()
)
xstInstanceCfgTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTxHoldCount.setStatus("current")


class _XstInstanceCfgPathCostMethod_Type(Integer32):
    """Custom type xstInstanceCfgPathCostMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_XstInstanceCfgPathCostMethod_Type.__name__ = "Integer32"
_XstInstanceCfgPathCostMethod_Object = MibTableColumn
xstInstanceCfgPathCostMethod = _XstInstanceCfgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 4, 1, 16),
    _XstInstanceCfgPathCostMethod_Type()
)
xstInstanceCfgPathCostMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgPathCostMethod.setStatus("current")
_XstInstancePortTable_Object = MibTable
xstInstancePortTable = _XstInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    xstInstancePortTable.setStatus("current")
_XstInstancePortEntry_Object = MibTableRow
xstInstancePortEntry = _XstInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1)
)
xstInstancePortEntry.setIndexNames(
    (0, "V2H124-24-MIB", "xstInstanceCfgIndex"),
    (0, "BRIDGE-MIB", "dot1dStpPort"),
)
if mibBuilder.loadTexts:
    xstInstancePortEntry.setStatus("current")


class _XstInstancePortPriority_Type(Integer32):
    """Custom type xstInstancePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_XstInstancePortPriority_Type.__name__ = "Integer32"
_XstInstancePortPriority_Object = MibTableColumn
xstInstancePortPriority = _XstInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 3),
    _XstInstancePortPriority_Type()
)
xstInstancePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortPriority.setStatus("current")


class _XstInstancePortState_Type(Integer32):
    """Custom type xstInstancePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("forwarding", 3),
          ("learning", 2))
    )


_XstInstancePortState_Type.__name__ = "Integer32"
_XstInstancePortState_Object = MibTableColumn
xstInstancePortState = _XstInstancePortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 4),
    _XstInstancePortState_Type()
)
xstInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortState.setStatus("current")
_XstInstancePortEnable_Type = EnabledStatus
_XstInstancePortEnable_Object = MibTableColumn
xstInstancePortEnable = _XstInstancePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 5),
    _XstInstancePortEnable_Type()
)
xstInstancePortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortEnable.setStatus("current")


class _XstInstancePortPathCost_Type(Integer32):
    """Custom type xstInstancePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_XstInstancePortPathCost_Type.__name__ = "Integer32"
_XstInstancePortPathCost_Object = MibTableColumn
xstInstancePortPathCost = _XstInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 6),
    _XstInstancePortPathCost_Type()
)
xstInstancePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortPathCost.setStatus("current")
_XstInstancePortDesignatedRoot_Type = BridgeId
_XstInstancePortDesignatedRoot_Object = MibTableColumn
xstInstancePortDesignatedRoot = _XstInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 7),
    _XstInstancePortDesignatedRoot_Type()
)
xstInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedRoot.setStatus("current")
_XstInstancePortDesignatedCost_Type = Integer32
_XstInstancePortDesignatedCost_Object = MibTableColumn
xstInstancePortDesignatedCost = _XstInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 8),
    _XstInstancePortDesignatedCost_Type()
)
xstInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedCost.setStatus("current")
_XstInstancePortDesignatedBridge_Type = BridgeId
_XstInstancePortDesignatedBridge_Object = MibTableColumn
xstInstancePortDesignatedBridge = _XstInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 9),
    _XstInstancePortDesignatedBridge_Type()
)
xstInstancePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedBridge.setStatus("current")


class _XstInstancePortDesignatedPort_Type(OctetString):
    """Custom type xstInstancePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_XstInstancePortDesignatedPort_Type.__name__ = "OctetString"
_XstInstancePortDesignatedPort_Object = MibTableColumn
xstInstancePortDesignatedPort = _XstInstancePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 10),
    _XstInstancePortDesignatedPort_Type()
)
xstInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedPort.setStatus("current")
_XstInstancePortForwardTransitions_Type = Counter32
_XstInstancePortForwardTransitions_Object = MibTableColumn
xstInstancePortForwardTransitions = _XstInstancePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 11),
    _XstInstancePortForwardTransitions_Type()
)
xstInstancePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortForwardTransitions.setStatus("current")


class _XstInstancePortPortRole_Type(Integer32):
    """Custom type xstInstancePortPortRole based on Integer32"""
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
        *(("alternate", 4),
          ("backup", 5),
          ("designated", 3),
          ("disabled", 1),
          ("root", 2))
    )


_XstInstancePortPortRole_Type.__name__ = "Integer32"
_XstInstancePortPortRole_Object = MibTableColumn
xstInstancePortPortRole = _XstInstancePortPortRole_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 5, 6, 5, 1, 12),
    _XstInstancePortPortRole_Type()
)
xstInstancePortPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortPortRole.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 7)
)


class _RestartOpCodeFile_Type(DisplayString):
    """Custom type restartOpCodeFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RestartOpCodeFile_Type.__name__ = "DisplayString"
_RestartOpCodeFile_Object = MibScalar
restartOpCodeFile = _RestartOpCodeFile_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 7, 1),
    _RestartOpCodeFile_Type()
)
restartOpCodeFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOpCodeFile.setStatus("current")


class _RestartConfigFile_Type(DisplayString):
    """Custom type restartConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RestartConfigFile_Type.__name__ = "DisplayString"
_RestartConfigFile_Object = MibScalar
restartConfigFile = _RestartConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 7, 2),
    _RestartConfigFile_Type()
)
restartConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartConfigFile.setStatus("current")


class _RestartControl_Type(Integer32):
    """Custom type restartControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldBoot", 3),
          ("running", 1),
          ("warmBoot", 2))
    )


_RestartControl_Type.__name__ = "Integer32"
_RestartControl_Object = MibScalar
restartControl = _RestartControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 7, 3),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_MirrorMgt_ObjectIdentity = ObjectIdentity
mirrorMgt = _MirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 8)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 8, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "V2H124-24-MIB", "mirrorDestinationPort"),
    (0, "V2H124-24-MIB", "mirrorSourcePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorDestinationPort_Type = Integer32
_MirrorDestinationPort_Object = MibTableColumn
mirrorDestinationPort = _MirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 8, 1, 1, 1),
    _MirrorDestinationPort_Type()
)
mirrorDestinationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorDestinationPort.setStatus("current")
_MirrorSourcePort_Type = Integer32
_MirrorSourcePort_Object = MibTableColumn
mirrorSourcePort = _MirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 8, 1, 1, 2),
    _MirrorSourcePort_Type()
)
mirrorSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorSourcePort.setStatus("current")


class _MirrorType_Type(Integer32):
    """Custom type mirrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("rx", 1),
          ("tx", 2))
    )


_MirrorType_Type.__name__ = "Integer32"
_MirrorType_Object = MibTableColumn
mirrorType = _MirrorType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 8, 1, 1, 3),
    _MirrorType_Type()
)
mirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorType.setStatus("current")
_MirrorStatus_Type = ValidStatus
_MirrorStatus_Object = MibTableColumn
mirrorStatus = _MirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 8, 1, 1, 4),
    _MirrorStatus_Type()
)
mirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorStatus.setStatus("current")
_IgmpSnoopMgt_ObjectIdentity = ObjectIdentity
igmpSnoopMgt = _IgmpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9)
)


class _IgmpSnoopStatus_Type(EnabledStatus):
    """Custom type igmpSnoopStatus based on EnabledStatus"""


_IgmpSnoopStatus_Object = MibScalar
igmpSnoopStatus = _IgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 1),
    _IgmpSnoopStatus_Type()
)
igmpSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopStatus.setStatus("current")


class _IgmpSnoopQuerier_Type(EnabledStatus):
    """Custom type igmpSnoopQuerier based on EnabledStatus"""


_IgmpSnoopQuerier_Object = MibScalar
igmpSnoopQuerier = _IgmpSnoopQuerier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 2),
    _IgmpSnoopQuerier_Type()
)
igmpSnoopQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQuerier.setStatus("current")


class _IgmpSnoopQueryCount_Type(Integer32):
    """Custom type igmpSnoopQueryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_IgmpSnoopQueryCount_Type.__name__ = "Integer32"
_IgmpSnoopQueryCount_Object = MibScalar
igmpSnoopQueryCount = _IgmpSnoopQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 3),
    _IgmpSnoopQueryCount_Type()
)
igmpSnoopQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryCount.setStatus("current")


class _IgmpSnoopQueryInterval_Type(Integer32):
    """Custom type igmpSnoopQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 125),
    )


_IgmpSnoopQueryInterval_Type.__name__ = "Integer32"
_IgmpSnoopQueryInterval_Object = MibScalar
igmpSnoopQueryInterval = _IgmpSnoopQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 4),
    _IgmpSnoopQueryInterval_Type()
)
igmpSnoopQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryInterval.setStatus("current")


class _IgmpSnoopQueryMaxResponseTime_Type(Integer32):
    """Custom type igmpSnoopQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 25),
    )


_IgmpSnoopQueryMaxResponseTime_Type.__name__ = "Integer32"
_IgmpSnoopQueryMaxResponseTime_Object = MibScalar
igmpSnoopQueryMaxResponseTime = _IgmpSnoopQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 5),
    _IgmpSnoopQueryMaxResponseTime_Type()
)
igmpSnoopQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryMaxResponseTime.setStatus("current")


class _IgmpSnoopRouterPortExpireTime_Type(Integer32):
    """Custom type igmpSnoopRouterPortExpireTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 500),
    )


_IgmpSnoopRouterPortExpireTime_Type.__name__ = "Integer32"
_IgmpSnoopRouterPortExpireTime_Object = MibScalar
igmpSnoopRouterPortExpireTime = _IgmpSnoopRouterPortExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 6),
    _IgmpSnoopRouterPortExpireTime_Type()
)
igmpSnoopRouterPortExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopRouterPortExpireTime.setStatus("current")


class _IgmpSnoopVersion_Type(Integer32):
    """Custom type igmpSnoopVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IgmpSnoopVersion_Type.__name__ = "Integer32"
_IgmpSnoopVersion_Object = MibScalar
igmpSnoopVersion = _IgmpSnoopVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 7),
    _IgmpSnoopVersion_Type()
)
igmpSnoopVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVersion.setStatus("current")
_IgmpSnoopRouterCurrentTable_Object = MibTable
igmpSnoopRouterCurrentTable = _IgmpSnoopRouterCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 8)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentTable.setStatus("current")
_IgmpSnoopRouterCurrentEntry_Object = MibTableRow
igmpSnoopRouterCurrentEntry = _IgmpSnoopRouterCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 8, 1)
)
igmpSnoopRouterCurrentEntry.setIndexNames(
    (0, "V2H124-24-MIB", "igmpSnoopRouterCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentEntry.setStatus("current")
_IgmpSnoopRouterCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object = MibTableColumn
igmpSnoopRouterCurrentVlanIndex = _IgmpSnoopRouterCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 8, 1, 1),
    _IgmpSnoopRouterCurrentVlanIndex_Type()
)
igmpSnoopRouterCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentVlanIndex.setStatus("current")
_IgmpSnoopRouterCurrentPorts_Type = PortList
_IgmpSnoopRouterCurrentPorts_Object = MibTableColumn
igmpSnoopRouterCurrentPorts = _IgmpSnoopRouterCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 8, 1, 2),
    _IgmpSnoopRouterCurrentPorts_Type()
)
igmpSnoopRouterCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentPorts.setStatus("current")
_IgmpSnoopRouterCurrentStatus_Type = PortList
_IgmpSnoopRouterCurrentStatus_Object = MibTableColumn
igmpSnoopRouterCurrentStatus = _IgmpSnoopRouterCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 8, 1, 3),
    _IgmpSnoopRouterCurrentStatus_Type()
)
igmpSnoopRouterCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentStatus.setStatus("current")
_IgmpSnoopRouterStaticTable_Object = MibTable
igmpSnoopRouterStaticTable = _IgmpSnoopRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticTable.setStatus("current")
_IgmpSnoopRouterStaticEntry_Object = MibTableRow
igmpSnoopRouterStaticEntry = _IgmpSnoopRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 9, 1)
)
igmpSnoopRouterStaticEntry.setIndexNames(
    (0, "V2H124-24-MIB", "igmpSnoopRouterStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticEntry.setStatus("current")
_IgmpSnoopRouterStaticVlanIndex_Type = Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object = MibTableColumn
igmpSnoopRouterStaticVlanIndex = _IgmpSnoopRouterStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 9, 1, 1),
    _IgmpSnoopRouterStaticVlanIndex_Type()
)
igmpSnoopRouterStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticVlanIndex.setStatus("current")
_IgmpSnoopRouterStaticPorts_Type = PortList
_IgmpSnoopRouterStaticPorts_Object = MibTableColumn
igmpSnoopRouterStaticPorts = _IgmpSnoopRouterStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 9, 1, 2),
    _IgmpSnoopRouterStaticPorts_Type()
)
igmpSnoopRouterStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticPorts.setStatus("current")
_IgmpSnoopRouterStaticStatus_Type = ValidStatus
_IgmpSnoopRouterStaticStatus_Object = MibTableColumn
igmpSnoopRouterStaticStatus = _IgmpSnoopRouterStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 9, 1, 3),
    _IgmpSnoopRouterStaticStatus_Type()
)
igmpSnoopRouterStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticStatus.setStatus("current")
_IgmpSnoopMulticastCurrentTable_Object = MibTable
igmpSnoopMulticastCurrentTable = _IgmpSnoopMulticastCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 10)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentTable.setStatus("current")
_IgmpSnoopMulticastCurrentEntry_Object = MibTableRow
igmpSnoopMulticastCurrentEntry = _IgmpSnoopMulticastCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 10, 1)
)
igmpSnoopMulticastCurrentEntry.setIndexNames(
    (0, "V2H124-24-MIB", "igmpSnoopMulticastCurrentVlanIndex"),
    (0, "V2H124-24-MIB", "igmpSnoopMulticastCurrentIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentEntry.setStatus("current")
_IgmpSnoopMulticastCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object = MibTableColumn
igmpSnoopMulticastCurrentVlanIndex = _IgmpSnoopMulticastCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 10, 1, 1),
    _IgmpSnoopMulticastCurrentVlanIndex_Type()
)
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentVlanIndex.setStatus("current")
_IgmpSnoopMulticastCurrentIpAddress_Type = IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object = MibTableColumn
igmpSnoopMulticastCurrentIpAddress = _IgmpSnoopMulticastCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 10, 1, 2),
    _IgmpSnoopMulticastCurrentIpAddress_Type()
)
igmpSnoopMulticastCurrentIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentIpAddress.setStatus("current")
_IgmpSnoopMulticastCurrentPorts_Type = PortList
_IgmpSnoopMulticastCurrentPorts_Object = MibTableColumn
igmpSnoopMulticastCurrentPorts = _IgmpSnoopMulticastCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 10, 1, 3),
    _IgmpSnoopMulticastCurrentPorts_Type()
)
igmpSnoopMulticastCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentPorts.setStatus("current")
_IgmpSnoopMulticastCurrentStatus_Type = PortList
_IgmpSnoopMulticastCurrentStatus_Object = MibTableColumn
igmpSnoopMulticastCurrentStatus = _IgmpSnoopMulticastCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 10, 1, 4),
    _IgmpSnoopMulticastCurrentStatus_Type()
)
igmpSnoopMulticastCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentStatus.setStatus("current")
_IgmpSnoopMulticastStaticTable_Object = MibTable
igmpSnoopMulticastStaticTable = _IgmpSnoopMulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 11)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticTable.setStatus("current")
_IgmpSnoopMulticastStaticEntry_Object = MibTableRow
igmpSnoopMulticastStaticEntry = _IgmpSnoopMulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 11, 1)
)
igmpSnoopMulticastStaticEntry.setIndexNames(
    (0, "V2H124-24-MIB", "igmpSnoopMulticastStaticVlanIndex"),
    (0, "V2H124-24-MIB", "igmpSnoopMulticastStaticIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticEntry.setStatus("current")
_IgmpSnoopMulticastStaticVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object = MibTableColumn
igmpSnoopMulticastStaticVlanIndex = _IgmpSnoopMulticastStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 11, 1, 1),
    _IgmpSnoopMulticastStaticVlanIndex_Type()
)
igmpSnoopMulticastStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticVlanIndex.setStatus("current")
_IgmpSnoopMulticastStaticIpAddress_Type = IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object = MibTableColumn
igmpSnoopMulticastStaticIpAddress = _IgmpSnoopMulticastStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 11, 1, 2),
    _IgmpSnoopMulticastStaticIpAddress_Type()
)
igmpSnoopMulticastStaticIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticIpAddress.setStatus("current")
_IgmpSnoopMulticastStaticPorts_Type = PortList
_IgmpSnoopMulticastStaticPorts_Object = MibTableColumn
igmpSnoopMulticastStaticPorts = _IgmpSnoopMulticastStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 11, 1, 3),
    _IgmpSnoopMulticastStaticPorts_Type()
)
igmpSnoopMulticastStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticPorts.setStatus("current")
_IgmpSnoopMulticastStaticStatus_Type = ValidStatus
_IgmpSnoopMulticastStaticStatus_Object = MibTableColumn
igmpSnoopMulticastStaticStatus = _IgmpSnoopMulticastStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 9, 11, 1, 4),
    _IgmpSnoopMulticastStaticStatus_Type()
)
igmpSnoopMulticastStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticStatus.setStatus("current")
_IpMgt_ObjectIdentity = ObjectIdentity
ipMgt = _IpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10)
)
_NetConfigTable_Object = MibTable
netConfigTable = _NetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 1)
)
if mibBuilder.loadTexts:
    netConfigTable.setStatus("current")
_NetConfigEntry_Object = MibTableRow
netConfigEntry = _NetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 1, 1)
)
netConfigEntry.setIndexNames(
    (0, "V2H124-24-MIB", "netConfigIfIndex"),
    (0, "V2H124-24-MIB", "netConfigIPAddress"),
    (0, "V2H124-24-MIB", "netConfigSubnetMask"),
)
if mibBuilder.loadTexts:
    netConfigEntry.setStatus("current")
_NetConfigIfIndex_Type = Integer32
_NetConfigIfIndex_Object = MibTableColumn
netConfigIfIndex = _NetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 1, 1, 1),
    _NetConfigIfIndex_Type()
)
netConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIfIndex.setStatus("current")
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibTableColumn
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 1, 1, 2),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("current")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibTableColumn
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 1, 1, 3),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigSubnetMask.setStatus("current")


class _NetConfigPrimaryInterface_Type(Integer32):
    """Custom type netConfigPrimaryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_NetConfigPrimaryInterface_Type.__name__ = "Integer32"
_NetConfigPrimaryInterface_Object = MibTableColumn
netConfigPrimaryInterface = _NetConfigPrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 1, 1, 4),
    _NetConfigPrimaryInterface_Type()
)
netConfigPrimaryInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigPrimaryInterface.setStatus("current")


class _NetConfigUnnumbered_Type(Integer32):
    """Custom type netConfigUnnumbered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notUnnumbered", 2),
          ("unnumbered", 1))
    )


_NetConfigUnnumbered_Type.__name__ = "Integer32"
_NetConfigUnnumbered_Object = MibTableColumn
netConfigUnnumbered = _NetConfigUnnumbered_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 1, 1, 5),
    _NetConfigUnnumbered_Type()
)
netConfigUnnumbered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigUnnumbered.setStatus("current")
_NetConfigStatus_Type = RowStatus
_NetConfigStatus_Object = MibTableColumn
netConfigStatus = _NetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 1, 1, 6),
    _NetConfigStatus_Type()
)
netConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigStatus.setStatus("current")
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 2),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("current")
_IpHttpState_Type = EnabledStatus
_IpHttpState_Object = MibScalar
ipHttpState = _IpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 3),
    _IpHttpState_Type()
)
ipHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpState.setStatus("current")


class _IpHttpPort_Type(Integer32):
    """Custom type ipHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpHttpPort_Type.__name__ = "Integer32"
_IpHttpPort_Object = MibScalar
ipHttpPort = _IpHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 4),
    _IpHttpPort_Type()
)
ipHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpPort.setStatus("current")


class _IpDhcpRestart_Type(Integer32):
    """Custom type ipDhcpRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRestart", 2),
          ("restart", 1))
    )


_IpDhcpRestart_Type.__name__ = "Integer32"
_IpDhcpRestart_Object = MibScalar
ipDhcpRestart = _IpDhcpRestart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 5),
    _IpDhcpRestart_Type()
)
ipDhcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpRestart.setStatus("current")
_IpHttpsState_Type = EnabledStatus
_IpHttpsState_Object = MibScalar
ipHttpsState = _IpHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 6),
    _IpHttpsState_Type()
)
ipHttpsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsState.setStatus("current")


class _IpHttpsPort_Type(Integer32):
    """Custom type ipHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpHttpsPort_Type.__name__ = "Integer32"
_IpHttpsPort_Object = MibScalar
ipHttpsPort = _IpHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 10, 7),
    _IpHttpsPort_Type()
)
ipHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsPort.setStatus("current")
_BcastStormMgt_ObjectIdentity = ObjectIdentity
bcastStormMgt = _BcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 11)
)
_BcastStormTable_Object = MibTable
bcastStormTable = _BcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 11, 1)
)
if mibBuilder.loadTexts:
    bcastStormTable.setStatus("current")
_BcastStormEntry_Object = MibTableRow
bcastStormEntry = _BcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 11, 1, 1)
)
bcastStormEntry.setIndexNames(
    (0, "V2H124-24-MIB", "bcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    bcastStormEntry.setStatus("current")
_BcastStormIfIndex_Type = Integer32
_BcastStormIfIndex_Object = MibTableColumn
bcastStormIfIndex = _BcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 11, 1, 1, 1),
    _BcastStormIfIndex_Type()
)
bcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcastStormIfIndex.setStatus("current")
_BcastStormStatus_Type = EnabledStatus
_BcastStormStatus_Object = MibTableColumn
bcastStormStatus = _BcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 11, 1, 1, 2),
    _BcastStormStatus_Type()
)
bcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormStatus.setStatus("current")


class _BcastStormSampleType_Type(Integer32):
    """Custom type bcastStormSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("octet-rate", 2),
          ("percent", 3),
          ("pkt-rate", 1))
    )


_BcastStormSampleType_Type.__name__ = "Integer32"
_BcastStormSampleType_Object = MibTableColumn
bcastStormSampleType = _BcastStormSampleType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 11, 1, 1, 3),
    _BcastStormSampleType_Type()
)
bcastStormSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormSampleType.setStatus("current")
_BcastStormPktRate_Type = Integer32
_BcastStormPktRate_Object = MibTableColumn
bcastStormPktRate = _BcastStormPktRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 11, 1, 1, 4),
    _BcastStormPktRate_Type()
)
bcastStormPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormPktRate.setStatus("current")
_BcastStormOctetRate_Type = Integer32
_BcastStormOctetRate_Object = MibTableColumn
bcastStormOctetRate = _BcastStormOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 11, 1, 1, 5),
    _BcastStormOctetRate_Type()
)
bcastStormOctetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormOctetRate.setStatus("current")
_BcastStormPercent_Type = Integer32
_BcastStormPercent_Object = MibTableColumn
bcastStormPercent = _BcastStormPercent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 11, 1, 1, 6),
    _BcastStormPercent_Type()
)
bcastStormPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormPercent.setStatus("current")
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 12)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 12, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "V2H124-24-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIndex_Type = Unsigned32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 12, 1, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("current")


class _VlanAddressMethod_Type(Integer32):
    """Custom type vlanAddressMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("user", 1))
    )


_VlanAddressMethod_Type.__name__ = "Integer32"
_VlanAddressMethod_Object = MibTableColumn
vlanAddressMethod = _VlanAddressMethod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 12, 1, 1, 2),
    _VlanAddressMethod_Type()
)
vlanAddressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAddressMethod.setStatus("current")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 12, 2)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 12, 2, 1)
)
vlanPortEntry.setIndexNames(
    (0, "V2H124-24-MIB", "vlanPortIndex"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("current")
_VlanPortIndex_Type = Integer32
_VlanPortIndex_Object = MibTableColumn
vlanPortIndex = _VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 12, 2, 1, 1),
    _VlanPortIndex_Type()
)
vlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPortIndex.setStatus("current")


class _VlanPortMode_Type(Integer32):
    """Custom type vlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 3),
          ("dot1qTrunk", 2),
          ("hybrid", 1))
    )


_VlanPortMode_Type.__name__ = "Integer32"
_VlanPortMode_Object = MibTableColumn
vlanPortMode = _VlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 12, 2, 1, 2),
    _VlanPortMode_Type()
)
vlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMode.setStatus("current")
_PriorityMgt_ObjectIdentity = ObjectIdentity
priorityMgt = _PriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13)
)


class _PrioIpPrecDscpStatus_Type(Integer32):
    """Custom type prioIpPrecDscpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("dscp", 3),
          ("precedence", 2))
    )


_PrioIpPrecDscpStatus_Type.__name__ = "Integer32"
_PrioIpPrecDscpStatus_Object = MibScalar
prioIpPrecDscpStatus = _PrioIpPrecDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 1),
    _PrioIpPrecDscpStatus_Type()
)
prioIpPrecDscpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecDscpStatus.setStatus("current")
_PrioIpPrecTable_Object = MibTable
prioIpPrecTable = _PrioIpPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 2)
)
if mibBuilder.loadTexts:
    prioIpPrecTable.setStatus("current")
_PrioIpPrecEntry_Object = MibTableRow
prioIpPrecEntry = _PrioIpPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 2, 1)
)
prioIpPrecEntry.setIndexNames(
    (0, "V2H124-24-MIB", "prioIpPrecPort"),
    (0, "V2H124-24-MIB", "prioIpPrecValue"),
)
if mibBuilder.loadTexts:
    prioIpPrecEntry.setStatus("current")
_PrioIpPrecPort_Type = Integer32
_PrioIpPrecPort_Object = MibTableColumn
prioIpPrecPort = _PrioIpPrecPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 2, 1, 2),
    _PrioIpPrecPort_Type()
)
prioIpPrecPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPrecPort.setStatus("current")


class _PrioIpPrecValue_Type(Integer32):
    """Custom type prioIpPrecValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpPrecValue_Type.__name__ = "Integer32"
_PrioIpPrecValue_Object = MibTableColumn
prioIpPrecValue = _PrioIpPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 2, 1, 3),
    _PrioIpPrecValue_Type()
)
prioIpPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPrecValue.setStatus("current")


class _PrioIpPrecCos_Type(Integer32):
    """Custom type prioIpPrecCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpPrecCos_Type.__name__ = "Integer32"
_PrioIpPrecCos_Object = MibTableColumn
prioIpPrecCos = _PrioIpPrecCos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 2, 1, 4),
    _PrioIpPrecCos_Type()
)
prioIpPrecCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecCos.setStatus("current")
_PrioIpPrecRestoreDefault_Type = Integer32
_PrioIpPrecRestoreDefault_Object = MibScalar
prioIpPrecRestoreDefault = _PrioIpPrecRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 3),
    _PrioIpPrecRestoreDefault_Type()
)
prioIpPrecRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecRestoreDefault.setStatus("current")
_PrioIpDscpTable_Object = MibTable
prioIpDscpTable = _PrioIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 4)
)
if mibBuilder.loadTexts:
    prioIpDscpTable.setStatus("current")
_PrioIpDscpEntry_Object = MibTableRow
prioIpDscpEntry = _PrioIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 4, 1)
)
prioIpDscpEntry.setIndexNames(
    (0, "V2H124-24-MIB", "prioIpDscpPort"),
    (0, "V2H124-24-MIB", "prioIpDscpValue"),
)
if mibBuilder.loadTexts:
    prioIpDscpEntry.setStatus("current")
_PrioIpDscpPort_Type = Integer32
_PrioIpDscpPort_Object = MibTableColumn
prioIpDscpPort = _PrioIpDscpPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 4, 1, 1),
    _PrioIpDscpPort_Type()
)
prioIpDscpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpDscpPort.setStatus("current")


class _PrioIpDscpValue_Type(Integer32):
    """Custom type prioIpDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PrioIpDscpValue_Type.__name__ = "Integer32"
_PrioIpDscpValue_Object = MibTableColumn
prioIpDscpValue = _PrioIpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 4, 1, 2),
    _PrioIpDscpValue_Type()
)
prioIpDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpDscpValue.setStatus("current")


class _PrioIpDscpCos_Type(Integer32):
    """Custom type prioIpDscpCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpDscpCos_Type.__name__ = "Integer32"
_PrioIpDscpCos_Object = MibTableColumn
prioIpDscpCos = _PrioIpDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 4, 1, 3),
    _PrioIpDscpCos_Type()
)
prioIpDscpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpCos.setStatus("current")
_PrioIpDscpRestoreDefault_Type = Integer32
_PrioIpDscpRestoreDefault_Object = MibScalar
prioIpDscpRestoreDefault = _PrioIpDscpRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 5),
    _PrioIpDscpRestoreDefault_Type()
)
prioIpDscpRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpRestoreDefault.setStatus("current")
_PrioIpPortEnableStatus_Type = EnabledStatus
_PrioIpPortEnableStatus_Object = MibScalar
prioIpPortEnableStatus = _PrioIpPortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 6),
    _PrioIpPortEnableStatus_Type()
)
prioIpPortEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPortEnableStatus.setStatus("current")
_PrioIpPortTable_Object = MibTable
prioIpPortTable = _PrioIpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 7)
)
if mibBuilder.loadTexts:
    prioIpPortTable.setStatus("current")
_PrioIpPortEntry_Object = MibTableRow
prioIpPortEntry = _PrioIpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 7, 1)
)
prioIpPortEntry.setIndexNames(
    (0, "V2H124-24-MIB", "prioIpPortPhysPort"),
    (0, "V2H124-24-MIB", "prioIpPortValue"),
)
if mibBuilder.loadTexts:
    prioIpPortEntry.setStatus("current")
_PrioIpPortPhysPort_Type = Integer32
_PrioIpPortPhysPort_Object = MibTableColumn
prioIpPortPhysPort = _PrioIpPortPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 7, 1, 1),
    _PrioIpPortPhysPort_Type()
)
prioIpPortPhysPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPortPhysPort.setStatus("current")


class _PrioIpPortValue_Type(Integer32):
    """Custom type prioIpPortValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrioIpPortValue_Type.__name__ = "Integer32"
_PrioIpPortValue_Object = MibTableColumn
prioIpPortValue = _PrioIpPortValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 7, 1, 2),
    _PrioIpPortValue_Type()
)
prioIpPortValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPortValue.setStatus("current")


class _PrioIpPortCos_Type(Integer32):
    """Custom type prioIpPortCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpPortCos_Type.__name__ = "Integer32"
_PrioIpPortCos_Object = MibTableColumn
prioIpPortCos = _PrioIpPortCos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 7, 1, 3),
    _PrioIpPortCos_Type()
)
prioIpPortCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioIpPortCos.setStatus("current")
_PrioIpPortStatus_Type = ValidStatus
_PrioIpPortStatus_Object = MibTableColumn
prioIpPortStatus = _PrioIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 7, 1, 4),
    _PrioIpPortStatus_Type()
)
prioIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioIpPortStatus.setStatus("current")
_PrioCopy_ObjectIdentity = ObjectIdentity
prioCopy = _PrioCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 8)
)
_PrioCopyIpPrec_Type = OctetString
_PrioCopyIpPrec_Object = MibScalar
prioCopyIpPrec = _PrioCopyIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 8, 1),
    _PrioCopyIpPrec_Type()
)
prioCopyIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpPrec.setStatus("current")
_PrioCopyIpDscp_Type = OctetString
_PrioCopyIpDscp_Object = MibScalar
prioCopyIpDscp = _PrioCopyIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 8, 2),
    _PrioCopyIpDscp_Type()
)
prioCopyIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpDscp.setStatus("current")
_PrioCopyIpPort_Type = OctetString
_PrioCopyIpPort_Object = MibScalar
prioCopyIpPort = _PrioCopyIpPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 8, 3),
    _PrioCopyIpPort_Type()
)
prioCopyIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpPort.setStatus("current")
_PrioWrrTable_Object = MibTable
prioWrrTable = _PrioWrrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 9)
)
if mibBuilder.loadTexts:
    prioWrrTable.setStatus("current")
_PrioWrrEntry_Object = MibTableRow
prioWrrEntry = _PrioWrrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 9, 1)
)
prioWrrEntry.setIndexNames(
    (0, "V2H124-24-MIB", "prioWrrTrafficClass"),
)
if mibBuilder.loadTexts:
    prioWrrEntry.setStatus("current")


class _PrioWrrTrafficClass_Type(Integer32):
    """Custom type prioWrrTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioWrrTrafficClass_Type.__name__ = "Integer32"
_PrioWrrTrafficClass_Object = MibTableColumn
prioWrrTrafficClass = _PrioWrrTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 9, 1, 1),
    _PrioWrrTrafficClass_Type()
)
prioWrrTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioWrrTrafficClass.setStatus("current")


class _PrioWrrWeight_Type(Integer32):
    """Custom type prioWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrioWrrWeight_Type.__name__ = "Integer32"
_PrioWrrWeight_Object = MibTableColumn
prioWrrWeight = _PrioWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 13, 9, 1, 2),
    _PrioWrrWeight_Type()
)
prioWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioWrrWeight.setStatus("current")
_TrapDestMgt_ObjectIdentity = ObjectIdentity
trapDestMgt = _TrapDestMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 14)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("current")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 14, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "V2H124-24-MIB", "trapDestAddress"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("current")
_TrapDestAddress_Type = IpAddress
_TrapDestAddress_Object = MibTableColumn
trapDestAddress = _TrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 14, 1, 1, 1),
    _TrapDestAddress_Type()
)
trapDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDestAddress.setStatus("current")


class _TrapDestCommunity_Type(OctetString):
    """Custom type trapDestCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TrapDestCommunity_Type.__name__ = "OctetString"
_TrapDestCommunity_Object = MibTableColumn
trapDestCommunity = _TrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 14, 1, 1, 2),
    _TrapDestCommunity_Type()
)
trapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestCommunity.setStatus("current")
_TrapDestStatus_Type = ValidStatus
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 14, 1, 1, 3),
    _TrapDestStatus_Type()
)
trapDestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestStatus.setStatus("current")


class _TrapDestVersion_Type(Integer32):
    """Custom type trapDestVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_TrapDestVersion_Type.__name__ = "Integer32"
_TrapDestVersion_Object = MibTableColumn
trapDestVersion = _TrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 14, 1, 1, 4),
    _TrapDestVersion_Type()
)
trapDestVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestVersion.setStatus("current")
_QosMgt_ObjectIdentity = ObjectIdentity
qosMgt = _QosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16)
)
_RateLimitMgt_ObjectIdentity = ObjectIdentity
rateLimitMgt = _RateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 1)
)
_RateLimitStatus_Type = EnabledStatus
_RateLimitStatus_Object = MibScalar
rateLimitStatus = _RateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 1, 1),
    _RateLimitStatus_Type()
)
rateLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitStatus.setStatus("current")
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("current")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 1, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "V2H124-24-MIB", "rlPortIndex"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("current")
_RlPortIndex_Type = Integer32
_RlPortIndex_Object = MibTableColumn
rlPortIndex = _RlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 1, 2, 1, 1),
    _RlPortIndex_Type()
)
rlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortIndex.setStatus("current")
_RlPortInputLimit_Type = Integer32
_RlPortInputLimit_Object = MibTableColumn
rlPortInputLimit = _RlPortInputLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 1, 2, 1, 2),
    _RlPortInputLimit_Type()
)
rlPortInputLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputLimit.setStatus("current")
_RlPortOutputLimit_Type = Integer32
_RlPortOutputLimit_Object = MibTableColumn
rlPortOutputLimit = _RlPortOutputLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 1, 2, 1, 3),
    _RlPortOutputLimit_Type()
)
rlPortOutputLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputLimit.setStatus("current")
_RlPortInputStatus_Type = EnabledStatus
_RlPortInputStatus_Object = MibTableColumn
rlPortInputStatus = _RlPortInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 1, 2, 1, 6),
    _RlPortInputStatus_Type()
)
rlPortInputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputStatus.setStatus("current")
_RlPortOutputStatus_Type = EnabledStatus
_RlPortOutputStatus_Object = MibTableColumn
rlPortOutputStatus = _RlPortOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 1, 2, 1, 7),
    _RlPortOutputStatus_Type()
)
rlPortOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputStatus.setStatus("current")
_MarkerMgt_ObjectIdentity = ObjectIdentity
markerMgt = _MarkerMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2)
)
_MarkerTable_Object = MibTable
markerTable = _MarkerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    markerTable.setStatus("current")
_MarkerEntry_Object = MibTableRow
markerEntry = _MarkerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2, 1, 1)
)
markerEntry.setIndexNames(
    (0, "V2H124-24-MIB", "markerIfIndex"),
    (0, "V2H124-24-MIB", "markerAclName"),
)
if mibBuilder.loadTexts:
    markerEntry.setStatus("current")
_MarkerIfIndex_Type = Integer32
_MarkerIfIndex_Object = MibTableColumn
markerIfIndex = _MarkerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2, 1, 1, 1),
    _MarkerIfIndex_Type()
)
markerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    markerIfIndex.setStatus("current")


class _MarkerAclName_Type(DisplayString):
    """Custom type markerAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MarkerAclName_Type.__name__ = "DisplayString"
_MarkerAclName_Object = MibTableColumn
markerAclName = _MarkerAclName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2, 1, 1, 2),
    _MarkerAclName_Type()
)
markerAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    markerAclName.setStatus("current")


class _MarkerActionBitList_Type(Bits):
    """Custom type markerActionBitList based on Bits"""
    namedValues = NamedValues(
        *(("dscp", 0),
          ("precedence", 1),
          ("priority", 2))
    )

_MarkerActionBitList_Type.__name__ = "Bits"
_MarkerActionBitList_Object = MibTableColumn
markerActionBitList = _MarkerActionBitList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2, 1, 1, 3),
    _MarkerActionBitList_Type()
)
markerActionBitList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerActionBitList.setStatus("current")


class _MarkerDscp_Type(Integer32):
    """Custom type markerDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MarkerDscp_Type.__name__ = "Integer32"
_MarkerDscp_Object = MibTableColumn
markerDscp = _MarkerDscp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2, 1, 1, 4),
    _MarkerDscp_Type()
)
markerDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerDscp.setStatus("current")


class _MarkerPrecedence_Type(Integer32):
    """Custom type markerPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MarkerPrecedence_Type.__name__ = "Integer32"
_MarkerPrecedence_Object = MibTableColumn
markerPrecedence = _MarkerPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2, 1, 1, 5),
    _MarkerPrecedence_Type()
)
markerPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerPrecedence.setStatus("current")


class _MarkerPriority_Type(Integer32):
    """Custom type markerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MarkerPriority_Type.__name__ = "Integer32"
_MarkerPriority_Object = MibTableColumn
markerPriority = _MarkerPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2, 1, 1, 6),
    _MarkerPriority_Type()
)
markerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerPriority.setStatus("current")
_MarkerStatus_Type = RowStatus
_MarkerStatus_Object = MibTableColumn
markerStatus = _MarkerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 2, 1, 1, 7),
    _MarkerStatus_Type()
)
markerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerStatus.setStatus("current")
_CosMgt_ObjectIdentity = ObjectIdentity
cosMgt = _CosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 3)
)
_PrioAclToCosMappingTable_Object = MibTable
prioAclToCosMappingTable = _PrioAclToCosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    prioAclToCosMappingTable.setStatus("current")
_PrioAclToCosMappingEntry_Object = MibTableRow
prioAclToCosMappingEntry = _PrioAclToCosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 3, 1, 1)
)
prioAclToCosMappingEntry.setIndexNames(
    (0, "V2H124-24-MIB", "prioAclToCosMappingIfIndex"),
    (0, "V2H124-24-MIB", "prioAclToCosMappingAclName"),
)
if mibBuilder.loadTexts:
    prioAclToCosMappingEntry.setStatus("current")
_PrioAclToCosMappingIfIndex_Type = Integer32
_PrioAclToCosMappingIfIndex_Object = MibTableColumn
prioAclToCosMappingIfIndex = _PrioAclToCosMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 3, 1, 1, 1),
    _PrioAclToCosMappingIfIndex_Type()
)
prioAclToCosMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioAclToCosMappingIfIndex.setStatus("current")


class _PrioAclToCosMappingAclName_Type(DisplayString):
    """Custom type prioAclToCosMappingAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_PrioAclToCosMappingAclName_Type.__name__ = "DisplayString"
_PrioAclToCosMappingAclName_Object = MibTableColumn
prioAclToCosMappingAclName = _PrioAclToCosMappingAclName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 3, 1, 1, 2),
    _PrioAclToCosMappingAclName_Type()
)
prioAclToCosMappingAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioAclToCosMappingAclName.setStatus("current")


class _PrioAclToCosMappingCosValue_Type(Integer32):
    """Custom type prioAclToCosMappingCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioAclToCosMappingCosValue_Type.__name__ = "Integer32"
_PrioAclToCosMappingCosValue_Object = MibTableColumn
prioAclToCosMappingCosValue = _PrioAclToCosMappingCosValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 3, 1, 1, 3),
    _PrioAclToCosMappingCosValue_Type()
)
prioAclToCosMappingCosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioAclToCosMappingCosValue.setStatus("current")
_PrioAclToCosMappingStatus_Type = RowStatus
_PrioAclToCosMappingStatus_Object = MibTableColumn
prioAclToCosMappingStatus = _PrioAclToCosMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 16, 3, 1, 1, 4),
    _PrioAclToCosMappingStatus_Type()
)
prioAclToCosMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioAclToCosMappingStatus.setStatus("current")
_SecurityMgt_ObjectIdentity = ObjectIdentity
securityMgt = _SecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17)
)
_PortSecurityMgt_ObjectIdentity = ObjectIdentity
portSecurityMgt = _PortSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 2)
)
_PortSecPortTable_Object = MibTable
portSecPortTable = _PortSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    portSecPortTable.setStatus("current")
_PortSecPortEntry_Object = MibTableRow
portSecPortEntry = _PortSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 2, 1, 1)
)
portSecPortEntry.setIndexNames(
    (0, "V2H124-24-MIB", "portSecPortIndex"),
)
if mibBuilder.loadTexts:
    portSecPortEntry.setStatus("current")
_PortSecPortIndex_Type = Integer32
_PortSecPortIndex_Object = MibTableColumn
portSecPortIndex = _PortSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 2, 1, 1, 1),
    _PortSecPortIndex_Type()
)
portSecPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecPortIndex.setStatus("current")
_PortSecPortStatus_Type = EnabledStatus
_PortSecPortStatus_Object = MibTableColumn
portSecPortStatus = _PortSecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 2, 1, 1, 2),
    _PortSecPortStatus_Type()
)
portSecPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecPortStatus.setStatus("current")


class _PortSecAction_Type(Integer32):
    """Custom type portSecAction based on Integer32"""
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
        *(("none", 1),
          ("shutdown", 3),
          ("trap", 2),
          ("trapAndShutdown", 4))
    )


_PortSecAction_Type.__name__ = "Integer32"
_PortSecAction_Object = MibTableColumn
portSecAction = _PortSecAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 2, 1, 1, 3),
    _PortSecAction_Type()
)
portSecAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecAction.setStatus("current")


class _PortSecMaxMacCount_Type(Integer32):
    """Custom type portSecMaxMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_PortSecMaxMacCount_Type.__name__ = "Integer32"
_PortSecMaxMacCount_Object = MibTableColumn
portSecMaxMacCount = _PortSecMaxMacCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 2, 1, 1, 4),
    _PortSecMaxMacCount_Type()
)
portSecMaxMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMaxMacCount.setStatus("current")
_RadiusMgt_ObjectIdentity = ObjectIdentity
radiusMgt = _RadiusMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 4)
)
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibScalar
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 4, 1),
    _RadiusServerAddress_Type()
)
radiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerAddress.setStatus("current")


class _RadiusServerPortNumber_Type(Integer32):
    """Custom type radiusServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerPortNumber_Type.__name__ = "Integer32"
_RadiusServerPortNumber_Object = MibScalar
radiusServerPortNumber = _RadiusServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 4, 2),
    _RadiusServerPortNumber_Type()
)
radiusServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerPortNumber.setStatus("current")


class _RadiusServerKey_Type(DisplayString):
    """Custom type radiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RadiusServerKey_Type.__name__ = "DisplayString"
_RadiusServerKey_Object = MibScalar
radiusServerKey = _RadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 4, 3),
    _RadiusServerKey_Type()
)
radiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerKey.setStatus("current")


class _RadiusServerRetransmit_Type(Integer32):
    """Custom type radiusServerRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RadiusServerRetransmit_Type.__name__ = "Integer32"
_RadiusServerRetransmit_Object = MibScalar
radiusServerRetransmit = _RadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 4, 4),
    _RadiusServerRetransmit_Type()
)
radiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerRetransmit.setStatus("current")


class _RadiusServerTimeout_Type(Integer32):
    """Custom type radiusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerTimeout_Type.__name__ = "Integer32"
_RadiusServerTimeout_Object = MibScalar
radiusServerTimeout = _RadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 4, 5),
    _RadiusServerTimeout_Type()
)
radiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerTimeout.setStatus("current")
_TacacsMgt_ObjectIdentity = ObjectIdentity
tacacsMgt = _TacacsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 5)
)
_TacacsServerAddress_Type = IpAddress
_TacacsServerAddress_Object = MibScalar
tacacsServerAddress = _TacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 5, 1),
    _TacacsServerAddress_Type()
)
tacacsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerAddress.setStatus("current")


class _TacacsServerPortNumber_Type(Integer32):
    """Custom type tacacsServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsServerPortNumber_Type.__name__ = "Integer32"
_TacacsServerPortNumber_Object = MibScalar
tacacsServerPortNumber = _TacacsServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 5, 2),
    _TacacsServerPortNumber_Type()
)
tacacsServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerPortNumber.setStatus("current")


class _TacacsServerKey_Type(DisplayString):
    """Custom type tacacsServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TacacsServerKey_Type.__name__ = "DisplayString"
_TacacsServerKey_Object = MibScalar
tacacsServerKey = _TacacsServerKey_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 5, 3),
    _TacacsServerKey_Type()
)
tacacsServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerKey.setStatus("current")
_SshMgt_ObjectIdentity = ObjectIdentity
sshMgt = _SshMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6)
)
_SshServerStatus_Type = EnabledStatus
_SshServerStatus_Object = MibScalar
sshServerStatus = _SshServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 1),
    _SshServerStatus_Type()
)
sshServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerStatus.setStatus("current")
_SshServerMajorVersion_Type = Integer32
_SshServerMajorVersion_Object = MibScalar
sshServerMajorVersion = _SshServerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 2),
    _SshServerMajorVersion_Type()
)
sshServerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMajorVersion.setStatus("current")
_SshServerMinorVersion_Type = Integer32
_SshServerMinorVersion_Object = MibScalar
sshServerMinorVersion = _SshServerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 3),
    _SshServerMinorVersion_Type()
)
sshServerMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMinorVersion.setStatus("current")


class _SshTimeout_Type(Integer32):
    """Custom type sshTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SshTimeout_Type.__name__ = "Integer32"
_SshTimeout_Object = MibScalar
sshTimeout = _SshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 4),
    _SshTimeout_Type()
)
sshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshTimeout.setStatus("current")


class _SshAuthRetries_Type(Integer32):
    """Custom type sshAuthRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SshAuthRetries_Type.__name__ = "Integer32"
_SshAuthRetries_Object = MibScalar
sshAuthRetries = _SshAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 5),
    _SshAuthRetries_Type()
)
sshAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAuthRetries.setStatus("current")
_SshConnInfoTable_Object = MibTable
sshConnInfoTable = _SshConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 6)
)
if mibBuilder.loadTexts:
    sshConnInfoTable.setStatus("current")
_SshConnInfoEntry_Object = MibTableRow
sshConnInfoEntry = _SshConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 6, 1)
)
sshConnInfoEntry.setIndexNames(
    (0, "V2H124-24-MIB", "sshConnID"),
)
if mibBuilder.loadTexts:
    sshConnInfoEntry.setStatus("current")
_SshConnID_Type = Integer32
_SshConnID_Object = MibTableColumn
sshConnID = _SshConnID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 6, 1, 1),
    _SshConnID_Type()
)
sshConnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshConnID.setStatus("current")
_SshConnMajorVersion_Type = Integer32
_SshConnMajorVersion_Object = MibTableColumn
sshConnMajorVersion = _SshConnMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 6, 1, 2),
    _SshConnMajorVersion_Type()
)
sshConnMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMajorVersion.setStatus("current")
_SshConnMinorVersion_Type = Integer32
_SshConnMinorVersion_Object = MibTableColumn
sshConnMinorVersion = _SshConnMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 6, 1, 3),
    _SshConnMinorVersion_Type()
)
sshConnMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMinorVersion.setStatus("current")


class _SshConnEncryptionType_Type(Integer32):
    """Custom type sshConnEncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("none", 1),
          ("tribeDes", 3))
    )


_SshConnEncryptionType_Type.__name__ = "Integer32"
_SshConnEncryptionType_Object = MibTableColumn
sshConnEncryptionType = _SshConnEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 6, 1, 4),
    _SshConnEncryptionType_Type()
)
sshConnEncryptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnEncryptionType.setStatus("current")


class _SshConnStatus_Type(Integer32):
    """Custom type sshConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticationStart", 2),
          ("negotiationStart", 1),
          ("sessionStart", 3))
    )


_SshConnStatus_Type.__name__ = "Integer32"
_SshConnStatus_Object = MibTableColumn
sshConnStatus = _SshConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 6, 1, 5),
    _SshConnStatus_Type()
)
sshConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnStatus.setStatus("current")
_SshConnUserName_Type = OctetString
_SshConnUserName_Object = MibTableColumn
sshConnUserName = _SshConnUserName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 6, 1, 6),
    _SshConnUserName_Type()
)
sshConnUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnUserName.setStatus("current")


class _SshDisconnect_Type(Integer32):
    """Custom type sshDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 2),
          ("noDisconnect", 1))
    )


_SshDisconnect_Type.__name__ = "Integer32"
_SshDisconnect_Object = MibTableColumn
sshDisconnect = _SshDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 6, 6, 1, 7),
    _SshDisconnect_Type()
)
sshDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshDisconnect.setStatus("current")
_AclMgt_ObjectIdentity = ObjectIdentity
aclMgt = _AclMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7)
)
_AclIpAceTable_Object = MibTable
aclIpAceTable = _AclIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1)
)
if mibBuilder.loadTexts:
    aclIpAceTable.setStatus("current")
_AclIpAceEntry_Object = MibTableRow
aclIpAceEntry = _AclIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1)
)
aclIpAceEntry.setIndexNames(
    (0, "V2H124-24-MIB", "aclIpAceName"),
    (0, "V2H124-24-MIB", "aclIpAceIndex"),
)
if mibBuilder.loadTexts:
    aclIpAceEntry.setStatus("current")


class _AclIpAceName_Type(DisplayString):
    """Custom type aclIpAceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AclIpAceName_Type.__name__ = "DisplayString"
_AclIpAceName_Object = MibTableColumn
aclIpAceName = _AclIpAceName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 1),
    _AclIpAceName_Type()
)
aclIpAceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIpAceName.setStatus("current")


class _AclIpAceIndex_Type(Integer32):
    """Custom type aclIpAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AclIpAceIndex_Type.__name__ = "Integer32"
_AclIpAceIndex_Object = MibTableColumn
aclIpAceIndex = _AclIpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 2),
    _AclIpAceIndex_Type()
)
aclIpAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIpAceIndex.setStatus("current")


class _AclIpAcePrecedence_Type(Integer32):
    """Custom type aclIpAcePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclIpAcePrecedence_Type.__name__ = "Integer32"
_AclIpAcePrecedence_Object = MibTableColumn
aclIpAcePrecedence = _AclIpAcePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 3),
    _AclIpAcePrecedence_Type()
)
aclIpAcePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIpAcePrecedence.setStatus("current")


class _AclIpAceAction_Type(Integer32):
    """Custom type aclIpAceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AclIpAceAction_Type.__name__ = "Integer32"
_AclIpAceAction_Object = MibTableColumn
aclIpAceAction = _AclIpAceAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 4),
    _AclIpAceAction_Type()
)
aclIpAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceAction.setStatus("current")
_AclIpAceSourceIpAddr_Type = IpAddress
_AclIpAceSourceIpAddr_Object = MibTableColumn
aclIpAceSourceIpAddr = _AclIpAceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 5),
    _AclIpAceSourceIpAddr_Type()
)
aclIpAceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourceIpAddr.setStatus("current")
_AclIpAceSourceIpAddrBitmask_Type = IpAddress
_AclIpAceSourceIpAddrBitmask_Object = MibTableColumn
aclIpAceSourceIpAddrBitmask = _AclIpAceSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 6),
    _AclIpAceSourceIpAddrBitmask_Type()
)
aclIpAceSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourceIpAddrBitmask.setStatus("current")
_AclIpAceDestIpAddr_Type = IpAddress
_AclIpAceDestIpAddr_Object = MibTableColumn
aclIpAceDestIpAddr = _AclIpAceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 7),
    _AclIpAceDestIpAddr_Type()
)
aclIpAceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestIpAddr.setStatus("current")
_AclIpAceDestIpAddrBitmask_Type = IpAddress
_AclIpAceDestIpAddrBitmask_Object = MibTableColumn
aclIpAceDestIpAddrBitmask = _AclIpAceDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 8),
    _AclIpAceDestIpAddrBitmask_Type()
)
aclIpAceDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestIpAddrBitmask.setStatus("current")


class _AclIpAceProtocol_Type(Integer32):
    """Custom type aclIpAceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AclIpAceProtocol_Type.__name__ = "Integer32"
_AclIpAceProtocol_Object = MibTableColumn
aclIpAceProtocol = _AclIpAceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 9),
    _AclIpAceProtocol_Type()
)
aclIpAceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceProtocol.setStatus("current")


class _AclIpAcePrec_Type(Integer32):
    """Custom type aclIpAcePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AclIpAcePrec_Type.__name__ = "Integer32"
_AclIpAcePrec_Object = MibTableColumn
aclIpAcePrec = _AclIpAcePrec_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 10),
    _AclIpAcePrec_Type()
)
aclIpAcePrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAcePrec.setStatus("current")


class _AclIpAceTos_Type(Integer32):
    """Custom type aclIpAceTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AclIpAceTos_Type.__name__ = "Integer32"
_AclIpAceTos_Object = MibTableColumn
aclIpAceTos = _AclIpAceTos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 11),
    _AclIpAceTos_Type()
)
aclIpAceTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceTos.setStatus("current")


class _AclIpAceDscp_Type(Integer32):
    """Custom type aclIpAceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AclIpAceDscp_Type.__name__ = "Integer32"
_AclIpAceDscp_Object = MibTableColumn
aclIpAceDscp = _AclIpAceDscp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 12),
    _AclIpAceDscp_Type()
)
aclIpAceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDscp.setStatus("current")


class _AclIpAceSourcePortOp_Type(Integer32):
    """Custom type aclIpAceSourcePortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_AclIpAceSourcePortOp_Type.__name__ = "Integer32"
_AclIpAceSourcePortOp_Object = MibTableColumn
aclIpAceSourcePortOp = _AclIpAceSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 13),
    _AclIpAceSourcePortOp_Type()
)
aclIpAceSourcePortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourcePortOp.setStatus("current")


class _AclIpAceMinSourcePort_Type(Integer32):
    """Custom type aclIpAceMinSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMinSourcePort_Type.__name__ = "Integer32"
_AclIpAceMinSourcePort_Object = MibTableColumn
aclIpAceMinSourcePort = _AclIpAceMinSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 14),
    _AclIpAceMinSourcePort_Type()
)
aclIpAceMinSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMinSourcePort.setStatus("current")


class _AclIpAceMaxSourcePort_Type(Integer32):
    """Custom type aclIpAceMaxSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMaxSourcePort_Type.__name__ = "Integer32"
_AclIpAceMaxSourcePort_Object = MibTableColumn
aclIpAceMaxSourcePort = _AclIpAceMaxSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 15),
    _AclIpAceMaxSourcePort_Type()
)
aclIpAceMaxSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMaxSourcePort.setStatus("current")


class _AclIpAceSourcePortBitmask_Type(Integer32):
    """Custom type aclIpAceSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceSourcePortBitmask_Type.__name__ = "Integer32"
_AclIpAceSourcePortBitmask_Object = MibTableColumn
aclIpAceSourcePortBitmask = _AclIpAceSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 16),
    _AclIpAceSourcePortBitmask_Type()
)
aclIpAceSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourcePortBitmask.setStatus("current")


class _AclIpAceDestPortOp_Type(Integer32):
    """Custom type aclIpAceDestPortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_AclIpAceDestPortOp_Type.__name__ = "Integer32"
_AclIpAceDestPortOp_Object = MibTableColumn
aclIpAceDestPortOp = _AclIpAceDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 17),
    _AclIpAceDestPortOp_Type()
)
aclIpAceDestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestPortOp.setStatus("current")


class _AclIpAceMinDestPort_Type(Integer32):
    """Custom type aclIpAceMinDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMinDestPort_Type.__name__ = "Integer32"
_AclIpAceMinDestPort_Object = MibTableColumn
aclIpAceMinDestPort = _AclIpAceMinDestPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 18),
    _AclIpAceMinDestPort_Type()
)
aclIpAceMinDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMinDestPort.setStatus("current")


class _AclIpAceMaxDestPort_Type(Integer32):
    """Custom type aclIpAceMaxDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMaxDestPort_Type.__name__ = "Integer32"
_AclIpAceMaxDestPort_Object = MibTableColumn
aclIpAceMaxDestPort = _AclIpAceMaxDestPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 19),
    _AclIpAceMaxDestPort_Type()
)
aclIpAceMaxDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMaxDestPort.setStatus("current")


class _AclIpAceDestPortBitmask_Type(Integer32):
    """Custom type aclIpAceDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceDestPortBitmask_Type.__name__ = "Integer32"
_AclIpAceDestPortBitmask_Object = MibTableColumn
aclIpAceDestPortBitmask = _AclIpAceDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 20),
    _AclIpAceDestPortBitmask_Type()
)
aclIpAceDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestPortBitmask.setStatus("current")


class _AclIpAceControlCode_Type(Integer32):
    """Custom type aclIpAceControlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclIpAceControlCode_Type.__name__ = "Integer32"
_AclIpAceControlCode_Object = MibTableColumn
aclIpAceControlCode = _AclIpAceControlCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 21),
    _AclIpAceControlCode_Type()
)
aclIpAceControlCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceControlCode.setStatus("current")


class _AclIpAceControlCodeBitmask_Type(Integer32):
    """Custom type aclIpAceControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclIpAceControlCodeBitmask_Type.__name__ = "Integer32"
_AclIpAceControlCodeBitmask_Object = MibTableColumn
aclIpAceControlCodeBitmask = _AclIpAceControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 22),
    _AclIpAceControlCodeBitmask_Type()
)
aclIpAceControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceControlCodeBitmask.setStatus("current")
_AclIpAceStatus_Type = RowStatus
_AclIpAceStatus_Object = MibTableColumn
aclIpAceStatus = _AclIpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 1, 1, 23),
    _AclIpAceStatus_Type()
)
aclIpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceStatus.setStatus("current")
_AclMacAceTable_Object = MibTable
aclMacAceTable = _AclMacAceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2)
)
if mibBuilder.loadTexts:
    aclMacAceTable.setStatus("current")
_AclMacAceEntry_Object = MibTableRow
aclMacAceEntry = _AclMacAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1)
)
aclMacAceEntry.setIndexNames(
    (0, "V2H124-24-MIB", "aclMacAceName"),
    (0, "V2H124-24-MIB", "aclMacAceIndex"),
)
if mibBuilder.loadTexts:
    aclMacAceEntry.setStatus("current")


class _AclMacAceName_Type(DisplayString):
    """Custom type aclMacAceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AclMacAceName_Type.__name__ = "DisplayString"
_AclMacAceName_Object = MibTableColumn
aclMacAceName = _AclMacAceName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 1),
    _AclMacAceName_Type()
)
aclMacAceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacAceName.setStatus("current")


class _AclMacAceIndex_Type(Integer32):
    """Custom type aclMacAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AclMacAceIndex_Type.__name__ = "Integer32"
_AclMacAceIndex_Object = MibTableColumn
aclMacAceIndex = _AclMacAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 2),
    _AclMacAceIndex_Type()
)
aclMacAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacAceIndex.setStatus("current")


class _AclMacAcePrecedence_Type(Integer32):
    """Custom type aclMacAcePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclMacAcePrecedence_Type.__name__ = "Integer32"
_AclMacAcePrecedence_Object = MibTableColumn
aclMacAcePrecedence = _AclMacAcePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 3),
    _AclMacAcePrecedence_Type()
)
aclMacAcePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMacAcePrecedence.setStatus("current")


class _AclMacAceAction_Type(Integer32):
    """Custom type aclMacAceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AclMacAceAction_Type.__name__ = "Integer32"
_AclMacAceAction_Object = MibTableColumn
aclMacAceAction = _AclMacAceAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 4),
    _AclMacAceAction_Type()
)
aclMacAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceAction.setStatus("current")


class _AclMacAcePktformat_Type(Integer32):
    """Custom type aclMacAcePktformat based on Integer32"""
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
        *(("any", 1),
          ("tagged802Dot3", 5),
          ("tagggedEth2", 4),
          ("untagged-Eth2", 2),
          ("untagged802Dot3", 3))
    )


_AclMacAcePktformat_Type.__name__ = "Integer32"
_AclMacAcePktformat_Object = MibTableColumn
aclMacAcePktformat = _AclMacAcePktformat_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 5),
    _AclMacAcePktformat_Type()
)
aclMacAcePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAcePktformat.setStatus("current")


class _AclMacAceSourceMacAddr_Type(OctetString):
    """Custom type aclMacAceSourceMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclMacAceSourceMacAddr_Type.__name__ = "OctetString"
_AclMacAceSourceMacAddr_Object = MibTableColumn
aclMacAceSourceMacAddr = _AclMacAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 6),
    _AclMacAceSourceMacAddr_Type()
)
aclMacAceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceSourceMacAddr.setStatus("current")


class _AclMacAceSourceMacAddrBitmask_Type(OctetString):
    """Custom type aclMacAceSourceMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclMacAceSourceMacAddrBitmask_Type.__name__ = "OctetString"
_AclMacAceSourceMacAddrBitmask_Object = MibTableColumn
aclMacAceSourceMacAddrBitmask = _AclMacAceSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 7),
    _AclMacAceSourceMacAddrBitmask_Type()
)
aclMacAceSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceSourceMacAddrBitmask.setStatus("current")


class _AclMacAceDestMacAddr_Type(OctetString):
    """Custom type aclMacAceDestMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclMacAceDestMacAddr_Type.__name__ = "OctetString"
_AclMacAceDestMacAddr_Object = MibTableColumn
aclMacAceDestMacAddr = _AclMacAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 8),
    _AclMacAceDestMacAddr_Type()
)
aclMacAceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceDestMacAddr.setStatus("current")


class _AclMacAceDestMacAddrBitmask_Type(OctetString):
    """Custom type aclMacAceDestMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclMacAceDestMacAddrBitmask_Type.__name__ = "OctetString"
_AclMacAceDestMacAddrBitmask_Object = MibTableColumn
aclMacAceDestMacAddrBitmask = _AclMacAceDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 9),
    _AclMacAceDestMacAddrBitmask_Type()
)
aclMacAceDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceDestMacAddrBitmask.setStatus("current")


class _AclMacAceVidOp_Type(Integer32):
    """Custom type aclMacAceVidOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_AclMacAceVidOp_Type.__name__ = "Integer32"
_AclMacAceVidOp_Object = MibTableColumn
aclMacAceVidOp = _AclMacAceVidOp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 10),
    _AclMacAceVidOp_Type()
)
aclMacAceVidOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceVidOp.setStatus("current")


class _AclMacAceMinVid_Type(Integer32):
    """Custom type aclMacAceMinVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AclMacAceMinVid_Type.__name__ = "Integer32"
_AclMacAceMinVid_Object = MibTableColumn
aclMacAceMinVid = _AclMacAceMinVid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 11),
    _AclMacAceMinVid_Type()
)
aclMacAceMinVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMinVid.setStatus("current")


class _AclMacAceVidBitmask_Type(Integer32):
    """Custom type aclMacAceVidBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclMacAceVidBitmask_Type.__name__ = "Integer32"
_AclMacAceVidBitmask_Object = MibTableColumn
aclMacAceVidBitmask = _AclMacAceVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 12),
    _AclMacAceVidBitmask_Type()
)
aclMacAceVidBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceVidBitmask.setStatus("current")


class _AclMacAceMaxVid_Type(Integer32):
    """Custom type aclMacAceMaxVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AclMacAceMaxVid_Type.__name__ = "Integer32"
_AclMacAceMaxVid_Object = MibTableColumn
aclMacAceMaxVid = _AclMacAceMaxVid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 13),
    _AclMacAceMaxVid_Type()
)
aclMacAceMaxVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMaxVid.setStatus("current")


class _AclMacAceEtherTypeOp_Type(Integer32):
    """Custom type aclMacAceEtherTypeOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_AclMacAceEtherTypeOp_Type.__name__ = "Integer32"
_AclMacAceEtherTypeOp_Object = MibTableColumn
aclMacAceEtherTypeOp = _AclMacAceEtherTypeOp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 14),
    _AclMacAceEtherTypeOp_Type()
)
aclMacAceEtherTypeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceEtherTypeOp.setStatus("current")


class _AclMacAceEtherTypeBitmask_Type(Integer32):
    """Custom type aclMacAceEtherTypeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclMacAceEtherTypeBitmask_Type.__name__ = "Integer32"
_AclMacAceEtherTypeBitmask_Object = MibTableColumn
aclMacAceEtherTypeBitmask = _AclMacAceEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 15),
    _AclMacAceEtherTypeBitmask_Type()
)
aclMacAceEtherTypeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceEtherTypeBitmask.setStatus("current")


class _AclMacAceMinEtherType_Type(Integer32):
    """Custom type aclMacAceMinEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_AclMacAceMinEtherType_Type.__name__ = "Integer32"
_AclMacAceMinEtherType_Object = MibTableColumn
aclMacAceMinEtherType = _AclMacAceMinEtherType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 16),
    _AclMacAceMinEtherType_Type()
)
aclMacAceMinEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMinEtherType.setStatus("current")


class _AclMacAceMaxEtherType_Type(Integer32):
    """Custom type aclMacAceMaxEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_AclMacAceMaxEtherType_Type.__name__ = "Integer32"
_AclMacAceMaxEtherType_Object = MibTableColumn
aclMacAceMaxEtherType = _AclMacAceMaxEtherType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 17),
    _AclMacAceMaxEtherType_Type()
)
aclMacAceMaxEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMaxEtherType.setStatus("current")
_AclMacAceStatus_Type = RowStatus
_AclMacAceStatus_Object = MibTableColumn
aclMacAceStatus = _AclMacAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 2, 1, 18),
    _AclMacAceStatus_Type()
)
aclMacAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceStatus.setStatus("current")
_AclAclGroupTable_Object = MibTable
aclAclGroupTable = _AclAclGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 3)
)
if mibBuilder.loadTexts:
    aclAclGroupTable.setStatus("current")
_AclAclGroupEntry_Object = MibTableRow
aclAclGroupEntry = _AclAclGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 3, 1)
)
aclAclGroupEntry.setIndexNames(
    (0, "V2H124-24-MIB", "aclAclGroupIfIndex"),
)
if mibBuilder.loadTexts:
    aclAclGroupEntry.setStatus("current")
_AclAclGroupIfIndex_Type = Integer32
_AclAclGroupIfIndex_Object = MibTableColumn
aclAclGroupIfIndex = _AclAclGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 3, 1, 1),
    _AclAclGroupIfIndex_Type()
)
aclAclGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclAclGroupIfIndex.setStatus("current")


class _AclAclGroupIngressIpAcl_Type(DisplayString):
    """Custom type aclAclGroupIngressIpAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupIngressIpAcl_Type.__name__ = "DisplayString"
_AclAclGroupIngressIpAcl_Object = MibTableColumn
aclAclGroupIngressIpAcl = _AclAclGroupIngressIpAcl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 3, 1, 2),
    _AclAclGroupIngressIpAcl_Type()
)
aclAclGroupIngressIpAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupIngressIpAcl.setStatus("current")


class _AclAclGroupEgressIpAcl_Type(DisplayString):
    """Custom type aclAclGroupEgressIpAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupEgressIpAcl_Type.__name__ = "DisplayString"
_AclAclGroupEgressIpAcl_Object = MibTableColumn
aclAclGroupEgressIpAcl = _AclAclGroupEgressIpAcl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 3, 1, 3),
    _AclAclGroupEgressIpAcl_Type()
)
aclAclGroupEgressIpAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupEgressIpAcl.setStatus("current")


class _AclAclGroupIngressMacAcl_Type(DisplayString):
    """Custom type aclAclGroupIngressMacAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupIngressMacAcl_Type.__name__ = "DisplayString"
_AclAclGroupIngressMacAcl_Object = MibTableColumn
aclAclGroupIngressMacAcl = _AclAclGroupIngressMacAcl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 3, 1, 4),
    _AclAclGroupIngressMacAcl_Type()
)
aclAclGroupIngressMacAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupIngressMacAcl.setStatus("current")


class _AclAclGroupEgressMacAcl_Type(DisplayString):
    """Custom type aclAclGroupEgressMacAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupEgressMacAcl_Type.__name__ = "DisplayString"
_AclAclGroupEgressMacAcl_Object = MibTableColumn
aclAclGroupEgressMacAcl = _AclAclGroupEgressMacAcl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 3, 1, 5),
    _AclAclGroupEgressMacAcl_Type()
)
aclAclGroupEgressMacAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupEgressMacAcl.setStatus("current")
_AclIngressIpMaskTable_Object = MibTable
aclIngressIpMaskTable = _AclIngressIpMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4)
)
if mibBuilder.loadTexts:
    aclIngressIpMaskTable.setStatus("current")
_AclIngressIpMaskEntry_Object = MibTableRow
aclIngressIpMaskEntry = _AclIngressIpMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1)
)
aclIngressIpMaskEntry.setIndexNames(
    (0, "V2H124-24-MIB", "aclIngressIpMaskIndex"),
)
if mibBuilder.loadTexts:
    aclIngressIpMaskEntry.setStatus("current")


class _AclIngressIpMaskIndex_Type(Integer32):
    """Custom type aclIngressIpMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AclIngressIpMaskIndex_Type.__name__ = "Integer32"
_AclIngressIpMaskIndex_Object = MibTableColumn
aclIngressIpMaskIndex = _AclIngressIpMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 1),
    _AclIngressIpMaskIndex_Type()
)
aclIngressIpMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIngressIpMaskIndex.setStatus("current")


class _AclIngressIpMaskPrecedence_Type(Integer32):
    """Custom type aclIngressIpMaskPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclIngressIpMaskPrecedence_Type.__name__ = "Integer32"
_AclIngressIpMaskPrecedence_Object = MibTableColumn
aclIngressIpMaskPrecedence = _AclIngressIpMaskPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 2),
    _AclIngressIpMaskPrecedence_Type()
)
aclIngressIpMaskPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIngressIpMaskPrecedence.setStatus("current")
_AclIngressIpMaskIsEnableTos_Type = EnabledStatus
_AclIngressIpMaskIsEnableTos_Object = MibTableColumn
aclIngressIpMaskIsEnableTos = _AclIngressIpMaskIsEnableTos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 3),
    _AclIngressIpMaskIsEnableTos_Type()
)
aclIngressIpMaskIsEnableTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskIsEnableTos.setStatus("current")
_AclIngressIpMaskIsEnableDscp_Type = EnabledStatus
_AclIngressIpMaskIsEnableDscp_Object = MibTableColumn
aclIngressIpMaskIsEnableDscp = _AclIngressIpMaskIsEnableDscp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 4),
    _AclIngressIpMaskIsEnableDscp_Type()
)
aclIngressIpMaskIsEnableDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskIsEnableDscp.setStatus("current")
_AclIngressIpMaskIsEnablePrecedence_Type = EnabledStatus
_AclIngressIpMaskIsEnablePrecedence_Object = MibTableColumn
aclIngressIpMaskIsEnablePrecedence = _AclIngressIpMaskIsEnablePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 5),
    _AclIngressIpMaskIsEnablePrecedence_Type()
)
aclIngressIpMaskIsEnablePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskIsEnablePrecedence.setStatus("current")
_AclIngressIpMaskIsEnableProtocol_Type = EnabledStatus
_AclIngressIpMaskIsEnableProtocol_Object = MibTableColumn
aclIngressIpMaskIsEnableProtocol = _AclIngressIpMaskIsEnableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 6),
    _AclIngressIpMaskIsEnableProtocol_Type()
)
aclIngressIpMaskIsEnableProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskIsEnableProtocol.setStatus("current")


class _AclIngressIpMaskSourceIpAddrBitmask_Type(Unsigned32):
    """Custom type aclIngressIpMaskSourceIpAddrBitmask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AclIngressIpMaskSourceIpAddrBitmask_Type.__name__ = "Unsigned32"
_AclIngressIpMaskSourceIpAddrBitmask_Object = MibTableColumn
aclIngressIpMaskSourceIpAddrBitmask = _AclIngressIpMaskSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 7),
    _AclIngressIpMaskSourceIpAddrBitmask_Type()
)
aclIngressIpMaskSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskSourceIpAddrBitmask.setStatus("current")


class _AclIngressIpMaskDestIpAddrBitmask_Type(Unsigned32):
    """Custom type aclIngressIpMaskDestIpAddrBitmask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AclIngressIpMaskDestIpAddrBitmask_Type.__name__ = "Unsigned32"
_AclIngressIpMaskDestIpAddrBitmask_Object = MibTableColumn
aclIngressIpMaskDestIpAddrBitmask = _AclIngressIpMaskDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 8),
    _AclIngressIpMaskDestIpAddrBitmask_Type()
)
aclIngressIpMaskDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskDestIpAddrBitmask.setStatus("current")


class _AclIngressIpMaskSourcePortBitmask_Type(Integer32):
    """Custom type aclIngressIpMaskSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIngressIpMaskSourcePortBitmask_Type.__name__ = "Integer32"
_AclIngressIpMaskSourcePortBitmask_Object = MibTableColumn
aclIngressIpMaskSourcePortBitmask = _AclIngressIpMaskSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 9),
    _AclIngressIpMaskSourcePortBitmask_Type()
)
aclIngressIpMaskSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskSourcePortBitmask.setStatus("current")


class _AclIngressIpMaskDestPortBitmask_Type(Integer32):
    """Custom type aclIngressIpMaskDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIngressIpMaskDestPortBitmask_Type.__name__ = "Integer32"
_AclIngressIpMaskDestPortBitmask_Object = MibTableColumn
aclIngressIpMaskDestPortBitmask = _AclIngressIpMaskDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 10),
    _AclIngressIpMaskDestPortBitmask_Type()
)
aclIngressIpMaskDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskDestPortBitmask.setStatus("current")


class _AclIngressIpMaskControlCodeBitmask_Type(Integer32):
    """Custom type aclIngressIpMaskControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclIngressIpMaskControlCodeBitmask_Type.__name__ = "Integer32"
_AclIngressIpMaskControlCodeBitmask_Object = MibTableColumn
aclIngressIpMaskControlCodeBitmask = _AclIngressIpMaskControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 11),
    _AclIngressIpMaskControlCodeBitmask_Type()
)
aclIngressIpMaskControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskControlCodeBitmask.setStatus("current")
_AclIngressIpMaskStatus_Type = RowStatus
_AclIngressIpMaskStatus_Object = MibTableColumn
aclIngressIpMaskStatus = _AclIngressIpMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 4, 1, 12),
    _AclIngressIpMaskStatus_Type()
)
aclIngressIpMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskStatus.setStatus("current")
_AclEgressIpMaskTable_Object = MibTable
aclEgressIpMaskTable = _AclEgressIpMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5)
)
if mibBuilder.loadTexts:
    aclEgressIpMaskTable.setStatus("current")
_AclEgressIpMaskEntry_Object = MibTableRow
aclEgressIpMaskEntry = _AclEgressIpMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1)
)
aclEgressIpMaskEntry.setIndexNames(
    (0, "V2H124-24-MIB", "aclEgressIpMaskIndex"),
)
if mibBuilder.loadTexts:
    aclEgressIpMaskEntry.setStatus("current")


class _AclEgressIpMaskIndex_Type(Integer32):
    """Custom type aclEgressIpMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AclEgressIpMaskIndex_Type.__name__ = "Integer32"
_AclEgressIpMaskIndex_Object = MibTableColumn
aclEgressIpMaskIndex = _AclEgressIpMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 1),
    _AclEgressIpMaskIndex_Type()
)
aclEgressIpMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclEgressIpMaskIndex.setStatus("current")


class _AclEgressIpMaskPrecedence_Type(Integer32):
    """Custom type aclEgressIpMaskPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclEgressIpMaskPrecedence_Type.__name__ = "Integer32"
_AclEgressIpMaskPrecedence_Object = MibTableColumn
aclEgressIpMaskPrecedence = _AclEgressIpMaskPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 2),
    _AclEgressIpMaskPrecedence_Type()
)
aclEgressIpMaskPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclEgressIpMaskPrecedence.setStatus("current")
_AclEgressIpMaskIsEnableTos_Type = EnabledStatus
_AclEgressIpMaskIsEnableTos_Object = MibTableColumn
aclEgressIpMaskIsEnableTos = _AclEgressIpMaskIsEnableTos_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 3),
    _AclEgressIpMaskIsEnableTos_Type()
)
aclEgressIpMaskIsEnableTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskIsEnableTos.setStatus("current")
_AclEgressIpMaskIsEnableDscp_Type = EnabledStatus
_AclEgressIpMaskIsEnableDscp_Object = MibTableColumn
aclEgressIpMaskIsEnableDscp = _AclEgressIpMaskIsEnableDscp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 4),
    _AclEgressIpMaskIsEnableDscp_Type()
)
aclEgressIpMaskIsEnableDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskIsEnableDscp.setStatus("current")
_AclEgressIpMaskIsEnablePrecedence_Type = EnabledStatus
_AclEgressIpMaskIsEnablePrecedence_Object = MibTableColumn
aclEgressIpMaskIsEnablePrecedence = _AclEgressIpMaskIsEnablePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 5),
    _AclEgressIpMaskIsEnablePrecedence_Type()
)
aclEgressIpMaskIsEnablePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskIsEnablePrecedence.setStatus("current")
_AclEgressIpMaskIsEnableProtocol_Type = EnabledStatus
_AclEgressIpMaskIsEnableProtocol_Object = MibTableColumn
aclEgressIpMaskIsEnableProtocol = _AclEgressIpMaskIsEnableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 6),
    _AclEgressIpMaskIsEnableProtocol_Type()
)
aclEgressIpMaskIsEnableProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskIsEnableProtocol.setStatus("current")


class _AclEgressIpMaskSourceIpAddrBitmask_Type(Unsigned32):
    """Custom type aclEgressIpMaskSourceIpAddrBitmask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AclEgressIpMaskSourceIpAddrBitmask_Type.__name__ = "Unsigned32"
_AclEgressIpMaskSourceIpAddrBitmask_Object = MibTableColumn
aclEgressIpMaskSourceIpAddrBitmask = _AclEgressIpMaskSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 7),
    _AclEgressIpMaskSourceIpAddrBitmask_Type()
)
aclEgressIpMaskSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskSourceIpAddrBitmask.setStatus("current")


class _AclEgressIpMaskDestIpAddrBitmask_Type(Unsigned32):
    """Custom type aclEgressIpMaskDestIpAddrBitmask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AclEgressIpMaskDestIpAddrBitmask_Type.__name__ = "Unsigned32"
_AclEgressIpMaskDestIpAddrBitmask_Object = MibTableColumn
aclEgressIpMaskDestIpAddrBitmask = _AclEgressIpMaskDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 8),
    _AclEgressIpMaskDestIpAddrBitmask_Type()
)
aclEgressIpMaskDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskDestIpAddrBitmask.setStatus("current")


class _AclEgressIpMaskSourcePortBitmask_Type(Integer32):
    """Custom type aclEgressIpMaskSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclEgressIpMaskSourcePortBitmask_Type.__name__ = "Integer32"
_AclEgressIpMaskSourcePortBitmask_Object = MibTableColumn
aclEgressIpMaskSourcePortBitmask = _AclEgressIpMaskSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 9),
    _AclEgressIpMaskSourcePortBitmask_Type()
)
aclEgressIpMaskSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskSourcePortBitmask.setStatus("current")


class _AclEgressIpMaskDestPortBitmask_Type(Integer32):
    """Custom type aclEgressIpMaskDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclEgressIpMaskDestPortBitmask_Type.__name__ = "Integer32"
_AclEgressIpMaskDestPortBitmask_Object = MibTableColumn
aclEgressIpMaskDestPortBitmask = _AclEgressIpMaskDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 10),
    _AclEgressIpMaskDestPortBitmask_Type()
)
aclEgressIpMaskDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskDestPortBitmask.setStatus("current")


class _AclEgressIpMaskControlCodeBitmask_Type(Integer32):
    """Custom type aclEgressIpMaskControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclEgressIpMaskControlCodeBitmask_Type.__name__ = "Integer32"
_AclEgressIpMaskControlCodeBitmask_Object = MibTableColumn
aclEgressIpMaskControlCodeBitmask = _AclEgressIpMaskControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 11),
    _AclEgressIpMaskControlCodeBitmask_Type()
)
aclEgressIpMaskControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskControlCodeBitmask.setStatus("current")
_AclEgressIpMaskStatus_Type = RowStatus
_AclEgressIpMaskStatus_Object = MibTableColumn
aclEgressIpMaskStatus = _AclEgressIpMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 5, 1, 12),
    _AclEgressIpMaskStatus_Type()
)
aclEgressIpMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskStatus.setStatus("current")
_AclIngressMacMaskTable_Object = MibTable
aclIngressMacMaskTable = _AclIngressMacMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6)
)
if mibBuilder.loadTexts:
    aclIngressMacMaskTable.setStatus("current")
_AclIngressMacMaskEntry_Object = MibTableRow
aclIngressMacMaskEntry = _AclIngressMacMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6, 1)
)
aclIngressMacMaskEntry.setIndexNames(
    (0, "V2H124-24-MIB", "aclIngressMacMaskIndex"),
)
if mibBuilder.loadTexts:
    aclIngressMacMaskEntry.setStatus("current")


class _AclIngressMacMaskIndex_Type(Integer32):
    """Custom type aclIngressMacMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AclIngressMacMaskIndex_Type.__name__ = "Integer32"
_AclIngressMacMaskIndex_Object = MibTableColumn
aclIngressMacMaskIndex = _AclIngressMacMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6, 1, 1),
    _AclIngressMacMaskIndex_Type()
)
aclIngressMacMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIngressMacMaskIndex.setStatus("current")


class _AclIngressMacMaskPrecedence_Type(Integer32):
    """Custom type aclIngressMacMaskPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclIngressMacMaskPrecedence_Type.__name__ = "Integer32"
_AclIngressMacMaskPrecedence_Object = MibTableColumn
aclIngressMacMaskPrecedence = _AclIngressMacMaskPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6, 1, 2),
    _AclIngressMacMaskPrecedence_Type()
)
aclIngressMacMaskPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIngressMacMaskPrecedence.setStatus("current")


class _AclIngressMacMaskSourceMacAddrBitmask_Type(OctetString):
    """Custom type aclIngressMacMaskSourceMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclIngressMacMaskSourceMacAddrBitmask_Type.__name__ = "OctetString"
_AclIngressMacMaskSourceMacAddrBitmask_Object = MibTableColumn
aclIngressMacMaskSourceMacAddrBitmask = _AclIngressMacMaskSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6, 1, 3),
    _AclIngressMacMaskSourceMacAddrBitmask_Type()
)
aclIngressMacMaskSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskSourceMacAddrBitmask.setStatus("current")


class _AclIngressMacMaskDestMacAddrBitmask_Type(OctetString):
    """Custom type aclIngressMacMaskDestMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclIngressMacMaskDestMacAddrBitmask_Type.__name__ = "OctetString"
_AclIngressMacMaskDestMacAddrBitmask_Object = MibTableColumn
aclIngressMacMaskDestMacAddrBitmask = _AclIngressMacMaskDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6, 1, 4),
    _AclIngressMacMaskDestMacAddrBitmask_Type()
)
aclIngressMacMaskDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskDestMacAddrBitmask.setStatus("current")


class _AclIngressMacMaskVidBitmask_Type(Integer32):
    """Custom type aclIngressMacMaskVidBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclIngressMacMaskVidBitmask_Type.__name__ = "Integer32"
_AclIngressMacMaskVidBitmask_Object = MibTableColumn
aclIngressMacMaskVidBitmask = _AclIngressMacMaskVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6, 1, 5),
    _AclIngressMacMaskVidBitmask_Type()
)
aclIngressMacMaskVidBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskVidBitmask.setStatus("current")


class _AclIngressMacMaskEtherTypeBitmask_Type(Integer32):
    """Custom type aclIngressMacMaskEtherTypeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIngressMacMaskEtherTypeBitmask_Type.__name__ = "Integer32"
_AclIngressMacMaskEtherTypeBitmask_Object = MibTableColumn
aclIngressMacMaskEtherTypeBitmask = _AclIngressMacMaskEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6, 1, 6),
    _AclIngressMacMaskEtherTypeBitmask_Type()
)
aclIngressMacMaskEtherTypeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskEtherTypeBitmask.setStatus("current")
_AclIngressMacMaskIsEnablePktformat_Type = EnabledStatus
_AclIngressMacMaskIsEnablePktformat_Object = MibTableColumn
aclIngressMacMaskIsEnablePktformat = _AclIngressMacMaskIsEnablePktformat_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6, 1, 7),
    _AclIngressMacMaskIsEnablePktformat_Type()
)
aclIngressMacMaskIsEnablePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskIsEnablePktformat.setStatus("current")
_AclIngressMacMaskStatus_Type = RowStatus
_AclIngressMacMaskStatus_Object = MibTableColumn
aclIngressMacMaskStatus = _AclIngressMacMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 6, 1, 8),
    _AclIngressMacMaskStatus_Type()
)
aclIngressMacMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskStatus.setStatus("current")
_AclEgressMacMaskTable_Object = MibTable
aclEgressMacMaskTable = _AclEgressMacMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7)
)
if mibBuilder.loadTexts:
    aclEgressMacMaskTable.setStatus("current")
_AclEgressMacMaskEntry_Object = MibTableRow
aclEgressMacMaskEntry = _AclEgressMacMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7, 1)
)
aclEgressMacMaskEntry.setIndexNames(
    (0, "V2H124-24-MIB", "aclEgressMacMaskIndex"),
)
if mibBuilder.loadTexts:
    aclEgressMacMaskEntry.setStatus("current")


class _AclEgressMacMaskIndex_Type(Integer32):
    """Custom type aclEgressMacMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AclEgressMacMaskIndex_Type.__name__ = "Integer32"
_AclEgressMacMaskIndex_Object = MibTableColumn
aclEgressMacMaskIndex = _AclEgressMacMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7, 1, 1),
    _AclEgressMacMaskIndex_Type()
)
aclEgressMacMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclEgressMacMaskIndex.setStatus("current")


class _AclEgressMacMaskPrecedence_Type(Integer32):
    """Custom type aclEgressMacMaskPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclEgressMacMaskPrecedence_Type.__name__ = "Integer32"
_AclEgressMacMaskPrecedence_Object = MibTableColumn
aclEgressMacMaskPrecedence = _AclEgressMacMaskPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7, 1, 2),
    _AclEgressMacMaskPrecedence_Type()
)
aclEgressMacMaskPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclEgressMacMaskPrecedence.setStatus("current")


class _AclEgressMacMaskSourceMacAddrBitmask_Type(OctetString):
    """Custom type aclEgressMacMaskSourceMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclEgressMacMaskSourceMacAddrBitmask_Type.__name__ = "OctetString"
_AclEgressMacMaskSourceMacAddrBitmask_Object = MibTableColumn
aclEgressMacMaskSourceMacAddrBitmask = _AclEgressMacMaskSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7, 1, 3),
    _AclEgressMacMaskSourceMacAddrBitmask_Type()
)
aclEgressMacMaskSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskSourceMacAddrBitmask.setStatus("current")


class _AclEgressMacMaskDestMacAddrBitmask_Type(OctetString):
    """Custom type aclEgressMacMaskDestMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclEgressMacMaskDestMacAddrBitmask_Type.__name__ = "OctetString"
_AclEgressMacMaskDestMacAddrBitmask_Object = MibTableColumn
aclEgressMacMaskDestMacAddrBitmask = _AclEgressMacMaskDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7, 1, 4),
    _AclEgressMacMaskDestMacAddrBitmask_Type()
)
aclEgressMacMaskDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskDestMacAddrBitmask.setStatus("current")


class _AclEgressMacMaskVidBitmask_Type(Integer32):
    """Custom type aclEgressMacMaskVidBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclEgressMacMaskVidBitmask_Type.__name__ = "Integer32"
_AclEgressMacMaskVidBitmask_Object = MibTableColumn
aclEgressMacMaskVidBitmask = _AclEgressMacMaskVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7, 1, 5),
    _AclEgressMacMaskVidBitmask_Type()
)
aclEgressMacMaskVidBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskVidBitmask.setStatus("current")


class _AclEgressMacMaskEtherTypeBitmask_Type(Integer32):
    """Custom type aclEgressMacMaskEtherTypeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclEgressMacMaskEtherTypeBitmask_Type.__name__ = "Integer32"
_AclEgressMacMaskEtherTypeBitmask_Object = MibTableColumn
aclEgressMacMaskEtherTypeBitmask = _AclEgressMacMaskEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7, 1, 6),
    _AclEgressMacMaskEtherTypeBitmask_Type()
)
aclEgressMacMaskEtherTypeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskEtherTypeBitmask.setStatus("current")
_AclEgressMacMaskIsEnablePktformat_Type = EnabledStatus
_AclEgressMacMaskIsEnablePktformat_Object = MibTableColumn
aclEgressMacMaskIsEnablePktformat = _AclEgressMacMaskIsEnablePktformat_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7, 1, 7),
    _AclEgressMacMaskIsEnablePktformat_Type()
)
aclEgressMacMaskIsEnablePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskIsEnablePktformat.setStatus("current")
_AclEgressMacMaskStatus_Type = RowStatus
_AclEgressMacMaskStatus_Object = MibTableColumn
aclEgressMacMaskStatus = _AclEgressMacMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 17, 7, 7, 1, 8),
    _AclEgressMacMaskStatus_Type()
)
aclEgressMacMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskStatus.setStatus("current")
_SysLogMgt_ObjectIdentity = ObjectIdentity
sysLogMgt = _SysLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 19)
)
_SysLogStatus_Type = EnabledStatus
_SysLogStatus_Object = MibScalar
sysLogStatus = _SysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 19, 1),
    _SysLogStatus_Type()
)
sysLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogStatus.setStatus("current")


class _SysLogHistoryFlashLevel_Type(Integer32):
    """Custom type sysLogHistoryFlashLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SysLogHistoryFlashLevel_Type.__name__ = "Integer32"
_SysLogHistoryFlashLevel_Object = MibScalar
sysLogHistoryFlashLevel = _SysLogHistoryFlashLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 19, 2),
    _SysLogHistoryFlashLevel_Type()
)
sysLogHistoryFlashLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryFlashLevel.setStatus("current")


class _SysLogHistoryRamLevel_Type(Integer32):
    """Custom type sysLogHistoryRamLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SysLogHistoryRamLevel_Type.__name__ = "Integer32"
_SysLogHistoryRamLevel_Object = MibScalar
sysLogHistoryRamLevel = _SysLogHistoryRamLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 19, 3),
    _SysLogHistoryRamLevel_Type()
)
sysLogHistoryRamLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryRamLevel.setStatus("current")
_LineMgt_ObjectIdentity = ObjectIdentity
lineMgt = _LineMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20)
)
_ConsoleMgt_ObjectIdentity = ObjectIdentity
consoleMgt = _ConsoleMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 1)
)


class _ConsoleDataBits_Type(Integer32):
    """Custom type consoleDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databits7", 1),
          ("databits8", 2))
    )


_ConsoleDataBits_Type.__name__ = "Integer32"
_ConsoleDataBits_Object = MibScalar
consoleDataBits = _ConsoleDataBits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 1, 1),
    _ConsoleDataBits_Type()
)
consoleDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleDataBits.setStatus("current")


class _ConsoleParity_Type(Integer32):
    """Custom type consoleParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("partyEven", 2),
          ("partyNone", 1),
          ("partyOdd", 3))
    )


_ConsoleParity_Type.__name__ = "Integer32"
_ConsoleParity_Object = MibScalar
consoleParity = _ConsoleParity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 1, 2),
    _ConsoleParity_Type()
)
consoleParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleParity.setStatus("current")


class _ConsoleBaudRate_Type(Integer32):
    """Custom type consoleBaudRate based on Integer32"""
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
        *(("baudRate115200", 5),
          ("baudRate19200", 2),
          ("baudRate38400", 3),
          ("baudRate57600", 4),
          ("baudRate9600", 1))
    )


_ConsoleBaudRate_Type.__name__ = "Integer32"
_ConsoleBaudRate_Object = MibScalar
consoleBaudRate = _ConsoleBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 1, 3),
    _ConsoleBaudRate_Type()
)
consoleBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleBaudRate.setStatus("current")


class _ConsoleStopBits_Type(Integer32):
    """Custom type consoleStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stopbits1", 1),
          ("stopbits2", 2))
    )


_ConsoleStopBits_Type.__name__ = "Integer32"
_ConsoleStopBits_Object = MibScalar
consoleStopBits = _ConsoleStopBits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 1, 4),
    _ConsoleStopBits_Type()
)
consoleStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleStopBits.setStatus("current")


class _ConsoleExecTimeout_Type(Integer32):
    """Custom type consoleExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConsoleExecTimeout_Type.__name__ = "Integer32"
_ConsoleExecTimeout_Object = MibScalar
consoleExecTimeout = _ConsoleExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 1, 5),
    _ConsoleExecTimeout_Type()
)
consoleExecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleExecTimeout.setStatus("current")


class _ConsolePasswordThreshold_Type(Integer32):
    """Custom type consolePasswordThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_ConsolePasswordThreshold_Type.__name__ = "Integer32"
_ConsolePasswordThreshold_Object = MibScalar
consolePasswordThreshold = _ConsolePasswordThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 1, 6),
    _ConsolePasswordThreshold_Type()
)
consolePasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePasswordThreshold.setStatus("current")


class _ConsoleSilentTime_Type(Integer32):
    """Custom type consoleSilentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConsoleSilentTime_Type.__name__ = "Integer32"
_ConsoleSilentTime_Object = MibScalar
consoleSilentTime = _ConsoleSilentTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 1, 7),
    _ConsoleSilentTime_Type()
)
consoleSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleSilentTime.setStatus("current")
_TelnetMgt_ObjectIdentity = ObjectIdentity
telnetMgt = _TelnetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 2)
)


class _TelnetExecTimeout_Type(Integer32):
    """Custom type telnetExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetExecTimeout_Type.__name__ = "Integer32"
_TelnetExecTimeout_Object = MibScalar
telnetExecTimeout = _TelnetExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 2, 1),
    _TelnetExecTimeout_Type()
)
telnetExecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetExecTimeout.setStatus("current")


class _TelnetPasswordThreshold_Type(Integer32):
    """Custom type telnetPasswordThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_TelnetPasswordThreshold_Type.__name__ = "Integer32"
_TelnetPasswordThreshold_Object = MibScalar
telnetPasswordThreshold = _TelnetPasswordThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 20, 2, 2),
    _TelnetPasswordThreshold_Type()
)
telnetPasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPasswordThreshold.setStatus("current")
_SysTimeMgt_ObjectIdentity = ObjectIdentity
sysTimeMgt = _SysTimeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23)
)
_SntpMgt_ObjectIdentity = ObjectIdentity
sntpMgt = _SntpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 1)
)
_SntpStatus_Type = EnabledStatus
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 1, 1),
    _SntpStatus_Type()
)
sntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpStatus.setStatus("current")


class _SntpServiceMode_Type(Integer32):
    """Custom type sntpServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("anycast", 3),
          ("broadcast", 2),
          ("unicast", 1))
    )


_SntpServiceMode_Type.__name__ = "Integer32"
_SntpServiceMode_Object = MibScalar
sntpServiceMode = _SntpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 1, 2),
    _SntpServiceMode_Type()
)
sntpServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServiceMode.setStatus("current")


class _SntpPollInterval_Type(Integer32):
    """Custom type sntpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16384),
    )


_SntpPollInterval_Type.__name__ = "Integer32"
_SntpPollInterval_Object = MibScalar
sntpPollInterval = _SntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 1, 3),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 1, 4)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 1, 4, 1)
)
sntpServerEntry.setIndexNames(
    (0, "V2H124-24-MIB", "sntpServerIndex"),
)
if mibBuilder.loadTexts:
    sntpServerEntry.setStatus("current")


class _SntpServerIndex_Type(Integer32):
    """Custom type sntpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SntpServerIndex_Type.__name__ = "Integer32"
_SntpServerIndex_Object = MibTableColumn
sntpServerIndex = _SntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 1, 4, 1, 1),
    _SntpServerIndex_Type()
)
sntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sntpServerIndex.setStatus("current")
_SntpServerIpAddress_Type = IpAddress
_SntpServerIpAddress_Object = MibTableColumn
sntpServerIpAddress = _SntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 1, 4, 1, 2),
    _SntpServerIpAddress_Type()
)
sntpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerIpAddress.setStatus("current")


class _SysCurrentTime_Type(DisplayString):
    """Custom type sysCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SysCurrentTime_Type.__name__ = "DisplayString"
_SysCurrentTime_Object = MibScalar
sysCurrentTime = _SysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 2),
    _SysCurrentTime_Type()
)
sysCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCurrentTime.setStatus("current")


class _SysTimeZone_Type(DisplayString):
    """Custom type sysTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SysTimeZone_Type.__name__ = "DisplayString"
_SysTimeZone_Object = MibScalar
sysTimeZone = _SysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 3),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("current")


class _SysTimeZoneName_Type(DisplayString):
    """Custom type sysTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysTimeZoneName_Type.__name__ = "DisplayString"
_SysTimeZoneName_Object = MibScalar
sysTimeZoneName = _SysTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 23, 4),
    _SysTimeZoneName_Type()
)
sysTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZoneName.setStatus("current")
_FileMgt_ObjectIdentity = ObjectIdentity
fileMgt = _FileMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24)
)
_FileCopyMgt_ObjectIdentity = ObjectIdentity
fileCopyMgt = _FileCopyMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1)
)


class _FileCopySrcOperType_Type(Integer32):
    """Custom type fileCopySrcOperType based on Integer32"""
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
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5))
    )


_FileCopySrcOperType_Type.__name__ = "Integer32"
_FileCopySrcOperType_Object = MibScalar
fileCopySrcOperType = _FileCopySrcOperType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 1),
    _FileCopySrcOperType_Type()
)
fileCopySrcOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopySrcOperType.setStatus("current")


class _FileCopySrcFileName_Type(DisplayString):
    """Custom type fileCopySrcFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FileCopySrcFileName_Type.__name__ = "DisplayString"
_FileCopySrcFileName_Object = MibScalar
fileCopySrcFileName = _FileCopySrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 2),
    _FileCopySrcFileName_Type()
)
fileCopySrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopySrcFileName.setStatus("current")


class _FileCopyDestOperType_Type(Integer32):
    """Custom type fileCopyDestOperType based on Integer32"""
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
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5))
    )


_FileCopyDestOperType_Type.__name__ = "Integer32"
_FileCopyDestOperType_Object = MibScalar
fileCopyDestOperType = _FileCopyDestOperType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 3),
    _FileCopyDestOperType_Type()
)
fileCopyDestOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyDestOperType.setStatus("current")


class _FileCopyDestFileName_Type(DisplayString):
    """Custom type fileCopyDestFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FileCopyDestFileName_Type.__name__ = "DisplayString"
_FileCopyDestFileName_Object = MibScalar
fileCopyDestFileName = _FileCopyDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 4),
    _FileCopyDestFileName_Type()
)
fileCopyDestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyDestFileName.setStatus("current")


class _FileCopyFileType_Type(Integer32):
    """Custom type fileCopyFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootRom", 3),
          ("config", 2),
          ("opcode", 1))
    )


_FileCopyFileType_Type.__name__ = "Integer32"
_FileCopyFileType_Object = MibScalar
fileCopyFileType = _FileCopyFileType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 5),
    _FileCopyFileType_Type()
)
fileCopyFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyFileType.setStatus("current")
_FileCopyTftpServer_Type = IpAddress
_FileCopyTftpServer_Object = MibScalar
fileCopyTftpServer = _FileCopyTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 6),
    _FileCopyTftpServer_Type()
)
fileCopyTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyTftpServer.setStatus("current")
_FileCopyUnitId_Type = Integer32
_FileCopyUnitId_Object = MibScalar
fileCopyUnitId = _FileCopyUnitId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 7),
    _FileCopyUnitId_Type()
)
fileCopyUnitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyUnitId.setStatus("current")


class _FileCopyAction_Type(Integer32):
    """Custom type fileCopyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("notCopying", 1))
    )


_FileCopyAction_Type.__name__ = "Integer32"
_FileCopyAction_Object = MibScalar
fileCopyAction = _FileCopyAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 8),
    _FileCopyAction_Type()
)
fileCopyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyAction.setStatus("current")


class _FileCopyStatus_Type(Integer32):
    """Custom type fileCopyStatus based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("fileCopyBusy", 17),
          ("fileCopyCompleted", 31),
          ("fileCopyError", 29),
          ("fileCopyFileSizeExceed", 21),
          ("fileCopyHeaderChecksumError", 24),
          ("fileCopyImageChecksumError", 25),
          ("fileCopyImageTypeError", 23),
          ("fileCopyMagicWordError", 22),
          ("fileCopyParaError", 16),
          ("fileCopyReadFileError", 19),
          ("fileCopySetStartupError", 20),
          ("fileCopySuccess", 30),
          ("fileCopyTftpAccessViolation", 3),
          ("fileCopyTftpCompleted", 15),
          ("fileCopyTftpDiskFull", 4),
          ("fileCopyTftpFileExisted", 7),
          ("fileCopyTftpFileNotFound", 2),
          ("fileCopyTftpIllegalOperation", 5),
          ("fileCopyTftpNoSuchUser", 8),
          ("fileCopyTftpReceiverError", 11),
          ("fileCopyTftpSendError", 10),
          ("fileCopyTftpSocketBindError", 13),
          ("fileCopyTftpSocketOpenError", 12),
          ("fileCopyTftpTimeout", 9),
          ("fileCopyTftpUndefError", 1),
          ("fileCopyTftpUnkownTransferId", 6),
          ("fileCopyTftpUserCancel", 14),
          ("fileCopyUnknown", 18),
          ("fileCopyWriteFlashError", 27),
          ("fileCopyWriteFlashFinish", 26),
          ("fileCopyWriteFlashProgramming", 28))
    )


_FileCopyStatus_Type.__name__ = "Integer32"
_FileCopyStatus_Object = MibScalar
fileCopyStatus = _FileCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 9),
    _FileCopyStatus_Type()
)
fileCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyStatus.setStatus("current")


class _FileCopyTftpErrMsg_Type(DisplayString):
    """Custom type fileCopyTftpErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FileCopyTftpErrMsg_Type.__name__ = "DisplayString"
_FileCopyTftpErrMsg_Object = MibScalar
fileCopyTftpErrMsg = _FileCopyTftpErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 10),
    _FileCopyTftpErrMsg_Type()
)
fileCopyTftpErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyTftpErrMsg.setStatus("current")


class _FileCopyTftpServerHostName_Type(DisplayString):
    """Custom type fileCopyTftpServerHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FileCopyTftpServerHostName_Type.__name__ = "DisplayString"
_FileCopyTftpServerHostName_Object = MibScalar
fileCopyTftpServerHostName = _FileCopyTftpServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 1, 11),
    _FileCopyTftpServerHostName_Type()
)
fileCopyTftpServerHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyTftpServerHostName.setStatus("current")
_FileInfoMgt_ObjectIdentity = ObjectIdentity
fileInfoMgt = _FileInfoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2)
)
_FileInfoTable_Object = MibTable
fileInfoTable = _FileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    fileInfoTable.setStatus("current")
_FileInfoEntry_Object = MibTableRow
fileInfoEntry = _FileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2, 1, 1)
)
fileInfoEntry.setIndexNames(
    (0, "V2H124-24-MIB", "fileInfoUnitID"),
    (1, "V2H124-24-MIB", "fileInfoFileName"),
)
if mibBuilder.loadTexts:
    fileInfoEntry.setStatus("current")
_FileInfoUnitID_Type = Integer32
_FileInfoUnitID_Object = MibTableColumn
fileInfoUnitID = _FileInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2, 1, 1, 1),
    _FileInfoUnitID_Type()
)
fileInfoUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileInfoUnitID.setStatus("current")


class _FileInfoFileName_Type(DisplayString):
    """Custom type fileInfoFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FileInfoFileName_Type.__name__ = "DisplayString"
_FileInfoFileName_Object = MibTableColumn
fileInfoFileName = _FileInfoFileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2, 1, 1, 2),
    _FileInfoFileName_Type()
)
fileInfoFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileInfoFileName.setStatus("current")


class _FileInfoFileType_Type(Integer32):
    """Custom type fileInfoFileType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("certificate", 8),
          ("cmdlog", 4),
          ("config", 5),
          ("diag", 1),
          ("postlog", 6),
          ("private", 7),
          ("runtime", 2),
          ("syslog", 3),
          ("webarchive", 9))
    )


_FileInfoFileType_Type.__name__ = "Integer32"
_FileInfoFileType_Object = MibTableColumn
fileInfoFileType = _FileInfoFileType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2, 1, 1, 3),
    _FileInfoFileType_Type()
)
fileInfoFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileType.setStatus("current")
_FileInfoIsStartUp_Type = TruthValue
_FileInfoIsStartUp_Object = MibTableColumn
fileInfoIsStartUp = _FileInfoIsStartUp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2, 1, 1, 4),
    _FileInfoIsStartUp_Type()
)
fileInfoIsStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoIsStartUp.setStatus("current")
_FileInfoFileSize_Type = Integer32
_FileInfoFileSize_Object = MibTableColumn
fileInfoFileSize = _FileInfoFileSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2, 1, 1, 5),
    _FileInfoFileSize_Type()
)
fileInfoFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileSize.setStatus("current")


class _FileInfoCreationTime_Type(DisplayString):
    """Custom type fileInfoCreationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_FileInfoCreationTime_Type.__name__ = "DisplayString"
_FileInfoCreationTime_Object = MibTableColumn
fileInfoCreationTime = _FileInfoCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2, 1, 1, 6),
    _FileInfoCreationTime_Type()
)
fileInfoCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoCreationTime.setStatus("current")


class _FileInfoDelete_Type(Integer32):
    """Custom type fileInfoDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("noDelete", 1))
    )


_FileInfoDelete_Type.__name__ = "Integer32"
_FileInfoDelete_Object = MibTableColumn
fileInfoDelete = _FileInfoDelete_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 1, 24, 2, 1, 1, 7),
    _FileInfoDelete_Type()
)
fileInfoDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoDelete.setStatus("current")
_V2h124_24Notifications_ObjectIdentity = ObjectIdentity
v2h124_24Notifications = _V2h124_24Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 2)
)
_V2h124_24Traps_ObjectIdentity = ObjectIdentity
v2h124_24Traps = _V2h124_24Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 2, 1)
)
_V2h124_24TrapsPrefix_ObjectIdentity = ObjectIdentity
v2h124_24TrapsPrefix = _V2h124_24TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 2, 1, 0)
)
_V2h124_24Conformance_ObjectIdentity = ObjectIdentity
v2h124_24Conformance = _V2h124_24Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 3)
)
dot1dStpPortEntry.registerAugmentions(
    ("V2H124-24-MIB",
     "staPortEntry")
)
staPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

swPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52, 4, 12, 30, 2, 1, 0, 1)
)
swPowerStatusChangeTrap.setObjects(
      *(("V2H124-24-MIB", "swIndivPowerUnitIndex"),
        ("V2H124-24-MIB", "swIndivPowerIndex"),
        ("V2H124-24-MIB", "swIndivPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "V2H124-24-MIB",
    **{"ValidStatus": ValidStatus,
       "v2h124-24MIB": v2h124_24MIB,
       "v2h124-24MIBObjects": v2h124_24MIBObjects,
       "switchMgt": switchMgt,
       "switchManagementVlan": switchManagementVlan,
       "v2h124switchNumber": v2h124switchNumber,
       "v2h124switchInfoTable": v2h124switchInfoTable,
       "v2h124switchInfoEntry": v2h124switchInfoEntry,
       "v2h124swUnitIndex": v2h124swUnitIndex,
       "v2h124swHardwareVer": v2h124swHardwareVer,
       "v2h124swMicrocodeVer": v2h124swMicrocodeVer,
       "v2h124swLoaderVer": v2h124swLoaderVer,
       "v2h124swBootRomVer": v2h124swBootRomVer,
       "v2h124swOpCodeVer": v2h124swOpCodeVer,
       "v2h124swPortNumber": v2h124swPortNumber,
       "v2h124swPowerStatus": v2h124swPowerStatus,
       "v2h124swRoleInSystem": v2h124swRoleInSystem,
       "v2h124swSerialNumber": v2h124swSerialNumber,
       "v2h124swExpansionSlot1": v2h124swExpansionSlot1,
       "v2h124swExpansionSlot2": v2h124swExpansionSlot2,
       "v2h124swServiceTag": v2h124swServiceTag,
       "switchOperState": switchOperState,
       "switchProductId": switchProductId,
       "swProdName": swProdName,
       "swProdManufacturer": swProdManufacturer,
       "swProdDescription": swProdDescription,
       "swProdVersion": swProdVersion,
       "swProdUrl": swProdUrl,
       "swIdentifier": swIdentifier,
       "swChassisServiceTag": swChassisServiceTag,
       "switchIndivPowerTable": switchIndivPowerTable,
       "switchIndivPowerEntry": switchIndivPowerEntry,
       "swIndivPowerUnitIndex": swIndivPowerUnitIndex,
       "swIndivPowerIndex": swIndivPowerIndex,
       "swIndivPowerStatus": swIndivPowerStatus,
       "portMgt": portMgt,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portName": portName,
       "portType": portType,
       "portSpeedDpxCfg": portSpeedDpxCfg,
       "portFlowCtrlCfg": portFlowCtrlCfg,
       "portCapabilities": portCapabilities,
       "portAutonegotiation": portAutonegotiation,
       "portSpeedDpxStatus": portSpeedDpxStatus,
       "portFlowCtrlStatus": portFlowCtrlStatus,
       "portTrunkIndex": portTrunkIndex,
       "trunkMgt": trunkMgt,
       "trunkMaxId": trunkMaxId,
       "trunkValidNumber": trunkValidNumber,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkIndex": trunkIndex,
       "trunkPorts": trunkPorts,
       "trunkCreation": trunkCreation,
       "trunkStatus": trunkStatus,
       "lacpMgt": lacpMgt,
       "lacpPortTable": lacpPortTable,
       "lacpPortEntry": lacpPortEntry,
       "lacpPortIndex": lacpPortIndex,
       "lacpPortStatus": lacpPortStatus,
       "staMgt": staMgt,
       "staSystemStatus": staSystemStatus,
       "staPortTable": staPortTable,
       "staPortEntry": staPortEntry,
       "staPortFastForward": staPortFastForward,
       "staPortProtocolMigration": staPortProtocolMigration,
       "staPortAdminEdgePort": staPortAdminEdgePort,
       "staPortOperEdgePort": staPortOperEdgePort,
       "staPortAdminPointToPoint": staPortAdminPointToPoint,
       "staPortOperPointToPoint": staPortOperPointToPoint,
       "staPortLongPathCost": staPortLongPathCost,
       "staProtocolType": staProtocolType,
       "staTxHoldCount": staTxHoldCount,
       "staPathCostMethod": staPathCostMethod,
       "xstMgt": xstMgt,
       "xstInstanceCfgTable": xstInstanceCfgTable,
       "xstInstanceCfgEntry": xstInstanceCfgEntry,
       "xstInstanceCfgIndex": xstInstanceCfgIndex,
       "xstInstanceCfgPriority": xstInstanceCfgPriority,
       "xstInstanceCfgTimeSinceTopologyChange": xstInstanceCfgTimeSinceTopologyChange,
       "xstInstanceCfgTopChanges": xstInstanceCfgTopChanges,
       "xstInstanceCfgDesignatedRoot": xstInstanceCfgDesignatedRoot,
       "xstInstanceCfgRootCost": xstInstanceCfgRootCost,
       "xstInstanceCfgRootPort": xstInstanceCfgRootPort,
       "xstInstanceCfgMaxAge": xstInstanceCfgMaxAge,
       "xstInstanceCfgHelloTime": xstInstanceCfgHelloTime,
       "xstInstanceCfgHoldTime": xstInstanceCfgHoldTime,
       "xstInstanceCfgForwardDelay": xstInstanceCfgForwardDelay,
       "xstInstanceCfgBridgeMaxAge": xstInstanceCfgBridgeMaxAge,
       "xstInstanceCfgBridgeHelloTime": xstInstanceCfgBridgeHelloTime,
       "xstInstanceCfgBridgeForwardDelay": xstInstanceCfgBridgeForwardDelay,
       "xstInstanceCfgTxHoldCount": xstInstanceCfgTxHoldCount,
       "xstInstanceCfgPathCostMethod": xstInstanceCfgPathCostMethod,
       "xstInstancePortTable": xstInstancePortTable,
       "xstInstancePortEntry": xstInstancePortEntry,
       "xstInstancePortPriority": xstInstancePortPriority,
       "xstInstancePortState": xstInstancePortState,
       "xstInstancePortEnable": xstInstancePortEnable,
       "xstInstancePortPathCost": xstInstancePortPathCost,
       "xstInstancePortDesignatedRoot": xstInstancePortDesignatedRoot,
       "xstInstancePortDesignatedCost": xstInstancePortDesignatedCost,
       "xstInstancePortDesignatedBridge": xstInstancePortDesignatedBridge,
       "xstInstancePortDesignatedPort": xstInstancePortDesignatedPort,
       "xstInstancePortForwardTransitions": xstInstancePortForwardTransitions,
       "xstInstancePortPortRole": xstInstancePortPortRole,
       "restartMgt": restartMgt,
       "restartOpCodeFile": restartOpCodeFile,
       "restartConfigFile": restartConfigFile,
       "restartControl": restartControl,
       "mirrorMgt": mirrorMgt,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorDestinationPort": mirrorDestinationPort,
       "mirrorSourcePort": mirrorSourcePort,
       "mirrorType": mirrorType,
       "mirrorStatus": mirrorStatus,
       "igmpSnoopMgt": igmpSnoopMgt,
       "igmpSnoopStatus": igmpSnoopStatus,
       "igmpSnoopQuerier": igmpSnoopQuerier,
       "igmpSnoopQueryCount": igmpSnoopQueryCount,
       "igmpSnoopQueryInterval": igmpSnoopQueryInterval,
       "igmpSnoopQueryMaxResponseTime": igmpSnoopQueryMaxResponseTime,
       "igmpSnoopRouterPortExpireTime": igmpSnoopRouterPortExpireTime,
       "igmpSnoopVersion": igmpSnoopVersion,
       "igmpSnoopRouterCurrentTable": igmpSnoopRouterCurrentTable,
       "igmpSnoopRouterCurrentEntry": igmpSnoopRouterCurrentEntry,
       "igmpSnoopRouterCurrentVlanIndex": igmpSnoopRouterCurrentVlanIndex,
       "igmpSnoopRouterCurrentPorts": igmpSnoopRouterCurrentPorts,
       "igmpSnoopRouterCurrentStatus": igmpSnoopRouterCurrentStatus,
       "igmpSnoopRouterStaticTable": igmpSnoopRouterStaticTable,
       "igmpSnoopRouterStaticEntry": igmpSnoopRouterStaticEntry,
       "igmpSnoopRouterStaticVlanIndex": igmpSnoopRouterStaticVlanIndex,
       "igmpSnoopRouterStaticPorts": igmpSnoopRouterStaticPorts,
       "igmpSnoopRouterStaticStatus": igmpSnoopRouterStaticStatus,
       "igmpSnoopMulticastCurrentTable": igmpSnoopMulticastCurrentTable,
       "igmpSnoopMulticastCurrentEntry": igmpSnoopMulticastCurrentEntry,
       "igmpSnoopMulticastCurrentVlanIndex": igmpSnoopMulticastCurrentVlanIndex,
       "igmpSnoopMulticastCurrentIpAddress": igmpSnoopMulticastCurrentIpAddress,
       "igmpSnoopMulticastCurrentPorts": igmpSnoopMulticastCurrentPorts,
       "igmpSnoopMulticastCurrentStatus": igmpSnoopMulticastCurrentStatus,
       "igmpSnoopMulticastStaticTable": igmpSnoopMulticastStaticTable,
       "igmpSnoopMulticastStaticEntry": igmpSnoopMulticastStaticEntry,
       "igmpSnoopMulticastStaticVlanIndex": igmpSnoopMulticastStaticVlanIndex,
       "igmpSnoopMulticastStaticIpAddress": igmpSnoopMulticastStaticIpAddress,
       "igmpSnoopMulticastStaticPorts": igmpSnoopMulticastStaticPorts,
       "igmpSnoopMulticastStaticStatus": igmpSnoopMulticastStaticStatus,
       "ipMgt": ipMgt,
       "netConfigTable": netConfigTable,
       "netConfigEntry": netConfigEntry,
       "netConfigIfIndex": netConfigIfIndex,
       "netConfigIPAddress": netConfigIPAddress,
       "netConfigSubnetMask": netConfigSubnetMask,
       "netConfigPrimaryInterface": netConfigPrimaryInterface,
       "netConfigUnnumbered": netConfigUnnumbered,
       "netConfigStatus": netConfigStatus,
       "netDefaultGateway": netDefaultGateway,
       "ipHttpState": ipHttpState,
       "ipHttpPort": ipHttpPort,
       "ipDhcpRestart": ipDhcpRestart,
       "ipHttpsState": ipHttpsState,
       "ipHttpsPort": ipHttpsPort,
       "bcastStormMgt": bcastStormMgt,
       "bcastStormTable": bcastStormTable,
       "bcastStormEntry": bcastStormEntry,
       "bcastStormIfIndex": bcastStormIfIndex,
       "bcastStormStatus": bcastStormStatus,
       "bcastStormSampleType": bcastStormSampleType,
       "bcastStormPktRate": bcastStormPktRate,
       "bcastStormOctetRate": bcastStormOctetRate,
       "bcastStormPercent": bcastStormPercent,
       "vlanMgt": vlanMgt,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanAddressMethod": vlanAddressMethod,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortIndex": vlanPortIndex,
       "vlanPortMode": vlanPortMode,
       "priorityMgt": priorityMgt,
       "prioIpPrecDscpStatus": prioIpPrecDscpStatus,
       "prioIpPrecTable": prioIpPrecTable,
       "prioIpPrecEntry": prioIpPrecEntry,
       "prioIpPrecPort": prioIpPrecPort,
       "prioIpPrecValue": prioIpPrecValue,
       "prioIpPrecCos": prioIpPrecCos,
       "prioIpPrecRestoreDefault": prioIpPrecRestoreDefault,
       "prioIpDscpTable": prioIpDscpTable,
       "prioIpDscpEntry": prioIpDscpEntry,
       "prioIpDscpPort": prioIpDscpPort,
       "prioIpDscpValue": prioIpDscpValue,
       "prioIpDscpCos": prioIpDscpCos,
       "prioIpDscpRestoreDefault": prioIpDscpRestoreDefault,
       "prioIpPortEnableStatus": prioIpPortEnableStatus,
       "prioIpPortTable": prioIpPortTable,
       "prioIpPortEntry": prioIpPortEntry,
       "prioIpPortPhysPort": prioIpPortPhysPort,
       "prioIpPortValue": prioIpPortValue,
       "prioIpPortCos": prioIpPortCos,
       "prioIpPortStatus": prioIpPortStatus,
       "prioCopy": prioCopy,
       "prioCopyIpPrec": prioCopyIpPrec,
       "prioCopyIpDscp": prioCopyIpDscp,
       "prioCopyIpPort": prioCopyIpPort,
       "prioWrrTable": prioWrrTable,
       "prioWrrEntry": prioWrrEntry,
       "prioWrrTrafficClass": prioWrrTrafficClass,
       "prioWrrWeight": prioWrrWeight,
       "trapDestMgt": trapDestMgt,
       "trapDestTable": trapDestTable,
       "trapDestEntry": trapDestEntry,
       "trapDestAddress": trapDestAddress,
       "trapDestCommunity": trapDestCommunity,
       "trapDestStatus": trapDestStatus,
       "trapDestVersion": trapDestVersion,
       "qosMgt": qosMgt,
       "rateLimitMgt": rateLimitMgt,
       "rateLimitStatus": rateLimitStatus,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rlPortIndex": rlPortIndex,
       "rlPortInputLimit": rlPortInputLimit,
       "rlPortOutputLimit": rlPortOutputLimit,
       "rlPortInputStatus": rlPortInputStatus,
       "rlPortOutputStatus": rlPortOutputStatus,
       "markerMgt": markerMgt,
       "markerTable": markerTable,
       "markerEntry": markerEntry,
       "markerIfIndex": markerIfIndex,
       "markerAclName": markerAclName,
       "markerActionBitList": markerActionBitList,
       "markerDscp": markerDscp,
       "markerPrecedence": markerPrecedence,
       "markerPriority": markerPriority,
       "markerStatus": markerStatus,
       "cosMgt": cosMgt,
       "prioAclToCosMappingTable": prioAclToCosMappingTable,
       "prioAclToCosMappingEntry": prioAclToCosMappingEntry,
       "prioAclToCosMappingIfIndex": prioAclToCosMappingIfIndex,
       "prioAclToCosMappingAclName": prioAclToCosMappingAclName,
       "prioAclToCosMappingCosValue": prioAclToCosMappingCosValue,
       "prioAclToCosMappingStatus": prioAclToCosMappingStatus,
       "securityMgt": securityMgt,
       "portSecurityMgt": portSecurityMgt,
       "portSecPortTable": portSecPortTable,
       "portSecPortEntry": portSecPortEntry,
       "portSecPortIndex": portSecPortIndex,
       "portSecPortStatus": portSecPortStatus,
       "portSecAction": portSecAction,
       "portSecMaxMacCount": portSecMaxMacCount,
       "radiusMgt": radiusMgt,
       "radiusServerAddress": radiusServerAddress,
       "radiusServerPortNumber": radiusServerPortNumber,
       "radiusServerKey": radiusServerKey,
       "radiusServerRetransmit": radiusServerRetransmit,
       "radiusServerTimeout": radiusServerTimeout,
       "tacacsMgt": tacacsMgt,
       "tacacsServerAddress": tacacsServerAddress,
       "tacacsServerPortNumber": tacacsServerPortNumber,
       "tacacsServerKey": tacacsServerKey,
       "sshMgt": sshMgt,
       "sshServerStatus": sshServerStatus,
       "sshServerMajorVersion": sshServerMajorVersion,
       "sshServerMinorVersion": sshServerMinorVersion,
       "sshTimeout": sshTimeout,
       "sshAuthRetries": sshAuthRetries,
       "sshConnInfoTable": sshConnInfoTable,
       "sshConnInfoEntry": sshConnInfoEntry,
       "sshConnID": sshConnID,
       "sshConnMajorVersion": sshConnMajorVersion,
       "sshConnMinorVersion": sshConnMinorVersion,
       "sshConnEncryptionType": sshConnEncryptionType,
       "sshConnStatus": sshConnStatus,
       "sshConnUserName": sshConnUserName,
       "sshDisconnect": sshDisconnect,
       "aclMgt": aclMgt,
       "aclIpAceTable": aclIpAceTable,
       "aclIpAceEntry": aclIpAceEntry,
       "aclIpAceName": aclIpAceName,
       "aclIpAceIndex": aclIpAceIndex,
       "aclIpAcePrecedence": aclIpAcePrecedence,
       "aclIpAceAction": aclIpAceAction,
       "aclIpAceSourceIpAddr": aclIpAceSourceIpAddr,
       "aclIpAceSourceIpAddrBitmask": aclIpAceSourceIpAddrBitmask,
       "aclIpAceDestIpAddr": aclIpAceDestIpAddr,
       "aclIpAceDestIpAddrBitmask": aclIpAceDestIpAddrBitmask,
       "aclIpAceProtocol": aclIpAceProtocol,
       "aclIpAcePrec": aclIpAcePrec,
       "aclIpAceTos": aclIpAceTos,
       "aclIpAceDscp": aclIpAceDscp,
       "aclIpAceSourcePortOp": aclIpAceSourcePortOp,
       "aclIpAceMinSourcePort": aclIpAceMinSourcePort,
       "aclIpAceMaxSourcePort": aclIpAceMaxSourcePort,
       "aclIpAceSourcePortBitmask": aclIpAceSourcePortBitmask,
       "aclIpAceDestPortOp": aclIpAceDestPortOp,
       "aclIpAceMinDestPort": aclIpAceMinDestPort,
       "aclIpAceMaxDestPort": aclIpAceMaxDestPort,
       "aclIpAceDestPortBitmask": aclIpAceDestPortBitmask,
       "aclIpAceControlCode": aclIpAceControlCode,
       "aclIpAceControlCodeBitmask": aclIpAceControlCodeBitmask,
       "aclIpAceStatus": aclIpAceStatus,
       "aclMacAceTable": aclMacAceTable,
       "aclMacAceEntry": aclMacAceEntry,
       "aclMacAceName": aclMacAceName,
       "aclMacAceIndex": aclMacAceIndex,
       "aclMacAcePrecedence": aclMacAcePrecedence,
       "aclMacAceAction": aclMacAceAction,
       "aclMacAcePktformat": aclMacAcePktformat,
       "aclMacAceSourceMacAddr": aclMacAceSourceMacAddr,
       "aclMacAceSourceMacAddrBitmask": aclMacAceSourceMacAddrBitmask,
       "aclMacAceDestMacAddr": aclMacAceDestMacAddr,
       "aclMacAceDestMacAddrBitmask": aclMacAceDestMacAddrBitmask,
       "aclMacAceVidOp": aclMacAceVidOp,
       "aclMacAceMinVid": aclMacAceMinVid,
       "aclMacAceVidBitmask": aclMacAceVidBitmask,
       "aclMacAceMaxVid": aclMacAceMaxVid,
       "aclMacAceEtherTypeOp": aclMacAceEtherTypeOp,
       "aclMacAceEtherTypeBitmask": aclMacAceEtherTypeBitmask,
       "aclMacAceMinEtherType": aclMacAceMinEtherType,
       "aclMacAceMaxEtherType": aclMacAceMaxEtherType,
       "aclMacAceStatus": aclMacAceStatus,
       "aclAclGroupTable": aclAclGroupTable,
       "aclAclGroupEntry": aclAclGroupEntry,
       "aclAclGroupIfIndex": aclAclGroupIfIndex,
       "aclAclGroupIngressIpAcl": aclAclGroupIngressIpAcl,
       "aclAclGroupEgressIpAcl": aclAclGroupEgressIpAcl,
       "aclAclGroupIngressMacAcl": aclAclGroupIngressMacAcl,
       "aclAclGroupEgressMacAcl": aclAclGroupEgressMacAcl,
       "aclIngressIpMaskTable": aclIngressIpMaskTable,
       "aclIngressIpMaskEntry": aclIngressIpMaskEntry,
       "aclIngressIpMaskIndex": aclIngressIpMaskIndex,
       "aclIngressIpMaskPrecedence": aclIngressIpMaskPrecedence,
       "aclIngressIpMaskIsEnableTos": aclIngressIpMaskIsEnableTos,
       "aclIngressIpMaskIsEnableDscp": aclIngressIpMaskIsEnableDscp,
       "aclIngressIpMaskIsEnablePrecedence": aclIngressIpMaskIsEnablePrecedence,
       "aclIngressIpMaskIsEnableProtocol": aclIngressIpMaskIsEnableProtocol,
       "aclIngressIpMaskSourceIpAddrBitmask": aclIngressIpMaskSourceIpAddrBitmask,
       "aclIngressIpMaskDestIpAddrBitmask": aclIngressIpMaskDestIpAddrBitmask,
       "aclIngressIpMaskSourcePortBitmask": aclIngressIpMaskSourcePortBitmask,
       "aclIngressIpMaskDestPortBitmask": aclIngressIpMaskDestPortBitmask,
       "aclIngressIpMaskControlCodeBitmask": aclIngressIpMaskControlCodeBitmask,
       "aclIngressIpMaskStatus": aclIngressIpMaskStatus,
       "aclEgressIpMaskTable": aclEgressIpMaskTable,
       "aclEgressIpMaskEntry": aclEgressIpMaskEntry,
       "aclEgressIpMaskIndex": aclEgressIpMaskIndex,
       "aclEgressIpMaskPrecedence": aclEgressIpMaskPrecedence,
       "aclEgressIpMaskIsEnableTos": aclEgressIpMaskIsEnableTos,
       "aclEgressIpMaskIsEnableDscp": aclEgressIpMaskIsEnableDscp,
       "aclEgressIpMaskIsEnablePrecedence": aclEgressIpMaskIsEnablePrecedence,
       "aclEgressIpMaskIsEnableProtocol": aclEgressIpMaskIsEnableProtocol,
       "aclEgressIpMaskSourceIpAddrBitmask": aclEgressIpMaskSourceIpAddrBitmask,
       "aclEgressIpMaskDestIpAddrBitmask": aclEgressIpMaskDestIpAddrBitmask,
       "aclEgressIpMaskSourcePortBitmask": aclEgressIpMaskSourcePortBitmask,
       "aclEgressIpMaskDestPortBitmask": aclEgressIpMaskDestPortBitmask,
       "aclEgressIpMaskControlCodeBitmask": aclEgressIpMaskControlCodeBitmask,
       "aclEgressIpMaskStatus": aclEgressIpMaskStatus,
       "aclIngressMacMaskTable": aclIngressMacMaskTable,
       "aclIngressMacMaskEntry": aclIngressMacMaskEntry,
       "aclIngressMacMaskIndex": aclIngressMacMaskIndex,
       "aclIngressMacMaskPrecedence": aclIngressMacMaskPrecedence,
       "aclIngressMacMaskSourceMacAddrBitmask": aclIngressMacMaskSourceMacAddrBitmask,
       "aclIngressMacMaskDestMacAddrBitmask": aclIngressMacMaskDestMacAddrBitmask,
       "aclIngressMacMaskVidBitmask": aclIngressMacMaskVidBitmask,
       "aclIngressMacMaskEtherTypeBitmask": aclIngressMacMaskEtherTypeBitmask,
       "aclIngressMacMaskIsEnablePktformat": aclIngressMacMaskIsEnablePktformat,
       "aclIngressMacMaskStatus": aclIngressMacMaskStatus,
       "aclEgressMacMaskTable": aclEgressMacMaskTable,
       "aclEgressMacMaskEntry": aclEgressMacMaskEntry,
       "aclEgressMacMaskIndex": aclEgressMacMaskIndex,
       "aclEgressMacMaskPrecedence": aclEgressMacMaskPrecedence,
       "aclEgressMacMaskSourceMacAddrBitmask": aclEgressMacMaskSourceMacAddrBitmask,
       "aclEgressMacMaskDestMacAddrBitmask": aclEgressMacMaskDestMacAddrBitmask,
       "aclEgressMacMaskVidBitmask": aclEgressMacMaskVidBitmask,
       "aclEgressMacMaskEtherTypeBitmask": aclEgressMacMaskEtherTypeBitmask,
       "aclEgressMacMaskIsEnablePktformat": aclEgressMacMaskIsEnablePktformat,
       "aclEgressMacMaskStatus": aclEgressMacMaskStatus,
       "sysLogMgt": sysLogMgt,
       "sysLogStatus": sysLogStatus,
       "sysLogHistoryFlashLevel": sysLogHistoryFlashLevel,
       "sysLogHistoryRamLevel": sysLogHistoryRamLevel,
       "lineMgt": lineMgt,
       "consoleMgt": consoleMgt,
       "consoleDataBits": consoleDataBits,
       "consoleParity": consoleParity,
       "consoleBaudRate": consoleBaudRate,
       "consoleStopBits": consoleStopBits,
       "consoleExecTimeout": consoleExecTimeout,
       "consolePasswordThreshold": consolePasswordThreshold,
       "consoleSilentTime": consoleSilentTime,
       "telnetMgt": telnetMgt,
       "telnetExecTimeout": telnetExecTimeout,
       "telnetPasswordThreshold": telnetPasswordThreshold,
       "sysTimeMgt": sysTimeMgt,
       "sntpMgt": sntpMgt,
       "sntpStatus": sntpStatus,
       "sntpServiceMode": sntpServiceMode,
       "sntpPollInterval": sntpPollInterval,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerIndex": sntpServerIndex,
       "sntpServerIpAddress": sntpServerIpAddress,
       "sysCurrentTime": sysCurrentTime,
       "sysTimeZone": sysTimeZone,
       "sysTimeZoneName": sysTimeZoneName,
       "fileMgt": fileMgt,
       "fileCopyMgt": fileCopyMgt,
       "fileCopySrcOperType": fileCopySrcOperType,
       "fileCopySrcFileName": fileCopySrcFileName,
       "fileCopyDestOperType": fileCopyDestOperType,
       "fileCopyDestFileName": fileCopyDestFileName,
       "fileCopyFileType": fileCopyFileType,
       "fileCopyTftpServer": fileCopyTftpServer,
       "fileCopyUnitId": fileCopyUnitId,
       "fileCopyAction": fileCopyAction,
       "fileCopyStatus": fileCopyStatus,
       "fileCopyTftpErrMsg": fileCopyTftpErrMsg,
       "fileCopyTftpServerHostName": fileCopyTftpServerHostName,
       "fileInfoMgt": fileInfoMgt,
       "fileInfoTable": fileInfoTable,
       "fileInfoEntry": fileInfoEntry,
       "fileInfoUnitID": fileInfoUnitID,
       "fileInfoFileName": fileInfoFileName,
       "fileInfoFileType": fileInfoFileType,
       "fileInfoIsStartUp": fileInfoIsStartUp,
       "fileInfoFileSize": fileInfoFileSize,
       "fileInfoCreationTime": fileInfoCreationTime,
       "fileInfoDelete": fileInfoDelete,
       "v2h124-24Notifications": v2h124_24Notifications,
       "v2h124-24Traps": v2h124_24Traps,
       "v2h124-24TrapsPrefix": v2h124_24TrapsPrefix,
       "swPowerStatusChangeTrap": swPowerStatusChangeTrap,
       "v2h124-24Conformance": v2h124_24Conformance}
)
