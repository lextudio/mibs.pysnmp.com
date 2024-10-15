# SNMP MIB module (PowerConnect3248-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PowerConnect3248-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:31 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 internet,
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
    "internet",
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

powerConnect3248MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3)
)
powerConnect3248MIB.setRevisions(
        ("2001-09-06 00:00",)
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

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_DellLan_ObjectIdentity = ObjectIdentity
dellLan = _DellLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895)
)
_PowerConnect3248MIBObjects_ObjectIdentity = ObjectIdentity
powerConnect3248MIBObjects = _PowerConnect3248MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1)
)
_SwitchMgt_ObjectIdentity = ObjectIdentity
switchMgt = _SwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 1),
    _SwitchManagementVlan_Type()
)
switchManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchManagementVlan.setStatus("current")
_SwitchNumber_Type = Integer32
_SwitchNumber_Object = MibScalar
switchNumber = _SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 2),
    _SwitchNumber_Type()
)
switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumber.setStatus("current")
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1)
)
switchInfoEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")
_SwUnitIndex_Type = Integer32
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 1),
    _SwUnitIndex_Type()
)
swUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitIndex.setStatus("current")


class _SwHardwareVer_Type(DisplayString):
    """Custom type swHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwHardwareVer_Type.__name__ = "DisplayString"
_SwHardwareVer_Object = MibTableColumn
swHardwareVer = _SwHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 2),
    _SwHardwareVer_Type()
)
swHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareVer.setStatus("current")


class _SwMicrocodeVer_Type(DisplayString):
    """Custom type swMicrocodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwMicrocodeVer_Type.__name__ = "DisplayString"
_SwMicrocodeVer_Object = MibTableColumn
swMicrocodeVer = _SwMicrocodeVer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 3),
    _SwMicrocodeVer_Type()
)
swMicrocodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMicrocodeVer.setStatus("current")


class _SwLoaderVer_Type(DisplayString):
    """Custom type swLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwLoaderVer_Type.__name__ = "DisplayString"
_SwLoaderVer_Object = MibTableColumn
swLoaderVer = _SwLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 4),
    _SwLoaderVer_Type()
)
swLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLoaderVer.setStatus("current")


class _SwBootRomVer_Type(DisplayString):
    """Custom type swBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBootRomVer_Type.__name__ = "DisplayString"
_SwBootRomVer_Object = MibTableColumn
swBootRomVer = _SwBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 5),
    _SwBootRomVer_Type()
)
swBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootRomVer.setStatus("current")


class _SwOpCodeVer_Type(DisplayString):
    """Custom type swOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwOpCodeVer_Type.__name__ = "DisplayString"
_SwOpCodeVer_Object = MibTableColumn
swOpCodeVer = _SwOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 6),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("current")
_SwPortNumber_Type = Integer32
_SwPortNumber_Object = MibTableColumn
swPortNumber = _SwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 7),
    _SwPortNumber_Type()
)
swPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortNumber.setStatus("current")


class _SwPowerStatus_Type(Integer32):
    """Custom type swPowerStatus based on Integer32"""
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


_SwPowerStatus_Type.__name__ = "Integer32"
_SwPowerStatus_Object = MibTableColumn
swPowerStatus = _SwPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 8),
    _SwPowerStatus_Type()
)
swPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerStatus.setStatus("current")


class _SwRoleInSystem_Type(Integer32):
    """Custom type swRoleInSystem based on Integer32"""
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


_SwRoleInSystem_Type.__name__ = "Integer32"
_SwRoleInSystem_Object = MibTableColumn
swRoleInSystem = _SwRoleInSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 9),
    _SwRoleInSystem_Type()
)
swRoleInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRoleInSystem.setStatus("current")


class _SwSerialNumber_Type(DisplayString):
    """Custom type swSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwSerialNumber_Type.__name__ = "DisplayString"
_SwSerialNumber_Object = MibTableColumn
swSerialNumber = _SwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 10),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")


class _SwExpansionSlot1_Type(Integer32):
    """Custom type swExpansionSlot1 based on Integer32"""
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
        *(("hundredBaseFxMtrjMmf", 5),
          ("hundredBaseFxScMmf", 3),
          ("hundredBaseFxScSmf", 4),
          ("notPresent", 1),
          ("other", 2),
          ("stackingModule", 11),
          ("thousandBaseLxScSmf", 9),
          ("thousandBaseSfp", 12),
          ("thousandBaseSxMtrjMmf", 7),
          ("thousandBaseSxScMmf", 6),
          ("thousandBaseT", 10),
          ("thousandBaseXGbic", 8))
    )


_SwExpansionSlot1_Type.__name__ = "Integer32"
_SwExpansionSlot1_Object = MibTableColumn
swExpansionSlot1 = _SwExpansionSlot1_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 11),
    _SwExpansionSlot1_Type()
)
swExpansionSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExpansionSlot1.setStatus("current")


class _SwExpansionSlot2_Type(Integer32):
    """Custom type swExpansionSlot2 based on Integer32"""
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
        *(("hundredBaseFxMtrjMmf", 5),
          ("hundredBaseFxScMmf", 3),
          ("hundredBaseFxScSmf", 4),
          ("notPresent", 1),
          ("other", 2),
          ("stackingModule", 11),
          ("thousandBaseLxScSmf", 9),
          ("thousandBaseSfp", 12),
          ("thousandBaseSxMtrjMmf", 7),
          ("thousandBaseSxScMmf", 6),
          ("thousandBaseT", 10),
          ("thousandBaseXGbic", 8))
    )


_SwExpansionSlot2_Type.__name__ = "Integer32"
_SwExpansionSlot2_Object = MibTableColumn
swExpansionSlot2 = _SwExpansionSlot2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 12),
    _SwExpansionSlot2_Type()
)
swExpansionSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExpansionSlot2.setStatus("current")


class _SwServiceTag_Type(DisplayString):
    """Custom type swServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwServiceTag_Type.__name__ = "DisplayString"
_SwServiceTag_Object = MibTableColumn
swServiceTag = _SwServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 3, 1, 13),
    _SwServiceTag_Type()
)
swServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swServiceTag.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 4),
    _SwitchOperState_Type()
)
switchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOperState.setStatus("current")
_SwitchProductId_ObjectIdentity = ObjectIdentity
switchProductId = _SwitchProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 5, 5),
    _SwProdUrl_Type()
)
swProdUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdUrl.setStatus("current")
_SwIdentifier_Type = Integer32
_SwIdentifier_Object = MibScalar
swIdentifier = _SwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 5, 6),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 5, 7),
    _SwChassisServiceTag_Type()
)
swChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swChassisServiceTag.setStatus("current")
_SwitchIndivPowerTable_Object = MibTable
switchIndivPowerTable = _SwitchIndivPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    switchIndivPowerTable.setStatus("current")
_SwitchIndivPowerEntry_Object = MibTableRow
switchIndivPowerEntry = _SwitchIndivPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 6, 1)
)
switchIndivPowerEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "swIndivPowerUnitIndex"),
    (0, "PowerConnect3248-MIB", "swIndivPowerIndex"),
)
if mibBuilder.loadTexts:
    switchIndivPowerEntry.setStatus("current")
_SwIndivPowerUnitIndex_Type = Integer32
_SwIndivPowerUnitIndex_Object = MibTableColumn
swIndivPowerUnitIndex = _SwIndivPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 6, 1, 1),
    _SwIndivPowerUnitIndex_Type()
)
swIndivPowerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivPowerUnitIndex.setStatus("current")


class _SwIndivPowerIndex_Type(Integer32):
    """Custom type swIndivPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SwIndivPowerIndex_Type.__name__ = "Integer32"
_SwIndivPowerIndex_Object = MibTableColumn
swIndivPowerIndex = _SwIndivPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 6, 1, 2),
    _SwIndivPowerIndex_Type()
)
swIndivPowerIndex.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 1, 6, 1, 3),
    _SwIndivPowerStatus_Type()
)
swIndivPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivPowerStatus.setStatus("current")
_PortMgt_ObjectIdentity = ObjectIdentity
portMgt = _PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1)
)
portEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 2),
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("hundredBaseFX", 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")


class _PortAutonegotiation_Type(Integer32):
    """Custom type portAutonegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PortAutonegotiation_Type.__name__ = "Integer32"
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_PortTrunkIndex_Type = Integer32
_PortTrunkIndex_Object = MibTableColumn
portTrunkIndex = _PortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 2, 1, 1, 10),
    _PortTrunkIndex_Type()
)
portTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkIndex.setStatus("current")
_TrunkMgt_ObjectIdentity = ObjectIdentity
trunkMgt = _TrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 3)
)
_TrunkMaxId_Type = Integer32
_TrunkMaxId_Object = MibScalar
trunkMaxId = _TrunkMaxId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 3, 1),
    _TrunkMaxId_Type()
)
trunkMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMaxId.setStatus("current")
_TrunkValidNumber_Type = Integer32
_TrunkValidNumber_Object = MibScalar
trunkValidNumber = _TrunkValidNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 3, 2),
    _TrunkValidNumber_Type()
)
trunkValidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkValidNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 3, 3, 1)
)
trunkEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 3, 3, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 3, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 3, 3, 1, 3),
    _TrunkCreation_Type()
)
trunkCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCreation.setStatus("current")


class _TrunkStatus_Type(Integer32):
    """Custom type trunkStatus based on Integer32"""
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


_TrunkStatus_Type.__name__ = "Integer32"
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 3, 3, 1, 4),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_LacpMgt_ObjectIdentity = ObjectIdentity
lacpMgt = _LacpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 4)
)
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 4, 1, 1)
)
lacpPortEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")
_LacpPortIndex_Type = Integer32
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 4, 1, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")


class _LacpPortStatus_Type(Integer32):
    """Custom type lacpPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_LacpPortStatus_Type.__name__ = "Integer32"
_LacpPortStatus_Object = MibTableColumn
lacpPortStatus = _LacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 4, 1, 1, 2),
    _LacpPortStatus_Type()
)
lacpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortStatus.setStatus("current")
_StaMgt_ObjectIdentity = ObjectIdentity
staMgt = _StaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5)
)


class _StaSystemStatus_Type(EnabledStatus):
    """Custom type staSystemStatus based on EnabledStatus"""


_StaSystemStatus_Object = MibScalar
staSystemStatus = _StaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 1),
    _StaSystemStatus_Type()
)
staSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemStatus.setStatus("current")
_StaPortTable_Object = MibTable
staPortTable = _StaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2)
)
if mibBuilder.loadTexts:
    staPortTable.setStatus("current")
_StaPortEntry_Object = MibTableRow
staPortEntry = _StaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2, 1)
)
staPortEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "staPortIndex"),
)
if mibBuilder.loadTexts:
    staPortEntry.setStatus("current")
_StaPortIndex_Type = Integer32
_StaPortIndex_Object = MibTableColumn
staPortIndex = _StaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2, 1, 1),
    _StaPortIndex_Type()
)
staPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortIndex.setStatus("current")
_StaPortFastForward_Type = EnabledStatus
_StaPortFastForward_Object = MibTableColumn
staPortFastForward = _StaPortFastForward_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2, 1, 2),
    _StaPortFastForward_Type()
)
staPortFastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortFastForward.setStatus("current")
_StaPortProtocolMigration_Type = TruthValue
_StaPortProtocolMigration_Object = MibTableColumn
staPortProtocolMigration = _StaPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2, 1, 3),
    _StaPortProtocolMigration_Type()
)
staPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortProtocolMigration.setStatus("current")
_StaPortAdminEdgePort_Type = TruthValue
_StaPortAdminEdgePort_Object = MibTableColumn
staPortAdminEdgePort = _StaPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2, 1, 4),
    _StaPortAdminEdgePort_Type()
)
staPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminEdgePort.setStatus("current")
_StaPortOperEdgePort_Type = TruthValue
_StaPortOperEdgePort_Object = MibTableColumn
staPortOperEdgePort = _StaPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2, 1, 6),
    _StaPortAdminPointToPoint_Type()
)
staPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminPointToPoint.setStatus("current")
_StaPortOperPointToPoint_Type = TruthValue
_StaPortOperPointToPoint_Object = MibTableColumn
staPortOperPointToPoint = _StaPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 2, 1, 8),
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
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 1))
    )


_StaProtocolType_Type.__name__ = "Integer32"
_StaProtocolType_Object = MibScalar
staProtocolType = _StaProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 5),
    _StaPathCostMethod_Type()
)
staPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPathCostMethod.setStatus("current")
_XstMgt_ObjectIdentity = ObjectIdentity
xstMgt = _XstMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6)
)
_XstInstanceCfgTable_Object = MibTable
xstInstanceCfgTable = _XstInstanceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    xstInstanceCfgTable.setStatus("current")
_XstInstanceCfgEntry_Object = MibTableRow
xstInstanceCfgEntry = _XstInstanceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1)
)
xstInstanceCfgEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "xstInstanceCfgIndex"),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 1),
    _XstInstanceCfgIndex_Type()
)
xstInstanceCfgIndex.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 2),
    _XstInstanceCfgPriority_Type()
)
xstInstanceCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstanceCfgPriority.setStatus("current")
_XstInstanceCfgTimeSinceTopologyChange_Type = Integer32
_XstInstanceCfgTimeSinceTopologyChange_Object = MibTableColumn
xstInstanceCfgTimeSinceTopologyChange = _XstInstanceCfgTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 3),
    _XstInstanceCfgTimeSinceTopologyChange_Type()
)
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTimeSinceTopologyChange.setStatus("current")
_XstInstanceCfgTopChanges_Type = Integer32
_XstInstanceCfgTopChanges_Object = MibTableColumn
xstInstanceCfgTopChanges = _XstInstanceCfgTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 4),
    _XstInstanceCfgTopChanges_Type()
)
xstInstanceCfgTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTopChanges.setStatus("current")
_XstInstanceCfgDesignatedRoot_Type = BridgeId
_XstInstanceCfgDesignatedRoot_Object = MibTableColumn
xstInstanceCfgDesignatedRoot = _XstInstanceCfgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 5),
    _XstInstanceCfgDesignatedRoot_Type()
)
xstInstanceCfgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgDesignatedRoot.setStatus("current")
_XstInstanceCfgRootCost_Type = Integer32
_XstInstanceCfgRootCost_Object = MibTableColumn
xstInstanceCfgRootCost = _XstInstanceCfgRootCost_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 6),
    _XstInstanceCfgRootCost_Type()
)
xstInstanceCfgRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootCost.setStatus("current")
_XstInstanceCfgRootPort_Type = Integer32
_XstInstanceCfgRootPort_Object = MibTableColumn
xstInstanceCfgRootPort = _XstInstanceCfgRootPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 7),
    _XstInstanceCfgRootPort_Type()
)
xstInstanceCfgRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootPort.setStatus("current")
_XstInstanceCfgMaxAge_Type = Timeout
_XstInstanceCfgMaxAge_Object = MibTableColumn
xstInstanceCfgMaxAge = _XstInstanceCfgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 8),
    _XstInstanceCfgMaxAge_Type()
)
xstInstanceCfgMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgMaxAge.setStatus("current")
_XstInstanceCfgHelloTime_Type = Timeout
_XstInstanceCfgHelloTime_Object = MibTableColumn
xstInstanceCfgHelloTime = _XstInstanceCfgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 9),
    _XstInstanceCfgHelloTime_Type()
)
xstInstanceCfgHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHelloTime.setStatus("current")
_XstInstanceCfgHoldTime_Type = Timeout
_XstInstanceCfgHoldTime_Object = MibTableColumn
xstInstanceCfgHoldTime = _XstInstanceCfgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 10),
    _XstInstanceCfgHoldTime_Type()
)
xstInstanceCfgHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHoldTime.setStatus("current")
_XstInstanceCfgForwardDelay_Type = Timeout
_XstInstanceCfgForwardDelay_Object = MibTableColumn
xstInstanceCfgForwardDelay = _XstInstanceCfgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 11),
    _XstInstanceCfgForwardDelay_Type()
)
xstInstanceCfgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgForwardDelay.setStatus("current")
_XstInstanceCfgBridgeMaxAge_Type = Timeout
_XstInstanceCfgBridgeMaxAge_Object = MibTableColumn
xstInstanceCfgBridgeMaxAge = _XstInstanceCfgBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 12),
    _XstInstanceCfgBridgeMaxAge_Type()
)
xstInstanceCfgBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeMaxAge.setStatus("current")
_XstInstanceCfgBridgeHelloTime_Type = Timeout
_XstInstanceCfgBridgeHelloTime_Object = MibTableColumn
xstInstanceCfgBridgeHelloTime = _XstInstanceCfgBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 13),
    _XstInstanceCfgBridgeHelloTime_Type()
)
xstInstanceCfgBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeHelloTime.setStatus("current")
_XstInstanceCfgBridgeForwardDelay_Type = Timeout
_XstInstanceCfgBridgeForwardDelay_Object = MibTableColumn
xstInstanceCfgBridgeForwardDelay = _XstInstanceCfgBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 14),
    _XstInstanceCfgBridgeForwardDelay_Type()
)
xstInstanceCfgBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeForwardDelay.setStatus("current")
_XstInstanceCfgTxHoldCount_Type = Integer32
_XstInstanceCfgTxHoldCount_Object = MibTableColumn
xstInstanceCfgTxHoldCount = _XstInstanceCfgTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 4, 1, 16),
    _XstInstanceCfgPathCostMethod_Type()
)
xstInstanceCfgPathCostMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgPathCostMethod.setStatus("current")
_XstInstancePortTable_Object = MibTable
xstInstancePortTable = _XstInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    xstInstancePortTable.setStatus("current")
_XstInstancePortEntry_Object = MibTableRow
xstInstancePortEntry = _XstInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1)
)
xstInstancePortEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "xstInstancePortInstance"),
    (0, "PowerConnect3248-MIB", "xstInstancePortPort"),
)
if mibBuilder.loadTexts:
    xstInstancePortEntry.setStatus("current")
_XstInstancePortInstance_Type = Integer32
_XstInstancePortInstance_Object = MibTableColumn
xstInstancePortInstance = _XstInstancePortInstance_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 1),
    _XstInstancePortInstance_Type()
)
xstInstancePortInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortInstance.setStatus("current")
_XstInstancePortPort_Type = Integer32
_XstInstancePortPort_Object = MibTableColumn
xstInstancePortPort = _XstInstancePortPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 2),
    _XstInstancePortPort_Type()
)
xstInstancePortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortPort.setStatus("current")


class _XstInstancePortPriority_Type(Integer32):
    """Custom type xstInstancePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_XstInstancePortPriority_Type.__name__ = "Integer32"
_XstInstancePortPriority_Object = MibTableColumn
xstInstancePortPriority = _XstInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 4),
    _XstInstancePortState_Type()
)
xstInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortState.setStatus("current")
_XstInstancePortEnable_Type = EnabledStatus
_XstInstancePortEnable_Object = MibTableColumn
xstInstancePortEnable = _XstInstancePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 6),
    _XstInstancePortPathCost_Type()
)
xstInstancePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortPathCost.setStatus("current")
_XstInstancePortDesignatedRoot_Type = BridgeId
_XstInstancePortDesignatedRoot_Object = MibTableColumn
xstInstancePortDesignatedRoot = _XstInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 7),
    _XstInstancePortDesignatedRoot_Type()
)
xstInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedRoot.setStatus("current")
_XstInstancePortDesignatedCost_Type = Integer32
_XstInstancePortDesignatedCost_Object = MibTableColumn
xstInstancePortDesignatedCost = _XstInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 8),
    _XstInstancePortDesignatedCost_Type()
)
xstInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedCost.setStatus("current")
_XstInstancePortDesignatedBridge_Type = BridgeId
_XstInstancePortDesignatedBridge_Object = MibTableColumn
xstInstancePortDesignatedBridge = _XstInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 10),
    _XstInstancePortDesignatedPort_Type()
)
xstInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedPort.setStatus("current")
_XstInstancePortForwardTransitions_Type = Counter32
_XstInstancePortForwardTransitions_Object = MibTableColumn
xstInstancePortForwardTransitions = _XstInstancePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 11),
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
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 4),
          ("backup", 5),
          ("designated", 3),
          ("disabled", 1),
          ("master", 6),
          ("root", 2))
    )


_XstInstancePortPortRole_Type.__name__ = "Integer32"
_XstInstancePortPortRole_Object = MibTableColumn
xstInstancePortPortRole = _XstInstancePortPortRole_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 5, 6, 5, 1, 12),
    _XstInstancePortPortRole_Type()
)
xstInstancePortPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortPortRole.setStatus("current")
_TftpMgt_ObjectIdentity = ObjectIdentity
tftpMgt = _TftpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 6)
)


class _TftpFileType_Type(Integer32):
    """Custom type tftpFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("opcode", 1))
    )


_TftpFileType_Type.__name__ = "Integer32"
_TftpFileType_Object = MibScalar
tftpFileType = _TftpFileType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 6, 1),
    _TftpFileType_Type()
)
tftpFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileType.setStatus("current")


class _TftpSrcFile_Type(DisplayString):
    """Custom type tftpSrcFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TftpSrcFile_Type.__name__ = "DisplayString"
_TftpSrcFile_Object = MibScalar
tftpSrcFile = _TftpSrcFile_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 6, 2),
    _TftpSrcFile_Type()
)
tftpSrcFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSrcFile.setStatus("current")


class _TftpDestFile_Type(DisplayString):
    """Custom type tftpDestFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TftpDestFile_Type.__name__ = "DisplayString"
_TftpDestFile_Object = MibScalar
tftpDestFile = _TftpDestFile_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 6, 3),
    _TftpDestFile_Type()
)
tftpDestFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDestFile.setStatus("current")
_TftpServer_Type = IpAddress
_TftpServer_Object = MibScalar
tftpServer = _TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 6, 4),
    _TftpServer_Type()
)
tftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServer.setStatus("current")


class _TftpAction_Type(Integer32):
    """Custom type tftpAction based on Integer32"""
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
        *(("downloadToPROM", 2),
          ("downloadToRAM", 3),
          ("notDownloading", 1),
          ("upload", 4))
    )


_TftpAction_Type.__name__ = "Integer32"
_TftpAction_Object = MibScalar
tftpAction = _TftpAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 6, 5),
    _TftpAction_Type()
)
tftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpAction.setStatus("current")


class _TftpStatus_Type(Integer32):
    """Custom type tftpStatus based on Integer32"""
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
        *(("tftpDownloadChecksumError", 5),
          ("tftpDownloadIncompatibleImage", 6),
          ("tftpGeneralError", 3),
          ("tftpNoResponseFromServer", 4),
          ("tftpStatusUnknown", 2),
          ("tftpSuccess", 1),
          ("tftpTftpAccessViolation", 8),
          ("tftpTftpFileNotFound", 7))
    )


_TftpStatus_Type.__name__ = "Integer32"
_TftpStatus_Object = MibScalar
tftpStatus = _TftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 6, 6),
    _TftpStatus_Type()
)
tftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpStatus.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 7)
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 7, 3),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_MirrorMgt_ObjectIdentity = ObjectIdentity
mirrorMgt = _MirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 8)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 8, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "mirrorDestinationPort"),
    (0, "PowerConnect3248-MIB", "mirrorSourcePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorDestinationPort_Type = Integer32
_MirrorDestinationPort_Object = MibTableColumn
mirrorDestinationPort = _MirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 8, 1, 1, 1),
    _MirrorDestinationPort_Type()
)
mirrorDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorDestinationPort.setStatus("current")
_MirrorSourcePort_Type = Integer32
_MirrorSourcePort_Object = MibTableColumn
mirrorSourcePort = _MirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 8, 1, 1, 2),
    _MirrorSourcePort_Type()
)
mirrorSourcePort.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 8, 1, 1, 3),
    _MirrorType_Type()
)
mirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorType.setStatus("current")


class _MirrorStatus_Type(Integer32):
    """Custom type mirrorStatus based on Integer32"""
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


_MirrorStatus_Type.__name__ = "Integer32"
_MirrorStatus_Object = MibTableColumn
mirrorStatus = _MirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 8, 1, 1, 4),
    _MirrorStatus_Type()
)
mirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorStatus.setStatus("current")
_IgmpSnoopMgt_ObjectIdentity = ObjectIdentity
igmpSnoopMgt = _IgmpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9)
)


class _IgmpSnoopStatus_Type(Integer32):
    """Custom type igmpSnoopStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IgmpSnoopStatus_Type.__name__ = "Integer32"
_IgmpSnoopStatus_Object = MibScalar
igmpSnoopStatus = _IgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 1),
    _IgmpSnoopStatus_Type()
)
igmpSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopStatus.setStatus("current")


class _IgmpSnoopQuerier_Type(Integer32):
    """Custom type igmpSnoopQuerier based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IgmpSnoopQuerier_Type.__name__ = "Integer32"
_IgmpSnoopQuerier_Object = MibScalar
igmpSnoopQuerier = _IgmpSnoopQuerier_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 4),
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
        ValueRangeConstraint(5, 30),
    )


_IgmpSnoopQueryMaxResponseTime_Type.__name__ = "Integer32"
_IgmpSnoopQueryMaxResponseTime_Object = MibScalar
igmpSnoopQueryMaxResponseTime = _IgmpSnoopQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 5),
    _IgmpSnoopQueryMaxResponseTime_Type()
)
igmpSnoopQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryMaxResponseTime.setStatus("current")


class _IgmpSnoopQueryTimeout_Type(Integer32):
    """Custom type igmpSnoopQueryTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 500),
    )


_IgmpSnoopQueryTimeout_Type.__name__ = "Integer32"
_IgmpSnoopQueryTimeout_Object = MibScalar
igmpSnoopQueryTimeout = _IgmpSnoopQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 6),
    _IgmpSnoopQueryTimeout_Type()
)
igmpSnoopQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryTimeout.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 7),
    _IgmpSnoopVersion_Type()
)
igmpSnoopVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVersion.setStatus("current")
_IgmpSnoopRouterCurrentTable_Object = MibTable
igmpSnoopRouterCurrentTable = _IgmpSnoopRouterCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 8)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentTable.setStatus("current")
_IgmpSnoopRouterCurrentEntry_Object = MibTableRow
igmpSnoopRouterCurrentEntry = _IgmpSnoopRouterCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 8, 1)
)
igmpSnoopRouterCurrentEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "igmpSnoopRouterCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentEntry.setStatus("current")
_IgmpSnoopRouterCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object = MibTableColumn
igmpSnoopRouterCurrentVlanIndex = _IgmpSnoopRouterCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 8, 1, 1),
    _IgmpSnoopRouterCurrentVlanIndex_Type()
)
igmpSnoopRouterCurrentVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentVlanIndex.setStatus("current")
_IgmpSnoopRouterCurrentPorts_Type = PortList
_IgmpSnoopRouterCurrentPorts_Object = MibTableColumn
igmpSnoopRouterCurrentPorts = _IgmpSnoopRouterCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 8, 1, 2),
    _IgmpSnoopRouterCurrentPorts_Type()
)
igmpSnoopRouterCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentPorts.setStatus("current")
_IgmpSnoopRouterCurrentStatus_Type = PortList
_IgmpSnoopRouterCurrentStatus_Object = MibTableColumn
igmpSnoopRouterCurrentStatus = _IgmpSnoopRouterCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 8, 1, 3),
    _IgmpSnoopRouterCurrentStatus_Type()
)
igmpSnoopRouterCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentStatus.setStatus("current")
_IgmpSnoopRouterStaticTable_Object = MibTable
igmpSnoopRouterStaticTable = _IgmpSnoopRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticTable.setStatus("current")
_IgmpSnoopRouterStaticEntry_Object = MibTableRow
igmpSnoopRouterStaticEntry = _IgmpSnoopRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 9, 1)
)
igmpSnoopRouterStaticEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "igmpSnoopRouterStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticEntry.setStatus("current")
_IgmpSnoopRouterStaticVlanIndex_Type = Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object = MibTableColumn
igmpSnoopRouterStaticVlanIndex = _IgmpSnoopRouterStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 9, 1, 1),
    _IgmpSnoopRouterStaticVlanIndex_Type()
)
igmpSnoopRouterStaticVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticVlanIndex.setStatus("current")
_IgmpSnoopRouterStaticPorts_Type = PortList
_IgmpSnoopRouterStaticPorts_Object = MibTableColumn
igmpSnoopRouterStaticPorts = _IgmpSnoopRouterStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 9, 1, 2),
    _IgmpSnoopRouterStaticPorts_Type()
)
igmpSnoopRouterStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticPorts.setStatus("current")


class _IgmpSnoopRouterStaticStatus_Type(Integer32):
    """Custom type igmpSnoopRouterStaticStatus based on Integer32"""
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


_IgmpSnoopRouterStaticStatus_Type.__name__ = "Integer32"
_IgmpSnoopRouterStaticStatus_Object = MibTableColumn
igmpSnoopRouterStaticStatus = _IgmpSnoopRouterStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 9, 1, 3),
    _IgmpSnoopRouterStaticStatus_Type()
)
igmpSnoopRouterStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticStatus.setStatus("current")
_IgmpSnoopMulticastCurrentTable_Object = MibTable
igmpSnoopMulticastCurrentTable = _IgmpSnoopMulticastCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 10)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentTable.setStatus("current")
_IgmpSnoopMulticastCurrentEntry_Object = MibTableRow
igmpSnoopMulticastCurrentEntry = _IgmpSnoopMulticastCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 10, 1)
)
igmpSnoopMulticastCurrentEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "igmpSnoopMulticastCurrentVlanIndex"),
    (0, "PowerConnect3248-MIB", "igmpSnoopMulticastCurrentIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentEntry.setStatus("current")
_IgmpSnoopMulticastCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object = MibTableColumn
igmpSnoopMulticastCurrentVlanIndex = _IgmpSnoopMulticastCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 10, 1, 1),
    _IgmpSnoopMulticastCurrentVlanIndex_Type()
)
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentVlanIndex.setStatus("current")
_IgmpSnoopMulticastCurrentIpAddress_Type = IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object = MibTableColumn
igmpSnoopMulticastCurrentIpAddress = _IgmpSnoopMulticastCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 10, 1, 2),
    _IgmpSnoopMulticastCurrentIpAddress_Type()
)
igmpSnoopMulticastCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentIpAddress.setStatus("current")
_IgmpSnoopMulticastCurrentPorts_Type = PortList
_IgmpSnoopMulticastCurrentPorts_Object = MibTableColumn
igmpSnoopMulticastCurrentPorts = _IgmpSnoopMulticastCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 10, 1, 3),
    _IgmpSnoopMulticastCurrentPorts_Type()
)
igmpSnoopMulticastCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentPorts.setStatus("current")
_IgmpSnoopMulticastCurrentStatus_Type = PortList
_IgmpSnoopMulticastCurrentStatus_Object = MibTableColumn
igmpSnoopMulticastCurrentStatus = _IgmpSnoopMulticastCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 10, 1, 4),
    _IgmpSnoopMulticastCurrentStatus_Type()
)
igmpSnoopMulticastCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentStatus.setStatus("current")
_IgmpSnoopMulticastStaticTable_Object = MibTable
igmpSnoopMulticastStaticTable = _IgmpSnoopMulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 11)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticTable.setStatus("current")
_IgmpSnoopMulticastStaticEntry_Object = MibTableRow
igmpSnoopMulticastStaticEntry = _IgmpSnoopMulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 11, 1)
)
igmpSnoopMulticastStaticEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "igmpSnoopMulticastStaticVlanIndex"),
    (0, "PowerConnect3248-MIB", "igmpSnoopMulticastStaticIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticEntry.setStatus("current")
_IgmpSnoopMulticastStaticVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object = MibTableColumn
igmpSnoopMulticastStaticVlanIndex = _IgmpSnoopMulticastStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 11, 1, 1),
    _IgmpSnoopMulticastStaticVlanIndex_Type()
)
igmpSnoopMulticastStaticVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticVlanIndex.setStatus("current")
_IgmpSnoopMulticastStaticIpAddress_Type = IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object = MibTableColumn
igmpSnoopMulticastStaticIpAddress = _IgmpSnoopMulticastStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 11, 1, 2),
    _IgmpSnoopMulticastStaticIpAddress_Type()
)
igmpSnoopMulticastStaticIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticIpAddress.setStatus("current")
_IgmpSnoopMulticastStaticPorts_Type = PortList
_IgmpSnoopMulticastStaticPorts_Object = MibTableColumn
igmpSnoopMulticastStaticPorts = _IgmpSnoopMulticastStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 11, 1, 3),
    _IgmpSnoopMulticastStaticPorts_Type()
)
igmpSnoopMulticastStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticPorts.setStatus("current")


class _IgmpSnoopMulticastStaticStatus_Type(Integer32):
    """Custom type igmpSnoopMulticastStaticStatus based on Integer32"""
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


_IgmpSnoopMulticastStaticStatus_Type.__name__ = "Integer32"
_IgmpSnoopMulticastStaticStatus_Object = MibTableColumn
igmpSnoopMulticastStaticStatus = _IgmpSnoopMulticastStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 9, 11, 1, 4),
    _IgmpSnoopMulticastStaticStatus_Type()
)
igmpSnoopMulticastStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticStatus.setStatus("current")
_IpMgt_ObjectIdentity = ObjectIdentity
ipMgt = _IpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10)
)
_NetConfigTable_Object = MibTable
netConfigTable = _NetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 1)
)
if mibBuilder.loadTexts:
    netConfigTable.setStatus("current")
_NetConfigEntry_Object = MibTableRow
netConfigEntry = _NetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 1, 1)
)
netConfigEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "netConfigIfIndex"),
    (0, "PowerConnect3248-MIB", "netConfigIPAddress"),
    (0, "PowerConnect3248-MIB", "netConfigSubnetMask"),
)
if mibBuilder.loadTexts:
    netConfigEntry.setStatus("current")
_NetConfigIfIndex_Type = Integer32
_NetConfigIfIndex_Object = MibTableColumn
netConfigIfIndex = _NetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 1, 1, 1),
    _NetConfigIfIndex_Type()
)
netConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigIfIndex.setStatus("current")
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibTableColumn
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 1, 1, 2),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("current")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibTableColumn
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 1, 1, 3),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 1, 1, 5),
    _NetConfigUnnumbered_Type()
)
netConfigUnnumbered.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigUnnumbered.setStatus("current")
_NetConfigStatus_Type = RowStatus
_NetConfigStatus_Object = MibTableColumn
netConfigStatus = _NetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 1, 1, 6),
    _NetConfigStatus_Type()
)
netConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigStatus.setStatus("current")
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 2),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("current")


class _IpHttpState_Type(Integer32):
    """Custom type ipHttpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpHttpState_Type.__name__ = "Integer32"
_IpHttpState_Object = MibScalar
ipHttpState = _IpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 5),
    _IpDhcpRestart_Type()
)
ipDhcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpRestart.setStatus("current")
_IpHttpsState_Type = EnabledStatus
_IpHttpsState_Object = MibScalar
ipHttpsState = _IpHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 6),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 10, 7),
    _IpHttpsPort_Type()
)
ipHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsPort.setStatus("current")
_BcastStormMgt_ObjectIdentity = ObjectIdentity
bcastStormMgt = _BcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 11)
)
_BcastStormTable_Object = MibTable
bcastStormTable = _BcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 11, 1)
)
if mibBuilder.loadTexts:
    bcastStormTable.setStatus("current")
_BcastStormEntry_Object = MibTableRow
bcastStormEntry = _BcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 11, 1, 1)
)
bcastStormEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "bcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    bcastStormEntry.setStatus("current")
_BcastStormIfIndex_Type = Integer32
_BcastStormIfIndex_Object = MibTableColumn
bcastStormIfIndex = _BcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 11, 1, 1, 1),
    _BcastStormIfIndex_Type()
)
bcastStormIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcastStormIfIndex.setStatus("current")


class _BcastStormStatus_Type(Integer32):
    """Custom type bcastStormStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BcastStormStatus_Type.__name__ = "Integer32"
_BcastStormStatus_Object = MibTableColumn
bcastStormStatus = _BcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 11, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 11, 1, 1, 3),
    _BcastStormSampleType_Type()
)
bcastStormSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormSampleType.setStatus("current")
_BcastStormPktRate_Type = Integer32
_BcastStormPktRate_Object = MibTableColumn
bcastStormPktRate = _BcastStormPktRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 11, 1, 1, 4),
    _BcastStormPktRate_Type()
)
bcastStormPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormPktRate.setStatus("current")
_BcastStormOctetRate_Type = Integer32
_BcastStormOctetRate_Object = MibTableColumn
bcastStormOctetRate = _BcastStormOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 11, 1, 1, 5),
    _BcastStormOctetRate_Type()
)
bcastStormOctetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormOctetRate.setStatus("current")
_BcastStormPercent_Type = Integer32
_BcastStormPercent_Object = MibTableColumn
bcastStormPercent = _BcastStormPercent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 11, 1, 1, 6),
    _BcastStormPercent_Type()
)
bcastStormPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormPercent.setStatus("current")
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 12)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 12, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIndex_Type = Unsigned32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 12, 1, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 12, 1, 1, 2),
    _VlanAddressMethod_Type()
)
vlanAddressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAddressMethod.setStatus("current")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 12, 2)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 12, 2, 1)
)
vlanPortEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "vlanPortIndex"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("current")
_VlanPortIndex_Type = Integer32
_VlanPortIndex_Object = MibTableColumn
vlanPortIndex = _VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 12, 2, 1, 1),
    _VlanPortIndex_Type()
)
vlanPortIndex.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 12, 2, 1, 2),
    _VlanPortMode_Type()
)
vlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMode.setStatus("current")
_PriorityMgt_ObjectIdentity = ObjectIdentity
priorityMgt = _PriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13)
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 1),
    _PrioIpPrecDscpStatus_Type()
)
prioIpPrecDscpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecDscpStatus.setStatus("current")
_PrioIpPrecTable_Object = MibTable
prioIpPrecTable = _PrioIpPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 2)
)
if mibBuilder.loadTexts:
    prioIpPrecTable.setStatus("current")
_PrioIpPrecEntry_Object = MibTableRow
prioIpPrecEntry = _PrioIpPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 2, 1)
)
prioIpPrecEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "prioIpPrecPort"),
    (0, "PowerConnect3248-MIB", "prioIpPrecValue"),
)
if mibBuilder.loadTexts:
    prioIpPrecEntry.setStatus("current")
_PrioIpPrecPort_Type = Integer32
_PrioIpPrecPort_Object = MibTableColumn
prioIpPrecPort = _PrioIpPrecPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 2, 1, 2),
    _PrioIpPrecPort_Type()
)
prioIpPrecPort.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 2, 1, 3),
    _PrioIpPrecValue_Type()
)
prioIpPrecValue.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 2, 1, 4),
    _PrioIpPrecCos_Type()
)
prioIpPrecCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecCos.setStatus("current")
_PrioIpPrecRestoreDefault_Type = Integer32
_PrioIpPrecRestoreDefault_Object = MibScalar
prioIpPrecRestoreDefault = _PrioIpPrecRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 3),
    _PrioIpPrecRestoreDefault_Type()
)
prioIpPrecRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecRestoreDefault.setStatus("current")
_PrioIpDscpTable_Object = MibTable
prioIpDscpTable = _PrioIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 4)
)
if mibBuilder.loadTexts:
    prioIpDscpTable.setStatus("current")
_PrioIpDscpEntry_Object = MibTableRow
prioIpDscpEntry = _PrioIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 4, 1)
)
prioIpDscpEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "prioIpDscpPort"),
    (0, "PowerConnect3248-MIB", "prioIpDscpValue"),
)
if mibBuilder.loadTexts:
    prioIpDscpEntry.setStatus("current")
_PrioIpDscpPort_Type = Integer32
_PrioIpDscpPort_Object = MibTableColumn
prioIpDscpPort = _PrioIpDscpPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 4, 1, 1),
    _PrioIpDscpPort_Type()
)
prioIpDscpPort.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 4, 1, 2),
    _PrioIpDscpValue_Type()
)
prioIpDscpValue.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 4, 1, 3),
    _PrioIpDscpCos_Type()
)
prioIpDscpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpCos.setStatus("current")
_PrioIpDscpRestoreDefault_Type = Integer32
_PrioIpDscpRestoreDefault_Object = MibScalar
prioIpDscpRestoreDefault = _PrioIpDscpRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 5),
    _PrioIpDscpRestoreDefault_Type()
)
prioIpDscpRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpRestoreDefault.setStatus("current")


class _PrioIpPortEnableStatus_Type(Integer32):
    """Custom type prioIpPortEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PrioIpPortEnableStatus_Type.__name__ = "Integer32"
_PrioIpPortEnableStatus_Object = MibScalar
prioIpPortEnableStatus = _PrioIpPortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 6),
    _PrioIpPortEnableStatus_Type()
)
prioIpPortEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPortEnableStatus.setStatus("current")
_PrioIpPortTable_Object = MibTable
prioIpPortTable = _PrioIpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 7)
)
if mibBuilder.loadTexts:
    prioIpPortTable.setStatus("current")
_PrioIpPortEntry_Object = MibTableRow
prioIpPortEntry = _PrioIpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 7, 1)
)
prioIpPortEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "prioIpPortPhysPort"),
    (0, "PowerConnect3248-MIB", "prioIpPortValue"),
)
if mibBuilder.loadTexts:
    prioIpPortEntry.setStatus("current")
_PrioIpPortPhysPort_Type = Integer32
_PrioIpPortPhysPort_Object = MibTableColumn
prioIpPortPhysPort = _PrioIpPortPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 7, 1, 1),
    _PrioIpPortPhysPort_Type()
)
prioIpPortPhysPort.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 7, 1, 2),
    _PrioIpPortValue_Type()
)
prioIpPortValue.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 7, 1, 3),
    _PrioIpPortCos_Type()
)
prioIpPortCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioIpPortCos.setStatus("current")


class _PrioIpPortStatus_Type(Integer32):
    """Custom type prioIpPortStatus based on Integer32"""
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


_PrioIpPortStatus_Type.__name__ = "Integer32"
_PrioIpPortStatus_Object = MibTableColumn
prioIpPortStatus = _PrioIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 7, 1, 4),
    _PrioIpPortStatus_Type()
)
prioIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioIpPortStatus.setStatus("current")
_PrioCopy_ObjectIdentity = ObjectIdentity
prioCopy = _PrioCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 8)
)
_PrioCopyIpPrec_Type = OctetString
_PrioCopyIpPrec_Object = MibScalar
prioCopyIpPrec = _PrioCopyIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 8, 1),
    _PrioCopyIpPrec_Type()
)
prioCopyIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpPrec.setStatus("current")
_PrioCopyIpDscp_Type = OctetString
_PrioCopyIpDscp_Object = MibScalar
prioCopyIpDscp = _PrioCopyIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 8, 2),
    _PrioCopyIpDscp_Type()
)
prioCopyIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpDscp.setStatus("current")
_PrioCopyIpPort_Type = OctetString
_PrioCopyIpPort_Object = MibScalar
prioCopyIpPort = _PrioCopyIpPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 8, 3),
    _PrioCopyIpPort_Type()
)
prioCopyIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpPort.setStatus("current")
_PrioWrrTable_Object = MibTable
prioWrrTable = _PrioWrrTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 9)
)
if mibBuilder.loadTexts:
    prioWrrTable.setStatus("current")
_PrioWrrEntry_Object = MibTableRow
prioWrrEntry = _PrioWrrEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 9, 1)
)
prioWrrEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "prioWrrTrafficClass"),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 9, 1, 1),
    _PrioWrrTrafficClass_Type()
)
prioWrrTrafficClass.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 13, 9, 1, 2),
    _PrioWrrWeight_Type()
)
prioWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioWrrWeight.setStatus("current")
_TrapDestMgt_ObjectIdentity = ObjectIdentity
trapDestMgt = _TrapDestMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 14)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("current")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 14, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "trapDestAddress"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("current")
_TrapDestAddress_Type = IpAddress
_TrapDestAddress_Object = MibTableColumn
trapDestAddress = _TrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 14, 1, 1, 1),
    _TrapDestAddress_Type()
)
trapDestAddress.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 14, 1, 1, 2),
    _TrapDestCommunity_Type()
)
trapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestCommunity.setStatus("current")


class _TrapDestStatus_Type(Integer32):
    """Custom type trapDestStatus based on Integer32"""
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


_TrapDestStatus_Type.__name__ = "Integer32"
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 14, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 14, 1, 1, 4),
    _TrapDestVersion_Type()
)
trapDestVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestVersion.setStatus("current")
_SecurityMgt_ObjectIdentity = ObjectIdentity
securityMgt = _SecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17)
)
_PortSecurityMgt_ObjectIdentity = ObjectIdentity
portSecurityMgt = _PortSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 2)
)
_PortSecPortTable_Object = MibTable
portSecPortTable = _PortSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    portSecPortTable.setStatus("current")
_PortSecPortEntry_Object = MibTableRow
portSecPortEntry = _PortSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 2, 1, 1)
)
portSecPortEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "portSecPortIndex"),
)
if mibBuilder.loadTexts:
    portSecPortEntry.setStatus("current")
_PortSecPortIndex_Type = Integer32
_PortSecPortIndex_Object = MibTableColumn
portSecPortIndex = _PortSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 2, 1, 1, 1),
    _PortSecPortIndex_Type()
)
portSecPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecPortIndex.setStatus("current")
_PortSecPortStatus_Type = EnabledStatus
_PortSecPortStatus_Object = MibTableColumn
portSecPortStatus = _PortSecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 2, 1, 1, 3),
    _PortSecAction_Type()
)
portSecAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecAction.setStatus("current")
_RadiusMgt_ObjectIdentity = ObjectIdentity
radiusMgt = _RadiusMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 4)
)
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibScalar
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 4, 2),
    _RadiusServerPortNumber_Type()
)
radiusServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerPortNumber.setStatus("current")
_RadiusServerKey_Type = DisplayString
_RadiusServerKey_Object = MibScalar
radiusServerKey = _RadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 4, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 4, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 4, 5),
    _RadiusServerTimeout_Type()
)
radiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerTimeout.setStatus("current")
_TacacsMgt_ObjectIdentity = ObjectIdentity
tacacsMgt = _TacacsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 5)
)
_TacacsServerAddress_Type = IpAddress
_TacacsServerAddress_Object = MibScalar
tacacsServerAddress = _TacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 5, 2),
    _TacacsServerPortNumber_Type()
)
tacacsServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerPortNumber.setStatus("current")
_TacacsServerKey_Type = DisplayString
_TacacsServerKey_Object = MibScalar
tacacsServerKey = _TacacsServerKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 5, 3),
    _TacacsServerKey_Type()
)
tacacsServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerKey.setStatus("current")
_SshMgt_ObjectIdentity = ObjectIdentity
sshMgt = _SshMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6)
)
_SshServerStatus_Type = EnabledStatus
_SshServerStatus_Object = MibScalar
sshServerStatus = _SshServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 1),
    _SshServerStatus_Type()
)
sshServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerStatus.setStatus("current")
_SshServerMajorVersion_Type = Integer32
_SshServerMajorVersion_Object = MibScalar
sshServerMajorVersion = _SshServerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 2),
    _SshServerMajorVersion_Type()
)
sshServerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMajorVersion.setStatus("current")
_SshServerMinorVersion_Type = Integer32
_SshServerMinorVersion_Object = MibScalar
sshServerMinorVersion = _SshServerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 5),
    _SshAuthRetries_Type()
)
sshAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAuthRetries.setStatus("current")
_SshConnInfoTable_Object = MibTable
sshConnInfoTable = _SshConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 6)
)
if mibBuilder.loadTexts:
    sshConnInfoTable.setStatus("current")
_SshConnInfoEntry_Object = MibTableRow
sshConnInfoEntry = _SshConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 6, 1)
)
sshConnInfoEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "sshConnID"),
)
if mibBuilder.loadTexts:
    sshConnInfoEntry.setStatus("current")
_SshConnID_Type = Integer32
_SshConnID_Object = MibTableColumn
sshConnID = _SshConnID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 6, 1, 1),
    _SshConnID_Type()
)
sshConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnID.setStatus("current")
_SshConnMajorVersion_Type = Integer32
_SshConnMajorVersion_Object = MibTableColumn
sshConnMajorVersion = _SshConnMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 6, 1, 2),
    _SshConnMajorVersion_Type()
)
sshConnMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMajorVersion.setStatus("current")
_SshConnMinorVersion_Type = Integer32
_SshConnMinorVersion_Object = MibTableColumn
sshConnMinorVersion = _SshConnMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 6, 1, 5),
    _SshConnStatus_Type()
)
sshConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnStatus.setStatus("current")
_SshConnUserName_Type = OctetString
_SshConnUserName_Object = MibTableColumn
sshConnUserName = _SshConnUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 17, 6, 6, 1, 7),
    _SshDisconnect_Type()
)
sshDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshDisconnect.setStatus("current")
_SysLogMgt_ObjectIdentity = ObjectIdentity
sysLogMgt = _SysLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19)
)


class _SysLogStatus_Type(Integer32):
    """Custom type sysLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SysLogStatus_Type.__name__ = "Integer32"
_SysLogStatus_Object = MibScalar
sysLogStatus = _SysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 1),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 3),
    _SysLogHistoryRamLevel_Type()
)
sysLogHistoryRamLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryRamLevel.setStatus("current")
_RemoteLogMgt_ObjectIdentity = ObjectIdentity
remoteLogMgt = _RemoteLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 6)
)
_RemoteLogStatus_Type = EnabledStatus
_RemoteLogStatus_Object = MibScalar
remoteLogStatus = _RemoteLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 6, 1),
    _RemoteLogStatus_Type()
)
remoteLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogStatus.setStatus("current")


class _RemoteLogLevel_Type(Integer32):
    """Custom type remoteLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RemoteLogLevel_Type.__name__ = "Integer32"
_RemoteLogLevel_Object = MibScalar
remoteLogLevel = _RemoteLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 6, 2),
    _RemoteLogLevel_Type()
)
remoteLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogLevel.setStatus("current")


class _RemoteLogFacilityType_Type(Integer32):
    """Custom type remoteLogFacilityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("localUse0", 16),
          ("localUse1", 17),
          ("localUse2", 18),
          ("localUse3", 19),
          ("localUse4", 20),
          ("localUse5", 21),
          ("localUse6", 22),
          ("localUse7", 23))
    )


_RemoteLogFacilityType_Type.__name__ = "Integer32"
_RemoteLogFacilityType_Object = MibScalar
remoteLogFacilityType = _RemoteLogFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 6, 3),
    _RemoteLogFacilityType_Type()
)
remoteLogFacilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogFacilityType.setStatus("current")
_RemoteLogServerTable_Object = MibTable
remoteLogServerTable = _RemoteLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 6, 4)
)
if mibBuilder.loadTexts:
    remoteLogServerTable.setStatus("current")
_RemoteLogServerEntry_Object = MibTableRow
remoteLogServerEntry = _RemoteLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 6, 4, 1)
)
remoteLogServerEntry.setIndexNames(
    (0, "PowerConnect3248-MIB", "remoteLogServerIp"),
)
if mibBuilder.loadTexts:
    remoteLogServerEntry.setStatus("current")
_RemoteLogServerIp_Type = IpAddress
_RemoteLogServerIp_Object = MibTableColumn
remoteLogServerIp = _RemoteLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 6, 4, 1, 1),
    _RemoteLogServerIp_Type()
)
remoteLogServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerIp.setStatus("current")
_RemoteLogServerStatus_Type = ValidStatus
_RemoteLogServerStatus_Object = MibTableColumn
remoteLogServerStatus = _RemoteLogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 19, 6, 4, 1, 2),
    _RemoteLogServerStatus_Type()
)
remoteLogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerStatus.setStatus("current")
_LineMgt_ObjectIdentity = ObjectIdentity
lineMgt = _LineMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20)
)
_ConsoleMgt_ObjectIdentity = ObjectIdentity
consoleMgt = _ConsoleMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 1)
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 1, 7),
    _ConsoleSilentTime_Type()
)
consoleSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleSilentTime.setStatus("current")
_TelnetMgt_ObjectIdentity = ObjectIdentity
telnetMgt = _TelnetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 2)
)


class _TelnetExecTimeout_Type(Integer32):
    """Custom type telnetExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TelnetExecTimeout_Type.__name__ = "Integer32"
_TelnetExecTimeout_Object = MibScalar
telnetExecTimeout = _TelnetExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 1, 20, 2, 2),
    _TelnetPasswordThreshold_Type()
)
telnetPasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPasswordThreshold.setStatus("current")
_PowerConnect3248Notifications_ObjectIdentity = ObjectIdentity
powerConnect3248Notifications = _PowerConnect3248Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 2)
)
_PowerConnect3248Traps_ObjectIdentity = ObjectIdentity
powerConnect3248Traps = _PowerConnect3248Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 2, 1)
)
_PowerConnect3248TrapsPrefix_ObjectIdentity = ObjectIdentity
powerConnect3248TrapsPrefix = _PowerConnect3248TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 2, 1, 0)
)
_PowerConnect3248Conformance_ObjectIdentity = ObjectIdentity
powerConnect3248Conformance = _PowerConnect3248Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 3)
)

# Managed Objects groups


# Notification objects

swPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 2, 1, 0, 1)
)
swPowerStatusChangeTrap.setObjects(
      *(("PowerConnect3248-MIB", "swIndivPowerUnitIndex"),
        ("PowerConnect3248-MIB", "swIndivPowerIndex"),
        ("PowerConnect3248-MIB", "swIndivPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChangeTrap.setStatus(
        "current"
    )

swPortSecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 3, 2, 1, 0, 36)
)
swPortSecurityTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    swPortSecurityTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PowerConnect3248-MIB",
    **{"ValidStatus": ValidStatus,
       "private": private,
       "enterprises": enterprises,
       "dell": dell,
       "dellLan": dellLan,
       "powerConnect3248MIB": powerConnect3248MIB,
       "powerConnect3248MIBObjects": powerConnect3248MIBObjects,
       "switchMgt": switchMgt,
       "switchManagementVlan": switchManagementVlan,
       "switchNumber": switchNumber,
       "switchInfoTable": switchInfoTable,
       "switchInfoEntry": switchInfoEntry,
       "swUnitIndex": swUnitIndex,
       "swHardwareVer": swHardwareVer,
       "swMicrocodeVer": swMicrocodeVer,
       "swLoaderVer": swLoaderVer,
       "swBootRomVer": swBootRomVer,
       "swOpCodeVer": swOpCodeVer,
       "swPortNumber": swPortNumber,
       "swPowerStatus": swPowerStatus,
       "swRoleInSystem": swRoleInSystem,
       "swSerialNumber": swSerialNumber,
       "swExpansionSlot1": swExpansionSlot1,
       "swExpansionSlot2": swExpansionSlot2,
       "swServiceTag": swServiceTag,
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
       "staPortIndex": staPortIndex,
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
       "xstInstancePortInstance": xstInstancePortInstance,
       "xstInstancePortPort": xstInstancePortPort,
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
       "tftpMgt": tftpMgt,
       "tftpFileType": tftpFileType,
       "tftpSrcFile": tftpSrcFile,
       "tftpDestFile": tftpDestFile,
       "tftpServer": tftpServer,
       "tftpAction": tftpAction,
       "tftpStatus": tftpStatus,
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
       "igmpSnoopQueryTimeout": igmpSnoopQueryTimeout,
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
       "securityMgt": securityMgt,
       "portSecurityMgt": portSecurityMgt,
       "portSecPortTable": portSecPortTable,
       "portSecPortEntry": portSecPortEntry,
       "portSecPortIndex": portSecPortIndex,
       "portSecPortStatus": portSecPortStatus,
       "portSecAction": portSecAction,
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
       "sysLogMgt": sysLogMgt,
       "sysLogStatus": sysLogStatus,
       "sysLogHistoryFlashLevel": sysLogHistoryFlashLevel,
       "sysLogHistoryRamLevel": sysLogHistoryRamLevel,
       "remoteLogMgt": remoteLogMgt,
       "remoteLogStatus": remoteLogStatus,
       "remoteLogLevel": remoteLogLevel,
       "remoteLogFacilityType": remoteLogFacilityType,
       "remoteLogServerTable": remoteLogServerTable,
       "remoteLogServerEntry": remoteLogServerEntry,
       "remoteLogServerIp": remoteLogServerIp,
       "remoteLogServerStatus": remoteLogServerStatus,
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
       "powerConnect3248Notifications": powerConnect3248Notifications,
       "powerConnect3248Traps": powerConnect3248Traps,
       "powerConnect3248TrapsPrefix": powerConnect3248TrapsPrefix,
       "swPowerStatusChangeTrap": swPowerStatusChangeTrap,
       "swPortSecurityTrap": swPortSecurityTrap,
       "powerConnect3248Conformance": powerConnect3248Conformance}
)
