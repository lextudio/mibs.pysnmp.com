# SNMP MIB module (ECS2100-28PP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ECS2100-28PP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:29 2024
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

(Dot1agCfmMepId,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepDbRMepIdentifier,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepId",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepDbRMepIdentifier",
    "dot1agCfmMepIdentifier")

(dot1xAuthConfigEntry,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xAuthConfigEntry")

(InterfaceIndex,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifOperStatus")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(pethMainPseEntry,
 pethPsePortEntry) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseEntry",
    "pethPsePortEntry")

(PortList,
 VlanId,
 VlanIndex,
 dot1qVlanStaticEntry,
 dot1vProtocolPortEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "VlanIndex",
    "dot1qVlanStaticEntry",
    "dot1vProtocolPortEntry")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ecs2100_28ppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43)
)
ecs2100_28ppMIB.setRevisions(
        ("2015-08-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class KeySegment(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



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



class StaPathCostMode(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_Accton_ObjectIdentity = ObjectIdentity
accton = _Accton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259)
)
_EdgecoreNetworks_ObjectIdentity = ObjectIdentity
edgecoreNetworks = _EdgecoreNetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10)
)
_EdgecoreNetworksMgt_ObjectIdentity = ObjectIdentity
edgecoreNetworksMgt = _EdgecoreNetworksMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1)
)
_Ecs2100_28ppMIBObjects_ObjectIdentity = ObjectIdentity
ecs2100_28ppMIBObjects = _Ecs2100_28ppMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1)
)
_SwitchMgt_ObjectIdentity = ObjectIdentity
switchMgt = _SwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1)
)
_SwitchNumber_Type = Integer32
_SwitchNumber_Object = MibScalar
switchNumber = _SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 2),
    _SwitchNumber_Type()
)
switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumber.setStatus("current")
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1)
)
switchInfoEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")


class _SwUnitIndex_Type(Integer32):
    """Custom type swUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SwUnitIndex_Type.__name__ = "Integer32"
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 1),
    _SwUnitIndex_Type()
)
swUnitIndex.setMaxAccess("not-accessible")
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 6),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("current")
_SwPortNumber_Type = Integer32
_SwPortNumber_Object = MibTableColumn
swPortNumber = _SwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 10),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")


class _SwServiceTag_Type(DisplayString):
    """Custom type swServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwServiceTag_Type.__name__ = "DisplayString"
_SwServiceTag_Object = MibTableColumn
swServiceTag = _SwServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 13),
    _SwServiceTag_Type()
)
swServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swServiceTag.setStatus("current")


class _SwModelNumber_Type(DisplayString):
    """Custom type swModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwModelNumber_Type.__name__ = "DisplayString"
_SwModelNumber_Object = MibTableColumn
swModelNumber = _SwModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 14),
    _SwModelNumber_Type()
)
swModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModelNumber.setStatus("current")


class _SwEpldVer_Type(DisplayString):
    """Custom type swEpldVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwEpldVer_Type.__name__ = "DisplayString"
_SwEpldVer_Object = MibTableColumn
swEpldVer = _SwEpldVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 3, 1, 15),
    _SwEpldVer_Type()
)
swEpldVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEpldVer.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 4),
    _SwitchOperState_Type()
)
switchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOperState.setStatus("current")
_SwitchProductId_ObjectIdentity = ObjectIdentity
switchProductId = _SwitchProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 5, 5),
    _SwProdUrl_Type()
)
swProdUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdUrl.setStatus("current")
_SwIdentifier_Type = Integer32
_SwIdentifier_Object = MibScalar
swIdentifier = _SwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 5, 6),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 5, 7),
    _SwChassisServiceTag_Type()
)
swChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swChassisServiceTag.setStatus("current")
_SwitchIndivPowerTable_Object = MibTable
switchIndivPowerTable = _SwitchIndivPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 6)
)
if mibBuilder.loadTexts:
    switchIndivPowerTable.setStatus("current")
_SwitchIndivPowerEntry_Object = MibTableRow
switchIndivPowerEntry = _SwitchIndivPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 6, 1)
)
switchIndivPowerEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "swIndivPowerUnitIndex"),
    (0, "ECS2100-28PP-MIB", "swIndivPowerIndex"),
)
if mibBuilder.loadTexts:
    switchIndivPowerEntry.setStatus("current")


class _SwIndivPowerUnitIndex_Type(Integer32):
    """Custom type swIndivPowerUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SwIndivPowerUnitIndex_Type.__name__ = "Integer32"
_SwIndivPowerUnitIndex_Object = MibTableColumn
swIndivPowerUnitIndex = _SwIndivPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 6, 1, 3),
    _SwIndivPowerStatus_Type()
)
swIndivPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivPowerStatus.setStatus("current")


class _SwitchJumboFrameStatus_Type(Integer32):
    """Custom type switchJumboFrameStatus based on Integer32"""
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


_SwitchJumboFrameStatus_Type.__name__ = "Integer32"
_SwitchJumboFrameStatus_Object = MibScalar
switchJumboFrameStatus = _SwitchJumboFrameStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 7),
    _SwitchJumboFrameStatus_Type()
)
switchJumboFrameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchJumboFrameStatus.setStatus("current")
_AmtrMgt_ObjectIdentity = ObjectIdentity
amtrMgt = _AmtrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 8)
)
_AmtrMacAddrAgingStatus_Type = EnabledStatus
_AmtrMacAddrAgingStatus_Object = MibScalar
amtrMacAddrAgingStatus = _AmtrMacAddrAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 1, 8, 3),
    _AmtrMacAddrAgingStatus_Type()
)
amtrMacAddrAgingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amtrMacAddrAgingStatus.setStatus("current")
_PortMgt_ObjectIdentity = ObjectIdentity
portMgt = _PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1)
)
portEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = InterfaceIndex
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 2),
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("hundredBaseFX", 3),
          ("hundredBaseFxScMultiMode", 10),
          ("hundredBaseFxScSingleMode", 9),
          ("hundredBaseTX", 2),
          ("other", 1),
          ("tenG", 12),
          ("thousandBaseCX", 11),
          ("thousandBaseGBIC", 7),
          ("thousandBaseLX", 5),
          ("thousandBaseSX", 4),
          ("thousandBaseSfp", 8),
          ("thousandBaseT", 6))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 3),
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("fullDuplex10g", 9),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6),
          ("halfDuplex10g", 8),
          ("reserved", 1))
    )


_PortSpeedDpxCfg_Type.__name__ = "Integer32"
_PortSpeedDpxCfg_Object = MibTableColumn
portSpeedDpxCfg = _PortSpeedDpxCfg_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 4),
    _PortSpeedDpxCfg_Type()
)
portSpeedDpxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedDpxCfg.setStatus("current")


class _PortFlowCtrlCfg_Type(Integer32):
    """Custom type portFlowCtrlCfg based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("rx", 6),
          ("tx", 5))
    )


_PortFlowCtrlCfg_Type.__name__ = "Integer32"
_PortFlowCtrlCfg_Object = MibTableColumn
portFlowCtrlCfg = _PortFlowCtrlCfg_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 5),
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
          ("portCap10gFull", 7),
          ("portCap10gHalf", 6),
          ("portCap10half", 0),
          ("portCapFlowCtrl", 15),
          ("portCapSym", 14),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("reserved8", 8),
          ("reserved9", 9))
    )

_PortCapabilities_Type.__name__ = "Bits"
_PortCapabilities_Object = MibTableColumn
portCapabilities = _PortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")
_PortAutonegotiation_Type = EnabledStatus
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 7),
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("fullDuplex10g", 9),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6),
          ("halfDuplex10g", 8))
    )


_PortSpeedDpxStatus_Type.__name__ = "Integer32"
_PortSpeedDpxStatus_Object = MibTableColumn
portSpeedDpxStatus = _PortSpeedDpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_PortTrunkIndex_Type = Integer32
_PortTrunkIndex_Object = MibTableColumn
portTrunkIndex = _PortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 10),
    _PortTrunkIndex_Type()
)
portTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkIndex.setStatus("current")


class _PortComboForcedMode_Type(Integer32):
    """Custom type portComboForcedMode based on Integer32"""
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
        *(("none", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("reserved5", 5),
          ("sfpForced", 4))
    )


_PortComboForcedMode_Type.__name__ = "Integer32"
_PortComboForcedMode_Object = MibTableColumn
portComboForcedMode = _PortComboForcedMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 12),
    _PortComboForcedMode_Type()
)
portComboForcedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portComboForcedMode.setStatus("current")


class _PortMasterSlaveModeCfg_Type(Integer32):
    """Custom type portMasterSlaveModeCfg based on Integer32"""
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
        *(("auto", 3),
          ("autoPreferMaster", 4),
          ("autoPreferSlave", 5),
          ("master", 1),
          ("slave", 2))
    )


_PortMasterSlaveModeCfg_Type.__name__ = "Integer32"
_PortMasterSlaveModeCfg_Object = MibTableColumn
portMasterSlaveModeCfg = _PortMasterSlaveModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 15),
    _PortMasterSlaveModeCfg_Type()
)
portMasterSlaveModeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMasterSlaveModeCfg.setStatus("current")


class _PortMacAddrLearningStatus_Type(EnabledStatus):
    """Custom type portMacAddrLearningStatus based on EnabledStatus"""


_PortMacAddrLearningStatus_Object = MibTableColumn
portMacAddrLearningStatus = _PortMacAddrLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 17),
    _PortMacAddrLearningStatus_Type()
)
portMacAddrLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMacAddrLearningStatus.setStatus("current")
_PortMacAddrLearningCount_Type = Counter32
_PortMacAddrLearningCount_Object = MibTableColumn
portMacAddrLearningCount = _PortMacAddrLearningCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 18),
    _PortMacAddrLearningCount_Type()
)
portMacAddrLearningCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacAddrLearningCount.setStatus("current")
_PortUpTime_Type = TimeTicks
_PortUpTime_Object = MibTableColumn
portUpTime = _PortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 19),
    _PortUpTime_Type()
)
portUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUpTime.setStatus("current")


class _PortShutdownReason_Type(Bits):
    """Custom type portShutdownReason based on Bits"""
    namedValues = NamedValues(
        *(("admin", 0),
          ("atcBstorm", 7),
          ("atcMstorm", 8),
          ("lbd", 6),
          ("networkAccessPortDynamicQos", 4),
          ("networkAccessPortLinkDetection", 3),
          ("portSec", 5),
          ("stpBpduGuard", 2),
          ("stpLbd", 1),
          ("udld", 9))
    )

_PortShutdownReason_Type.__name__ = "Bits"
_PortShutdownReason_Object = MibTableColumn
portShutdownReason = _PortShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 1, 1, 20),
    _PortShutdownReason_Type()
)
portShutdownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portShutdownReason.setStatus("current")
_CableDiagMgt_ObjectIdentity = ObjectIdentity
cableDiagMgt = _CableDiagMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3)
)
_CableDiagCtlAction_Type = Integer32
_CableDiagCtlAction_Object = MibScalar
cableDiagCtlAction = _CableDiagCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 1),
    _CableDiagCtlAction_Type()
)
cableDiagCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableDiagCtlAction.setStatus("current")
_CableDiagResultTable_Object = MibTable
cableDiagResultTable = _CableDiagResultTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cableDiagResultTable.setStatus("current")
_CableDiagResultEntry_Object = MibTableRow
cableDiagResultEntry = _CableDiagResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1)
)
cableDiagResultEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "cableDiagResultIfIndex"),
)
if mibBuilder.loadTexts:
    cableDiagResultEntry.setStatus("current")
_CableDiagResultIfIndex_Type = InterfaceIndex
_CableDiagResultIfIndex_Object = MibTableColumn
cableDiagResultIfIndex = _CableDiagResultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 1),
    _CableDiagResultIfIndex_Type()
)
cableDiagResultIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cableDiagResultIfIndex.setStatus("current")


class _CableDiagResultStatusPairA_Type(Integer32):
    """Custom type cableDiagResultStatusPairA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("failed", 9),
          ("impedanceMismatch", 8),
          ("noCable", 11),
          ("notSupported", 10),
          ("notTestedYet", 1),
          ("ok", 2),
          ("open", 3),
          ("short", 4))
    )


_CableDiagResultStatusPairA_Type.__name__ = "Integer32"
_CableDiagResultStatusPairA_Object = MibTableColumn
cableDiagResultStatusPairA = _CableDiagResultStatusPairA_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 2),
    _CableDiagResultStatusPairA_Type()
)
cableDiagResultStatusPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultStatusPairA.setStatus("current")


class _CableDiagResultStatusPairB_Type(Integer32):
    """Custom type cableDiagResultStatusPairB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("failed", 9),
          ("impedanceMismatch", 8),
          ("noCable", 11),
          ("notSupported", 10),
          ("notTestedYet", 1),
          ("ok", 2),
          ("open", 3),
          ("short", 4))
    )


_CableDiagResultStatusPairB_Type.__name__ = "Integer32"
_CableDiagResultStatusPairB_Object = MibTableColumn
cableDiagResultStatusPairB = _CableDiagResultStatusPairB_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 3),
    _CableDiagResultStatusPairB_Type()
)
cableDiagResultStatusPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultStatusPairB.setStatus("current")


class _CableDiagResultStatusPairC_Type(Integer32):
    """Custom type cableDiagResultStatusPairC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("failed", 9),
          ("impedanceMismatch", 8),
          ("noCable", 11),
          ("notSupported", 10),
          ("notTestedYet", 1),
          ("ok", 2),
          ("open", 3),
          ("short", 4))
    )


_CableDiagResultStatusPairC_Type.__name__ = "Integer32"
_CableDiagResultStatusPairC_Object = MibTableColumn
cableDiagResultStatusPairC = _CableDiagResultStatusPairC_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 4),
    _CableDiagResultStatusPairC_Type()
)
cableDiagResultStatusPairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultStatusPairC.setStatus("current")


class _CableDiagResultStatusPairD_Type(Integer32):
    """Custom type cableDiagResultStatusPairD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("failed", 9),
          ("impedanceMismatch", 8),
          ("noCable", 11),
          ("notSupported", 10),
          ("notTestedYet", 1),
          ("ok", 2),
          ("open", 3),
          ("short", 4))
    )


_CableDiagResultStatusPairD_Type.__name__ = "Integer32"
_CableDiagResultStatusPairD_Object = MibTableColumn
cableDiagResultStatusPairD = _CableDiagResultStatusPairD_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 5),
    _CableDiagResultStatusPairD_Type()
)
cableDiagResultStatusPairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultStatusPairD.setStatus("current")
_CableDiagResultDistancePairA_Type = Integer32
_CableDiagResultDistancePairA_Object = MibTableColumn
cableDiagResultDistancePairA = _CableDiagResultDistancePairA_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 6),
    _CableDiagResultDistancePairA_Type()
)
cableDiagResultDistancePairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultDistancePairA.setStatus("current")
_CableDiagResultDistancePairB_Type = Integer32
_CableDiagResultDistancePairB_Object = MibTableColumn
cableDiagResultDistancePairB = _CableDiagResultDistancePairB_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 7),
    _CableDiagResultDistancePairB_Type()
)
cableDiagResultDistancePairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultDistancePairB.setStatus("current")
_CableDiagResultDistancePairC_Type = Integer32
_CableDiagResultDistancePairC_Object = MibTableColumn
cableDiagResultDistancePairC = _CableDiagResultDistancePairC_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 8),
    _CableDiagResultDistancePairC_Type()
)
cableDiagResultDistancePairC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultDistancePairC.setStatus("current")
_CableDiagResultDistancePairD_Type = Integer32
_CableDiagResultDistancePairD_Object = MibTableColumn
cableDiagResultDistancePairD = _CableDiagResultDistancePairD_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 9),
    _CableDiagResultDistancePairD_Type()
)
cableDiagResultDistancePairD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultDistancePairD.setStatus("current")


class _CableDiagResultTime_Type(DisplayString):
    """Custom type cableDiagResultTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CableDiagResultTime_Type.__name__ = "DisplayString"
_CableDiagResultTime_Object = MibTableColumn
cableDiagResultTime = _CableDiagResultTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 3, 2, 1, 11),
    _CableDiagResultTime_Type()
)
cableDiagResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultTime.setStatus("current")
_PortUtilTable_Object = MibTable
portUtilTable = _PortUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 6)
)
if mibBuilder.loadTexts:
    portUtilTable.setStatus("current")
_PortUtilEntry_Object = MibTableRow
portUtilEntry = _PortUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 6, 1)
)
portUtilEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "portUtilIfIndex"),
)
if mibBuilder.loadTexts:
    portUtilEntry.setStatus("current")
_PortUtilIfIndex_Type = InterfaceIndex
_PortUtilIfIndex_Object = MibTableColumn
portUtilIfIndex = _PortUtilIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 6, 1, 1),
    _PortUtilIfIndex_Type()
)
portUtilIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portUtilIfIndex.setStatus("current")
_PortInOctetRate_Type = Counter64
_PortInOctetRate_Object = MibTableColumn
portInOctetRate = _PortInOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 6, 1, 2),
    _PortInOctetRate_Type()
)
portInOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInOctetRate.setStatus("current")
_PortInPacketRate_Type = Counter64
_PortInPacketRate_Object = MibTableColumn
portInPacketRate = _PortInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 6, 1, 3),
    _PortInPacketRate_Type()
)
portInPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInPacketRate.setStatus("current")
_PortInUtil_Type = Integer32
_PortInUtil_Object = MibTableColumn
portInUtil = _PortInUtil_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 6, 1, 4),
    _PortInUtil_Type()
)
portInUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInUtil.setStatus("current")
_PortOutOctetRate_Type = Counter64
_PortOutOctetRate_Object = MibTableColumn
portOutOctetRate = _PortOutOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 6, 1, 5),
    _PortOutOctetRate_Type()
)
portOutOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutOctetRate.setStatus("current")
_PortOutPacketRate_Type = Counter64
_PortOutPacketRate_Object = MibTableColumn
portOutPacketRate = _PortOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 6, 1, 6),
    _PortOutPacketRate_Type()
)
portOutPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutPacketRate.setStatus("current")
_PortOutUtil_Type = Integer32
_PortOutUtil_Object = MibTableColumn
portOutUtil = _PortOutUtil_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 6, 1, 7),
    _PortOutUtil_Type()
)
portOutUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutUtil.setStatus("current")
_PortHist_ObjectIdentity = ObjectIdentity
portHist = _PortHist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8)
)
_PortHistControlTable_Object = MibTable
portHistControlTable = _PortHistControlTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    portHistControlTable.setStatus("current")
_PortHistControlEntry_Object = MibTableRow
portHistControlEntry = _PortHistControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 1, 1)
)
portHistControlEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "portHistControlIndex"),
)
if mibBuilder.loadTexts:
    portHistControlEntry.setStatus("current")


class _PortHistControlIndex_Type(Integer32):
    """Custom type portHistControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortHistControlIndex_Type.__name__ = "Integer32"
_PortHistControlIndex_Object = MibTableColumn
portHistControlIndex = _PortHistControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 1, 1, 1),
    _PortHistControlIndex_Type()
)
portHistControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistControlIndex.setStatus("current")


class _PortHistControlName_Type(DisplayString):
    """Custom type portHistControlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PortHistControlName_Type.__name__ = "DisplayString"
_PortHistControlName_Object = MibTableColumn
portHistControlName = _PortHistControlName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 1, 1, 2),
    _PortHistControlName_Type()
)
portHistControlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portHistControlName.setStatus("current")
_PortHistControlDataSource_Type = InterfaceIndex
_PortHistControlDataSource_Object = MibTableColumn
portHistControlDataSource = _PortHistControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 1, 1, 3),
    _PortHistControlDataSource_Type()
)
portHistControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portHistControlDataSource.setStatus("current")


class _PortHistControlInterval_Type(Integer32):
    """Custom type portHistControlInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_PortHistControlInterval_Type.__name__ = "Integer32"
_PortHistControlInterval_Object = MibTableColumn
portHistControlInterval = _PortHistControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 1, 1, 4),
    _PortHistControlInterval_Type()
)
portHistControlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portHistControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    portHistControlInterval.setUnits("Minutes")


class _PortHistControlBucketsRequested_Type(Integer32):
    """Custom type portHistControlBucketsRequested based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PortHistControlBucketsRequested_Type.__name__ = "Integer32"
_PortHistControlBucketsRequested_Object = MibTableColumn
portHistControlBucketsRequested = _PortHistControlBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 1, 1, 5),
    _PortHistControlBucketsRequested_Type()
)
portHistControlBucketsRequested.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portHistControlBucketsRequested.setStatus("current")


class _PortHistControlBucketsGranted_Type(Integer32):
    """Custom type portHistControlBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PortHistControlBucketsGranted_Type.__name__ = "Integer32"
_PortHistControlBucketsGranted_Object = MibTableColumn
portHistControlBucketsGranted = _PortHistControlBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 1, 1, 6),
    _PortHistControlBucketsGranted_Type()
)
portHistControlBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistControlBucketsGranted.setStatus("current")
_PortHistControlStatus_Type = RowStatus
_PortHistControlStatus_Object = MibTableColumn
portHistControlStatus = _PortHistControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 1, 1, 7),
    _PortHistControlStatus_Type()
)
portHistControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portHistControlStatus.setStatus("current")
_PortHistCurrentTable_Object = MibTable
portHistCurrentTable = _PortHistCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    portHistCurrentTable.setStatus("current")
_PortHistCurrentEntry_Object = MibTableRow
portHistCurrentEntry = _PortHistCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1)
)
portHistCurrentEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "portHistCurrentIndex"),
)
if mibBuilder.loadTexts:
    portHistCurrentEntry.setStatus("current")


class _PortHistCurrentIndex_Type(Integer32):
    """Custom type portHistCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortHistCurrentIndex_Type.__name__ = "Integer32"
_PortHistCurrentIndex_Object = MibTableColumn
portHistCurrentIndex = _PortHistCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 1),
    _PortHistCurrentIndex_Type()
)
portHistCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentIndex.setStatus("current")


class _PortHistCurrentSampleIndex_Type(Integer32):
    """Custom type portHistCurrentSampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortHistCurrentSampleIndex_Type.__name__ = "Integer32"
_PortHistCurrentSampleIndex_Object = MibTableColumn
portHistCurrentSampleIndex = _PortHistCurrentSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 2),
    _PortHistCurrentSampleIndex_Type()
)
portHistCurrentSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentSampleIndex.setStatus("current")
_PortHistCurrentIntervalStart_Type = TimeTicks
_PortHistCurrentIntervalStart_Object = MibTableColumn
portHistCurrentIntervalStart = _PortHistCurrentIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 3),
    _PortHistCurrentIntervalStart_Type()
)
portHistCurrentIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentIntervalStart.setStatus("current")
_PortHistCurrentInOctets_Type = Counter64
_PortHistCurrentInOctets_Object = MibTableColumn
portHistCurrentInOctets = _PortHistCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 4),
    _PortHistCurrentInOctets_Type()
)
portHistCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentInOctets.setStatus("current")
_PortHistCurrentInUcastPkts_Type = Counter64
_PortHistCurrentInUcastPkts_Object = MibTableColumn
portHistCurrentInUcastPkts = _PortHistCurrentInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 5),
    _PortHistCurrentInUcastPkts_Type()
)
portHistCurrentInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentInUcastPkts.setStatus("current")
_PortHistCurrentInMulticastPkts_Type = Counter64
_PortHistCurrentInMulticastPkts_Object = MibTableColumn
portHistCurrentInMulticastPkts = _PortHistCurrentInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 6),
    _PortHistCurrentInMulticastPkts_Type()
)
portHistCurrentInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentInMulticastPkts.setStatus("current")
_PortHistCurrentInBroadcastPkts_Type = Counter64
_PortHistCurrentInBroadcastPkts_Object = MibTableColumn
portHistCurrentInBroadcastPkts = _PortHistCurrentInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 7),
    _PortHistCurrentInBroadcastPkts_Type()
)
portHistCurrentInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentInBroadcastPkts.setStatus("current")
_PortHistCurrentInDiscards_Type = Counter64
_PortHistCurrentInDiscards_Object = MibTableColumn
portHistCurrentInDiscards = _PortHistCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 8),
    _PortHistCurrentInDiscards_Type()
)
portHistCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentInDiscards.setStatus("current")
_PortHistCurrentInErrors_Type = Counter64
_PortHistCurrentInErrors_Object = MibTableColumn
portHistCurrentInErrors = _PortHistCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 9),
    _PortHistCurrentInErrors_Type()
)
portHistCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentInErrors.setStatus("current")
_PortHistCurrentInUnknownProtos_Type = Counter64
_PortHistCurrentInUnknownProtos_Object = MibTableColumn
portHistCurrentInUnknownProtos = _PortHistCurrentInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 10),
    _PortHistCurrentInUnknownProtos_Type()
)
portHistCurrentInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentInUnknownProtos.setStatus("current")
_PortHistCurrentOutOctets_Type = Counter64
_PortHistCurrentOutOctets_Object = MibTableColumn
portHistCurrentOutOctets = _PortHistCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 11),
    _PortHistCurrentOutOctets_Type()
)
portHistCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentOutOctets.setStatus("current")
_PortHistCurrentOutUcastPkts_Type = Counter64
_PortHistCurrentOutUcastPkts_Object = MibTableColumn
portHistCurrentOutUcastPkts = _PortHistCurrentOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 12),
    _PortHistCurrentOutUcastPkts_Type()
)
portHistCurrentOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentOutUcastPkts.setStatus("current")
_PortHistCurrentOutMulticastPkts_Type = Counter64
_PortHistCurrentOutMulticastPkts_Object = MibTableColumn
portHistCurrentOutMulticastPkts = _PortHistCurrentOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 13),
    _PortHistCurrentOutMulticastPkts_Type()
)
portHistCurrentOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentOutMulticastPkts.setStatus("current")
_PortHistCurrentOutBroadcastPkts_Type = Counter64
_PortHistCurrentOutBroadcastPkts_Object = MibTableColumn
portHistCurrentOutBroadcastPkts = _PortHistCurrentOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 14),
    _PortHistCurrentOutBroadcastPkts_Type()
)
portHistCurrentOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentOutBroadcastPkts.setStatus("current")
_PortHistCurrentOutDiscards_Type = Counter64
_PortHistCurrentOutDiscards_Object = MibTableColumn
portHistCurrentOutDiscards = _PortHistCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 15),
    _PortHistCurrentOutDiscards_Type()
)
portHistCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentOutDiscards.setStatus("current")
_PortHistCurrentOutErrors_Type = Counter64
_PortHistCurrentOutErrors_Object = MibTableColumn
portHistCurrentOutErrors = _PortHistCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 16),
    _PortHistCurrentOutErrors_Type()
)
portHistCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentOutErrors.setStatus("current")


class _PortHistCurrentInUtilization_Type(Integer32):
    """Custom type portHistCurrentInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PortHistCurrentInUtilization_Type.__name__ = "Integer32"
_PortHistCurrentInUtilization_Object = MibTableColumn
portHistCurrentInUtilization = _PortHistCurrentInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 17),
    _PortHistCurrentInUtilization_Type()
)
portHistCurrentInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentInUtilization.setStatus("current")


class _PortHistCurrentOutUtilization_Type(Integer32):
    """Custom type portHistCurrentOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PortHistCurrentOutUtilization_Type.__name__ = "Integer32"
_PortHistCurrentOutUtilization_Object = MibTableColumn
portHistCurrentOutUtilization = _PortHistCurrentOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 2, 1, 18),
    _PortHistCurrentOutUtilization_Type()
)
portHistCurrentOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistCurrentOutUtilization.setStatus("current")
_PortHistPreviousTable_Object = MibTable
portHistPreviousTable = _PortHistPreviousTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    portHistPreviousTable.setStatus("current")
_PortHistPreviousEntry_Object = MibTableRow
portHistPreviousEntry = _PortHistPreviousEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1)
)
portHistPreviousEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "portHistPreviousIndex"),
    (0, "ECS2100-28PP-MIB", "portHistPreviousSampleIndex"),
)
if mibBuilder.loadTexts:
    portHistPreviousEntry.setStatus("current")


class _PortHistPreviousIndex_Type(Integer32):
    """Custom type portHistPreviousIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortHistPreviousIndex_Type.__name__ = "Integer32"
_PortHistPreviousIndex_Object = MibTableColumn
portHistPreviousIndex = _PortHistPreviousIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 1),
    _PortHistPreviousIndex_Type()
)
portHistPreviousIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousIndex.setStatus("current")


class _PortHistPreviousSampleIndex_Type(Integer32):
    """Custom type portHistPreviousSampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortHistPreviousSampleIndex_Type.__name__ = "Integer32"
_PortHistPreviousSampleIndex_Object = MibTableColumn
portHistPreviousSampleIndex = _PortHistPreviousSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 2),
    _PortHistPreviousSampleIndex_Type()
)
portHistPreviousSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousSampleIndex.setStatus("current")
_PortHistPreviousIntervalStart_Type = TimeTicks
_PortHistPreviousIntervalStart_Object = MibTableColumn
portHistPreviousIntervalStart = _PortHistPreviousIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 3),
    _PortHistPreviousIntervalStart_Type()
)
portHistPreviousIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousIntervalStart.setStatus("current")
_PortHistPreviousInOctets_Type = Counter64
_PortHistPreviousInOctets_Object = MibTableColumn
portHistPreviousInOctets = _PortHistPreviousInOctets_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 4),
    _PortHistPreviousInOctets_Type()
)
portHistPreviousInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousInOctets.setStatus("current")
_PortHistPreviousInUcastPkts_Type = Counter64
_PortHistPreviousInUcastPkts_Object = MibTableColumn
portHistPreviousInUcastPkts = _PortHistPreviousInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 5),
    _PortHistPreviousInUcastPkts_Type()
)
portHistPreviousInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousInUcastPkts.setStatus("current")
_PortHistPreviousInMulticastPkts_Type = Counter64
_PortHistPreviousInMulticastPkts_Object = MibTableColumn
portHistPreviousInMulticastPkts = _PortHistPreviousInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 6),
    _PortHistPreviousInMulticastPkts_Type()
)
portHistPreviousInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousInMulticastPkts.setStatus("current")
_PortHistPreviousInBroadcastPkts_Type = Counter64
_PortHistPreviousInBroadcastPkts_Object = MibTableColumn
portHistPreviousInBroadcastPkts = _PortHistPreviousInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 7),
    _PortHistPreviousInBroadcastPkts_Type()
)
portHistPreviousInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousInBroadcastPkts.setStatus("current")
_PortHistPreviousInDiscards_Type = Counter64
_PortHistPreviousInDiscards_Object = MibTableColumn
portHistPreviousInDiscards = _PortHistPreviousInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 8),
    _PortHistPreviousInDiscards_Type()
)
portHistPreviousInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousInDiscards.setStatus("current")
_PortHistPreviousInErrors_Type = Counter64
_PortHistPreviousInErrors_Object = MibTableColumn
portHistPreviousInErrors = _PortHistPreviousInErrors_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 9),
    _PortHistPreviousInErrors_Type()
)
portHistPreviousInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousInErrors.setStatus("current")
_PortHistPreviousInUnknownProtos_Type = Counter64
_PortHistPreviousInUnknownProtos_Object = MibTableColumn
portHistPreviousInUnknownProtos = _PortHistPreviousInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 10),
    _PortHistPreviousInUnknownProtos_Type()
)
portHistPreviousInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousInUnknownProtos.setStatus("current")
_PortHistPreviousOutOctets_Type = Counter64
_PortHistPreviousOutOctets_Object = MibTableColumn
portHistPreviousOutOctets = _PortHistPreviousOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 11),
    _PortHistPreviousOutOctets_Type()
)
portHistPreviousOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousOutOctets.setStatus("current")
_PortHistPreviousOutUcastPkts_Type = Counter64
_PortHistPreviousOutUcastPkts_Object = MibTableColumn
portHistPreviousOutUcastPkts = _PortHistPreviousOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 12),
    _PortHistPreviousOutUcastPkts_Type()
)
portHistPreviousOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousOutUcastPkts.setStatus("current")
_PortHistPreviousOutMulticastPkts_Type = Counter64
_PortHistPreviousOutMulticastPkts_Object = MibTableColumn
portHistPreviousOutMulticastPkts = _PortHistPreviousOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 13),
    _PortHistPreviousOutMulticastPkts_Type()
)
portHistPreviousOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousOutMulticastPkts.setStatus("current")
_PortHistPreviousOutBroadcastPkts_Type = Counter64
_PortHistPreviousOutBroadcastPkts_Object = MibTableColumn
portHistPreviousOutBroadcastPkts = _PortHistPreviousOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 14),
    _PortHistPreviousOutBroadcastPkts_Type()
)
portHistPreviousOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousOutBroadcastPkts.setStatus("current")
_PortHistPreviousOutDiscards_Type = Counter64
_PortHistPreviousOutDiscards_Object = MibTableColumn
portHistPreviousOutDiscards = _PortHistPreviousOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 15),
    _PortHistPreviousOutDiscards_Type()
)
portHistPreviousOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousOutDiscards.setStatus("current")
_PortHistPreviousOutErrors_Type = Counter64
_PortHistPreviousOutErrors_Object = MibTableColumn
portHistPreviousOutErrors = _PortHistPreviousOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 16),
    _PortHistPreviousOutErrors_Type()
)
portHistPreviousOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousOutErrors.setStatus("current")


class _PortHistPreviousInUtilization_Type(Integer32):
    """Custom type portHistPreviousInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PortHistPreviousInUtilization_Type.__name__ = "Integer32"
_PortHistPreviousInUtilization_Object = MibTableColumn
portHistPreviousInUtilization = _PortHistPreviousInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 17),
    _PortHistPreviousInUtilization_Type()
)
portHistPreviousInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousInUtilization.setStatus("current")


class _PortHistPreviousOutUtilization_Type(Integer32):
    """Custom type portHistPreviousOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PortHistPreviousOutUtilization_Type.__name__ = "Integer32"
_PortHistPreviousOutUtilization_Object = MibTableColumn
portHistPreviousOutUtilization = _PortHistPreviousOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 8, 3, 1, 18),
    _PortHistPreviousOutUtilization_Type()
)
portHistPreviousOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portHistPreviousOutUtilization.setStatus("current")
_PortMediaInfoTable_Object = MibTable
portMediaInfoTable = _PortMediaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10)
)
if mibBuilder.loadTexts:
    portMediaInfoTable.setStatus("current")
_PortMediaInfoEntry_Object = MibTableRow
portMediaInfoEntry = _PortMediaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1)
)
portMediaInfoEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "portMediaInfoIfIndex"),
)
if mibBuilder.loadTexts:
    portMediaInfoEntry.setStatus("current")
_PortMediaInfoIfIndex_Type = InterfaceIndex
_PortMediaInfoIfIndex_Object = MibTableColumn
portMediaInfoIfIndex = _PortMediaInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 1),
    _PortMediaInfoIfIndex_Type()
)
portMediaInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portMediaInfoIfIndex.setStatus("current")


class _PortMediaInfoConnectorType_Type(DisplayString):
    """Custom type portMediaInfoConnectorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoConnectorType_Type.__name__ = "DisplayString"
_PortMediaInfoConnectorType_Object = MibTableColumn
portMediaInfoConnectorType = _PortMediaInfoConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 2),
    _PortMediaInfoConnectorType_Type()
)
portMediaInfoConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoConnectorType.setStatus("current")


class _PortMediaInfoFiberType_Type(DisplayString):
    """Custom type portMediaInfoFiberType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoFiberType_Type.__name__ = "DisplayString"
_PortMediaInfoFiberType_Object = MibTableColumn
portMediaInfoFiberType = _PortMediaInfoFiberType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 3),
    _PortMediaInfoFiberType_Type()
)
portMediaInfoFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoFiberType.setStatus("current")


class _PortMediaInfoEthComplianceCodes_Type(DisplayString):
    """Custom type portMediaInfoEthComplianceCodes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoEthComplianceCodes_Type.__name__ = "DisplayString"
_PortMediaInfoEthComplianceCodes_Object = MibTableColumn
portMediaInfoEthComplianceCodes = _PortMediaInfoEthComplianceCodes_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 4),
    _PortMediaInfoEthComplianceCodes_Type()
)
portMediaInfoEthComplianceCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoEthComplianceCodes.setStatus("current")


class _PortMediaInfoBaudRate_Type(DisplayString):
    """Custom type portMediaInfoBaudRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoBaudRate_Type.__name__ = "DisplayString"
_PortMediaInfoBaudRate_Object = MibTableColumn
portMediaInfoBaudRate = _PortMediaInfoBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 5),
    _PortMediaInfoBaudRate_Type()
)
portMediaInfoBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoBaudRate.setStatus("current")


class _PortMediaInfoVendorOUI_Type(DisplayString):
    """Custom type portMediaInfoVendorOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoVendorOUI_Type.__name__ = "DisplayString"
_PortMediaInfoVendorOUI_Object = MibTableColumn
portMediaInfoVendorOUI = _PortMediaInfoVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 6),
    _PortMediaInfoVendorOUI_Type()
)
portMediaInfoVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoVendorOUI.setStatus("current")


class _PortMediaInfoVendorName_Type(DisplayString):
    """Custom type portMediaInfoVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoVendorName_Type.__name__ = "DisplayString"
_PortMediaInfoVendorName_Object = MibTableColumn
portMediaInfoVendorName = _PortMediaInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 7),
    _PortMediaInfoVendorName_Type()
)
portMediaInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoVendorName.setStatus("current")


class _PortMediaInfoPartNumber_Type(DisplayString):
    """Custom type portMediaInfoPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoPartNumber_Type.__name__ = "DisplayString"
_PortMediaInfoPartNumber_Object = MibTableColumn
portMediaInfoPartNumber = _PortMediaInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 8),
    _PortMediaInfoPartNumber_Type()
)
portMediaInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoPartNumber.setStatus("current")


class _PortMediaInfoRevision_Type(DisplayString):
    """Custom type portMediaInfoRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoRevision_Type.__name__ = "DisplayString"
_PortMediaInfoRevision_Object = MibTableColumn
portMediaInfoRevision = _PortMediaInfoRevision_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 9),
    _PortMediaInfoRevision_Type()
)
portMediaInfoRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoRevision.setStatus("current")


class _PortMediaInfoSerialNumber_Type(DisplayString):
    """Custom type portMediaInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoSerialNumber_Type.__name__ = "DisplayString"
_PortMediaInfoSerialNumber_Object = MibTableColumn
portMediaInfoSerialNumber = _PortMediaInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 10),
    _PortMediaInfoSerialNumber_Type()
)
portMediaInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoSerialNumber.setStatus("current")


class _PortMediaInfoDateCode_Type(DisplayString):
    """Custom type portMediaInfoDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMediaInfoDateCode_Type.__name__ = "DisplayString"
_PortMediaInfoDateCode_Object = MibTableColumn
portMediaInfoDateCode = _PortMediaInfoDateCode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 10, 1, 11),
    _PortMediaInfoDateCode_Type()
)
portMediaInfoDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaInfoDateCode.setStatus("current")
_PortOpticalMonitoringInfoTable_Object = MibTable
portOpticalMonitoringInfoTable = _PortOpticalMonitoringInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 11)
)
if mibBuilder.loadTexts:
    portOpticalMonitoringInfoTable.setStatus("current")
_PortOpticalMonitoringInfoEntry_Object = MibTableRow
portOpticalMonitoringInfoEntry = _PortOpticalMonitoringInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 11, 1)
)
portOpticalMonitoringInfoEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "portOpticalMonitoringInfoIfIndex"),
)
if mibBuilder.loadTexts:
    portOpticalMonitoringInfoEntry.setStatus("current")
_PortOpticalMonitoringInfoIfIndex_Type = InterfaceIndex
_PortOpticalMonitoringInfoIfIndex_Object = MibTableColumn
portOpticalMonitoringInfoIfIndex = _PortOpticalMonitoringInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 11, 1, 1),
    _PortOpticalMonitoringInfoIfIndex_Type()
)
portOpticalMonitoringInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portOpticalMonitoringInfoIfIndex.setStatus("current")


class _PortOpticalMonitoringInfoTemperature_Type(DisplayString):
    """Custom type portOpticalMonitoringInfoTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortOpticalMonitoringInfoTemperature_Type.__name__ = "DisplayString"
_PortOpticalMonitoringInfoTemperature_Object = MibTableColumn
portOpticalMonitoringInfoTemperature = _PortOpticalMonitoringInfoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 11, 1, 2),
    _PortOpticalMonitoringInfoTemperature_Type()
)
portOpticalMonitoringInfoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpticalMonitoringInfoTemperature.setStatus("current")


class _PortOpticalMonitoringInfoVcc_Type(DisplayString):
    """Custom type portOpticalMonitoringInfoVcc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortOpticalMonitoringInfoVcc_Type.__name__ = "DisplayString"
_PortOpticalMonitoringInfoVcc_Object = MibTableColumn
portOpticalMonitoringInfoVcc = _PortOpticalMonitoringInfoVcc_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 11, 1, 3),
    _PortOpticalMonitoringInfoVcc_Type()
)
portOpticalMonitoringInfoVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpticalMonitoringInfoVcc.setStatus("current")


class _PortOpticalMonitoringInfoTxBiasCurrent_Type(DisplayString):
    """Custom type portOpticalMonitoringInfoTxBiasCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortOpticalMonitoringInfoTxBiasCurrent_Type.__name__ = "DisplayString"
_PortOpticalMonitoringInfoTxBiasCurrent_Object = MibTableColumn
portOpticalMonitoringInfoTxBiasCurrent = _PortOpticalMonitoringInfoTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 11, 1, 4),
    _PortOpticalMonitoringInfoTxBiasCurrent_Type()
)
portOpticalMonitoringInfoTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpticalMonitoringInfoTxBiasCurrent.setStatus("current")


class _PortOpticalMonitoringInfoTxPower_Type(DisplayString):
    """Custom type portOpticalMonitoringInfoTxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortOpticalMonitoringInfoTxPower_Type.__name__ = "DisplayString"
_PortOpticalMonitoringInfoTxPower_Object = MibTableColumn
portOpticalMonitoringInfoTxPower = _PortOpticalMonitoringInfoTxPower_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 11, 1, 5),
    _PortOpticalMonitoringInfoTxPower_Type()
)
portOpticalMonitoringInfoTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpticalMonitoringInfoTxPower.setStatus("current")


class _PortOpticalMonitoringInfoRxPower_Type(DisplayString):
    """Custom type portOpticalMonitoringInfoRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortOpticalMonitoringInfoRxPower_Type.__name__ = "DisplayString"
_PortOpticalMonitoringInfoRxPower_Object = MibTableColumn
portOpticalMonitoringInfoRxPower = _PortOpticalMonitoringInfoRxPower_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 11, 1, 6),
    _PortOpticalMonitoringInfoRxPower_Type()
)
portOpticalMonitoringInfoRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpticalMonitoringInfoRxPower.setStatus("current")
_PortTransceiverThresholdInfoTable_Object = MibTable
portTransceiverThresholdInfoTable = _PortTransceiverThresholdInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12)
)
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTable.setStatus("current")
_PortTransceiverThresholdInfoEntry_Object = MibTableRow
portTransceiverThresholdInfoEntry = _PortTransceiverThresholdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1)
)
portTransceiverThresholdInfoEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "portTransceiverThresholdInfoIfIndex"),
)
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoEntry.setStatus("current")
_PortTransceiverThresholdInfoIfIndex_Type = InterfaceIndex
_PortTransceiverThresholdInfoIfIndex_Object = MibTableColumn
portTransceiverThresholdInfoIfIndex = _PortTransceiverThresholdInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 1),
    _PortTransceiverThresholdInfoIfIndex_Type()
)
portTransceiverThresholdInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoIfIndex.setStatus("current")
_PortTransceiverThresholdInfoTemperatureLowAlarm_Type = Integer32
_PortTransceiverThresholdInfoTemperatureLowAlarm_Object = MibTableColumn
portTransceiverThresholdInfoTemperatureLowAlarm = _PortTransceiverThresholdInfoTemperatureLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 2),
    _PortTransceiverThresholdInfoTemperatureLowAlarm_Type()
)
portTransceiverThresholdInfoTemperatureLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTemperatureLowAlarm.setStatus("current")
_PortTransceiverThresholdInfoTemperatureLowWarn_Type = Integer32
_PortTransceiverThresholdInfoTemperatureLowWarn_Object = MibTableColumn
portTransceiverThresholdInfoTemperatureLowWarn = _PortTransceiverThresholdInfoTemperatureLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 3),
    _PortTransceiverThresholdInfoTemperatureLowWarn_Type()
)
portTransceiverThresholdInfoTemperatureLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTemperatureLowWarn.setStatus("current")
_PortTransceiverThresholdInfoTemperatureHighWarn_Type = Integer32
_PortTransceiverThresholdInfoTemperatureHighWarn_Object = MibTableColumn
portTransceiverThresholdInfoTemperatureHighWarn = _PortTransceiverThresholdInfoTemperatureHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 4),
    _PortTransceiverThresholdInfoTemperatureHighWarn_Type()
)
portTransceiverThresholdInfoTemperatureHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTemperatureHighWarn.setStatus("current")
_PortTransceiverThresholdInfoTemperatureHighAlarm_Type = Integer32
_PortTransceiverThresholdInfoTemperatureHighAlarm_Object = MibTableColumn
portTransceiverThresholdInfoTemperatureHighAlarm = _PortTransceiverThresholdInfoTemperatureHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 5),
    _PortTransceiverThresholdInfoTemperatureHighAlarm_Type()
)
portTransceiverThresholdInfoTemperatureHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTemperatureHighAlarm.setStatus("current")
_PortTransceiverThresholdInfoVccLowAlarm_Type = Integer32
_PortTransceiverThresholdInfoVccLowAlarm_Object = MibTableColumn
portTransceiverThresholdInfoVccLowAlarm = _PortTransceiverThresholdInfoVccLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 6),
    _PortTransceiverThresholdInfoVccLowAlarm_Type()
)
portTransceiverThresholdInfoVccLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoVccLowAlarm.setStatus("current")
_PortTransceiverThresholdInfoVccLowWarn_Type = Integer32
_PortTransceiverThresholdInfoVccLowWarn_Object = MibTableColumn
portTransceiverThresholdInfoVccLowWarn = _PortTransceiverThresholdInfoVccLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 7),
    _PortTransceiverThresholdInfoVccLowWarn_Type()
)
portTransceiverThresholdInfoVccLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoVccLowWarn.setStatus("current")
_PortTransceiverThresholdInfoVccHighWarn_Type = Integer32
_PortTransceiverThresholdInfoVccHighWarn_Object = MibTableColumn
portTransceiverThresholdInfoVccHighWarn = _PortTransceiverThresholdInfoVccHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 8),
    _PortTransceiverThresholdInfoVccHighWarn_Type()
)
portTransceiverThresholdInfoVccHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoVccHighWarn.setStatus("current")
_PortTransceiverThresholdInfoVccHighAlarm_Type = Integer32
_PortTransceiverThresholdInfoVccHighAlarm_Object = MibTableColumn
portTransceiverThresholdInfoVccHighAlarm = _PortTransceiverThresholdInfoVccHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 9),
    _PortTransceiverThresholdInfoVccHighAlarm_Type()
)
portTransceiverThresholdInfoVccHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoVccHighAlarm.setStatus("current")
_PortTransceiverThresholdInfoTxBiasCurrentLowAlarm_Type = Integer32
_PortTransceiverThresholdInfoTxBiasCurrentLowAlarm_Object = MibTableColumn
portTransceiverThresholdInfoTxBiasCurrentLowAlarm = _PortTransceiverThresholdInfoTxBiasCurrentLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 10),
    _PortTransceiverThresholdInfoTxBiasCurrentLowAlarm_Type()
)
portTransceiverThresholdInfoTxBiasCurrentLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTxBiasCurrentLowAlarm.setStatus("current")
_PortTransceiverThresholdInfoTxBiasCurrentLowWarn_Type = Integer32
_PortTransceiverThresholdInfoTxBiasCurrentLowWarn_Object = MibTableColumn
portTransceiverThresholdInfoTxBiasCurrentLowWarn = _PortTransceiverThresholdInfoTxBiasCurrentLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 11),
    _PortTransceiverThresholdInfoTxBiasCurrentLowWarn_Type()
)
portTransceiverThresholdInfoTxBiasCurrentLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTxBiasCurrentLowWarn.setStatus("current")
_PortTransceiverThresholdInfoTxBiasCurrentHighWarn_Type = Integer32
_PortTransceiverThresholdInfoTxBiasCurrentHighWarn_Object = MibTableColumn
portTransceiverThresholdInfoTxBiasCurrentHighWarn = _PortTransceiverThresholdInfoTxBiasCurrentHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 12),
    _PortTransceiverThresholdInfoTxBiasCurrentHighWarn_Type()
)
portTransceiverThresholdInfoTxBiasCurrentHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTxBiasCurrentHighWarn.setStatus("current")
_PortTransceiverThresholdInfoTxBiasCurrentHighAlarm_Type = Integer32
_PortTransceiverThresholdInfoTxBiasCurrentHighAlarm_Object = MibTableColumn
portTransceiverThresholdInfoTxBiasCurrentHighAlarm = _PortTransceiverThresholdInfoTxBiasCurrentHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 13),
    _PortTransceiverThresholdInfoTxBiasCurrentHighAlarm_Type()
)
portTransceiverThresholdInfoTxBiasCurrentHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTxBiasCurrentHighAlarm.setStatus("current")
_PortTransceiverThresholdInfoTxPowerLowAlarm_Type = Integer32
_PortTransceiverThresholdInfoTxPowerLowAlarm_Object = MibTableColumn
portTransceiverThresholdInfoTxPowerLowAlarm = _PortTransceiverThresholdInfoTxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 14),
    _PortTransceiverThresholdInfoTxPowerLowAlarm_Type()
)
portTransceiverThresholdInfoTxPowerLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTxPowerLowAlarm.setStatus("current")
_PortTransceiverThresholdInfoTxPowerLowWarn_Type = Integer32
_PortTransceiverThresholdInfoTxPowerLowWarn_Object = MibTableColumn
portTransceiverThresholdInfoTxPowerLowWarn = _PortTransceiverThresholdInfoTxPowerLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 15),
    _PortTransceiverThresholdInfoTxPowerLowWarn_Type()
)
portTransceiverThresholdInfoTxPowerLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTxPowerLowWarn.setStatus("current")
_PortTransceiverThresholdInfoTxPowerHighWarn_Type = Integer32
_PortTransceiverThresholdInfoTxPowerHighWarn_Object = MibTableColumn
portTransceiverThresholdInfoTxPowerHighWarn = _PortTransceiverThresholdInfoTxPowerHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 16),
    _PortTransceiverThresholdInfoTxPowerHighWarn_Type()
)
portTransceiverThresholdInfoTxPowerHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTxPowerHighWarn.setStatus("current")
_PortTransceiverThresholdInfoTxPowerHighAlarm_Type = Integer32
_PortTransceiverThresholdInfoTxPowerHighAlarm_Object = MibTableColumn
portTransceiverThresholdInfoTxPowerHighAlarm = _PortTransceiverThresholdInfoTxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 17),
    _PortTransceiverThresholdInfoTxPowerHighAlarm_Type()
)
portTransceiverThresholdInfoTxPowerHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoTxPowerHighAlarm.setStatus("current")
_PortTransceiverThresholdInfoRxPowerLowAlarm_Type = Integer32
_PortTransceiverThresholdInfoRxPowerLowAlarm_Object = MibTableColumn
portTransceiverThresholdInfoRxPowerLowAlarm = _PortTransceiverThresholdInfoRxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 18),
    _PortTransceiverThresholdInfoRxPowerLowAlarm_Type()
)
portTransceiverThresholdInfoRxPowerLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoRxPowerLowAlarm.setStatus("current")
_PortTransceiverThresholdInfoRxPowerLowWarn_Type = Integer32
_PortTransceiverThresholdInfoRxPowerLowWarn_Object = MibTableColumn
portTransceiverThresholdInfoRxPowerLowWarn = _PortTransceiverThresholdInfoRxPowerLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 19),
    _PortTransceiverThresholdInfoRxPowerLowWarn_Type()
)
portTransceiverThresholdInfoRxPowerLowWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoRxPowerLowWarn.setStatus("current")
_PortTransceiverThresholdInfoRxPowerHighWarn_Type = Integer32
_PortTransceiverThresholdInfoRxPowerHighWarn_Object = MibTableColumn
portTransceiverThresholdInfoRxPowerHighWarn = _PortTransceiverThresholdInfoRxPowerHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 20),
    _PortTransceiverThresholdInfoRxPowerHighWarn_Type()
)
portTransceiverThresholdInfoRxPowerHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoRxPowerHighWarn.setStatus("current")
_PortTransceiverThresholdInfoRxPowerHighAlarm_Type = Integer32
_PortTransceiverThresholdInfoRxPowerHighAlarm_Object = MibTableColumn
portTransceiverThresholdInfoRxPowerHighAlarm = _PortTransceiverThresholdInfoRxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 21),
    _PortTransceiverThresholdInfoRxPowerHighAlarm_Type()
)
portTransceiverThresholdInfoRxPowerHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdInfoRxPowerHighAlarm.setStatus("current")
_PortTransceiverThresholdAutoMode_Type = TruthValue
_PortTransceiverThresholdAutoMode_Object = MibTableColumn
portTransceiverThresholdAutoMode = _PortTransceiverThresholdAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 12, 1, 22),
    _PortTransceiverThresholdAutoMode_Type()
)
portTransceiverThresholdAutoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTransceiverThresholdAutoMode.setStatus("current")
_PowerSavingTable_Object = MibTable
powerSavingTable = _PowerSavingTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 14)
)
if mibBuilder.loadTexts:
    powerSavingTable.setStatus("current")
_PowerSavingEntry_Object = MibTableRow
powerSavingEntry = _PowerSavingEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 14, 1)
)
powerSavingEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "powerSavingIfIndex"),
)
if mibBuilder.loadTexts:
    powerSavingEntry.setStatus("current")
_PowerSavingIfIndex_Type = InterfaceIndex
_PowerSavingIfIndex_Object = MibTableColumn
powerSavingIfIndex = _PowerSavingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 14, 1, 1),
    _PowerSavingIfIndex_Type()
)
powerSavingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerSavingIfIndex.setStatus("current")
_PowerSavingStatus_Type = EnabledStatus
_PowerSavingStatus_Object = MibTableColumn
powerSavingStatus = _PowerSavingStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 2, 14, 1, 2),
    _PowerSavingStatus_Type()
)
powerSavingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSavingStatus.setStatus("current")
_TrunkMgt_ObjectIdentity = ObjectIdentity
trunkMgt = _TrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3)
)
_TrunkMaxId_Type = Integer32
_TrunkMaxId_Object = MibScalar
trunkMaxId = _TrunkMaxId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3, 1),
    _TrunkMaxId_Type()
)
trunkMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMaxId.setStatus("current")
_TrunkValidNumber_Type = Integer32
_TrunkValidNumber_Object = MibScalar
trunkValidNumber = _TrunkValidNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3, 2),
    _TrunkValidNumber_Type()
)
trunkValidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkValidNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3, 3, 1)
)
trunkEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")


class _TrunkIndex_Type(Integer32):
    """Custom type trunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_TrunkIndex_Type.__name__ = "Integer32"
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3, 3, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3, 3, 1, 3),
    _TrunkCreation_Type()
)
trunkCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCreation.setStatus("current")
_TrunkStatus_Type = ValidStatus
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3, 3, 1, 4),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")


class _TrunkBalanceMode_Type(Integer32):
    """Custom type trunkBalanceMode based on Integer32"""
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
        *(("ipDst", 5),
          ("ipSrc", 4),
          ("ipSrcDst", 6),
          ("macDst", 2),
          ("macSrc", 1),
          ("macSrcDst", 3))
    )


_TrunkBalanceMode_Type.__name__ = "Integer32"
_TrunkBalanceMode_Object = MibScalar
trunkBalanceMode = _TrunkBalanceMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 3, 4),
    _TrunkBalanceMode_Type()
)
trunkBalanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkBalanceMode.setStatus("current")
_LacpMgt_ObjectIdentity = ObjectIdentity
lacpMgt = _LacpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 4)
)
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 4, 1, 1)
)
lacpPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")
_LacpPortIndex_Type = InterfaceIndex
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 4, 1, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")
_LacpPortStatus_Type = EnabledStatus
_LacpPortStatus_Object = MibTableColumn
lacpPortStatus = _LacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 4, 1, 1, 2),
    _LacpPortStatus_Type()
)
lacpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortStatus.setStatus("current")
_StaMgt_ObjectIdentity = ObjectIdentity
staMgt = _StaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5)
)


class _StaSystemStatus_Type(EnabledStatus):
    """Custom type staSystemStatus based on EnabledStatus"""


_StaSystemStatus_Object = MibScalar
staSystemStatus = _StaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 1),
    _StaSystemStatus_Type()
)
staSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemStatus.setStatus("current")
_StaPortTable_Object = MibTable
staPortTable = _StaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2)
)
if mibBuilder.loadTexts:
    staPortTable.setStatus("current")
_StaPortEntry_Object = MibTableRow
staPortEntry = _StaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    staPortEntry.setStatus("current")
_StaPortProtocolMigration_Type = TruthValue
_StaPortProtocolMigration_Object = MibTableColumn
staPortProtocolMigration = _StaPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 3),
    _StaPortProtocolMigration_Type()
)
staPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortProtocolMigration.setStatus("current")
_StaPortOperEdgePort_Type = TruthValue
_StaPortOperEdgePort_Object = MibTableColumn
staPortOperEdgePort = _StaPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 6),
    _StaPortAdminPointToPoint_Type()
)
staPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminPointToPoint.setStatus("current")
_StaPortOperPointToPoint_Type = TruthValue
_StaPortOperPointToPoint_Object = MibTableColumn
staPortOperPointToPoint = _StaPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 7),
    _StaPortOperPointToPoint_Type()
)
staPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperPointToPoint.setStatus("current")


class _StaPortSystemStatus_Type(EnabledStatus):
    """Custom type staPortSystemStatus based on EnabledStatus"""


_StaPortSystemStatus_Object = MibTableColumn
staPortSystemStatus = _StaPortSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 9),
    _StaPortSystemStatus_Type()
)
staPortSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortSystemStatus.setStatus("current")


class _StaPortLongAdminPathCost_Type(Integer32):
    """Custom type staPortLongAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_StaPortLongAdminPathCost_Type.__name__ = "Integer32"
_StaPortLongAdminPathCost_Object = MibTableColumn
staPortLongAdminPathCost = _StaPortLongAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 10),
    _StaPortLongAdminPathCost_Type()
)
staPortLongAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortLongAdminPathCost.setStatus("current")


class _StaPortLongOperPathCost_Type(Integer32):
    """Custom type staPortLongOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StaPortLongOperPathCost_Type.__name__ = "Integer32"
_StaPortLongOperPathCost_Object = MibTableColumn
staPortLongOperPathCost = _StaPortLongOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 11),
    _StaPortLongOperPathCost_Type()
)
staPortLongOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortLongOperPathCost.setStatus("current")
_StaPortBpduFlooding_Type = EnabledStatus
_StaPortBpduFlooding_Object = MibTableColumn
staPortBpduFlooding = _StaPortBpduFlooding_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 12),
    _StaPortBpduFlooding_Type()
)
staPortBpduFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortBpduFlooding.setStatus("current")
_StaPortBpduGuard_Type = EnabledStatus
_StaPortBpduGuard_Object = MibTableColumn
staPortBpduGuard = _StaPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 15),
    _StaPortBpduGuard_Type()
)
staPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortBpduGuard.setStatus("current")


class _StaPortAdminEdgePortWithAuto_Type(Integer32):
    """Custom type staPortAdminEdgePortWithAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("false", 2),
          ("true", 1))
    )


_StaPortAdminEdgePortWithAuto_Type.__name__ = "Integer32"
_StaPortAdminEdgePortWithAuto_Object = MibTableColumn
staPortAdminEdgePortWithAuto = _StaPortAdminEdgePortWithAuto_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 16),
    _StaPortAdminEdgePortWithAuto_Type()
)
staPortAdminEdgePortWithAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminEdgePortWithAuto.setStatus("current")
_StaPortBpduFilter_Type = EnabledStatus
_StaPortBpduFilter_Object = MibTableColumn
staPortBpduFilter = _StaPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 17),
    _StaPortBpduFilter_Type()
)
staPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortBpduFilter.setStatus("current")
_StaPortRootGuardStatus_Type = EnabledStatus
_StaPortRootGuardStatus_Object = MibTableColumn
staPortRootGuardStatus = _StaPortRootGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 18),
    _StaPortRootGuardStatus_Type()
)
staPortRootGuardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortRootGuardStatus.setStatus("current")
_StaPortBpduGuardAutoRecovery_Type = EnabledStatus
_StaPortBpduGuardAutoRecovery_Object = MibTableColumn
staPortBpduGuardAutoRecovery = _StaPortBpduGuardAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 19),
    _StaPortBpduGuardAutoRecovery_Type()
)
staPortBpduGuardAutoRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortBpduGuardAutoRecovery.setStatus("current")


class _StaPortBpduGuardAutoRecoveryInterval_Type(Unsigned32):
    """Custom type staPortBpduGuardAutoRecoveryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_StaPortBpduGuardAutoRecoveryInterval_Type.__name__ = "Unsigned32"
_StaPortBpduGuardAutoRecoveryInterval_Object = MibTableColumn
staPortBpduGuardAutoRecoveryInterval = _StaPortBpduGuardAutoRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 20),
    _StaPortBpduGuardAutoRecoveryInterval_Type()
)
staPortBpduGuardAutoRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortBpduGuardAutoRecoveryInterval.setStatus("current")
_StaPortTcPropStop_Type = TruthValue
_StaPortTcPropStop_Object = MibTableColumn
staPortTcPropStop = _StaPortTcPropStop_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 2, 1, 21),
    _StaPortTcPropStop_Type()
)
staPortTcPropStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortTcPropStop.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 4),
    _StaTxHoldCount_Type()
)
staTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staTxHoldCount.setStatus("current")


class _StaPathCostMethod_Type(StaPathCostMode):
    """Custom type staPathCostMethod based on StaPathCostMode"""


_StaPathCostMethod_Object = MibScalar
staPathCostMethod = _StaPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 5),
    _StaPathCostMethod_Type()
)
staPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPathCostMethod.setStatus("current")
_XstMgt_ObjectIdentity = ObjectIdentity
xstMgt = _XstMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6)
)


class _MstName_Type(DisplayString):
    """Custom type mstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MstName_Type.__name__ = "DisplayString"
_MstName_Object = MibScalar
mstName = _MstName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 1),
    _MstName_Type()
)
mstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstName.setStatus("current")
_MstRevision_Type = Integer32
_MstRevision_Object = MibScalar
mstRevision = _MstRevision_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 2),
    _MstRevision_Type()
)
mstRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstRevision.setStatus("current")


class _MstMaxHops_Type(Integer32):
    """Custom type mstMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_MstMaxHops_Type.__name__ = "Integer32"
_MstMaxHops_Object = MibScalar
mstMaxHops = _MstMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 3),
    _MstMaxHops_Type()
)
mstMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMaxHops.setStatus("current")
_XstInstanceCfgTable_Object = MibTable
xstInstanceCfgTable = _XstInstanceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    xstInstanceCfgTable.setStatus("current")
_XstInstanceCfgEntry_Object = MibTableRow
xstInstanceCfgEntry = _XstInstanceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1)
)
xstInstanceCfgEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "xstInstanceCfgIndex"),
)
if mibBuilder.loadTexts:
    xstInstanceCfgEntry.setStatus("current")


class _XstInstanceCfgIndex_Type(Integer32):
    """Custom type xstInstanceCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_XstInstanceCfgIndex_Type.__name__ = "Integer32"
_XstInstanceCfgIndex_Object = MibTableColumn
xstInstanceCfgIndex = _XstInstanceCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 2),
    _XstInstanceCfgPriority_Type()
)
xstInstanceCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstanceCfgPriority.setStatus("current")
_XstInstanceCfgTimeSinceTopologyChange_Type = TimeTicks
_XstInstanceCfgTimeSinceTopologyChange_Object = MibTableColumn
xstInstanceCfgTimeSinceTopologyChange = _XstInstanceCfgTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 3),
    _XstInstanceCfgTimeSinceTopologyChange_Type()
)
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTimeSinceTopologyChange.setStatus("current")
_XstInstanceCfgTopChanges_Type = Integer32
_XstInstanceCfgTopChanges_Object = MibTableColumn
xstInstanceCfgTopChanges = _XstInstanceCfgTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 4),
    _XstInstanceCfgTopChanges_Type()
)
xstInstanceCfgTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTopChanges.setStatus("current")
_XstInstanceCfgDesignatedRoot_Type = BridgeId
_XstInstanceCfgDesignatedRoot_Object = MibTableColumn
xstInstanceCfgDesignatedRoot = _XstInstanceCfgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 5),
    _XstInstanceCfgDesignatedRoot_Type()
)
xstInstanceCfgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgDesignatedRoot.setStatus("current")
_XstInstanceCfgRootCost_Type = Integer32
_XstInstanceCfgRootCost_Object = MibTableColumn
xstInstanceCfgRootCost = _XstInstanceCfgRootCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 6),
    _XstInstanceCfgRootCost_Type()
)
xstInstanceCfgRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootCost.setStatus("current")
_XstInstanceCfgRootPort_Type = Integer32
_XstInstanceCfgRootPort_Object = MibTableColumn
xstInstanceCfgRootPort = _XstInstanceCfgRootPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 7),
    _XstInstanceCfgRootPort_Type()
)
xstInstanceCfgRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootPort.setStatus("current")
_XstInstanceCfgMaxAge_Type = Timeout
_XstInstanceCfgMaxAge_Object = MibTableColumn
xstInstanceCfgMaxAge = _XstInstanceCfgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 8),
    _XstInstanceCfgMaxAge_Type()
)
xstInstanceCfgMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgMaxAge.setStatus("current")
_XstInstanceCfgHelloTime_Type = Timeout
_XstInstanceCfgHelloTime_Object = MibTableColumn
xstInstanceCfgHelloTime = _XstInstanceCfgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 9),
    _XstInstanceCfgHelloTime_Type()
)
xstInstanceCfgHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHelloTime.setStatus("current")
_XstInstanceCfgHoldTime_Type = Timeout
_XstInstanceCfgHoldTime_Object = MibTableColumn
xstInstanceCfgHoldTime = _XstInstanceCfgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 10),
    _XstInstanceCfgHoldTime_Type()
)
xstInstanceCfgHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHoldTime.setStatus("current")
_XstInstanceCfgForwardDelay_Type = Timeout
_XstInstanceCfgForwardDelay_Object = MibTableColumn
xstInstanceCfgForwardDelay = _XstInstanceCfgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 11),
    _XstInstanceCfgForwardDelay_Type()
)
xstInstanceCfgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgForwardDelay.setStatus("current")
_XstInstanceCfgBridgeMaxAge_Type = Timeout
_XstInstanceCfgBridgeMaxAge_Object = MibTableColumn
xstInstanceCfgBridgeMaxAge = _XstInstanceCfgBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 12),
    _XstInstanceCfgBridgeMaxAge_Type()
)
xstInstanceCfgBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeMaxAge.setStatus("current")
_XstInstanceCfgBridgeHelloTime_Type = Timeout
_XstInstanceCfgBridgeHelloTime_Object = MibTableColumn
xstInstanceCfgBridgeHelloTime = _XstInstanceCfgBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 13),
    _XstInstanceCfgBridgeHelloTime_Type()
)
xstInstanceCfgBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeHelloTime.setStatus("current")
_XstInstanceCfgBridgeForwardDelay_Type = Timeout
_XstInstanceCfgBridgeForwardDelay_Object = MibTableColumn
xstInstanceCfgBridgeForwardDelay = _XstInstanceCfgBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 14),
    _XstInstanceCfgBridgeForwardDelay_Type()
)
xstInstanceCfgBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeForwardDelay.setStatus("current")
_XstInstanceCfgTxHoldCount_Type = Integer32
_XstInstanceCfgTxHoldCount_Object = MibTableColumn
xstInstanceCfgTxHoldCount = _XstInstanceCfgTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 15),
    _XstInstanceCfgTxHoldCount_Type()
)
xstInstanceCfgTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTxHoldCount.setStatus("current")
_XstInstanceCfgPathCostMethod_Type = StaPathCostMode
_XstInstanceCfgPathCostMethod_Object = MibTableColumn
xstInstanceCfgPathCostMethod = _XstInstanceCfgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 4, 1, 16),
    _XstInstanceCfgPathCostMethod_Type()
)
xstInstanceCfgPathCostMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgPathCostMethod.setStatus("current")
_XstInstancePortTable_Object = MibTable
xstInstancePortTable = _XstInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    xstInstancePortTable.setStatus("current")
_XstInstancePortEntry_Object = MibTableRow
xstInstancePortEntry = _XstInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1)
)
xstInstancePortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "xstInstanceCfgIndex"),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 4),
    _XstInstancePortState_Type()
)
xstInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortState.setStatus("current")
_XstInstancePortEnable_Type = EnabledStatus
_XstInstancePortEnable_Object = MibTableColumn
xstInstancePortEnable = _XstInstancePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 5),
    _XstInstancePortEnable_Type()
)
xstInstancePortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortEnable.setStatus("current")
_XstInstancePortDesignatedRoot_Type = BridgeId
_XstInstancePortDesignatedRoot_Object = MibTableColumn
xstInstancePortDesignatedRoot = _XstInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 7),
    _XstInstancePortDesignatedRoot_Type()
)
xstInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedRoot.setStatus("current")
_XstInstancePortDesignatedCost_Type = Integer32
_XstInstancePortDesignatedCost_Object = MibTableColumn
xstInstancePortDesignatedCost = _XstInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 8),
    _XstInstancePortDesignatedCost_Type()
)
xstInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedCost.setStatus("current")
_XstInstancePortDesignatedBridge_Type = BridgeId
_XstInstancePortDesignatedBridge_Object = MibTableColumn
xstInstancePortDesignatedBridge = _XstInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 10),
    _XstInstancePortDesignatedPort_Type()
)
xstInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedPort.setStatus("current")
_XstInstancePortForwardTransitions_Type = Counter32
_XstInstancePortForwardTransitions_Object = MibTableColumn
xstInstancePortForwardTransitions = _XstInstancePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 12),
    _XstInstancePortPortRole_Type()
)
xstInstancePortPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortPortRole.setStatus("current")


class _XstInstancePortAdminPathCost_Type(Integer32):
    """Custom type xstInstancePortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_XstInstancePortAdminPathCost_Type.__name__ = "Integer32"
_XstInstancePortAdminPathCost_Object = MibTableColumn
xstInstancePortAdminPathCost = _XstInstancePortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 13),
    _XstInstancePortAdminPathCost_Type()
)
xstInstancePortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortAdminPathCost.setStatus("current")


class _XstInstancePortOperPathCost_Type(Integer32):
    """Custom type xstInstancePortOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_XstInstancePortOperPathCost_Type.__name__ = "Integer32"
_XstInstancePortOperPathCost_Object = MibTableColumn
xstInstancePortOperPathCost = _XstInstancePortOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 5, 1, 14),
    _XstInstancePortOperPathCost_Type()
)
xstInstancePortOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortOperPathCost.setStatus("current")
_MstInstanceEditTable_Object = MibTable
mstInstanceEditTable = _MstInstanceEditTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    mstInstanceEditTable.setStatus("current")
_MstInstanceEditEntry_Object = MibTableRow
mstInstanceEditEntry = _MstInstanceEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 6, 1)
)
mstInstanceEditEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mstInstanceEditIndex"),
)
if mibBuilder.loadTexts:
    mstInstanceEditEntry.setStatus("current")


class _MstInstanceEditIndex_Type(Integer32):
    """Custom type mstInstanceEditIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MstInstanceEditIndex_Type.__name__ = "Integer32"
_MstInstanceEditIndex_Object = MibTableColumn
mstInstanceEditIndex = _MstInstanceEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 6, 1, 1),
    _MstInstanceEditIndex_Type()
)
mstInstanceEditIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstInstanceEditIndex.setStatus("current")


class _MstInstanceEditVlansMap_Type(OctetString):
    """Custom type mstInstanceEditVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap_Object = MibTableColumn
mstInstanceEditVlansMap = _MstInstanceEditVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 6, 1, 2),
    _MstInstanceEditVlansMap_Type()
)
mstInstanceEditVlansMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap.setStatus("current")


class _MstInstanceEditVlansMap2k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap2k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap2k_Object = MibTableColumn
mstInstanceEditVlansMap2k = _MstInstanceEditVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 6, 1, 3),
    _MstInstanceEditVlansMap2k_Type()
)
mstInstanceEditVlansMap2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap2k.setStatus("current")


class _MstInstanceEditVlansMap3k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap3k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap3k_Object = MibTableColumn
mstInstanceEditVlansMap3k = _MstInstanceEditVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 6, 1, 4),
    _MstInstanceEditVlansMap3k_Type()
)
mstInstanceEditVlansMap3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap3k.setStatus("current")


class _MstInstanceEditVlansMap4k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap4k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap4k_Object = MibTableColumn
mstInstanceEditVlansMap4k = _MstInstanceEditVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 6, 1, 5),
    _MstInstanceEditVlansMap4k_Type()
)
mstInstanceEditVlansMap4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap4k.setStatus("current")
_MstInstanceEditRemainingHops_Type = Integer32
_MstInstanceEditRemainingHops_Object = MibTableColumn
mstInstanceEditRemainingHops = _MstInstanceEditRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 6, 1, 6),
    _MstInstanceEditRemainingHops_Type()
)
mstInstanceEditRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceEditRemainingHops.setStatus("current")
_MstInstanceOperTable_Object = MibTable
mstInstanceOperTable = _MstInstanceOperTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    mstInstanceOperTable.setStatus("current")
_MstInstanceOperEntry_Object = MibTableRow
mstInstanceOperEntry = _MstInstanceOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 7, 1)
)
mstInstanceOperEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mstInstanceOperIndex"),
)
if mibBuilder.loadTexts:
    mstInstanceOperEntry.setStatus("current")


class _MstInstanceOperIndex_Type(Integer32):
    """Custom type mstInstanceOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MstInstanceOperIndex_Type.__name__ = "Integer32"
_MstInstanceOperIndex_Object = MibTableColumn
mstInstanceOperIndex = _MstInstanceOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 7, 1, 1),
    _MstInstanceOperIndex_Type()
)
mstInstanceOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstInstanceOperIndex.setStatus("current")


class _MstInstanceOperVlansMap_Type(OctetString):
    """Custom type mstInstanceOperVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap_Object = MibTableColumn
mstInstanceOperVlansMap = _MstInstanceOperVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 7, 1, 2),
    _MstInstanceOperVlansMap_Type()
)
mstInstanceOperVlansMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap.setStatus("current")


class _MstInstanceOperVlansMap2k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap2k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap2k_Object = MibTableColumn
mstInstanceOperVlansMap2k = _MstInstanceOperVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 7, 1, 3),
    _MstInstanceOperVlansMap2k_Type()
)
mstInstanceOperVlansMap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap2k.setStatus("current")


class _MstInstanceOperVlansMap3k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap3k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap3k_Object = MibTableColumn
mstInstanceOperVlansMap3k = _MstInstanceOperVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 7, 1, 4),
    _MstInstanceOperVlansMap3k_Type()
)
mstInstanceOperVlansMap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap3k.setStatus("current")


class _MstInstanceOperVlansMap4k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap4k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap4k_Object = MibTableColumn
mstInstanceOperVlansMap4k = _MstInstanceOperVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 6, 7, 1, 5),
    _MstInstanceOperVlansMap4k_Type()
)
mstInstanceOperVlansMap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap4k.setStatus("current")
_StaLoopbackDetectionPortTable_Object = MibTable
staLoopbackDetectionPortTable = _StaLoopbackDetectionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 8)
)
if mibBuilder.loadTexts:
    staLoopbackDetectionPortTable.setStatus("current")
_StaLoopbackDetectionPortEntry_Object = MibTableRow
staLoopbackDetectionPortEntry = _StaLoopbackDetectionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 8, 1)
)
staLoopbackDetectionPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "staLoopbackDetectionPortIfIndex"),
)
if mibBuilder.loadTexts:
    staLoopbackDetectionPortEntry.setStatus("current")
_StaLoopbackDetectionPortIfIndex_Type = InterfaceIndex
_StaLoopbackDetectionPortIfIndex_Object = MibTableColumn
staLoopbackDetectionPortIfIndex = _StaLoopbackDetectionPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 8, 1, 1),
    _StaLoopbackDetectionPortIfIndex_Type()
)
staLoopbackDetectionPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortIfIndex.setStatus("current")
_StaLoopbackDetectionPortStatus_Type = EnabledStatus
_StaLoopbackDetectionPortStatus_Object = MibTableColumn
staLoopbackDetectionPortStatus = _StaLoopbackDetectionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 8, 1, 2),
    _StaLoopbackDetectionPortStatus_Type()
)
staLoopbackDetectionPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortStatus.setStatus("current")
_StaLoopbackDetectionPortTrapStatus_Type = EnabledStatus
_StaLoopbackDetectionPortTrapStatus_Object = MibTableColumn
staLoopbackDetectionPortTrapStatus = _StaLoopbackDetectionPortTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 8, 1, 3),
    _StaLoopbackDetectionPortTrapStatus_Type()
)
staLoopbackDetectionPortTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortTrapStatus.setStatus("current")


class _StaLoopbackDetectionPortReleaseMode_Type(Integer32):
    """Custom type staLoopbackDetectionPortReleaseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_StaLoopbackDetectionPortReleaseMode_Type.__name__ = "Integer32"
_StaLoopbackDetectionPortReleaseMode_Object = MibTableColumn
staLoopbackDetectionPortReleaseMode = _StaLoopbackDetectionPortReleaseMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 8, 1, 4),
    _StaLoopbackDetectionPortReleaseMode_Type()
)
staLoopbackDetectionPortReleaseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortReleaseMode.setStatus("current")


class _StaLoopbackDetectionPortRelease_Type(Integer32):
    """Custom type staLoopbackDetectionPortRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRelease", 1),
          ("release", 2))
    )


_StaLoopbackDetectionPortRelease_Type.__name__ = "Integer32"
_StaLoopbackDetectionPortRelease_Object = MibTableColumn
staLoopbackDetectionPortRelease = _StaLoopbackDetectionPortRelease_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 8, 1, 5),
    _StaLoopbackDetectionPortRelease_Type()
)
staLoopbackDetectionPortRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortRelease.setStatus("current")


class _StaLoopbackDetectionPortShutdownInterval_Type(Integer32):
    """Custom type staLoopbackDetectionPortShutdownInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_StaLoopbackDetectionPortShutdownInterval_Type.__name__ = "Integer32"
_StaLoopbackDetectionPortShutdownInterval_Object = MibTableColumn
staLoopbackDetectionPortShutdownInterval = _StaLoopbackDetectionPortShutdownInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 8, 1, 7),
    _StaLoopbackDetectionPortShutdownInterval_Type()
)
staLoopbackDetectionPortShutdownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortShutdownInterval.setStatus("current")


class _StaSystemBPDUFlooding_Type(Integer32):
    """Custom type staSystemBPDUFlooding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("to-all", 2),
          ("to-vlan", 1))
    )


_StaSystemBPDUFlooding_Type.__name__ = "Integer32"
_StaSystemBPDUFlooding_Object = MibScalar
staSystemBPDUFlooding = _StaSystemBPDUFlooding_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 9),
    _StaSystemBPDUFlooding_Type()
)
staSystemBPDUFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemBPDUFlooding.setStatus("current")
_StaCiscoPrestandardCompatibility_Type = EnabledStatus
_StaCiscoPrestandardCompatibility_Object = MibScalar
staCiscoPrestandardCompatibility = _StaCiscoPrestandardCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 5, 11),
    _StaCiscoPrestandardCompatibility_Type()
)
staCiscoPrestandardCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staCiscoPrestandardCompatibility.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 7)
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 7, 3),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_MirrorMgt_ObjectIdentity = ObjectIdentity
mirrorMgt = _MirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mirrorDestinationPort"),
    (0, "ECS2100-28PP-MIB", "mirrorSourcePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorDestinationPort_Type = InterfaceIndex
_MirrorDestinationPort_Object = MibTableColumn
mirrorDestinationPort = _MirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 1, 1, 1),
    _MirrorDestinationPort_Type()
)
mirrorDestinationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorDestinationPort.setStatus("current")
_MirrorSourcePort_Type = InterfaceIndex
_MirrorSourcePort_Object = MibTableColumn
mirrorSourcePort = _MirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 1, 1, 3),
    _MirrorType_Type()
)
mirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorType.setStatus("current")
_MirrorStatus_Type = ValidStatus
_MirrorStatus_Object = MibTableColumn
mirrorStatus = _MirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 1, 1, 4),
    _MirrorStatus_Type()
)
mirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorStatus.setStatus("current")
_RspanTable_Object = MibTable
rspanTable = _RspanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3)
)
if mibBuilder.loadTexts:
    rspanTable.setStatus("current")
_RspanEntry_Object = MibTableRow
rspanEntry = _RspanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1)
)
rspanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "rspanSessionId"),
)
if mibBuilder.loadTexts:
    rspanEntry.setStatus("current")


class _RspanSessionId_Type(Integer32):
    """Custom type rspanSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RspanSessionId_Type.__name__ = "Integer32"
_RspanSessionId_Object = MibTableColumn
rspanSessionId = _RspanSessionId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 1),
    _RspanSessionId_Type()
)
rspanSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rspanSessionId.setStatus("current")
_RspanSrcTxPorts_Type = PortList
_RspanSrcTxPorts_Object = MibTableColumn
rspanSrcTxPorts = _RspanSrcTxPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 2),
    _RspanSrcTxPorts_Type()
)
rspanSrcTxPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rspanSrcTxPorts.setStatus("current")
_RspanSrcRxPorts_Type = PortList
_RspanSrcRxPorts_Object = MibTableColumn
rspanSrcRxPorts = _RspanSrcRxPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 3),
    _RspanSrcRxPorts_Type()
)
rspanSrcRxPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rspanSrcRxPorts.setStatus("current")
_RspanDstPort_Type = Integer32
_RspanDstPort_Object = MibTableColumn
rspanDstPort = _RspanDstPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 4),
    _RspanDstPort_Type()
)
rspanDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rspanDstPort.setStatus("current")


class _RspanDstPortTag_Type(Integer32):
    """Custom type rspanDstPortTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tagged", 3),
          ("untagged", 2))
    )


_RspanDstPortTag_Type.__name__ = "Integer32"
_RspanDstPortTag_Object = MibTableColumn
rspanDstPortTag = _RspanDstPortTag_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 5),
    _RspanDstPortTag_Type()
)
rspanDstPortTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rspanDstPortTag.setStatus("current")


class _RspanSwitchRole_Type(Integer32):
    """Custom type rspanSwitchRole based on Integer32"""
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
        *(("destination", 4),
          ("intermediate", 3),
          ("none", 1),
          ("source", 2))
    )


_RspanSwitchRole_Type.__name__ = "Integer32"
_RspanSwitchRole_Object = MibTableColumn
rspanSwitchRole = _RspanSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 6),
    _RspanSwitchRole_Type()
)
rspanSwitchRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rspanSwitchRole.setStatus("current")
_RspanRemotePorts_Type = PortList
_RspanRemotePorts_Object = MibTableColumn
rspanRemotePorts = _RspanRemotePorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 7),
    _RspanRemotePorts_Type()
)
rspanRemotePorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rspanRemotePorts.setStatus("current")


class _RspanRemoteVlanId_Type(Integer32):
    """Custom type rspanRemoteVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RspanRemoteVlanId_Type.__name__ = "Integer32"
_RspanRemoteVlanId_Object = MibTableColumn
rspanRemoteVlanId = _RspanRemoteVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 8),
    _RspanRemoteVlanId_Type()
)
rspanRemoteVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rspanRemoteVlanId.setStatus("current")


class _RspanOperStatus_Type(Integer32):
    """Custom type rspanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_RspanOperStatus_Type.__name__ = "Integer32"
_RspanOperStatus_Object = MibTableColumn
rspanOperStatus = _RspanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 9),
    _RspanOperStatus_Type()
)
rspanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rspanOperStatus.setStatus("current")
_RspanStatus_Type = ValidStatus
_RspanStatus_Object = MibTableColumn
rspanStatus = _RspanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 8, 3, 1, 10),
    _RspanStatus_Type()
)
rspanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rspanStatus.setStatus("current")
_IgmpSnoopMgt_ObjectIdentity = ObjectIdentity
igmpSnoopMgt = _IgmpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9)
)


class _IgmpSnoopStatus_Type(EnabledStatus):
    """Custom type igmpSnoopStatus based on EnabledStatus"""


_IgmpSnoopStatus_Object = MibScalar
igmpSnoopStatus = _IgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 1),
    _IgmpSnoopStatus_Type()
)
igmpSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopStatus.setStatus("current")


class _IgmpSnoopQuerier_Type(EnabledStatus):
    """Custom type igmpSnoopQuerier based on EnabledStatus"""


_IgmpSnoopQuerier_Object = MibScalar
igmpSnoopQuerier = _IgmpSnoopQuerier_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 2),
    _IgmpSnoopQuerier_Type()
)
igmpSnoopQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQuerier.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 6),
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
        ValueRangeConstraint(1, 3),
    )


_IgmpSnoopVersion_Type.__name__ = "Integer32"
_IgmpSnoopVersion_Object = MibScalar
igmpSnoopVersion = _IgmpSnoopVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 7),
    _IgmpSnoopVersion_Type()
)
igmpSnoopVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVersion.setStatus("current")
_IgmpSnoopRouterCurrentTable_Object = MibTable
igmpSnoopRouterCurrentTable = _IgmpSnoopRouterCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 8)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentTable.setStatus("current")
_IgmpSnoopRouterCurrentEntry_Object = MibTableRow
igmpSnoopRouterCurrentEntry = _IgmpSnoopRouterCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 8, 1)
)
igmpSnoopRouterCurrentEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopRouterCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentEntry.setStatus("current")
_IgmpSnoopRouterCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object = MibTableColumn
igmpSnoopRouterCurrentVlanIndex = _IgmpSnoopRouterCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 8, 1, 1),
    _IgmpSnoopRouterCurrentVlanIndex_Type()
)
igmpSnoopRouterCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentVlanIndex.setStatus("current")
_IgmpSnoopRouterCurrentPorts_Type = PortList
_IgmpSnoopRouterCurrentPorts_Object = MibTableColumn
igmpSnoopRouterCurrentPorts = _IgmpSnoopRouterCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 8, 1, 2),
    _IgmpSnoopRouterCurrentPorts_Type()
)
igmpSnoopRouterCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentPorts.setStatus("current")
_IgmpSnoopRouterCurrentStatus_Type = PortList
_IgmpSnoopRouterCurrentStatus_Object = MibTableColumn
igmpSnoopRouterCurrentStatus = _IgmpSnoopRouterCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 8, 1, 3),
    _IgmpSnoopRouterCurrentStatus_Type()
)
igmpSnoopRouterCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentStatus.setStatus("current")
_IgmpSnoopRouterStaticTable_Object = MibTable
igmpSnoopRouterStaticTable = _IgmpSnoopRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticTable.setStatus("current")
_IgmpSnoopRouterStaticEntry_Object = MibTableRow
igmpSnoopRouterStaticEntry = _IgmpSnoopRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 9, 1)
)
igmpSnoopRouterStaticEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopRouterStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticEntry.setStatus("current")
_IgmpSnoopRouterStaticVlanIndex_Type = Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object = MibTableColumn
igmpSnoopRouterStaticVlanIndex = _IgmpSnoopRouterStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 9, 1, 1),
    _IgmpSnoopRouterStaticVlanIndex_Type()
)
igmpSnoopRouterStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticVlanIndex.setStatus("current")
_IgmpSnoopRouterStaticPorts_Type = PortList
_IgmpSnoopRouterStaticPorts_Object = MibTableColumn
igmpSnoopRouterStaticPorts = _IgmpSnoopRouterStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 9, 1, 2),
    _IgmpSnoopRouterStaticPorts_Type()
)
igmpSnoopRouterStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticPorts.setStatus("current")
_IgmpSnoopRouterStaticStatus_Type = ValidStatus
_IgmpSnoopRouterStaticStatus_Object = MibTableColumn
igmpSnoopRouterStaticStatus = _IgmpSnoopRouterStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 9, 1, 3),
    _IgmpSnoopRouterStaticStatus_Type()
)
igmpSnoopRouterStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticStatus.setStatus("current")
_IgmpSnoopMulticastStaticTable_Object = MibTable
igmpSnoopMulticastStaticTable = _IgmpSnoopMulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 11)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticTable.setStatus("current")
_IgmpSnoopMulticastStaticEntry_Object = MibTableRow
igmpSnoopMulticastStaticEntry = _IgmpSnoopMulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 11, 1)
)
igmpSnoopMulticastStaticEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopMulticastStaticVlanIndex"),
    (0, "ECS2100-28PP-MIB", "igmpSnoopMulticastStaticIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticEntry.setStatus("current")
_IgmpSnoopMulticastStaticVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object = MibTableColumn
igmpSnoopMulticastStaticVlanIndex = _IgmpSnoopMulticastStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 11, 1, 1),
    _IgmpSnoopMulticastStaticVlanIndex_Type()
)
igmpSnoopMulticastStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticVlanIndex.setStatus("current")
_IgmpSnoopMulticastStaticIpAddress_Type = IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object = MibTableColumn
igmpSnoopMulticastStaticIpAddress = _IgmpSnoopMulticastStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 11, 1, 2),
    _IgmpSnoopMulticastStaticIpAddress_Type()
)
igmpSnoopMulticastStaticIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticIpAddress.setStatus("current")
_IgmpSnoopMulticastStaticPorts_Type = PortList
_IgmpSnoopMulticastStaticPorts_Object = MibTableColumn
igmpSnoopMulticastStaticPorts = _IgmpSnoopMulticastStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 11, 1, 3),
    _IgmpSnoopMulticastStaticPorts_Type()
)
igmpSnoopMulticastStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticPorts.setStatus("current")
_IgmpSnoopMulticastStaticStatus_Type = ValidStatus
_IgmpSnoopMulticastStaticStatus_Object = MibTableColumn
igmpSnoopMulticastStaticStatus = _IgmpSnoopMulticastStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 11, 1, 4),
    _IgmpSnoopMulticastStaticStatus_Type()
)
igmpSnoopMulticastStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticStatus.setStatus("current")
_IgmpSnoopCurrentVlanTable_Object = MibTable
igmpSnoopCurrentVlanTable = _IgmpSnoopCurrentVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14)
)
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanTable.setStatus("current")
_IgmpSnoopCurrentVlanEntry_Object = MibTableRow
igmpSnoopCurrentVlanEntry = _IgmpSnoopCurrentVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1)
)
igmpSnoopCurrentVlanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanEntry.setStatus("current")
_IgmpSnoopCurrentVlanIndex_Type = VlanIndex
_IgmpSnoopCurrentVlanIndex_Object = MibTableColumn
igmpSnoopCurrentVlanIndex = _IgmpSnoopCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 1),
    _IgmpSnoopCurrentVlanIndex_Type()
)
igmpSnoopCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanIndex.setStatus("current")
_IgmpSnoopCurrentVlanStatus_Type = EnabledStatus
_IgmpSnoopCurrentVlanStatus_Object = MibTableColumn
igmpSnoopCurrentVlanStatus = _IgmpSnoopCurrentVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 2),
    _IgmpSnoopCurrentVlanStatus_Type()
)
igmpSnoopCurrentVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanStatus.setStatus("current")
_IgmpSnoopCurrentVlanImmediateLeave_Type = EnabledStatus
_IgmpSnoopCurrentVlanImmediateLeave_Object = MibTableColumn
igmpSnoopCurrentVlanImmediateLeave = _IgmpSnoopCurrentVlanImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 3),
    _IgmpSnoopCurrentVlanImmediateLeave_Type()
)
igmpSnoopCurrentVlanImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanImmediateLeave.setStatus("current")
_IgmpSnoopCurrentVlanGeneralQuerySuppression_Type = EnabledStatus
_IgmpSnoopCurrentVlanGeneralQuerySuppression_Object = MibTableColumn
igmpSnoopCurrentVlanGeneralQuerySuppression = _IgmpSnoopCurrentVlanGeneralQuerySuppression_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 4),
    _IgmpSnoopCurrentVlanGeneralQuerySuppression_Type()
)
igmpSnoopCurrentVlanGeneralQuerySuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanGeneralQuerySuppression.setStatus("current")


class _IgmpSnoopCurrentVlanLastMemQueryCount_Type(Unsigned32):
    """Custom type igmpSnoopCurrentVlanLastMemQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IgmpSnoopCurrentVlanLastMemQueryCount_Type.__name__ = "Unsigned32"
_IgmpSnoopCurrentVlanLastMemQueryCount_Object = MibTableColumn
igmpSnoopCurrentVlanLastMemQueryCount = _IgmpSnoopCurrentVlanLastMemQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 5),
    _IgmpSnoopCurrentVlanLastMemQueryCount_Type()
)
igmpSnoopCurrentVlanLastMemQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanLastMemQueryCount.setStatus("current")


class _IgmpSnoopCurrentVlanLastMemQueryIntvl_Type(Unsigned32):
    """Custom type igmpSnoopCurrentVlanLastMemQueryIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31744),
    )


_IgmpSnoopCurrentVlanLastMemQueryIntvl_Type.__name__ = "Unsigned32"
_IgmpSnoopCurrentVlanLastMemQueryIntvl_Object = MibTableColumn
igmpSnoopCurrentVlanLastMemQueryIntvl = _IgmpSnoopCurrentVlanLastMemQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 6),
    _IgmpSnoopCurrentVlanLastMemQueryIntvl_Type()
)
igmpSnoopCurrentVlanLastMemQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanLastMemQueryIntvl.setStatus("current")
_IgmpSnoopCurrentVlanProxyAddress_Type = IpAddress
_IgmpSnoopCurrentVlanProxyAddress_Object = MibTableColumn
igmpSnoopCurrentVlanProxyAddress = _IgmpSnoopCurrentVlanProxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 7),
    _IgmpSnoopCurrentVlanProxyAddress_Type()
)
igmpSnoopCurrentVlanProxyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanProxyAddress.setStatus("current")


class _IgmpSnoopCurrentVlanQueryIntvl_Type(Unsigned32):
    """Custom type igmpSnoopCurrentVlanQueryIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 31744),
    )


_IgmpSnoopCurrentVlanQueryIntvl_Type.__name__ = "Unsigned32"
_IgmpSnoopCurrentVlanQueryIntvl_Object = MibTableColumn
igmpSnoopCurrentVlanQueryIntvl = _IgmpSnoopCurrentVlanQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 8),
    _IgmpSnoopCurrentVlanQueryIntvl_Type()
)
igmpSnoopCurrentVlanQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanQueryIntvl.setStatus("current")


class _IgmpSnoopCurrentVlanQueryRespIntvl_Type(Unsigned32):
    """Custom type igmpSnoopCurrentVlanQueryRespIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 31740),
    )


_IgmpSnoopCurrentVlanQueryRespIntvl_Type.__name__ = "Unsigned32"
_IgmpSnoopCurrentVlanQueryRespIntvl_Object = MibTableColumn
igmpSnoopCurrentVlanQueryRespIntvl = _IgmpSnoopCurrentVlanQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 9),
    _IgmpSnoopCurrentVlanQueryRespIntvl_Type()
)
igmpSnoopCurrentVlanQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanQueryRespIntvl.setStatus("current")


class _IgmpSnoopCurrentVlanProxyReporting_Type(Integer32):
    """Custom type igmpSnoopCurrentVlanProxyReporting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_IgmpSnoopCurrentVlanProxyReporting_Type.__name__ = "Integer32"
_IgmpSnoopCurrentVlanProxyReporting_Object = MibTableColumn
igmpSnoopCurrentVlanProxyReporting = _IgmpSnoopCurrentVlanProxyReporting_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 10),
    _IgmpSnoopCurrentVlanProxyReporting_Type()
)
igmpSnoopCurrentVlanProxyReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanProxyReporting.setStatus("current")


class _IgmpSnoopCurrentVlanVersion_Type(Unsigned32):
    """Custom type igmpSnoopCurrentVlanVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IgmpSnoopCurrentVlanVersion_Type.__name__ = "Unsigned32"
_IgmpSnoopCurrentVlanVersion_Object = MibTableColumn
igmpSnoopCurrentVlanVersion = _IgmpSnoopCurrentVlanVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 11),
    _IgmpSnoopCurrentVlanVersion_Type()
)
igmpSnoopCurrentVlanVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanVersion.setStatus("current")
_IgmpSnoopCurrentVlanVersionExclusive_Type = EnabledStatus
_IgmpSnoopCurrentVlanVersionExclusive_Object = MibTableColumn
igmpSnoopCurrentVlanVersionExclusive = _IgmpSnoopCurrentVlanVersionExclusive_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 12),
    _IgmpSnoopCurrentVlanVersionExclusive_Type()
)
igmpSnoopCurrentVlanVersionExclusive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanVersionExclusive.setStatus("current")
_IgmpSnoopCurrentVlanImmediateLeaveByHostIp_Type = EnabledStatus
_IgmpSnoopCurrentVlanImmediateLeaveByHostIp_Object = MibTableColumn
igmpSnoopCurrentVlanImmediateLeaveByHostIp = _IgmpSnoopCurrentVlanImmediateLeaveByHostIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 14, 1, 14),
    _IgmpSnoopCurrentVlanImmediateLeaveByHostIp_Type()
)
igmpSnoopCurrentVlanImmediateLeaveByHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanImmediateLeaveByHostIp.setStatus("current")
_IgmpSnoopMulticastGroupTable_Object = MibTable
igmpSnoopMulticastGroupTable = _IgmpSnoopMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 15)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastGroupTable.setStatus("current")
_IgmpSnoopMulticastGroupEntry_Object = MibTableRow
igmpSnoopMulticastGroupEntry = _IgmpSnoopMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 15, 1)
)
igmpSnoopMulticastGroupEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopMulticastGroupVlanIndex"),
    (0, "ECS2100-28PP-MIB", "igmpSnoopMulticastGroupIpAddress"),
    (0, "ECS2100-28PP-MIB", "igmpSnoopMulticastGroupSourceIPAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastGroupEntry.setStatus("current")
_IgmpSnoopMulticastGroupVlanIndex_Type = VlanIndex
_IgmpSnoopMulticastGroupVlanIndex_Object = MibTableColumn
igmpSnoopMulticastGroupVlanIndex = _IgmpSnoopMulticastGroupVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 15, 1, 1),
    _IgmpSnoopMulticastGroupVlanIndex_Type()
)
igmpSnoopMulticastGroupVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastGroupVlanIndex.setStatus("current")
_IgmpSnoopMulticastGroupIpAddress_Type = IpAddress
_IgmpSnoopMulticastGroupIpAddress_Object = MibTableColumn
igmpSnoopMulticastGroupIpAddress = _IgmpSnoopMulticastGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 15, 1, 2),
    _IgmpSnoopMulticastGroupIpAddress_Type()
)
igmpSnoopMulticastGroupIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastGroupIpAddress.setStatus("current")
_IgmpSnoopMulticastGroupSourceIPAddress_Type = IpAddress
_IgmpSnoopMulticastGroupSourceIPAddress_Object = MibTableColumn
igmpSnoopMulticastGroupSourceIPAddress = _IgmpSnoopMulticastGroupSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 15, 1, 3),
    _IgmpSnoopMulticastGroupSourceIPAddress_Type()
)
igmpSnoopMulticastGroupSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastGroupSourceIPAddress.setStatus("current")
_IgmpSnoopMulticastGroupPorts_Type = PortList
_IgmpSnoopMulticastGroupPorts_Object = MibTableColumn
igmpSnoopMulticastGroupPorts = _IgmpSnoopMulticastGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 15, 1, 4),
    _IgmpSnoopMulticastGroupPorts_Type()
)
igmpSnoopMulticastGroupPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastGroupPorts.setStatus("current")
_IgmpSnoopMulticastGroupStatus_Type = PortList
_IgmpSnoopMulticastGroupStatus_Object = MibTableColumn
igmpSnoopMulticastGroupStatus = _IgmpSnoopMulticastGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 15, 1, 5),
    _IgmpSnoopMulticastGroupStatus_Type()
)
igmpSnoopMulticastGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastGroupStatus.setStatus("current")
_IgmpSnoopMulticastGroupPortCount_Type = Unsigned32
_IgmpSnoopMulticastGroupPortCount_Object = MibTableColumn
igmpSnoopMulticastGroupPortCount = _IgmpSnoopMulticastGroupPortCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 15, 1, 6),
    _IgmpSnoopMulticastGroupPortCount_Type()
)
igmpSnoopMulticastGroupPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastGroupPortCount.setStatus("current")
_IgmpSnoopFilterStatus_Type = EnabledStatus
_IgmpSnoopFilterStatus_Object = MibScalar
igmpSnoopFilterStatus = _IgmpSnoopFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 17),
    _IgmpSnoopFilterStatus_Type()
)
igmpSnoopFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopFilterStatus.setStatus("current")
_IgmpSnoopProfileTable_Object = MibTable
igmpSnoopProfileTable = _IgmpSnoopProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 18)
)
if mibBuilder.loadTexts:
    igmpSnoopProfileTable.setStatus("current")
_IgmpSnoopProfileEntry_Object = MibTableRow
igmpSnoopProfileEntry = _IgmpSnoopProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 18, 1)
)
igmpSnoopProfileEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopProfileId"),
)
if mibBuilder.loadTexts:
    igmpSnoopProfileEntry.setStatus("current")
_IgmpSnoopProfileId_Type = Unsigned32
_IgmpSnoopProfileId_Object = MibTableColumn
igmpSnoopProfileId = _IgmpSnoopProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 18, 1, 1),
    _IgmpSnoopProfileId_Type()
)
igmpSnoopProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileId.setStatus("current")


class _IgmpSnoopProfileAction_Type(Integer32):
    """Custom type igmpSnoopProfileAction based on Integer32"""
    defaultValue = 2

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


_IgmpSnoopProfileAction_Type.__name__ = "Integer32"
_IgmpSnoopProfileAction_Object = MibTableColumn
igmpSnoopProfileAction = _IgmpSnoopProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 18, 1, 2),
    _IgmpSnoopProfileAction_Type()
)
igmpSnoopProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileAction.setStatus("current")
_IgmpSnoopProfileStatus_Type = ValidStatus
_IgmpSnoopProfileStatus_Object = MibTableColumn
igmpSnoopProfileStatus = _IgmpSnoopProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 18, 1, 3),
    _IgmpSnoopProfileStatus_Type()
)
igmpSnoopProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileStatus.setStatus("current")
_IgmpSnoopProfileCtl_ObjectIdentity = ObjectIdentity
igmpSnoopProfileCtl = _IgmpSnoopProfileCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 19)
)
_IgmpSnoopProfileCtlId_Type = Unsigned32
_IgmpSnoopProfileCtlId_Object = MibScalar
igmpSnoopProfileCtlId = _IgmpSnoopProfileCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 19, 1),
    _IgmpSnoopProfileCtlId_Type()
)
igmpSnoopProfileCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlId.setStatus("current")
_IgmpSnoopProfileCtlInetAddressType_Type = InetAddressType
_IgmpSnoopProfileCtlInetAddressType_Object = MibScalar
igmpSnoopProfileCtlInetAddressType = _IgmpSnoopProfileCtlInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 19, 2),
    _IgmpSnoopProfileCtlInetAddressType_Type()
)
igmpSnoopProfileCtlInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlInetAddressType.setStatus("current")
_IgmpSnoopProfileCtlStartInetAddress_Type = InetAddress
_IgmpSnoopProfileCtlStartInetAddress_Object = MibScalar
igmpSnoopProfileCtlStartInetAddress = _IgmpSnoopProfileCtlStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 19, 3),
    _IgmpSnoopProfileCtlStartInetAddress_Type()
)
igmpSnoopProfileCtlStartInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlStartInetAddress.setStatus("current")
_IgmpSnoopProfileCtlEndInetAddress_Type = InetAddress
_IgmpSnoopProfileCtlEndInetAddress_Object = MibScalar
igmpSnoopProfileCtlEndInetAddress = _IgmpSnoopProfileCtlEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 19, 4),
    _IgmpSnoopProfileCtlEndInetAddress_Type()
)
igmpSnoopProfileCtlEndInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlEndInetAddress.setStatus("current")


class _IgmpSnoopProfileCtlAction_Type(Integer32):
    """Custom type igmpSnoopProfileCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("destroy", 3),
          ("noAction", 1))
    )


_IgmpSnoopProfileCtlAction_Type.__name__ = "Integer32"
_IgmpSnoopProfileCtlAction_Object = MibScalar
igmpSnoopProfileCtlAction = _IgmpSnoopProfileCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 19, 5),
    _IgmpSnoopProfileCtlAction_Type()
)
igmpSnoopProfileCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlAction.setStatus("current")
_IgmpSnoopProfileRangeTable_Object = MibTable
igmpSnoopProfileRangeTable = _IgmpSnoopProfileRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 20)
)
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeTable.setStatus("current")
_IgmpSnoopProfileRangeEntry_Object = MibTableRow
igmpSnoopProfileRangeEntry = _IgmpSnoopProfileRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 20, 1)
)
igmpSnoopProfileRangeEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopProfileRangeProfileId"),
    (0, "ECS2100-28PP-MIB", "igmpSnoopProfileRangeInetAddressType"),
    (0, "ECS2100-28PP-MIB", "igmpSnoopProfileRangeStartInetAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeEntry.setStatus("current")


class _IgmpSnoopProfileRangeProfileId_Type(Unsigned32):
    """Custom type igmpSnoopProfileRangeProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IgmpSnoopProfileRangeProfileId_Type.__name__ = "Unsigned32"
_IgmpSnoopProfileRangeProfileId_Object = MibTableColumn
igmpSnoopProfileRangeProfileId = _IgmpSnoopProfileRangeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 20, 1, 1),
    _IgmpSnoopProfileRangeProfileId_Type()
)
igmpSnoopProfileRangeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeProfileId.setStatus("current")
_IgmpSnoopProfileRangeInetAddressType_Type = InetAddressType
_IgmpSnoopProfileRangeInetAddressType_Object = MibTableColumn
igmpSnoopProfileRangeInetAddressType = _IgmpSnoopProfileRangeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 20, 1, 2),
    _IgmpSnoopProfileRangeInetAddressType_Type()
)
igmpSnoopProfileRangeInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeInetAddressType.setStatus("current")
_IgmpSnoopProfileRangeStartInetAddress_Type = InetAddress
_IgmpSnoopProfileRangeStartInetAddress_Object = MibTableColumn
igmpSnoopProfileRangeStartInetAddress = _IgmpSnoopProfileRangeStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 20, 1, 3),
    _IgmpSnoopProfileRangeStartInetAddress_Type()
)
igmpSnoopProfileRangeStartInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeStartInetAddress.setStatus("current")
_IgmpSnoopProfileRangeEndInetAddress_Type = InetAddress
_IgmpSnoopProfileRangeEndInetAddress_Object = MibTableColumn
igmpSnoopProfileRangeEndInetAddress = _IgmpSnoopProfileRangeEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 20, 1, 4),
    _IgmpSnoopProfileRangeEndInetAddress_Type()
)
igmpSnoopProfileRangeEndInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeEndInetAddress.setStatus("current")


class _IgmpSnoopProfileRangeAction_Type(Integer32):
    """Custom type igmpSnoopProfileRangeAction based on Integer32"""
    defaultValue = 2

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


_IgmpSnoopProfileRangeAction_Type.__name__ = "Integer32"
_IgmpSnoopProfileRangeAction_Object = MibTableColumn
igmpSnoopProfileRangeAction = _IgmpSnoopProfileRangeAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 20, 1, 5),
    _IgmpSnoopProfileRangeAction_Type()
)
igmpSnoopProfileRangeAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeAction.setStatus("current")
_IgmpSnoopFilterPortTable_Object = MibTable
igmpSnoopFilterPortTable = _IgmpSnoopFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 21)
)
if mibBuilder.loadTexts:
    igmpSnoopFilterPortTable.setStatus("current")
_IgmpSnoopFilterPortEntry_Object = MibTableRow
igmpSnoopFilterPortEntry = _IgmpSnoopFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 21, 1)
)
igmpSnoopFilterPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopFilterPortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopFilterPortEntry.setStatus("current")
_IgmpSnoopFilterPortIndex_Type = Unsigned32
_IgmpSnoopFilterPortIndex_Object = MibTableColumn
igmpSnoopFilterPortIndex = _IgmpSnoopFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 21, 1, 1),
    _IgmpSnoopFilterPortIndex_Type()
)
igmpSnoopFilterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopFilterPortIndex.setStatus("current")
_IgmpSnoopFilterPortProfileId_Type = Integer32
_IgmpSnoopFilterPortProfileId_Object = MibTableColumn
igmpSnoopFilterPortProfileId = _IgmpSnoopFilterPortProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 21, 1, 2),
    _IgmpSnoopFilterPortProfileId_Type()
)
igmpSnoopFilterPortProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopFilterPortProfileId.setStatus("current")
_IgmpSnoopThrottlePortTable_Object = MibTable
igmpSnoopThrottlePortTable = _IgmpSnoopThrottlePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 22)
)
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortTable.setStatus("current")
_IgmpSnoopThrottlePortEntry_Object = MibTableRow
igmpSnoopThrottlePortEntry = _IgmpSnoopThrottlePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 22, 1)
)
igmpSnoopThrottlePortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopThrottlePortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortEntry.setStatus("current")
_IgmpSnoopThrottlePortIndex_Type = Unsigned32
_IgmpSnoopThrottlePortIndex_Object = MibTableColumn
igmpSnoopThrottlePortIndex = _IgmpSnoopThrottlePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 22, 1, 1),
    _IgmpSnoopThrottlePortIndex_Type()
)
igmpSnoopThrottlePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortIndex.setStatus("current")
_IgmpSnoopThrottlePortRunningStatus_Type = TruthValue
_IgmpSnoopThrottlePortRunningStatus_Object = MibTableColumn
igmpSnoopThrottlePortRunningStatus = _IgmpSnoopThrottlePortRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 22, 1, 2),
    _IgmpSnoopThrottlePortRunningStatus_Type()
)
igmpSnoopThrottlePortRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortRunningStatus.setStatus("current")


class _IgmpSnoopThrottlePortAction_Type(Integer32):
    """Custom type igmpSnoopThrottlePortAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("replace", 1))
    )


_IgmpSnoopThrottlePortAction_Type.__name__ = "Integer32"
_IgmpSnoopThrottlePortAction_Object = MibTableColumn
igmpSnoopThrottlePortAction = _IgmpSnoopThrottlePortAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 22, 1, 3),
    _IgmpSnoopThrottlePortAction_Type()
)
igmpSnoopThrottlePortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortAction.setStatus("current")


class _IgmpSnoopThrottlePortMaxGroups_Type(Integer32):
    """Custom type igmpSnoopThrottlePortMaxGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IgmpSnoopThrottlePortMaxGroups_Type.__name__ = "Integer32"
_IgmpSnoopThrottlePortMaxGroups_Object = MibTableColumn
igmpSnoopThrottlePortMaxGroups = _IgmpSnoopThrottlePortMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 22, 1, 4),
    _IgmpSnoopThrottlePortMaxGroups_Type()
)
igmpSnoopThrottlePortMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortMaxGroups.setStatus("current")
_IgmpSnoopThrottlePortCurrentGroups_Type = Integer32
_IgmpSnoopThrottlePortCurrentGroups_Object = MibTableColumn
igmpSnoopThrottlePortCurrentGroups = _IgmpSnoopThrottlePortCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 22, 1, 5),
    _IgmpSnoopThrottlePortCurrentGroups_Type()
)
igmpSnoopThrottlePortCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortCurrentGroups.setStatus("current")
_IgmpSnoopPortTable_Object = MibTable
igmpSnoopPortTable = _IgmpSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27)
)
if mibBuilder.loadTexts:
    igmpSnoopPortTable.setStatus("current")
_IgmpSnoopPortEntry_Object = MibTableRow
igmpSnoopPortEntry = _IgmpSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1)
)
igmpSnoopPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopPortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopPortEntry.setStatus("current")
_IgmpSnoopPortIndex_Type = Unsigned32
_IgmpSnoopPortIndex_Object = MibTableColumn
igmpSnoopPortIndex = _IgmpSnoopPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 1),
    _IgmpSnoopPortIndex_Type()
)
igmpSnoopPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopPortIndex.setStatus("current")


class _IgmpSnoopQueryDrop_Type(Integer32):
    """Custom type igmpSnoopQueryDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IgmpSnoopQueryDrop_Type.__name__ = "Integer32"
_IgmpSnoopQueryDrop_Object = MibTableColumn
igmpSnoopQueryDrop = _IgmpSnoopQueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 3),
    _IgmpSnoopQueryDrop_Type()
)
igmpSnoopQueryDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryDrop.setStatus("current")


class _IgmpSnoopMulticastDataDrop_Type(Integer32):
    """Custom type igmpSnoopMulticastDataDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IgmpSnoopMulticastDataDrop_Type.__name__ = "Integer32"
_IgmpSnoopMulticastDataDrop_Object = MibTableColumn
igmpSnoopMulticastDataDrop = _IgmpSnoopMulticastDataDrop_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 4),
    _IgmpSnoopMulticastDataDrop_Type()
)
igmpSnoopMulticastDataDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopMulticastDataDrop.setStatus("current")
_IgmpSnoopPortNumGroups_Type = Unsigned32
_IgmpSnoopPortNumGroups_Object = MibTableColumn
igmpSnoopPortNumGroups = _IgmpSnoopPortNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 5),
    _IgmpSnoopPortNumGroups_Type()
)
igmpSnoopPortNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumGroups.setStatus("current")
_IgmpSnoopPortNumJoinSend_Type = Unsigned32
_IgmpSnoopPortNumJoinSend_Object = MibTableColumn
igmpSnoopPortNumJoinSend = _IgmpSnoopPortNumJoinSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 6),
    _IgmpSnoopPortNumJoinSend_Type()
)
igmpSnoopPortNumJoinSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumJoinSend.setStatus("current")
_IgmpSnoopPortNumJoins_Type = Unsigned32
_IgmpSnoopPortNumJoins_Object = MibTableColumn
igmpSnoopPortNumJoins = _IgmpSnoopPortNumJoins_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 7),
    _IgmpSnoopPortNumJoins_Type()
)
igmpSnoopPortNumJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumJoins.setStatus("current")
_IgmpSnoopPortNumJoinSuccess_Type = Unsigned32
_IgmpSnoopPortNumJoinSuccess_Object = MibTableColumn
igmpSnoopPortNumJoinSuccess = _IgmpSnoopPortNumJoinSuccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 8),
    _IgmpSnoopPortNumJoinSuccess_Type()
)
igmpSnoopPortNumJoinSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumJoinSuccess.setStatus("current")
_IgmpSnoopPortNumLeavesSend_Type = Unsigned32
_IgmpSnoopPortNumLeavesSend_Object = MibTableColumn
igmpSnoopPortNumLeavesSend = _IgmpSnoopPortNumLeavesSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 9),
    _IgmpSnoopPortNumLeavesSend_Type()
)
igmpSnoopPortNumLeavesSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumLeavesSend.setStatus("current")
_IgmpSnoopPortNumLeaves_Type = Unsigned32
_IgmpSnoopPortNumLeaves_Object = MibTableColumn
igmpSnoopPortNumLeaves = _IgmpSnoopPortNumLeaves_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 10),
    _IgmpSnoopPortNumLeaves_Type()
)
igmpSnoopPortNumLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumLeaves.setStatus("current")
_IgmpSnoopPortNumGeneralQuerySend_Type = Unsigned32
_IgmpSnoopPortNumGeneralQuerySend_Object = MibTableColumn
igmpSnoopPortNumGeneralQuerySend = _IgmpSnoopPortNumGeneralQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 11),
    _IgmpSnoopPortNumGeneralQuerySend_Type()
)
igmpSnoopPortNumGeneralQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumGeneralQuerySend.setStatus("current")
_IgmpSnoopPortNumGeneralQueryRecevied_Type = Unsigned32
_IgmpSnoopPortNumGeneralQueryRecevied_Object = MibTableColumn
igmpSnoopPortNumGeneralQueryRecevied = _IgmpSnoopPortNumGeneralQueryRecevied_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 12),
    _IgmpSnoopPortNumGeneralQueryRecevied_Type()
)
igmpSnoopPortNumGeneralQueryRecevied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumGeneralQueryRecevied.setStatus("current")
_IgmpSnoopPortNumSepcificQuerySend_Type = Unsigned32
_IgmpSnoopPortNumSepcificQuerySend_Object = MibTableColumn
igmpSnoopPortNumSepcificQuerySend = _IgmpSnoopPortNumSepcificQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 13),
    _IgmpSnoopPortNumSepcificQuerySend_Type()
)
igmpSnoopPortNumSepcificQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumSepcificQuerySend.setStatus("current")
_IgmpSnoopPortNumSpecificQueryReceived_Type = Unsigned32
_IgmpSnoopPortNumSpecificQueryReceived_Object = MibTableColumn
igmpSnoopPortNumSpecificQueryReceived = _IgmpSnoopPortNumSpecificQueryReceived_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 14),
    _IgmpSnoopPortNumSpecificQueryReceived_Type()
)
igmpSnoopPortNumSpecificQueryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumSpecificQueryReceived.setStatus("current")
_IgmpSnoopPortNumInvalidReport_Type = Unsigned32
_IgmpSnoopPortNumInvalidReport_Object = MibTableColumn
igmpSnoopPortNumInvalidReport = _IgmpSnoopPortNumInvalidReport_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 15),
    _IgmpSnoopPortNumInvalidReport_Type()
)
igmpSnoopPortNumInvalidReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopPortNumInvalidReport.setStatus("current")
_IgmpSnoopPortClearStatistics_Type = TruthValue
_IgmpSnoopPortClearStatistics_Object = MibTableColumn
igmpSnoopPortClearStatistics = _IgmpSnoopPortClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 27, 1, 16),
    _IgmpSnoopPortClearStatistics_Type()
)
igmpSnoopPortClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopPortClearStatistics.setStatus("current")
_IgmpSnoopGlobalMgt_ObjectIdentity = ObjectIdentity
igmpSnoopGlobalMgt = _IgmpSnoopGlobalMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 28)
)


class _IgmpSnoopProxyReporting_Type(EnabledStatus):
    """Custom type igmpSnoopProxyReporting based on EnabledStatus"""


_IgmpSnoopProxyReporting_Object = MibScalar
igmpSnoopProxyReporting = _IgmpSnoopProxyReporting_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 28, 1),
    _IgmpSnoopProxyReporting_Type()
)
igmpSnoopProxyReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProxyReporting.setStatus("current")


class _IgmpSnoopRouterAlertOptionCheck_Type(EnabledStatus):
    """Custom type igmpSnoopRouterAlertOptionCheck based on EnabledStatus"""


_IgmpSnoopRouterAlertOptionCheck_Object = MibScalar
igmpSnoopRouterAlertOptionCheck = _IgmpSnoopRouterAlertOptionCheck_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 28, 2),
    _IgmpSnoopRouterAlertOptionCheck_Type()
)
igmpSnoopRouterAlertOptionCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopRouterAlertOptionCheck.setStatus("current")


class _IgmpSnoopTcnFlood_Type(EnabledStatus):
    """Custom type igmpSnoopTcnFlood based on EnabledStatus"""


_IgmpSnoopTcnFlood_Object = MibScalar
igmpSnoopTcnFlood = _IgmpSnoopTcnFlood_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 28, 3),
    _IgmpSnoopTcnFlood_Type()
)
igmpSnoopTcnFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopTcnFlood.setStatus("current")


class _IgmpSnoopTcnQuerySolicit_Type(EnabledStatus):
    """Custom type igmpSnoopTcnQuerySolicit based on EnabledStatus"""


_IgmpSnoopTcnQuerySolicit_Object = MibScalar
igmpSnoopTcnQuerySolicit = _IgmpSnoopTcnQuerySolicit_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 28, 4),
    _IgmpSnoopTcnQuerySolicit_Type()
)
igmpSnoopTcnQuerySolicit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopTcnQuerySolicit.setStatus("current")


class _IgmpSnoopUnregisteredDataFlood_Type(EnabledStatus):
    """Custom type igmpSnoopUnregisteredDataFlood based on EnabledStatus"""


_IgmpSnoopUnregisteredDataFlood_Object = MibScalar
igmpSnoopUnregisteredDataFlood = _IgmpSnoopUnregisteredDataFlood_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 28, 5),
    _IgmpSnoopUnregisteredDataFlood_Type()
)
igmpSnoopUnregisteredDataFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopUnregisteredDataFlood.setStatus("current")


class _IgmpSnoopUnsolicitedReportInterval_Type(Unsigned32):
    """Custom type igmpSnoopUnsolicitedReportInterval based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IgmpSnoopUnsolicitedReportInterval_Type.__name__ = "Unsigned32"
_IgmpSnoopUnsolicitedReportInterval_Object = MibScalar
igmpSnoopUnsolicitedReportInterval = _IgmpSnoopUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 28, 6),
    _IgmpSnoopUnsolicitedReportInterval_Type()
)
igmpSnoopUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopUnsolicitedReportInterval.setStatus("current")


class _IgmpSnoopVersionExclusive_Type(EnabledStatus):
    """Custom type igmpSnoopVersionExclusive based on EnabledStatus"""


_IgmpSnoopVersionExclusive_Object = MibScalar
igmpSnoopVersionExclusive = _IgmpSnoopVersionExclusive_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 28, 7),
    _IgmpSnoopVersionExclusive_Type()
)
igmpSnoopVersionExclusive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVersionExclusive.setStatus("current")


class _IgmpSnoopMrouterForwardMode_Type(Integer32):
    """Custom type igmpSnoopMrouterForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("forward", 2))
    )


_IgmpSnoopMrouterForwardMode_Type.__name__ = "Integer32"
_IgmpSnoopMrouterForwardMode_Object = MibScalar
igmpSnoopMrouterForwardMode = _IgmpSnoopMrouterForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 28, 8),
    _IgmpSnoopMrouterForwardMode_Type()
)
igmpSnoopMrouterForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopMrouterForwardMode.setStatus("current")


class _IgmpSnoopForwardingPriority_Type(Integer32):
    """Custom type igmpSnoopForwardingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(65535, 65535),
    )


_IgmpSnoopForwardingPriority_Type.__name__ = "Integer32"
_IgmpSnoopForwardingPriority_Object = MibScalar
igmpSnoopForwardingPriority = _IgmpSnoopForwardingPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 29),
    _IgmpSnoopForwardingPriority_Type()
)
igmpSnoopForwardingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopForwardingPriority.setStatus("current")
_IgmpSnoopQueryDropTable_Object = MibTable
igmpSnoopQueryDropTable = _IgmpSnoopQueryDropTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 30)
)
if mibBuilder.loadTexts:
    igmpSnoopQueryDropTable.setStatus("current")
_IgmpSnoopQueryDropEntry_Object = MibTableRow
igmpSnoopQueryDropEntry = _IgmpSnoopQueryDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 30, 1)
)
igmpSnoopQueryDropEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopQueryDropPortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopQueryDropEntry.setStatus("current")
_IgmpSnoopQueryDropPortIndex_Type = Unsigned32
_IgmpSnoopQueryDropPortIndex_Object = MibTableColumn
igmpSnoopQueryDropPortIndex = _IgmpSnoopQueryDropPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 30, 1, 1),
    _IgmpSnoopQueryDropPortIndex_Type()
)
igmpSnoopQueryDropPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopQueryDropPortIndex.setStatus("current")


class _IgmpSnoopQueryDropVlanBitmap_Type(OctetString):
    """Custom type igmpSnoopQueryDropVlanBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_IgmpSnoopQueryDropVlanBitmap_Type.__name__ = "OctetString"
_IgmpSnoopQueryDropVlanBitmap_Object = MibTableColumn
igmpSnoopQueryDropVlanBitmap = _IgmpSnoopQueryDropVlanBitmap_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 30, 1, 2),
    _IgmpSnoopQueryDropVlanBitmap_Type()
)
igmpSnoopQueryDropVlanBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryDropVlanBitmap.setStatus("current")
_IgmpSnoopClearDynamicGroups_Type = TruthValue
_IgmpSnoopClearDynamicGroups_Object = MibScalar
igmpSnoopClearDynamicGroups = _IgmpSnoopClearDynamicGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 32),
    _IgmpSnoopClearDynamicGroups_Type()
)
igmpSnoopClearDynamicGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopClearDynamicGroups.setStatus("current")
_IgmpSnoopVlanTable_Object = MibTable
igmpSnoopVlanTable = _IgmpSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33)
)
if mibBuilder.loadTexts:
    igmpSnoopVlanTable.setStatus("current")
_IgmpSnoopVlanEntry_Object = MibTableRow
igmpSnoopVlanEntry = _IgmpSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1)
)
igmpSnoopVlanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "igmpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopVlanEntry.setStatus("current")
_IgmpSnoopVlanIndex_Type = VlanIndex
_IgmpSnoopVlanIndex_Object = MibTableColumn
igmpSnoopVlanIndex = _IgmpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 1),
    _IgmpSnoopVlanIndex_Type()
)
igmpSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopVlanIndex.setStatus("current")
_IgmpSnoopVlanNumGroups_Type = Unsigned32
_IgmpSnoopVlanNumGroups_Object = MibTableColumn
igmpSnoopVlanNumGroups = _IgmpSnoopVlanNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 2),
    _IgmpSnoopVlanNumGroups_Type()
)
igmpSnoopVlanNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumGroups.setStatus("current")
_IgmpSnoopVlanNumJoinSend_Type = Unsigned32
_IgmpSnoopVlanNumJoinSend_Object = MibTableColumn
igmpSnoopVlanNumJoinSend = _IgmpSnoopVlanNumJoinSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 3),
    _IgmpSnoopVlanNumJoinSend_Type()
)
igmpSnoopVlanNumJoinSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumJoinSend.setStatus("current")
_IgmpSnoopVlanNumJoins_Type = Unsigned32
_IgmpSnoopVlanNumJoins_Object = MibTableColumn
igmpSnoopVlanNumJoins = _IgmpSnoopVlanNumJoins_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 4),
    _IgmpSnoopVlanNumJoins_Type()
)
igmpSnoopVlanNumJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumJoins.setStatus("current")
_IgmpSnoopVlanNumJoinSuccess_Type = Unsigned32
_IgmpSnoopVlanNumJoinSuccess_Object = MibTableColumn
igmpSnoopVlanNumJoinSuccess = _IgmpSnoopVlanNumJoinSuccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 5),
    _IgmpSnoopVlanNumJoinSuccess_Type()
)
igmpSnoopVlanNumJoinSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumJoinSuccess.setStatus("current")
_IgmpSnoopVlanNumLeavesSend_Type = Unsigned32
_IgmpSnoopVlanNumLeavesSend_Object = MibTableColumn
igmpSnoopVlanNumLeavesSend = _IgmpSnoopVlanNumLeavesSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 6),
    _IgmpSnoopVlanNumLeavesSend_Type()
)
igmpSnoopVlanNumLeavesSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumLeavesSend.setStatus("current")
_IgmpSnoopVlanNumLeaves_Type = Unsigned32
_IgmpSnoopVlanNumLeaves_Object = MibTableColumn
igmpSnoopVlanNumLeaves = _IgmpSnoopVlanNumLeaves_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 7),
    _IgmpSnoopVlanNumLeaves_Type()
)
igmpSnoopVlanNumLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumLeaves.setStatus("current")
_IgmpSnoopVlanNumGeneralQuerySend_Type = Unsigned32
_IgmpSnoopVlanNumGeneralQuerySend_Object = MibTableColumn
igmpSnoopVlanNumGeneralQuerySend = _IgmpSnoopVlanNumGeneralQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 8),
    _IgmpSnoopVlanNumGeneralQuerySend_Type()
)
igmpSnoopVlanNumGeneralQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumGeneralQuerySend.setStatus("current")
_IgmpSnoopVlanNumGeneralQueryRecevied_Type = Unsigned32
_IgmpSnoopVlanNumGeneralQueryRecevied_Object = MibTableColumn
igmpSnoopVlanNumGeneralQueryRecevied = _IgmpSnoopVlanNumGeneralQueryRecevied_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 9),
    _IgmpSnoopVlanNumGeneralQueryRecevied_Type()
)
igmpSnoopVlanNumGeneralQueryRecevied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumGeneralQueryRecevied.setStatus("current")
_IgmpSnoopVlanNumSepcificQuerySend_Type = Unsigned32
_IgmpSnoopVlanNumSepcificQuerySend_Object = MibTableColumn
igmpSnoopVlanNumSepcificQuerySend = _IgmpSnoopVlanNumSepcificQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 10),
    _IgmpSnoopVlanNumSepcificQuerySend_Type()
)
igmpSnoopVlanNumSepcificQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumSepcificQuerySend.setStatus("current")
_IgmpSnoopVlanNumSpecificQueryReceived_Type = Unsigned32
_IgmpSnoopVlanNumSpecificQueryReceived_Object = MibTableColumn
igmpSnoopVlanNumSpecificQueryReceived = _IgmpSnoopVlanNumSpecificQueryReceived_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 11),
    _IgmpSnoopVlanNumSpecificQueryReceived_Type()
)
igmpSnoopVlanNumSpecificQueryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumSpecificQueryReceived.setStatus("current")
_IgmpSnoopVlanNumInvalidReport_Type = Unsigned32
_IgmpSnoopVlanNumInvalidReport_Object = MibTableColumn
igmpSnoopVlanNumInvalidReport = _IgmpSnoopVlanNumInvalidReport_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 12),
    _IgmpSnoopVlanNumInvalidReport_Type()
)
igmpSnoopVlanNumInvalidReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopVlanNumInvalidReport.setStatus("current")
_IgmpSnoopVlanClearStatistics_Type = TruthValue
_IgmpSnoopVlanClearStatistics_Object = MibTableColumn
igmpSnoopVlanClearStatistics = _IgmpSnoopVlanClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 9, 33, 1, 13),
    _IgmpSnoopVlanClearStatistics_Type()
)
igmpSnoopVlanClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVlanClearStatistics.setStatus("current")
_IpMgt_ObjectIdentity = ObjectIdentity
ipMgt = _IpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10)
)
_NetConfigTable_Object = MibTable
netConfigTable = _NetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 1)
)
if mibBuilder.loadTexts:
    netConfigTable.setStatus("current")
_NetConfigEntry_Object = MibTableRow
netConfigEntry = _NetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 1, 1)
)
netConfigEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "netConfigIfIndex"),
    (0, "ECS2100-28PP-MIB", "netConfigIPAddress"),
    (0, "ECS2100-28PP-MIB", "netConfigSubnetMask"),
)
if mibBuilder.loadTexts:
    netConfigEntry.setStatus("current")


class _NetConfigIfIndex_Type(Integer32):
    """Custom type netConfigIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 5097),
    )


_NetConfigIfIndex_Type.__name__ = "Integer32"
_NetConfigIfIndex_Object = MibTableColumn
netConfigIfIndex = _NetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 1, 1, 1),
    _NetConfigIfIndex_Type()
)
netConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIfIndex.setStatus("current")
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibTableColumn
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 1, 1, 2),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("current")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibTableColumn
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 1, 1, 5),
    _NetConfigUnnumbered_Type()
)
netConfigUnnumbered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigUnnumbered.setStatus("current")
_NetConfigStatus_Type = RowStatus
_NetConfigStatus_Object = MibTableColumn
netConfigStatus = _NetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 1, 1, 6),
    _NetConfigStatus_Type()
)
netConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigStatus.setStatus("current")
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 2),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("current")
_IpHttpState_Type = EnabledStatus
_IpHttpState_Object = MibScalar
ipHttpState = _IpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 5),
    _IpDhcpRestart_Type()
)
ipDhcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpRestart.setStatus("current")
_IpHttpsState_Type = EnabledStatus
_IpHttpsState_Object = MibScalar
ipHttpsState = _IpHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 6),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 7),
    _IpHttpsPort_Type()
)
ipHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsPort.setStatus("current")
_DhcpMgt_ObjectIdentity = ObjectIdentity
dhcpMgt = _DhcpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11)
)
_DhcpClient_ObjectIdentity = ObjectIdentity
dhcpClient = _DhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 1)
)
_DhcpcOptions_ObjectIdentity = ObjectIdentity
dhcpcOptions = _DhcpcOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 1, 1)
)
_DhcpcInterfaceTable_Object = MibTable
dhcpcInterfaceTable = _DhcpcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpcInterfaceTable.setStatus("current")
_DhcpcInterfaceEntry_Object = MibTableRow
dhcpcInterfaceEntry = _DhcpcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 1, 1, 1, 1)
)
dhcpcInterfaceEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "dhcpcIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpcInterfaceEntry.setStatus("current")


class _DhcpcIfIndex_Type(Integer32):
    """Custom type dhcpcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_DhcpcIfIndex_Type.__name__ = "Integer32"
_DhcpcIfIndex_Object = MibTableColumn
dhcpcIfIndex = _DhcpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 1, 1, 1, 1, 1),
    _DhcpcIfIndex_Type()
)
dhcpcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpcIfIndex.setStatus("current")


class _DhcpcIfVendorClassIdMode_Type(Integer32):
    """Custom type dhcpcIfVendorClassIdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hex", 3),
          ("notSpecify", 1),
          ("text", 2))
    )


_DhcpcIfVendorClassIdMode_Type.__name__ = "Integer32"
_DhcpcIfVendorClassIdMode_Object = MibTableColumn
dhcpcIfVendorClassIdMode = _DhcpcIfVendorClassIdMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 1, 1, 1, 1, 4),
    _DhcpcIfVendorClassIdMode_Type()
)
dhcpcIfVendorClassIdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpcIfVendorClassIdMode.setStatus("current")


class _DhcpcIfVendorClassId_Type(OctetString):
    """Custom type dhcpcIfVendorClassId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DhcpcIfVendorClassId_Type.__name__ = "OctetString"
_DhcpcIfVendorClassId_Object = MibTableColumn
dhcpcIfVendorClassId = _DhcpcIfVendorClassId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 1, 1, 1, 1, 5),
    _DhcpcIfVendorClassId_Type()
)
dhcpcIfVendorClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpcIfVendorClassId.setStatus("current")
_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 2)
)


class _DhcpRelayRestart_Type(Integer32):
    """Custom type dhcpRelayRestart based on Integer32"""
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


_DhcpRelayRestart_Type.__name__ = "Integer32"
_DhcpRelayRestart_Object = MibScalar
dhcpRelayRestart = _DhcpRelayRestart_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 2, 3),
    _DhcpRelayRestart_Type()
)
dhcpRelayRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayRestart.setStatus("current")
_DhcpRelayServerInetAddrTable_Object = MibTable
dhcpRelayServerInetAddrTable = _DhcpRelayServerInetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 2, 4)
)
if mibBuilder.loadTexts:
    dhcpRelayServerInetAddrTable.setStatus("current")
_DhcpRelayServerInetAddrEntry_Object = MibTableRow
dhcpRelayServerInetAddrEntry = _DhcpRelayServerInetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 2, 4, 1)
)
dhcpRelayServerInetAddrEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "dhcpRelayServerInetAddrIfIndex"),
    (0, "ECS2100-28PP-MIB", "dhcpRelayServerInetAddrIndex"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerInetAddrEntry.setStatus("current")


class _DhcpRelayServerInetAddrIfIndex_Type(Integer32):
    """Custom type dhcpRelayServerInetAddrIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_DhcpRelayServerInetAddrIfIndex_Type.__name__ = "Integer32"
_DhcpRelayServerInetAddrIfIndex_Object = MibTableColumn
dhcpRelayServerInetAddrIfIndex = _DhcpRelayServerInetAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 2, 4, 1, 1),
    _DhcpRelayServerInetAddrIfIndex_Type()
)
dhcpRelayServerInetAddrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpRelayServerInetAddrIfIndex.setStatus("current")


class _DhcpRelayServerInetAddrIndex_Type(Integer32):
    """Custom type dhcpRelayServerInetAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DhcpRelayServerInetAddrIndex_Type.__name__ = "Integer32"
_DhcpRelayServerInetAddrIndex_Object = MibTableColumn
dhcpRelayServerInetAddrIndex = _DhcpRelayServerInetAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 2, 4, 1, 2),
    _DhcpRelayServerInetAddrIndex_Type()
)
dhcpRelayServerInetAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpRelayServerInetAddrIndex.setStatus("current")
_DhcpRelayServerInetAddressType_Type = InetAddressType
_DhcpRelayServerInetAddressType_Object = MibTableColumn
dhcpRelayServerInetAddressType = _DhcpRelayServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 2, 4, 1, 3),
    _DhcpRelayServerInetAddressType_Type()
)
dhcpRelayServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayServerInetAddressType.setStatus("current")
_DhcpRelayServerInetAddress_Type = InetAddress
_DhcpRelayServerInetAddress_Object = MibTableColumn
dhcpRelayServerInetAddress = _DhcpRelayServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 2, 4, 1, 4),
    _DhcpRelayServerInetAddress_Type()
)
dhcpRelayServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayServerInetAddress.setStatus("current")
_DhcpOption82_ObjectIdentity = ObjectIdentity
dhcpOption82 = _DhcpOption82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4)
)


class _DhcpOption82Status_Type(Integer32):
    """Custom type dhcpOption82Status based on Integer32"""
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


_DhcpOption82Status_Type.__name__ = "Integer32"
_DhcpOption82Status_Object = MibScalar
dhcpOption82Status = _DhcpOption82Status_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4, 1),
    _DhcpOption82Status_Type()
)
dhcpOption82Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82Status.setStatus("current")


class _DhcpOption82Policy_Type(Integer32):
    """Custom type dhcpOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 3),
          ("replace", 2))
    )


_DhcpOption82Policy_Type.__name__ = "Integer32"
_DhcpOption82Policy_Object = MibScalar
dhcpOption82Policy = _DhcpOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4, 2),
    _DhcpOption82Policy_Type()
)
dhcpOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82Policy.setStatus("current")


class _DhcpOption82RemoteIDMode_Type(Integer32):
    """Custom type dhcpOption82RemoteIDMode based on Integer32"""
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
        *(("configured-string", 5),
          ("ip-address-in-ascii", 4),
          ("ip-address-in-hex", 3),
          ("mac-address-in-ascii", 2),
          ("mac-address-in-hex", 1))
    )


_DhcpOption82RemoteIDMode_Type.__name__ = "Integer32"
_DhcpOption82RemoteIDMode_Object = MibScalar
dhcpOption82RemoteIDMode = _DhcpOption82RemoteIDMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4, 3),
    _DhcpOption82RemoteIDMode_Type()
)
dhcpOption82RemoteIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82RemoteIDMode.setStatus("current")


class _DhcpOption82RemoteIDString_Type(OctetString):
    """Custom type dhcpOption82RemoteIDString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DhcpOption82RemoteIDString_Type.__name__ = "OctetString"
_DhcpOption82RemoteIDString_Object = MibScalar
dhcpOption82RemoteIDString = _DhcpOption82RemoteIDString_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4, 4),
    _DhcpOption82RemoteIDString_Type()
)
dhcpOption82RemoteIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82RemoteIDString.setStatus("current")


class _DhcpOption82EncodeFormat_Type(Integer32):
    """Custom type dhcpOption82EncodeFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extra-subtype-included", 1),
          ("no-extra-subtype-included", 2))
    )


_DhcpOption82EncodeFormat_Type.__name__ = "Integer32"
_DhcpOption82EncodeFormat_Object = MibScalar
dhcpOption82EncodeFormat = _DhcpOption82EncodeFormat_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4, 5),
    _DhcpOption82EncodeFormat_Type()
)
dhcpOption82EncodeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82EncodeFormat.setStatus("current")
_DhcpOption82RelayServerAddrTable_Object = MibTable
dhcpOption82RelayServerAddrTable = _DhcpOption82RelayServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4, 6)
)
if mibBuilder.loadTexts:
    dhcpOption82RelayServerAddrTable.setStatus("current")
_DhcpOption82RelayServerAddrEntry_Object = MibTableRow
dhcpOption82RelayServerAddrEntry = _DhcpOption82RelayServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4, 6, 1)
)
dhcpOption82RelayServerAddrEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "dhcpOption82RelayServerAddrIndex"),
)
if mibBuilder.loadTexts:
    dhcpOption82RelayServerAddrEntry.setStatus("current")


class _DhcpOption82RelayServerAddrIndex_Type(Integer32):
    """Custom type dhcpOption82RelayServerAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DhcpOption82RelayServerAddrIndex_Type.__name__ = "Integer32"
_DhcpOption82RelayServerAddrIndex_Object = MibTableColumn
dhcpOption82RelayServerAddrIndex = _DhcpOption82RelayServerAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4, 6, 1, 1),
    _DhcpOption82RelayServerAddrIndex_Type()
)
dhcpOption82RelayServerAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpOption82RelayServerAddrIndex.setStatus("current")
_DhcpOption82RelayServerAddrServerIp_Type = IpAddress
_DhcpOption82RelayServerAddrServerIp_Object = MibTableColumn
dhcpOption82RelayServerAddrServerIp = _DhcpOption82RelayServerAddrServerIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 11, 4, 6, 1, 2),
    _DhcpOption82RelayServerAddrServerIp_Type()
)
dhcpOption82RelayServerAddrServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82RelayServerAddrServerIp.setStatus("current")
_PingMgt_ObjectIdentity = ObjectIdentity
pingMgt = _PingMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15)
)
_PingIpAddress_Type = IpAddress
_PingIpAddress_Object = MibScalar
pingIpAddress = _PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 1),
    _PingIpAddress_Type()
)
pingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIpAddress.setStatus("current")


class _PingPacketSize_Type(Integer32):
    """Custom type pingPacketSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 512),
    )


_PingPacketSize_Type.__name__ = "Integer32"
_PingPacketSize_Object = MibScalar
pingPacketSize = _PingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 2),
    _PingPacketSize_Type()
)
pingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingPacketSize.setStatus("current")
_PingCompleted_Type = TruthValue
_PingCompleted_Object = MibScalar
pingCompleted = _PingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 4),
    _PingCompleted_Type()
)
pingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingCompleted.setStatus("current")


class _PingAction_Type(Integer32):
    """Custom type pingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("pingStart", 2))
    )


_PingAction_Type.__name__ = "Integer32"
_PingAction_Object = MibScalar
pingAction = _PingAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 5),
    _PingAction_Type()
)
pingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingAction.setStatus("current")


class _PingProbeCount_Type(Integer32):
    """Custom type pingProbeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PingProbeCount_Type.__name__ = "Integer32"
_PingProbeCount_Object = MibScalar
pingProbeCount = _PingProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 6),
    _PingProbeCount_Type()
)
pingProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingProbeCount.setStatus("current")
_PingSentPackets_Type = Integer32
_PingSentPackets_Object = MibScalar
pingSentPackets = _PingSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 7),
    _PingSentPackets_Type()
)
pingSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingSentPackets.setStatus("current")
_PingReceivedPackets_Type = Integer32
_PingReceivedPackets_Object = MibScalar
pingReceivedPackets = _PingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 8),
    _PingReceivedPackets_Type()
)
pingReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingReceivedPackets.setStatus("current")


class _PingPacketLossRate_Type(Integer32):
    """Custom type pingPacketLossRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PingPacketLossRate_Type.__name__ = "Integer32"
_PingPacketLossRate_Object = MibScalar
pingPacketLossRate = _PingPacketLossRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 9),
    _PingPacketLossRate_Type()
)
pingPacketLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingPacketLossRate.setStatus("current")
_PingHistoryTable_Object = MibTable
pingHistoryTable = _PingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 10)
)
if mibBuilder.loadTexts:
    pingHistoryTable.setStatus("current")
_PingHistoryEntry_Object = MibTableRow
pingHistoryEntry = _PingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 10, 1)
)
pingHistoryEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "pingHistoryIndex"),
)
if mibBuilder.loadTexts:
    pingHistoryEntry.setStatus("current")


class _PingHistoryIndex_Type(Integer32):
    """Custom type pingHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PingHistoryIndex_Type.__name__ = "Integer32"
_PingHistoryIndex_Object = MibTableColumn
pingHistoryIndex = _PingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 10, 1, 1),
    _PingHistoryIndex_Type()
)
pingHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingHistoryIndex.setStatus("current")
_PingHistoryResponse_Type = Integer32
_PingHistoryResponse_Object = MibTableColumn
pingHistoryResponse = _PingHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 15, 10, 1, 2),
    _PingHistoryResponse_Type()
)
pingHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    pingHistoryResponse.setUnits("milliseconds")


class _ArpCacheDeleteAll_Type(Integer32):
    """Custom type arpCacheDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("noDelete", 2))
    )


_ArpCacheDeleteAll_Type.__name__ = "Integer32"
_ArpCacheDeleteAll_Object = MibScalar
arpCacheDeleteAll = _ArpCacheDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 10, 17),
    _ArpCacheDeleteAll_Type()
)
arpCacheDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpCacheDeleteAll.setStatus("current")
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIndex_Type = Unsigned32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 1, 1, 2),
    _VlanAddressMethod_Type()
)
vlanAddressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAddressMethod.setStatus("current")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 2)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 2, 1)
)
vlanPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "vlanPortIndex"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("current")


class _VlanPortIndex_Type(Integer32):
    """Custom type vlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_VlanPortIndex_Type.__name__ = "Integer32"
_VlanPortIndex_Object = MibTableColumn
vlanPortIndex = _VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 2, 1, 2),
    _VlanPortMode_Type()
)
vlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMode.setStatus("current")


class _VlanPortPrivateVlanType_Type(Integer32):
    """Custom type vlanPortPrivateVlanType based on Integer32"""
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
        *(("community", 3),
          ("isolated", 2),
          ("normal", 1),
          ("promiscous", 4))
    )


_VlanPortPrivateVlanType_Type.__name__ = "Integer32"
_VlanPortPrivateVlanType_Object = MibTableColumn
vlanPortPrivateVlanType = _VlanPortPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 2, 1, 3),
    _VlanPortPrivateVlanType_Type()
)
vlanPortPrivateVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortPrivateVlanType.setStatus("current")
_VoiceVlanMgt_ObjectIdentity = ObjectIdentity
voiceVlanMgt = _VoiceVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6)
)
_VoiceVlanOuiTable_Object = MibTable
voiceVlanOuiTable = _VoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 1)
)
if mibBuilder.loadTexts:
    voiceVlanOuiTable.setStatus("current")
_VoiceVlanOuiEntry_Object = MibTableRow
voiceVlanOuiEntry = _VoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 1, 1)
)
voiceVlanOuiEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "voiceVlanOuiAddress"),
)
if mibBuilder.loadTexts:
    voiceVlanOuiEntry.setStatus("current")
_VoiceVlanOuiAddress_Type = MacAddress
_VoiceVlanOuiAddress_Object = MibTableColumn
voiceVlanOuiAddress = _VoiceVlanOuiAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 1, 1, 1),
    _VoiceVlanOuiAddress_Type()
)
voiceVlanOuiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceVlanOuiAddress.setStatus("current")
_VoiceVlanOuiMask_Type = MacAddress
_VoiceVlanOuiMask_Object = MibTableColumn
voiceVlanOuiMask = _VoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 1, 1, 2),
    _VoiceVlanOuiMask_Type()
)
voiceVlanOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanOuiMask.setStatus("current")


class _VoiceVlanOuiDescription_Type(DisplayString):
    """Custom type voiceVlanOuiDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_VoiceVlanOuiDescription_Type.__name__ = "DisplayString"
_VoiceVlanOuiDescription_Object = MibTableColumn
voiceVlanOuiDescription = _VoiceVlanOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 1, 1, 3),
    _VoiceVlanOuiDescription_Type()
)
voiceVlanOuiDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanOuiDescription.setStatus("current")
_VoiceVlanOuiStatus_Type = ValidStatus
_VoiceVlanOuiStatus_Object = MibTableColumn
voiceVlanOuiStatus = _VoiceVlanOuiStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 1, 1, 4),
    _VoiceVlanOuiStatus_Type()
)
voiceVlanOuiStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voiceVlanOuiStatus.setStatus("current")


class _VoiceVlanEnabledId_Type(Integer32):
    """Custom type voiceVlanEnabledId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4093),
    )


_VoiceVlanEnabledId_Type.__name__ = "Integer32"
_VoiceVlanEnabledId_Object = MibScalar
voiceVlanEnabledId = _VoiceVlanEnabledId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 2),
    _VoiceVlanEnabledId_Type()
)
voiceVlanEnabledId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanEnabledId.setStatus("current")


class _VoiceVlanAgingTime_Type(Integer32):
    """Custom type voiceVlanAgingTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 43200),
    )


_VoiceVlanAgingTime_Type.__name__ = "Integer32"
_VoiceVlanAgingTime_Object = MibScalar
voiceVlanAgingTime = _VoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 3),
    _VoiceVlanAgingTime_Type()
)
voiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanAgingTime.setStatus("current")
_VoiceVlanPortTable_Object = MibTable
voiceVlanPortTable = _VoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 7)
)
if mibBuilder.loadTexts:
    voiceVlanPortTable.setStatus("current")
_VoiceVlanPortEntry_Object = MibTableRow
voiceVlanPortEntry = _VoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 7, 1)
)
voiceVlanPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "voiceVlanPortIfIndex"),
)
if mibBuilder.loadTexts:
    voiceVlanPortEntry.setStatus("current")


class _VoiceVlanPortIfIndex_Type(Integer32):
    """Custom type voiceVlanPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VoiceVlanPortIfIndex_Type.__name__ = "Integer32"
_VoiceVlanPortIfIndex_Object = MibTableColumn
voiceVlanPortIfIndex = _VoiceVlanPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 7, 1, 1),
    _VoiceVlanPortIfIndex_Type()
)
voiceVlanPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voiceVlanPortIfIndex.setStatus("current")


class _VoiceVlanPortMode_Type(Integer32):
    """Custom type voiceVlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2),
          ("none", 3))
    )


_VoiceVlanPortMode_Type.__name__ = "Integer32"
_VoiceVlanPortMode_Object = MibTableColumn
voiceVlanPortMode = _VoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 7, 1, 2),
    _VoiceVlanPortMode_Type()
)
voiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortMode.setStatus("current")
_VoiceVlanPortSecurity_Type = EnabledStatus
_VoiceVlanPortSecurity_Object = MibTableColumn
voiceVlanPortSecurity = _VoiceVlanPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 7, 1, 3),
    _VoiceVlanPortSecurity_Type()
)
voiceVlanPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortSecurity.setStatus("current")


class _VoiceVlanPortPriority_Type(Integer32):
    """Custom type voiceVlanPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_VoiceVlanPortPriority_Type.__name__ = "Integer32"
_VoiceVlanPortPriority_Object = MibTableColumn
voiceVlanPortPriority = _VoiceVlanPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 7, 1, 4),
    _VoiceVlanPortPriority_Type()
)
voiceVlanPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortPriority.setStatus("current")
_VoiceVlanPortRuleOui_Type = EnabledStatus
_VoiceVlanPortRuleOui_Object = MibTableColumn
voiceVlanPortRuleOui = _VoiceVlanPortRuleOui_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 7, 1, 5),
    _VoiceVlanPortRuleOui_Type()
)
voiceVlanPortRuleOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortRuleOui.setStatus("current")
_VoiceVlanPortRuleLldp_Type = EnabledStatus
_VoiceVlanPortRuleLldp_Object = MibTableColumn
voiceVlanPortRuleLldp = _VoiceVlanPortRuleLldp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 7, 1, 6),
    _VoiceVlanPortRuleLldp_Type()
)
voiceVlanPortRuleLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortRuleLldp.setStatus("current")


class _VoiceVlanPortRemainAge_Type(DisplayString):
    """Custom type voiceVlanPortRemainAge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_VoiceVlanPortRemainAge_Type.__name__ = "DisplayString"
_VoiceVlanPortRemainAge_Object = MibTableColumn
voiceVlanPortRemainAge = _VoiceVlanPortRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 6, 7, 1, 7),
    _VoiceVlanPortRemainAge_Type()
)
voiceVlanPortRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceVlanPortRemainAge.setStatus("current")
_Dot1vProtocolExPortTable_Object = MibTable
dot1vProtocolExPortTable = _Dot1vProtocolExPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 10)
)
if mibBuilder.loadTexts:
    dot1vProtocolExPortTable.setStatus("current")
_Dot1vProtocolExPortEntry_Object = MibTableRow
dot1vProtocolExPortEntry = _Dot1vProtocolExPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 10, 1)
)
if mibBuilder.loadTexts:
    dot1vProtocolExPortEntry.setStatus("current")


class _Dot1vProtocolExPortGroupPriority_Type(Integer32):
    """Custom type dot1vProtocolExPortGroupPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1vProtocolExPortGroupPriority_Type.__name__ = "Integer32"
_Dot1vProtocolExPortGroupPriority_Object = MibTableColumn
dot1vProtocolExPortGroupPriority = _Dot1vProtocolExPortGroupPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 10, 1, 1),
    _Dot1vProtocolExPortGroupPriority_Type()
)
dot1vProtocolExPortGroupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1vProtocolExPortGroupPriority.setStatus("current")
_MacVlanTable_Object = MibTable
macVlanTable = _MacVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 11)
)
if mibBuilder.loadTexts:
    macVlanTable.setStatus("current")
_MacVlanEntry_Object = MibTableRow
macVlanEntry = _MacVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 11, 1)
)
macVlanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "macVlanMacMask"),
    (0, "ECS2100-28PP-MIB", "macVlanMacAddress"),
)
if mibBuilder.loadTexts:
    macVlanEntry.setStatus("current")
_MacVlanMacAddress_Type = MacAddress
_MacVlanMacAddress_Object = MibTableColumn
macVlanMacAddress = _MacVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 11, 1, 1),
    _MacVlanMacAddress_Type()
)
macVlanMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macVlanMacAddress.setStatus("current")
_MacVlanId_Type = VlanId
_MacVlanId_Object = MibTableColumn
macVlanId = _MacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 11, 1, 2),
    _MacVlanId_Type()
)
macVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macVlanId.setStatus("current")


class _MacVlanPriority_Type(Integer32):
    """Custom type macVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MacVlanPriority_Type.__name__ = "Integer32"
_MacVlanPriority_Object = MibTableColumn
macVlanPriority = _MacVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 11, 1, 3),
    _MacVlanPriority_Type()
)
macVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macVlanPriority.setStatus("current")
_MacVlanStatus_Type = ValidStatus
_MacVlanStatus_Object = MibTableColumn
macVlanStatus = _MacVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 11, 1, 4),
    _MacVlanStatus_Type()
)
macVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macVlanStatus.setStatus("current")
_MacVlanMacMask_Type = MacAddress
_MacVlanMacMask_Object = MibTableColumn
macVlanMacMask = _MacVlanMacMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 11, 1, 5),
    _MacVlanMacMask_Type()
)
macVlanMacMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macVlanMacMask.setStatus("current")


class _MacVlanClearAction_Type(Integer32):
    """Custom type macVlanClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noClear", 1))
    )


_MacVlanClearAction_Type.__name__ = "Integer32"
_MacVlanClearAction_Object = MibScalar
macVlanClearAction = _MacVlanClearAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 12),
    _MacVlanClearAction_Type()
)
macVlanClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macVlanClearAction.setStatus("current")
_SubnetVlanTable_Object = MibTable
subnetVlanTable = _SubnetVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 13)
)
if mibBuilder.loadTexts:
    subnetVlanTable.setStatus("current")
_SubnetVlanEntry_Object = MibTableRow
subnetVlanEntry = _SubnetVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 13, 1)
)
subnetVlanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "subnetVlanMask"),
    (0, "ECS2100-28PP-MIB", "subnetVlanIpAddress"),
)
if mibBuilder.loadTexts:
    subnetVlanEntry.setStatus("current")
_SubnetVlanIpAddress_Type = IpAddress
_SubnetVlanIpAddress_Object = MibTableColumn
subnetVlanIpAddress = _SubnetVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 13, 1, 1),
    _SubnetVlanIpAddress_Type()
)
subnetVlanIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetVlanIpAddress.setStatus("current")
_SubnetVlanMask_Type = IpAddress
_SubnetVlanMask_Object = MibTableColumn
subnetVlanMask = _SubnetVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 13, 1, 2),
    _SubnetVlanMask_Type()
)
subnetVlanMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetVlanMask.setStatus("current")


class _SubnetVlanId_Type(Integer32):
    """Custom type subnetVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SubnetVlanId_Type.__name__ = "Integer32"
_SubnetVlanId_Object = MibTableColumn
subnetVlanId = _SubnetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 13, 1, 3),
    _SubnetVlanId_Type()
)
subnetVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetVlanId.setStatus("current")


class _SubnetVlanPriority_Type(Integer32):
    """Custom type subnetVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SubnetVlanPriority_Type.__name__ = "Integer32"
_SubnetVlanPriority_Object = MibTableColumn
subnetVlanPriority = _SubnetVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 13, 1, 4),
    _SubnetVlanPriority_Type()
)
subnetVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetVlanPriority.setStatus("current")
_SubnetVlanStatus_Type = ValidStatus
_SubnetVlanStatus_Object = MibTableColumn
subnetVlanStatus = _SubnetVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 13, 1, 5),
    _SubnetVlanStatus_Type()
)
subnetVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetVlanStatus.setStatus("current")


class _SubnetVlanClearAction_Type(Integer32):
    """Custom type subnetVlanClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noClear", 1))
    )


_SubnetVlanClearAction_Type.__name__ = "Integer32"
_SubnetVlanClearAction_Object = MibScalar
subnetVlanClearAction = _SubnetVlanClearAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 14),
    _SubnetVlanClearAction_Type()
)
subnetVlanClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetVlanClearAction.setStatus("current")
_VlanStaticExtTable_Object = MibTable
vlanStaticExtTable = _VlanStaticExtTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 15)
)
if mibBuilder.loadTexts:
    vlanStaticExtTable.setStatus("current")
_VlanStaticExtEntry_Object = MibTableRow
vlanStaticExtEntry = _VlanStaticExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 15, 1)
)
if mibBuilder.loadTexts:
    vlanStaticExtEntry.setStatus("current")


class _VlanStaticExtRspanStatus_Type(Integer32):
    """Custom type vlanStaticExtRspanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destroy", 1),
          ("rspanVlan", 3),
          ("vlan", 2))
    )


_VlanStaticExtRspanStatus_Type.__name__ = "Integer32"
_VlanStaticExtRspanStatus_Object = MibTableColumn
vlanStaticExtRspanStatus = _VlanStaticExtRspanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 15, 1, 1),
    _VlanStaticExtRspanStatus_Type()
)
vlanStaticExtRspanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanStaticExtRspanStatus.setStatus("current")
_VlanStaticTable_Object = MibTable
vlanStaticTable = _VlanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 17)
)
if mibBuilder.loadTexts:
    vlanStaticTable.setStatus("current")
_VlanStaticEntry_Object = MibTableRow
vlanStaticEntry = _VlanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 17, 1)
)
vlanStaticEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "vlanStaticIndex"),
)
if mibBuilder.loadTexts:
    vlanStaticEntry.setStatus("current")
_VlanStaticIndex_Type = VlanIndex
_VlanStaticIndex_Object = MibTableColumn
vlanStaticIndex = _VlanStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 17, 1, 1),
    _VlanStaticIndex_Type()
)
vlanStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanStaticIndex.setStatus("current")


class _VlanStaticInterfaceType_Type(Integer32):
    """Custom type vlanStaticInterfaceType based on Integer32"""
    defaultValue = 135

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(135,
              136)
        )
    )
    namedValues = NamedValues(
        *(("l2vlan", 135),
          ("l3ipvlan", 136))
    )


_VlanStaticInterfaceType_Type.__name__ = "Integer32"
_VlanStaticInterfaceType_Object = MibTableColumn
vlanStaticInterfaceType = _VlanStaticInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 12, 17, 1, 2),
    _VlanStaticInterfaceType_Type()
)
vlanStaticInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanStaticInterfaceType.setStatus("current")
_PriorityMgt_ObjectIdentity = ObjectIdentity
priorityMgt = _PriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13)
)
_PrioWrrPortTable_Object = MibTable
prioWrrPortTable = _PrioWrrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 12)
)
if mibBuilder.loadTexts:
    prioWrrPortTable.setStatus("current")
_PrioWrrPortEntry_Object = MibTableRow
prioWrrPortEntry = _PrioWrrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 12, 1)
)
prioWrrPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "prioWrrPortIfIndex"),
    (0, "ECS2100-28PP-MIB", "prioWrrPortTrafficClass"),
)
if mibBuilder.loadTexts:
    prioWrrPortEntry.setStatus("current")
_PrioWrrPortIfIndex_Type = InterfaceIndex
_PrioWrrPortIfIndex_Object = MibTableColumn
prioWrrPortIfIndex = _PrioWrrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 12, 1, 1),
    _PrioWrrPortIfIndex_Type()
)
prioWrrPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioWrrPortIfIndex.setStatus("current")


class _PrioWrrPortTrafficClass_Type(Integer32):
    """Custom type prioWrrPortTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioWrrPortTrafficClass_Type.__name__ = "Integer32"
_PrioWrrPortTrafficClass_Object = MibTableColumn
prioWrrPortTrafficClass = _PrioWrrPortTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 12, 1, 2),
    _PrioWrrPortTrafficClass_Type()
)
prioWrrPortTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioWrrPortTrafficClass.setStatus("current")


class _PrioWrrPortWeight_Type(Integer32):
    """Custom type prioWrrPortWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_PrioWrrPortWeight_Type.__name__ = "Integer32"
_PrioWrrPortWeight_Object = MibTableColumn
prioWrrPortWeight = _PrioWrrPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 12, 1, 3),
    _PrioWrrPortWeight_Type()
)
prioWrrPortWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioWrrPortWeight.setStatus("current")
_PrioWrrPortStrictStatus_Type = EnabledStatus
_PrioWrrPortStrictStatus_Object = MibTableColumn
prioWrrPortStrictStatus = _PrioWrrPortStrictStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 12, 1, 4),
    _PrioWrrPortStrictStatus_Type()
)
prioWrrPortStrictStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioWrrPortStrictStatus.setStatus("current")
_PrioSchedModePortTable_Object = MibTable
prioSchedModePortTable = _PrioSchedModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 15)
)
if mibBuilder.loadTexts:
    prioSchedModePortTable.setStatus("current")
_PrioSchedModePortEntry_Object = MibTableRow
prioSchedModePortEntry = _PrioSchedModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 15, 1)
)
prioSchedModePortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "prioSchedModePortIndex"),
)
if mibBuilder.loadTexts:
    prioSchedModePortEntry.setStatus("current")
_PrioSchedModePortIndex_Type = InterfaceIndex
_PrioSchedModePortIndex_Object = MibTableColumn
prioSchedModePortIndex = _PrioSchedModePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 15, 1, 1),
    _PrioSchedModePortIndex_Type()
)
prioSchedModePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioSchedModePortIndex.setStatus("current")


class _PrioSchedModePort_Type(Integer32):
    """Custom type prioSchedModePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("strict", 2),
          ("strict-wrr", 4),
          ("wrr", 1))
    )


_PrioSchedModePort_Type.__name__ = "Integer32"
_PrioSchedModePort_Object = MibTableColumn
prioSchedModePort = _PrioSchedModePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 13, 15, 1, 2),
    _PrioSchedModePort_Type()
)
prioSchedModePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioSchedModePort.setStatus("current")
_TrapDestMgt_ObjectIdentity = ObjectIdentity
trapDestMgt = _TrapDestMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14)
)
_TrapVar_ObjectIdentity = ObjectIdentity
trapVar = _TrapVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2)
)


class _TrapIpFilterRejectMode_Type(Integer32):
    """Custom type trapIpFilterRejectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 2),
          ("telnet", 3),
          ("web", 1))
    )


_TrapIpFilterRejectMode_Type.__name__ = "Integer32"
_TrapIpFilterRejectMode_Object = MibScalar
trapIpFilterRejectMode = _TrapIpFilterRejectMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 6),
    _TrapIpFilterRejectMode_Type()
)
trapIpFilterRejectMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIpFilterRejectMode.setStatus("current")
_TrapIpFilterRejectIp_Type = IpAddress
_TrapIpFilterRejectIp_Object = MibScalar
trapIpFilterRejectIp = _TrapIpFilterRejectIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 7),
    _TrapIpFilterRejectIp_Type()
)
trapIpFilterRejectIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIpFilterRejectIp.setStatus("current")
_TrapVarMacAddr_Type = MacAddress
_TrapVarMacAddr_Object = MibScalar
trapVarMacAddr = _TrapVarMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 10),
    _TrapVarMacAddr_Type()
)
trapVarMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapVarMacAddr.setStatus("current")


class _TrapVarLoginUserName_Type(DisplayString):
    """Custom type trapVarLoginUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_TrapVarLoginUserName_Type.__name__ = "DisplayString"
_TrapVarLoginUserName_Object = MibScalar
trapVarLoginUserName = _TrapVarLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 11),
    _TrapVarLoginUserName_Type()
)
trapVarLoginUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapVarLoginUserName.setStatus("current")


class _TrapVarSessionType_Type(Integer32):
    """Custom type trapVarSessionType based on Integer32"""
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
        *(("console", 4),
          ("http", 6),
          ("https", 7),
          ("snmp", 2),
          ("ssh", 5),
          ("telnet", 3),
          ("web", 1))
    )


_TrapVarSessionType_Type.__name__ = "Integer32"
_TrapVarSessionType_Object = MibScalar
trapVarSessionType = _TrapVarSessionType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 12),
    _TrapVarSessionType_Type()
)
trapVarSessionType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapVarSessionType.setStatus("current")
_TrapVarLoginInetAddressType_Type = InetAddressType
_TrapVarLoginInetAddressType_Object = MibScalar
trapVarLoginInetAddressType = _TrapVarLoginInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 15),
    _TrapVarLoginInetAddressType_Type()
)
trapVarLoginInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapVarLoginInetAddressType.setStatus("current")
_TrapVarLoginInetAddress_Type = InetAddress
_TrapVarLoginInetAddress_Object = MibScalar
trapVarLoginInetAddress = _TrapVarLoginInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 16),
    _TrapVarLoginInetAddress_Type()
)
trapVarLoginInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapVarLoginInetAddress.setStatus("current")
_TrapIpFilterRejectInetAddressType_Type = InetAddressType
_TrapIpFilterRejectInetAddressType_Object = MibScalar
trapIpFilterRejectInetAddressType = _TrapIpFilterRejectInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 17),
    _TrapIpFilterRejectInetAddressType_Type()
)
trapIpFilterRejectInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIpFilterRejectInetAddressType.setStatus("current")
_TrapIpFilterRejectInetAddress_Type = InetAddress
_TrapIpFilterRejectInetAddress_Object = MibScalar
trapIpFilterRejectInetAddress = _TrapIpFilterRejectInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 18),
    _TrapIpFilterRejectInetAddress_Type()
)
trapIpFilterRejectInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIpFilterRejectInetAddress.setStatus("current")


class _TrapAutoUpgradeResult_Type(Integer32):
    """Custom type trapAutoUpgradeResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("succeeded", 1))
    )


_TrapAutoUpgradeResult_Type.__name__ = "Integer32"
_TrapAutoUpgradeResult_Object = MibScalar
trapAutoUpgradeResult = _TrapAutoUpgradeResult_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 22),
    _TrapAutoUpgradeResult_Type()
)
trapAutoUpgradeResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAutoUpgradeResult.setStatus("current")


class _TrapAutoUpgradeNewVer_Type(DisplayString):
    """Custom type trapAutoUpgradeNewVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TrapAutoUpgradeNewVer_Type.__name__ = "DisplayString"
_TrapAutoUpgradeNewVer_Object = MibScalar
trapAutoUpgradeNewVer = _TrapAutoUpgradeNewVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 23),
    _TrapAutoUpgradeNewVer_Type()
)
trapAutoUpgradeNewVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAutoUpgradeNewVer.setStatus("current")
_TrapIfIndex_Type = Unsigned32
_TrapIfIndex_Object = MibScalar
trapIfIndex = _TrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 30),
    _TrapIfIndex_Type()
)
trapIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIfIndex.setStatus("current")
_TrapVlanId_Type = Unsigned32
_TrapVlanId_Object = MibScalar
trapVlanId = _TrapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 31),
    _TrapVlanId_Type()
)
trapVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapVlanId.setStatus("current")
_TrapDhcpClientPortIfIndex_Type = Integer32
_TrapDhcpClientPortIfIndex_Object = MibScalar
trapDhcpClientPortIfIndex = _TrapDhcpClientPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 62),
    _TrapDhcpClientPortIfIndex_Type()
)
trapDhcpClientPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDhcpClientPortIfIndex.setStatus("current")
_TrapDhcpServerIpAddress_Type = DisplayString
_TrapDhcpServerIpAddress_Object = MibScalar
trapDhcpServerIpAddress = _TrapDhcpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 63),
    _TrapDhcpServerIpAddress_Type()
)
trapDhcpServerIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDhcpServerIpAddress.setStatus("current")
_TrapSfpThresholdAlarmWarnIfIndex_Type = Integer32
_TrapSfpThresholdAlarmWarnIfIndex_Object = MibScalar
trapSfpThresholdAlarmWarnIfIndex = _TrapSfpThresholdAlarmWarnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 64),
    _TrapSfpThresholdAlarmWarnIfIndex_Type()
)
trapSfpThresholdAlarmWarnIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSfpThresholdAlarmWarnIfIndex.setStatus("current")


class _TrapSfpThresholdAlarmWarnType_Type(Integer32):
    """Custom type trapSfpThresholdAlarmWarnType based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("currentAlarmWarnCease", 25),
          ("currentHighAlarm", 17),
          ("currentHighWarning", 19),
          ("currentLowAlarm", 18),
          ("currentLowWarning", 20),
          ("rxPowerAlarmWarnCease", 21),
          ("rxPowerHighAlarm", 1),
          ("rxPowerHighWarning", 3),
          ("rxPowerLowAlarm", 2),
          ("rxPowerLowWarning", 4),
          ("temperatureAlarmWarnCease", 23),
          ("temperatureHighAlarm", 9),
          ("temperatureHighWarning", 11),
          ("temperatureLowAlarm", 10),
          ("temperatureLowWarning", 12),
          ("txPowerAlarmWarnCease", 22),
          ("txPowerHighAlarm", 5),
          ("txPowerHighWarning", 7),
          ("txPowerLowAlarm", 6),
          ("txPowerLowWarning", 8),
          ("voltageAlarmWarnCease", 24),
          ("voltageHighAlarm", 13),
          ("voltageHighWarning", 15),
          ("voltageLowAlarm", 14),
          ("voltageLowWarning", 16))
    )


_TrapSfpThresholdAlarmWarnType_Type.__name__ = "Integer32"
_TrapSfpThresholdAlarmWarnType_Object = MibScalar
trapSfpThresholdAlarmWarnType = _TrapSfpThresholdAlarmWarnType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 65),
    _TrapSfpThresholdAlarmWarnType_Type()
)
trapSfpThresholdAlarmWarnType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSfpThresholdAlarmWarnType.setStatus("current")


class _TrapUdldPortShutdownReason_Type(Integer32):
    """Custom type trapUdldPortShutdownReason based on Integer32"""
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
        *(("aggressiveModeFailure", 4),
          ("mismatchWithNeighbor", 2),
          ("transmitToReceiveLoop", 3),
          ("unidirectionalLink", 1))
    )


_TrapUdldPortShutdownReason_Type.__name__ = "Integer32"
_TrapUdldPortShutdownReason_Object = MibScalar
trapUdldPortShutdownReason = _TrapUdldPortShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 66),
    _TrapUdldPortShutdownReason_Type()
)
trapUdldPortShutdownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapUdldPortShutdownReason.setStatus("current")
_TrapDhcpServerMacAddress_Type = MacAddress
_TrapDhcpServerMacAddress_Object = MibScalar
trapDhcpServerMacAddress = _TrapDhcpServerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 67),
    _TrapDhcpServerMacAddress_Type()
)
trapDhcpServerMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDhcpServerMacAddress.setStatus("current")


class _TrapMacNotifyAction_Type(Integer32):
    """Custom type trapMacNotifyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_TrapMacNotifyAction_Type.__name__ = "Integer32"
_TrapMacNotifyAction_Object = MibScalar
trapMacNotifyAction = _TrapMacNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 14, 2, 68),
    _TrapMacNotifyAction_Type()
)
trapMacNotifyAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMacNotifyAction.setStatus("current")
_QosMgt_ObjectIdentity = ObjectIdentity
qosMgt = _QosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16)
)
_RateLimitMgt_ObjectIdentity = ObjectIdentity
rateLimitMgt = _RateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 1)
)
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("current")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 1, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "rlPortIndex"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("current")
_RlPortIndex_Type = InterfaceIndex
_RlPortIndex_Object = MibTableColumn
rlPortIndex = _RlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 1, 2, 1, 1),
    _RlPortIndex_Type()
)
rlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortIndex.setStatus("current")
_RlPortInputStatus_Type = EnabledStatus
_RlPortInputStatus_Object = MibTableColumn
rlPortInputStatus = _RlPortInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 1, 2, 1, 6),
    _RlPortInputStatus_Type()
)
rlPortInputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputStatus.setStatus("current")
_RlPortOutputStatus_Type = EnabledStatus
_RlPortOutputStatus_Object = MibTableColumn
rlPortOutputStatus = _RlPortOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 1, 2, 1, 7),
    _RlPortOutputStatus_Type()
)
rlPortOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputStatus.setStatus("current")
_RlPortInputLimitInKilo_Type = Integer32
_RlPortInputLimitInKilo_Object = MibTableColumn
rlPortInputLimitInKilo = _RlPortInputLimitInKilo_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 1, 2, 1, 10),
    _RlPortInputLimitInKilo_Type()
)
rlPortInputLimitInKilo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputLimitInKilo.setStatus("current")
_RlPortOutputLimitInKilo_Type = Integer32
_RlPortOutputLimitInKilo_Object = MibTableColumn
rlPortOutputLimitInKilo = _RlPortOutputLimitInKilo_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 1, 2, 1, 11),
    _RlPortOutputLimitInKilo_Type()
)
rlPortOutputLimitInKilo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputLimitInKilo.setStatus("current")
_RlPortLimitInKiloResolution_Type = Integer32
_RlPortLimitInKiloResolution_Object = MibTableColumn
rlPortLimitInKiloResolution = _RlPortLimitInKiloResolution_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 1, 2, 1, 12),
    _RlPortLimitInKiloResolution_Type()
)
rlPortLimitInKiloResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPortLimitInKiloResolution.setStatus("current")
_CosMgt_ObjectIdentity = ObjectIdentity
cosMgt = _CosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3)
)
_PrioIfClassificationModeTable_Object = MibTable
prioIfClassificationModeTable = _PrioIfClassificationModeTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 2)
)
if mibBuilder.loadTexts:
    prioIfClassificationModeTable.setStatus("current")
_PrioIfClassificationModeEntry_Object = MibTableRow
prioIfClassificationModeEntry = _PrioIfClassificationModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 2, 1)
)
prioIfClassificationModeEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "prioIfClassificationModeIf"),
)
if mibBuilder.loadTexts:
    prioIfClassificationModeEntry.setStatus("current")
_PrioIfClassificationModeIf_Type = InterfaceIndex
_PrioIfClassificationModeIf_Object = MibTableColumn
prioIfClassificationModeIf = _PrioIfClassificationModeIf_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 2, 1, 1),
    _PrioIfClassificationModeIf_Type()
)
prioIfClassificationModeIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIfClassificationModeIf.setStatus("current")


class _PrioIfClassificationModeStatus_Type(Integer32):
    """Custom type prioIfClassificationModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cos", 0),
          ("dscp", 2),
          ("ipPrecedence", 1))
    )


_PrioIfClassificationModeStatus_Type.__name__ = "Integer32"
_PrioIfClassificationModeStatus_Object = MibTableColumn
prioIfClassificationModeStatus = _PrioIfClassificationModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 2, 1, 2),
    _PrioIfClassificationModeStatus_Type()
)
prioIfClassificationModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIfClassificationModeStatus.setStatus("current")
_PrioCosToDscpTable_Object = MibTable
prioCosToDscpTable = _PrioCosToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 3)
)
if mibBuilder.loadTexts:
    prioCosToDscpTable.setStatus("current")
_PrioCosToDscpEntry_Object = MibTableRow
prioCosToDscpEntry = _PrioCosToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 3, 1)
)
prioCosToDscpEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "prioCosToDscpIfValue"),
    (0, "ECS2100-28PP-MIB", "prioCosToDscpCosValue"),
    (0, "ECS2100-28PP-MIB", "prioCosToDscpCFIValue"),
)
if mibBuilder.loadTexts:
    prioCosToDscpEntry.setStatus("current")
_PrioCosToDscpIfValue_Type = InterfaceIndex
_PrioCosToDscpIfValue_Object = MibTableColumn
prioCosToDscpIfValue = _PrioCosToDscpIfValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 3, 1, 1),
    _PrioCosToDscpIfValue_Type()
)
prioCosToDscpIfValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioCosToDscpIfValue.setStatus("current")


class _PrioCosToDscpCosValue_Type(Integer32):
    """Custom type prioCosToDscpCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioCosToDscpCosValue_Type.__name__ = "Integer32"
_PrioCosToDscpCosValue_Object = MibTableColumn
prioCosToDscpCosValue = _PrioCosToDscpCosValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 3, 1, 2),
    _PrioCosToDscpCosValue_Type()
)
prioCosToDscpCosValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioCosToDscpCosValue.setStatus("current")


class _PrioCosToDscpCFIValue_Type(Integer32):
    """Custom type prioCosToDscpCFIValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PrioCosToDscpCFIValue_Type.__name__ = "Integer32"
_PrioCosToDscpCFIValue_Object = MibTableColumn
prioCosToDscpCFIValue = _PrioCosToDscpCFIValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 3, 1, 3),
    _PrioCosToDscpCFIValue_Type()
)
prioCosToDscpCFIValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioCosToDscpCFIValue.setStatus("current")


class _PrioCosToDscpPhbValue_Type(Integer32):
    """Custom type prioCosToDscpPhbValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioCosToDscpPhbValue_Type.__name__ = "Integer32"
_PrioCosToDscpPhbValue_Object = MibTableColumn
prioCosToDscpPhbValue = _PrioCosToDscpPhbValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 3, 1, 5),
    _PrioCosToDscpPhbValue_Type()
)
prioCosToDscpPhbValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCosToDscpPhbValue.setStatus("current")
_PrioDscpToDscpTable_Object = MibTable
prioDscpToDscpTable = _PrioDscpToDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 5)
)
if mibBuilder.loadTexts:
    prioDscpToDscpTable.setStatus("current")
_PrioDscpToDscpEntry_Object = MibTableRow
prioDscpToDscpEntry = _PrioDscpToDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 5, 1)
)
prioDscpToDscpEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "prioDscpToDscpIfValue"),
    (0, "ECS2100-28PP-MIB", "prioDscpToDscpIngressDscpValue"),
)
if mibBuilder.loadTexts:
    prioDscpToDscpEntry.setStatus("current")
_PrioDscpToDscpIfValue_Type = InterfaceIndex
_PrioDscpToDscpIfValue_Object = MibTableColumn
prioDscpToDscpIfValue = _PrioDscpToDscpIfValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 5, 1, 1),
    _PrioDscpToDscpIfValue_Type()
)
prioDscpToDscpIfValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioDscpToDscpIfValue.setStatus("current")


class _PrioDscpToDscpIngressDscpValue_Type(Integer32):
    """Custom type prioDscpToDscpIngressDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PrioDscpToDscpIngressDscpValue_Type.__name__ = "Integer32"
_PrioDscpToDscpIngressDscpValue_Object = MibTableColumn
prioDscpToDscpIngressDscpValue = _PrioDscpToDscpIngressDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 5, 1, 2),
    _PrioDscpToDscpIngressDscpValue_Type()
)
prioDscpToDscpIngressDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioDscpToDscpIngressDscpValue.setStatus("current")


class _PrioDscpToDscpPhbValue_Type(Integer32):
    """Custom type prioDscpToDscpPhbValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioDscpToDscpPhbValue_Type.__name__ = "Integer32"
_PrioDscpToDscpPhbValue_Object = MibTableColumn
prioDscpToDscpPhbValue = _PrioDscpToDscpPhbValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 3, 5, 1, 4),
    _PrioDscpToDscpPhbValue_Type()
)
prioDscpToDscpPhbValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioDscpToDscpPhbValue.setStatus("current")
_DiffServMgt_ObjectIdentity = ObjectIdentity
diffServMgt = _DiffServMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4)
)
_DiffServPolicyMapTable_Object = MibTable
diffServPolicyMapTable = _DiffServPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 10)
)
if mibBuilder.loadTexts:
    diffServPolicyMapTable.setStatus("current")
_DiffServPolicyMapEntry_Object = MibTableRow
diffServPolicyMapEntry = _DiffServPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 10, 1)
)
diffServPolicyMapEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    diffServPolicyMapEntry.setStatus("current")


class _DiffServPolicyMapIndex_Type(Integer32):
    """Custom type diffServPolicyMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DiffServPolicyMapIndex_Type.__name__ = "Integer32"
_DiffServPolicyMapIndex_Object = MibTableColumn
diffServPolicyMapIndex = _DiffServPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 10, 1, 1),
    _DiffServPolicyMapIndex_Type()
)
diffServPolicyMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPolicyMapIndex.setStatus("current")


class _DiffServPolicyMapName_Type(DisplayString):
    """Custom type diffServPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DiffServPolicyMapName_Type.__name__ = "DisplayString"
_DiffServPolicyMapName_Object = MibTableColumn
diffServPolicyMapName = _DiffServPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 10, 1, 2),
    _DiffServPolicyMapName_Type()
)
diffServPolicyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapName.setStatus("current")


class _DiffServPolicyMapDescription_Type(DisplayString):
    """Custom type diffServPolicyMapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiffServPolicyMapDescription_Type.__name__ = "DisplayString"
_DiffServPolicyMapDescription_Object = MibTableColumn
diffServPolicyMapDescription = _DiffServPolicyMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 10, 1, 3),
    _DiffServPolicyMapDescription_Type()
)
diffServPolicyMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapDescription.setStatus("current")


class _DiffServPolicyMapElementIndexList_Type(OctetString):
    """Custom type diffServPolicyMapElementIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DiffServPolicyMapElementIndexList_Type.__name__ = "OctetString"
_DiffServPolicyMapElementIndexList_Object = MibTableColumn
diffServPolicyMapElementIndexList = _DiffServPolicyMapElementIndexList_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 10, 1, 4),
    _DiffServPolicyMapElementIndexList_Type()
)
diffServPolicyMapElementIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServPolicyMapElementIndexList.setStatus("current")
_DiffServPolicyMapStatus_Type = RowStatus
_DiffServPolicyMapStatus_Object = MibTableColumn
diffServPolicyMapStatus = _DiffServPolicyMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 10, 1, 5),
    _DiffServPolicyMapStatus_Type()
)
diffServPolicyMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapStatus.setStatus("current")
_DiffServPolicyMapAttachCtl_ObjectIdentity = ObjectIdentity
diffServPolicyMapAttachCtl = _DiffServPolicyMapAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 11)
)
_DiffServPolicyMapAttachCtlIndex_Type = Integer32
_DiffServPolicyMapAttachCtlIndex_Object = MibScalar
diffServPolicyMapAttachCtlIndex = _DiffServPolicyMapAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 11, 1),
    _DiffServPolicyMapAttachCtlIndex_Type()
)
diffServPolicyMapAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlIndex.setStatus("current")
_DiffServPolicyMapAttachCtlElementIndex_Type = Integer32
_DiffServPolicyMapAttachCtlElementIndex_Object = MibScalar
diffServPolicyMapAttachCtlElementIndex = _DiffServPolicyMapAttachCtlElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 11, 2),
    _DiffServPolicyMapAttachCtlElementIndex_Type()
)
diffServPolicyMapAttachCtlElementIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlElementIndex.setStatus("current")


class _DiffServPolicyMapAttachCtlAction_Type(Integer32):
    """Custom type diffServPolicyMapAttachCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attach", 2),
          ("detach", 3),
          ("noAction", 1))
    )


_DiffServPolicyMapAttachCtlAction_Type.__name__ = "Integer32"
_DiffServPolicyMapAttachCtlAction_Object = MibScalar
diffServPolicyMapAttachCtlAction = _DiffServPolicyMapAttachCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 11, 3),
    _DiffServPolicyMapAttachCtlAction_Type()
)
diffServPolicyMapAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlAction.setStatus("current")
_DiffServPolicyMapElementTable_Object = MibTable
diffServPolicyMapElementTable = _DiffServPolicyMapElementTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 12)
)
if mibBuilder.loadTexts:
    diffServPolicyMapElementTable.setStatus("current")
_DiffServPolicyMapElementEntry_Object = MibTableRow
diffServPolicyMapElementEntry = _DiffServPolicyMapElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 12, 1)
)
diffServPolicyMapElementEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServPolicyMapElementIndex"),
)
if mibBuilder.loadTexts:
    diffServPolicyMapElementEntry.setStatus("current")


class _DiffServPolicyMapElementIndex_Type(Integer32):
    """Custom type diffServPolicyMapElementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DiffServPolicyMapElementIndex_Type.__name__ = "Integer32"
_DiffServPolicyMapElementIndex_Object = MibTableColumn
diffServPolicyMapElementIndex = _DiffServPolicyMapElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 12, 1, 1),
    _DiffServPolicyMapElementIndex_Type()
)
diffServPolicyMapElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPolicyMapElementIndex.setStatus("current")


class _DiffServPolicyMapElementClassMapIndex_Type(Integer32):
    """Custom type diffServPolicyMapElementClassMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DiffServPolicyMapElementClassMapIndex_Type.__name__ = "Integer32"
_DiffServPolicyMapElementClassMapIndex_Object = MibTableColumn
diffServPolicyMapElementClassMapIndex = _DiffServPolicyMapElementClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 12, 1, 2),
    _DiffServPolicyMapElementClassMapIndex_Type()
)
diffServPolicyMapElementClassMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementClassMapIndex.setStatus("current")
_DiffServPolicyMapElementMeterIndex_Type = Integer32
_DiffServPolicyMapElementMeterIndex_Object = MibTableColumn
diffServPolicyMapElementMeterIndex = _DiffServPolicyMapElementMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 12, 1, 3),
    _DiffServPolicyMapElementMeterIndex_Type()
)
diffServPolicyMapElementMeterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementMeterIndex.setStatus("current")


class _DiffServPolicyMapElementActionIndex_Type(Integer32):
    """Custom type diffServPolicyMapElementActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DiffServPolicyMapElementActionIndex_Type.__name__ = "Integer32"
_DiffServPolicyMapElementActionIndex_Object = MibTableColumn
diffServPolicyMapElementActionIndex = _DiffServPolicyMapElementActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 12, 1, 4),
    _DiffServPolicyMapElementActionIndex_Type()
)
diffServPolicyMapElementActionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementActionIndex.setStatus("current")
_DiffServPolicyMapElementStatus_Type = RowStatus
_DiffServPolicyMapElementStatus_Object = MibTableColumn
diffServPolicyMapElementStatus = _DiffServPolicyMapElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 12, 1, 5),
    _DiffServPolicyMapElementStatus_Type()
)
diffServPolicyMapElementStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementStatus.setStatus("current")
_DiffServClassMapTable_Object = MibTable
diffServClassMapTable = _DiffServClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 13)
)
if mibBuilder.loadTexts:
    diffServClassMapTable.setStatus("current")
_DiffServClassMapEntry_Object = MibTableRow
diffServClassMapEntry = _DiffServClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 13, 1)
)
diffServClassMapEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServClassMapIndex"),
)
if mibBuilder.loadTexts:
    diffServClassMapEntry.setStatus("current")


class _DiffServClassMapIndex_Type(Integer32):
    """Custom type diffServClassMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DiffServClassMapIndex_Type.__name__ = "Integer32"
_DiffServClassMapIndex_Object = MibTableColumn
diffServClassMapIndex = _DiffServClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 13, 1, 1),
    _DiffServClassMapIndex_Type()
)
diffServClassMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServClassMapIndex.setStatus("current")


class _DiffServClassMapName_Type(DisplayString):
    """Custom type diffServClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServClassMapName_Type.__name__ = "DisplayString"
_DiffServClassMapName_Object = MibTableColumn
diffServClassMapName = _DiffServClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 13, 1, 2),
    _DiffServClassMapName_Type()
)
diffServClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapName.setStatus("current")


class _DiffServClassMapDescription_Type(DisplayString):
    """Custom type diffServClassMapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiffServClassMapDescription_Type.__name__ = "DisplayString"
_DiffServClassMapDescription_Object = MibTableColumn
diffServClassMapDescription = _DiffServClassMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 13, 1, 3),
    _DiffServClassMapDescription_Type()
)
diffServClassMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapDescription.setStatus("current")


class _DiffServClassMapMatchType_Type(Integer32):
    """Custom type diffServClassMapMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchAll", 2),
          ("matchAny", 1))
    )


_DiffServClassMapMatchType_Type.__name__ = "Integer32"
_DiffServClassMapMatchType_Object = MibTableColumn
diffServClassMapMatchType = _DiffServClassMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 13, 1, 4),
    _DiffServClassMapMatchType_Type()
)
diffServClassMapMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapMatchType.setStatus("current")


class _DiffServClassMapElementIndexTypeList_Type(OctetString):
    """Custom type diffServClassMapElementIndexTypeList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiffServClassMapElementIndexTypeList_Type.__name__ = "OctetString"
_DiffServClassMapElementIndexTypeList_Object = MibTableColumn
diffServClassMapElementIndexTypeList = _DiffServClassMapElementIndexTypeList_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 13, 1, 5),
    _DiffServClassMapElementIndexTypeList_Type()
)
diffServClassMapElementIndexTypeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClassMapElementIndexTypeList.setStatus("current")


class _DiffServClassMapElementIndexList_Type(OctetString):
    """Custom type diffServClassMapElementIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiffServClassMapElementIndexList_Type.__name__ = "OctetString"
_DiffServClassMapElementIndexList_Object = MibTableColumn
diffServClassMapElementIndexList = _DiffServClassMapElementIndexList_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 13, 1, 6),
    _DiffServClassMapElementIndexList_Type()
)
diffServClassMapElementIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClassMapElementIndexList.setStatus("current")
_DiffServClassMapStatus_Type = RowStatus
_DiffServClassMapStatus_Object = MibTableColumn
diffServClassMapStatus = _DiffServClassMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 13, 1, 7),
    _DiffServClassMapStatus_Type()
)
diffServClassMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapStatus.setStatus("current")
_DiffServClassMapAttachCtl_ObjectIdentity = ObjectIdentity
diffServClassMapAttachCtl = _DiffServClassMapAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 14)
)
_DiffServClassMapAttachCtlIndex_Type = Integer32
_DiffServClassMapAttachCtlIndex_Object = MibScalar
diffServClassMapAttachCtlIndex = _DiffServClassMapAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 14, 1),
    _DiffServClassMapAttachCtlIndex_Type()
)
diffServClassMapAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlIndex.setStatus("current")


class _DiffServClassMapAttachCtlElementIndexType_Type(Integer32):
    """Custom type diffServClassMapAttachCtlElementIndexType based on Integer32"""
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
        *(("acl", 3),
          ("ipAce", 2),
          ("ipv6Ace", 4),
          ("macAce", 1))
    )


_DiffServClassMapAttachCtlElementIndexType_Type.__name__ = "Integer32"
_DiffServClassMapAttachCtlElementIndexType_Object = MibScalar
diffServClassMapAttachCtlElementIndexType = _DiffServClassMapAttachCtlElementIndexType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 14, 2),
    _DiffServClassMapAttachCtlElementIndexType_Type()
)
diffServClassMapAttachCtlElementIndexType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlElementIndexType.setStatus("current")
_DiffServClassMapAttachCtlElementIndex_Type = Integer32
_DiffServClassMapAttachCtlElementIndex_Object = MibScalar
diffServClassMapAttachCtlElementIndex = _DiffServClassMapAttachCtlElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 14, 3),
    _DiffServClassMapAttachCtlElementIndex_Type()
)
diffServClassMapAttachCtlElementIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlElementIndex.setStatus("current")


class _DiffServClassMapAttachCtlAction_Type(Integer32):
    """Custom type diffServClassMapAttachCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attach", 2),
          ("detach", 3),
          ("noAction", 1))
    )


_DiffServClassMapAttachCtlAction_Type.__name__ = "Integer32"
_DiffServClassMapAttachCtlAction_Object = MibScalar
diffServClassMapAttachCtlAction = _DiffServClassMapAttachCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 14, 4),
    _DiffServClassMapAttachCtlAction_Type()
)
diffServClassMapAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlAction.setStatus("current")
_DiffServAclTable_Object = MibTable
diffServAclTable = _DiffServAclTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 15)
)
if mibBuilder.loadTexts:
    diffServAclTable.setStatus("current")
_DiffServAclEntry_Object = MibTableRow
diffServAclEntry = _DiffServAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 15, 1)
)
diffServAclEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServAclIndex"),
)
if mibBuilder.loadTexts:
    diffServAclEntry.setStatus("current")


class _DiffServAclIndex_Type(Integer32):
    """Custom type diffServAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DiffServAclIndex_Type.__name__ = "Integer32"
_DiffServAclIndex_Object = MibTableColumn
diffServAclIndex = _DiffServAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 15, 1, 1),
    _DiffServAclIndex_Type()
)
diffServAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServAclIndex.setStatus("current")


class _DiffServAclName_Type(DisplayString):
    """Custom type diffServAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServAclName_Type.__name__ = "DisplayString"
_DiffServAclName_Object = MibTableColumn
diffServAclName = _DiffServAclName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 15, 1, 2),
    _DiffServAclName_Type()
)
diffServAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclName.setStatus("current")


class _DiffServAclType_Type(Integer32):
    """Custom type diffServAclType based on Integer32"""
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
        *(("arp", 6),
          ("ipextended", 3),
          ("ipstandard", 2),
          ("ipv6extended", 5),
          ("ipv6standard", 4),
          ("mac", 1))
    )


_DiffServAclType_Type.__name__ = "Integer32"
_DiffServAclType_Object = MibTableColumn
diffServAclType = _DiffServAclType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 15, 1, 3),
    _DiffServAclType_Type()
)
diffServAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclType.setStatus("current")


class _DiffServAclAceIndexList_Type(OctetString):
    """Custom type diffServAclAceIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiffServAclAceIndexList_Type.__name__ = "OctetString"
_DiffServAclAceIndexList_Object = MibTableColumn
diffServAclAceIndexList = _DiffServAclAceIndexList_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 15, 1, 4),
    _DiffServAclAceIndexList_Type()
)
diffServAclAceIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAclAceIndexList.setStatus("current")
_DiffServAclStatus_Type = RowStatus
_DiffServAclStatus_Object = MibTableColumn
diffServAclStatus = _DiffServAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 15, 1, 5),
    _DiffServAclStatus_Type()
)
diffServAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclStatus.setStatus("current")
_DiffServAclAttachCtl_ObjectIdentity = ObjectIdentity
diffServAclAttachCtl = _DiffServAclAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 16)
)
_DiffServAclAttachCtlIndex_Type = Integer32
_DiffServAclAttachCtlIndex_Object = MibScalar
diffServAclAttachCtlIndex = _DiffServAclAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 16, 1),
    _DiffServAclAttachCtlIndex_Type()
)
diffServAclAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlIndex.setStatus("current")


class _DiffServAclAttachCtlAceType_Type(Integer32):
    """Custom type diffServAclAttachCtlAceType based on Integer32"""
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
        *(("arpAce", 4),
          ("ipAce", 2),
          ("ipv6Ace", 3),
          ("macAce", 1))
    )


_DiffServAclAttachCtlAceType_Type.__name__ = "Integer32"
_DiffServAclAttachCtlAceType_Object = MibScalar
diffServAclAttachCtlAceType = _DiffServAclAttachCtlAceType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 16, 2),
    _DiffServAclAttachCtlAceType_Type()
)
diffServAclAttachCtlAceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAceType.setStatus("current")
_DiffServAclAttachCtlAceIndex_Type = Integer32
_DiffServAclAttachCtlAceIndex_Object = MibScalar
diffServAclAttachCtlAceIndex = _DiffServAclAttachCtlAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 16, 3),
    _DiffServAclAttachCtlAceIndex_Type()
)
diffServAclAttachCtlAceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAceIndex.setStatus("current")


class _DiffServAclAttachCtlAction_Type(Integer32):
    """Custom type diffServAclAttachCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attach", 2),
          ("detach", 3),
          ("noAction", 1))
    )


_DiffServAclAttachCtlAction_Type.__name__ = "Integer32"
_DiffServAclAttachCtlAction_Object = MibScalar
diffServAclAttachCtlAction = _DiffServAclAttachCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 16, 4),
    _DiffServAclAttachCtlAction_Type()
)
diffServAclAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAction.setStatus("current")
_DiffServIpAceTable_Object = MibTable
diffServIpAceTable = _DiffServIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17)
)
if mibBuilder.loadTexts:
    diffServIpAceTable.setStatus("current")
_DiffServIpAceEntry_Object = MibTableRow
diffServIpAceEntry = _DiffServIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1)
)
diffServIpAceEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServIpAceIndex"),
)
if mibBuilder.loadTexts:
    diffServIpAceEntry.setStatus("current")


class _DiffServIpAceIndex_Type(Integer32):
    """Custom type diffServIpAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DiffServIpAceIndex_Type.__name__ = "Integer32"
_DiffServIpAceIndex_Object = MibTableColumn
diffServIpAceIndex = _DiffServIpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 1),
    _DiffServIpAceIndex_Type()
)
diffServIpAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServIpAceIndex.setStatus("current")


class _DiffServIpAceType_Type(Integer32):
    """Custom type diffServIpAceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("standard", 1))
    )


_DiffServIpAceType_Type.__name__ = "Integer32"
_DiffServIpAceType_Object = MibTableColumn
diffServIpAceType = _DiffServIpAceType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 2),
    _DiffServIpAceType_Type()
)
diffServIpAceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceType.setStatus("current")


class _DiffServIpAceAccess_Type(Integer32):
    """Custom type diffServIpAceAccess based on Integer32"""
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


_DiffServIpAceAccess_Type.__name__ = "Integer32"
_DiffServIpAceAccess_Object = MibTableColumn
diffServIpAceAccess = _DiffServIpAceAccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 3),
    _DiffServIpAceAccess_Type()
)
diffServIpAceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceAccess.setStatus("current")
_DiffServIpAceSourceIpAddr_Type = IpAddress
_DiffServIpAceSourceIpAddr_Object = MibTableColumn
diffServIpAceSourceIpAddr = _DiffServIpAceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 4),
    _DiffServIpAceSourceIpAddr_Type()
)
diffServIpAceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourceIpAddr.setStatus("current")
_DiffServIpAceSourceIpAddrBitmask_Type = IpAddress
_DiffServIpAceSourceIpAddrBitmask_Object = MibTableColumn
diffServIpAceSourceIpAddrBitmask = _DiffServIpAceSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 5),
    _DiffServIpAceSourceIpAddrBitmask_Type()
)
diffServIpAceSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourceIpAddrBitmask.setStatus("current")
_DiffServIpAceDestIpAddr_Type = IpAddress
_DiffServIpAceDestIpAddr_Object = MibTableColumn
diffServIpAceDestIpAddr = _DiffServIpAceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 6),
    _DiffServIpAceDestIpAddr_Type()
)
diffServIpAceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestIpAddr.setStatus("current")
_DiffServIpAceDestIpAddrBitmask_Type = IpAddress
_DiffServIpAceDestIpAddrBitmask_Object = MibTableColumn
diffServIpAceDestIpAddrBitmask = _DiffServIpAceDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 7),
    _DiffServIpAceDestIpAddrBitmask_Type()
)
diffServIpAceDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestIpAddrBitmask.setStatus("current")


class _DiffServIpAceProtocol_Type(Integer32):
    """Custom type diffServIpAceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_DiffServIpAceProtocol_Type.__name__ = "Integer32"
_DiffServIpAceProtocol_Object = MibTableColumn
diffServIpAceProtocol = _DiffServIpAceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 8),
    _DiffServIpAceProtocol_Type()
)
diffServIpAceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceProtocol.setStatus("current")


class _DiffServIpAcePrec_Type(Integer32):
    """Custom type diffServIpAcePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DiffServIpAcePrec_Type.__name__ = "Integer32"
_DiffServIpAcePrec_Object = MibTableColumn
diffServIpAcePrec = _DiffServIpAcePrec_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 9),
    _DiffServIpAcePrec_Type()
)
diffServIpAcePrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAcePrec.setStatus("current")


class _DiffServIpAceDscp_Type(Integer32):
    """Custom type diffServIpAceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DiffServIpAceDscp_Type.__name__ = "Integer32"
_DiffServIpAceDscp_Object = MibTableColumn
diffServIpAceDscp = _DiffServIpAceDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 11),
    _DiffServIpAceDscp_Type()
)
diffServIpAceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDscp.setStatus("current")


class _DiffServIpAceSourcePortOp_Type(Integer32):
    """Custom type diffServIpAceSourcePortOp based on Integer32"""
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


_DiffServIpAceSourcePortOp_Type.__name__ = "Integer32"
_DiffServIpAceSourcePortOp_Object = MibTableColumn
diffServIpAceSourcePortOp = _DiffServIpAceSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 12),
    _DiffServIpAceSourcePortOp_Type()
)
diffServIpAceSourcePortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourcePortOp.setStatus("current")


class _DiffServIpAceMinSourcePort_Type(Integer32):
    """Custom type diffServIpAceMinSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceMinSourcePort_Type.__name__ = "Integer32"
_DiffServIpAceMinSourcePort_Object = MibTableColumn
diffServIpAceMinSourcePort = _DiffServIpAceMinSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 13),
    _DiffServIpAceMinSourcePort_Type()
)
diffServIpAceMinSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceMinSourcePort.setStatus("current")


class _DiffServIpAceSourcePortBitmask_Type(Integer32):
    """Custom type diffServIpAceSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceSourcePortBitmask_Type.__name__ = "Integer32"
_DiffServIpAceSourcePortBitmask_Object = MibTableColumn
diffServIpAceSourcePortBitmask = _DiffServIpAceSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 15),
    _DiffServIpAceSourcePortBitmask_Type()
)
diffServIpAceSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourcePortBitmask.setStatus("current")


class _DiffServIpAceDestPortOp_Type(Integer32):
    """Custom type diffServIpAceDestPortOp based on Integer32"""
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


_DiffServIpAceDestPortOp_Type.__name__ = "Integer32"
_DiffServIpAceDestPortOp_Object = MibTableColumn
diffServIpAceDestPortOp = _DiffServIpAceDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 16),
    _DiffServIpAceDestPortOp_Type()
)
diffServIpAceDestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestPortOp.setStatus("current")


class _DiffServIpAceMinDestPort_Type(Integer32):
    """Custom type diffServIpAceMinDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceMinDestPort_Type.__name__ = "Integer32"
_DiffServIpAceMinDestPort_Object = MibTableColumn
diffServIpAceMinDestPort = _DiffServIpAceMinDestPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 17),
    _DiffServIpAceMinDestPort_Type()
)
diffServIpAceMinDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceMinDestPort.setStatus("current")


class _DiffServIpAceDestPortBitmask_Type(Integer32):
    """Custom type diffServIpAceDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceDestPortBitmask_Type.__name__ = "Integer32"
_DiffServIpAceDestPortBitmask_Object = MibTableColumn
diffServIpAceDestPortBitmask = _DiffServIpAceDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 19),
    _DiffServIpAceDestPortBitmask_Type()
)
diffServIpAceDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestPortBitmask.setStatus("current")


class _DiffServIpAceControlCode_Type(Integer32):
    """Custom type diffServIpAceControlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServIpAceControlCode_Type.__name__ = "Integer32"
_DiffServIpAceControlCode_Object = MibTableColumn
diffServIpAceControlCode = _DiffServIpAceControlCode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 20),
    _DiffServIpAceControlCode_Type()
)
diffServIpAceControlCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceControlCode.setStatus("current")


class _DiffServIpAceControlCodeBitmask_Type(Integer32):
    """Custom type diffServIpAceControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServIpAceControlCodeBitmask_Type.__name__ = "Integer32"
_DiffServIpAceControlCodeBitmask_Object = MibTableColumn
diffServIpAceControlCodeBitmask = _DiffServIpAceControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 21),
    _DiffServIpAceControlCodeBitmask_Type()
)
diffServIpAceControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceControlCodeBitmask.setStatus("current")
_DiffServIpAceStatus_Type = RowStatus
_DiffServIpAceStatus_Object = MibTableColumn
diffServIpAceStatus = _DiffServIpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 17, 1, 22),
    _DiffServIpAceStatus_Type()
)
diffServIpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceStatus.setStatus("current")
_DiffServMacAceTable_Object = MibTable
diffServMacAceTable = _DiffServMacAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18)
)
if mibBuilder.loadTexts:
    diffServMacAceTable.setStatus("current")
_DiffServMacAceEntry_Object = MibTableRow
diffServMacAceEntry = _DiffServMacAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1)
)
diffServMacAceEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServMacAceIndex"),
)
if mibBuilder.loadTexts:
    diffServMacAceEntry.setStatus("current")


class _DiffServMacAceIndex_Type(Integer32):
    """Custom type diffServMacAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DiffServMacAceIndex_Type.__name__ = "Integer32"
_DiffServMacAceIndex_Object = MibTableColumn
diffServMacAceIndex = _DiffServMacAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 1),
    _DiffServMacAceIndex_Type()
)
diffServMacAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMacAceIndex.setStatus("current")


class _DiffServMacAceAccess_Type(Integer32):
    """Custom type diffServMacAceAccess based on Integer32"""
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


_DiffServMacAceAccess_Type.__name__ = "Integer32"
_DiffServMacAceAccess_Object = MibTableColumn
diffServMacAceAccess = _DiffServMacAceAccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 2),
    _DiffServMacAceAccess_Type()
)
diffServMacAceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceAccess.setStatus("current")


class _DiffServMacAcePktformat_Type(Integer32):
    """Custom type diffServMacAcePktformat based on Integer32"""
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


_DiffServMacAcePktformat_Type.__name__ = "Integer32"
_DiffServMacAcePktformat_Object = MibTableColumn
diffServMacAcePktformat = _DiffServMacAcePktformat_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 3),
    _DiffServMacAcePktformat_Type()
)
diffServMacAcePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAcePktformat.setStatus("current")
_DiffServMacAceSourceMacAddr_Type = MacAddress
_DiffServMacAceSourceMacAddr_Object = MibTableColumn
diffServMacAceSourceMacAddr = _DiffServMacAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 4),
    _DiffServMacAceSourceMacAddr_Type()
)
diffServMacAceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceSourceMacAddr.setStatus("current")
_DiffServMacAceSourceMacAddrBitmask_Type = MacAddress
_DiffServMacAceSourceMacAddrBitmask_Object = MibTableColumn
diffServMacAceSourceMacAddrBitmask = _DiffServMacAceSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 5),
    _DiffServMacAceSourceMacAddrBitmask_Type()
)
diffServMacAceSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceSourceMacAddrBitmask.setStatus("current")
_DiffServMacAceDestMacAddr_Type = MacAddress
_DiffServMacAceDestMacAddr_Object = MibTableColumn
diffServMacAceDestMacAddr = _DiffServMacAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 6),
    _DiffServMacAceDestMacAddr_Type()
)
diffServMacAceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceDestMacAddr.setStatus("current")
_DiffServMacAceDestMacAddrBitmask_Type = MacAddress
_DiffServMacAceDestMacAddrBitmask_Object = MibTableColumn
diffServMacAceDestMacAddrBitmask = _DiffServMacAceDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 7),
    _DiffServMacAceDestMacAddrBitmask_Type()
)
diffServMacAceDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceDestMacAddrBitmask.setStatus("current")


class _DiffServMacAceVidOp_Type(Integer32):
    """Custom type diffServMacAceVidOp based on Integer32"""
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


_DiffServMacAceVidOp_Type.__name__ = "Integer32"
_DiffServMacAceVidOp_Object = MibTableColumn
diffServMacAceVidOp = _DiffServMacAceVidOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 8),
    _DiffServMacAceVidOp_Type()
)
diffServMacAceVidOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceVidOp.setStatus("current")


class _DiffServMacAceMinVid_Type(Integer32):
    """Custom type diffServMacAceMinVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DiffServMacAceMinVid_Type.__name__ = "Integer32"
_DiffServMacAceMinVid_Object = MibTableColumn
diffServMacAceMinVid = _DiffServMacAceMinVid_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 9),
    _DiffServMacAceMinVid_Type()
)
diffServMacAceMinVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinVid.setStatus("current")


class _DiffServMacAceVidBitmask_Type(Integer32):
    """Custom type diffServMacAceVidBitmask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_DiffServMacAceVidBitmask_Type.__name__ = "Integer32"
_DiffServMacAceVidBitmask_Object = MibTableColumn
diffServMacAceVidBitmask = _DiffServMacAceVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 10),
    _DiffServMacAceVidBitmask_Type()
)
diffServMacAceVidBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceVidBitmask.setStatus("current")


class _DiffServMacAceEtherTypeOp_Type(Integer32):
    """Custom type diffServMacAceEtherTypeOp based on Integer32"""
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


_DiffServMacAceEtherTypeOp_Type.__name__ = "Integer32"
_DiffServMacAceEtherTypeOp_Object = MibTableColumn
diffServMacAceEtherTypeOp = _DiffServMacAceEtherTypeOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 12),
    _DiffServMacAceEtherTypeOp_Type()
)
diffServMacAceEtherTypeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceEtherTypeOp.setStatus("current")


class _DiffServMacAceEtherTypeBitmask_Type(Integer32):
    """Custom type diffServMacAceEtherTypeBitmask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServMacAceEtherTypeBitmask_Type.__name__ = "Integer32"
_DiffServMacAceEtherTypeBitmask_Object = MibTableColumn
diffServMacAceEtherTypeBitmask = _DiffServMacAceEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 13),
    _DiffServMacAceEtherTypeBitmask_Type()
)
diffServMacAceEtherTypeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceEtherTypeBitmask.setStatus("current")


class _DiffServMacAceMinEtherType_Type(Integer32):
    """Custom type diffServMacAceMinEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServMacAceMinEtherType_Type.__name__ = "Integer32"
_DiffServMacAceMinEtherType_Object = MibTableColumn
diffServMacAceMinEtherType = _DiffServMacAceMinEtherType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 14),
    _DiffServMacAceMinEtherType_Type()
)
diffServMacAceMinEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinEtherType.setStatus("current")
_DiffServMacAceStatus_Type = RowStatus
_DiffServMacAceStatus_Object = MibTableColumn
diffServMacAceStatus = _DiffServMacAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 16),
    _DiffServMacAceStatus_Type()
)
diffServMacAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceStatus.setStatus("current")


class _DiffServMacAceCosOp_Type(Integer32):
    """Custom type diffServMacAceCosOp based on Integer32"""
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


_DiffServMacAceCosOp_Type.__name__ = "Integer32"
_DiffServMacAceCosOp_Object = MibTableColumn
diffServMacAceCosOp = _DiffServMacAceCosOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 17),
    _DiffServMacAceCosOp_Type()
)
diffServMacAceCosOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceCosOp.setStatus("current")


class _DiffServMacAceCosBitmask_Type(Integer32):
    """Custom type diffServMacAceCosBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DiffServMacAceCosBitmask_Type.__name__ = "Integer32"
_DiffServMacAceCosBitmask_Object = MibTableColumn
diffServMacAceCosBitmask = _DiffServMacAceCosBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 18),
    _DiffServMacAceCosBitmask_Type()
)
diffServMacAceCosBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceCosBitmask.setStatus("current")


class _DiffServMacAceMinCos_Type(Integer32):
    """Custom type diffServMacAceMinCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DiffServMacAceMinCos_Type.__name__ = "Integer32"
_DiffServMacAceMinCos_Object = MibTableColumn
diffServMacAceMinCos = _DiffServMacAceMinCos_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 18, 1, 19),
    _DiffServMacAceMinCos_Type()
)
diffServMacAceMinCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinCos.setStatus("current")
_DiffServActionTable_Object = MibTable
diffServActionTable = _DiffServActionTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 19)
)
if mibBuilder.loadTexts:
    diffServActionTable.setStatus("current")
_DiffServActionEntry_Object = MibTableRow
diffServActionEntry = _DiffServActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 19, 1)
)
diffServActionEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServActionIndex"),
)
if mibBuilder.loadTexts:
    diffServActionEntry.setStatus("current")


class _DiffServActionIndex_Type(Integer32):
    """Custom type diffServActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DiffServActionIndex_Type.__name__ = "Integer32"
_DiffServActionIndex_Object = MibTableColumn
diffServActionIndex = _DiffServActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 19, 1, 1),
    _DiffServActionIndex_Type()
)
diffServActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServActionIndex.setStatus("current")


class _DiffServActionList_Type(Bits):
    """Custom type diffServActionList based on Bits"""
    namedValues = NamedValues(
        *(("actionPktNewDscp", 11),
          ("actionPktNewPhb", 9),
          ("actionPktNewPri", 0))
    )

_DiffServActionList_Type.__name__ = "Bits"
_DiffServActionList_Object = MibTableColumn
diffServActionList = _DiffServActionList_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 19, 1, 2),
    _DiffServActionList_Type()
)
diffServActionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionList.setStatus("current")


class _DiffServActionPktNewPri_Type(Integer32):
    """Custom type diffServActionPktNewPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DiffServActionPktNewPri_Type.__name__ = "Integer32"
_DiffServActionPktNewPri_Object = MibTableColumn
diffServActionPktNewPri = _DiffServActionPktNewPri_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 19, 1, 3),
    _DiffServActionPktNewPri_Type()
)
diffServActionPktNewPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionPktNewPri.setStatus("current")


class _DiffServActionPktNewPhb_Type(Integer32):
    """Custom type diffServActionPktNewPhb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DiffServActionPktNewPhb_Type.__name__ = "Integer32"
_DiffServActionPktNewPhb_Object = MibTableColumn
diffServActionPktNewPhb = _DiffServActionPktNewPhb_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 19, 1, 4),
    _DiffServActionPktNewPhb_Type()
)
diffServActionPktNewPhb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionPktNewPhb.setStatus("current")
_DiffServActionStatus_Type = RowStatus
_DiffServActionStatus_Object = MibTableColumn
diffServActionStatus = _DiffServActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 19, 1, 11),
    _DiffServActionStatus_Type()
)
diffServActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionStatus.setStatus("current")


class _DiffServActionPktNewDscp_Type(Integer32):
    """Custom type diffServActionPktNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServActionPktNewDscp_Type.__name__ = "Integer32"
_DiffServActionPktNewDscp_Object = MibTableColumn
diffServActionPktNewDscp = _DiffServActionPktNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 19, 1, 13),
    _DiffServActionPktNewDscp_Type()
)
diffServActionPktNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionPktNewDscp.setStatus("current")
_DiffServMeterTable_Object = MibTable
diffServMeterTable = _DiffServMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 20)
)
if mibBuilder.loadTexts:
    diffServMeterTable.setStatus("current")
_DiffServMeterEntry_Object = MibTableRow
diffServMeterEntry = _DiffServMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 20, 1)
)
diffServMeterEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServActionIndex"),
)
if mibBuilder.loadTexts:
    diffServMeterEntry.setStatus("current")
_DiffServMeterIndex_Type = Integer32
_DiffServMeterIndex_Object = MibTableColumn
diffServMeterIndex = _DiffServMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 20, 1, 1),
    _DiffServMeterIndex_Type()
)
diffServMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMeterIndex.setStatus("current")


class _DiffServMeterModel_Type(Integer32):
    """Custom type diffServMeterModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("rate", 8))
    )


_DiffServMeterModel_Type.__name__ = "Integer32"
_DiffServMeterModel_Object = MibTableColumn
diffServMeterModel = _DiffServMeterModel_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 20, 1, 2),
    _DiffServMeterModel_Type()
)
diffServMeterModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterModel.setStatus("current")


class _DiffServMeterRate_Type(Integer32):
    """Custom type diffServMeterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1000000),
    )


_DiffServMeterRate_Type.__name__ = "Integer32"
_DiffServMeterRate_Object = MibTableColumn
diffServMeterRate = _DiffServMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 20, 1, 3),
    _DiffServMeterRate_Type()
)
diffServMeterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterRate.setStatus("current")
_DiffServMeterStatus_Type = RowStatus
_DiffServMeterStatus_Object = MibTableColumn
diffServMeterStatus = _DiffServMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 20, 1, 6),
    _DiffServMeterStatus_Type()
)
diffServMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterStatus.setStatus("current")
_DiffServIpv6AceTable_Object = MibTable
diffServIpv6AceTable = _DiffServIpv6AceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21)
)
if mibBuilder.loadTexts:
    diffServIpv6AceTable.setStatus("current")
_DiffServIpv6AceEntry_Object = MibTableRow
diffServIpv6AceEntry = _DiffServIpv6AceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1)
)
diffServIpv6AceEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServIpv6AceIndex"),
)
if mibBuilder.loadTexts:
    diffServIpv6AceEntry.setStatus("current")


class _DiffServIpv6AceIndex_Type(Integer32):
    """Custom type diffServIpv6AceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_DiffServIpv6AceIndex_Type.__name__ = "Integer32"
_DiffServIpv6AceIndex_Object = MibTableColumn
diffServIpv6AceIndex = _DiffServIpv6AceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 1),
    _DiffServIpv6AceIndex_Type()
)
diffServIpv6AceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServIpv6AceIndex.setStatus("current")


class _DiffServIpv6AceType_Type(Integer32):
    """Custom type diffServIpv6AceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("standard", 1))
    )


_DiffServIpv6AceType_Type.__name__ = "Integer32"
_DiffServIpv6AceType_Object = MibTableColumn
diffServIpv6AceType = _DiffServIpv6AceType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 2),
    _DiffServIpv6AceType_Type()
)
diffServIpv6AceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceType.setStatus("current")


class _DiffServIpv6AceAccess_Type(Integer32):
    """Custom type diffServIpv6AceAccess based on Integer32"""
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


_DiffServIpv6AceAccess_Type.__name__ = "Integer32"
_DiffServIpv6AceAccess_Object = MibTableColumn
diffServIpv6AceAccess = _DiffServIpv6AceAccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 3),
    _DiffServIpv6AceAccess_Type()
)
diffServIpv6AceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceAccess.setStatus("current")


class _DiffServIpv6AceSourceIpAddr_Type(OctetString):
    """Custom type diffServIpv6AceSourceIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DiffServIpv6AceSourceIpAddr_Type.__name__ = "OctetString"
_DiffServIpv6AceSourceIpAddr_Object = MibTableColumn
diffServIpv6AceSourceIpAddr = _DiffServIpv6AceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 4),
    _DiffServIpv6AceSourceIpAddr_Type()
)
diffServIpv6AceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceSourceIpAddr.setStatus("current")


class _DiffServIpv6AceSourceIpAddrPrefixLen_Type(Integer32):
    """Custom type diffServIpv6AceSourceIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DiffServIpv6AceSourceIpAddrPrefixLen_Type.__name__ = "Integer32"
_DiffServIpv6AceSourceIpAddrPrefixLen_Object = MibTableColumn
diffServIpv6AceSourceIpAddrPrefixLen = _DiffServIpv6AceSourceIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 5),
    _DiffServIpv6AceSourceIpAddrPrefixLen_Type()
)
diffServIpv6AceSourceIpAddrPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceSourceIpAddrPrefixLen.setStatus("current")


class _DiffServIpv6AceDestIpAddr_Type(OctetString):
    """Custom type diffServIpv6AceDestIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DiffServIpv6AceDestIpAddr_Type.__name__ = "OctetString"
_DiffServIpv6AceDestIpAddr_Object = MibTableColumn
diffServIpv6AceDestIpAddr = _DiffServIpv6AceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 6),
    _DiffServIpv6AceDestIpAddr_Type()
)
diffServIpv6AceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceDestIpAddr.setStatus("current")


class _DiffServIpv6AceDestIpAddrPrefixLen_Type(Integer32):
    """Custom type diffServIpv6AceDestIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DiffServIpv6AceDestIpAddrPrefixLen_Type.__name__ = "Integer32"
_DiffServIpv6AceDestIpAddrPrefixLen_Object = MibTableColumn
diffServIpv6AceDestIpAddrPrefixLen = _DiffServIpv6AceDestIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 7),
    _DiffServIpv6AceDestIpAddrPrefixLen_Type()
)
diffServIpv6AceDestIpAddrPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceDestIpAddrPrefixLen.setStatus("current")


class _DiffServIpv6AceNextHeader_Type(Integer32):
    """Custom type diffServIpv6AceNextHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DiffServIpv6AceNextHeader_Type.__name__ = "Integer32"
_DiffServIpv6AceNextHeader_Object = MibTableColumn
diffServIpv6AceNextHeader = _DiffServIpv6AceNextHeader_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 8),
    _DiffServIpv6AceNextHeader_Type()
)
diffServIpv6AceNextHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceNextHeader.setStatus("current")


class _DiffServIpv6AceDscp_Type(Integer32):
    """Custom type diffServIpv6AceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DiffServIpv6AceDscp_Type.__name__ = "Integer32"
_DiffServIpv6AceDscp_Object = MibTableColumn
diffServIpv6AceDscp = _DiffServIpv6AceDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 9),
    _DiffServIpv6AceDscp_Type()
)
diffServIpv6AceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceDscp.setStatus("current")
_DiffServIpv6AceStatus_Type = RowStatus
_DiffServIpv6AceStatus_Object = MibTableColumn
diffServIpv6AceStatus = _DiffServIpv6AceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 11),
    _DiffServIpv6AceStatus_Type()
)
diffServIpv6AceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceStatus.setStatus("current")


class _DiffServIpv6AceSourcePortOp_Type(Integer32):
    """Custom type diffServIpv6AceSourcePortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1))
    )


_DiffServIpv6AceSourcePortOp_Type.__name__ = "Integer32"
_DiffServIpv6AceSourcePortOp_Object = MibTableColumn
diffServIpv6AceSourcePortOp = _DiffServIpv6AceSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 13),
    _DiffServIpv6AceSourcePortOp_Type()
)
diffServIpv6AceSourcePortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceSourcePortOp.setStatus("current")


class _DiffServIpv6AceSourcePort_Type(Integer32):
    """Custom type diffServIpv6AceSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpv6AceSourcePort_Type.__name__ = "Integer32"
_DiffServIpv6AceSourcePort_Object = MibTableColumn
diffServIpv6AceSourcePort = _DiffServIpv6AceSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 14),
    _DiffServIpv6AceSourcePort_Type()
)
diffServIpv6AceSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServIpv6AceSourcePort.setStatus("current")


class _DiffServIpv6AceSourcePortBitmask_Type(Integer32):
    """Custom type diffServIpv6AceSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpv6AceSourcePortBitmask_Type.__name__ = "Integer32"
_DiffServIpv6AceSourcePortBitmask_Object = MibTableColumn
diffServIpv6AceSourcePortBitmask = _DiffServIpv6AceSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 15),
    _DiffServIpv6AceSourcePortBitmask_Type()
)
diffServIpv6AceSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceSourcePortBitmask.setStatus("current")


class _DiffServIpv6AceDestPortOp_Type(Integer32):
    """Custom type diffServIpv6AceDestPortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1))
    )


_DiffServIpv6AceDestPortOp_Type.__name__ = "Integer32"
_DiffServIpv6AceDestPortOp_Object = MibTableColumn
diffServIpv6AceDestPortOp = _DiffServIpv6AceDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 16),
    _DiffServIpv6AceDestPortOp_Type()
)
diffServIpv6AceDestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceDestPortOp.setStatus("current")


class _DiffServIpv6AceDestPort_Type(Integer32):
    """Custom type diffServIpv6AceDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpv6AceDestPort_Type.__name__ = "Integer32"
_DiffServIpv6AceDestPort_Object = MibTableColumn
diffServIpv6AceDestPort = _DiffServIpv6AceDestPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 17),
    _DiffServIpv6AceDestPort_Type()
)
diffServIpv6AceDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceDestPort.setStatus("current")


class _DiffServIpv6AceDestPortBitmask_Type(Integer32):
    """Custom type diffServIpv6AceDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpv6AceDestPortBitmask_Type.__name__ = "Integer32"
_DiffServIpv6AceDestPortBitmask_Object = MibTableColumn
diffServIpv6AceDestPortBitmask = _DiffServIpv6AceDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 21, 1, 18),
    _DiffServIpv6AceDestPortBitmask_Type()
)
diffServIpv6AceDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceDestPortBitmask.setStatus("current")
_DiffServArpAceTable_Object = MibTable
diffServArpAceTable = _DiffServArpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23)
)
if mibBuilder.loadTexts:
    diffServArpAceTable.setStatus("current")
_DiffServArpAceEntry_Object = MibTableRow
diffServArpAceEntry = _DiffServArpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1)
)
diffServArpAceEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServArpAceIndex"),
)
if mibBuilder.loadTexts:
    diffServArpAceEntry.setStatus("current")


class _DiffServArpAceIndex_Type(Integer32):
    """Custom type diffServArpAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DiffServArpAceIndex_Type.__name__ = "Integer32"
_DiffServArpAceIndex_Object = MibTableColumn
diffServArpAceIndex = _DiffServArpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 1),
    _DiffServArpAceIndex_Type()
)
diffServArpAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServArpAceIndex.setStatus("current")


class _DiffServArpAceAction_Type(Integer32):
    """Custom type diffServArpAceAction based on Integer32"""
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


_DiffServArpAceAction_Type.__name__ = "Integer32"
_DiffServArpAceAction_Object = MibTableColumn
diffServArpAceAction = _DiffServArpAceAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 2),
    _DiffServArpAceAction_Type()
)
diffServArpAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceAction.setStatus("current")


class _DiffServArpAcePktType_Type(Integer32):
    """Custom type diffServArpAcePktType based on Integer32"""
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
          ("request", 1),
          ("response", 2))
    )


_DiffServArpAcePktType_Type.__name__ = "Integer32"
_DiffServArpAcePktType_Object = MibTableColumn
diffServArpAcePktType = _DiffServArpAcePktType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 3),
    _DiffServArpAcePktType_Type()
)
diffServArpAcePktType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAcePktType.setStatus("current")
_DiffServArpAceSourceIpAddr_Type = IpAddress
_DiffServArpAceSourceIpAddr_Object = MibTableColumn
diffServArpAceSourceIpAddr = _DiffServArpAceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 4),
    _DiffServArpAceSourceIpAddr_Type()
)
diffServArpAceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceSourceIpAddr.setStatus("current")
_DiffServArpAceSourceIpAddrBitmask_Type = IpAddress
_DiffServArpAceSourceIpAddrBitmask_Object = MibTableColumn
diffServArpAceSourceIpAddrBitmask = _DiffServArpAceSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 5),
    _DiffServArpAceSourceIpAddrBitmask_Type()
)
diffServArpAceSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceSourceIpAddrBitmask.setStatus("current")
_DiffServArpAceDestIpAddr_Type = IpAddress
_DiffServArpAceDestIpAddr_Object = MibTableColumn
diffServArpAceDestIpAddr = _DiffServArpAceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 6),
    _DiffServArpAceDestIpAddr_Type()
)
diffServArpAceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceDestIpAddr.setStatus("current")
_DiffServArpAceDestIpAddrBitmask_Type = IpAddress
_DiffServArpAceDestIpAddrBitmask_Object = MibTableColumn
diffServArpAceDestIpAddrBitmask = _DiffServArpAceDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 7),
    _DiffServArpAceDestIpAddrBitmask_Type()
)
diffServArpAceDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceDestIpAddrBitmask.setStatus("current")


class _DiffServArpAceSourceMacAddr_Type(OctetString):
    """Custom type diffServArpAceSourceMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DiffServArpAceSourceMacAddr_Type.__name__ = "OctetString"
_DiffServArpAceSourceMacAddr_Object = MibTableColumn
diffServArpAceSourceMacAddr = _DiffServArpAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 8),
    _DiffServArpAceSourceMacAddr_Type()
)
diffServArpAceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceSourceMacAddr.setStatus("current")


class _DiffServArpAceSourceMacAddrBitmask_Type(OctetString):
    """Custom type diffServArpAceSourceMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DiffServArpAceSourceMacAddrBitmask_Type.__name__ = "OctetString"
_DiffServArpAceSourceMacAddrBitmask_Object = MibTableColumn
diffServArpAceSourceMacAddrBitmask = _DiffServArpAceSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 9),
    _DiffServArpAceSourceMacAddrBitmask_Type()
)
diffServArpAceSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceSourceMacAddrBitmask.setStatus("current")


class _DiffServArpAceDestMacAddr_Type(OctetString):
    """Custom type diffServArpAceDestMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DiffServArpAceDestMacAddr_Type.__name__ = "OctetString"
_DiffServArpAceDestMacAddr_Object = MibTableColumn
diffServArpAceDestMacAddr = _DiffServArpAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 10),
    _DiffServArpAceDestMacAddr_Type()
)
diffServArpAceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceDestMacAddr.setStatus("current")


class _DiffServArpAceDestMacAddrBitmask_Type(OctetString):
    """Custom type diffServArpAceDestMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_DiffServArpAceDestMacAddrBitmask_Type.__name__ = "OctetString"
_DiffServArpAceDestMacAddrBitmask_Object = MibTableColumn
diffServArpAceDestMacAddrBitmask = _DiffServArpAceDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 11),
    _DiffServArpAceDestMacAddrBitmask_Type()
)
diffServArpAceDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceDestMacAddrBitmask.setStatus("current")
_DiffServArpAceLogStatus_Type = EnabledStatus
_DiffServArpAceLogStatus_Object = MibTableColumn
diffServArpAceLogStatus = _DiffServArpAceLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 12),
    _DiffServArpAceLogStatus_Type()
)
diffServArpAceLogStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceLogStatus.setStatus("current")
_DiffServArpAceStatus_Type = RowStatus
_DiffServArpAceStatus_Object = MibTableColumn
diffServArpAceStatus = _DiffServArpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 23, 1, 13),
    _DiffServArpAceStatus_Type()
)
diffServArpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceStatus.setStatus("current")
_DiffServArpTable_Object = MibTable
diffServArpTable = _DiffServArpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 24)
)
if mibBuilder.loadTexts:
    diffServArpTable.setStatus("current")
_DiffServArpEntry_Object = MibTableRow
diffServArpEntry = _DiffServArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 24, 1)
)
diffServArpEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServArpAclName"),
)
if mibBuilder.loadTexts:
    diffServArpEntry.setStatus("current")


class _DiffServArpAclName_Type(DisplayString):
    """Custom type diffServArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServArpAclName_Type.__name__ = "DisplayString"
_DiffServArpAclName_Object = MibTableColumn
diffServArpAclName = _DiffServArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 24, 1, 1),
    _DiffServArpAclName_Type()
)
diffServArpAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServArpAclName.setStatus("current")
_DiffServAclHwCounterTable_Object = MibTable
diffServAclHwCounterTable = _DiffServAclHwCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 26)
)
if mibBuilder.loadTexts:
    diffServAclHwCounterTable.setStatus("current")
_DiffServAclHwCounterEntry_Object = MibTableRow
diffServAclHwCounterEntry = _DiffServAclHwCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 26, 1)
)
diffServAclHwCounterEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServAclHwCounterIfIndex"),
    (0, "ECS2100-28PP-MIB", "diffServAclHwCounterDirection"),
    (0, "ECS2100-28PP-MIB", "diffServAclHwCounterAclIndex"),
    (0, "ECS2100-28PP-MIB", "diffServAclHwCounterAceIndex"),
)
if mibBuilder.loadTexts:
    diffServAclHwCounterEntry.setStatus("current")
_DiffServAclHwCounterIfIndex_Type = InterfaceIndex
_DiffServAclHwCounterIfIndex_Object = MibTableColumn
diffServAclHwCounterIfIndex = _DiffServAclHwCounterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 26, 1, 1),
    _DiffServAclHwCounterIfIndex_Type()
)
diffServAclHwCounterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAclHwCounterIfIndex.setStatus("current")


class _DiffServAclHwCounterDirection_Type(Integer32):
    """Custom type diffServAclHwCounterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ingress", 1)
    )


_DiffServAclHwCounterDirection_Type.__name__ = "Integer32"
_DiffServAclHwCounterDirection_Object = MibTableColumn
diffServAclHwCounterDirection = _DiffServAclHwCounterDirection_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 26, 1, 2),
    _DiffServAclHwCounterDirection_Type()
)
diffServAclHwCounterDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAclHwCounterDirection.setStatus("current")


class _DiffServAclHwCounterAclIndex_Type(Integer32):
    """Custom type diffServAclHwCounterAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServAclHwCounterAclIndex_Type.__name__ = "Integer32"
_DiffServAclHwCounterAclIndex_Object = MibTableColumn
diffServAclHwCounterAclIndex = _DiffServAclHwCounterAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 26, 1, 3),
    _DiffServAclHwCounterAclIndex_Type()
)
diffServAclHwCounterAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAclHwCounterAclIndex.setStatus("current")


class _DiffServAclHwCounterAceIndex_Type(Integer32):
    """Custom type diffServAclHwCounterAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DiffServAclHwCounterAceIndex_Type.__name__ = "Integer32"
_DiffServAclHwCounterAceIndex_Object = MibTableColumn
diffServAclHwCounterAceIndex = _DiffServAclHwCounterAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 26, 1, 4),
    _DiffServAclHwCounterAceIndex_Type()
)
diffServAclHwCounterAceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAclHwCounterAceIndex.setStatus("current")
_DiffServAclHwCounterAceHitCount_Type = Unsigned32
_DiffServAclHwCounterAceHitCount_Object = MibTableColumn
diffServAclHwCounterAceHitCount = _DiffServAclHwCounterAceHitCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 26, 1, 5),
    _DiffServAclHwCounterAceHitCount_Type()
)
diffServAclHwCounterAceHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAclHwCounterAceHitCount.setStatus("current")
_DiffServPolicyMapPortTable_Object = MibTable
diffServPolicyMapPortTable = _DiffServPolicyMapPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 27)
)
if mibBuilder.loadTexts:
    diffServPolicyMapPortTable.setStatus("current")
_DiffServPolicyMapPortEntry_Object = MibTableRow
diffServPolicyMapPortEntry = _DiffServPolicyMapPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 27, 1)
)
diffServPolicyMapPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServPolicyMapPortIfIndex"),
    (0, "ECS2100-28PP-MIB", "diffServPolicyMapPortDirection"),
)
if mibBuilder.loadTexts:
    diffServPolicyMapPortEntry.setStatus("current")
_DiffServPolicyMapPortIfIndex_Type = InterfaceIndex
_DiffServPolicyMapPortIfIndex_Object = MibTableColumn
diffServPolicyMapPortIfIndex = _DiffServPolicyMapPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 27, 1, 1),
    _DiffServPolicyMapPortIfIndex_Type()
)
diffServPolicyMapPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPolicyMapPortIfIndex.setStatus("current")


class _DiffServPolicyMapPortDirection_Type(Integer32):
    """Custom type diffServPolicyMapPortDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ingress", 1)
    )


_DiffServPolicyMapPortDirection_Type.__name__ = "Integer32"
_DiffServPolicyMapPortDirection_Object = MibTableColumn
diffServPolicyMapPortDirection = _DiffServPolicyMapPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 27, 1, 2),
    _DiffServPolicyMapPortDirection_Type()
)
diffServPolicyMapPortDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPolicyMapPortDirection.setStatus("current")
_DiffServPolicyMapPortPolicyMapIndex_Type = Integer32
_DiffServPolicyMapPortPolicyMapIndex_Object = MibTableColumn
diffServPolicyMapPortPolicyMapIndex = _DiffServPolicyMapPortPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 27, 1, 3),
    _DiffServPolicyMapPortPolicyMapIndex_Type()
)
diffServPolicyMapPortPolicyMapIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapPortPolicyMapIndex.setStatus("current")
_DiffServPolicyMapPortStatus_Type = RowStatus
_DiffServPolicyMapPortStatus_Object = MibTableColumn
diffServPolicyMapPortStatus = _DiffServPolicyMapPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 27, 1, 4),
    _DiffServPolicyMapPortStatus_Type()
)
diffServPolicyMapPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapPortStatus.setStatus("current")
_DiffServAccessGroupTable_Object = MibTable
diffServAccessGroupTable = _DiffServAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 28)
)
if mibBuilder.loadTexts:
    diffServAccessGroupTable.setStatus("current")
_DiffServAccessGroupEntry_Object = MibTableRow
diffServAccessGroupEntry = _DiffServAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 28, 1)
)
diffServAccessGroupEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServAccessGroupIfIndex"),
    (0, "ECS2100-28PP-MIB", "diffServAccessGroupDirection"),
    (0, "ECS2100-28PP-MIB", "diffServAccessGroupType"),
)
if mibBuilder.loadTexts:
    diffServAccessGroupEntry.setStatus("current")
_DiffServAccessGroupIfIndex_Type = InterfaceIndex
_DiffServAccessGroupIfIndex_Object = MibTableColumn
diffServAccessGroupIfIndex = _DiffServAccessGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 28, 1, 1),
    _DiffServAccessGroupIfIndex_Type()
)
diffServAccessGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServAccessGroupIfIndex.setStatus("current")


class _DiffServAccessGroupDirection_Type(Integer32):
    """Custom type diffServAccessGroupDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ingress", 1)
    )


_DiffServAccessGroupDirection_Type.__name__ = "Integer32"
_DiffServAccessGroupDirection_Object = MibTableColumn
diffServAccessGroupDirection = _DiffServAccessGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 28, 1, 2),
    _DiffServAccessGroupDirection_Type()
)
diffServAccessGroupDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServAccessGroupDirection.setStatus("current")


class _DiffServAccessGroupType_Type(Integer32):
    """Custom type diffServAccessGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("ipv6", 3),
          ("mac", 1))
    )


_DiffServAccessGroupType_Type.__name__ = "Integer32"
_DiffServAccessGroupType_Object = MibTableColumn
diffServAccessGroupType = _DiffServAccessGroupType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 28, 1, 3),
    _DiffServAccessGroupType_Type()
)
diffServAccessGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServAccessGroupType.setStatus("current")
_DiffServAccessGroupAclIndex_Type = Integer32
_DiffServAccessGroupAclIndex_Object = MibTableColumn
diffServAccessGroupAclIndex = _DiffServAccessGroupAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 28, 1, 4),
    _DiffServAccessGroupAclIndex_Type()
)
diffServAccessGroupAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAccessGroupAclIndex.setStatus("current")


class _DiffServAccessGroupTimeRangeName_Type(DisplayString):
    """Custom type diffServAccessGroupTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DiffServAccessGroupTimeRangeName_Type.__name__ = "DisplayString"
_DiffServAccessGroupTimeRangeName_Object = MibTableColumn
diffServAccessGroupTimeRangeName = _DiffServAccessGroupTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 28, 1, 5),
    _DiffServAccessGroupTimeRangeName_Type()
)
diffServAccessGroupTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAccessGroupTimeRangeName.setStatus("current")
_DiffServAccessGroupCounterStatus_Type = EnabledStatus
_DiffServAccessGroupCounterStatus_Object = MibTableColumn
diffServAccessGroupCounterStatus = _DiffServAccessGroupCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 28, 1, 6),
    _DiffServAccessGroupCounterStatus_Type()
)
diffServAccessGroupCounterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAccessGroupCounterStatus.setStatus("current")
_DiffServAccessGroupStatus_Type = RowStatus
_DiffServAccessGroupStatus_Object = MibTableColumn
diffServAccessGroupStatus = _DiffServAccessGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 28, 1, 7),
    _DiffServAccessGroupStatus_Type()
)
diffServAccessGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAccessGroupStatus.setStatus("current")
_DiffServTcamTable_Object = MibTable
diffServTcamTable = _DiffServTcamTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 29)
)
if mibBuilder.loadTexts:
    diffServTcamTable.setStatus("current")
_DiffServTcamEntry_Object = MibTableRow
diffServTcamEntry = _DiffServTcamEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 29, 1)
)
diffServTcamEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "diffServTcamUnit"),
    (0, "ECS2100-28PP-MIB", "diffServTcamDevice"),
    (0, "ECS2100-28PP-MIB", "diffServTcamPool"),
)
if mibBuilder.loadTexts:
    diffServTcamEntry.setStatus("current")


class _DiffServTcamUnit_Type(Integer32):
    """Custom type diffServTcamUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DiffServTcamUnit_Type.__name__ = "Integer32"
_DiffServTcamUnit_Object = MibTableColumn
diffServTcamUnit = _DiffServTcamUnit_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 29, 1, 1),
    _DiffServTcamUnit_Type()
)
diffServTcamUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServTcamUnit.setStatus("current")
_DiffServTcamDevice_Type = Integer32
_DiffServTcamDevice_Object = MibTableColumn
diffServTcamDevice = _DiffServTcamDevice_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 29, 1, 2),
    _DiffServTcamDevice_Type()
)
diffServTcamDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServTcamDevice.setStatus("current")
_DiffServTcamPool_Type = Integer32
_DiffServTcamPool_Object = MibTableColumn
diffServTcamPool = _DiffServTcamPool_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 29, 1, 3),
    _DiffServTcamPool_Type()
)
diffServTcamPool.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServTcamPool.setStatus("current")


class _DiffServTcamPoolCapability_Type(Bits):
    """Custom type diffServTcamPoolCapability based on Bits"""
    namedValues = NamedValues(
        *(("cpuInterface", 19),
          ("egressIpAcl", 9),
          ("egressIpDiffServ", 13),
          ("egressIpv6ExtAcl", 11),
          ("egressIpv6ExtDiffServ", 15),
          ("egressIpv6StdAcl", 10),
          ("egressIpv6StdDiffServ", 14),
          ("egressMacAcl", 8),
          ("egressMacDiffServ", 12),
          ("ipAcl", 1),
          ("ipDiffServ", 5),
          ("ipSourceGuard", 17),
          ("ipv6ExtAcl", 3),
          ("ipv6ExtDiffServ", 7),
          ("ipv6SourceGuard", 18),
          ("ipv6StdAcl", 2),
          ("ipv6StdDiffServ", 6),
          ("linkLocal", 21),
          ("macAcl", 0),
          ("macDiffServ", 4),
          ("rateLimit", 20),
          ("reserved", 22),
          ("webAuth", 16))
    )

_DiffServTcamPoolCapability_Type.__name__ = "Bits"
_DiffServTcamPoolCapability_Object = MibTableColumn
diffServTcamPoolCapability = _DiffServTcamPoolCapability_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 29, 1, 4),
    _DiffServTcamPoolCapability_Type()
)
diffServTcamPoolCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServTcamPoolCapability.setStatus("current")
_DiffServTcamTotal_Type = Integer32
_DiffServTcamTotal_Object = MibTableColumn
diffServTcamTotal = _DiffServTcamTotal_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 29, 1, 5),
    _DiffServTcamTotal_Type()
)
diffServTcamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServTcamTotal.setStatus("current")
_DiffServTcamFree_Type = Integer32
_DiffServTcamFree_Object = MibTableColumn
diffServTcamFree = _DiffServTcamFree_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 29, 1, 6),
    _DiffServTcamFree_Type()
)
diffServTcamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServTcamFree.setStatus("current")
_DiffServTcamUsed_Type = Integer32
_DiffServTcamUsed_Object = MibTableColumn
diffServTcamUsed = _DiffServTcamUsed_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 16, 4, 29, 1, 7),
    _DiffServTcamUsed_Type()
)
diffServTcamUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServTcamUsed.setStatus("current")
_SecurityMgt_ObjectIdentity = ObjectIdentity
securityMgt = _SecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17)
)
_PrivateVlanMgt_ObjectIdentity = ObjectIdentity
privateVlanMgt = _PrivateVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1)
)
_PrivateVlanStatus_Type = EnabledStatus
_PrivateVlanStatus_Object = MibScalar
privateVlanStatus = _PrivateVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 1),
    _PrivateVlanStatus_Type()
)
privateVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanStatus.setStatus("current")
_PrivateVlanUplinkPorts_Type = PortList
_PrivateVlanUplinkPorts_Object = MibScalar
privateVlanUplinkPorts = _PrivateVlanUplinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 2),
    _PrivateVlanUplinkPorts_Type()
)
privateVlanUplinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanUplinkPorts.setStatus("current")
_PrivateVlanDownlinkPorts_Type = PortList
_PrivateVlanDownlinkPorts_Object = MibScalar
privateVlanDownlinkPorts = _PrivateVlanDownlinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 3),
    _PrivateVlanDownlinkPorts_Type()
)
privateVlanDownlinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanDownlinkPorts.setStatus("current")
_PrivateVlanVlanTable_Object = MibTable
privateVlanVlanTable = _PrivateVlanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 4)
)
if mibBuilder.loadTexts:
    privateVlanVlanTable.setStatus("current")
_PrivateVlanVlanEntry_Object = MibTableRow
privateVlanVlanEntry = _PrivateVlanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 4, 1)
)
privateVlanVlanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "privateVlanVlanIndex"),
)
if mibBuilder.loadTexts:
    privateVlanVlanEntry.setStatus("current")


class _PrivateVlanVlanIndex_Type(Integer32):
    """Custom type privateVlanVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PrivateVlanVlanIndex_Type.__name__ = "Integer32"
_PrivateVlanVlanIndex_Object = MibTableColumn
privateVlanVlanIndex = _PrivateVlanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 4, 1, 1),
    _PrivateVlanVlanIndex_Type()
)
privateVlanVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateVlanVlanIndex.setStatus("current")


class _PrivateVlanVlanType_Type(Integer32):
    """Custom type privateVlanVlanType based on Integer32"""
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
        *(("community", 4),
          ("invalid", 1),
          ("isolated", 3),
          ("primary", 2))
    )


_PrivateVlanVlanType_Type.__name__ = "Integer32"
_PrivateVlanVlanType_Object = MibTableColumn
privateVlanVlanType = _PrivateVlanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 4, 1, 2),
    _PrivateVlanVlanType_Type()
)
privateVlanVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanVlanType.setStatus("current")


class _PrivateVlanAssoicatedPrimaryVlan_Type(Integer32):
    """Custom type privateVlanAssoicatedPrimaryVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrivateVlanAssoicatedPrimaryVlan_Type.__name__ = "Integer32"
_PrivateVlanAssoicatedPrimaryVlan_Object = MibTableColumn
privateVlanAssoicatedPrimaryVlan = _PrivateVlanAssoicatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 4, 1, 3),
    _PrivateVlanAssoicatedPrimaryVlan_Type()
)
privateVlanAssoicatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanAssoicatedPrimaryVlan.setStatus("current")
_PrivateVlanPrivatePortTable_Object = MibTable
privateVlanPrivatePortTable = _PrivateVlanPrivatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 5)
)
if mibBuilder.loadTexts:
    privateVlanPrivatePortTable.setStatus("current")
_PrivateVlanPrivatePortEntry_Object = MibTableRow
privateVlanPrivatePortEntry = _PrivateVlanPrivatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 5, 1)
)
privateVlanPrivatePortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "privateVlanPrivatePortIfIndex"),
)
if mibBuilder.loadTexts:
    privateVlanPrivatePortEntry.setStatus("current")
_PrivateVlanPrivatePortIfIndex_Type = InterfaceIndex
_PrivateVlanPrivatePortIfIndex_Object = MibTableColumn
privateVlanPrivatePortIfIndex = _PrivateVlanPrivatePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 5, 1, 1),
    _PrivateVlanPrivatePortIfIndex_Type()
)
privateVlanPrivatePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateVlanPrivatePortIfIndex.setStatus("current")


class _PrivateVlanPrivatePortSecondaryVlan_Type(Integer32):
    """Custom type privateVlanPrivatePortSecondaryVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrivateVlanPrivatePortSecondaryVlan_Type.__name__ = "Integer32"
_PrivateVlanPrivatePortSecondaryVlan_Object = MibTableColumn
privateVlanPrivatePortSecondaryVlan = _PrivateVlanPrivatePortSecondaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 5, 1, 2),
    _PrivateVlanPrivatePortSecondaryVlan_Type()
)
privateVlanPrivatePortSecondaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanPrivatePortSecondaryVlan.setStatus("current")
_PrivateVlanPromPortTable_Object = MibTable
privateVlanPromPortTable = _PrivateVlanPromPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 6)
)
if mibBuilder.loadTexts:
    privateVlanPromPortTable.setStatus("current")
_PrivateVlanPromPortEntry_Object = MibTableRow
privateVlanPromPortEntry = _PrivateVlanPromPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 6, 1)
)
privateVlanPromPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "privateVlanPromPortIfIndex"),
)
if mibBuilder.loadTexts:
    privateVlanPromPortEntry.setStatus("current")
_PrivateVlanPromPortIfIndex_Type = InterfaceIndex
_PrivateVlanPromPortIfIndex_Object = MibTableColumn
privateVlanPromPortIfIndex = _PrivateVlanPromPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 6, 1, 1),
    _PrivateVlanPromPortIfIndex_Type()
)
privateVlanPromPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateVlanPromPortIfIndex.setStatus("current")


class _PrivateVlanPromPortPrimaryVlanId_Type(Integer32):
    """Custom type privateVlanPromPortPrimaryVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrivateVlanPromPortPrimaryVlanId_Type.__name__ = "Integer32"
_PrivateVlanPromPortPrimaryVlanId_Object = MibTableColumn
privateVlanPromPortPrimaryVlanId = _PrivateVlanPromPortPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 6, 1, 2),
    _PrivateVlanPromPortPrimaryVlanId_Type()
)
privateVlanPromPortPrimaryVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanPromPortPrimaryVlanId.setStatus("current")


class _PrivateVlanPromPortSecondaryRemap_Type(OctetString):
    """Custom type privateVlanPromPortSecondaryRemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PrivateVlanPromPortSecondaryRemap_Type.__name__ = "OctetString"
_PrivateVlanPromPortSecondaryRemap_Object = MibTableColumn
privateVlanPromPortSecondaryRemap = _PrivateVlanPromPortSecondaryRemap_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 6, 1, 3),
    _PrivateVlanPromPortSecondaryRemap_Type()
)
privateVlanPromPortSecondaryRemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPromPortSecondaryRemap.setStatus("current")


class _PrivateVlanPromPortSecondaryRemap2k_Type(OctetString):
    """Custom type privateVlanPromPortSecondaryRemap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PrivateVlanPromPortSecondaryRemap2k_Type.__name__ = "OctetString"
_PrivateVlanPromPortSecondaryRemap2k_Object = MibTableColumn
privateVlanPromPortSecondaryRemap2k = _PrivateVlanPromPortSecondaryRemap2k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 6, 1, 4),
    _PrivateVlanPromPortSecondaryRemap2k_Type()
)
privateVlanPromPortSecondaryRemap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPromPortSecondaryRemap2k.setStatus("current")


class _PrivateVlanPromPortSecondaryRemap3k_Type(OctetString):
    """Custom type privateVlanPromPortSecondaryRemap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PrivateVlanPromPortSecondaryRemap3k_Type.__name__ = "OctetString"
_PrivateVlanPromPortSecondaryRemap3k_Object = MibTableColumn
privateVlanPromPortSecondaryRemap3k = _PrivateVlanPromPortSecondaryRemap3k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 6, 1, 5),
    _PrivateVlanPromPortSecondaryRemap3k_Type()
)
privateVlanPromPortSecondaryRemap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPromPortSecondaryRemap3k.setStatus("current")


class _PrivateVlanPromPortSecondaryRemap4k_Type(OctetString):
    """Custom type privateVlanPromPortSecondaryRemap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PrivateVlanPromPortSecondaryRemap4k_Type.__name__ = "OctetString"
_PrivateVlanPromPortSecondaryRemap4k_Object = MibTableColumn
privateVlanPromPortSecondaryRemap4k = _PrivateVlanPromPortSecondaryRemap4k_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 6, 1, 6),
    _PrivateVlanPromPortSecondaryRemap4k_Type()
)
privateVlanPromPortSecondaryRemap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPromPortSecondaryRemap4k.setStatus("current")
_PrivateVlanSessionTable_Object = MibTable
privateVlanSessionTable = _PrivateVlanSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 8)
)
if mibBuilder.loadTexts:
    privateVlanSessionTable.setStatus("current")
_PrivateVlanSessionEntry_Object = MibTableRow
privateVlanSessionEntry = _PrivateVlanSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 8, 1)
)
privateVlanSessionEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "privateVlanSessionId"),
)
if mibBuilder.loadTexts:
    privateVlanSessionEntry.setStatus("current")


class _PrivateVlanSessionId_Type(Integer32):
    """Custom type privateVlanSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PrivateVlanSessionId_Type.__name__ = "Integer32"
_PrivateVlanSessionId_Object = MibTableColumn
privateVlanSessionId = _PrivateVlanSessionId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 8, 1, 1),
    _PrivateVlanSessionId_Type()
)
privateVlanSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateVlanSessionId.setStatus("current")
_PrivateVlanSessionUplinkPorts_Type = PortList
_PrivateVlanSessionUplinkPorts_Object = MibTableColumn
privateVlanSessionUplinkPorts = _PrivateVlanSessionUplinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 8, 1, 2),
    _PrivateVlanSessionUplinkPorts_Type()
)
privateVlanSessionUplinkPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanSessionUplinkPorts.setStatus("current")
_PrivateVlanSessionDownlinkPorts_Type = PortList
_PrivateVlanSessionDownlinkPorts_Object = MibTableColumn
privateVlanSessionDownlinkPorts = _PrivateVlanSessionDownlinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 8, 1, 3),
    _PrivateVlanSessionDownlinkPorts_Type()
)
privateVlanSessionDownlinkPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanSessionDownlinkPorts.setStatus("current")
_PrivateVlanSessionStatus_Type = ValidStatus
_PrivateVlanSessionStatus_Object = MibTableColumn
privateVlanSessionStatus = _PrivateVlanSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 8, 1, 4),
    _PrivateVlanSessionStatus_Type()
)
privateVlanSessionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanSessionStatus.setStatus("current")


class _PrivateVlanUplinkToUplink_Type(Integer32):
    """Custom type privateVlanUplinkToUplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("forwarding", 2))
    )


_PrivateVlanUplinkToUplink_Type.__name__ = "Integer32"
_PrivateVlanUplinkToUplink_Object = MibScalar
privateVlanUplinkToUplink = _PrivateVlanUplinkToUplink_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 1, 9),
    _PrivateVlanUplinkToUplink_Type()
)
privateVlanUplinkToUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanUplinkToUplink.setStatus("current")
_PortSecurityMgt_ObjectIdentity = ObjectIdentity
portSecurityMgt = _PortSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2)
)
_PortSecPortTable_Object = MibTable
portSecPortTable = _PortSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    portSecPortTable.setStatus("current")
_PortSecPortEntry_Object = MibTableRow
portSecPortEntry = _PortSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2, 1, 1)
)
portSecPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "portSecPortIndex"),
)
if mibBuilder.loadTexts:
    portSecPortEntry.setStatus("current")
_PortSecPortIndex_Type = InterfaceIndex
_PortSecPortIndex_Object = MibTableColumn
portSecPortIndex = _PortSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2, 1, 1, 1),
    _PortSecPortIndex_Type()
)
portSecPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecPortIndex.setStatus("current")
_PortSecPortStatus_Type = EnabledStatus
_PortSecPortStatus_Object = MibTableColumn
portSecPortStatus = _PortSecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2, 1, 1, 3),
    _PortSecAction_Type()
)
portSecAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecAction.setStatus("current")


class _PortSecMaxMacCount_Type(Integer32):
    """Custom type portSecMaxMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PortSecMaxMacCount_Type.__name__ = "Integer32"
_PortSecMaxMacCount_Object = MibTableColumn
portSecMaxMacCount = _PortSecMaxMacCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2, 1, 1, 4),
    _PortSecMaxMacCount_Type()
)
portSecMaxMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMaxMacCount.setStatus("current")
_PortSecMacAsPermanentMgt_ObjectIdentity = ObjectIdentity
portSecMacAsPermanentMgt = _PortSecMacAsPermanentMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2, 6)
)
_PortSecMacAsPermanentPortIndex_Type = Integer32
_PortSecMacAsPermanentPortIndex_Object = MibScalar
portSecMacAsPermanentPortIndex = _PortSecMacAsPermanentPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2, 6, 1),
    _PortSecMacAsPermanentPortIndex_Type()
)
portSecMacAsPermanentPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMacAsPermanentPortIndex.setStatus("current")


class _PortSecMacAsPermanentAction_Type(Integer32):
    """Custom type portSecMacAsPermanentAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("action", 2),
          ("noAction", 1))
    )


_PortSecMacAsPermanentAction_Type.__name__ = "Integer32"
_PortSecMacAsPermanentAction_Object = MibScalar
portSecMacAsPermanentAction = _PortSecMacAsPermanentAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 2, 6, 2),
    _PortSecMacAsPermanentAction_Type()
)
portSecMacAsPermanentAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMacAsPermanentAction.setStatus("current")
_RadiusMgt_ObjectIdentity = ObjectIdentity
radiusMgt = _RadiusMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4)
)


class _RadiusServerGlobalAuthPort_Type(Integer32):
    """Custom type radiusServerGlobalAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerGlobalAuthPort_Type.__name__ = "Integer32"
_RadiusServerGlobalAuthPort_Object = MibScalar
radiusServerGlobalAuthPort = _RadiusServerGlobalAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 1),
    _RadiusServerGlobalAuthPort_Type()
)
radiusServerGlobalAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalAuthPort.setStatus("current")


class _RadiusServerGlobalAcctPort_Type(Integer32):
    """Custom type radiusServerGlobalAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerGlobalAcctPort_Type.__name__ = "Integer32"
_RadiusServerGlobalAcctPort_Object = MibScalar
radiusServerGlobalAcctPort = _RadiusServerGlobalAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 2),
    _RadiusServerGlobalAcctPort_Type()
)
radiusServerGlobalAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalAcctPort.setStatus("current")


class _RadiusServerGlobalKey_Type(DisplayString):
    """Custom type radiusServerGlobalKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RadiusServerGlobalKey_Type.__name__ = "DisplayString"
_RadiusServerGlobalKey_Object = MibScalar
radiusServerGlobalKey = _RadiusServerGlobalKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 3),
    _RadiusServerGlobalKey_Type()
)
radiusServerGlobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalKey.setStatus("current")


class _RadiusServerGlobalRetransmit_Type(Integer32):
    """Custom type radiusServerGlobalRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RadiusServerGlobalRetransmit_Type.__name__ = "Integer32"
_RadiusServerGlobalRetransmit_Object = MibScalar
radiusServerGlobalRetransmit = _RadiusServerGlobalRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 4),
    _RadiusServerGlobalRetransmit_Type()
)
radiusServerGlobalRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalRetransmit.setStatus("current")


class _RadiusServerGlobalTimeout_Type(Integer32):
    """Custom type radiusServerGlobalTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerGlobalTimeout_Type.__name__ = "Integer32"
_RadiusServerGlobalTimeout_Object = MibScalar
radiusServerGlobalTimeout = _RadiusServerGlobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 5),
    _RadiusServerGlobalTimeout_Type()
)
radiusServerGlobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalTimeout.setStatus("current")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("current")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7, 1)
)
radiusServerEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "radiusServerIndex"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("current")


class _RadiusServerIndex_Type(Integer32):
    """Custom type radiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RadiusServerIndex_Type.__name__ = "Integer32"
_RadiusServerIndex_Object = MibTableColumn
radiusServerIndex = _RadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7, 1, 1),
    _RadiusServerIndex_Type()
)
radiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusServerIndex.setStatus("current")
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibTableColumn
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7, 1, 2),
    _RadiusServerAddress_Type()
)
radiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAddress.setStatus("current")


class _RadiusServerAuthPortNumber_Type(Integer32):
    """Custom type radiusServerAuthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerAuthPortNumber_Type.__name__ = "Integer32"
_RadiusServerAuthPortNumber_Object = MibTableColumn
radiusServerAuthPortNumber = _RadiusServerAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7, 1, 3),
    _RadiusServerAuthPortNumber_Type()
)
radiusServerAuthPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAuthPortNumber.setStatus("current")


class _RadiusServerAcctPortNumber_Type(Integer32):
    """Custom type radiusServerAcctPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerAcctPortNumber_Type.__name__ = "Integer32"
_RadiusServerAcctPortNumber_Object = MibTableColumn
radiusServerAcctPortNumber = _RadiusServerAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7, 1, 4),
    _RadiusServerAcctPortNumber_Type()
)
radiusServerAcctPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAcctPortNumber.setStatus("current")


class _RadiusServerKey_Type(DisplayString):
    """Custom type radiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RadiusServerKey_Type.__name__ = "DisplayString"
_RadiusServerKey_Object = MibTableColumn
radiusServerKey = _RadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7, 1, 5),
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
_RadiusServerRetransmit_Object = MibTableColumn
radiusServerRetransmit = _RadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7, 1, 6),
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
_RadiusServerTimeout_Object = MibTableColumn
radiusServerTimeout = _RadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7, 1, 7),
    _RadiusServerTimeout_Type()
)
radiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerTimeout.setStatus("current")
_RadiusServerStatus_Type = ValidStatus
_RadiusServerStatus_Object = MibTableColumn
radiusServerStatus = _RadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 4, 7, 1, 8),
    _RadiusServerStatus_Type()
)
radiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerStatus.setStatus("current")
_TacacsMgt_ObjectIdentity = ObjectIdentity
tacacsMgt = _TacacsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5)
)


class _TacacsPlusServerGlobalPortNumber_Type(Integer32):
    """Custom type tacacsPlusServerGlobalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsPlusServerGlobalPortNumber_Type.__name__ = "Integer32"
_TacacsPlusServerGlobalPortNumber_Object = MibScalar
tacacsPlusServerGlobalPortNumber = _TacacsPlusServerGlobalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5, 2),
    _TacacsPlusServerGlobalPortNumber_Type()
)
tacacsPlusServerGlobalPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalPortNumber.setStatus("current")


class _TacacsPlusServerGlobalKey_Type(DisplayString):
    """Custom type tacacsPlusServerGlobalKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TacacsPlusServerGlobalKey_Type.__name__ = "DisplayString"
_TacacsPlusServerGlobalKey_Object = MibScalar
tacacsPlusServerGlobalKey = _TacacsPlusServerGlobalKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5, 3),
    _TacacsPlusServerGlobalKey_Type()
)
tacacsPlusServerGlobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalKey.setStatus("current")
_TacacsPlusServerTable_Object = MibTable
tacacsPlusServerTable = _TacacsPlusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5, 4)
)
if mibBuilder.loadTexts:
    tacacsPlusServerTable.setStatus("current")
_TacacsPlusServerEntry_Object = MibTableRow
tacacsPlusServerEntry = _TacacsPlusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5, 4, 1)
)
tacacsPlusServerEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "tacacsPlusServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsPlusServerEntry.setStatus("current")


class _TacacsPlusServerIndex_Type(Integer32):
    """Custom type tacacsPlusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TacacsPlusServerIndex_Type.__name__ = "Integer32"
_TacacsPlusServerIndex_Object = MibTableColumn
tacacsPlusServerIndex = _TacacsPlusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5, 4, 1, 1),
    _TacacsPlusServerIndex_Type()
)
tacacsPlusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsPlusServerIndex.setStatus("current")
_TacacsPlusServerAddress_Type = IpAddress
_TacacsPlusServerAddress_Object = MibTableColumn
tacacsPlusServerAddress = _TacacsPlusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5, 4, 1, 2),
    _TacacsPlusServerAddress_Type()
)
tacacsPlusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerAddress.setStatus("current")


class _TacacsPlusServerPortNumber_Type(Integer32):
    """Custom type tacacsPlusServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsPlusServerPortNumber_Type.__name__ = "Integer32"
_TacacsPlusServerPortNumber_Object = MibTableColumn
tacacsPlusServerPortNumber = _TacacsPlusServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5, 4, 1, 3),
    _TacacsPlusServerPortNumber_Type()
)
tacacsPlusServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerPortNumber.setStatus("current")


class _TacacsPlusServerKey_Type(DisplayString):
    """Custom type tacacsPlusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TacacsPlusServerKey_Type.__name__ = "DisplayString"
_TacacsPlusServerKey_Object = MibTableColumn
tacacsPlusServerKey = _TacacsPlusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5, 4, 1, 4),
    _TacacsPlusServerKey_Type()
)
tacacsPlusServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerKey.setStatus("current")
_TacacsPlusServerStatus_Type = ValidStatus
_TacacsPlusServerStatus_Object = MibTableColumn
tacacsPlusServerStatus = _TacacsPlusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 5, 4, 1, 8),
    _TacacsPlusServerStatus_Type()
)
tacacsPlusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerStatus.setStatus("current")
_SshMgt_ObjectIdentity = ObjectIdentity
sshMgt = _SshMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6)
)
_SshServerStatus_Type = EnabledStatus
_SshServerStatus_Object = MibScalar
sshServerStatus = _SshServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 1),
    _SshServerStatus_Type()
)
sshServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerStatus.setStatus("current")
_SshServerMajorVersion_Type = Integer32
_SshServerMajorVersion_Object = MibScalar
sshServerMajorVersion = _SshServerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 2),
    _SshServerMajorVersion_Type()
)
sshServerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMajorVersion.setStatus("current")
_SshServerMinorVersion_Type = Integer32
_SshServerMinorVersion_Object = MibScalar
sshServerMinorVersion = _SshServerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 4),
    _SshTimeout_Type()
)
sshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sshTimeout.setUnits("seconds")


class _SshAuthRetries_Type(Integer32):
    """Custom type sshAuthRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SshAuthRetries_Type.__name__ = "Integer32"
_SshAuthRetries_Object = MibScalar
sshAuthRetries = _SshAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 5),
    _SshAuthRetries_Type()
)
sshAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAuthRetries.setStatus("current")
_SshConnInfoTable_Object = MibTable
sshConnInfoTable = _SshConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 6)
)
if mibBuilder.loadTexts:
    sshConnInfoTable.setStatus("current")
_SshConnInfoEntry_Object = MibTableRow
sshConnInfoEntry = _SshConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 6, 1)
)
sshConnInfoEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "sshConnID"),
)
if mibBuilder.loadTexts:
    sshConnInfoEntry.setStatus("current")


class _SshConnID_Type(Integer32):
    """Custom type sshConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SshConnID_Type.__name__ = "Integer32"
_SshConnID_Object = MibTableColumn
sshConnID = _SshConnID_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 6, 1, 1),
    _SshConnID_Type()
)
sshConnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshConnID.setStatus("current")
_SshConnMajorVersion_Type = Integer32
_SshConnMajorVersion_Object = MibTableColumn
sshConnMajorVersion = _SshConnMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 6, 1, 2),
    _SshConnMajorVersion_Type()
)
sshConnMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMajorVersion.setStatus("current")
_SshConnMinorVersion_Type = Integer32
_SshConnMinorVersion_Object = MibTableColumn
sshConnMinorVersion = _SshConnMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 6, 1, 3),
    _SshConnMinorVersion_Type()
)
sshConnMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMinorVersion.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 6, 1, 5),
    _SshConnStatus_Type()
)
sshConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnStatus.setStatus("current")


class _SshConnUserName_Type(DisplayString):
    """Custom type sshConnUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SshConnUserName_Type.__name__ = "DisplayString"
_SshConnUserName_Object = MibTableColumn
sshConnUserName = _SshConnUserName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 6, 1, 7),
    _SshDisconnect_Type()
)
sshDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshDisconnect.setStatus("current")


class _SshConnEncryptionTypeStr_Type(DisplayString):
    """Custom type sshConnEncryptionTypeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SshConnEncryptionTypeStr_Type.__name__ = "DisplayString"
_SshConnEncryptionTypeStr_Object = MibTableColumn
sshConnEncryptionTypeStr = _SshConnEncryptionTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 6, 1, 8),
    _SshConnEncryptionTypeStr_Type()
)
sshConnEncryptionTypeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnEncryptionTypeStr.setStatus("current")


class _SshKeySize_Type(Integer32):
    """Custom type sshKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 896),
    )


_SshKeySize_Type.__name__ = "Integer32"
_SshKeySize_Object = MibScalar
sshKeySize = _SshKeySize_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 7),
    _SshKeySize_Type()
)
sshKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshKeySize.setStatus("current")
_SshRsaHostKey1_Type = KeySegment
_SshRsaHostKey1_Object = MibScalar
sshRsaHostKey1 = _SshRsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 8),
    _SshRsaHostKey1_Type()
)
sshRsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey1.setStatus("current")
_SshRsaHostKey2_Type = KeySegment
_SshRsaHostKey2_Object = MibScalar
sshRsaHostKey2 = _SshRsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 9),
    _SshRsaHostKey2_Type()
)
sshRsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey2.setStatus("current")
_SshRsaHostKey3_Type = KeySegment
_SshRsaHostKey3_Object = MibScalar
sshRsaHostKey3 = _SshRsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 10),
    _SshRsaHostKey3_Type()
)
sshRsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey3.setStatus("current")
_SshRsaHostKey4_Type = KeySegment
_SshRsaHostKey4_Object = MibScalar
sshRsaHostKey4 = _SshRsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 11),
    _SshRsaHostKey4_Type()
)
sshRsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey4.setStatus("current")
_SshRsaHostKey5_Type = KeySegment
_SshRsaHostKey5_Object = MibScalar
sshRsaHostKey5 = _SshRsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 12),
    _SshRsaHostKey5_Type()
)
sshRsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey5.setStatus("current")
_SshRsaHostKey6_Type = KeySegment
_SshRsaHostKey6_Object = MibScalar
sshRsaHostKey6 = _SshRsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 13),
    _SshRsaHostKey6_Type()
)
sshRsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey6.setStatus("current")
_SshRsaHostKey7_Type = KeySegment
_SshRsaHostKey7_Object = MibScalar
sshRsaHostKey7 = _SshRsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 14),
    _SshRsaHostKey7_Type()
)
sshRsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey7.setStatus("current")
_SshRsaHostKey8_Type = KeySegment
_SshRsaHostKey8_Object = MibScalar
sshRsaHostKey8 = _SshRsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 15),
    _SshRsaHostKey8_Type()
)
sshRsaHostKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey8.setStatus("current")
_SshDsaHostKey1_Type = KeySegment
_SshDsaHostKey1_Object = MibScalar
sshDsaHostKey1 = _SshDsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 16),
    _SshDsaHostKey1_Type()
)
sshDsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey1.setStatus("current")
_SshDsaHostKey2_Type = KeySegment
_SshDsaHostKey2_Object = MibScalar
sshDsaHostKey2 = _SshDsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 17),
    _SshDsaHostKey2_Type()
)
sshDsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey2.setStatus("current")
_SshDsaHostKey3_Type = KeySegment
_SshDsaHostKey3_Object = MibScalar
sshDsaHostKey3 = _SshDsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 18),
    _SshDsaHostKey3_Type()
)
sshDsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey3.setStatus("current")
_SshDsaHostKey4_Type = KeySegment
_SshDsaHostKey4_Object = MibScalar
sshDsaHostKey4 = _SshDsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 19),
    _SshDsaHostKey4_Type()
)
sshDsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey4.setStatus("current")
_SshDsaHostKey5_Type = KeySegment
_SshDsaHostKey5_Object = MibScalar
sshDsaHostKey5 = _SshDsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 20),
    _SshDsaHostKey5_Type()
)
sshDsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey5.setStatus("current")
_SshDsaHostKey6_Type = KeySegment
_SshDsaHostKey6_Object = MibScalar
sshDsaHostKey6 = _SshDsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 21),
    _SshDsaHostKey6_Type()
)
sshDsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey6.setStatus("current")
_SshDsaHostKey7_Type = KeySegment
_SshDsaHostKey7_Object = MibScalar
sshDsaHostKey7 = _SshDsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 22),
    _SshDsaHostKey7_Type()
)
sshDsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey7.setStatus("current")
_SshDsaHostKey8_Type = KeySegment
_SshDsaHostKey8_Object = MibScalar
sshDsaHostKey8 = _SshDsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 23),
    _SshDsaHostKey8_Type()
)
sshDsaHostKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey8.setStatus("current")


class _SshHostKeyGenAction_Type(Integer32):
    """Custom type sshHostKeyGenAction based on Integer32"""
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
        *(("genBothKeys", 4),
          ("genDsaKey", 3),
          ("genRsaKey", 2),
          ("noGen", 1))
    )


_SshHostKeyGenAction_Type.__name__ = "Integer32"
_SshHostKeyGenAction_Object = MibScalar
sshHostKeyGenAction = _SshHostKeyGenAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 24),
    _SshHostKeyGenAction_Type()
)
sshHostKeyGenAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyGenAction.setStatus("current")


class _SshHostKeyGenStatus_Type(Integer32):
    """Custom type sshHostKeyGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("success", 2),
          ("unknown", 1))
    )


_SshHostKeyGenStatus_Type.__name__ = "Integer32"
_SshHostKeyGenStatus_Object = MibScalar
sshHostKeyGenStatus = _SshHostKeyGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 25),
    _SshHostKeyGenStatus_Type()
)
sshHostKeyGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshHostKeyGenStatus.setStatus("current")


class _SshHostKeySaveAction_Type(Integer32):
    """Custom type sshHostKeySaveAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSave", 1),
          ("save", 2))
    )


_SshHostKeySaveAction_Type.__name__ = "Integer32"
_SshHostKeySaveAction_Object = MibScalar
sshHostKeySaveAction = _SshHostKeySaveAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 26),
    _SshHostKeySaveAction_Type()
)
sshHostKeySaveAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeySaveAction.setStatus("current")


class _SshHostKeySaveStatus_Type(Integer32):
    """Custom type sshHostKeySaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("success", 2),
          ("unknown", 1))
    )


_SshHostKeySaveStatus_Type.__name__ = "Integer32"
_SshHostKeySaveStatus_Object = MibScalar
sshHostKeySaveStatus = _SshHostKeySaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 27),
    _SshHostKeySaveStatus_Type()
)
sshHostKeySaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshHostKeySaveStatus.setStatus("current")


class _SshHostKeyDelAction_Type(Integer32):
    """Custom type sshHostKeyDelAction based on Integer32"""
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
        *(("delBothKeys", 4),
          ("delDsaKey", 3),
          ("delRsaKey", 2),
          ("noDel", 1))
    )


_SshHostKeyDelAction_Type.__name__ = "Integer32"
_SshHostKeyDelAction_Object = MibScalar
sshHostKeyDelAction = _SshHostKeyDelAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 28),
    _SshHostKeyDelAction_Type()
)
sshHostKeyDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyDelAction.setStatus("current")
_SshUserTable_Object = MibTable
sshUserTable = _SshUserTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29)
)
if mibBuilder.loadTexts:
    sshUserTable.setStatus("current")
_SshUserEntry_Object = MibTableRow
sshUserEntry = _SshUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1)
)
sshUserEntry.setIndexNames(
    (1, "ECS2100-28PP-MIB", "sshUserName"),
)
if mibBuilder.loadTexts:
    sshUserEntry.setStatus("current")


class _SshUserName_Type(DisplayString):
    """Custom type sshUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SshUserName_Type.__name__ = "DisplayString"
_SshUserName_Object = MibTableColumn
sshUserName = _SshUserName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 1),
    _SshUserName_Type()
)
sshUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshUserName.setStatus("current")
_SshUserRsaKey1_Type = KeySegment
_SshUserRsaKey1_Object = MibTableColumn
sshUserRsaKey1 = _SshUserRsaKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 2),
    _SshUserRsaKey1_Type()
)
sshUserRsaKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey1.setStatus("current")
_SshUserRsaKey2_Type = KeySegment
_SshUserRsaKey2_Object = MibTableColumn
sshUserRsaKey2 = _SshUserRsaKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 3),
    _SshUserRsaKey2_Type()
)
sshUserRsaKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey2.setStatus("current")
_SshUserRsaKey3_Type = KeySegment
_SshUserRsaKey3_Object = MibTableColumn
sshUserRsaKey3 = _SshUserRsaKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 4),
    _SshUserRsaKey3_Type()
)
sshUserRsaKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey3.setStatus("current")
_SshUserRsaKey4_Type = KeySegment
_SshUserRsaKey4_Object = MibTableColumn
sshUserRsaKey4 = _SshUserRsaKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 5),
    _SshUserRsaKey4_Type()
)
sshUserRsaKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey4.setStatus("current")
_SshUserRsaKey5_Type = KeySegment
_SshUserRsaKey5_Object = MibTableColumn
sshUserRsaKey5 = _SshUserRsaKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 6),
    _SshUserRsaKey5_Type()
)
sshUserRsaKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey5.setStatus("current")
_SshUserRsaKey6_Type = KeySegment
_SshUserRsaKey6_Object = MibTableColumn
sshUserRsaKey6 = _SshUserRsaKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 7),
    _SshUserRsaKey6_Type()
)
sshUserRsaKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey6.setStatus("current")
_SshUserRsaKey7_Type = KeySegment
_SshUserRsaKey7_Object = MibTableColumn
sshUserRsaKey7 = _SshUserRsaKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 8),
    _SshUserRsaKey7_Type()
)
sshUserRsaKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey7.setStatus("current")
_SshUserRsaKey8_Type = KeySegment
_SshUserRsaKey8_Object = MibTableColumn
sshUserRsaKey8 = _SshUserRsaKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 9),
    _SshUserRsaKey8_Type()
)
sshUserRsaKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey8.setStatus("current")
_SshUserDsaKey1_Type = KeySegment
_SshUserDsaKey1_Object = MibTableColumn
sshUserDsaKey1 = _SshUserDsaKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 10),
    _SshUserDsaKey1_Type()
)
sshUserDsaKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey1.setStatus("current")
_SshUserDsaKey2_Type = KeySegment
_SshUserDsaKey2_Object = MibTableColumn
sshUserDsaKey2 = _SshUserDsaKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 11),
    _SshUserDsaKey2_Type()
)
sshUserDsaKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey2.setStatus("current")
_SshUserDsaKey3_Type = KeySegment
_SshUserDsaKey3_Object = MibTableColumn
sshUserDsaKey3 = _SshUserDsaKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 12),
    _SshUserDsaKey3_Type()
)
sshUserDsaKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey3.setStatus("current")
_SshUserDsaKey4_Type = KeySegment
_SshUserDsaKey4_Object = MibTableColumn
sshUserDsaKey4 = _SshUserDsaKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 13),
    _SshUserDsaKey4_Type()
)
sshUserDsaKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey4.setStatus("current")
_SshUserDsaKey5_Type = KeySegment
_SshUserDsaKey5_Object = MibTableColumn
sshUserDsaKey5 = _SshUserDsaKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 14),
    _SshUserDsaKey5_Type()
)
sshUserDsaKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey5.setStatus("current")
_SshUserDsaKey6_Type = KeySegment
_SshUserDsaKey6_Object = MibTableColumn
sshUserDsaKey6 = _SshUserDsaKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 15),
    _SshUserDsaKey6_Type()
)
sshUserDsaKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey6.setStatus("current")
_SshUserDsaKey7_Type = KeySegment
_SshUserDsaKey7_Object = MibTableColumn
sshUserDsaKey7 = _SshUserDsaKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 16),
    _SshUserDsaKey7_Type()
)
sshUserDsaKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey7.setStatus("current")
_SshUserDsaKey8_Type = KeySegment
_SshUserDsaKey8_Object = MibTableColumn
sshUserDsaKey8 = _SshUserDsaKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 17),
    _SshUserDsaKey8_Type()
)
sshUserDsaKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey8.setStatus("current")


class _SshUserKeyDelAction_Type(Integer32):
    """Custom type sshUserKeyDelAction based on Integer32"""
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
        *(("delBothKeys", 4),
          ("delDsaKey", 3),
          ("delRsaKey", 2),
          ("noDel", 1))
    )


_SshUserKeyDelAction_Type.__name__ = "Integer32"
_SshUserKeyDelAction_Object = MibTableColumn
sshUserKeyDelAction = _SshUserKeyDelAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 29, 1, 18),
    _SshUserKeyDelAction_Type()
)
sshUserKeyDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserKeyDelAction.setStatus("current")


class _SshRsaHostKeySHA1FingerPrint_Type(DisplayString):
    """Custom type sshRsaHostKeySHA1FingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(65, 65),
    )


_SshRsaHostKeySHA1FingerPrint_Type.__name__ = "DisplayString"
_SshRsaHostKeySHA1FingerPrint_Object = MibScalar
sshRsaHostKeySHA1FingerPrint = _SshRsaHostKeySHA1FingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 30),
    _SshRsaHostKeySHA1FingerPrint_Type()
)
sshRsaHostKeySHA1FingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKeySHA1FingerPrint.setStatus("current")


class _SshRsaHostKeyMD5FingerPrint_Type(DisplayString):
    """Custom type sshRsaHostKeyMD5FingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(47, 47),
    )


_SshRsaHostKeyMD5FingerPrint_Type.__name__ = "DisplayString"
_SshRsaHostKeyMD5FingerPrint_Object = MibScalar
sshRsaHostKeyMD5FingerPrint = _SshRsaHostKeyMD5FingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 31),
    _SshRsaHostKeyMD5FingerPrint_Type()
)
sshRsaHostKeyMD5FingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKeyMD5FingerPrint.setStatus("current")


class _SshDsaHostKeySHA1FingerPrint_Type(DisplayString):
    """Custom type sshDsaHostKeySHA1FingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(65, 65),
    )


_SshDsaHostKeySHA1FingerPrint_Type.__name__ = "DisplayString"
_SshDsaHostKeySHA1FingerPrint_Object = MibScalar
sshDsaHostKeySHA1FingerPrint = _SshDsaHostKeySHA1FingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 32),
    _SshDsaHostKeySHA1FingerPrint_Type()
)
sshDsaHostKeySHA1FingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKeySHA1FingerPrint.setStatus("current")


class _SshDsaHostKeyMD5FingerPrint_Type(DisplayString):
    """Custom type sshDsaHostKeyMD5FingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(47, 47),
    )


_SshDsaHostKeyMD5FingerPrint_Type.__name__ = "DisplayString"
_SshDsaHostKeyMD5FingerPrint_Object = MibScalar
sshDsaHostKeyMD5FingerPrint = _SshDsaHostKeyMD5FingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 6, 33),
    _SshDsaHostKeyMD5FingerPrint_Type()
)
sshDsaHostKeyMD5FingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKeyMD5FingerPrint.setStatus("current")
_IpFilterMgt_ObjectIdentity = ObjectIdentity
ipFilterMgt = _IpFilterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9)
)
_IpFilterSnmpInetTable_Object = MibTable
ipFilterSnmpInetTable = _IpFilterSnmpInetTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 12)
)
if mibBuilder.loadTexts:
    ipFilterSnmpInetTable.setStatus("current")
_IpFilterSnmpInetEntry_Object = MibTableRow
ipFilterSnmpInetEntry = _IpFilterSnmpInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 12, 1)
)
ipFilterSnmpInetEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "ipFilterSnmpInetAddressType"),
    (1, "ECS2100-28PP-MIB", "ipFilterSnmpInetAddressStart"),
)
if mibBuilder.loadTexts:
    ipFilterSnmpInetEntry.setStatus("current")
_IpFilterSnmpInetAddressType_Type = InetAddressType
_IpFilterSnmpInetAddressType_Object = MibTableColumn
ipFilterSnmpInetAddressType = _IpFilterSnmpInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 12, 1, 1),
    _IpFilterSnmpInetAddressType_Type()
)
ipFilterSnmpInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSnmpInetAddressType.setStatus("current")
_IpFilterSnmpInetAddressStart_Type = InetAddress
_IpFilterSnmpInetAddressStart_Object = MibTableColumn
ipFilterSnmpInetAddressStart = _IpFilterSnmpInetAddressStart_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 12, 1, 2),
    _IpFilterSnmpInetAddressStart_Type()
)
ipFilterSnmpInetAddressStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSnmpInetAddressStart.setStatus("current")
_IpFilterSnmpInetAddressEnd_Type = InetAddress
_IpFilterSnmpInetAddressEnd_Object = MibTableColumn
ipFilterSnmpInetAddressEnd = _IpFilterSnmpInetAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 12, 1, 3),
    _IpFilterSnmpInetAddressEnd_Type()
)
ipFilterSnmpInetAddressEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpInetAddressEnd.setStatus("current")
_IpFilterSnmpInetStatus_Type = ValidStatus
_IpFilterSnmpInetStatus_Object = MibTableColumn
ipFilterSnmpInetStatus = _IpFilterSnmpInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 12, 1, 4),
    _IpFilterSnmpInetStatus_Type()
)
ipFilterSnmpInetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpInetStatus.setStatus("current")
_IpFilterHttpInetTable_Object = MibTable
ipFilterHttpInetTable = _IpFilterHttpInetTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 13)
)
if mibBuilder.loadTexts:
    ipFilterHttpInetTable.setStatus("current")
_IpFilterHttpInetEntry_Object = MibTableRow
ipFilterHttpInetEntry = _IpFilterHttpInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 13, 1)
)
ipFilterHttpInetEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "ipFilterHttpInetAddressType"),
    (1, "ECS2100-28PP-MIB", "ipFilterHttpInetAddressStart"),
)
if mibBuilder.loadTexts:
    ipFilterHttpInetEntry.setStatus("current")
_IpFilterHttpInetAddressType_Type = InetAddressType
_IpFilterHttpInetAddressType_Object = MibTableColumn
ipFilterHttpInetAddressType = _IpFilterHttpInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 13, 1, 1),
    _IpFilterHttpInetAddressType_Type()
)
ipFilterHttpInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterHttpInetAddressType.setStatus("current")
_IpFilterHttpInetAddressStart_Type = InetAddress
_IpFilterHttpInetAddressStart_Object = MibTableColumn
ipFilterHttpInetAddressStart = _IpFilterHttpInetAddressStart_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 13, 1, 2),
    _IpFilterHttpInetAddressStart_Type()
)
ipFilterHttpInetAddressStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterHttpInetAddressStart.setStatus("current")
_IpFilterHttpInetAddressEnd_Type = InetAddress
_IpFilterHttpInetAddressEnd_Object = MibTableColumn
ipFilterHttpInetAddressEnd = _IpFilterHttpInetAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 13, 1, 3),
    _IpFilterHttpInetAddressEnd_Type()
)
ipFilterHttpInetAddressEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHttpInetAddressEnd.setStatus("current")
_IpFilterHttpInetStatus_Type = ValidStatus
_IpFilterHttpInetStatus_Object = MibTableColumn
ipFilterHttpInetStatus = _IpFilterHttpInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 13, 1, 4),
    _IpFilterHttpInetStatus_Type()
)
ipFilterHttpInetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHttpInetStatus.setStatus("current")
_IpFilterTelnetInetTable_Object = MibTable
ipFilterTelnetInetTable = _IpFilterTelnetInetTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 14)
)
if mibBuilder.loadTexts:
    ipFilterTelnetInetTable.setStatus("current")
_IpFilterTelnetInetEntry_Object = MibTableRow
ipFilterTelnetInetEntry = _IpFilterTelnetInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 14, 1)
)
ipFilterTelnetInetEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "ipFilterTelnetInetAddressType"),
    (1, "ECS2100-28PP-MIB", "ipFilterTelnetInetAddressStart"),
)
if mibBuilder.loadTexts:
    ipFilterTelnetInetEntry.setStatus("current")
_IpFilterTelnetInetAddressType_Type = InetAddressType
_IpFilterTelnetInetAddressType_Object = MibTableColumn
ipFilterTelnetInetAddressType = _IpFilterTelnetInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 14, 1, 1),
    _IpFilterTelnetInetAddressType_Type()
)
ipFilterTelnetInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterTelnetInetAddressType.setStatus("current")
_IpFilterTelnetInetAddressStart_Type = InetAddress
_IpFilterTelnetInetAddressStart_Object = MibTableColumn
ipFilterTelnetInetAddressStart = _IpFilterTelnetInetAddressStart_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 14, 1, 2),
    _IpFilterTelnetInetAddressStart_Type()
)
ipFilterTelnetInetAddressStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterTelnetInetAddressStart.setStatus("current")
_IpFilterTelnetInetAddressEnd_Type = InetAddress
_IpFilterTelnetInetAddressEnd_Object = MibTableColumn
ipFilterTelnetInetAddressEnd = _IpFilterTelnetInetAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 14, 1, 3),
    _IpFilterTelnetInetAddressEnd_Type()
)
ipFilterTelnetInetAddressEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetInetAddressEnd.setStatus("current")
_IpFilterTelnetInetStatus_Type = ValidStatus
_IpFilterTelnetInetStatus_Object = MibTableColumn
ipFilterTelnetInetStatus = _IpFilterTelnetInetStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 14, 1, 4),
    _IpFilterTelnetInetStatus_Type()
)
ipFilterTelnetInetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetInetStatus.setStatus("current")
_IpFilterAllClientCtl_ObjectIdentity = ObjectIdentity
ipFilterAllClientCtl = _IpFilterAllClientCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 15)
)
_IpFilterAllClientCtlInetAddressType_Type = InetAddressType
_IpFilterAllClientCtlInetAddressType_Object = MibScalar
ipFilterAllClientCtlInetAddressType = _IpFilterAllClientCtlInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 15, 1),
    _IpFilterAllClientCtlInetAddressType_Type()
)
ipFilterAllClientCtlInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterAllClientCtlInetAddressType.setStatus("current")
_IpFilterAllClientCtlInetAddressStart_Type = InetAddress
_IpFilterAllClientCtlInetAddressStart_Object = MibScalar
ipFilterAllClientCtlInetAddressStart = _IpFilterAllClientCtlInetAddressStart_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 15, 2),
    _IpFilterAllClientCtlInetAddressStart_Type()
)
ipFilterAllClientCtlInetAddressStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterAllClientCtlInetAddressStart.setStatus("current")
_IpFilterAllClientCtlInetAddressEnd_Type = InetAddress
_IpFilterAllClientCtlInetAddressEnd_Object = MibScalar
ipFilterAllClientCtlInetAddressEnd = _IpFilterAllClientCtlInetAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 15, 3),
    _IpFilterAllClientCtlInetAddressEnd_Type()
)
ipFilterAllClientCtlInetAddressEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterAllClientCtlInetAddressEnd.setStatus("current")


class _IpFilterAllClientCtlAction_Type(Integer32):
    """Custom type ipFilterAllClientCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("destroy", 3),
          ("noAction", 1))
    )


_IpFilterAllClientCtlAction_Type.__name__ = "Integer32"
_IpFilterAllClientCtlAction_Object = MibScalar
ipFilterAllClientCtlAction = _IpFilterAllClientCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 9, 15, 4),
    _IpFilterAllClientCtlAction_Type()
)
ipFilterAllClientCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFilterAllClientCtlAction.setStatus("current")
_UserAuthMgt_ObjectIdentity = ObjectIdentity
userAuthMgt = _UserAuthMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10)
)


class _UserAuthEnablePassword_Type(DisplayString):
    """Custom type userAuthEnablePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserAuthEnablePassword_Type.__name__ = "DisplayString"
_UserAuthEnablePassword_Object = MibScalar
userAuthEnablePassword = _UserAuthEnablePassword_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10, 3),
    _UserAuthEnablePassword_Type()
)
userAuthEnablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthEnablePassword.setStatus("current")


class _UserAuthMethod_Type(Integer32):
    """Custom type userAuthMethod based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("localradius", 2),
          ("localradiustacacs", 3),
          ("localtacacs", 4),
          ("localtacacsradius", 5),
          ("radius", 6),
          ("radiuslocal", 7),
          ("radiuslocaltacacs", 8),
          ("radiustacacs", 9),
          ("radiustacacslocal", 10),
          ("tacacs", 11),
          ("tacacslocal", 12),
          ("tacacslocalradius", 13),
          ("tacacsradius", 14),
          ("tacacsradiuslocal", 15))
    )


_UserAuthMethod_Type.__name__ = "Integer32"
_UserAuthMethod_Object = MibScalar
userAuthMethod = _UserAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10, 4),
    _UserAuthMethod_Type()
)
userAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAuthMethod.setStatus("current")
_UserAuthTable_Object = MibTable
userAuthTable = _UserAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10, 5)
)
if mibBuilder.loadTexts:
    userAuthTable.setStatus("current")
_UserAuthEntry_Object = MibTableRow
userAuthEntry = _UserAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10, 5, 1)
)
userAuthEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "userAuthUserName"),
)
if mibBuilder.loadTexts:
    userAuthEntry.setStatus("current")


class _UserAuthUserName_Type(DisplayString):
    """Custom type userAuthUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UserAuthUserName_Type.__name__ = "DisplayString"
_UserAuthUserName_Object = MibTableColumn
userAuthUserName = _UserAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10, 5, 1, 1),
    _UserAuthUserName_Type()
)
userAuthUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    userAuthUserName.setStatus("current")


class _UserAuthPassword_Type(DisplayString):
    """Custom type userAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UserAuthPassword_Type.__name__ = "DisplayString"
_UserAuthPassword_Object = MibTableColumn
userAuthPassword = _UserAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10, 5, 1, 2),
    _UserAuthPassword_Type()
)
userAuthPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthPassword.setStatus("current")


class _UserAuthPrivilege_Type(Integer32):
    """Custom type userAuthPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_UserAuthPrivilege_Type.__name__ = "Integer32"
_UserAuthPrivilege_Object = MibTableColumn
userAuthPrivilege = _UserAuthPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10, 5, 1, 3),
    _UserAuthPrivilege_Type()
)
userAuthPrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthPrivilege.setStatus("current")
_UserAuthPublicKey_Type = DisplayString
_UserAuthPublicKey_Object = MibTableColumn
userAuthPublicKey = _UserAuthPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10, 5, 1, 4),
    _UserAuthPublicKey_Type()
)
userAuthPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAuthPublicKey.setStatus("current")


class _UserAuthStatus_Type(Integer32):
    """Custom type userAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UserAuthStatus_Type.__name__ = "Integer32"
_UserAuthStatus_Object = MibTableColumn
userAuthStatus = _UserAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 10, 5, 1, 5),
    _UserAuthStatus_Type()
)
userAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userAuthStatus.setStatus("current")
_Dot1xMgt_ObjectIdentity = ObjectIdentity
dot1xMgt = _Dot1xMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 11)
)
_Dot1xAuthConfigExtTable_Object = MibTable
dot1xAuthConfigExtTable = _Dot1xAuthConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 11, 1)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigExtTable.setStatus("current")
_Dot1xAuthConfigExtEntry_Object = MibTableRow
dot1xAuthConfigExtEntry = _Dot1xAuthConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 11, 1, 1)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigExtEntry.setStatus("current")


class _Dot1xAuthConfigExtOperMode_Type(Integer32):
    """Custom type dot1xAuthConfigExtOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macBasedAuth", 3),
          ("multiHost", 2),
          ("singleHost", 1))
    )


_Dot1xAuthConfigExtOperMode_Type.__name__ = "Integer32"
_Dot1xAuthConfigExtOperMode_Object = MibTableColumn
dot1xAuthConfigExtOperMode = _Dot1xAuthConfigExtOperMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 11, 1, 1, 1),
    _Dot1xAuthConfigExtOperMode_Type()
)
dot1xAuthConfigExtOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthConfigExtOperMode.setStatus("current")


class _Dot1xAuthConfigExtMultiHostMaxCnt_Type(Integer32):
    """Custom type dot1xAuthConfigExtMultiHostMaxCnt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Dot1xAuthConfigExtMultiHostMaxCnt_Type.__name__ = "Integer32"
_Dot1xAuthConfigExtMultiHostMaxCnt_Object = MibTableColumn
dot1xAuthConfigExtMultiHostMaxCnt = _Dot1xAuthConfigExtMultiHostMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 11, 1, 1, 2),
    _Dot1xAuthConfigExtMultiHostMaxCnt_Type()
)
dot1xAuthConfigExtMultiHostMaxCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthConfigExtMultiHostMaxCnt.setStatus("current")


class _Dot1xAuthConfigExtPortIntrusionAction_Type(Integer32):
    """Custom type dot1xAuthConfigExtPortIntrusionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block-traffic", 1),
          ("guest-vlan", 2))
    )


_Dot1xAuthConfigExtPortIntrusionAction_Type.__name__ = "Integer32"
_Dot1xAuthConfigExtPortIntrusionAction_Object = MibTableColumn
dot1xAuthConfigExtPortIntrusionAction = _Dot1xAuthConfigExtPortIntrusionAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 11, 1, 1, 3),
    _Dot1xAuthConfigExtPortIntrusionAction_Type()
)
dot1xAuthConfigExtPortIntrusionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthConfigExtPortIntrusionAction.setStatus("current")
_AaaMgt_ObjectIdentity = ObjectIdentity
aaaMgt = _AaaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12)
)
_AaaMethodTable_Object = MibTable
aaaMethodTable = _AaaMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 1)
)
if mibBuilder.loadTexts:
    aaaMethodTable.setStatus("current")
_AaaMethodEntry_Object = MibTableRow
aaaMethodEntry = _AaaMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 1, 1)
)
aaaMethodEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "aaaMethodIndex"),
)
if mibBuilder.loadTexts:
    aaaMethodEntry.setStatus("current")


class _AaaMethodIndex_Type(Integer32):
    """Custom type aaaMethodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AaaMethodIndex_Type.__name__ = "Integer32"
_AaaMethodIndex_Object = MibTableColumn
aaaMethodIndex = _AaaMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 1, 1, 1),
    _AaaMethodIndex_Type()
)
aaaMethodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaMethodIndex.setStatus("current")


class _AaaMethodName_Type(DisplayString):
    """Custom type aaaMethodName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AaaMethodName_Type.__name__ = "DisplayString"
_AaaMethodName_Object = MibTableColumn
aaaMethodName = _AaaMethodName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 1, 1, 2),
    _AaaMethodName_Type()
)
aaaMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodName.setStatus("current")


class _AaaMethodGroupName_Type(DisplayString):
    """Custom type aaaMethodGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AaaMethodGroupName_Type.__name__ = "DisplayString"
_AaaMethodGroupName_Object = MibTableColumn
aaaMethodGroupName = _AaaMethodGroupName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 1, 1, 3),
    _AaaMethodGroupName_Type()
)
aaaMethodGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodGroupName.setStatus("current")


class _AaaMethodMode_Type(Integer32):
    """Custom type aaaMethodMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start-stop", 1)
    )


_AaaMethodMode_Type.__name__ = "Integer32"
_AaaMethodMode_Object = MibTableColumn
aaaMethodMode = _AaaMethodMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 1, 1, 4),
    _AaaMethodMode_Type()
)
aaaMethodMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodMode.setStatus("current")
_AaaMethodStatus_Type = ValidStatus
_AaaMethodStatus_Object = MibTableColumn
aaaMethodStatus = _AaaMethodStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 1, 1, 5),
    _AaaMethodStatus_Type()
)
aaaMethodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodStatus.setStatus("current")


class _AaaMethodClientType_Type(Integer32):
    """Custom type aaaMethodClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commands", 3),
          ("dot1x", 1),
          ("exec", 2))
    )


_AaaMethodClientType_Type.__name__ = "Integer32"
_AaaMethodClientType_Object = MibTableColumn
aaaMethodClientType = _AaaMethodClientType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 1, 1, 6),
    _AaaMethodClientType_Type()
)
aaaMethodClientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodClientType.setStatus("current")


class _AaaMethodPrivilegeLevel_Type(Integer32):
    """Custom type aaaMethodPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AaaMethodPrivilegeLevel_Type.__name__ = "Integer32"
_AaaMethodPrivilegeLevel_Object = MibTableColumn
aaaMethodPrivilegeLevel = _AaaMethodPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 1, 1, 7),
    _AaaMethodPrivilegeLevel_Type()
)
aaaMethodPrivilegeLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodPrivilegeLevel.setStatus("current")
_AaaRadiusGroupTable_Object = MibTable
aaaRadiusGroupTable = _AaaRadiusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 2)
)
if mibBuilder.loadTexts:
    aaaRadiusGroupTable.setStatus("current")
_AaaRadiusGroupEntry_Object = MibTableRow
aaaRadiusGroupEntry = _AaaRadiusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 2, 1)
)
aaaRadiusGroupEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "aaaRadiusGroupIndex"),
)
if mibBuilder.loadTexts:
    aaaRadiusGroupEntry.setStatus("current")


class _AaaRadiusGroupIndex_Type(Integer32):
    """Custom type aaaRadiusGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AaaRadiusGroupIndex_Type.__name__ = "Integer32"
_AaaRadiusGroupIndex_Object = MibTableColumn
aaaRadiusGroupIndex = _AaaRadiusGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 2, 1, 1),
    _AaaRadiusGroupIndex_Type()
)
aaaRadiusGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaRadiusGroupIndex.setStatus("current")


class _AaaRadiusGroupServerBitMap_Type(OctetString):
    """Custom type aaaRadiusGroupServerBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AaaRadiusGroupServerBitMap_Type.__name__ = "OctetString"
_AaaRadiusGroupServerBitMap_Object = MibTableColumn
aaaRadiusGroupServerBitMap = _AaaRadiusGroupServerBitMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 2, 1, 2),
    _AaaRadiusGroupServerBitMap_Type()
)
aaaRadiusGroupServerBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaRadiusGroupServerBitMap.setStatus("current")
_AaaRadiusGroupName_Type = DisplayString
_AaaRadiusGroupName_Object = MibTableColumn
aaaRadiusGroupName = _AaaRadiusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 2, 1, 3),
    _AaaRadiusGroupName_Type()
)
aaaRadiusGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaRadiusGroupName.setStatus("current")
_AaaRadiusGroupStatus_Type = ValidStatus
_AaaRadiusGroupStatus_Object = MibTableColumn
aaaRadiusGroupStatus = _AaaRadiusGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 2, 1, 4),
    _AaaRadiusGroupStatus_Type()
)
aaaRadiusGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaRadiusGroupStatus.setStatus("current")
_AaaTacacsPlusGroupTable_Object = MibTable
aaaTacacsPlusGroupTable = _AaaTacacsPlusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 3)
)
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupTable.setStatus("current")
_AaaTacacsPlusGroupEntry_Object = MibTableRow
aaaTacacsPlusGroupEntry = _AaaTacacsPlusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 3, 1)
)
aaaTacacsPlusGroupEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "aaaTacacsPlusGroupIndex"),
)
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupEntry.setStatus("current")


class _AaaTacacsPlusGroupIndex_Type(Integer32):
    """Custom type aaaTacacsPlusGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AaaTacacsPlusGroupIndex_Type.__name__ = "Integer32"
_AaaTacacsPlusGroupIndex_Object = MibTableColumn
aaaTacacsPlusGroupIndex = _AaaTacacsPlusGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 3, 1, 1),
    _AaaTacacsPlusGroupIndex_Type()
)
aaaTacacsPlusGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupIndex.setStatus("current")


class _AaaTacacsPlusGroupServerBitMap_Type(OctetString):
    """Custom type aaaTacacsPlusGroupServerBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AaaTacacsPlusGroupServerBitMap_Type.__name__ = "OctetString"
_AaaTacacsPlusGroupServerBitMap_Object = MibTableColumn
aaaTacacsPlusGroupServerBitMap = _AaaTacacsPlusGroupServerBitMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 3, 1, 2),
    _AaaTacacsPlusGroupServerBitMap_Type()
)
aaaTacacsPlusGroupServerBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupServerBitMap.setStatus("current")
_AaaTacacsPlusGroupName_Type = DisplayString
_AaaTacacsPlusGroupName_Object = MibTableColumn
aaaTacacsPlusGroupName = _AaaTacacsPlusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 3, 1, 3),
    _AaaTacacsPlusGroupName_Type()
)
aaaTacacsPlusGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupName.setStatus("current")
_AaaTacacsPlusGroupStatus_Type = ValidStatus
_AaaTacacsPlusGroupStatus_Object = MibTableColumn
aaaTacacsPlusGroupStatus = _AaaTacacsPlusGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 3, 1, 4),
    _AaaTacacsPlusGroupStatus_Type()
)
aaaTacacsPlusGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupStatus.setStatus("current")


class _AaaUpdate_Type(Integer32):
    """Custom type aaaUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AaaUpdate_Type.__name__ = "Integer32"
_AaaUpdate_Object = MibScalar
aaaUpdate = _AaaUpdate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 4),
    _AaaUpdate_Type()
)
aaaUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaUpdate.setStatus("current")
_AaaAccountTable_Object = MibTable
aaaAccountTable = _AaaAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 5)
)
if mibBuilder.loadTexts:
    aaaAccountTable.setStatus("current")
_AaaAccountEntry_Object = MibTableRow
aaaAccountEntry = _AaaAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 5, 1)
)
aaaAccountEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "aaaAccountIfIndex"),
)
if mibBuilder.loadTexts:
    aaaAccountEntry.setStatus("current")
_AaaAccountIfIndex_Type = InterfaceIndex
_AaaAccountIfIndex_Object = MibTableColumn
aaaAccountIfIndex = _AaaAccountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 5, 1, 1),
    _AaaAccountIfIndex_Type()
)
aaaAccountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaAccountIfIndex.setStatus("current")
_AaaAccountMethodName_Type = DisplayString
_AaaAccountMethodName_Object = MibTableColumn
aaaAccountMethodName = _AaaAccountMethodName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 5, 1, 2),
    _AaaAccountMethodName_Type()
)
aaaAccountMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAccountMethodName.setStatus("current")
_AaaAccountProtocol_Type = Integer32
_AaaAccountProtocol_Object = MibTableColumn
aaaAccountProtocol = _AaaAccountProtocol_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 5, 1, 3),
    _AaaAccountProtocol_Type()
)
aaaAccountProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAccountProtocol.setStatus("current")
_AaaAccountStatus_Type = ValidStatus
_AaaAccountStatus_Object = MibTableColumn
aaaAccountStatus = _AaaAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 5, 1, 4),
    _AaaAccountStatus_Type()
)
aaaAccountStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAccountStatus.setStatus("current")
_AaaCommandPrivilegesTable_Object = MibTable
aaaCommandPrivilegesTable = _AaaCommandPrivilegesTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 8)
)
if mibBuilder.loadTexts:
    aaaCommandPrivilegesTable.setStatus("current")
_AaaCommandPrivilegesEntry_Object = MibTableRow
aaaCommandPrivilegesEntry = _AaaCommandPrivilegesEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 8, 1)
)
aaaCommandPrivilegesEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "aaaCommandPrivilegesLevel"),
    (0, "ECS2100-28PP-MIB", "aaaCommandPrivilegesInterfaceIndex"),
)
if mibBuilder.loadTexts:
    aaaCommandPrivilegesEntry.setStatus("current")


class _AaaCommandPrivilegesLevel_Type(Integer32):
    """Custom type aaaCommandPrivilegesLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AaaCommandPrivilegesLevel_Type.__name__ = "Integer32"
_AaaCommandPrivilegesLevel_Object = MibTableColumn
aaaCommandPrivilegesLevel = _AaaCommandPrivilegesLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 8, 1, 1),
    _AaaCommandPrivilegesLevel_Type()
)
aaaCommandPrivilegesLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaCommandPrivilegesLevel.setStatus("current")


class _AaaCommandPrivilegesInterfaceIndex_Type(Integer32):
    """Custom type aaaCommandPrivilegesInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("vty", 2))
    )


_AaaCommandPrivilegesInterfaceIndex_Type.__name__ = "Integer32"
_AaaCommandPrivilegesInterfaceIndex_Object = MibTableColumn
aaaCommandPrivilegesInterfaceIndex = _AaaCommandPrivilegesInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 8, 1, 2),
    _AaaCommandPrivilegesInterfaceIndex_Type()
)
aaaCommandPrivilegesInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaCommandPrivilegesInterfaceIndex.setStatus("current")


class _AaaCommandPrivilegesMethodName_Type(DisplayString):
    """Custom type aaaCommandPrivilegesMethodName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AaaCommandPrivilegesMethodName_Type.__name__ = "DisplayString"
_AaaCommandPrivilegesMethodName_Object = MibTableColumn
aaaCommandPrivilegesMethodName = _AaaCommandPrivilegesMethodName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 8, 1, 3),
    _AaaCommandPrivilegesMethodName_Type()
)
aaaCommandPrivilegesMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaCommandPrivilegesMethodName.setStatus("current")
_AaaAccExecTable_Object = MibTable
aaaAccExecTable = _AaaAccExecTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 9)
)
if mibBuilder.loadTexts:
    aaaAccExecTable.setStatus("current")
_AaaAccExecEntry_Object = MibTableRow
aaaAccExecEntry = _AaaAccExecEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 9, 1)
)
aaaAccExecEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "aaaAccExecIndex"),
)
if mibBuilder.loadTexts:
    aaaAccExecEntry.setStatus("current")


class _AaaAccExecIndex_Type(Integer32):
    """Custom type aaaAccExecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("vty", 2))
    )


_AaaAccExecIndex_Type.__name__ = "Integer32"
_AaaAccExecIndex_Object = MibTableColumn
aaaAccExecIndex = _AaaAccExecIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 9, 1, 1),
    _AaaAccExecIndex_Type()
)
aaaAccExecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaAccExecIndex.setStatus("current")
_AaaAccExecMethodName_Type = DisplayString
_AaaAccExecMethodName_Object = MibTableColumn
aaaAccExecMethodName = _AaaAccExecMethodName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 12, 9, 1, 2),
    _AaaAccExecMethodName_Type()
)
aaaAccExecMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAccExecMethodName.setStatus("current")
_NetworkAccessMgt_ObjectIdentity = ObjectIdentity
networkAccessMgt = _NetworkAccessMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13)
)
_NetworkAccessPortTable_Object = MibTable
networkAccessPortTable = _NetworkAccessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 2)
)
if mibBuilder.loadTexts:
    networkAccessPortTable.setStatus("current")
_NetworkAccessPortEntry_Object = MibTableRow
networkAccessPortEntry = _NetworkAccessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 2, 1)
)
networkAccessPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "networkAccessPortPortIndex"),
)
if mibBuilder.loadTexts:
    networkAccessPortEntry.setStatus("current")
_NetworkAccessPortPortIndex_Type = InterfaceIndex
_NetworkAccessPortPortIndex_Object = MibTableColumn
networkAccessPortPortIndex = _NetworkAccessPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 2, 1, 1),
    _NetworkAccessPortPortIndex_Type()
)
networkAccessPortPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessPortPortIndex.setStatus("current")
_NetworkAccessPortDynamicVlan_Type = EnabledStatus
_NetworkAccessPortDynamicVlan_Object = MibTableColumn
networkAccessPortDynamicVlan = _NetworkAccessPortDynamicVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 2, 1, 2),
    _NetworkAccessPortDynamicVlan_Type()
)
networkAccessPortDynamicVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortDynamicVlan.setStatus("current")


class _NetworkAccessPortMacFilter_Type(Integer32):
    """Custom type networkAccessPortMacFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_NetworkAccessPortMacFilter_Type.__name__ = "Integer32"
_NetworkAccessPortMacFilter_Object = MibTableColumn
networkAccessPortMacFilter = _NetworkAccessPortMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 2, 1, 5),
    _NetworkAccessPortMacFilter_Type()
)
networkAccessPortMacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortMacFilter.setStatus("current")


class _NetworkAccessPortGuestVlan_Type(Integer32):
    """Custom type networkAccessPortGuestVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_NetworkAccessPortGuestVlan_Type.__name__ = "Integer32"
_NetworkAccessPortGuestVlan_Object = MibTableColumn
networkAccessPortGuestVlan = _NetworkAccessPortGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 2, 1, 6),
    _NetworkAccessPortGuestVlan_Type()
)
networkAccessPortGuestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortGuestVlan.setStatus("current")
_NetworkAccessPortDynamicQos_Type = EnabledStatus
_NetworkAccessPortDynamicQos_Object = MibTableColumn
networkAccessPortDynamicQos = _NetworkAccessPortDynamicQos_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 2, 1, 10),
    _NetworkAccessPortDynamicQos_Type()
)
networkAccessPortDynamicQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortDynamicQos.setStatus("current")
_NetworkAccessClearMacAddressMgt_ObjectIdentity = ObjectIdentity
networkAccessClearMacAddressMgt = _NetworkAccessClearMacAddressMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 3)
)


class _NetworkAccessClearMacAddressAttribute_Type(Integer32):
    """Custom type networkAccessClearMacAddressAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("dynamic", 3),
          ("static", 2))
    )


_NetworkAccessClearMacAddressAttribute_Type.__name__ = "Integer32"
_NetworkAccessClearMacAddressAttribute_Object = MibScalar
networkAccessClearMacAddressAttribute = _NetworkAccessClearMacAddressAttribute_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 3, 1),
    _NetworkAccessClearMacAddressAttribute_Type()
)
networkAccessClearMacAddressAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessClearMacAddressAttribute.setStatus("current")
_NetworkAccessClearMacAddressMacAddress_Type = MacAddress
_NetworkAccessClearMacAddressMacAddress_Object = MibScalar
networkAccessClearMacAddressMacAddress = _NetworkAccessClearMacAddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 3, 2),
    _NetworkAccessClearMacAddressMacAddress_Type()
)
networkAccessClearMacAddressMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessClearMacAddressMacAddress.setStatus("current")
_NetworkAccessClearMacAddressPort_Type = Integer32
_NetworkAccessClearMacAddressPort_Object = MibScalar
networkAccessClearMacAddressPort = _NetworkAccessClearMacAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 3, 3),
    _NetworkAccessClearMacAddressPort_Type()
)
networkAccessClearMacAddressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessClearMacAddressPort.setStatus("current")


class _NetworkAccessClearMacAddressAction_Type(Integer32):
    """Custom type networkAccessClearMacAddressAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noclear", 1))
    )


_NetworkAccessClearMacAddressAction_Type.__name__ = "Integer32"
_NetworkAccessClearMacAddressAction_Object = MibScalar
networkAccessClearMacAddressAction = _NetworkAccessClearMacAddressAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 3, 4),
    _NetworkAccessClearMacAddressAction_Type()
)
networkAccessClearMacAddressAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessClearMacAddressAction.setStatus("current")
_NetworkAccessMacAddressTable_Object = MibTable
networkAccessMacAddressTable = _NetworkAccessMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 4)
)
if mibBuilder.loadTexts:
    networkAccessMacAddressTable.setStatus("current")
_NetworkAccessMacAddressEntry_Object = MibTableRow
networkAccessMacAddressEntry = _NetworkAccessMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 4, 1)
)
networkAccessMacAddressEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "networkAccessMacAddressAddress"),
    (0, "ECS2100-28PP-MIB", "networkAccessMacAddressPort"),
)
if mibBuilder.loadTexts:
    networkAccessMacAddressEntry.setStatus("current")
_NetworkAccessMacAddressAddress_Type = MacAddress
_NetworkAccessMacAddressAddress_Object = MibTableColumn
networkAccessMacAddressAddress = _NetworkAccessMacAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 4, 1, 1),
    _NetworkAccessMacAddressAddress_Type()
)
networkAccessMacAddressAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacAddressAddress.setStatus("current")
_NetworkAccessMacAddressPort_Type = InterfaceIndex
_NetworkAccessMacAddressPort_Object = MibTableColumn
networkAccessMacAddressPort = _NetworkAccessMacAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 4, 1, 2),
    _NetworkAccessMacAddressPort_Type()
)
networkAccessMacAddressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacAddressPort.setStatus("current")
_NetworkAccessMacAddressInetAddressType_Type = InetAddressType
_NetworkAccessMacAddressInetAddressType_Object = MibTableColumn
networkAccessMacAddressInetAddressType = _NetworkAccessMacAddressInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 4, 1, 3),
    _NetworkAccessMacAddressInetAddressType_Type()
)
networkAccessMacAddressInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAccessMacAddressInetAddressType.setStatus("current")
_NetworkAccessMacAddressRadiusServerInetAddress_Type = InetAddress
_NetworkAccessMacAddressRadiusServerInetAddress_Object = MibTableColumn
networkAccessMacAddressRadiusServerInetAddress = _NetworkAccessMacAddressRadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 4, 1, 4),
    _NetworkAccessMacAddressRadiusServerInetAddress_Type()
)
networkAccessMacAddressRadiusServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAccessMacAddressRadiusServerInetAddress.setStatus("current")


class _NetworkAccessMacAddressTime_Type(DisplayString):
    """Custom type networkAccessMacAddressTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_NetworkAccessMacAddressTime_Type.__name__ = "DisplayString"
_NetworkAccessMacAddressTime_Object = MibTableColumn
networkAccessMacAddressTime = _NetworkAccessMacAddressTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 4, 1, 5),
    _NetworkAccessMacAddressTime_Type()
)
networkAccessMacAddressTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAccessMacAddressTime.setStatus("current")


class _NetworkAccessMacAddressAttribute_Type(Integer32):
    """Custom type networkAccessMacAddressAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_NetworkAccessMacAddressAttribute_Type.__name__ = "Integer32"
_NetworkAccessMacAddressAttribute_Object = MibTableColumn
networkAccessMacAddressAttribute = _NetworkAccessMacAddressAttribute_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 4, 1, 6),
    _NetworkAccessMacAddressAttribute_Type()
)
networkAccessMacAddressAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAccessMacAddressAttribute.setStatus("current")
_NetworkAccessAging_Type = EnabledStatus
_NetworkAccessAging_Object = MibScalar
networkAccessAging = _NetworkAccessAging_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 5),
    _NetworkAccessAging_Type()
)
networkAccessAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessAging.setStatus("current")
_NetworkAccessMacFilterWithMaskTable_Object = MibTable
networkAccessMacFilterWithMaskTable = _NetworkAccessMacFilterWithMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 6)
)
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskTable.setStatus("current")
_NetworkAccessMacFilterWithMaskEntry_Object = MibTableRow
networkAccessMacFilterWithMaskEntry = _NetworkAccessMacFilterWithMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 6, 1)
)
networkAccessMacFilterWithMaskEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "networkAccessMacFilterWithMaskID"),
    (0, "ECS2100-28PP-MIB", "networkAccessMacFilterWithMaskMacAddress"),
    (0, "ECS2100-28PP-MIB", "networkAccessMacFilterWithMaskMacAddressMask"),
)
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskEntry.setStatus("current")


class _NetworkAccessMacFilterWithMaskID_Type(Integer32):
    """Custom type networkAccessMacFilterWithMaskID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_NetworkAccessMacFilterWithMaskID_Type.__name__ = "Integer32"
_NetworkAccessMacFilterWithMaskID_Object = MibTableColumn
networkAccessMacFilterWithMaskID = _NetworkAccessMacFilterWithMaskID_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 6, 1, 1),
    _NetworkAccessMacFilterWithMaskID_Type()
)
networkAccessMacFilterWithMaskID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskID.setStatus("current")
_NetworkAccessMacFilterWithMaskMacAddress_Type = MacAddress
_NetworkAccessMacFilterWithMaskMacAddress_Object = MibTableColumn
networkAccessMacFilterWithMaskMacAddress = _NetworkAccessMacFilterWithMaskMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 6, 1, 2),
    _NetworkAccessMacFilterWithMaskMacAddress_Type()
)
networkAccessMacFilterWithMaskMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskMacAddress.setStatus("current")
_NetworkAccessMacFilterWithMaskMacAddressMask_Type = MacAddress
_NetworkAccessMacFilterWithMaskMacAddressMask_Object = MibTableColumn
networkAccessMacFilterWithMaskMacAddressMask = _NetworkAccessMacFilterWithMaskMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 6, 1, 3),
    _NetworkAccessMacFilterWithMaskMacAddressMask_Type()
)
networkAccessMacFilterWithMaskMacAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskMacAddressMask.setStatus("current")
_NetworkAccessMacFilterWithMaskStatus_Type = ValidStatus
_NetworkAccessMacFilterWithMaskStatus_Object = MibTableColumn
networkAccessMacFilterWithMaskStatus = _NetworkAccessMacFilterWithMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 13, 6, 1, 4),
    _NetworkAccessMacFilterWithMaskStatus_Type()
)
networkAccessMacFilterWithMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskStatus.setStatus("current")
_DosMgt_ObjectIdentity = ObjectIdentity
dosMgt = _DosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1)
)
_DosSmurf_ObjectIdentity = ObjectIdentity
dosSmurf = _DosSmurf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 3)
)
_DosSmurfStatus_Type = EnabledStatus
_DosSmurfStatus_Object = MibScalar
dosSmurfStatus = _DosSmurfStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 3, 1),
    _DosSmurfStatus_Type()
)
dosSmurfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosSmurfStatus.setStatus("current")
_DosTcpNullScan_ObjectIdentity = ObjectIdentity
dosTcpNullScan = _DosTcpNullScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 5)
)
_DosTcpNullScanStatus_Type = EnabledStatus
_DosTcpNullScanStatus_Object = MibScalar
dosTcpNullScanStatus = _DosTcpNullScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 5, 1),
    _DosTcpNullScanStatus_Type()
)
dosTcpNullScanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosTcpNullScanStatus.setStatus("current")
_DosTcpSynFinScan_ObjectIdentity = ObjectIdentity
dosTcpSynFinScan = _DosTcpSynFinScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 6)
)
_DosTcpSynFinScanStatus_Type = EnabledStatus
_DosTcpSynFinScanStatus_Object = MibScalar
dosTcpSynFinScanStatus = _DosTcpSynFinScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 6, 1),
    _DosTcpSynFinScanStatus_Type()
)
dosTcpSynFinScanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosTcpSynFinScanStatus.setStatus("current")
_DosTcpXmasScan_ObjectIdentity = ObjectIdentity
dosTcpXmasScan = _DosTcpXmasScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 7)
)
_DosTcpXmasScanStatus_Type = EnabledStatus
_DosTcpXmasScanStatus_Object = MibScalar
dosTcpXmasScanStatus = _DosTcpXmasScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 7, 1),
    _DosTcpXmasScanStatus_Type()
)
dosTcpXmasScanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosTcpXmasScanStatus.setStatus("current")
_DosTcpUdpPortZero_ObjectIdentity = ObjectIdentity
dosTcpUdpPortZero = _DosTcpUdpPortZero_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 11)
)
_DosTcpUdpPortZeroStatus_Type = EnabledStatus
_DosTcpUdpPortZeroStatus_Object = MibScalar
dosTcpUdpPortZeroStatus = _DosTcpUdpPortZeroStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 17, 16, 1, 11, 1),
    _DosTcpUdpPortZeroStatus_Type()
)
dosTcpUdpPortZeroStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dosTcpUdpPortZeroStatus.setStatus("current")
_SysLogMgt_ObjectIdentity = ObjectIdentity
sysLogMgt = _SysLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19)
)
_SysLogStatus_Type = EnabledStatus
_SysLogStatus_Object = MibScalar
sysLogStatus = _SysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 3),
    _SysLogHistoryRamLevel_Type()
)
sysLogHistoryRamLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryRamLevel.setStatus("current")
_RemoteLogMgt_ObjectIdentity = ObjectIdentity
remoteLogMgt = _RemoteLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6)
)
_RemoteLogStatus_Type = EnabledStatus
_RemoteLogStatus_Object = MibScalar
remoteLogStatus = _RemoteLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6, 3),
    _RemoteLogFacilityType_Type()
)
remoteLogFacilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogFacilityType.setStatus("current")
_RemoteLogServerInetTable_Object = MibTable
remoteLogServerInetTable = _RemoteLogServerInetTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6, 7)
)
if mibBuilder.loadTexts:
    remoteLogServerInetTable.setStatus("current")
_RemoteLogServerInetEntry_Object = MibTableRow
remoteLogServerInetEntry = _RemoteLogServerInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6, 7, 1)
)
remoteLogServerInetEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "remoteLogServerInetAddressType"),
    (0, "ECS2100-28PP-MIB", "remoteLogServerInetAddress"),
)
if mibBuilder.loadTexts:
    remoteLogServerInetEntry.setStatus("current")
_RemoteLogServerInetAddressType_Type = InetAddressType
_RemoteLogServerInetAddressType_Object = MibTableColumn
remoteLogServerInetAddressType = _RemoteLogServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6, 7, 1, 1),
    _RemoteLogServerInetAddressType_Type()
)
remoteLogServerInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteLogServerInetAddressType.setStatus("current")
_RemoteLogServerInetAddress_Type = InetAddress
_RemoteLogServerInetAddress_Object = MibTableColumn
remoteLogServerInetAddress = _RemoteLogServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6, 7, 1, 2),
    _RemoteLogServerInetAddress_Type()
)
remoteLogServerInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteLogServerInetAddress.setStatus("current")
_RemoteLogServerStatus_Type = ValidStatus
_RemoteLogServerStatus_Object = MibTableColumn
remoteLogServerStatus = _RemoteLogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6, 7, 1, 3),
    _RemoteLogServerStatus_Type()
)
remoteLogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerStatus.setStatus("current")


class _RemoteLogServerUdpPort_Type(Integer32):
    """Custom type remoteLogServerUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RemoteLogServerUdpPort_Type.__name__ = "Integer32"
_RemoteLogServerUdpPort_Object = MibTableColumn
remoteLogServerUdpPort = _RemoteLogServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 6, 7, 1, 4),
    _RemoteLogServerUdpPort_Type()
)
remoteLogServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogServerUdpPort.setStatus("current")
_SmtpMgt_ObjectIdentity = ObjectIdentity
smtpMgt = _SmtpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7)
)
_SmtpStatus_Type = EnabledStatus
_SmtpStatus_Object = MibScalar
smtpStatus = _SmtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 1),
    _SmtpStatus_Type()
)
smtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpStatus.setStatus("current")


class _SmtpSeverityLevel_Type(Integer32):
    """Custom type smtpSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SmtpSeverityLevel_Type.__name__ = "Integer32"
_SmtpSeverityLevel_Object = MibScalar
smtpSeverityLevel = _SmtpSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 2),
    _SmtpSeverityLevel_Type()
)
smtpSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSeverityLevel.setStatus("current")


class _SmtpSourceEMail_Type(DisplayString):
    """Custom type smtpSourceEMail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SmtpSourceEMail_Type.__name__ = "DisplayString"
_SmtpSourceEMail_Object = MibScalar
smtpSourceEMail = _SmtpSourceEMail_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 3),
    _SmtpSourceEMail_Type()
)
smtpSourceEMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSourceEMail.setStatus("current")
_SmtpServerIpTable_Object = MibTable
smtpServerIpTable = _SmtpServerIpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 4)
)
if mibBuilder.loadTexts:
    smtpServerIpTable.setStatus("current")
_SmtpServerIpEntry_Object = MibTableRow
smtpServerIpEntry = _SmtpServerIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 4, 1)
)
smtpServerIpEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "smtpServerIp"),
)
if mibBuilder.loadTexts:
    smtpServerIpEntry.setStatus("current")
_SmtpServerIp_Type = IpAddress
_SmtpServerIp_Object = MibTableColumn
smtpServerIp = _SmtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 4, 1, 1),
    _SmtpServerIp_Type()
)
smtpServerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smtpServerIp.setStatus("current")
_SmtpServerIpStatus_Type = ValidStatus
_SmtpServerIpStatus_Object = MibTableColumn
smtpServerIpStatus = _SmtpServerIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 4, 1, 2),
    _SmtpServerIpStatus_Type()
)
smtpServerIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpServerIpStatus.setStatus("current")
_SmtpDestEMailTable_Object = MibTable
smtpDestEMailTable = _SmtpDestEMailTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 5)
)
if mibBuilder.loadTexts:
    smtpDestEMailTable.setStatus("current")
_SmtpDestEMailEntry_Object = MibTableRow
smtpDestEMailEntry = _SmtpDestEMailEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 5, 1)
)
smtpDestEMailEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "smtpDestEMail"),
)
if mibBuilder.loadTexts:
    smtpDestEMailEntry.setStatus("current")


class _SmtpDestEMail_Type(DisplayString):
    """Custom type smtpDestEMail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SmtpDestEMail_Type.__name__ = "DisplayString"
_SmtpDestEMail_Object = MibTableColumn
smtpDestEMail = _SmtpDestEMail_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 5, 1, 1),
    _SmtpDestEMail_Type()
)
smtpDestEMail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smtpDestEMail.setStatus("current")
_SmtpDestEMailStatus_Type = ValidStatus
_SmtpDestEMailStatus_Object = MibTableColumn
smtpDestEMailStatus = _SmtpDestEMailStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 7, 5, 1, 2),
    _SmtpDestEMailStatus_Type()
)
smtpDestEMailStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpDestEMailStatus.setStatus("current")
_SysLogCommandLogStatus_Type = EnabledStatus
_SysLogCommandLogStatus_Object = MibScalar
sysLogCommandLogStatus = _SysLogCommandLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 19, 10),
    _SysLogCommandLogStatus_Type()
)
sysLogCommandLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogCommandLogStatus.setStatus("current")
_LineMgt_ObjectIdentity = ObjectIdentity
lineMgt = _LineMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20)
)
_ConsoleMgt_ObjectIdentity = ObjectIdentity
consoleMgt = _ConsoleMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 1)
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 1, 4),
    _ConsoleStopBits_Type()
)
consoleStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleStopBits.setStatus("current")


class _ConsoleExecTimeout_Type(Integer32):
    """Custom type consoleExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 65535),
    )


_ConsoleExecTimeout_Type.__name__ = "Integer32"
_ConsoleExecTimeout_Object = MibScalar
consoleExecTimeout = _ConsoleExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 1, 5),
    _ConsoleExecTimeout_Type()
)
consoleExecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleExecTimeout.setStatus("current")


class _ConsolePasswordThreshold_Type(Integer32):
    """Custom type consolePasswordThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 120),
    )


_ConsolePasswordThreshold_Type.__name__ = "Integer32"
_ConsolePasswordThreshold_Object = MibScalar
consolePasswordThreshold = _ConsolePasswordThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 1, 6),
    _ConsolePasswordThreshold_Type()
)
consolePasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePasswordThreshold.setStatus("current")


class _ConsoleSilentTime_Type(Integer32):
    """Custom type consoleSilentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_ConsoleSilentTime_Type.__name__ = "Integer32"
_ConsoleSilentTime_Object = MibScalar
consoleSilentTime = _ConsoleSilentTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 1, 7),
    _ConsoleSilentTime_Type()
)
consoleSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleSilentTime.setStatus("current")


class _ConsoleLoginResponseTimeout_Type(Integer32):
    """Custom type consoleLoginResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_ConsoleLoginResponseTimeout_Type.__name__ = "Integer32"
_ConsoleLoginResponseTimeout_Object = MibScalar
consoleLoginResponseTimeout = _ConsoleLoginResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 1, 10),
    _ConsoleLoginResponseTimeout_Type()
)
consoleLoginResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleLoginResponseTimeout.setStatus("current")
_TelnetMgt_ObjectIdentity = ObjectIdentity
telnetMgt = _TelnetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 2)
)


class _TelnetStatus_Type(EnabledStatus):
    """Custom type telnetStatus based on EnabledStatus"""


_TelnetStatus_Object = MibScalar
telnetStatus = _TelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 2, 4),
    _TelnetStatus_Type()
)
telnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetStatus.setStatus("current")


class _TelnetPortNumber_Type(Integer32):
    """Custom type telnetPortNumber based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetPortNumber_Type.__name__ = "Integer32"
_TelnetPortNumber_Object = MibScalar
telnetPortNumber = _TelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 2, 5),
    _TelnetPortNumber_Type()
)
telnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortNumber.setStatus("current")
_VtyMgt_ObjectIdentity = ObjectIdentity
vtyMgt = _VtyMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 3)
)


class _VtyExecTimeout_Type(Integer32):
    """Custom type vtyExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_VtyExecTimeout_Type.__name__ = "Integer32"
_VtyExecTimeout_Object = MibScalar
vtyExecTimeout = _VtyExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 3, 1),
    _VtyExecTimeout_Type()
)
vtyExecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtyExecTimeout.setStatus("current")


class _VtyPasswordThreshold_Type(Integer32):
    """Custom type vtyPasswordThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 120),
    )


_VtyPasswordThreshold_Type.__name__ = "Integer32"
_VtyPasswordThreshold_Object = MibScalar
vtyPasswordThreshold = _VtyPasswordThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 3, 2),
    _VtyPasswordThreshold_Type()
)
vtyPasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtyPasswordThreshold.setStatus("current")


class _VtyLoginResponseTimeout_Type(Integer32):
    """Custom type vtyLoginResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_VtyLoginResponseTimeout_Type.__name__ = "Integer32"
_VtyLoginResponseTimeout_Object = MibScalar
vtyLoginResponseTimeout = _VtyLoginResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 3, 3),
    _VtyLoginResponseTimeout_Type()
)
vtyLoginResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtyLoginResponseTimeout.setStatus("current")


class _VtyMaxSession_Type(Integer32):
    """Custom type vtyMaxSession based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_VtyMaxSession_Type.__name__ = "Integer32"
_VtyMaxSession_Object = MibScalar
vtyMaxSession = _VtyMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 3, 4),
    _VtyMaxSession_Type()
)
vtyMaxSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtyMaxSession.setStatus("current")


class _VtySilentTime_Type(Integer32):
    """Custom type vtySilentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_VtySilentTime_Type.__name__ = "Integer32"
_VtySilentTime_Object = MibScalar
vtySilentTime = _VtySilentTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 20, 3, 5),
    _VtySilentTime_Type()
)
vtySilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtySilentTime.setStatus("current")
if mibBuilder.loadTexts:
    vtySilentTime.setUnits("seconds")
_SysTimeMgt_ObjectIdentity = ObjectIdentity
sysTimeMgt = _SysTimeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23)
)
_SntpMgt_ObjectIdentity = ObjectIdentity
sntpMgt = _SntpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1)
)
_SntpStatus_Type = EnabledStatus
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1, 1),
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
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_SntpServiceMode_Type.__name__ = "Integer32"
_SntpServiceMode_Object = MibScalar
sntpServiceMode = _SntpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1, 2),
    _SntpServiceMode_Type()
)
sntpServiceMode.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1, 3),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1, 4)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1, 4, 1)
)
sntpServerEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "sntpServerIndex"),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1, 4, 1, 1),
    _SntpServerIndex_Type()
)
sntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sntpServerIndex.setStatus("current")
_SntpServerInetAddressType_Type = InetAddressType
_SntpServerInetAddressType_Object = MibTableColumn
sntpServerInetAddressType = _SntpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1, 4, 1, 4),
    _SntpServerInetAddressType_Type()
)
sntpServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerInetAddressType.setStatus("current")
_SntpServerInetAddress_Type = InetAddress
_SntpServerInetAddress_Object = MibTableColumn
sntpServerInetAddress = _SntpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1, 4, 1, 5),
    _SntpServerInetAddress_Type()
)
sntpServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerInetAddress.setStatus("current")
_SntpServerStatus_Type = ValidStatus
_SntpServerStatus_Object = MibTableColumn
sntpServerStatus = _SntpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 1, 4, 1, 6),
    _SntpServerStatus_Type()
)
sntpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sntpServerStatus.setStatus("current")


class _SysCurrentTime_Type(DisplayString):
    """Custom type sysCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SysCurrentTime_Type.__name__ = "DisplayString"
_SysCurrentTime_Object = MibScalar
sysCurrentTime = _SysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 3),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("current")


class _SysTimeZoneName_Type(DisplayString):
    """Custom type sysTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SysTimeZoneName_Type.__name__ = "DisplayString"
_SysTimeZoneName_Object = MibScalar
sysTimeZoneName = _SysTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 4),
    _SysTimeZoneName_Type()
)
sysTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZoneName.setStatus("current")
_NtpMgt_ObjectIdentity = ObjectIdentity
ntpMgt = _NtpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5)
)
_NtpStatus_Type = EnabledStatus
_NtpStatus_Object = MibScalar
ntpStatus = _NtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 1),
    _NtpStatus_Type()
)
ntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpStatus.setStatus("current")


class _NtpServiceMode_Type(Integer32):
    """Custom type ntpServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_NtpServiceMode_Type.__name__ = "Integer32"
_NtpServiceMode_Object = MibScalar
ntpServiceMode = _NtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 2),
    _NtpServiceMode_Type()
)
ntpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServiceMode.setStatus("current")
_NtpPollInterval_Type = Integer32
_NtpPollInterval_Object = MibScalar
ntpPollInterval = _NtpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 3),
    _NtpPollInterval_Type()
)
ntpPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPollInterval.setStatus("current")
_NtpAuthenticateStatus_Type = EnabledStatus
_NtpAuthenticateStatus_Object = MibScalar
ntpAuthenticateStatus = _NtpAuthenticateStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 4),
    _NtpAuthenticateStatus_Type()
)
ntpAuthenticateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticateStatus.setStatus("current")
_NtpServerTable_Object = MibTable
ntpServerTable = _NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 5)
)
if mibBuilder.loadTexts:
    ntpServerTable.setStatus("current")
_NtpServerEntry_Object = MibTableRow
ntpServerEntry = _NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 5, 1)
)
ntpServerEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "ntpServerIpAddress"),
)
if mibBuilder.loadTexts:
    ntpServerEntry.setStatus("current")
_NtpServerIpAddress_Type = IpAddress
_NtpServerIpAddress_Object = MibTableColumn
ntpServerIpAddress = _NtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 5, 1, 1),
    _NtpServerIpAddress_Type()
)
ntpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpServerIpAddress.setStatus("current")
_NtpServerVersion_Type = Integer32
_NtpServerVersion_Object = MibTableColumn
ntpServerVersion = _NtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 5, 1, 2),
    _NtpServerVersion_Type()
)
ntpServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServerVersion.setStatus("current")


class _NtpServerKeyId_Type(Integer32):
    """Custom type ntpServerKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtpServerKeyId_Type.__name__ = "Integer32"
_NtpServerKeyId_Object = MibTableColumn
ntpServerKeyId = _NtpServerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 5, 1, 3),
    _NtpServerKeyId_Type()
)
ntpServerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerKeyId.setStatus("current")
_NtpServerStatus_Type = ValidStatus
_NtpServerStatus_Object = MibTableColumn
ntpServerStatus = _NtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 5, 1, 4),
    _NtpServerStatus_Type()
)
ntpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpServerStatus.setStatus("current")
_NtpAuthKeyTable_Object = MibTable
ntpAuthKeyTable = _NtpAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 6)
)
if mibBuilder.loadTexts:
    ntpAuthKeyTable.setStatus("current")
_NtpAuthKeyEntry_Object = MibTableRow
ntpAuthKeyEntry = _NtpAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 6, 1)
)
ntpAuthKeyEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "ntpAuthKeyId"),
)
if mibBuilder.loadTexts:
    ntpAuthKeyEntry.setStatus("current")


class _NtpAuthKeyId_Type(Integer32):
    """Custom type ntpAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_NtpAuthKeyId_Type.__name__ = "Integer32"
_NtpAuthKeyId_Object = MibTableColumn
ntpAuthKeyId = _NtpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 6, 1, 1),
    _NtpAuthKeyId_Type()
)
ntpAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpAuthKeyId.setStatus("current")


class _NtpAuthKeyWord_Type(OctetString):
    """Custom type ntpAuthKeyWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAuthKeyWord_Type.__name__ = "OctetString"
_NtpAuthKeyWord_Object = MibTableColumn
ntpAuthKeyWord = _NtpAuthKeyWord_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 6, 1, 2),
    _NtpAuthKeyWord_Type()
)
ntpAuthKeyWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthKeyWord.setStatus("current")
_NtpAuthKeyStatus_Type = ValidStatus
_NtpAuthKeyStatus_Object = MibTableColumn
ntpAuthKeyStatus = _NtpAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 23, 5, 6, 1, 3),
    _NtpAuthKeyStatus_Type()
)
ntpAuthKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthKeyStatus.setStatus("current")
_FileMgt_ObjectIdentity = ObjectIdentity
fileMgt = _FileMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24)
)
_FileCopyMgt_ObjectIdentity = ObjectIdentity
fileCopyMgt = _FileCopyMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1)
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
              5,
              6,
              7,
              10)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("ftp", 7),
          ("http", 6),
          ("runningCfg", 2),
          ("sftp", 10),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5))
    )


_FileCopySrcOperType_Type.__name__ = "Integer32"
_FileCopySrcOperType_Object = MibScalar
fileCopySrcOperType = _FileCopySrcOperType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 2),
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
              5,
              6,
              7,
              10,
              15)
        )
    )
    namedValues = NamedValues(
        *(("addRunningCfg", 15),
          ("file", 1),
          ("ftp", 7),
          ("http", 6),
          ("runningCfg", 2),
          ("sftp", 10),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5))
    )


_FileCopyDestOperType_Type.__name__ = "Integer32"
_FileCopyDestOperType_Object = MibScalar
fileCopyDestOperType = _FileCopyDestOperType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 4),
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
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bootRom", 3),
          ("config", 2),
          ("loader", 5),
          ("opcode", 1))
    )


_FileCopyFileType_Type.__name__ = "Integer32"
_FileCopyFileType_Object = MibScalar
fileCopyFileType = _FileCopyFileType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 5),
    _FileCopyFileType_Type()
)
fileCopyFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyFileType.setStatus("current")
_FileCopyUnitId_Type = Integer32
_FileCopyUnitId_Object = MibScalar
fileCopyUnitId = _FileCopyUnitId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 8),
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
              31,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56)
        )
    )
    namedValues = NamedValues(
        *(("fileCopyBusy", 17),
          ("fileCopyCompleted", 31),
          ("fileCopyConnectError", 44),
          ("fileCopyDataConnectionOpenError", 46),
          ("fileCopyError", 29),
          ("fileCopyFileNotFound", 41),
          ("fileCopyFileNumExceed", 55),
          ("fileCopyFileSizeExceed", 21),
          ("fileCopyFileUnavailable", 51),
          ("fileCopyHeaderChecksumError", 24),
          ("fileCopyImageChecksumError", 25),
          ("fileCopyImageTypeError", 23),
          ("fileCopyInvalidFileName", 48),
          ("fileCopyLogInError", 47),
          ("fileCopyMagicWordError", 22),
          ("fileCopyParaError", 16),
          ("fileCopyProjectIdError", 54),
          ("fileCopyReadFileError", 19),
          ("fileCopySameVersion", 56),
          ("fileCopyServerNotAcceptProvidedCiphers", 49),
          ("fileCopyServerNotInService", 45),
          ("fileCopyServerNotSupportFtps", 50),
          ("fileCopyServerPermissionDenied", 42),
          ("fileCopySetStartupError", 20),
          ("fileCopyStorageFull", 43),
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
          ("fileCopyTimeout", 53),
          ("fileCopyUnclassifiedError", 52),
          ("fileCopyUnknown", 18),
          ("fileCopyWriteFlashError", 27),
          ("fileCopyWriteFlashFinish", 26),
          ("fileCopyWriteFlashProgramming", 28))
    )


_FileCopyStatus_Type.__name__ = "Integer32"
_FileCopyStatus_Object = MibScalar
fileCopyStatus = _FileCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 9),
    _FileCopyStatus_Type()
)
fileCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyStatus.setStatus("current")
_FileCopyServerInetAddressType_Type = InetAddressType
_FileCopyServerInetAddressType_Object = MibScalar
fileCopyServerInetAddressType = _FileCopyServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 20),
    _FileCopyServerInetAddressType_Type()
)
fileCopyServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyServerInetAddressType.setStatus("current")
_FileCopyServerInetAddress_Type = InetAddress
_FileCopyServerInetAddress_Object = MibScalar
fileCopyServerInetAddress = _FileCopyServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 21),
    _FileCopyServerInetAddress_Type()
)
fileCopyServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyServerInetAddress.setStatus("current")


class _FileCopyServerUserName_Type(DisplayString):
    """Custom type fileCopyServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FileCopyServerUserName_Type.__name__ = "DisplayString"
_FileCopyServerUserName_Object = MibScalar
fileCopyServerUserName = _FileCopyServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 22),
    _FileCopyServerUserName_Type()
)
fileCopyServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyServerUserName.setStatus("current")


class _FileCopyServerPassword_Type(DisplayString):
    """Custom type fileCopyServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FileCopyServerPassword_Type.__name__ = "DisplayString"
_FileCopyServerPassword_Object = MibScalar
fileCopyServerPassword = _FileCopyServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 1, 23),
    _FileCopyServerPassword_Type()
)
fileCopyServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyServerPassword.setStatus("current")
_FileInfoMgt_ObjectIdentity = ObjectIdentity
fileInfoMgt = _FileInfoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2)
)
_FileInfoTable_Object = MibTable
fileInfoTable = _FileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    fileInfoTable.setStatus("current")
_FileInfoEntry_Object = MibTableRow
fileInfoEntry = _FileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2, 1, 1)
)
fileInfoEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "fileInfoUnitID"),
    (1, "ECS2100-28PP-MIB", "fileInfoFileName"),
)
if mibBuilder.loadTexts:
    fileInfoEntry.setStatus("current")


class _FileInfoUnitID_Type(Integer32):
    """Custom type fileInfoUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_FileInfoUnitID_Type.__name__ = "Integer32"
_FileInfoUnitID_Object = MibTableColumn
fileInfoUnitID = _FileInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2, 1, 1, 3),
    _FileInfoFileType_Type()
)
fileInfoFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileType.setStatus("current")
_FileInfoIsStartUp_Type = TruthValue
_FileInfoIsStartUp_Object = MibTableColumn
fileInfoIsStartUp = _FileInfoIsStartUp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2, 1, 1, 4),
    _FileInfoIsStartUp_Type()
)
fileInfoIsStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoIsStartUp.setStatus("current")
_FileInfoFileSize_Type = Integer32
_FileInfoFileSize_Object = MibTableColumn
fileInfoFileSize = _FileInfoFileSize_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2, 1, 1, 5),
    _FileInfoFileSize_Type()
)
fileInfoFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileSize.setStatus("current")
if mibBuilder.loadTexts:
    fileInfoFileSize.setUnits("bytes")


class _FileInfoCreationTime_Type(DisplayString):
    """Custom type fileInfoCreationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_FileInfoCreationTime_Type.__name__ = "DisplayString"
_FileInfoCreationTime_Object = MibTableColumn
fileInfoCreationTime = _FileInfoCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 2, 1, 1, 7),
    _FileInfoDelete_Type()
)
fileInfoDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoDelete.setStatus("current")
_FileAutoDownloadResultTable_Object = MibTable
fileAutoDownloadResultTable = _FileAutoDownloadResultTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 3)
)
if mibBuilder.loadTexts:
    fileAutoDownloadResultTable.setStatus("current")
_FileAutoDownloadResultEntry_Object = MibTableRow
fileAutoDownloadResultEntry = _FileAutoDownloadResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 3, 1)
)
fileAutoDownloadResultEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "fileAutoDownloadResultUnitID"),
)
if mibBuilder.loadTexts:
    fileAutoDownloadResultEntry.setStatus("current")


class _FileAutoDownloadResultUnitID_Type(Integer32):
    """Custom type fileAutoDownloadResultUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_FileAutoDownloadResultUnitID_Type.__name__ = "Integer32"
_FileAutoDownloadResultUnitID_Object = MibTableColumn
fileAutoDownloadResultUnitID = _FileAutoDownloadResultUnitID_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 3, 1, 1),
    _FileAutoDownloadResultUnitID_Type()
)
fileAutoDownloadResultUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileAutoDownloadResultUnitID.setStatus("current")


class _FileAutoDownloadResultAction_Type(Integer32):
    """Custom type fileAutoDownloadResultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copying", 2),
          ("notCopying", 1))
    )


_FileAutoDownloadResultAction_Type.__name__ = "Integer32"
_FileAutoDownloadResultAction_Object = MibTableColumn
fileAutoDownloadResultAction = _FileAutoDownloadResultAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 3, 1, 2),
    _FileAutoDownloadResultAction_Type()
)
fileAutoDownloadResultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAutoDownloadResultAction.setStatus("current")


class _FileAutoDownloadResultStatus_Type(Integer32):
    """Custom type fileAutoDownloadResultStatus based on Integer32"""
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
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56)
        )
    )
    namedValues = NamedValues(
        *(("fileCopyBusy", 17),
          ("fileCopyCompleted", 31),
          ("fileCopyConnectError", 44),
          ("fileCopyDataConnectionOpenError", 46),
          ("fileCopyError", 29),
          ("fileCopyFileNotFound", 41),
          ("fileCopyFileNumExceed", 55),
          ("fileCopyFileSizeExceed", 21),
          ("fileCopyFileUnavailable", 51),
          ("fileCopyHeaderChecksumError", 24),
          ("fileCopyImageChecksumError", 25),
          ("fileCopyImageTypeError", 23),
          ("fileCopyInvalidFileName", 48),
          ("fileCopyLogInError", 47),
          ("fileCopyMagicWordError", 22),
          ("fileCopyParaError", 16),
          ("fileCopyProjectIdError", 54),
          ("fileCopyReadFileError", 19),
          ("fileCopySameVersion", 56),
          ("fileCopyServerNotAcceptProvidedCiphers", 49),
          ("fileCopyServerNotInService", 45),
          ("fileCopyServerNotSupportFtps", 50),
          ("fileCopyServerPermissionDenied", 42),
          ("fileCopySetStartupError", 20),
          ("fileCopyStorageFull", 43),
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
          ("fileCopyTimeout", 53),
          ("fileCopyUnclassifiedError", 52),
          ("fileCopyUnknown", 18),
          ("fileCopyWriteFlashError", 27),
          ("fileCopyWriteFlashFinish", 26),
          ("fileCopyWriteFlashProgramming", 28))
    )


_FileAutoDownloadResultStatus_Type.__name__ = "Integer32"
_FileAutoDownloadResultStatus_Object = MibTableColumn
fileAutoDownloadResultStatus = _FileAutoDownloadResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 24, 3, 1, 3),
    _FileAutoDownloadResultStatus_Type()
)
fileAutoDownloadResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAutoDownloadResultStatus.setStatus("current")
_PoeMgt_ObjectIdentity = ObjectIdentity
poeMgt = _PoeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28)
)
_PethPseMainExtTable_Object = MibTable
pethPseMainExtTable = _PethPseMainExtTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 5)
)
if mibBuilder.loadTexts:
    pethPseMainExtTable.setStatus("current")
_PethPseMainExtEntry_Object = MibTableRow
pethPseMainExtEntry = _PethPseMainExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 5, 1)
)
if mibBuilder.loadTexts:
    pethPseMainExtEntry.setStatus("current")


class _PethPseMainExtDllPowerType_Type(Integer32):
    """Custom type pethPseMainExtDllPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1Pse", 2),
          ("type2Pse", 0))
    )


_PethPseMainExtDllPowerType_Type.__name__ = "Integer32"
_PethPseMainExtDllPowerType_Object = MibTableColumn
pethPseMainExtDllPowerType = _PethPseMainExtDllPowerType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 5, 1, 1),
    _PethPseMainExtDllPowerType_Type()
)
pethPseMainExtDllPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPseMainExtDllPowerType.setStatus("current")


class _PethPseMainExtDllPowerSource_Type(Integer32):
    """Custom type pethPseMainExtDllPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1),
          ("unknown", 0))
    )


_PethPseMainExtDllPowerSource_Type.__name__ = "Integer32"
_PethPseMainExtDllPowerSource_Object = MibTableColumn
pethPseMainExtDllPowerSource = _PethPseMainExtDllPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 5, 1, 2),
    _PethPseMainExtDllPowerSource_Type()
)
pethPseMainExtDllPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPseMainExtDllPowerSource.setStatus("current")
_PethPsePortExtTable_Object = MibTable
pethPsePortExtTable = _PethPsePortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 6)
)
if mibBuilder.loadTexts:
    pethPsePortExtTable.setStatus("current")
_PethPsePortExtEntry_Object = MibTableRow
pethPsePortExtEntry = _PethPsePortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 6, 1)
)
if mibBuilder.loadTexts:
    pethPsePortExtEntry.setStatus("current")
_PethPsePortExtMirroredDllPdRequestedPowerValue_Type = Integer32
_PethPsePortExtMirroredDllPdRequestedPowerValue_Object = MibTableColumn
pethPsePortExtMirroredDllPdRequestedPowerValue = _PethPsePortExtMirroredDllPdRequestedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 6, 1, 4),
    _PethPsePortExtMirroredDllPdRequestedPowerValue_Type()
)
pethPsePortExtMirroredDllPdRequestedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortExtMirroredDllPdRequestedPowerValue.setStatus("current")
_PethPsePortExtDllPseAllocatedPowerValue_Type = Integer32
_PethPsePortExtDllPseAllocatedPowerValue_Object = MibTableColumn
pethPsePortExtDllPseAllocatedPowerValue = _PethPsePortExtDllPseAllocatedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 6, 1, 6),
    _PethPsePortExtDllPseAllocatedPowerValue_Type()
)
pethPsePortExtDllPseAllocatedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortExtDllPseAllocatedPowerValue.setStatus("current")


class _PethPsePortTimeRange_Type(DisplayString):
    """Custom type pethPsePortTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PethPsePortTimeRange_Type.__name__ = "DisplayString"
_PethPsePortTimeRange_Object = MibTableColumn
pethPsePortTimeRange = _PethPsePortTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 6, 1, 11),
    _PethPsePortTimeRange_Type()
)
pethPsePortTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortTimeRange.setStatus("current")


class _PethPsePortTimeRangeStatus_Type(Integer32):
    """Custom type pethPsePortTimeRangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("none", 0))
    )


_PethPsePortTimeRangeStatus_Type.__name__ = "Integer32"
_PethPsePortTimeRangeStatus_Object = MibTableColumn
pethPsePortTimeRangeStatus = _PethPsePortTimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 6, 1, 12),
    _PethPsePortTimeRangeStatus_Type()
)
pethPsePortTimeRangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortTimeRangeStatus.setStatus("current")


class _PethPsePortExtMaximumPowerValue_Type(Integer32):
    """Custom type pethPsePortExtMaximumPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 34200),
    )


_PethPsePortExtMaximumPowerValue_Type.__name__ = "Integer32"
_PethPsePortExtMaximumPowerValue_Object = MibTableColumn
pethPsePortExtMaximumPowerValue = _PethPsePortExtMaximumPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 6, 1, 13),
    _PethPsePortExtMaximumPowerValue_Type()
)
pethPsePortExtMaximumPowerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortExtMaximumPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    pethPsePortExtMaximumPowerValue.setUnits("milliwatts")
_PethPsePortExtUsedPowerValue_Type = Integer32
_PethPsePortExtUsedPowerValue_Object = MibTableColumn
pethPsePortExtUsedPowerValue = _PethPsePortExtUsedPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 28, 6, 1, 14),
    _PethPsePortExtUsedPowerValue_Type()
)
pethPsePortExtUsedPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortExtUsedPowerValue.setStatus("current")
if mibBuilder.loadTexts:
    pethPsePortExtUsedPowerValue.setUnits("milliwatts")
_StormMgt_ObjectIdentity = ObjectIdentity
stormMgt = _StormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33)
)
_McastStormMgt_ObjectIdentity = ObjectIdentity
mcastStormMgt = _McastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 1)
)
_McastStormTable_Object = MibTable
mcastStormTable = _McastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 1, 1)
)
if mibBuilder.loadTexts:
    mcastStormTable.setStatus("current")
_McastStormEntry_Object = MibTableRow
mcastStormEntry = _McastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 1, 1, 1)
)
mcastStormEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    mcastStormEntry.setStatus("current")
_McastStormIfIndex_Type = InterfaceIndex
_McastStormIfIndex_Object = MibTableColumn
mcastStormIfIndex = _McastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 1, 1, 1, 1),
    _McastStormIfIndex_Type()
)
mcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcastStormIfIndex.setStatus("current")
_McastStormStatus_Type = EnabledStatus
_McastStormStatus_Object = MibTableColumn
mcastStormStatus = _McastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 1, 1, 1, 2),
    _McastStormStatus_Type()
)
mcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastStormStatus.setStatus("current")
_McastStormPktRate_Type = Integer32
_McastStormPktRate_Object = MibTableColumn
mcastStormPktRate = _McastStormPktRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 1, 1, 1, 4),
    _McastStormPktRate_Type()
)
mcastStormPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastStormPktRate.setStatus("current")
_McastStormPktRateResolution_Type = Integer32
_McastStormPktRateResolution_Object = MibTableColumn
mcastStormPktRateResolution = _McastStormPktRateResolution_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 1, 1, 1, 8),
    _McastStormPktRateResolution_Type()
)
mcastStormPktRateResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastStormPktRateResolution.setStatus("current")
_BcastStormMgt_ObjectIdentity = ObjectIdentity
bcastStormMgt = _BcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 3)
)
_BcastStormTable_Object = MibTable
bcastStormTable = _BcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 3, 1)
)
if mibBuilder.loadTexts:
    bcastStormTable.setStatus("current")
_BcastStormEntry_Object = MibTableRow
bcastStormEntry = _BcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 3, 1, 1)
)
bcastStormEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "bcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    bcastStormEntry.setStatus("current")
_BcastStormIfIndex_Type = InterfaceIndex
_BcastStormIfIndex_Object = MibTableColumn
bcastStormIfIndex = _BcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 3, 1, 1, 1),
    _BcastStormIfIndex_Type()
)
bcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcastStormIfIndex.setStatus("current")
_BcastStormStatus_Type = EnabledStatus
_BcastStormStatus_Object = MibTableColumn
bcastStormStatus = _BcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 3, 1, 1, 2),
    _BcastStormStatus_Type()
)
bcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormStatus.setStatus("current")
_BcastStormPktRate_Type = Integer32
_BcastStormPktRate_Object = MibTableColumn
bcastStormPktRate = _BcastStormPktRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 3, 1, 1, 4),
    _BcastStormPktRate_Type()
)
bcastStormPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormPktRate.setStatus("current")
_BcastStormPktRateResolution_Type = Integer32
_BcastStormPktRateResolution_Object = MibTableColumn
bcastStormPktRateResolution = _BcastStormPktRateResolution_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 3, 1, 1, 8),
    _BcastStormPktRateResolution_Type()
)
bcastStormPktRateResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcastStormPktRateResolution.setStatus("current")
_UnknownUcastStormMgt_ObjectIdentity = ObjectIdentity
unknownUcastStormMgt = _UnknownUcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 4)
)
_UnknownUcastStormTable_Object = MibTable
unknownUcastStormTable = _UnknownUcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 4, 1)
)
if mibBuilder.loadTexts:
    unknownUcastStormTable.setStatus("current")
_UnknownUcastStormEntry_Object = MibTableRow
unknownUcastStormEntry = _UnknownUcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 4, 1, 1)
)
unknownUcastStormEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "unknownUcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    unknownUcastStormEntry.setStatus("current")
_UnknownUcastStormIfIndex_Type = InterfaceIndex
_UnknownUcastStormIfIndex_Object = MibTableColumn
unknownUcastStormIfIndex = _UnknownUcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 4, 1, 1, 1),
    _UnknownUcastStormIfIndex_Type()
)
unknownUcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unknownUcastStormIfIndex.setStatus("current")
_UnknownUcastStormStatus_Type = EnabledStatus
_UnknownUcastStormStatus_Object = MibTableColumn
unknownUcastStormStatus = _UnknownUcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 4, 1, 1, 2),
    _UnknownUcastStormStatus_Type()
)
unknownUcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownUcastStormStatus.setStatus("current")
_UnknownUcastStormPktRate_Type = Integer32
_UnknownUcastStormPktRate_Object = MibTableColumn
unknownUcastStormPktRate = _UnknownUcastStormPktRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 4, 1, 1, 4),
    _UnknownUcastStormPktRate_Type()
)
unknownUcastStormPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownUcastStormPktRate.setStatus("current")
_UnknownUcastStormPktRateResolution_Type = Integer32
_UnknownUcastStormPktRateResolution_Object = MibTableColumn
unknownUcastStormPktRateResolution = _UnknownUcastStormPktRateResolution_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 4, 1, 1, 8),
    _UnknownUcastStormPktRateResolution_Type()
)
unknownUcastStormPktRateResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unknownUcastStormPktRateResolution.setStatus("current")
_AtcMgt_ObjectIdentity = ObjectIdentity
atcMgt = _AtcMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5)
)
_AtcBcastStormTcApplyTime_Type = Integer32
_AtcBcastStormTcApplyTime_Object = MibScalar
atcBcastStormTcApplyTime = _AtcBcastStormTcApplyTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 1),
    _AtcBcastStormTcApplyTime_Type()
)
atcBcastStormTcApplyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcApplyTime.setStatus("current")
_AtcBcastStormTcReleaseTime_Type = Integer32
_AtcBcastStormTcReleaseTime_Object = MibScalar
atcBcastStormTcReleaseTime = _AtcBcastStormTcReleaseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 2),
    _AtcBcastStormTcReleaseTime_Type()
)
atcBcastStormTcReleaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcReleaseTime.setStatus("current")
_AtcBcastStormTable_Object = MibTable
atcBcastStormTable = _AtcBcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3)
)
if mibBuilder.loadTexts:
    atcBcastStormTable.setStatus("current")
_AtcBcastStormEntry_Object = MibTableRow
atcBcastStormEntry = _AtcBcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1)
)
atcBcastStormEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "atcBcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    atcBcastStormEntry.setStatus("current")
_AtcBcastStormIfIndex_Type = InterfaceIndex
_AtcBcastStormIfIndex_Object = MibTableColumn
atcBcastStormIfIndex = _AtcBcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 1),
    _AtcBcastStormIfIndex_Type()
)
atcBcastStormIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atcBcastStormIfIndex.setStatus("current")
_AtcBcastStormEnable_Type = EnabledStatus
_AtcBcastStormEnable_Object = MibTableColumn
atcBcastStormEnable = _AtcBcastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 2),
    _AtcBcastStormEnable_Type()
)
atcBcastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormEnable.setStatus("current")
_AtcBcastStormAutoRelease_Type = EnabledStatus
_AtcBcastStormAutoRelease_Object = MibTableColumn
atcBcastStormAutoRelease = _AtcBcastStormAutoRelease_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 3),
    _AtcBcastStormAutoRelease_Type()
)
atcBcastStormAutoRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAutoRelease.setStatus("current")


class _AtcBcastStormSampleType_Type(Integer32):
    """Custom type atcBcastStormSampleType based on Integer32"""
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
          ("packet-rate", 1),
          ("percent", 3))
    )


_AtcBcastStormSampleType_Type.__name__ = "Integer32"
_AtcBcastStormSampleType_Object = MibTableColumn
atcBcastStormSampleType = _AtcBcastStormSampleType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 4),
    _AtcBcastStormSampleType_Type()
)
atcBcastStormSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormSampleType.setStatus("current")
_AtcBcastStormCurrentTrafficRate_Type = Integer32
_AtcBcastStormCurrentTrafficRate_Object = MibTableColumn
atcBcastStormCurrentTrafficRate = _AtcBcastStormCurrentTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 5),
    _AtcBcastStormCurrentTrafficRate_Type()
)
atcBcastStormCurrentTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atcBcastStormCurrentTrafficRate.setStatus("current")
_AtcBcastStormAlarmFireThreshold_Type = Integer32
_AtcBcastStormAlarmFireThreshold_Object = MibTableColumn
atcBcastStormAlarmFireThreshold = _AtcBcastStormAlarmFireThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 6),
    _AtcBcastStormAlarmFireThreshold_Type()
)
atcBcastStormAlarmFireThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAlarmFireThreshold.setStatus("current")
_AtcBcastStormAlarmClearThreshold_Type = Integer32
_AtcBcastStormAlarmClearThreshold_Object = MibTableColumn
atcBcastStormAlarmClearThreshold = _AtcBcastStormAlarmClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 7),
    _AtcBcastStormAlarmClearThreshold_Type()
)
atcBcastStormAlarmClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAlarmClearThreshold.setStatus("current")


class _AtcBcastStormTcAction_Type(Integer32):
    """Custom type atcBcastStormTcAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-control", 1),
          ("shutdown", 2))
    )


_AtcBcastStormTcAction_Type.__name__ = "Integer32"
_AtcBcastStormTcAction_Object = MibTableColumn
atcBcastStormTcAction = _AtcBcastStormTcAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 8),
    _AtcBcastStormTcAction_Type()
)
atcBcastStormTcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcAction.setStatus("current")
_AtcBcastStormAlarmFireTrapStatus_Type = EnabledStatus
_AtcBcastStormAlarmFireTrapStatus_Object = MibTableColumn
atcBcastStormAlarmFireTrapStatus = _AtcBcastStormAlarmFireTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 9),
    _AtcBcastStormAlarmFireTrapStatus_Type()
)
atcBcastStormAlarmFireTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAlarmFireTrapStatus.setStatus("current")
_AtcBcastStormAlarmClearTrapStatus_Type = EnabledStatus
_AtcBcastStormAlarmClearTrapStatus_Object = MibTableColumn
atcBcastStormAlarmClearTrapStatus = _AtcBcastStormAlarmClearTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 10),
    _AtcBcastStormAlarmClearTrapStatus_Type()
)
atcBcastStormAlarmClearTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAlarmClearTrapStatus.setStatus("current")
_AtcBcastStormTcApplyTrapStatus_Type = EnabledStatus
_AtcBcastStormTcApplyTrapStatus_Object = MibTableColumn
atcBcastStormTcApplyTrapStatus = _AtcBcastStormTcApplyTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 11),
    _AtcBcastStormTcApplyTrapStatus_Type()
)
atcBcastStormTcApplyTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcApplyTrapStatus.setStatus("current")
_AtcBcastStormTcReleaseTrapStatus_Type = EnabledStatus
_AtcBcastStormTcReleaseTrapStatus_Object = MibTableColumn
atcBcastStormTcReleaseTrapStatus = _AtcBcastStormTcReleaseTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 3, 1, 12),
    _AtcBcastStormTcReleaseTrapStatus_Type()
)
atcBcastStormTcReleaseTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcReleaseTrapStatus.setStatus("current")
_AtcMcastStormTcApplyTime_Type = Integer32
_AtcMcastStormTcApplyTime_Object = MibScalar
atcMcastStormTcApplyTime = _AtcMcastStormTcApplyTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 4),
    _AtcMcastStormTcApplyTime_Type()
)
atcMcastStormTcApplyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcApplyTime.setStatus("current")
_AtcMcastStormTcReleaseTime_Type = Integer32
_AtcMcastStormTcReleaseTime_Object = MibScalar
atcMcastStormTcReleaseTime = _AtcMcastStormTcReleaseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 5),
    _AtcMcastStormTcReleaseTime_Type()
)
atcMcastStormTcReleaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcReleaseTime.setStatus("current")
_AtcMcastStormTable_Object = MibTable
atcMcastStormTable = _AtcMcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6)
)
if mibBuilder.loadTexts:
    atcMcastStormTable.setStatus("current")
_AtcMcastStormEntry_Object = MibTableRow
atcMcastStormEntry = _AtcMcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1)
)
atcMcastStormEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "atcMcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    atcMcastStormEntry.setStatus("current")
_AtcMcastStormIfIndex_Type = InterfaceIndex
_AtcMcastStormIfIndex_Object = MibTableColumn
atcMcastStormIfIndex = _AtcMcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 1),
    _AtcMcastStormIfIndex_Type()
)
atcMcastStormIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atcMcastStormIfIndex.setStatus("current")
_AtcMcastStormEnable_Type = EnabledStatus
_AtcMcastStormEnable_Object = MibTableColumn
atcMcastStormEnable = _AtcMcastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 2),
    _AtcMcastStormEnable_Type()
)
atcMcastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormEnable.setStatus("current")
_AtcMcastStormAutoRelease_Type = EnabledStatus
_AtcMcastStormAutoRelease_Object = MibTableColumn
atcMcastStormAutoRelease = _AtcMcastStormAutoRelease_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 3),
    _AtcMcastStormAutoRelease_Type()
)
atcMcastStormAutoRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAutoRelease.setStatus("current")


class _AtcMcastStormSampleType_Type(Integer32):
    """Custom type atcMcastStormSampleType based on Integer32"""
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
          ("packet-rate", 1),
          ("percent", 3))
    )


_AtcMcastStormSampleType_Type.__name__ = "Integer32"
_AtcMcastStormSampleType_Object = MibTableColumn
atcMcastStormSampleType = _AtcMcastStormSampleType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 4),
    _AtcMcastStormSampleType_Type()
)
atcMcastStormSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormSampleType.setStatus("current")
_AtcMcastStormCurrentTrafficRate_Type = Integer32
_AtcMcastStormCurrentTrafficRate_Object = MibTableColumn
atcMcastStormCurrentTrafficRate = _AtcMcastStormCurrentTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 5),
    _AtcMcastStormCurrentTrafficRate_Type()
)
atcMcastStormCurrentTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atcMcastStormCurrentTrafficRate.setStatus("current")
_AtcMcastStormAlarmFireThreshold_Type = Integer32
_AtcMcastStormAlarmFireThreshold_Object = MibTableColumn
atcMcastStormAlarmFireThreshold = _AtcMcastStormAlarmFireThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 6),
    _AtcMcastStormAlarmFireThreshold_Type()
)
atcMcastStormAlarmFireThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAlarmFireThreshold.setStatus("current")
_AtcMcastStormAlarmClearThreshold_Type = Integer32
_AtcMcastStormAlarmClearThreshold_Object = MibTableColumn
atcMcastStormAlarmClearThreshold = _AtcMcastStormAlarmClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 7),
    _AtcMcastStormAlarmClearThreshold_Type()
)
atcMcastStormAlarmClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAlarmClearThreshold.setStatus("current")


class _AtcMcastStormTcAction_Type(Integer32):
    """Custom type atcMcastStormTcAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-control", 1),
          ("shutdown", 2))
    )


_AtcMcastStormTcAction_Type.__name__ = "Integer32"
_AtcMcastStormTcAction_Object = MibTableColumn
atcMcastStormTcAction = _AtcMcastStormTcAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 8),
    _AtcMcastStormTcAction_Type()
)
atcMcastStormTcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcAction.setStatus("current")
_AtcMcastStormAlarmFireTrapStatus_Type = EnabledStatus
_AtcMcastStormAlarmFireTrapStatus_Object = MibTableColumn
atcMcastStormAlarmFireTrapStatus = _AtcMcastStormAlarmFireTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 9),
    _AtcMcastStormAlarmFireTrapStatus_Type()
)
atcMcastStormAlarmFireTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAlarmFireTrapStatus.setStatus("current")
_AtcMcastStormAlarmClearTrapStatus_Type = EnabledStatus
_AtcMcastStormAlarmClearTrapStatus_Object = MibTableColumn
atcMcastStormAlarmClearTrapStatus = _AtcMcastStormAlarmClearTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 10),
    _AtcMcastStormAlarmClearTrapStatus_Type()
)
atcMcastStormAlarmClearTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAlarmClearTrapStatus.setStatus("current")
_AtcMcastStormTcApplyTrapStatus_Type = EnabledStatus
_AtcMcastStormTcApplyTrapStatus_Object = MibTableColumn
atcMcastStormTcApplyTrapStatus = _AtcMcastStormTcApplyTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 11),
    _AtcMcastStormTcApplyTrapStatus_Type()
)
atcMcastStormTcApplyTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcApplyTrapStatus.setStatus("current")
_AtcMcastStormTcReleaseTrapStatus_Type = EnabledStatus
_AtcMcastStormTcReleaseTrapStatus_Object = MibTableColumn
atcMcastStormTcReleaseTrapStatus = _AtcMcastStormTcReleaseTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 33, 5, 6, 1, 12),
    _AtcMcastStormTcReleaseTrapStatus_Type()
)
atcMcastStormTcReleaseTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcReleaseTrapStatus.setStatus("current")
_SysResourceMgt_ObjectIdentity = ObjectIdentity
sysResourceMgt = _SysResourceMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39)
)
_CpuStatus_ObjectIdentity = ObjectIdentity
cpuStatus = _CpuStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 2)
)


class _CpuCurrentUti_Type(Integer32):
    """Custom type cpuCurrentUti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuCurrentUti_Type.__name__ = "Integer32"
_CpuCurrentUti_Object = MibScalar
cpuCurrentUti = _CpuCurrentUti_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 2, 1),
    _CpuCurrentUti_Type()
)
cpuCurrentUti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCurrentUti.setStatus("current")
if mibBuilder.loadTexts:
    cpuCurrentUti.setUnits("%")


class _CpuStatMaxUti_Type(Integer32):
    """Custom type cpuStatMaxUti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuStatMaxUti_Type.__name__ = "Integer32"
_CpuStatMaxUti_Object = MibScalar
cpuStatMaxUti = _CpuStatMaxUti_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 2, 2),
    _CpuStatMaxUti_Type()
)
cpuStatMaxUti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatMaxUti.setStatus("current")
if mibBuilder.loadTexts:
    cpuStatMaxUti.setUnits("%")


class _CpuStatAvgUti_Type(Integer32):
    """Custom type cpuStatAvgUti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuStatAvgUti_Type.__name__ = "Integer32"
_CpuStatAvgUti_Object = MibScalar
cpuStatAvgUti = _CpuStatAvgUti_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 2, 3),
    _CpuStatAvgUti_Type()
)
cpuStatAvgUti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatAvgUti.setStatus("current")
if mibBuilder.loadTexts:
    cpuStatAvgUti.setUnits("%")
_CpuPeakTime_Type = DisplayString
_CpuPeakTime_Object = MibScalar
cpuPeakTime = _CpuPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 2, 4),
    _CpuPeakTime_Type()
)
cpuPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPeakTime.setStatus("current")
_CpuPeakDuration_Type = Integer32
_CpuPeakDuration_Object = MibScalar
cpuPeakDuration = _CpuPeakDuration_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 2, 5),
    _CpuPeakDuration_Type()
)
cpuPeakDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPeakDuration.setStatus("current")
if mibBuilder.loadTexts:
    cpuPeakDuration.setUnits("second")


class _CpuUtiRisingThreshold_Type(Integer32):
    """Custom type cpuUtiRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuUtiRisingThreshold_Type.__name__ = "Integer32"
_CpuUtiRisingThreshold_Object = MibScalar
cpuUtiRisingThreshold = _CpuUtiRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 2, 6),
    _CpuUtiRisingThreshold_Type()
)
cpuUtiRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuUtiRisingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cpuUtiRisingThreshold.setUnits("%")


class _CpuUtiFallingThreshold_Type(Integer32):
    """Custom type cpuUtiFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuUtiFallingThreshold_Type.__name__ = "Integer32"
_CpuUtiFallingThreshold_Object = MibScalar
cpuUtiFallingThreshold = _CpuUtiFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 2, 7),
    _CpuUtiFallingThreshold_Type()
)
cpuUtiFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuUtiFallingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cpuUtiFallingThreshold.setUnits("%")
_MemoryStatus_ObjectIdentity = ObjectIdentity
memoryStatus = _MemoryStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 3)
)
_MemoryTotal_Type = Integer32
_MemoryTotal_Object = MibScalar
memoryTotal = _MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 3, 1),
    _MemoryTotal_Type()
)
memoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotal.setStatus("current")
_MemoryAllocated_Type = Integer32
_MemoryAllocated_Object = MibScalar
memoryAllocated = _MemoryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 3, 2),
    _MemoryAllocated_Type()
)
memoryAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAllocated.setStatus("current")
_MemoryFreed_Type = Integer32
_MemoryFreed_Object = MibScalar
memoryFreed = _MemoryFreed_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 3, 3),
    _MemoryFreed_Type()
)
memoryFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFreed.setStatus("current")


class _MemoryFreedInPercent_Type(Integer32):
    """Custom type memoryFreedInPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MemoryFreedInPercent_Type.__name__ = "Integer32"
_MemoryFreedInPercent_Object = MibScalar
memoryFreedInPercent = _MemoryFreedInPercent_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 3, 4),
    _MemoryFreedInPercent_Type()
)
memoryFreedInPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFreedInPercent.setStatus("current")


class _MemoryUtiRisingThreshold_Type(Integer32):
    """Custom type memoryUtiRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MemoryUtiRisingThreshold_Type.__name__ = "Integer32"
_MemoryUtiRisingThreshold_Object = MibScalar
memoryUtiRisingThreshold = _MemoryUtiRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 3, 5),
    _MemoryUtiRisingThreshold_Type()
)
memoryUtiRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryUtiRisingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    memoryUtiRisingThreshold.setUnits("%")


class _MemoryUtiFallingThreshold_Type(Integer32):
    """Custom type memoryUtiFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MemoryUtiFallingThreshold_Type.__name__ = "Integer32"
_MemoryUtiFallingThreshold_Object = MibScalar
memoryUtiFallingThreshold = _MemoryUtiFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 3, 6),
    _MemoryUtiFallingThreshold_Type()
)
memoryUtiFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryUtiFallingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    memoryUtiFallingThreshold.setUnits("%")
_TaskCpuTable_Object = MibTable
taskCpuTable = _TaskCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 4)
)
if mibBuilder.loadTexts:
    taskCpuTable.setStatus("current")
_TaskCpuEntry_Object = MibTableRow
taskCpuEntry = _TaskCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 4, 1)
)
taskCpuEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "taskCpuName"),
)
if mibBuilder.loadTexts:
    taskCpuEntry.setStatus("current")


class _TaskCpuName_Type(DisplayString):
    """Custom type taskCpuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TaskCpuName_Type.__name__ = "DisplayString"
_TaskCpuName_Object = MibTableColumn
taskCpuName = _TaskCpuName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 4, 1, 1),
    _TaskCpuName_Type()
)
taskCpuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    taskCpuName.setStatus("current")


class _TaskCpuCurrentUti_Type(Integer32):
    """Custom type taskCpuCurrentUti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TaskCpuCurrentUti_Type.__name__ = "Integer32"
_TaskCpuCurrentUti_Object = MibTableColumn
taskCpuCurrentUti = _TaskCpuCurrentUti_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 4, 1, 2),
    _TaskCpuCurrentUti_Type()
)
taskCpuCurrentUti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskCpuCurrentUti.setStatus("current")


class _TaskCpuStatMaxUti_Type(Integer32):
    """Custom type taskCpuStatMaxUti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TaskCpuStatMaxUti_Type.__name__ = "Integer32"
_TaskCpuStatMaxUti_Object = MibTableColumn
taskCpuStatMaxUti = _TaskCpuStatMaxUti_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 4, 1, 3),
    _TaskCpuStatMaxUti_Type()
)
taskCpuStatMaxUti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskCpuStatMaxUti.setStatus("current")


class _TaskCpuStatAvgUti_Type(Integer32):
    """Custom type taskCpuStatAvgUti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TaskCpuStatAvgUti_Type.__name__ = "Integer32"
_TaskCpuStatAvgUti_Object = MibTableColumn
taskCpuStatAvgUti = _TaskCpuStatAvgUti_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 4, 1, 4),
    _TaskCpuStatAvgUti_Type()
)
taskCpuStatAvgUti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskCpuStatAvgUti.setStatus("current")
_CpuGuard_ObjectIdentity = ObjectIdentity
cpuGuard = _CpuGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 5)
)
_CpuGuardStatus_Type = EnabledStatus
_CpuGuardStatus_Object = MibScalar
cpuGuardStatus = _CpuGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 5, 1),
    _CpuGuardStatus_Type()
)
cpuGuardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuGuardStatus.setStatus("current")


class _CpuGuardHighWatermark_Type(Integer32):
    """Custom type cpuGuardHighWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_CpuGuardHighWatermark_Type.__name__ = "Integer32"
_CpuGuardHighWatermark_Object = MibScalar
cpuGuardHighWatermark = _CpuGuardHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 5, 2),
    _CpuGuardHighWatermark_Type()
)
cpuGuardHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuGuardHighWatermark.setStatus("current")


class _CpuGuardLowWatermark_Type(Integer32):
    """Custom type cpuGuardLowWatermark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_CpuGuardLowWatermark_Type.__name__ = "Integer32"
_CpuGuardLowWatermark_Object = MibScalar
cpuGuardLowWatermark = _CpuGuardLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 5, 3),
    _CpuGuardLowWatermark_Type()
)
cpuGuardLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuGuardLowWatermark.setStatus("current")


class _CpuGuardMaxThreshold_Type(Integer32):
    """Custom type cpuGuardMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CpuGuardMaxThreshold_Type.__name__ = "Integer32"
_CpuGuardMaxThreshold_Object = MibScalar
cpuGuardMaxThreshold = _CpuGuardMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 5, 4),
    _CpuGuardMaxThreshold_Type()
)
cpuGuardMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuGuardMaxThreshold.setStatus("current")


class _CpuGuardMinThreshold_Type(Integer32):
    """Custom type cpuGuardMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CpuGuardMinThreshold_Type.__name__ = "Integer32"
_CpuGuardMinThreshold_Object = MibScalar
cpuGuardMinThreshold = _CpuGuardMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 5, 5),
    _CpuGuardMinThreshold_Type()
)
cpuGuardMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuGuardMinThreshold.setStatus("current")
_CpuGuardTrapStatus_Type = EnabledStatus
_CpuGuardTrapStatus_Object = MibScalar
cpuGuardTrapStatus = _CpuGuardTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 5, 6),
    _CpuGuardTrapStatus_Type()
)
cpuGuardTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuGuardTrapStatus.setStatus("current")


class _CpuGuardCurrentThreshold_Type(Integer32):
    """Custom type cpuGuardCurrentThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_CpuGuardCurrentThreshold_Type.__name__ = "Integer32"
_CpuGuardCurrentThreshold_Object = MibScalar
cpuGuardCurrentThreshold = _CpuGuardCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 39, 5, 7),
    _CpuGuardCurrentThreshold_Type()
)
cpuGuardCurrentThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuGuardCurrentThreshold.setStatus("current")
_MvrMgt_ObjectIdentity = ObjectIdentity
mvrMgt = _MvrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44)
)


class _MvrForwardingPriority_Type(Integer32):
    """Custom type mvrForwardingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(65535, 65535),
    )


_MvrForwardingPriority_Type.__name__ = "Integer32"
_MvrForwardingPriority_Object = MibScalar
mvrForwardingPriority = _MvrForwardingPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 18),
    _MvrForwardingPriority_Type()
)
mvrForwardingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrForwardingPriority.setStatus("current")
_MvrDomainTable_Object = MibTable
mvrDomainTable = _MvrDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 20)
)
if mibBuilder.loadTexts:
    mvrDomainTable.setStatus("current")
_MvrDomainEntry_Object = MibTableRow
mvrDomainEntry = _MvrDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 20, 1)
)
mvrDomainEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mvrDomainId"),
)
if mibBuilder.loadTexts:
    mvrDomainEntry.setStatus("current")


class _MvrDomainId_Type(Integer32):
    """Custom type mvrDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MvrDomainId_Type.__name__ = "Integer32"
_MvrDomainId_Object = MibTableColumn
mvrDomainId = _MvrDomainId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 20, 1, 1),
    _MvrDomainId_Type()
)
mvrDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrDomainId.setStatus("current")
_MvrDomainStatus_Type = EnabledStatus
_MvrDomainStatus_Object = MibTableColumn
mvrDomainStatus = _MvrDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 20, 1, 2),
    _MvrDomainStatus_Type()
)
mvrDomainStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrDomainStatus.setStatus("current")


class _MvrDomainRunningStatus_Type(Integer32):
    """Custom type mvrDomainRunningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MvrDomainRunningStatus_Type.__name__ = "Integer32"
_MvrDomainRunningStatus_Object = MibTableColumn
mvrDomainRunningStatus = _MvrDomainRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 20, 1, 3),
    _MvrDomainRunningStatus_Type()
)
mvrDomainRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrDomainRunningStatus.setStatus("current")
_MvrDomainVlanId_Type = VlanIndex
_MvrDomainVlanId_Object = MibTableColumn
mvrDomainVlanId = _MvrDomainVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 20, 1, 4),
    _MvrDomainVlanId_Type()
)
mvrDomainVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrDomainVlanId.setStatus("current")
_MvrDomainUpstreamSourceIp_Type = IpAddress
_MvrDomainUpstreamSourceIp_Object = MibTableColumn
mvrDomainUpstreamSourceIp = _MvrDomainUpstreamSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 20, 1, 5),
    _MvrDomainUpstreamSourceIp_Type()
)
mvrDomainUpstreamSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrDomainUpstreamSourceIp.setStatus("current")
_MvrDomainClearDynamicGroups_Type = TruthValue
_MvrDomainClearDynamicGroups_Object = MibTableColumn
mvrDomainClearDynamicGroups = _MvrDomainClearDynamicGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 20, 1, 6),
    _MvrDomainClearDynamicGroups_Type()
)
mvrDomainClearDynamicGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrDomainClearDynamicGroups.setStatus("current")
_MvrDomainPortTable_Object = MibTable
mvrDomainPortTable = _MvrDomainPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 21)
)
if mibBuilder.loadTexts:
    mvrDomainPortTable.setStatus("current")
_MvrDomainPortEntry_Object = MibTableRow
mvrDomainPortEntry = _MvrDomainPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 21, 1)
)
mvrDomainPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mvrPortDomainId"),
    (0, "ECS2100-28PP-MIB", "mvrDomainIfIndex"),
)
if mibBuilder.loadTexts:
    mvrDomainPortEntry.setStatus("current")


class _MvrPortDomainId_Type(Integer32):
    """Custom type mvrPortDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MvrPortDomainId_Type.__name__ = "Integer32"
_MvrPortDomainId_Object = MibTableColumn
mvrPortDomainId = _MvrPortDomainId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 21, 1, 1),
    _MvrPortDomainId_Type()
)
mvrPortDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrPortDomainId.setStatus("current")
_MvrDomainIfIndex_Type = InterfaceIndex
_MvrDomainIfIndex_Object = MibTableColumn
mvrDomainIfIndex = _MvrDomainIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 21, 1, 2),
    _MvrDomainIfIndex_Type()
)
mvrDomainIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrDomainIfIndex.setStatus("current")


class _MvrDomainPortType_Type(Integer32):
    """Custom type mvrDomainPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("receiver", 2),
          ("source", 1))
    )


_MvrDomainPortType_Type.__name__ = "Integer32"
_MvrDomainPortType_Object = MibTableColumn
mvrDomainPortType = _MvrDomainPortType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 21, 1, 3),
    _MvrDomainPortType_Type()
)
mvrDomainPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrDomainPortType.setStatus("current")
_MvrDomainPortImmediateLeave_Type = EnabledStatus
_MvrDomainPortImmediateLeave_Object = MibTableColumn
mvrDomainPortImmediateLeave = _MvrDomainPortImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 21, 1, 4),
    _MvrDomainPortImmediateLeave_Type()
)
mvrDomainPortImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrDomainPortImmediateLeave.setStatus("current")


class _MvrDomainPortActive_Type(Integer32):
    """Custom type mvrDomainPortActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MvrDomainPortActive_Type.__name__ = "Integer32"
_MvrDomainPortActive_Object = MibTableColumn
mvrDomainPortActive = _MvrDomainPortActive_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 21, 1, 5),
    _MvrDomainPortActive_Type()
)
mvrDomainPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrDomainPortActive.setStatus("current")
_MvrDomainPortImmediateLeaveByHostIp_Type = EnabledStatus
_MvrDomainPortImmediateLeaveByHostIp_Object = MibTableColumn
mvrDomainPortImmediateLeaveByHostIp = _MvrDomainPortImmediateLeaveByHostIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 21, 1, 6),
    _MvrDomainPortImmediateLeaveByHostIp_Type()
)
mvrDomainPortImmediateLeaveByHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrDomainPortImmediateLeaveByHostIp.setStatus("current")
_MvrProfileTable_ObjectIdentity = ObjectIdentity
mvrProfileTable = _MvrProfileTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22)
)
_MvrProfileCtlTable_Object = MibTable
mvrProfileCtlTable = _MvrProfileCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 1)
)
if mibBuilder.loadTexts:
    mvrProfileCtlTable.setStatus("current")
_MvrProfileCtlEntry_Object = MibTableRow
mvrProfileCtlEntry = _MvrProfileCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 1, 1)
)
mvrProfileCtlEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mvrProfileCtlId"),
)
if mibBuilder.loadTexts:
    mvrProfileCtlEntry.setStatus("current")


class _MvrProfileCtlId_Type(Integer32):
    """Custom type mvrProfileCtlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MvrProfileCtlId_Type.__name__ = "Integer32"
_MvrProfileCtlId_Object = MibTableColumn
mvrProfileCtlId = _MvrProfileCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 1, 1, 1),
    _MvrProfileCtlId_Type()
)
mvrProfileCtlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrProfileCtlId.setStatus("current")
_MvrProfileName_Type = OctetString
_MvrProfileName_Object = MibTableColumn
mvrProfileName = _MvrProfileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 1, 1, 2),
    _MvrProfileName_Type()
)
mvrProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrProfileName.setStatus("current")


class _MvrProfileCtlAction_Type(Integer32):
    """Custom type mvrProfileCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("destory", 2),
          ("noAction", 0))
    )


_MvrProfileCtlAction_Type.__name__ = "Integer32"
_MvrProfileCtlAction_Object = MibTableColumn
mvrProfileCtlAction = _MvrProfileCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 1, 1, 5),
    _MvrProfileCtlAction_Type()
)
mvrProfileCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrProfileCtlAction.setStatus("current")
_MvrProfileGroupCtlTable_Object = MibTable
mvrProfileGroupCtlTable = _MvrProfileGroupCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 2)
)
if mibBuilder.loadTexts:
    mvrProfileGroupCtlTable.setStatus("current")
_MvrProfileGroupCtlEntry_Object = MibTableRow
mvrProfileGroupCtlEntry = _MvrProfileGroupCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 2, 1)
)
mvrProfileGroupCtlEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mvrProfileGropuCtlProfileId"),
    (0, "ECS2100-28PP-MIB", "mvrProfileGroupCtlId"),
)
if mibBuilder.loadTexts:
    mvrProfileGroupCtlEntry.setStatus("current")


class _MvrProfileGropuCtlProfileId_Type(Integer32):
    """Custom type mvrProfileGropuCtlProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MvrProfileGropuCtlProfileId_Type.__name__ = "Integer32"
_MvrProfileGropuCtlProfileId_Object = MibTableColumn
mvrProfileGropuCtlProfileId = _MvrProfileGropuCtlProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 2, 1, 1),
    _MvrProfileGropuCtlProfileId_Type()
)
mvrProfileGropuCtlProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrProfileGropuCtlProfileId.setStatus("current")


class _MvrProfileGroupCtlId_Type(Integer32):
    """Custom type mvrProfileGroupCtlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MvrProfileGroupCtlId_Type.__name__ = "Integer32"
_MvrProfileGroupCtlId_Object = MibTableColumn
mvrProfileGroupCtlId = _MvrProfileGroupCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 2, 1, 2),
    _MvrProfileGroupCtlId_Type()
)
mvrProfileGroupCtlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrProfileGroupCtlId.setStatus("current")
_MvrProfileGroupStartIPAddress_Type = IpAddress
_MvrProfileGroupStartIPAddress_Object = MibTableColumn
mvrProfileGroupStartIPAddress = _MvrProfileGroupStartIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 2, 1, 3),
    _MvrProfileGroupStartIPAddress_Type()
)
mvrProfileGroupStartIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrProfileGroupStartIPAddress.setStatus("current")
_MvrProfileGroupEndIPAddress_Type = IpAddress
_MvrProfileGroupEndIPAddress_Object = MibTableColumn
mvrProfileGroupEndIPAddress = _MvrProfileGroupEndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 2, 1, 4),
    _MvrProfileGroupEndIPAddress_Type()
)
mvrProfileGroupEndIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrProfileGroupEndIPAddress.setStatus("current")


class _MvrProfileGroupCtlAction_Type(Integer32):
    """Custom type mvrProfileGroupCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("destory", 2),
          ("noAction", 0))
    )


_MvrProfileGroupCtlAction_Type.__name__ = "Integer32"
_MvrProfileGroupCtlAction_Object = MibTableColumn
mvrProfileGroupCtlAction = _MvrProfileGroupCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 22, 2, 1, 5),
    _MvrProfileGroupCtlAction_Type()
)
mvrProfileGroupCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrProfileGroupCtlAction.setStatus("current")
_MvrDomainAssociatedProfileTable_Object = MibTable
mvrDomainAssociatedProfileTable = _MvrDomainAssociatedProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 23)
)
if mibBuilder.loadTexts:
    mvrDomainAssociatedProfileTable.setStatus("current")
_MvrDomainAssociatedProfileEntry_Object = MibTableRow
mvrDomainAssociatedProfileEntry = _MvrDomainAssociatedProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 23, 1)
)
mvrDomainAssociatedProfileEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mvrProfileDomainId"),
    (0, "ECS2100-28PP-MIB", "mvrProfileId"),
)
if mibBuilder.loadTexts:
    mvrDomainAssociatedProfileEntry.setStatus("current")


class _MvrProfileDomainId_Type(Integer32):
    """Custom type mvrProfileDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MvrProfileDomainId_Type.__name__ = "Integer32"
_MvrProfileDomainId_Object = MibTableColumn
mvrProfileDomainId = _MvrProfileDomainId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 23, 1, 1),
    _MvrProfileDomainId_Type()
)
mvrProfileDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrProfileDomainId.setStatus("current")


class _MvrProfileId_Type(Integer32):
    """Custom type mvrProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MvrProfileId_Type.__name__ = "Integer32"
_MvrProfileId_Object = MibTableColumn
mvrProfileId = _MvrProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 23, 1, 2),
    _MvrProfileId_Type()
)
mvrProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrProfileId.setStatus("current")


class _MvrProfileAction_Type(Integer32):
    """Custom type mvrProfileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("destory", 2),
          ("noAction", 0))
    )


_MvrProfileAction_Type.__name__ = "Integer32"
_MvrProfileAction_Object = MibTableColumn
mvrProfileAction = _MvrProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 23, 1, 3),
    _MvrProfileAction_Type()
)
mvrProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrProfileAction.setStatus("current")
_MvrDomainGroupStaticTable_Object = MibTable
mvrDomainGroupStaticTable = _MvrDomainGroupStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 24)
)
if mibBuilder.loadTexts:
    mvrDomainGroupStaticTable.setStatus("current")
_MvrDomainGroupStaticEntry_Object = MibTableRow
mvrDomainGroupStaticEntry = _MvrDomainGroupStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 24, 1)
)
mvrDomainGroupStaticEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mvrGroupStaticDomainId"),
    (0, "ECS2100-28PP-MIB", "mvrDomainGroupStaticAddress"),
    (0, "ECS2100-28PP-MIB", "mvrDomainGroupStaticReceiverVlan"),
)
if mibBuilder.loadTexts:
    mvrDomainGroupStaticEntry.setStatus("current")


class _MvrGroupStaticDomainId_Type(Integer32):
    """Custom type mvrGroupStaticDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MvrGroupStaticDomainId_Type.__name__ = "Integer32"
_MvrGroupStaticDomainId_Object = MibTableColumn
mvrGroupStaticDomainId = _MvrGroupStaticDomainId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 24, 1, 1),
    _MvrGroupStaticDomainId_Type()
)
mvrGroupStaticDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupStaticDomainId.setStatus("current")
_MvrDomainGroupStaticAddress_Type = IpAddress
_MvrDomainGroupStaticAddress_Object = MibTableColumn
mvrDomainGroupStaticAddress = _MvrDomainGroupStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 24, 1, 2),
    _MvrDomainGroupStaticAddress_Type()
)
mvrDomainGroupStaticAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrDomainGroupStaticAddress.setStatus("current")


class _MvrDomainGroupStaticReceiverVlan_Type(Integer32):
    """Custom type mvrDomainGroupStaticReceiverVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_MvrDomainGroupStaticReceiverVlan_Type.__name__ = "Integer32"
_MvrDomainGroupStaticReceiverVlan_Object = MibTableColumn
mvrDomainGroupStaticReceiverVlan = _MvrDomainGroupStaticReceiverVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 24, 1, 3),
    _MvrDomainGroupStaticReceiverVlan_Type()
)
mvrDomainGroupStaticReceiverVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrDomainGroupStaticReceiverVlan.setStatus("current")
_MvrDomainGroupStaticPorts_Type = PortList
_MvrDomainGroupStaticPorts_Object = MibTableColumn
mvrDomainGroupStaticPorts = _MvrDomainGroupStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 24, 1, 4),
    _MvrDomainGroupStaticPorts_Type()
)
mvrDomainGroupStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrDomainGroupStaticPorts.setStatus("current")
_MvrDomainGroupCurrentTable_Object = MibTable
mvrDomainGroupCurrentTable = _MvrDomainGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 25)
)
if mibBuilder.loadTexts:
    mvrDomainGroupCurrentTable.setStatus("current")
_MvrDomainGroupCurrentEntry_Object = MibTableRow
mvrDomainGroupCurrentEntry = _MvrDomainGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 25, 1)
)
mvrDomainGroupCurrentEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mvrGroupCurrenDomainId"),
    (0, "ECS2100-28PP-MIB", "mvrDomainGroupCurrentAddress"),
    (0, "ECS2100-28PP-MIB", "mvrDomainGroupCurrentReceiverVlan"),
)
if mibBuilder.loadTexts:
    mvrDomainGroupCurrentEntry.setStatus("current")


class _MvrGroupCurrenDomainId_Type(Integer32):
    """Custom type mvrGroupCurrenDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MvrGroupCurrenDomainId_Type.__name__ = "Integer32"
_MvrGroupCurrenDomainId_Object = MibTableColumn
mvrGroupCurrenDomainId = _MvrGroupCurrenDomainId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 25, 1, 1),
    _MvrGroupCurrenDomainId_Type()
)
mvrGroupCurrenDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupCurrenDomainId.setStatus("current")
_MvrDomainGroupCurrentAddress_Type = IpAddress
_MvrDomainGroupCurrentAddress_Object = MibTableColumn
mvrDomainGroupCurrentAddress = _MvrDomainGroupCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 25, 1, 2),
    _MvrDomainGroupCurrentAddress_Type()
)
mvrDomainGroupCurrentAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrDomainGroupCurrentAddress.setStatus("current")


class _MvrDomainGroupCurrentReceiverVlan_Type(Integer32):
    """Custom type mvrDomainGroupCurrentReceiverVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_MvrDomainGroupCurrentReceiverVlan_Type.__name__ = "Integer32"
_MvrDomainGroupCurrentReceiverVlan_Object = MibTableColumn
mvrDomainGroupCurrentReceiverVlan = _MvrDomainGroupCurrentReceiverVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 25, 1, 3),
    _MvrDomainGroupCurrentReceiverVlan_Type()
)
mvrDomainGroupCurrentReceiverVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrDomainGroupCurrentReceiverVlan.setStatus("current")
_MvrDomainGroupCurrentPorts_Type = PortList
_MvrDomainGroupCurrentPorts_Object = MibTableColumn
mvrDomainGroupCurrentPorts = _MvrDomainGroupCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 25, 1, 4),
    _MvrDomainGroupCurrentPorts_Type()
)
mvrDomainGroupCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrDomainGroupCurrentPorts.setStatus("current")
_MvrProxySwitching_Type = EnabledStatus
_MvrProxySwitching_Object = MibScalar
mvrProxySwitching = _MvrProxySwitching_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 27),
    _MvrProxySwitching_Type()
)
mvrProxySwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrProxySwitching.setStatus("current")
_MvrRobustnessValue_Type = Integer32
_MvrRobustnessValue_Object = MibScalar
mvrRobustnessValue = _MvrRobustnessValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 28),
    _MvrRobustnessValue_Type()
)
mvrRobustnessValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrRobustnessValue.setStatus("current")
_MvrProxyQueryInterval_Type = Integer32
_MvrProxyQueryInterval_Object = MibScalar
mvrProxyQueryInterval = _MvrProxyQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 29),
    _MvrProxyQueryInterval_Type()
)
mvrProxyQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrProxyQueryInterval.setStatus("current")


class _MvrSourcePortmode_Type(Integer32):
    """Custom type mvrSourcePortmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("forward", 2))
    )


_MvrSourcePortmode_Type.__name__ = "Integer32"
_MvrSourcePortmode_Object = MibScalar
mvrSourcePortmode = _MvrSourcePortmode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 30),
    _MvrSourcePortmode_Type()
)
mvrSourcePortmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrSourcePortmode.setStatus("current")
_MvrPortStatisticsTable_Object = MibTable
mvrPortStatisticsTable = _MvrPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32)
)
if mibBuilder.loadTexts:
    mvrPortStatisticsTable.setStatus("current")
_MvrPortStatisticsEntry_Object = MibTableRow
mvrPortStatisticsEntry = _MvrPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1)
)
mvrPortStatisticsEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mvrPortStatisticsDomainId"),
    (0, "ECS2100-28PP-MIB", "mvrPortStatisticsPortIndex"),
)
if mibBuilder.loadTexts:
    mvrPortStatisticsEntry.setStatus("current")


class _MvrPortStatisticsDomainId_Type(Integer32):
    """Custom type mvrPortStatisticsDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MvrPortStatisticsDomainId_Type.__name__ = "Integer32"
_MvrPortStatisticsDomainId_Object = MibTableColumn
mvrPortStatisticsDomainId = _MvrPortStatisticsDomainId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 1),
    _MvrPortStatisticsDomainId_Type()
)
mvrPortStatisticsDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrPortStatisticsDomainId.setStatus("current")
_MvrPortStatisticsPortIndex_Type = InterfaceIndex
_MvrPortStatisticsPortIndex_Object = MibTableColumn
mvrPortStatisticsPortIndex = _MvrPortStatisticsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 2),
    _MvrPortStatisticsPortIndex_Type()
)
mvrPortStatisticsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrPortStatisticsPortIndex.setStatus("current")
_MvrPortStatisticsNumGroups_Type = Unsigned32
_MvrPortStatisticsNumGroups_Object = MibTableColumn
mvrPortStatisticsNumGroups = _MvrPortStatisticsNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 3),
    _MvrPortStatisticsNumGroups_Type()
)
mvrPortStatisticsNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumGroups.setStatus("current")
_MvrPortStatisticsNumJoinSend_Type = Unsigned32
_MvrPortStatisticsNumJoinSend_Object = MibTableColumn
mvrPortStatisticsNumJoinSend = _MvrPortStatisticsNumJoinSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 4),
    _MvrPortStatisticsNumJoinSend_Type()
)
mvrPortStatisticsNumJoinSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumJoinSend.setStatus("current")
_MvrPortStatisticsNumJoins_Type = Unsigned32
_MvrPortStatisticsNumJoins_Object = MibTableColumn
mvrPortStatisticsNumJoins = _MvrPortStatisticsNumJoins_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 5),
    _MvrPortStatisticsNumJoins_Type()
)
mvrPortStatisticsNumJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumJoins.setStatus("current")
_MvrPortStatisticsNumJoinSuccess_Type = Unsigned32
_MvrPortStatisticsNumJoinSuccess_Object = MibTableColumn
mvrPortStatisticsNumJoinSuccess = _MvrPortStatisticsNumJoinSuccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 6),
    _MvrPortStatisticsNumJoinSuccess_Type()
)
mvrPortStatisticsNumJoinSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumJoinSuccess.setStatus("current")
_MvrPortStatisticsNumLeavesSend_Type = Unsigned32
_MvrPortStatisticsNumLeavesSend_Object = MibTableColumn
mvrPortStatisticsNumLeavesSend = _MvrPortStatisticsNumLeavesSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 7),
    _MvrPortStatisticsNumLeavesSend_Type()
)
mvrPortStatisticsNumLeavesSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumLeavesSend.setStatus("current")
_MvrPortStatisticsNumLeaves_Type = Unsigned32
_MvrPortStatisticsNumLeaves_Object = MibTableColumn
mvrPortStatisticsNumLeaves = _MvrPortStatisticsNumLeaves_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 8),
    _MvrPortStatisticsNumLeaves_Type()
)
mvrPortStatisticsNumLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumLeaves.setStatus("current")
_MvrPortStatisticsNumGeneralQuerySend_Type = Unsigned32
_MvrPortStatisticsNumGeneralQuerySend_Object = MibTableColumn
mvrPortStatisticsNumGeneralQuerySend = _MvrPortStatisticsNumGeneralQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 9),
    _MvrPortStatisticsNumGeneralQuerySend_Type()
)
mvrPortStatisticsNumGeneralQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumGeneralQuerySend.setStatus("current")
_MvrPortStatisticsNumGeneralQueryRecevied_Type = Unsigned32
_MvrPortStatisticsNumGeneralQueryRecevied_Object = MibTableColumn
mvrPortStatisticsNumGeneralQueryRecevied = _MvrPortStatisticsNumGeneralQueryRecevied_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 10),
    _MvrPortStatisticsNumGeneralQueryRecevied_Type()
)
mvrPortStatisticsNumGeneralQueryRecevied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumGeneralQueryRecevied.setStatus("current")
_MvrPortStatisticsNumSepcificQuerySend_Type = Unsigned32
_MvrPortStatisticsNumSepcificQuerySend_Object = MibTableColumn
mvrPortStatisticsNumSepcificQuerySend = _MvrPortStatisticsNumSepcificQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 11),
    _MvrPortStatisticsNumSepcificQuerySend_Type()
)
mvrPortStatisticsNumSepcificQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumSepcificQuerySend.setStatus("current")
_MvrPortStatisticsNumSpecificQueryReceived_Type = Unsigned32
_MvrPortStatisticsNumSpecificQueryReceived_Object = MibTableColumn
mvrPortStatisticsNumSpecificQueryReceived = _MvrPortStatisticsNumSpecificQueryReceived_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 12),
    _MvrPortStatisticsNumSpecificQueryReceived_Type()
)
mvrPortStatisticsNumSpecificQueryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumSpecificQueryReceived.setStatus("current")
_MvrPortStatisticsNumInvalidReport_Type = Unsigned32
_MvrPortStatisticsNumInvalidReport_Object = MibTableColumn
mvrPortStatisticsNumInvalidReport = _MvrPortStatisticsNumInvalidReport_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 13),
    _MvrPortStatisticsNumInvalidReport_Type()
)
mvrPortStatisticsNumInvalidReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatisticsNumInvalidReport.setStatus("current")
_MvrPortStatisticsClearStatistics_Type = TruthValue
_MvrPortStatisticsClearStatistics_Object = MibTableColumn
mvrPortStatisticsClearStatistics = _MvrPortStatisticsClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 32, 1, 14),
    _MvrPortStatisticsClearStatistics_Type()
)
mvrPortStatisticsClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortStatisticsClearStatistics.setStatus("current")
_MvrVlanStatisticsTable_Object = MibTable
mvrVlanStatisticsTable = _MvrVlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33)
)
if mibBuilder.loadTexts:
    mvrVlanStatisticsTable.setStatus("current")
_MvrVlanStatisticsEntry_Object = MibTableRow
mvrVlanStatisticsEntry = _MvrVlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1)
)
mvrVlanStatisticsEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mvrVlanStatisticsDomainId"),
    (0, "ECS2100-28PP-MIB", "mvrVlanStatisticsVlanId"),
)
if mibBuilder.loadTexts:
    mvrVlanStatisticsEntry.setStatus("current")


class _MvrVlanStatisticsDomainId_Type(Integer32):
    """Custom type mvrVlanStatisticsDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MvrVlanStatisticsDomainId_Type.__name__ = "Integer32"
_MvrVlanStatisticsDomainId_Object = MibTableColumn
mvrVlanStatisticsDomainId = _MvrVlanStatisticsDomainId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 1),
    _MvrVlanStatisticsDomainId_Type()
)
mvrVlanStatisticsDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrVlanStatisticsDomainId.setStatus("current")
_MvrVlanStatisticsVlanId_Type = VlanIndex
_MvrVlanStatisticsVlanId_Object = MibTableColumn
mvrVlanStatisticsVlanId = _MvrVlanStatisticsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 2),
    _MvrVlanStatisticsVlanId_Type()
)
mvrVlanStatisticsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrVlanStatisticsVlanId.setStatus("current")
_MvrVlanStatisticsNumGroups_Type = Unsigned32
_MvrVlanStatisticsNumGroups_Object = MibTableColumn
mvrVlanStatisticsNumGroups = _MvrVlanStatisticsNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 3),
    _MvrVlanStatisticsNumGroups_Type()
)
mvrVlanStatisticsNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumGroups.setStatus("current")
_MvrVlanStatisticsNumJoinSend_Type = Unsigned32
_MvrVlanStatisticsNumJoinSend_Object = MibTableColumn
mvrVlanStatisticsNumJoinSend = _MvrVlanStatisticsNumJoinSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 4),
    _MvrVlanStatisticsNumJoinSend_Type()
)
mvrVlanStatisticsNumJoinSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumJoinSend.setStatus("current")
_MvrVlanStatisticsNumJoins_Type = Unsigned32
_MvrVlanStatisticsNumJoins_Object = MibTableColumn
mvrVlanStatisticsNumJoins = _MvrVlanStatisticsNumJoins_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 5),
    _MvrVlanStatisticsNumJoins_Type()
)
mvrVlanStatisticsNumJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumJoins.setStatus("current")
_MvrVlanStatisticsNumJoinSuccess_Type = Unsigned32
_MvrVlanStatisticsNumJoinSuccess_Object = MibTableColumn
mvrVlanStatisticsNumJoinSuccess = _MvrVlanStatisticsNumJoinSuccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 6),
    _MvrVlanStatisticsNumJoinSuccess_Type()
)
mvrVlanStatisticsNumJoinSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumJoinSuccess.setStatus("current")
_MvrVlanStatisticsNumLeavesSend_Type = Unsigned32
_MvrVlanStatisticsNumLeavesSend_Object = MibTableColumn
mvrVlanStatisticsNumLeavesSend = _MvrVlanStatisticsNumLeavesSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 7),
    _MvrVlanStatisticsNumLeavesSend_Type()
)
mvrVlanStatisticsNumLeavesSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumLeavesSend.setStatus("current")
_MvrVlanStatisticsNumLeaves_Type = Unsigned32
_MvrVlanStatisticsNumLeaves_Object = MibTableColumn
mvrVlanStatisticsNumLeaves = _MvrVlanStatisticsNumLeaves_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 8),
    _MvrVlanStatisticsNumLeaves_Type()
)
mvrVlanStatisticsNumLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumLeaves.setStatus("current")
_MvrVlanStatisticsNumGeneralQuerySend_Type = Unsigned32
_MvrVlanStatisticsNumGeneralQuerySend_Object = MibTableColumn
mvrVlanStatisticsNumGeneralQuerySend = _MvrVlanStatisticsNumGeneralQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 9),
    _MvrVlanStatisticsNumGeneralQuerySend_Type()
)
mvrVlanStatisticsNumGeneralQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumGeneralQuerySend.setStatus("current")
_MvrVlanStatisticsNumGeneralQueryRecevied_Type = Unsigned32
_MvrVlanStatisticsNumGeneralQueryRecevied_Object = MibTableColumn
mvrVlanStatisticsNumGeneralQueryRecevied = _MvrVlanStatisticsNumGeneralQueryRecevied_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 10),
    _MvrVlanStatisticsNumGeneralQueryRecevied_Type()
)
mvrVlanStatisticsNumGeneralQueryRecevied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumGeneralQueryRecevied.setStatus("current")
_MvrVlanStatisticsNumSepcificQuerySend_Type = Unsigned32
_MvrVlanStatisticsNumSepcificQuerySend_Object = MibTableColumn
mvrVlanStatisticsNumSepcificQuerySend = _MvrVlanStatisticsNumSepcificQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 11),
    _MvrVlanStatisticsNumSepcificQuerySend_Type()
)
mvrVlanStatisticsNumSepcificQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumSepcificQuerySend.setStatus("current")
_MvrVlanStatisticsNumSpecificQueryReceived_Type = Unsigned32
_MvrVlanStatisticsNumSpecificQueryReceived_Object = MibTableColumn
mvrVlanStatisticsNumSpecificQueryReceived = _MvrVlanStatisticsNumSpecificQueryReceived_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 12),
    _MvrVlanStatisticsNumSpecificQueryReceived_Type()
)
mvrVlanStatisticsNumSpecificQueryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumSpecificQueryReceived.setStatus("current")
_MvrVlanStatisticsNumInvalidReport_Type = Unsigned32
_MvrVlanStatisticsNumInvalidReport_Object = MibTableColumn
mvrVlanStatisticsNumInvalidReport = _MvrVlanStatisticsNumInvalidReport_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 13),
    _MvrVlanStatisticsNumInvalidReport_Type()
)
mvrVlanStatisticsNumInvalidReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrVlanStatisticsNumInvalidReport.setStatus("current")
_MvrVlanStatisticsClearStatistics_Type = TruthValue
_MvrVlanStatisticsClearStatistics_Object = MibTableColumn
mvrVlanStatisticsClearStatistics = _MvrVlanStatisticsClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 44, 33, 1, 14),
    _MvrVlanStatisticsClearStatistics_Type()
)
mvrVlanStatisticsClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrVlanStatisticsClearStatistics.setStatus("current")
_DhcpSnoopMgt_ObjectIdentity = ObjectIdentity
dhcpSnoopMgt = _DhcpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46)
)
_DhcpSnoopGlobal_ObjectIdentity = ObjectIdentity
dhcpSnoopGlobal = _DhcpSnoopGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 1)
)
_DhcpSnoopEnable_Type = EnabledStatus
_DhcpSnoopEnable_Object = MibScalar
dhcpSnoopEnable = _DhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 1, 1),
    _DhcpSnoopEnable_Type()
)
dhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopEnable.setStatus("current")
_DhcpSnoopVerifyMacAddressEnable_Type = EnabledStatus
_DhcpSnoopVerifyMacAddressEnable_Object = MibScalar
dhcpSnoopVerifyMacAddressEnable = _DhcpSnoopVerifyMacAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 1, 2),
    _DhcpSnoopVerifyMacAddressEnable_Type()
)
dhcpSnoopVerifyMacAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVerifyMacAddressEnable.setStatus("current")
_DhcpSnoopInformationOptionEnable_Type = EnabledStatus
_DhcpSnoopInformationOptionEnable_Object = MibScalar
dhcpSnoopInformationOptionEnable = _DhcpSnoopInformationOptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 1, 3),
    _DhcpSnoopInformationOptionEnable_Type()
)
dhcpSnoopInformationOptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopInformationOptionEnable.setStatus("current")


class _DhcpSnoopInformationOptionPolicy_Type(Integer32):
    """Custom type dhcpSnoopInformationOptionPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_DhcpSnoopInformationOptionPolicy_Type.__name__ = "Integer32"
_DhcpSnoopInformationOptionPolicy_Object = MibScalar
dhcpSnoopInformationOptionPolicy = _DhcpSnoopInformationOptionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 1, 4),
    _DhcpSnoopInformationOptionPolicy_Type()
)
dhcpSnoopInformationOptionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopInformationOptionPolicy.setStatus("current")


class _DhcpSnoopBindingsTableCtlAction_Type(Integer32):
    """Custom type dhcpSnoopBindingsTableCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("noAction", 1),
          ("store", 2))
    )


_DhcpSnoopBindingsTableCtlAction_Type.__name__ = "Integer32"
_DhcpSnoopBindingsTableCtlAction_Object = MibScalar
dhcpSnoopBindingsTableCtlAction = _DhcpSnoopBindingsTableCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 1, 5),
    _DhcpSnoopBindingsTableCtlAction_Type()
)
dhcpSnoopBindingsTableCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsTableCtlAction.setStatus("current")


class _DhcpSnoopLimitRate_Type(Integer32):
    """Custom type dhcpSnoopLimitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_DhcpSnoopLimitRate_Type.__name__ = "Integer32"
_DhcpSnoopLimitRate_Object = MibScalar
dhcpSnoopLimitRate = _DhcpSnoopLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 1, 6),
    _DhcpSnoopLimitRate_Type()
)
dhcpSnoopLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopLimitRate.setStatus("current")


class _DhcpSnoopInformationOptionEncodeFormat_Type(Integer32):
    """Custom type dhcpSnoopInformationOptionEncodeFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extra-subtype-included", 1),
          ("no-extra-subtype-included", 2))
    )


_DhcpSnoopInformationOptionEncodeFormat_Type.__name__ = "Integer32"
_DhcpSnoopInformationOptionEncodeFormat_Object = MibScalar
dhcpSnoopInformationOptionEncodeFormat = _DhcpSnoopInformationOptionEncodeFormat_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 1, 7),
    _DhcpSnoopInformationOptionEncodeFormat_Type()
)
dhcpSnoopInformationOptionEncodeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopInformationOptionEncodeFormat.setStatus("current")
_DhcpSnoopVlan_ObjectIdentity = ObjectIdentity
dhcpSnoopVlan = _DhcpSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 2)
)
_DhcpSnoopVlanConfigTable_Object = MibTable
dhcpSnoopVlanConfigTable = _DhcpSnoopVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopVlanConfigTable.setStatus("current")
_DhcpSnoopVlanConfigEntry_Object = MibTableRow
dhcpSnoopVlanConfigEntry = _DhcpSnoopVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 2, 1, 1)
)
dhcpSnoopVlanConfigEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "dhcpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopVlanConfigEntry.setStatus("current")
_DhcpSnoopVlanIndex_Type = VlanIndex
_DhcpSnoopVlanIndex_Object = MibTableColumn
dhcpSnoopVlanIndex = _DhcpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 2, 1, 1, 1),
    _DhcpSnoopVlanIndex_Type()
)
dhcpSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopVlanIndex.setStatus("current")
_DhcpSnoopVlanEnable_Type = EnabledStatus
_DhcpSnoopVlanEnable_Object = MibTableColumn
dhcpSnoopVlanEnable = _DhcpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 2, 1, 1, 2),
    _DhcpSnoopVlanEnable_Type()
)
dhcpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVlanEnable.setStatus("current")
_DhcpSnoopInterface_ObjectIdentity = ObjectIdentity
dhcpSnoopInterface = _DhcpSnoopInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 3)
)
_DhcpSnoopPortConfigTable_Object = MibTable
dhcpSnoopPortConfigTable = _DhcpSnoopPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortConfigTable.setStatus("current")
_DhcpSnoopPortConfigEntry_Object = MibTableRow
dhcpSnoopPortConfigEntry = _DhcpSnoopPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 3, 1, 1)
)
dhcpSnoopPortConfigEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "dhcpSnoopPortIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopPortConfigEntry.setStatus("current")
_DhcpSnoopPortIfIndex_Type = InterfaceIndex
_DhcpSnoopPortIfIndex_Object = MibTableColumn
dhcpSnoopPortIfIndex = _DhcpSnoopPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 3, 1, 1, 1),
    _DhcpSnoopPortIfIndex_Type()
)
dhcpSnoopPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopPortIfIndex.setStatus("current")
_DhcpSnoopPortTrustEnable_Type = EnabledStatus
_DhcpSnoopPortTrustEnable_Object = MibTableColumn
dhcpSnoopPortTrustEnable = _DhcpSnoopPortTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 3, 1, 1, 2),
    _DhcpSnoopPortTrustEnable_Type()
)
dhcpSnoopPortTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPortTrustEnable.setStatus("current")


class _DhcpSnoopPortMaxNumber_Type(Integer32):
    """Custom type dhcpSnoopPortMaxNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DhcpSnoopPortMaxNumber_Type.__name__ = "Integer32"
_DhcpSnoopPortMaxNumber_Object = MibTableColumn
dhcpSnoopPortMaxNumber = _DhcpSnoopPortMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 3, 1, 1, 6),
    _DhcpSnoopPortMaxNumber_Type()
)
dhcpSnoopPortMaxNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPortMaxNumber.setStatus("current")
_DhcpSnoopBindings_ObjectIdentity = ObjectIdentity
dhcpSnoopBindings = _DhcpSnoopBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4)
)
_DhcpSnoopBindingsTable_Object = MibTable
dhcpSnoopBindingsTable = _DhcpSnoopBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopBindingsTable.setStatus("current")
_DhcpSnoopBindingsEntry_Object = MibTableRow
dhcpSnoopBindingsEntry = _DhcpSnoopBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4, 1, 1)
)
dhcpSnoopBindingsEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "dhcpSnoopBindingsIpAddress"),
    (0, "ECS2100-28PP-MIB", "dhcpSnoopBindingsMacAddress"),
)
if mibBuilder.loadTexts:
    dhcpSnoopBindingsEntry.setStatus("current")
_DhcpSnoopBindingsVlanIndex_Type = VlanIndex
_DhcpSnoopBindingsVlanIndex_Object = MibTableColumn
dhcpSnoopBindingsVlanIndex = _DhcpSnoopBindingsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4, 1, 1, 1),
    _DhcpSnoopBindingsVlanIndex_Type()
)
dhcpSnoopBindingsVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsVlanIndex.setStatus("current")
_DhcpSnoopBindingsMacAddress_Type = MacAddress
_DhcpSnoopBindingsMacAddress_Object = MibTableColumn
dhcpSnoopBindingsMacAddress = _DhcpSnoopBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4, 1, 1, 2),
    _DhcpSnoopBindingsMacAddress_Type()
)
dhcpSnoopBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsMacAddress.setStatus("current")
_DhcpSnoopBindingsAddrType_Type = InetAddressType
_DhcpSnoopBindingsAddrType_Object = MibTableColumn
dhcpSnoopBindingsAddrType = _DhcpSnoopBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4, 1, 1, 3),
    _DhcpSnoopBindingsAddrType_Type()
)
dhcpSnoopBindingsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsAddrType.setStatus("current")


class _DhcpSnoopBindingsEntryType_Type(Integer32):
    """Custom type dhcpSnoopBindingsEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_DhcpSnoopBindingsEntryType_Type.__name__ = "Integer32"
_DhcpSnoopBindingsEntryType_Object = MibTableColumn
dhcpSnoopBindingsEntryType = _DhcpSnoopBindingsEntryType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4, 1, 1, 4),
    _DhcpSnoopBindingsEntryType_Type()
)
dhcpSnoopBindingsEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsEntryType.setStatus("current")
_DhcpSnoopBindingsIpAddress_Type = IpAddress
_DhcpSnoopBindingsIpAddress_Object = MibTableColumn
dhcpSnoopBindingsIpAddress = _DhcpSnoopBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4, 1, 1, 5),
    _DhcpSnoopBindingsIpAddress_Type()
)
dhcpSnoopBindingsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsIpAddress.setStatus("current")
_DhcpSnoopBindingsPortIfIndex_Type = InterfaceIndex
_DhcpSnoopBindingsPortIfIndex_Object = MibTableColumn
dhcpSnoopBindingsPortIfIndex = _DhcpSnoopBindingsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4, 1, 1, 6),
    _DhcpSnoopBindingsPortIfIndex_Type()
)
dhcpSnoopBindingsPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsPortIfIndex.setStatus("current")
_DhcpSnoopBindingsLeaseTime_Type = Unsigned32
_DhcpSnoopBindingsLeaseTime_Object = MibTableColumn
dhcpSnoopBindingsLeaseTime = _DhcpSnoopBindingsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 4, 1, 1, 7),
    _DhcpSnoopBindingsLeaseTime_Type()
)
dhcpSnoopBindingsLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsLeaseTime.setStatus("current")
_DhcpSnoopStatistics_ObjectIdentity = ObjectIdentity
dhcpSnoopStatistics = _DhcpSnoopStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 5)
)
_DhcpSnoopTotalForwardedPkts_Type = Counter32
_DhcpSnoopTotalForwardedPkts_Object = MibScalar
dhcpSnoopTotalForwardedPkts = _DhcpSnoopTotalForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 5, 1),
    _DhcpSnoopTotalForwardedPkts_Type()
)
dhcpSnoopTotalForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopTotalForwardedPkts.setStatus("current")
_DhcpSnoopUntrustedPortDroppedPkts_Type = Counter32
_DhcpSnoopUntrustedPortDroppedPkts_Object = MibScalar
dhcpSnoopUntrustedPortDroppedPkts = _DhcpSnoopUntrustedPortDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 46, 5, 3),
    _DhcpSnoopUntrustedPortDroppedPkts_Type()
)
dhcpSnoopUntrustedPortDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopUntrustedPortDroppedPkts.setStatus("current")
_IpSrcGuardMgt_ObjectIdentity = ObjectIdentity
ipSrcGuardMgt = _IpSrcGuardMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48)
)
_IpSrcGuardConfigTable_Object = MibTable
ipSrcGuardConfigTable = _IpSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 1)
)
if mibBuilder.loadTexts:
    ipSrcGuardConfigTable.setStatus("current")
_IpSrcGuardConfigEntry_Object = MibTableRow
ipSrcGuardConfigEntry = _IpSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 1, 1)
)
ipSrcGuardConfigEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "ipSrcGuardPortIfIndex"),
)
if mibBuilder.loadTexts:
    ipSrcGuardConfigEntry.setStatus("current")
_IpSrcGuardPortIfIndex_Type = InterfaceIndex
_IpSrcGuardPortIfIndex_Object = MibTableColumn
ipSrcGuardPortIfIndex = _IpSrcGuardPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 1, 1, 1),
    _IpSrcGuardPortIfIndex_Type()
)
ipSrcGuardPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardPortIfIndex.setStatus("current")


class _IpSrcGuardMode_Type(Integer32):
    """Custom type ipSrcGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diabled", 0),
          ("srcIp", 1),
          ("srcIpMac", 2))
    )


_IpSrcGuardMode_Type.__name__ = "Integer32"
_IpSrcGuardMode_Object = MibTableColumn
ipSrcGuardMode = _IpSrcGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 1, 1, 2),
    _IpSrcGuardMode_Type()
)
ipSrcGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSrcGuardMode.setStatus("current")
_IpSrcGuardAclTable_Object = MibTable
ipSrcGuardAclTable = _IpSrcGuardAclTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 3)
)
if mibBuilder.loadTexts:
    ipSrcGuardAclTable.setStatus("current")
_IpSrcGuardAclEntry_Object = MibTableRow
ipSrcGuardAclEntry = _IpSrcGuardAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 3, 1)
)
ipSrcGuardAclEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "ipSrcGuardAclBindingIpAddress"),
    (0, "ECS2100-28PP-MIB", "ipSrcGuardAclBindingMacAddress"),
    (0, "ECS2100-28PP-MIB", "ipSrcGuardAclBindingEntryType"),
)
if mibBuilder.loadTexts:
    ipSrcGuardAclEntry.setStatus("current")
_IpSrcGuardAclBindingIpAddress_Type = IpAddress
_IpSrcGuardAclBindingIpAddress_Object = MibTableColumn
ipSrcGuardAclBindingIpAddress = _IpSrcGuardAclBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 3, 1, 1),
    _IpSrcGuardAclBindingIpAddress_Type()
)
ipSrcGuardAclBindingIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardAclBindingIpAddress.setStatus("current")
_IpSrcGuardAclBindingMacAddress_Type = MacAddress
_IpSrcGuardAclBindingMacAddress_Object = MibTableColumn
ipSrcGuardAclBindingMacAddress = _IpSrcGuardAclBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 3, 1, 2),
    _IpSrcGuardAclBindingMacAddress_Type()
)
ipSrcGuardAclBindingMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardAclBindingMacAddress.setStatus("current")


class _IpSrcGuardAclBindingEntryType_Type(Integer32):
    """Custom type ipSrcGuardAclBindingEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 3),
          ("dhcp", 2),
          ("static", 1))
    )


_IpSrcGuardAclBindingEntryType_Type.__name__ = "Integer32"
_IpSrcGuardAclBindingEntryType_Object = MibTableColumn
ipSrcGuardAclBindingEntryType = _IpSrcGuardAclBindingEntryType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 3, 1, 3),
    _IpSrcGuardAclBindingEntryType_Type()
)
ipSrcGuardAclBindingEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardAclBindingEntryType.setStatus("current")
_IpSrcGuardAclBindingVlanIndex_Type = VlanIndex
_IpSrcGuardAclBindingVlanIndex_Object = MibTableColumn
ipSrcGuardAclBindingVlanIndex = _IpSrcGuardAclBindingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 3, 1, 4),
    _IpSrcGuardAclBindingVlanIndex_Type()
)
ipSrcGuardAclBindingVlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardAclBindingVlanIndex.setStatus("current")
_IpSrcGuardAclBindingPortIfIndex_Type = InterfaceIndex
_IpSrcGuardAclBindingPortIfIndex_Object = MibTableColumn
ipSrcGuardAclBindingPortIfIndex = _IpSrcGuardAclBindingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 3, 1, 5),
    _IpSrcGuardAclBindingPortIfIndex_Type()
)
ipSrcGuardAclBindingPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardAclBindingPortIfIndex.setStatus("current")
_IpSrcGuardAclBindingStatus_Type = RowStatus
_IpSrcGuardAclBindingStatus_Object = MibTableColumn
ipSrcGuardAclBindingStatus = _IpSrcGuardAclBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 48, 3, 1, 6),
    _IpSrcGuardAclBindingStatus_Type()
)
ipSrcGuardAclBindingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardAclBindingStatus.setStatus("current")
_MldSnoopMgt_ObjectIdentity = ObjectIdentity
mldSnoopMgt = _MldSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54)
)


class _MldSnoopStatus_Type(EnabledStatus):
    """Custom type mldSnoopStatus based on EnabledStatus"""


_MldSnoopStatus_Object = MibScalar
mldSnoopStatus = _MldSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 1),
    _MldSnoopStatus_Type()
)
mldSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopStatus.setStatus("current")


class _MldSnoopQuerier_Type(EnabledStatus):
    """Custom type mldSnoopQuerier based on EnabledStatus"""


_MldSnoopQuerier_Object = MibScalar
mldSnoopQuerier = _MldSnoopQuerier_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 2),
    _MldSnoopQuerier_Type()
)
mldSnoopQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopQuerier.setStatus("current")


class _MldSnoopRobustness_Type(Integer32):
    """Custom type mldSnoopRobustness based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_MldSnoopRobustness_Type.__name__ = "Integer32"
_MldSnoopRobustness_Object = MibScalar
mldSnoopRobustness = _MldSnoopRobustness_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 3),
    _MldSnoopRobustness_Type()
)
mldSnoopRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopRobustness.setStatus("current")


class _MldSnoopQueryInterval_Type(Integer32):
    """Custom type mldSnoopQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 125),
    )


_MldSnoopQueryInterval_Type.__name__ = "Integer32"
_MldSnoopQueryInterval_Object = MibScalar
mldSnoopQueryInterval = _MldSnoopQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 4),
    _MldSnoopQueryInterval_Type()
)
mldSnoopQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopQueryInterval.setStatus("current")


class _MldSnoopQueryMaxResponseTime_Type(Integer32):
    """Custom type mldSnoopQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 25),
    )


_MldSnoopQueryMaxResponseTime_Type.__name__ = "Integer32"
_MldSnoopQueryMaxResponseTime_Object = MibScalar
mldSnoopQueryMaxResponseTime = _MldSnoopQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 5),
    _MldSnoopQueryMaxResponseTime_Type()
)
mldSnoopQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopQueryMaxResponseTime.setStatus("current")


class _MldSnoopRouterPortExpireTime_Type(Integer32):
    """Custom type mldSnoopRouterPortExpireTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 500),
    )


_MldSnoopRouterPortExpireTime_Type.__name__ = "Integer32"
_MldSnoopRouterPortExpireTime_Object = MibScalar
mldSnoopRouterPortExpireTime = _MldSnoopRouterPortExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 6),
    _MldSnoopRouterPortExpireTime_Type()
)
mldSnoopRouterPortExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopRouterPortExpireTime.setStatus("current")


class _MldSnoopVersion_Type(Integer32):
    """Custom type mldSnoopVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MldSnoopVersion_Type.__name__ = "Integer32"
_MldSnoopVersion_Object = MibScalar
mldSnoopVersion = _MldSnoopVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 7),
    _MldSnoopVersion_Type()
)
mldSnoopVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopVersion.setStatus("current")


class _MldSnoopUnknownMcastMode_Type(Integer32):
    """Custom type mldSnoopUnknownMcastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flood", 1),
          ("toRouterPort", 2))
    )


_MldSnoopUnknownMcastMode_Type.__name__ = "Integer32"
_MldSnoopUnknownMcastMode_Object = MibScalar
mldSnoopUnknownMcastMode = _MldSnoopUnknownMcastMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 8),
    _MldSnoopUnknownMcastMode_Type()
)
mldSnoopUnknownMcastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopUnknownMcastMode.setStatus("current")
_MldSnoopRouterCurrentTable_Object = MibTable
mldSnoopRouterCurrentTable = _MldSnoopRouterCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 9)
)
if mibBuilder.loadTexts:
    mldSnoopRouterCurrentTable.setStatus("current")
_MldSnoopRouterCurrentEntry_Object = MibTableRow
mldSnoopRouterCurrentEntry = _MldSnoopRouterCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 9, 1)
)
mldSnoopRouterCurrentEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopRouterCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    mldSnoopRouterCurrentEntry.setStatus("current")
_MldSnoopRouterCurrentVlanIndex_Type = Unsigned32
_MldSnoopRouterCurrentVlanIndex_Object = MibTableColumn
mldSnoopRouterCurrentVlanIndex = _MldSnoopRouterCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 9, 1, 1),
    _MldSnoopRouterCurrentVlanIndex_Type()
)
mldSnoopRouterCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopRouterCurrentVlanIndex.setStatus("current")
_MldSnoopRouterCurrentPorts_Type = PortList
_MldSnoopRouterCurrentPorts_Object = MibTableColumn
mldSnoopRouterCurrentPorts = _MldSnoopRouterCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 9, 1, 2),
    _MldSnoopRouterCurrentPorts_Type()
)
mldSnoopRouterCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopRouterCurrentPorts.setStatus("current")
_MldSnoopRouterStaticTable_Object = MibTable
mldSnoopRouterStaticTable = _MldSnoopRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 10)
)
if mibBuilder.loadTexts:
    mldSnoopRouterStaticTable.setStatus("current")
_MldSnoopRouterStaticEntry_Object = MibTableRow
mldSnoopRouterStaticEntry = _MldSnoopRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 10, 1)
)
mldSnoopRouterStaticEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopRouterStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    mldSnoopRouterStaticEntry.setStatus("current")
_MldSnoopRouterStaticVlanIndex_Type = Unsigned32
_MldSnoopRouterStaticVlanIndex_Object = MibTableColumn
mldSnoopRouterStaticVlanIndex = _MldSnoopRouterStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 10, 1, 1),
    _MldSnoopRouterStaticVlanIndex_Type()
)
mldSnoopRouterStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopRouterStaticVlanIndex.setStatus("current")
_MldSnoopRouterStaticPorts_Type = PortList
_MldSnoopRouterStaticPorts_Object = MibTableColumn
mldSnoopRouterStaticPorts = _MldSnoopRouterStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 10, 1, 2),
    _MldSnoopRouterStaticPorts_Type()
)
mldSnoopRouterStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldSnoopRouterStaticPorts.setStatus("current")
_MldSnoopRouterStaticStatus_Type = ValidStatus
_MldSnoopRouterStaticStatus_Object = MibTableColumn
mldSnoopRouterStaticStatus = _MldSnoopRouterStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 10, 1, 3),
    _MldSnoopRouterStaticStatus_Type()
)
mldSnoopRouterStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldSnoopRouterStaticStatus.setStatus("current")
_MldSnoopMulticastCurrentTable_Object = MibTable
mldSnoopMulticastCurrentTable = _MldSnoopMulticastCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 11)
)
if mibBuilder.loadTexts:
    mldSnoopMulticastCurrentTable.setStatus("current")
_MldSnoopMulticastCurrentEntry_Object = MibTableRow
mldSnoopMulticastCurrentEntry = _MldSnoopMulticastCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 11, 1)
)
mldSnoopMulticastCurrentEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopMulticastCurrentVlanIndex"),
    (0, "ECS2100-28PP-MIB", "mldSnoopMulticastCurrentIpAddress"),
    (0, "ECS2100-28PP-MIB", "mldSnoopMulticastCurrentSourceIpAddress"),
)
if mibBuilder.loadTexts:
    mldSnoopMulticastCurrentEntry.setStatus("current")
_MldSnoopMulticastCurrentVlanIndex_Type = Unsigned32
_MldSnoopMulticastCurrentVlanIndex_Object = MibTableColumn
mldSnoopMulticastCurrentVlanIndex = _MldSnoopMulticastCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 11, 1, 1),
    _MldSnoopMulticastCurrentVlanIndex_Type()
)
mldSnoopMulticastCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopMulticastCurrentVlanIndex.setStatus("current")
_MldSnoopMulticastCurrentIpAddress_Type = InetAddressIPv6
_MldSnoopMulticastCurrentIpAddress_Object = MibTableColumn
mldSnoopMulticastCurrentIpAddress = _MldSnoopMulticastCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 11, 1, 2),
    _MldSnoopMulticastCurrentIpAddress_Type()
)
mldSnoopMulticastCurrentIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopMulticastCurrentIpAddress.setStatus("current")
_MldSnoopMulticastCurrentSourceIpAddress_Type = InetAddressIPv6
_MldSnoopMulticastCurrentSourceIpAddress_Object = MibTableColumn
mldSnoopMulticastCurrentSourceIpAddress = _MldSnoopMulticastCurrentSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 11, 1, 3),
    _MldSnoopMulticastCurrentSourceIpAddress_Type()
)
mldSnoopMulticastCurrentSourceIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopMulticastCurrentSourceIpAddress.setStatus("current")
_MldSnoopMulticastCurrentPorts_Type = PortList
_MldSnoopMulticastCurrentPorts_Object = MibTableColumn
mldSnoopMulticastCurrentPorts = _MldSnoopMulticastCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 11, 1, 4),
    _MldSnoopMulticastCurrentPorts_Type()
)
mldSnoopMulticastCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopMulticastCurrentPorts.setStatus("current")
_MldSnoopMulticastStaticTable_Object = MibTable
mldSnoopMulticastStaticTable = _MldSnoopMulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 12)
)
if mibBuilder.loadTexts:
    mldSnoopMulticastStaticTable.setStatus("current")
_MldSnoopMulticastStaticEntry_Object = MibTableRow
mldSnoopMulticastStaticEntry = _MldSnoopMulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 12, 1)
)
mldSnoopMulticastStaticEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopMulticastStaticVlanIndex"),
    (0, "ECS2100-28PP-MIB", "mldSnoopMulticastStaticIpAddress"),
)
if mibBuilder.loadTexts:
    mldSnoopMulticastStaticEntry.setStatus("current")
_MldSnoopMulticastStaticVlanIndex_Type = Unsigned32
_MldSnoopMulticastStaticVlanIndex_Object = MibTableColumn
mldSnoopMulticastStaticVlanIndex = _MldSnoopMulticastStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 12, 1, 1),
    _MldSnoopMulticastStaticVlanIndex_Type()
)
mldSnoopMulticastStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopMulticastStaticVlanIndex.setStatus("current")
_MldSnoopMulticastStaticIpAddress_Type = InetAddressIPv6
_MldSnoopMulticastStaticIpAddress_Object = MibTableColumn
mldSnoopMulticastStaticIpAddress = _MldSnoopMulticastStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 12, 1, 2),
    _MldSnoopMulticastStaticIpAddress_Type()
)
mldSnoopMulticastStaticIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopMulticastStaticIpAddress.setStatus("current")
_MldSnoopMulticastStaticPorts_Type = PortList
_MldSnoopMulticastStaticPorts_Object = MibTableColumn
mldSnoopMulticastStaticPorts = _MldSnoopMulticastStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 12, 1, 3),
    _MldSnoopMulticastStaticPorts_Type()
)
mldSnoopMulticastStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldSnoopMulticastStaticPorts.setStatus("current")
_MldSnoopMulticastStaticStatus_Type = ValidStatus
_MldSnoopMulticastStaticStatus_Object = MibTableColumn
mldSnoopMulticastStaticStatus = _MldSnoopMulticastStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 12, 1, 4),
    _MldSnoopMulticastStaticStatus_Type()
)
mldSnoopMulticastStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mldSnoopMulticastStaticStatus.setStatus("current")
_MldSnoopCurrentVlanTable_Object = MibTable
mldSnoopCurrentVlanTable = _MldSnoopCurrentVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 13)
)
if mibBuilder.loadTexts:
    mldSnoopCurrentVlanTable.setStatus("current")
_MldSnoopCurrentVlanEntry_Object = MibTableRow
mldSnoopCurrentVlanEntry = _MldSnoopCurrentVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 13, 1)
)
mldSnoopCurrentVlanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    mldSnoopCurrentVlanEntry.setStatus("current")
_MldSnoopCurrentVlanIndex_Type = Unsigned32
_MldSnoopCurrentVlanIndex_Object = MibTableColumn
mldSnoopCurrentVlanIndex = _MldSnoopCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 13, 1, 1),
    _MldSnoopCurrentVlanIndex_Type()
)
mldSnoopCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopCurrentVlanIndex.setStatus("current")
_MldSnoopCurrentVlanImmediateLeave_Type = EnabledStatus
_MldSnoopCurrentVlanImmediateLeave_Object = MibTableColumn
mldSnoopCurrentVlanImmediateLeave = _MldSnoopCurrentVlanImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 13, 1, 2),
    _MldSnoopCurrentVlanImmediateLeave_Type()
)
mldSnoopCurrentVlanImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopCurrentVlanImmediateLeave.setStatus("current")
_MldSnoopCurrentVlanImmediateLeaveByHostIp_Type = EnabledStatus
_MldSnoopCurrentVlanImmediateLeaveByHostIp_Object = MibTableColumn
mldSnoopCurrentVlanImmediateLeaveByHostIp = _MldSnoopCurrentVlanImmediateLeaveByHostIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 13, 1, 3),
    _MldSnoopCurrentVlanImmediateLeaveByHostIp_Type()
)
mldSnoopCurrentVlanImmediateLeaveByHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopCurrentVlanImmediateLeaveByHostIp.setStatus("current")


class _MldSnoopProxyReporting_Type(EnabledStatus):
    """Custom type mldSnoopProxyReporting based on EnabledStatus"""


_MldSnoopProxyReporting_Object = MibScalar
mldSnoopProxyReporting = _MldSnoopProxyReporting_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 14),
    _MldSnoopProxyReporting_Type()
)
mldSnoopProxyReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopProxyReporting.setStatus("current")


class _MldSnoopUnsolicitedReportInterval_Type(Unsigned32):
    """Custom type mldSnoopUnsolicitedReportInterval based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MldSnoopUnsolicitedReportInterval_Type.__name__ = "Unsigned32"
_MldSnoopUnsolicitedReportInterval_Object = MibScalar
mldSnoopUnsolicitedReportInterval = _MldSnoopUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 15),
    _MldSnoopUnsolicitedReportInterval_Type()
)
mldSnoopUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopUnsolicitedReportInterval.setStatus("current")
_MldSnoopPortTable_Object = MibTable
mldSnoopPortTable = _MldSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16)
)
if mibBuilder.loadTexts:
    mldSnoopPortTable.setStatus("current")
_MldSnoopPortEntry_Object = MibTableRow
mldSnoopPortEntry = _MldSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1)
)
mldSnoopPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopPortIndex"),
)
if mibBuilder.loadTexts:
    mldSnoopPortEntry.setStatus("current")
_MldSnoopPortIndex_Type = Unsigned32
_MldSnoopPortIndex_Object = MibTableColumn
mldSnoopPortIndex = _MldSnoopPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 1),
    _MldSnoopPortIndex_Type()
)
mldSnoopPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopPortIndex.setStatus("current")


class _MldSnoopQueryDrop_Type(Integer32):
    """Custom type mldSnoopQueryDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MldSnoopQueryDrop_Type.__name__ = "Integer32"
_MldSnoopQueryDrop_Object = MibTableColumn
mldSnoopQueryDrop = _MldSnoopQueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 3),
    _MldSnoopQueryDrop_Type()
)
mldSnoopQueryDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopQueryDrop.setStatus("current")


class _MldSnoopMulticastDataDrop_Type(Integer32):
    """Custom type mldSnoopMulticastDataDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MldSnoopMulticastDataDrop_Type.__name__ = "Integer32"
_MldSnoopMulticastDataDrop_Object = MibTableColumn
mldSnoopMulticastDataDrop = _MldSnoopMulticastDataDrop_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 4),
    _MldSnoopMulticastDataDrop_Type()
)
mldSnoopMulticastDataDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopMulticastDataDrop.setStatus("current")
_MldSnoopPortNumGroups_Type = Unsigned32
_MldSnoopPortNumGroups_Object = MibTableColumn
mldSnoopPortNumGroups = _MldSnoopPortNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 5),
    _MldSnoopPortNumGroups_Type()
)
mldSnoopPortNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumGroups.setStatus("current")
_MldSnoopPortNumJoinSend_Type = Unsigned32
_MldSnoopPortNumJoinSend_Object = MibTableColumn
mldSnoopPortNumJoinSend = _MldSnoopPortNumJoinSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 6),
    _MldSnoopPortNumJoinSend_Type()
)
mldSnoopPortNumJoinSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumJoinSend.setStatus("current")
_MldSnoopPortNumJoins_Type = Unsigned32
_MldSnoopPortNumJoins_Object = MibTableColumn
mldSnoopPortNumJoins = _MldSnoopPortNumJoins_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 7),
    _MldSnoopPortNumJoins_Type()
)
mldSnoopPortNumJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumJoins.setStatus("current")
_MldSnoopPortNumJoinSuccess_Type = Unsigned32
_MldSnoopPortNumJoinSuccess_Object = MibTableColumn
mldSnoopPortNumJoinSuccess = _MldSnoopPortNumJoinSuccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 8),
    _MldSnoopPortNumJoinSuccess_Type()
)
mldSnoopPortNumJoinSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumJoinSuccess.setStatus("current")
_MldSnoopPortNumLeavesSend_Type = Unsigned32
_MldSnoopPortNumLeavesSend_Object = MibTableColumn
mldSnoopPortNumLeavesSend = _MldSnoopPortNumLeavesSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 9),
    _MldSnoopPortNumLeavesSend_Type()
)
mldSnoopPortNumLeavesSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumLeavesSend.setStatus("current")
_MldSnoopPortNumLeaves_Type = Unsigned32
_MldSnoopPortNumLeaves_Object = MibTableColumn
mldSnoopPortNumLeaves = _MldSnoopPortNumLeaves_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 10),
    _MldSnoopPortNumLeaves_Type()
)
mldSnoopPortNumLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumLeaves.setStatus("current")
_MldSnoopPortNumGeneralQuerySend_Type = Unsigned32
_MldSnoopPortNumGeneralQuerySend_Object = MibTableColumn
mldSnoopPortNumGeneralQuerySend = _MldSnoopPortNumGeneralQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 11),
    _MldSnoopPortNumGeneralQuerySend_Type()
)
mldSnoopPortNumGeneralQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumGeneralQuerySend.setStatus("current")
_MldSnoopPortNumGeneralQueryRecevied_Type = Unsigned32
_MldSnoopPortNumGeneralQueryRecevied_Object = MibTableColumn
mldSnoopPortNumGeneralQueryRecevied = _MldSnoopPortNumGeneralQueryRecevied_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 12),
    _MldSnoopPortNumGeneralQueryRecevied_Type()
)
mldSnoopPortNumGeneralQueryRecevied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumGeneralQueryRecevied.setStatus("current")
_MldSnoopPortNumSepcificQuerySend_Type = Unsigned32
_MldSnoopPortNumSepcificQuerySend_Object = MibTableColumn
mldSnoopPortNumSepcificQuerySend = _MldSnoopPortNumSepcificQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 13),
    _MldSnoopPortNumSepcificQuerySend_Type()
)
mldSnoopPortNumSepcificQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumSepcificQuerySend.setStatus("current")
_MldsnoopPortNumSpecificQueryReceived_Type = Unsigned32
_MldsnoopPortNumSpecificQueryReceived_Object = MibTableColumn
mldsnoopPortNumSpecificQueryReceived = _MldsnoopPortNumSpecificQueryReceived_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 14),
    _MldsnoopPortNumSpecificQueryReceived_Type()
)
mldsnoopPortNumSpecificQueryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsnoopPortNumSpecificQueryReceived.setStatus("current")
_MldSnoopPortNumInvalidReport_Type = Unsigned32
_MldSnoopPortNumInvalidReport_Object = MibTableColumn
mldSnoopPortNumInvalidReport = _MldSnoopPortNumInvalidReport_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 15),
    _MldSnoopPortNumInvalidReport_Type()
)
mldSnoopPortNumInvalidReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopPortNumInvalidReport.setStatus("current")
_MldSnoopPortClearStatistics_Type = TruthValue
_MldSnoopPortClearStatistics_Object = MibTableColumn
mldSnoopPortClearStatistics = _MldSnoopPortClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 16, 1, 16),
    _MldSnoopPortClearStatistics_Type()
)
mldSnoopPortClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopPortClearStatistics.setStatus("current")
_MldSnoopFilterStatus_Type = EnabledStatus
_MldSnoopFilterStatus_Object = MibScalar
mldSnoopFilterStatus = _MldSnoopFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 17),
    _MldSnoopFilterStatus_Type()
)
mldSnoopFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopFilterStatus.setStatus("current")
_MldSnoopProfileTable_Object = MibTable
mldSnoopProfileTable = _MldSnoopProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 18)
)
if mibBuilder.loadTexts:
    mldSnoopProfileTable.setStatus("current")
_MldSnoopProfileEntry_Object = MibTableRow
mldSnoopProfileEntry = _MldSnoopProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 18, 1)
)
mldSnoopProfileEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopProfileId"),
)
if mibBuilder.loadTexts:
    mldSnoopProfileEntry.setStatus("current")
_MldSnoopProfileId_Type = Unsigned32
_MldSnoopProfileId_Object = MibTableColumn
mldSnoopProfileId = _MldSnoopProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 18, 1, 1),
    _MldSnoopProfileId_Type()
)
mldSnoopProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopProfileId.setStatus("current")


class _MldSnoopProfileAction_Type(Integer32):
    """Custom type mldSnoopProfileAction based on Integer32"""
    defaultValue = 2

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


_MldSnoopProfileAction_Type.__name__ = "Integer32"
_MldSnoopProfileAction_Object = MibTableColumn
mldSnoopProfileAction = _MldSnoopProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 18, 1, 2),
    _MldSnoopProfileAction_Type()
)
mldSnoopProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopProfileAction.setStatus("current")
_MldSnoopProfileStatus_Type = ValidStatus
_MldSnoopProfileStatus_Object = MibTableColumn
mldSnoopProfileStatus = _MldSnoopProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 18, 1, 3),
    _MldSnoopProfileStatus_Type()
)
mldSnoopProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopProfileStatus.setStatus("current")
_MldSnoopProfileCtl_ObjectIdentity = ObjectIdentity
mldSnoopProfileCtl = _MldSnoopProfileCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 19)
)
_MldSnoopProfileCtlId_Type = Unsigned32
_MldSnoopProfileCtlId_Object = MibScalar
mldSnoopProfileCtlId = _MldSnoopProfileCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 19, 1),
    _MldSnoopProfileCtlId_Type()
)
mldSnoopProfileCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopProfileCtlId.setStatus("current")
_MldSnoopProfileCtlInetAddressType_Type = InetAddressType
_MldSnoopProfileCtlInetAddressType_Object = MibScalar
mldSnoopProfileCtlInetAddressType = _MldSnoopProfileCtlInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 19, 2),
    _MldSnoopProfileCtlInetAddressType_Type()
)
mldSnoopProfileCtlInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopProfileCtlInetAddressType.setStatus("current")
_MldSnoopProfileCtlStartInetAddress_Type = InetAddress
_MldSnoopProfileCtlStartInetAddress_Object = MibScalar
mldSnoopProfileCtlStartInetAddress = _MldSnoopProfileCtlStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 19, 3),
    _MldSnoopProfileCtlStartInetAddress_Type()
)
mldSnoopProfileCtlStartInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopProfileCtlStartInetAddress.setStatus("current")
_MldSnoopProfileCtlEndInetAddress_Type = InetAddress
_MldSnoopProfileCtlEndInetAddress_Object = MibScalar
mldSnoopProfileCtlEndInetAddress = _MldSnoopProfileCtlEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 19, 4),
    _MldSnoopProfileCtlEndInetAddress_Type()
)
mldSnoopProfileCtlEndInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopProfileCtlEndInetAddress.setStatus("current")


class _MldSnoopProfileCtlAction_Type(Integer32):
    """Custom type mldSnoopProfileCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("destroy", 3),
          ("noAction", 1))
    )


_MldSnoopProfileCtlAction_Type.__name__ = "Integer32"
_MldSnoopProfileCtlAction_Object = MibScalar
mldSnoopProfileCtlAction = _MldSnoopProfileCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 19, 5),
    _MldSnoopProfileCtlAction_Type()
)
mldSnoopProfileCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopProfileCtlAction.setStatus("current")
_MldSnoopProfileRangeTable_Object = MibTable
mldSnoopProfileRangeTable = _MldSnoopProfileRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 20)
)
if mibBuilder.loadTexts:
    mldSnoopProfileRangeTable.setStatus("current")
_MldSnoopProfileRangeEntry_Object = MibTableRow
mldSnoopProfileRangeEntry = _MldSnoopProfileRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 20, 1)
)
mldSnoopProfileRangeEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopProfileRangeProfileId"),
    (0, "ECS2100-28PP-MIB", "mldSnoopProfileRangeInetAddressType"),
    (0, "ECS2100-28PP-MIB", "mldSnoopProfileRangeStartInetAddress"),
    (0, "ECS2100-28PP-MIB", "mldSnoopProfileRangeEndInetAddress"),
)
if mibBuilder.loadTexts:
    mldSnoopProfileRangeEntry.setStatus("current")


class _MldSnoopProfileRangeProfileId_Type(Unsigned32):
    """Custom type mldSnoopProfileRangeProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MldSnoopProfileRangeProfileId_Type.__name__ = "Unsigned32"
_MldSnoopProfileRangeProfileId_Object = MibTableColumn
mldSnoopProfileRangeProfileId = _MldSnoopProfileRangeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 20, 1, 1),
    _MldSnoopProfileRangeProfileId_Type()
)
mldSnoopProfileRangeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopProfileRangeProfileId.setStatus("current")
_MldSnoopProfileRangeInetAddressType_Type = InetAddressType
_MldSnoopProfileRangeInetAddressType_Object = MibTableColumn
mldSnoopProfileRangeInetAddressType = _MldSnoopProfileRangeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 20, 1, 2),
    _MldSnoopProfileRangeInetAddressType_Type()
)
mldSnoopProfileRangeInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopProfileRangeInetAddressType.setStatus("current")
_MldSnoopProfileRangeStartInetAddress_Type = InetAddress
_MldSnoopProfileRangeStartInetAddress_Object = MibTableColumn
mldSnoopProfileRangeStartInetAddress = _MldSnoopProfileRangeStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 20, 1, 3),
    _MldSnoopProfileRangeStartInetAddress_Type()
)
mldSnoopProfileRangeStartInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopProfileRangeStartInetAddress.setStatus("current")
_MldSnoopProfileRangeEndInetAddress_Type = InetAddress
_MldSnoopProfileRangeEndInetAddress_Object = MibTableColumn
mldSnoopProfileRangeEndInetAddress = _MldSnoopProfileRangeEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 20, 1, 4),
    _MldSnoopProfileRangeEndInetAddress_Type()
)
mldSnoopProfileRangeEndInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopProfileRangeEndInetAddress.setStatus("current")


class _MldSnoopProfileRangeAction_Type(Integer32):
    """Custom type mldSnoopProfileRangeAction based on Integer32"""
    defaultValue = 2

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


_MldSnoopProfileRangeAction_Type.__name__ = "Integer32"
_MldSnoopProfileRangeAction_Object = MibTableColumn
mldSnoopProfileRangeAction = _MldSnoopProfileRangeAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 20, 1, 5),
    _MldSnoopProfileRangeAction_Type()
)
mldSnoopProfileRangeAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopProfileRangeAction.setStatus("current")
_MldSnoopFilterPortTable_Object = MibTable
mldSnoopFilterPortTable = _MldSnoopFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 21)
)
if mibBuilder.loadTexts:
    mldSnoopFilterPortTable.setStatus("current")
_MldSnoopFilterPortEntry_Object = MibTableRow
mldSnoopFilterPortEntry = _MldSnoopFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 21, 1)
)
mldSnoopFilterPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopFilterPortIndex"),
)
if mibBuilder.loadTexts:
    mldSnoopFilterPortEntry.setStatus("current")
_MldSnoopFilterPortIndex_Type = Unsigned32
_MldSnoopFilterPortIndex_Object = MibTableColumn
mldSnoopFilterPortIndex = _MldSnoopFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 21, 1, 1),
    _MldSnoopFilterPortIndex_Type()
)
mldSnoopFilterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopFilterPortIndex.setStatus("current")
_MldSnoopFilterPortProfileId_Type = Integer32
_MldSnoopFilterPortProfileId_Object = MibTableColumn
mldSnoopFilterPortProfileId = _MldSnoopFilterPortProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 21, 1, 2),
    _MldSnoopFilterPortProfileId_Type()
)
mldSnoopFilterPortProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopFilterPortProfileId.setStatus("current")
_MldSnoopThrottlePortTable_Object = MibTable
mldSnoopThrottlePortTable = _MldSnoopThrottlePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 22)
)
if mibBuilder.loadTexts:
    mldSnoopThrottlePortTable.setStatus("current")
_MldSnoopThrottlePortEntry_Object = MibTableRow
mldSnoopThrottlePortEntry = _MldSnoopThrottlePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 22, 1)
)
mldSnoopThrottlePortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopThrottlePortIndex"),
)
if mibBuilder.loadTexts:
    mldSnoopThrottlePortEntry.setStatus("current")
_MldSnoopThrottlePortIndex_Type = Unsigned32
_MldSnoopThrottlePortIndex_Object = MibTableColumn
mldSnoopThrottlePortIndex = _MldSnoopThrottlePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 22, 1, 1),
    _MldSnoopThrottlePortIndex_Type()
)
mldSnoopThrottlePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopThrottlePortIndex.setStatus("current")
_MldSnoopThrottlePortRunningStatus_Type = TruthValue
_MldSnoopThrottlePortRunningStatus_Object = MibTableColumn
mldSnoopThrottlePortRunningStatus = _MldSnoopThrottlePortRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 22, 1, 2),
    _MldSnoopThrottlePortRunningStatus_Type()
)
mldSnoopThrottlePortRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopThrottlePortRunningStatus.setStatus("current")


class _MldSnoopThrottlePortAction_Type(Integer32):
    """Custom type mldSnoopThrottlePortAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("replace", 1))
    )


_MldSnoopThrottlePortAction_Type.__name__ = "Integer32"
_MldSnoopThrottlePortAction_Object = MibTableColumn
mldSnoopThrottlePortAction = _MldSnoopThrottlePortAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 22, 1, 3),
    _MldSnoopThrottlePortAction_Type()
)
mldSnoopThrottlePortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopThrottlePortAction.setStatus("current")


class _MldSnoopThrottlePortMaxGroups_Type(Integer32):
    """Custom type mldSnoopThrottlePortMaxGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MldSnoopThrottlePortMaxGroups_Type.__name__ = "Integer32"
_MldSnoopThrottlePortMaxGroups_Object = MibTableColumn
mldSnoopThrottlePortMaxGroups = _MldSnoopThrottlePortMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 22, 1, 4),
    _MldSnoopThrottlePortMaxGroups_Type()
)
mldSnoopThrottlePortMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopThrottlePortMaxGroups.setStatus("current")
_MldSnoopThrottlePortCurrentGroups_Type = Integer32
_MldSnoopThrottlePortCurrentGroups_Object = MibTableColumn
mldSnoopThrottlePortCurrentGroups = _MldSnoopThrottlePortCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 22, 1, 5),
    _MldSnoopThrottlePortCurrentGroups_Type()
)
mldSnoopThrottlePortCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopThrottlePortCurrentGroups.setStatus("current")
_MldSnoopClearDynamicGroups_Type = TruthValue
_MldSnoopClearDynamicGroups_Object = MibScalar
mldSnoopClearDynamicGroups = _MldSnoopClearDynamicGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 23),
    _MldSnoopClearDynamicGroups_Type()
)
mldSnoopClearDynamicGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopClearDynamicGroups.setStatus("current")
_MldSnoopVlanTable_Object = MibTable
mldSnoopVlanTable = _MldSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24)
)
if mibBuilder.loadTexts:
    mldSnoopVlanTable.setStatus("current")
_MldSnoopVlanEntry_Object = MibTableRow
mldSnoopVlanEntry = _MldSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1)
)
mldSnoopVlanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "mldSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    mldSnoopVlanEntry.setStatus("current")
_MldSnoopVlanIndex_Type = VlanIndex
_MldSnoopVlanIndex_Object = MibTableColumn
mldSnoopVlanIndex = _MldSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 1),
    _MldSnoopVlanIndex_Type()
)
mldSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldSnoopVlanIndex.setStatus("current")
_MldSnoopVlanNumGroups_Type = Unsigned32
_MldSnoopVlanNumGroups_Object = MibTableColumn
mldSnoopVlanNumGroups = _MldSnoopVlanNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 2),
    _MldSnoopVlanNumGroups_Type()
)
mldSnoopVlanNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumGroups.setStatus("current")
_MldSnoopVlanNumJoinSend_Type = Unsigned32
_MldSnoopVlanNumJoinSend_Object = MibTableColumn
mldSnoopVlanNumJoinSend = _MldSnoopVlanNumJoinSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 3),
    _MldSnoopVlanNumJoinSend_Type()
)
mldSnoopVlanNumJoinSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumJoinSend.setStatus("current")
_MldSnoopVlanNumJoins_Type = Unsigned32
_MldSnoopVlanNumJoins_Object = MibTableColumn
mldSnoopVlanNumJoins = _MldSnoopVlanNumJoins_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 4),
    _MldSnoopVlanNumJoins_Type()
)
mldSnoopVlanNumJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumJoins.setStatus("current")
_MldSnoopVlanNumJoinSuccess_Type = Unsigned32
_MldSnoopVlanNumJoinSuccess_Object = MibTableColumn
mldSnoopVlanNumJoinSuccess = _MldSnoopVlanNumJoinSuccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 5),
    _MldSnoopVlanNumJoinSuccess_Type()
)
mldSnoopVlanNumJoinSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumJoinSuccess.setStatus("current")
_MldSnoopVlanNumLeavesSend_Type = Unsigned32
_MldSnoopVlanNumLeavesSend_Object = MibTableColumn
mldSnoopVlanNumLeavesSend = _MldSnoopVlanNumLeavesSend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 6),
    _MldSnoopVlanNumLeavesSend_Type()
)
mldSnoopVlanNumLeavesSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumLeavesSend.setStatus("current")
_MldSnoopVlanNumLeaves_Type = Unsigned32
_MldSnoopVlanNumLeaves_Object = MibTableColumn
mldSnoopVlanNumLeaves = _MldSnoopVlanNumLeaves_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 7),
    _MldSnoopVlanNumLeaves_Type()
)
mldSnoopVlanNumLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumLeaves.setStatus("current")
_MldSnoopVlanNumGeneralQuerySend_Type = Unsigned32
_MldSnoopVlanNumGeneralQuerySend_Object = MibTableColumn
mldSnoopVlanNumGeneralQuerySend = _MldSnoopVlanNumGeneralQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 8),
    _MldSnoopVlanNumGeneralQuerySend_Type()
)
mldSnoopVlanNumGeneralQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumGeneralQuerySend.setStatus("current")
_MldSnoopVlanNumGeneralQueryRecevied_Type = Unsigned32
_MldSnoopVlanNumGeneralQueryRecevied_Object = MibTableColumn
mldSnoopVlanNumGeneralQueryRecevied = _MldSnoopVlanNumGeneralQueryRecevied_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 9),
    _MldSnoopVlanNumGeneralQueryRecevied_Type()
)
mldSnoopVlanNumGeneralQueryRecevied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumGeneralQueryRecevied.setStatus("current")
_MldSnoopVlanNumSepcificQuerySend_Type = Unsigned32
_MldSnoopVlanNumSepcificQuerySend_Object = MibTableColumn
mldSnoopVlanNumSepcificQuerySend = _MldSnoopVlanNumSepcificQuerySend_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 10),
    _MldSnoopVlanNumSepcificQuerySend_Type()
)
mldSnoopVlanNumSepcificQuerySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumSepcificQuerySend.setStatus("current")
_MldsnoopVlanNumSpecificQueryReceived_Type = Unsigned32
_MldsnoopVlanNumSpecificQueryReceived_Object = MibTableColumn
mldsnoopVlanNumSpecificQueryReceived = _MldsnoopVlanNumSpecificQueryReceived_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 11),
    _MldsnoopVlanNumSpecificQueryReceived_Type()
)
mldsnoopVlanNumSpecificQueryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldsnoopVlanNumSpecificQueryReceived.setStatus("current")
_MldSnoopVlanNumInvalidReport_Type = Unsigned32
_MldSnoopVlanNumInvalidReport_Object = MibTableColumn
mldSnoopVlanNumInvalidReport = _MldSnoopVlanNumInvalidReport_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 12),
    _MldSnoopVlanNumInvalidReport_Type()
)
mldSnoopVlanNumInvalidReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldSnoopVlanNumInvalidReport.setStatus("current")
_MldSnoopVlanClearStatistics_Type = TruthValue
_MldSnoopVlanClearStatistics_Object = MibTableColumn
mldSnoopVlanClearStatistics = _MldSnoopVlanClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 54, 24, 1, 13),
    _MldSnoopVlanClearStatistics_Type()
)
mldSnoopVlanClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mldSnoopVlanClearStatistics.setStatus("current")
_DynamicArpInspectionMgt_ObjectIdentity = ObjectIdentity
dynamicArpInspectionMgt = _DynamicArpInspectionMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56)
)
_DaiGlobal_ObjectIdentity = ObjectIdentity
daiGlobal = _DaiGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 1)
)
_DaiGlobalStatus_Type = EnabledStatus
_DaiGlobalStatus_Object = MibScalar
daiGlobalStatus = _DaiGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 1, 1),
    _DaiGlobalStatus_Type()
)
daiGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalStatus.setStatus("current")
_DaiGlobalSrcMacValidation_Type = EnabledStatus
_DaiGlobalSrcMacValidation_Object = MibScalar
daiGlobalSrcMacValidation = _DaiGlobalSrcMacValidation_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 1, 2),
    _DaiGlobalSrcMacValidation_Type()
)
daiGlobalSrcMacValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalSrcMacValidation.setStatus("current")
_DaiGlobalDestMacValidation_Type = EnabledStatus
_DaiGlobalDestMacValidation_Object = MibScalar
daiGlobalDestMacValidation = _DaiGlobalDestMacValidation_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 1, 3),
    _DaiGlobalDestMacValidation_Type()
)
daiGlobalDestMacValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalDestMacValidation.setStatus("current")
_DaiGlobalIpAddrValidation_Type = EnabledStatus
_DaiGlobalIpAddrValidation_Object = MibScalar
daiGlobalIpAddrValidation = _DaiGlobalIpAddrValidation_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 1, 4),
    _DaiGlobalIpAddrValidation_Type()
)
daiGlobalIpAddrValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalIpAddrValidation.setStatus("current")


class _DaiGlobalLogNumber_Type(Integer32):
    """Custom type daiGlobalLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_DaiGlobalLogNumber_Type.__name__ = "Integer32"
_DaiGlobalLogNumber_Object = MibScalar
daiGlobalLogNumber = _DaiGlobalLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 1, 5),
    _DaiGlobalLogNumber_Type()
)
daiGlobalLogNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalLogNumber.setStatus("current")


class _DaiGlobalLogInterval_Type(Integer32):
    """Custom type daiGlobalLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DaiGlobalLogInterval_Type.__name__ = "Integer32"
_DaiGlobalLogInterval_Object = MibScalar
daiGlobalLogInterval = _DaiGlobalLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 1, 6),
    _DaiGlobalLogInterval_Type()
)
daiGlobalLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalLogInterval.setStatus("current")
_DaiGlobalAdditionalValidStatus_Type = EnabledStatus
_DaiGlobalAdditionalValidStatus_Object = MibScalar
daiGlobalAdditionalValidStatus = _DaiGlobalAdditionalValidStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 1, 7),
    _DaiGlobalAdditionalValidStatus_Type()
)
daiGlobalAdditionalValidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiGlobalAdditionalValidStatus.setStatus("current")
_DaiGlobalIpAddrValidationAllowZeros_Type = EnabledStatus
_DaiGlobalIpAddrValidationAllowZeros_Object = MibScalar
daiGlobalIpAddrValidationAllowZeros = _DaiGlobalIpAddrValidationAllowZeros_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 1, 8),
    _DaiGlobalIpAddrValidationAllowZeros_Type()
)
daiGlobalIpAddrValidationAllowZeros.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalIpAddrValidationAllowZeros.setStatus("current")
_DaiVlan_ObjectIdentity = ObjectIdentity
daiVlan = _DaiVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 2)
)
_DaiVlanTable_Object = MibTable
daiVlanTable = _DaiVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 2, 1)
)
if mibBuilder.loadTexts:
    daiVlanTable.setStatus("current")
_DaiVlanEntry_Object = MibTableRow
daiVlanEntry = _DaiVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 2, 1, 1)
)
daiVlanEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "daiVlanIndex"),
)
if mibBuilder.loadTexts:
    daiVlanEntry.setStatus("current")
_DaiVlanIndex_Type = VlanIndex
_DaiVlanIndex_Object = MibTableColumn
daiVlanIndex = _DaiVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 2, 1, 1, 1),
    _DaiVlanIndex_Type()
)
daiVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    daiVlanIndex.setStatus("current")
_DaiVlanStatus_Type = EnabledStatus
_DaiVlanStatus_Object = MibTableColumn
daiVlanStatus = _DaiVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 2, 1, 1, 2),
    _DaiVlanStatus_Type()
)
daiVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiVlanStatus.setStatus("current")


class _DaiVlanArpAclName_Type(DisplayString):
    """Custom type daiVlanArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DaiVlanArpAclName_Type.__name__ = "DisplayString"
_DaiVlanArpAclName_Object = MibTableColumn
daiVlanArpAclName = _DaiVlanArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 2, 1, 1, 3),
    _DaiVlanArpAclName_Type()
)
daiVlanArpAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiVlanArpAclName.setStatus("current")


class _DaiVlanArpAclStatus_Type(Integer32):
    """Custom type daiVlanArpAclStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_DaiVlanArpAclStatus_Type.__name__ = "Integer32"
_DaiVlanArpAclStatus_Object = MibTableColumn
daiVlanArpAclStatus = _DaiVlanArpAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 2, 1, 1, 4),
    _DaiVlanArpAclStatus_Type()
)
daiVlanArpAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiVlanArpAclStatus.setStatus("current")
_DaiInterface_ObjectIdentity = ObjectIdentity
daiInterface = _DaiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 3)
)
_DaiPortTable_Object = MibTable
daiPortTable = _DaiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 3, 1)
)
if mibBuilder.loadTexts:
    daiPortTable.setStatus("current")
_DaiPortEntry_Object = MibTableRow
daiPortEntry = _DaiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 3, 1, 1)
)
daiPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "daiPortIfIndex"),
)
if mibBuilder.loadTexts:
    daiPortEntry.setStatus("current")
_DaiPortIfIndex_Type = InterfaceIndex
_DaiPortIfIndex_Object = MibTableColumn
daiPortIfIndex = _DaiPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 3, 1, 1, 1),
    _DaiPortIfIndex_Type()
)
daiPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    daiPortIfIndex.setStatus("current")
_DaiPortTrustStatus_Type = EnabledStatus
_DaiPortTrustStatus_Object = MibTableColumn
daiPortTrustStatus = _DaiPortTrustStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 3, 1, 1, 2),
    _DaiPortTrustStatus_Type()
)
daiPortTrustStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiPortTrustStatus.setStatus("current")


class _DaiPortRateLimit_Type(Unsigned32):
    """Custom type daiPortRateLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_DaiPortRateLimit_Type.__name__ = "Unsigned32"
_DaiPortRateLimit_Object = MibTableColumn
daiPortRateLimit = _DaiPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 3, 1, 1, 3),
    _DaiPortRateLimit_Type()
)
daiPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiPortRateLimit.setStatus("current")
_DaiLog_ObjectIdentity = ObjectIdentity
daiLog = _DaiLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4)
)
_DaiLogTable_Object = MibTable
daiLogTable = _DaiLogTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4, 1)
)
if mibBuilder.loadTexts:
    daiLogTable.setStatus("current")
_DaiLogEntry_Object = MibTableRow
daiLogEntry = _DaiLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4, 1, 1)
)
daiLogEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "daiLogIndex"),
)
if mibBuilder.loadTexts:
    daiLogEntry.setStatus("current")


class _DaiLogIndex_Type(Integer32):
    """Custom type daiLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DaiLogIndex_Type.__name__ = "Integer32"
_DaiLogIndex_Object = MibTableColumn
daiLogIndex = _DaiLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4, 1, 1, 1),
    _DaiLogIndex_Type()
)
daiLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    daiLogIndex.setStatus("current")
_DaiLogVlan_Type = VlanIndex
_DaiLogVlan_Object = MibTableColumn
daiLogVlan = _DaiLogVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4, 1, 1, 2),
    _DaiLogVlan_Type()
)
daiLogVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogVlan.setStatus("current")
_DaiLogPort_Type = InterfaceIndex
_DaiLogPort_Object = MibTableColumn
daiLogPort = _DaiLogPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4, 1, 1, 3),
    _DaiLogPort_Type()
)
daiLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogPort.setStatus("current")
_DaiLogSrcIpAddress_Type = IpAddress
_DaiLogSrcIpAddress_Object = MibTableColumn
daiLogSrcIpAddress = _DaiLogSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4, 1, 1, 4),
    _DaiLogSrcIpAddress_Type()
)
daiLogSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogSrcIpAddress.setStatus("current")
_DaiLogDestIpAddress_Type = IpAddress
_DaiLogDestIpAddress_Object = MibTableColumn
daiLogDestIpAddress = _DaiLogDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4, 1, 1, 5),
    _DaiLogDestIpAddress_Type()
)
daiLogDestIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogDestIpAddress.setStatus("current")
_DaiLogSrcMacAddress_Type = MacAddress
_DaiLogSrcMacAddress_Object = MibTableColumn
daiLogSrcMacAddress = _DaiLogSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4, 1, 1, 6),
    _DaiLogSrcMacAddress_Type()
)
daiLogSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogSrcMacAddress.setStatus("current")
_DaiLogDestMacAddress_Type = MacAddress
_DaiLogDestMacAddress_Object = MibTableColumn
daiLogDestMacAddress = _DaiLogDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 4, 1, 1, 7),
    _DaiLogDestMacAddress_Type()
)
daiLogDestMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogDestMacAddress.setStatus("current")
_DaiStatistics_ObjectIdentity = ObjectIdentity
daiStatistics = _DaiStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 5)
)
_DaiTotalReceivedPkts_Type = Counter32
_DaiTotalReceivedPkts_Object = MibScalar
daiTotalReceivedPkts = _DaiTotalReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 5, 1),
    _DaiTotalReceivedPkts_Type()
)
daiTotalReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalReceivedPkts.setStatus("current")
_DaiTotalDroppedPkts_Type = Counter32
_DaiTotalDroppedPkts_Object = MibScalar
daiTotalDroppedPkts = _DaiTotalDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 5, 2),
    _DaiTotalDroppedPkts_Type()
)
daiTotalDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalDroppedPkts.setStatus("current")
_DaiTotalProcessedPkts_Type = Counter32
_DaiTotalProcessedPkts_Object = MibScalar
daiTotalProcessedPkts = _DaiTotalProcessedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 5, 3),
    _DaiTotalProcessedPkts_Type()
)
daiTotalProcessedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalProcessedPkts.setStatus("current")
_DaiTotalSrcMacDroppedPkts_Type = Counter32
_DaiTotalSrcMacDroppedPkts_Object = MibScalar
daiTotalSrcMacDroppedPkts = _DaiTotalSrcMacDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 5, 4),
    _DaiTotalSrcMacDroppedPkts_Type()
)
daiTotalSrcMacDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalSrcMacDroppedPkts.setStatus("current")
_DaiTotalDestMacDroppedPkts_Type = Counter32
_DaiTotalDestMacDroppedPkts_Object = MibScalar
daiTotalDestMacDroppedPkts = _DaiTotalDestMacDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 5, 5),
    _DaiTotalDestMacDroppedPkts_Type()
)
daiTotalDestMacDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalDestMacDroppedPkts.setStatus("current")
_DaiTotalIpAddrDroppedPkts_Type = Counter32
_DaiTotalIpAddrDroppedPkts_Object = MibScalar
daiTotalIpAddrDroppedPkts = _DaiTotalIpAddrDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 5, 6),
    _DaiTotalIpAddrDroppedPkts_Type()
)
daiTotalIpAddrDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalIpAddrDroppedPkts.setStatus("current")
_DaiTotalArpAclDroppedPkts_Type = Counter32
_DaiTotalArpAclDroppedPkts_Object = MibScalar
daiTotalArpAclDroppedPkts = _DaiTotalArpAclDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 5, 7),
    _DaiTotalArpAclDroppedPkts_Type()
)
daiTotalArpAclDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalArpAclDroppedPkts.setStatus("current")
_DaiTotalDhcpSnoopingDroppedPkts_Type = Counter32
_DaiTotalDhcpSnoopingDroppedPkts_Object = MibScalar
daiTotalDhcpSnoopingDroppedPkts = _DaiTotalDhcpSnoopingDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 56, 5, 8),
    _DaiTotalDhcpSnoopingDroppedPkts_Type()
)
daiTotalDhcpSnoopingDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalDhcpSnoopingDroppedPkts.setStatus("current")
_TimeRangeMgt_ObjectIdentity = ObjectIdentity
timeRangeMgt = _TimeRangeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61)
)
_TimeRangeTable_Object = MibTable
timeRangeTable = _TimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 1)
)
if mibBuilder.loadTexts:
    timeRangeTable.setStatus("current")
_TimeRangeEntry_Object = MibTableRow
timeRangeEntry = _TimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 1, 1)
)
timeRangeEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "timeRangeIndex"),
)
if mibBuilder.loadTexts:
    timeRangeEntry.setStatus("current")
_TimeRangeIndex_Type = Integer32
_TimeRangeIndex_Object = MibTableColumn
timeRangeIndex = _TimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 1, 1, 1),
    _TimeRangeIndex_Type()
)
timeRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRangeIndex.setStatus("current")


class _TimeRangeName_Type(DisplayString):
    """Custom type timeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TimeRangeName_Type.__name__ = "DisplayString"
_TimeRangeName_Object = MibTableColumn
timeRangeName = _TimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 1, 1, 2),
    _TimeRangeName_Type()
)
timeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeName.setStatus("current")
_TimeRangeStatus_Type = ValidStatus
_TimeRangeStatus_Object = MibTableColumn
timeRangeStatus = _TimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 1, 1, 3),
    _TimeRangeStatus_Type()
)
timeRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeStatus.setStatus("current")
_TimeRangePeriodicTable_Object = MibTable
timeRangePeriodicTable = _TimeRangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2)
)
if mibBuilder.loadTexts:
    timeRangePeriodicTable.setStatus("current")
_TimeRangePeriodicEntry_Object = MibTableRow
timeRangePeriodicEntry = _TimeRangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2, 1)
)
timeRangePeriodicEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "timeRangePeriodicTimeRangeIndex"),
    (0, "ECS2100-28PP-MIB", "timeRangePeriodicStartDaysOfTheWeek"),
    (0, "ECS2100-28PP-MIB", "timeRangePeriodicStartHours"),
    (0, "ECS2100-28PP-MIB", "timeRangePeriodicStartMinutes"),
    (0, "ECS2100-28PP-MIB", "timeRangePeriodicEndDaysOfTheWeek"),
    (0, "ECS2100-28PP-MIB", "timeRangePeriodicEndHours"),
    (0, "ECS2100-28PP-MIB", "timeRangePeriodicEndMinutes"),
)
if mibBuilder.loadTexts:
    timeRangePeriodicEntry.setStatus("current")
_TimeRangePeriodicTimeRangeIndex_Type = Integer32
_TimeRangePeriodicTimeRangeIndex_Object = MibTableColumn
timeRangePeriodicTimeRangeIndex = _TimeRangePeriodicTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2, 1, 1),
    _TimeRangePeriodicTimeRangeIndex_Type()
)
timeRangePeriodicTimeRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangePeriodicTimeRangeIndex.setStatus("current")


class _TimeRangePeriodicStartDaysOfTheWeek_Type(Integer32):
    """Custom type timeRangePeriodicStartDaysOfTheWeek based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("daily", 7),
          ("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3),
          ("weekdays", 8),
          ("weekend", 9))
    )


_TimeRangePeriodicStartDaysOfTheWeek_Type.__name__ = "Integer32"
_TimeRangePeriodicStartDaysOfTheWeek_Object = MibTableColumn
timeRangePeriodicStartDaysOfTheWeek = _TimeRangePeriodicStartDaysOfTheWeek_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2, 1, 2),
    _TimeRangePeriodicStartDaysOfTheWeek_Type()
)
timeRangePeriodicStartDaysOfTheWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicStartDaysOfTheWeek.setStatus("current")


class _TimeRangePeriodicStartHours_Type(Integer32):
    """Custom type timeRangePeriodicStartHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TimeRangePeriodicStartHours_Type.__name__ = "Integer32"
_TimeRangePeriodicStartHours_Object = MibTableColumn
timeRangePeriodicStartHours = _TimeRangePeriodicStartHours_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2, 1, 3),
    _TimeRangePeriodicStartHours_Type()
)
timeRangePeriodicStartHours.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangePeriodicStartHours.setStatus("current")


class _TimeRangePeriodicStartMinutes_Type(Integer32):
    """Custom type timeRangePeriodicStartMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TimeRangePeriodicStartMinutes_Type.__name__ = "Integer32"
_TimeRangePeriodicStartMinutes_Object = MibTableColumn
timeRangePeriodicStartMinutes = _TimeRangePeriodicStartMinutes_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2, 1, 4),
    _TimeRangePeriodicStartMinutes_Type()
)
timeRangePeriodicStartMinutes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangePeriodicStartMinutes.setStatus("current")


class _TimeRangePeriodicEndDaysOfTheWeek_Type(Integer32):
    """Custom type timeRangePeriodicEndDaysOfTheWeek based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("daily", 7),
          ("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3),
          ("weekdays", 8),
          ("weekend", 9))
    )


_TimeRangePeriodicEndDaysOfTheWeek_Type.__name__ = "Integer32"
_TimeRangePeriodicEndDaysOfTheWeek_Object = MibTableColumn
timeRangePeriodicEndDaysOfTheWeek = _TimeRangePeriodicEndDaysOfTheWeek_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2, 1, 5),
    _TimeRangePeriodicEndDaysOfTheWeek_Type()
)
timeRangePeriodicEndDaysOfTheWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicEndDaysOfTheWeek.setStatus("current")


class _TimeRangePeriodicEndHours_Type(Integer32):
    """Custom type timeRangePeriodicEndHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TimeRangePeriodicEndHours_Type.__name__ = "Integer32"
_TimeRangePeriodicEndHours_Object = MibTableColumn
timeRangePeriodicEndHours = _TimeRangePeriodicEndHours_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2, 1, 6),
    _TimeRangePeriodicEndHours_Type()
)
timeRangePeriodicEndHours.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangePeriodicEndHours.setStatus("current")


class _TimeRangePeriodicEndMinutes_Type(Integer32):
    """Custom type timeRangePeriodicEndMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TimeRangePeriodicEndMinutes_Type.__name__ = "Integer32"
_TimeRangePeriodicEndMinutes_Object = MibTableColumn
timeRangePeriodicEndMinutes = _TimeRangePeriodicEndMinutes_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2, 1, 7),
    _TimeRangePeriodicEndMinutes_Type()
)
timeRangePeriodicEndMinutes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangePeriodicEndMinutes.setStatus("current")
_TimeRangePeriodicStatus_Type = ValidStatus
_TimeRangePeriodicStatus_Object = MibTableColumn
timeRangePeriodicStatus = _TimeRangePeriodicStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 2, 1, 8),
    _TimeRangePeriodicStatus_Type()
)
timeRangePeriodicStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangePeriodicStatus.setStatus("current")
_TimeRangeAbsoluteTable_Object = MibTable
timeRangeAbsoluteTable = _TimeRangeAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3)
)
if mibBuilder.loadTexts:
    timeRangeAbsoluteTable.setStatus("current")
_TimeRangeAbsoluteEntry_Object = MibTableRow
timeRangeAbsoluteEntry = _TimeRangeAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1)
)
timeRangeAbsoluteEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteTimeRangeIndex"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteStartYears"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteStartMonths"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteStartDays"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteStartHours"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteStartMinutes"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteEndYears"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteEndMonths"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteEndDays"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteEndHours"),
    (0, "ECS2100-28PP-MIB", "timeRangeAbsoluteEndMinutes"),
)
if mibBuilder.loadTexts:
    timeRangeAbsoluteEntry.setStatus("current")
_TimeRangeAbsoluteTimeRangeIndex_Type = Integer32
_TimeRangeAbsoluteTimeRangeIndex_Object = MibTableColumn
timeRangeAbsoluteTimeRangeIndex = _TimeRangeAbsoluteTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 1),
    _TimeRangeAbsoluteTimeRangeIndex_Type()
)
timeRangeAbsoluteTimeRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteTimeRangeIndex.setStatus("current")


class _TimeRangeAbsoluteStartYears_Type(Integer32):
    """Custom type timeRangeAbsoluteStartYears based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2013, 2037),
        ValueRangeConstraint(65535, 65535),
    )


_TimeRangeAbsoluteStartYears_Type.__name__ = "Integer32"
_TimeRangeAbsoluteStartYears_Object = MibTableColumn
timeRangeAbsoluteStartYears = _TimeRangeAbsoluteStartYears_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 2),
    _TimeRangeAbsoluteStartYears_Type()
)
timeRangeAbsoluteStartYears.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteStartYears.setStatus("current")


class _TimeRangeAbsoluteStartMonths_Type(Integer32):
    """Custom type timeRangeAbsoluteStartMonths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
        ValueRangeConstraint(255, 255),
    )


_TimeRangeAbsoluteStartMonths_Type.__name__ = "Integer32"
_TimeRangeAbsoluteStartMonths_Object = MibTableColumn
timeRangeAbsoluteStartMonths = _TimeRangeAbsoluteStartMonths_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 3),
    _TimeRangeAbsoluteStartMonths_Type()
)
timeRangeAbsoluteStartMonths.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteStartMonths.setStatus("current")


class _TimeRangeAbsoluteStartDays_Type(Integer32):
    """Custom type timeRangeAbsoluteStartDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
        ValueRangeConstraint(255, 255),
    )


_TimeRangeAbsoluteStartDays_Type.__name__ = "Integer32"
_TimeRangeAbsoluteStartDays_Object = MibTableColumn
timeRangeAbsoluteStartDays = _TimeRangeAbsoluteStartDays_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 4),
    _TimeRangeAbsoluteStartDays_Type()
)
timeRangeAbsoluteStartDays.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteStartDays.setStatus("current")


class _TimeRangeAbsoluteStartHours_Type(Integer32):
    """Custom type timeRangeAbsoluteStartHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
        ValueRangeConstraint(255, 255),
    )


_TimeRangeAbsoluteStartHours_Type.__name__ = "Integer32"
_TimeRangeAbsoluteStartHours_Object = MibTableColumn
timeRangeAbsoluteStartHours = _TimeRangeAbsoluteStartHours_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 5),
    _TimeRangeAbsoluteStartHours_Type()
)
timeRangeAbsoluteStartHours.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteStartHours.setStatus("current")


class _TimeRangeAbsoluteStartMinutes_Type(Integer32):
    """Custom type timeRangeAbsoluteStartMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
        ValueRangeConstraint(255, 255),
    )


_TimeRangeAbsoluteStartMinutes_Type.__name__ = "Integer32"
_TimeRangeAbsoluteStartMinutes_Object = MibTableColumn
timeRangeAbsoluteStartMinutes = _TimeRangeAbsoluteStartMinutes_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 6),
    _TimeRangeAbsoluteStartMinutes_Type()
)
timeRangeAbsoluteStartMinutes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteStartMinutes.setStatus("current")


class _TimeRangeAbsoluteEndYears_Type(Integer32):
    """Custom type timeRangeAbsoluteEndYears based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2013, 2037),
        ValueRangeConstraint(65535, 65535),
    )


_TimeRangeAbsoluteEndYears_Type.__name__ = "Integer32"
_TimeRangeAbsoluteEndYears_Object = MibTableColumn
timeRangeAbsoluteEndYears = _TimeRangeAbsoluteEndYears_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 7),
    _TimeRangeAbsoluteEndYears_Type()
)
timeRangeAbsoluteEndYears.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteEndYears.setStatus("current")


class _TimeRangeAbsoluteEndMonths_Type(Integer32):
    """Custom type timeRangeAbsoluteEndMonths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
        ValueRangeConstraint(255, 255),
    )


_TimeRangeAbsoluteEndMonths_Type.__name__ = "Integer32"
_TimeRangeAbsoluteEndMonths_Object = MibTableColumn
timeRangeAbsoluteEndMonths = _TimeRangeAbsoluteEndMonths_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 8),
    _TimeRangeAbsoluteEndMonths_Type()
)
timeRangeAbsoluteEndMonths.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteEndMonths.setStatus("current")


class _TimeRangeAbsoluteEndDays_Type(Integer32):
    """Custom type timeRangeAbsoluteEndDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
        ValueRangeConstraint(255, 255),
    )


_TimeRangeAbsoluteEndDays_Type.__name__ = "Integer32"
_TimeRangeAbsoluteEndDays_Object = MibTableColumn
timeRangeAbsoluteEndDays = _TimeRangeAbsoluteEndDays_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 9),
    _TimeRangeAbsoluteEndDays_Type()
)
timeRangeAbsoluteEndDays.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteEndDays.setStatus("current")


class _TimeRangeAbsoluteEndHours_Type(Integer32):
    """Custom type timeRangeAbsoluteEndHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
        ValueRangeConstraint(255, 255),
    )


_TimeRangeAbsoluteEndHours_Type.__name__ = "Integer32"
_TimeRangeAbsoluteEndHours_Object = MibTableColumn
timeRangeAbsoluteEndHours = _TimeRangeAbsoluteEndHours_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 10),
    _TimeRangeAbsoluteEndHours_Type()
)
timeRangeAbsoluteEndHours.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteEndHours.setStatus("current")


class _TimeRangeAbsoluteEndMinutes_Type(Integer32):
    """Custom type timeRangeAbsoluteEndMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
        ValueRangeConstraint(255, 255),
    )


_TimeRangeAbsoluteEndMinutes_Type.__name__ = "Integer32"
_TimeRangeAbsoluteEndMinutes_Object = MibTableColumn
timeRangeAbsoluteEndMinutes = _TimeRangeAbsoluteEndMinutes_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 11),
    _TimeRangeAbsoluteEndMinutes_Type()
)
timeRangeAbsoluteEndMinutes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeAbsoluteEndMinutes.setStatus("current")
_TimeRangeAbsoluteStatus_Type = ValidStatus
_TimeRangeAbsoluteStatus_Object = MibTableColumn
timeRangeAbsoluteStatus = _TimeRangeAbsoluteStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 61, 3, 1, 12),
    _TimeRangeAbsoluteStatus_Type()
)
timeRangeAbsoluteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeAbsoluteStatus.setStatus("current")
_LbdMgt_ObjectIdentity = ObjectIdentity
lbdMgt = _LbdMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63)
)
_LbdGlobal_ObjectIdentity = ObjectIdentity
lbdGlobal = _LbdGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 1)
)


class _LbdGlobalStatus_Type(Integer32):
    """Custom type lbdGlobalStatus based on Integer32"""
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


_LbdGlobalStatus_Type.__name__ = "Integer32"
_LbdGlobalStatus_Object = MibScalar
lbdGlobalStatus = _LbdGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 1, 1),
    _LbdGlobalStatus_Type()
)
lbdGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdGlobalStatus.setStatus("current")


class _LbdTransmitInterval_Type(Unsigned32):
    """Custom type lbdTransmitInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_LbdTransmitInterval_Type.__name__ = "Unsigned32"
_LbdTransmitInterval_Object = MibScalar
lbdTransmitInterval = _LbdTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 1, 2),
    _LbdTransmitInterval_Type()
)
lbdTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdTransmitInterval.setStatus("current")


class _LbdRecoverTime_Type(Unsigned32):
    """Custom type lbdRecoverTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1000000),
    )


_LbdRecoverTime_Type.__name__ = "Unsigned32"
_LbdRecoverTime_Object = MibScalar
lbdRecoverTime = _LbdRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 1, 3),
    _LbdRecoverTime_Type()
)
lbdRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdRecoverTime.setStatus("current")


class _LbdMode_Type(Integer32):
    """Custom type lbdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-based", 1),
          ("vlan-based", 2))
    )


_LbdMode_Type.__name__ = "Integer32"
_LbdMode_Object = MibScalar
lbdMode = _LbdMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 1, 4),
    _LbdMode_Type()
)
lbdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdMode.setStatus("deprecated")


class _LbdAction_Type(Integer32):
    """Custom type lbdAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("shutdown", 2))
    )


_LbdAction_Type.__name__ = "Integer32"
_LbdAction_Object = MibScalar
lbdAction = _LbdAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 1, 5),
    _LbdAction_Type()
)
lbdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdAction.setStatus("current")


class _LbdTrap_Type(Integer32):
    """Custom type lbdTrap based on Integer32"""
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
        *(("both", 4),
          ("detect", 2),
          ("none", 1),
          ("recover", 3))
    )


_LbdTrap_Type.__name__ = "Integer32"
_LbdTrap_Object = MibScalar
lbdTrap = _LbdTrap_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 1, 6),
    _LbdTrap_Type()
)
lbdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdTrap.setStatus("current")
_LbdInterface_ObjectIdentity = ObjectIdentity
lbdInterface = _LbdInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 2)
)
_LbdPortTable_Object = MibTable
lbdPortTable = _LbdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 2, 1)
)
if mibBuilder.loadTexts:
    lbdPortTable.setStatus("current")
_LbdPortEntry_Object = MibTableRow
lbdPortEntry = _LbdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 2, 1, 1)
)
lbdPortEntry.setIndexNames(
    (0, "ECS2100-28PP-MIB", "lbdPortIfIndex"),
)
if mibBuilder.loadTexts:
    lbdPortEntry.setStatus("current")
_LbdPortIfIndex_Type = InterfaceIndex
_LbdPortIfIndex_Object = MibTableColumn
lbdPortIfIndex = _LbdPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 2, 1, 1, 1),
    _LbdPortIfIndex_Type()
)
lbdPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lbdPortIfIndex.setStatus("current")


class _LbdPortAdminState_Type(Integer32):
    """Custom type lbdPortAdminState based on Integer32"""
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


_LbdPortAdminState_Type.__name__ = "Integer32"
_LbdPortAdminState_Object = MibTableColumn
lbdPortAdminState = _LbdPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 2, 1, 1, 2),
    _LbdPortAdminState_Type()
)
lbdPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdPortAdminState.setStatus("current")


class _LbdPortOperState_Type(Integer32):
    """Custom type lbdPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("looped", 2),
          ("normal", 1))
    )


_LbdPortOperState_Type.__name__ = "Integer32"
_LbdPortOperState_Object = MibTableColumn
lbdPortOperState = _LbdPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 2, 1, 1, 3),
    _LbdPortOperState_Type()
)
lbdPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbdPortOperState.setStatus("current")


class _LbdPortLoopedVlan_Type(OctetString):
    """Custom type lbdPortLoopedVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LbdPortLoopedVlan_Type.__name__ = "OctetString"
_LbdPortLoopedVlan_Object = MibTableColumn
lbdPortLoopedVlan = _LbdPortLoopedVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 1, 63, 2, 1, 1, 4),
    _LbdPortLoopedVlan_Type()
)
lbdPortLoopedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbdPortLoopedVlan.setStatus("current")
_Ecs2100_28ppNotifications_ObjectIdentity = ObjectIdentity
ecs2100_28ppNotifications = _Ecs2100_28ppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2)
)
_Ecs2100_28ppTraps_ObjectIdentity = ObjectIdentity
ecs2100_28ppTraps = _Ecs2100_28ppTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1)
)
_Ecs2100_28ppTrapsPrefix_ObjectIdentity = ObjectIdentity
ecs2100_28ppTrapsPrefix = _Ecs2100_28ppTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0)
)
_Ecs2100_10t_ObjectIdentity = ObjectIdentity
ecs2100_10t = _Ecs2100_10t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 101)
)
_Ecs2100_10pe_ObjectIdentity = ObjectIdentity
ecs2100_10pe = _Ecs2100_10pe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 102)
)
_Ecs2100_10p_ObjectIdentity = ObjectIdentity
ecs2100_10p = _Ecs2100_10p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 103)
)
_Ecs2100_28t_ObjectIdentity = ObjectIdentity
ecs2100_28t = _Ecs2100_28t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 104)
)
_Ecs2100_28p_ObjectIdentity = ObjectIdentity
ecs2100_28p = _Ecs2100_28p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 105)
)
_Ecs2100_28pp_ObjectIdentity = ObjectIdentity
ecs2100_28pp = _Ecs2100_28pp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 106)
)
_Ecs2100_52t_ObjectIdentity = ObjectIdentity
ecs2100_52t = _Ecs2100_52t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 107)
)
_Ecs2110_26t_ObjectIdentity = ObjectIdentity
ecs2110_26t = _Ecs2110_26t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 108)
)
dot1dStpPortEntry.registerAugmentions(
    ("ECS2100-28PP-MIB",
     "staPortEntry")
)
staPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
dot1vProtocolPortEntry.registerAugmentions(
    ("ECS2100-28PP-MIB",
     "dot1vProtocolExPortEntry")
)
dot1vProtocolExPortEntry.setIndexNames(*dot1vProtocolPortEntry.getIndexNames())
dot1qVlanStaticEntry.registerAugmentions(
    ("ECS2100-28PP-MIB",
     "vlanStaticExtEntry")
)
vlanStaticExtEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
dot1xAuthConfigEntry.registerAugmentions(
    ("ECS2100-28PP-MIB",
     "dot1xAuthConfigExtEntry")
)
dot1xAuthConfigExtEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
pethMainPseEntry.registerAugmentions(
    ("ECS2100-28PP-MIB",
     "pethPseMainExtEntry")
)
pethPseMainExtEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethPsePortEntry.registerAugmentions(
    ("ECS2100-28PP-MIB",
     "pethPsePortExtEntry")
)
pethPsePortExtEntry.setIndexNames(*pethPsePortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

swPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 1)
)
swPowerStatusChangeTrap.setObjects(
      *(("ECS2100-28PP-MIB", "swIndivPowerUnitIndex"),
        ("ECS2100-28PP-MIB", "swIndivPowerIndex"),
        ("ECS2100-28PP-MIB", "swIndivPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChangeTrap.setStatus(
        "current"
    )

swPortSecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 36)
)
swPortSecurityTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    swPortSecurityTrap.setStatus(
        "current"
    )

swIpFilterRejectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 40)
)
swIpFilterRejectTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapIpFilterRejectMode"),
        ("ECS2100-28PP-MIB", "trapIpFilterRejectIp"))
)
if mibBuilder.loadTexts:
    swIpFilterRejectTrap.setStatus(
        "current"
    )

pethPsePortOnOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 43)
)
pethPsePortOnOffNotification.setObjects(
    ("ECS2100-28PP-MIB", "pethPsePortDetectionStatus")
)
if mibBuilder.loadTexts:
    pethPsePortOnOffNotification.setStatus(
        "current"
    )

pethPsePortPowerMaintenanceStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 44)
)
pethPsePortPowerMaintenanceStatusNotification.setObjects(
    ("ECS2100-28PP-MIB", "pethPsePortPowerMaintenanceStatus")
)
if mibBuilder.loadTexts:
    pethPsePortPowerMaintenanceStatusNotification.setStatus(
        "current"
    )

pethMainPowerUsageOnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 45)
)
pethMainPowerUsageOnNotification.setObjects(
    ("ECS2100-28PP-MIB", "pethMainPseConsumptionPower")
)
if mibBuilder.loadTexts:
    pethMainPowerUsageOnNotification.setStatus(
        "current"
    )

pethMainPowerUsageOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 46)
)
pethMainPowerUsageOffNotification.setObjects(
    ("ECS2100-28PP-MIB", "pethMainPseConsumptionPower")
)
if mibBuilder.loadTexts:
    pethMainPowerUsageOffNotification.setStatus(
        "current"
    )

swAtcBcastStormAlarmFireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 70)
)
swAtcBcastStormAlarmFireTrap.setObjects(
      *(("ECS2100-28PP-MIB", "atcBcastStormIfIndex"),
        ("ECS2100-28PP-MIB", "atcBcastStormSampleType"),
        ("ECS2100-28PP-MIB", "atcBcastStormCurrentTrafficRate"),
        ("ECS2100-28PP-MIB", "atcBcastStormAlarmFireThreshold"))
)
if mibBuilder.loadTexts:
    swAtcBcastStormAlarmFireTrap.setStatus(
        "current"
    )

swAtcBcastStormAlarmClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 71)
)
swAtcBcastStormAlarmClearTrap.setObjects(
      *(("ECS2100-28PP-MIB", "atcBcastStormIfIndex"),
        ("ECS2100-28PP-MIB", "atcBcastStormSampleType"),
        ("ECS2100-28PP-MIB", "atcBcastStormCurrentTrafficRate"),
        ("ECS2100-28PP-MIB", "atcBcastStormAlarmClearThreshold"))
)
if mibBuilder.loadTexts:
    swAtcBcastStormAlarmClearTrap.setStatus(
        "current"
    )

swAtcBcastStormTcApplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 72)
)
swAtcBcastStormTcApplyTrap.setObjects(
      *(("ECS2100-28PP-MIB", "atcBcastStormIfIndex"),
        ("ECS2100-28PP-MIB", "atcBcastStormSampleType"),
        ("ECS2100-28PP-MIB", "atcBcastStormCurrentTrafficRate"),
        ("ECS2100-28PP-MIB", "atcBcastStormAlarmFireThreshold"),
        ("ECS2100-28PP-MIB", "atcBcastStormTcApplyTime"))
)
if mibBuilder.loadTexts:
    swAtcBcastStormTcApplyTrap.setStatus(
        "current"
    )

swAtcBcastStormTcReleaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 73)
)
swAtcBcastStormTcReleaseTrap.setObjects(
      *(("ECS2100-28PP-MIB", "atcBcastStormIfIndex"),
        ("ECS2100-28PP-MIB", "atcBcastStormSampleType"),
        ("ECS2100-28PP-MIB", "atcBcastStormCurrentTrafficRate"),
        ("ECS2100-28PP-MIB", "atcBcastStormAlarmClearThreshold"),
        ("ECS2100-28PP-MIB", "atcBcastStormTcReleaseTime"))
)
if mibBuilder.loadTexts:
    swAtcBcastStormTcReleaseTrap.setStatus(
        "current"
    )

swAtcMcastStormAlarmFireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 74)
)
swAtcMcastStormAlarmFireTrap.setObjects(
      *(("ECS2100-28PP-MIB", "atcMcastStormIfIndex"),
        ("ECS2100-28PP-MIB", "atcMcastStormSampleType"),
        ("ECS2100-28PP-MIB", "atcMcastStormCurrentTrafficRate"),
        ("ECS2100-28PP-MIB", "atcMcastStormAlarmFireThreshold"))
)
if mibBuilder.loadTexts:
    swAtcMcastStormAlarmFireTrap.setStatus(
        "current"
    )

swAtcMcastStormAlarmClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 75)
)
swAtcMcastStormAlarmClearTrap.setObjects(
      *(("ECS2100-28PP-MIB", "atcMcastStormIfIndex"),
        ("ECS2100-28PP-MIB", "atcMcastStormSampleType"),
        ("ECS2100-28PP-MIB", "atcMcastStormCurrentTrafficRate"),
        ("ECS2100-28PP-MIB", "atcMcastStormAlarmClearThreshold"))
)
if mibBuilder.loadTexts:
    swAtcMcastStormAlarmClearTrap.setStatus(
        "current"
    )

swAtcMcastStormTcApplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 76)
)
swAtcMcastStormTcApplyTrap.setObjects(
      *(("ECS2100-28PP-MIB", "atcMcastStormIfIndex"),
        ("ECS2100-28PP-MIB", "atcMcastStormSampleType"),
        ("ECS2100-28PP-MIB", "atcMcastStormCurrentTrafficRate"),
        ("ECS2100-28PP-MIB", "atcMcastStormAlarmFireThreshold"),
        ("ECS2100-28PP-MIB", "atcMcastStormTcApplyTime"))
)
if mibBuilder.loadTexts:
    swAtcMcastStormTcApplyTrap.setStatus(
        "current"
    )

swAtcMcastStormTcReleaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 77)
)
swAtcMcastStormTcReleaseTrap.setObjects(
      *(("ECS2100-28PP-MIB", "atcMcastStormIfIndex"),
        ("ECS2100-28PP-MIB", "atcMcastStormSampleType"),
        ("ECS2100-28PP-MIB", "atcMcastStormCurrentTrafficRate"),
        ("ECS2100-28PP-MIB", "atcMcastStormAlarmClearThreshold"),
        ("ECS2100-28PP-MIB", "atcMcastStormTcReleaseTime"))
)
if mibBuilder.loadTexts:
    swAtcMcastStormTcReleaseTrap.setStatus(
        "current"
    )

stpBpduGuardPortShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 91)
)
stpBpduGuardPortShutdownTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    stpBpduGuardPortShutdownTrap.setStatus(
        "current"
    )

swLoopbackDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 95)
)
swLoopbackDetectionTrap.setObjects(
    ("ECS2100-28PP-MIB", "staLoopbackDetectionPortIfIndex")
)
if mibBuilder.loadTexts:
    swLoopbackDetectionTrap.setStatus(
        "current"
    )

networkAccessPortLinkDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 96)
)
networkAccessPortLinkDetectionTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifOperStatus"),
        ("ECS2100-28PP-MIB", "networkAccessPortLinkDetectionMode"),
        ("ECS2100-28PP-MIB", "networkAccessPortLinkDetectionAciton"))
)
if mibBuilder.loadTexts:
    networkAccessPortLinkDetectionTrap.setStatus(
        "current"
    )

dot1agCfmMepUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 97)
)
dot1agCfmMepUpTrap.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmMepUpTrap.setStatus(
        "current"
    )

dot1agCfmMepDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 98)
)
dot1agCfmMepDownTrap.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmMepDownTrap.setStatus(
        "current"
    )

dot1agCfmConfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 99)
)
dot1agCfmConfigFailTrap.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmConfigFailTrap.setStatus(
        "current"
    )

dot1agCfmLoopFindTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 100)
)
dot1agCfmLoopFindTrap.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmLoopFindTrap.setStatus(
        "current"
    )

dot1agCfmMepUnknownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 101)
)
dot1agCfmMepUnknownTrap.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmMepUnknownTrap.setStatus(
        "current"
    )

dot1agCfmMepMissingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 102)
)
dot1agCfmMepMissingTrap.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmMepMissingTrap.setStatus(
        "current"
    )

dot1agCfmMaUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 103)
)
dot1agCfmMaUpTrap.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex")
)
if mibBuilder.loadTexts:
    dot1agCfmMaUpTrap.setStatus(
        "current"
    )

autoUpgradeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 104)
)
autoUpgradeTrap.setObjects(
      *(("ECS2100-28PP-MIB", "fileCopyFileType"),
        ("ECS2100-28PP-MIB", "trapAutoUpgradeResult"),
        ("ECS2100-28PP-MIB", "trapAutoUpgradeNewVer"))
)
if mibBuilder.loadTexts:
    autoUpgradeTrap.setStatus(
        "current"
    )

swCpuUtiRisingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 107)
)
if mibBuilder.loadTexts:
    swCpuUtiRisingNotification.setStatus(
        "current"
    )

swCpuUtiFallingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 108)
)
if mibBuilder.loadTexts:
    swCpuUtiFallingNotification.setStatus(
        "current"
    )

swMemoryUtiRisingThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 109)
)
if mibBuilder.loadTexts:
    swMemoryUtiRisingThresholdNotification.setStatus(
        "current"
    )

swMemoryUtiFallingThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 110)
)
if mibBuilder.loadTexts:
    swMemoryUtiFallingThresholdNotification.setStatus(
        "current"
    )

dhcpRogueServerAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 114)
)
dhcpRogueServerAttackTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapDhcpClientPortIfIndex"),
        ("ECS2100-28PP-MIB", "trapDhcpServerIpAddress"),
        ("ECS2100-28PP-MIB", "trapDhcpServerMacAddress"))
)
if mibBuilder.loadTexts:
    dhcpRogueServerAttackTrap.setStatus(
        "current"
    )

macNotificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 138)
)
macNotificationTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapIfIndex"),
        ("ECS2100-28PP-MIB", "trapVlanId"),
        ("ECS2100-28PP-MIB", "trapVarMacAddr"),
        ("ECS2100-28PP-MIB", "trapMacNotifyAction"))
)
if mibBuilder.loadTexts:
    macNotificationTrap.setStatus(
        "current"
    )

lbdDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 141)
)
lbdDetectionTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapIfIndex"),
        ("ECS2100-28PP-MIB", "trapVlanId"))
)
if mibBuilder.loadTexts:
    lbdDetectionTrap.setStatus(
        "current"
    )

lbdRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 142)
)
lbdRecoveryTrap.setObjects(
    ("ECS2100-28PP-MIB", "trapIfIndex")
)
if mibBuilder.loadTexts:
    lbdRecoveryTrap.setStatus(
        "current"
    )

sfpThresholdAlarmWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 189)
)
sfpThresholdAlarmWarnTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapSfpThresholdAlarmWarnIfIndex"),
        ("ECS2100-28PP-MIB", "trapSfpThresholdAlarmWarnType"))
)
if mibBuilder.loadTexts:
    sfpThresholdAlarmWarnTrap.setStatus(
        "current"
    )

udldPortShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 192)
)
udldPortShutdownTrap.setObjects(
      *(("ECS2100-28PP-MIB", "udldPortIndex"),
        ("ECS2100-28PP-MIB", "trapUdldPortShutdownReason"))
)
if mibBuilder.loadTexts:
    udldPortShutdownTrap.setStatus(
        "current"
    )

userAuthenticationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 199)
)
userAuthenticationFailureTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapVarLoginUserName"),
        ("ECS2100-28PP-MIB", "trapVarSessionType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddressType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddress"))
)
if mibBuilder.loadTexts:
    userAuthenticationFailureTrap.setStatus(
        "current"
    )

userAuthenticationSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 200)
)
userAuthenticationSuccessTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapVarLoginUserName"),
        ("ECS2100-28PP-MIB", "trapVarSessionType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddressType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddress"))
)
if mibBuilder.loadTexts:
    userAuthenticationSuccessTrap.setStatus(
        "current"
    )

loginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 201)
)
loginTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapVarLoginUserName"),
        ("ECS2100-28PP-MIB", "trapVarSessionType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddressType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddress"))
)
if mibBuilder.loadTexts:
    loginTrap.setStatus(
        "current"
    )

logoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 202)
)
logoutTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapVarLoginUserName"),
        ("ECS2100-28PP-MIB", "trapVarSessionType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddressType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddress"))
)
if mibBuilder.loadTexts:
    logoutTrap.setStatus(
        "current"
    )

fileCopyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 208)
)
fileCopyTrap.setObjects(
      *(("ECS2100-28PP-MIB", "trapVarLoginUserName"),
        ("ECS2100-28PP-MIB", "trapVarSessionType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddressType"),
        ("ECS2100-28PP-MIB", "trapVarLoginInetAddress"),
        ("ECS2100-28PP-MIB", "fileCopySrcOperType"),
        ("ECS2100-28PP-MIB", "fileCopySrcFileName"),
        ("ECS2100-28PP-MIB", "fileCopyDestOperType"),
        ("ECS2100-28PP-MIB", "fileCopyDestFileName"),
        ("ECS2100-28PP-MIB", "fileCopyFileType"),
        ("ECS2100-28PP-MIB", "fileCopyUnitId"),
        ("ECS2100-28PP-MIB", "fileCopyStatus"),
        ("ECS2100-28PP-MIB", "fileCopyServerInetAddressType"),
        ("ECS2100-28PP-MIB", "fileCopyServerInetAddress"))
)
if mibBuilder.loadTexts:
    fileCopyTrap.setStatus(
        "current"
    )

userauthCreateUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 209)
)
userauthCreateUserTrap.setObjects(
    ("ECS2100-28PP-MIB", "userAuthUserName")
)
if mibBuilder.loadTexts:
    userauthCreateUserTrap.setStatus(
        "current"
    )

userauthDeleteUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 210)
)
userauthDeleteUserTrap.setObjects(
    ("ECS2100-28PP-MIB", "userAuthUserName")
)
if mibBuilder.loadTexts:
    userauthDeleteUserTrap.setStatus(
        "current"
    )

userauthModifyUserPrivilegeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 211)
)
userauthModifyUserPrivilegeTrap.setObjects(
      *(("ECS2100-28PP-MIB", "userAuthUserName"),
        ("ECS2100-28PP-MIB", "userAuthPrivilege"))
)
if mibBuilder.loadTexts:
    userauthModifyUserPrivilegeTrap.setStatus(
        "current"
    )

cpuGuardControlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 213)
)
if mibBuilder.loadTexts:
    cpuGuardControlTrap.setStatus(
        "current"
    )

cpuGuardReleaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 43, 2, 1, 0, 214)
)
if mibBuilder.loadTexts:
    cpuGuardReleaseTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ECS2100-28PP-MIB",
    **{"KeySegment": KeySegment,
       "ValidStatus": ValidStatus,
       "StaPathCostMode": StaPathCostMode,
       "accton": accton,
       "edgecoreNetworks": edgecoreNetworks,
       "edgecoreNetworksMgt": edgecoreNetworksMgt,
       "ecs2100-28ppMIB": ecs2100_28ppMIB,
       "ecs2100-28ppMIBObjects": ecs2100_28ppMIBObjects,
       "switchMgt": switchMgt,
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
       "swServiceTag": swServiceTag,
       "swModelNumber": swModelNumber,
       "swEpldVer": swEpldVer,
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
       "switchJumboFrameStatus": switchJumboFrameStatus,
       "amtrMgt": amtrMgt,
       "amtrMacAddrAgingStatus": amtrMacAddrAgingStatus,
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
       "portComboForcedMode": portComboForcedMode,
       "portMasterSlaveModeCfg": portMasterSlaveModeCfg,
       "portMacAddrLearningStatus": portMacAddrLearningStatus,
       "portMacAddrLearningCount": portMacAddrLearningCount,
       "portUpTime": portUpTime,
       "portShutdownReason": portShutdownReason,
       "cableDiagMgt": cableDiagMgt,
       "cableDiagCtlAction": cableDiagCtlAction,
       "cableDiagResultTable": cableDiagResultTable,
       "cableDiagResultEntry": cableDiagResultEntry,
       "cableDiagResultIfIndex": cableDiagResultIfIndex,
       "cableDiagResultStatusPairA": cableDiagResultStatusPairA,
       "cableDiagResultStatusPairB": cableDiagResultStatusPairB,
       "cableDiagResultStatusPairC": cableDiagResultStatusPairC,
       "cableDiagResultStatusPairD": cableDiagResultStatusPairD,
       "cableDiagResultDistancePairA": cableDiagResultDistancePairA,
       "cableDiagResultDistancePairB": cableDiagResultDistancePairB,
       "cableDiagResultDistancePairC": cableDiagResultDistancePairC,
       "cableDiagResultDistancePairD": cableDiagResultDistancePairD,
       "cableDiagResultTime": cableDiagResultTime,
       "portUtilTable": portUtilTable,
       "portUtilEntry": portUtilEntry,
       "portUtilIfIndex": portUtilIfIndex,
       "portInOctetRate": portInOctetRate,
       "portInPacketRate": portInPacketRate,
       "portInUtil": portInUtil,
       "portOutOctetRate": portOutOctetRate,
       "portOutPacketRate": portOutPacketRate,
       "portOutUtil": portOutUtil,
       "portHist": portHist,
       "portHistControlTable": portHistControlTable,
       "portHistControlEntry": portHistControlEntry,
       "portHistControlIndex": portHistControlIndex,
       "portHistControlName": portHistControlName,
       "portHistControlDataSource": portHistControlDataSource,
       "portHistControlInterval": portHistControlInterval,
       "portHistControlBucketsRequested": portHistControlBucketsRequested,
       "portHistControlBucketsGranted": portHistControlBucketsGranted,
       "portHistControlStatus": portHistControlStatus,
       "portHistCurrentTable": portHistCurrentTable,
       "portHistCurrentEntry": portHistCurrentEntry,
       "portHistCurrentIndex": portHistCurrentIndex,
       "portHistCurrentSampleIndex": portHistCurrentSampleIndex,
       "portHistCurrentIntervalStart": portHistCurrentIntervalStart,
       "portHistCurrentInOctets": portHistCurrentInOctets,
       "portHistCurrentInUcastPkts": portHistCurrentInUcastPkts,
       "portHistCurrentInMulticastPkts": portHistCurrentInMulticastPkts,
       "portHistCurrentInBroadcastPkts": portHistCurrentInBroadcastPkts,
       "portHistCurrentInDiscards": portHistCurrentInDiscards,
       "portHistCurrentInErrors": portHistCurrentInErrors,
       "portHistCurrentInUnknownProtos": portHistCurrentInUnknownProtos,
       "portHistCurrentOutOctets": portHistCurrentOutOctets,
       "portHistCurrentOutUcastPkts": portHistCurrentOutUcastPkts,
       "portHistCurrentOutMulticastPkts": portHistCurrentOutMulticastPkts,
       "portHistCurrentOutBroadcastPkts": portHistCurrentOutBroadcastPkts,
       "portHistCurrentOutDiscards": portHistCurrentOutDiscards,
       "portHistCurrentOutErrors": portHistCurrentOutErrors,
       "portHistCurrentInUtilization": portHistCurrentInUtilization,
       "portHistCurrentOutUtilization": portHistCurrentOutUtilization,
       "portHistPreviousTable": portHistPreviousTable,
       "portHistPreviousEntry": portHistPreviousEntry,
       "portHistPreviousIndex": portHistPreviousIndex,
       "portHistPreviousSampleIndex": portHistPreviousSampleIndex,
       "portHistPreviousIntervalStart": portHistPreviousIntervalStart,
       "portHistPreviousInOctets": portHistPreviousInOctets,
       "portHistPreviousInUcastPkts": portHistPreviousInUcastPkts,
       "portHistPreviousInMulticastPkts": portHistPreviousInMulticastPkts,
       "portHistPreviousInBroadcastPkts": portHistPreviousInBroadcastPkts,
       "portHistPreviousInDiscards": portHistPreviousInDiscards,
       "portHistPreviousInErrors": portHistPreviousInErrors,
       "portHistPreviousInUnknownProtos": portHistPreviousInUnknownProtos,
       "portHistPreviousOutOctets": portHistPreviousOutOctets,
       "portHistPreviousOutUcastPkts": portHistPreviousOutUcastPkts,
       "portHistPreviousOutMulticastPkts": portHistPreviousOutMulticastPkts,
       "portHistPreviousOutBroadcastPkts": portHistPreviousOutBroadcastPkts,
       "portHistPreviousOutDiscards": portHistPreviousOutDiscards,
       "portHistPreviousOutErrors": portHistPreviousOutErrors,
       "portHistPreviousInUtilization": portHistPreviousInUtilization,
       "portHistPreviousOutUtilization": portHistPreviousOutUtilization,
       "portMediaInfoTable": portMediaInfoTable,
       "portMediaInfoEntry": portMediaInfoEntry,
       "portMediaInfoIfIndex": portMediaInfoIfIndex,
       "portMediaInfoConnectorType": portMediaInfoConnectorType,
       "portMediaInfoFiberType": portMediaInfoFiberType,
       "portMediaInfoEthComplianceCodes": portMediaInfoEthComplianceCodes,
       "portMediaInfoBaudRate": portMediaInfoBaudRate,
       "portMediaInfoVendorOUI": portMediaInfoVendorOUI,
       "portMediaInfoVendorName": portMediaInfoVendorName,
       "portMediaInfoPartNumber": portMediaInfoPartNumber,
       "portMediaInfoRevision": portMediaInfoRevision,
       "portMediaInfoSerialNumber": portMediaInfoSerialNumber,
       "portMediaInfoDateCode": portMediaInfoDateCode,
       "portOpticalMonitoringInfoTable": portOpticalMonitoringInfoTable,
       "portOpticalMonitoringInfoEntry": portOpticalMonitoringInfoEntry,
       "portOpticalMonitoringInfoIfIndex": portOpticalMonitoringInfoIfIndex,
       "portOpticalMonitoringInfoTemperature": portOpticalMonitoringInfoTemperature,
       "portOpticalMonitoringInfoVcc": portOpticalMonitoringInfoVcc,
       "portOpticalMonitoringInfoTxBiasCurrent": portOpticalMonitoringInfoTxBiasCurrent,
       "portOpticalMonitoringInfoTxPower": portOpticalMonitoringInfoTxPower,
       "portOpticalMonitoringInfoRxPower": portOpticalMonitoringInfoRxPower,
       "portTransceiverThresholdInfoTable": portTransceiverThresholdInfoTable,
       "portTransceiverThresholdInfoEntry": portTransceiverThresholdInfoEntry,
       "portTransceiverThresholdInfoIfIndex": portTransceiverThresholdInfoIfIndex,
       "portTransceiverThresholdInfoTemperatureLowAlarm": portTransceiverThresholdInfoTemperatureLowAlarm,
       "portTransceiverThresholdInfoTemperatureLowWarn": portTransceiverThresholdInfoTemperatureLowWarn,
       "portTransceiverThresholdInfoTemperatureHighWarn": portTransceiverThresholdInfoTemperatureHighWarn,
       "portTransceiverThresholdInfoTemperatureHighAlarm": portTransceiverThresholdInfoTemperatureHighAlarm,
       "portTransceiverThresholdInfoVccLowAlarm": portTransceiverThresholdInfoVccLowAlarm,
       "portTransceiverThresholdInfoVccLowWarn": portTransceiverThresholdInfoVccLowWarn,
       "portTransceiverThresholdInfoVccHighWarn": portTransceiverThresholdInfoVccHighWarn,
       "portTransceiverThresholdInfoVccHighAlarm": portTransceiverThresholdInfoVccHighAlarm,
       "portTransceiverThresholdInfoTxBiasCurrentLowAlarm": portTransceiverThresholdInfoTxBiasCurrentLowAlarm,
       "portTransceiverThresholdInfoTxBiasCurrentLowWarn": portTransceiverThresholdInfoTxBiasCurrentLowWarn,
       "portTransceiverThresholdInfoTxBiasCurrentHighWarn": portTransceiverThresholdInfoTxBiasCurrentHighWarn,
       "portTransceiverThresholdInfoTxBiasCurrentHighAlarm": portTransceiverThresholdInfoTxBiasCurrentHighAlarm,
       "portTransceiverThresholdInfoTxPowerLowAlarm": portTransceiverThresholdInfoTxPowerLowAlarm,
       "portTransceiverThresholdInfoTxPowerLowWarn": portTransceiverThresholdInfoTxPowerLowWarn,
       "portTransceiverThresholdInfoTxPowerHighWarn": portTransceiverThresholdInfoTxPowerHighWarn,
       "portTransceiverThresholdInfoTxPowerHighAlarm": portTransceiverThresholdInfoTxPowerHighAlarm,
       "portTransceiverThresholdInfoRxPowerLowAlarm": portTransceiverThresholdInfoRxPowerLowAlarm,
       "portTransceiverThresholdInfoRxPowerLowWarn": portTransceiverThresholdInfoRxPowerLowWarn,
       "portTransceiverThresholdInfoRxPowerHighWarn": portTransceiverThresholdInfoRxPowerHighWarn,
       "portTransceiverThresholdInfoRxPowerHighAlarm": portTransceiverThresholdInfoRxPowerHighAlarm,
       "portTransceiverThresholdAutoMode": portTransceiverThresholdAutoMode,
       "powerSavingTable": powerSavingTable,
       "powerSavingEntry": powerSavingEntry,
       "powerSavingIfIndex": powerSavingIfIndex,
       "powerSavingStatus": powerSavingStatus,
       "trunkMgt": trunkMgt,
       "trunkMaxId": trunkMaxId,
       "trunkValidNumber": trunkValidNumber,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkIndex": trunkIndex,
       "trunkPorts": trunkPorts,
       "trunkCreation": trunkCreation,
       "trunkStatus": trunkStatus,
       "trunkBalanceMode": trunkBalanceMode,
       "lacpMgt": lacpMgt,
       "lacpPortTable": lacpPortTable,
       "lacpPortEntry": lacpPortEntry,
       "lacpPortIndex": lacpPortIndex,
       "lacpPortStatus": lacpPortStatus,
       "staMgt": staMgt,
       "staSystemStatus": staSystemStatus,
       "staPortTable": staPortTable,
       "staPortEntry": staPortEntry,
       "staPortProtocolMigration": staPortProtocolMigration,
       "staPortOperEdgePort": staPortOperEdgePort,
       "staPortAdminPointToPoint": staPortAdminPointToPoint,
       "staPortOperPointToPoint": staPortOperPointToPoint,
       "staPortSystemStatus": staPortSystemStatus,
       "staPortLongAdminPathCost": staPortLongAdminPathCost,
       "staPortLongOperPathCost": staPortLongOperPathCost,
       "staPortBpduFlooding": staPortBpduFlooding,
       "staPortBpduGuard": staPortBpduGuard,
       "staPortAdminEdgePortWithAuto": staPortAdminEdgePortWithAuto,
       "staPortBpduFilter": staPortBpduFilter,
       "staPortRootGuardStatus": staPortRootGuardStatus,
       "staPortBpduGuardAutoRecovery": staPortBpduGuardAutoRecovery,
       "staPortBpduGuardAutoRecoveryInterval": staPortBpduGuardAutoRecoveryInterval,
       "staPortTcPropStop": staPortTcPropStop,
       "staProtocolType": staProtocolType,
       "staTxHoldCount": staTxHoldCount,
       "staPathCostMethod": staPathCostMethod,
       "xstMgt": xstMgt,
       "mstName": mstName,
       "mstRevision": mstRevision,
       "mstMaxHops": mstMaxHops,
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
       "xstInstancePortDesignatedRoot": xstInstancePortDesignatedRoot,
       "xstInstancePortDesignatedCost": xstInstancePortDesignatedCost,
       "xstInstancePortDesignatedBridge": xstInstancePortDesignatedBridge,
       "xstInstancePortDesignatedPort": xstInstancePortDesignatedPort,
       "xstInstancePortForwardTransitions": xstInstancePortForwardTransitions,
       "xstInstancePortPortRole": xstInstancePortPortRole,
       "xstInstancePortAdminPathCost": xstInstancePortAdminPathCost,
       "xstInstancePortOperPathCost": xstInstancePortOperPathCost,
       "mstInstanceEditTable": mstInstanceEditTable,
       "mstInstanceEditEntry": mstInstanceEditEntry,
       "mstInstanceEditIndex": mstInstanceEditIndex,
       "mstInstanceEditVlansMap": mstInstanceEditVlansMap,
       "mstInstanceEditVlansMap2k": mstInstanceEditVlansMap2k,
       "mstInstanceEditVlansMap3k": mstInstanceEditVlansMap3k,
       "mstInstanceEditVlansMap4k": mstInstanceEditVlansMap4k,
       "mstInstanceEditRemainingHops": mstInstanceEditRemainingHops,
       "mstInstanceOperTable": mstInstanceOperTable,
       "mstInstanceOperEntry": mstInstanceOperEntry,
       "mstInstanceOperIndex": mstInstanceOperIndex,
       "mstInstanceOperVlansMap": mstInstanceOperVlansMap,
       "mstInstanceOperVlansMap2k": mstInstanceOperVlansMap2k,
       "mstInstanceOperVlansMap3k": mstInstanceOperVlansMap3k,
       "mstInstanceOperVlansMap4k": mstInstanceOperVlansMap4k,
       "staLoopbackDetectionPortTable": staLoopbackDetectionPortTable,
       "staLoopbackDetectionPortEntry": staLoopbackDetectionPortEntry,
       "staLoopbackDetectionPortIfIndex": staLoopbackDetectionPortIfIndex,
       "staLoopbackDetectionPortStatus": staLoopbackDetectionPortStatus,
       "staLoopbackDetectionPortTrapStatus": staLoopbackDetectionPortTrapStatus,
       "staLoopbackDetectionPortReleaseMode": staLoopbackDetectionPortReleaseMode,
       "staLoopbackDetectionPortRelease": staLoopbackDetectionPortRelease,
       "staLoopbackDetectionPortShutdownInterval": staLoopbackDetectionPortShutdownInterval,
       "staSystemBPDUFlooding": staSystemBPDUFlooding,
       "staCiscoPrestandardCompatibility": staCiscoPrestandardCompatibility,
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
       "rspanTable": rspanTable,
       "rspanEntry": rspanEntry,
       "rspanSessionId": rspanSessionId,
       "rspanSrcTxPorts": rspanSrcTxPorts,
       "rspanSrcRxPorts": rspanSrcRxPorts,
       "rspanDstPort": rspanDstPort,
       "rspanDstPortTag": rspanDstPortTag,
       "rspanSwitchRole": rspanSwitchRole,
       "rspanRemotePorts": rspanRemotePorts,
       "rspanRemoteVlanId": rspanRemoteVlanId,
       "rspanOperStatus": rspanOperStatus,
       "rspanStatus": rspanStatus,
       "igmpSnoopMgt": igmpSnoopMgt,
       "igmpSnoopStatus": igmpSnoopStatus,
       "igmpSnoopQuerier": igmpSnoopQuerier,
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
       "igmpSnoopMulticastStaticTable": igmpSnoopMulticastStaticTable,
       "igmpSnoopMulticastStaticEntry": igmpSnoopMulticastStaticEntry,
       "igmpSnoopMulticastStaticVlanIndex": igmpSnoopMulticastStaticVlanIndex,
       "igmpSnoopMulticastStaticIpAddress": igmpSnoopMulticastStaticIpAddress,
       "igmpSnoopMulticastStaticPorts": igmpSnoopMulticastStaticPorts,
       "igmpSnoopMulticastStaticStatus": igmpSnoopMulticastStaticStatus,
       "igmpSnoopCurrentVlanTable": igmpSnoopCurrentVlanTable,
       "igmpSnoopCurrentVlanEntry": igmpSnoopCurrentVlanEntry,
       "igmpSnoopCurrentVlanIndex": igmpSnoopCurrentVlanIndex,
       "igmpSnoopCurrentVlanStatus": igmpSnoopCurrentVlanStatus,
       "igmpSnoopCurrentVlanImmediateLeave": igmpSnoopCurrentVlanImmediateLeave,
       "igmpSnoopCurrentVlanGeneralQuerySuppression": igmpSnoopCurrentVlanGeneralQuerySuppression,
       "igmpSnoopCurrentVlanLastMemQueryCount": igmpSnoopCurrentVlanLastMemQueryCount,
       "igmpSnoopCurrentVlanLastMemQueryIntvl": igmpSnoopCurrentVlanLastMemQueryIntvl,
       "igmpSnoopCurrentVlanProxyAddress": igmpSnoopCurrentVlanProxyAddress,
       "igmpSnoopCurrentVlanQueryIntvl": igmpSnoopCurrentVlanQueryIntvl,
       "igmpSnoopCurrentVlanQueryRespIntvl": igmpSnoopCurrentVlanQueryRespIntvl,
       "igmpSnoopCurrentVlanProxyReporting": igmpSnoopCurrentVlanProxyReporting,
       "igmpSnoopCurrentVlanVersion": igmpSnoopCurrentVlanVersion,
       "igmpSnoopCurrentVlanVersionExclusive": igmpSnoopCurrentVlanVersionExclusive,
       "igmpSnoopCurrentVlanImmediateLeaveByHostIp": igmpSnoopCurrentVlanImmediateLeaveByHostIp,
       "igmpSnoopMulticastGroupTable": igmpSnoopMulticastGroupTable,
       "igmpSnoopMulticastGroupEntry": igmpSnoopMulticastGroupEntry,
       "igmpSnoopMulticastGroupVlanIndex": igmpSnoopMulticastGroupVlanIndex,
       "igmpSnoopMulticastGroupIpAddress": igmpSnoopMulticastGroupIpAddress,
       "igmpSnoopMulticastGroupSourceIPAddress": igmpSnoopMulticastGroupSourceIPAddress,
       "igmpSnoopMulticastGroupPorts": igmpSnoopMulticastGroupPorts,
       "igmpSnoopMulticastGroupStatus": igmpSnoopMulticastGroupStatus,
       "igmpSnoopMulticastGroupPortCount": igmpSnoopMulticastGroupPortCount,
       "igmpSnoopFilterStatus": igmpSnoopFilterStatus,
       "igmpSnoopProfileTable": igmpSnoopProfileTable,
       "igmpSnoopProfileEntry": igmpSnoopProfileEntry,
       "igmpSnoopProfileId": igmpSnoopProfileId,
       "igmpSnoopProfileAction": igmpSnoopProfileAction,
       "igmpSnoopProfileStatus": igmpSnoopProfileStatus,
       "igmpSnoopProfileCtl": igmpSnoopProfileCtl,
       "igmpSnoopProfileCtlId": igmpSnoopProfileCtlId,
       "igmpSnoopProfileCtlInetAddressType": igmpSnoopProfileCtlInetAddressType,
       "igmpSnoopProfileCtlStartInetAddress": igmpSnoopProfileCtlStartInetAddress,
       "igmpSnoopProfileCtlEndInetAddress": igmpSnoopProfileCtlEndInetAddress,
       "igmpSnoopProfileCtlAction": igmpSnoopProfileCtlAction,
       "igmpSnoopProfileRangeTable": igmpSnoopProfileRangeTable,
       "igmpSnoopProfileRangeEntry": igmpSnoopProfileRangeEntry,
       "igmpSnoopProfileRangeProfileId": igmpSnoopProfileRangeProfileId,
       "igmpSnoopProfileRangeInetAddressType": igmpSnoopProfileRangeInetAddressType,
       "igmpSnoopProfileRangeStartInetAddress": igmpSnoopProfileRangeStartInetAddress,
       "igmpSnoopProfileRangeEndInetAddress": igmpSnoopProfileRangeEndInetAddress,
       "igmpSnoopProfileRangeAction": igmpSnoopProfileRangeAction,
       "igmpSnoopFilterPortTable": igmpSnoopFilterPortTable,
       "igmpSnoopFilterPortEntry": igmpSnoopFilterPortEntry,
       "igmpSnoopFilterPortIndex": igmpSnoopFilterPortIndex,
       "igmpSnoopFilterPortProfileId": igmpSnoopFilterPortProfileId,
       "igmpSnoopThrottlePortTable": igmpSnoopThrottlePortTable,
       "igmpSnoopThrottlePortEntry": igmpSnoopThrottlePortEntry,
       "igmpSnoopThrottlePortIndex": igmpSnoopThrottlePortIndex,
       "igmpSnoopThrottlePortRunningStatus": igmpSnoopThrottlePortRunningStatus,
       "igmpSnoopThrottlePortAction": igmpSnoopThrottlePortAction,
       "igmpSnoopThrottlePortMaxGroups": igmpSnoopThrottlePortMaxGroups,
       "igmpSnoopThrottlePortCurrentGroups": igmpSnoopThrottlePortCurrentGroups,
       "igmpSnoopPortTable": igmpSnoopPortTable,
       "igmpSnoopPortEntry": igmpSnoopPortEntry,
       "igmpSnoopPortIndex": igmpSnoopPortIndex,
       "igmpSnoopQueryDrop": igmpSnoopQueryDrop,
       "igmpSnoopMulticastDataDrop": igmpSnoopMulticastDataDrop,
       "igmpSnoopPortNumGroups": igmpSnoopPortNumGroups,
       "igmpSnoopPortNumJoinSend": igmpSnoopPortNumJoinSend,
       "igmpSnoopPortNumJoins": igmpSnoopPortNumJoins,
       "igmpSnoopPortNumJoinSuccess": igmpSnoopPortNumJoinSuccess,
       "igmpSnoopPortNumLeavesSend": igmpSnoopPortNumLeavesSend,
       "igmpSnoopPortNumLeaves": igmpSnoopPortNumLeaves,
       "igmpSnoopPortNumGeneralQuerySend": igmpSnoopPortNumGeneralQuerySend,
       "igmpSnoopPortNumGeneralQueryRecevied": igmpSnoopPortNumGeneralQueryRecevied,
       "igmpSnoopPortNumSepcificQuerySend": igmpSnoopPortNumSepcificQuerySend,
       "igmpSnoopPortNumSpecificQueryReceived": igmpSnoopPortNumSpecificQueryReceived,
       "igmpSnoopPortNumInvalidReport": igmpSnoopPortNumInvalidReport,
       "igmpSnoopPortClearStatistics": igmpSnoopPortClearStatistics,
       "igmpSnoopGlobalMgt": igmpSnoopGlobalMgt,
       "igmpSnoopProxyReporting": igmpSnoopProxyReporting,
       "igmpSnoopRouterAlertOptionCheck": igmpSnoopRouterAlertOptionCheck,
       "igmpSnoopTcnFlood": igmpSnoopTcnFlood,
       "igmpSnoopTcnQuerySolicit": igmpSnoopTcnQuerySolicit,
       "igmpSnoopUnregisteredDataFlood": igmpSnoopUnregisteredDataFlood,
       "igmpSnoopUnsolicitedReportInterval": igmpSnoopUnsolicitedReportInterval,
       "igmpSnoopVersionExclusive": igmpSnoopVersionExclusive,
       "igmpSnoopMrouterForwardMode": igmpSnoopMrouterForwardMode,
       "igmpSnoopForwardingPriority": igmpSnoopForwardingPriority,
       "igmpSnoopQueryDropTable": igmpSnoopQueryDropTable,
       "igmpSnoopQueryDropEntry": igmpSnoopQueryDropEntry,
       "igmpSnoopQueryDropPortIndex": igmpSnoopQueryDropPortIndex,
       "igmpSnoopQueryDropVlanBitmap": igmpSnoopQueryDropVlanBitmap,
       "igmpSnoopClearDynamicGroups": igmpSnoopClearDynamicGroups,
       "igmpSnoopVlanTable": igmpSnoopVlanTable,
       "igmpSnoopVlanEntry": igmpSnoopVlanEntry,
       "igmpSnoopVlanIndex": igmpSnoopVlanIndex,
       "igmpSnoopVlanNumGroups": igmpSnoopVlanNumGroups,
       "igmpSnoopVlanNumJoinSend": igmpSnoopVlanNumJoinSend,
       "igmpSnoopVlanNumJoins": igmpSnoopVlanNumJoins,
       "igmpSnoopVlanNumJoinSuccess": igmpSnoopVlanNumJoinSuccess,
       "igmpSnoopVlanNumLeavesSend": igmpSnoopVlanNumLeavesSend,
       "igmpSnoopVlanNumLeaves": igmpSnoopVlanNumLeaves,
       "igmpSnoopVlanNumGeneralQuerySend": igmpSnoopVlanNumGeneralQuerySend,
       "igmpSnoopVlanNumGeneralQueryRecevied": igmpSnoopVlanNumGeneralQueryRecevied,
       "igmpSnoopVlanNumSepcificQuerySend": igmpSnoopVlanNumSepcificQuerySend,
       "igmpSnoopVlanNumSpecificQueryReceived": igmpSnoopVlanNumSpecificQueryReceived,
       "igmpSnoopVlanNumInvalidReport": igmpSnoopVlanNumInvalidReport,
       "igmpSnoopVlanClearStatistics": igmpSnoopVlanClearStatistics,
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
       "dhcpMgt": dhcpMgt,
       "dhcpClient": dhcpClient,
       "dhcpcOptions": dhcpcOptions,
       "dhcpcInterfaceTable": dhcpcInterfaceTable,
       "dhcpcInterfaceEntry": dhcpcInterfaceEntry,
       "dhcpcIfIndex": dhcpcIfIndex,
       "dhcpcIfVendorClassIdMode": dhcpcIfVendorClassIdMode,
       "dhcpcIfVendorClassId": dhcpcIfVendorClassId,
       "dhcpRelay": dhcpRelay,
       "dhcpRelayRestart": dhcpRelayRestart,
       "dhcpRelayServerInetAddrTable": dhcpRelayServerInetAddrTable,
       "dhcpRelayServerInetAddrEntry": dhcpRelayServerInetAddrEntry,
       "dhcpRelayServerInetAddrIfIndex": dhcpRelayServerInetAddrIfIndex,
       "dhcpRelayServerInetAddrIndex": dhcpRelayServerInetAddrIndex,
       "dhcpRelayServerInetAddressType": dhcpRelayServerInetAddressType,
       "dhcpRelayServerInetAddress": dhcpRelayServerInetAddress,
       "dhcpOption82": dhcpOption82,
       "dhcpOption82Status": dhcpOption82Status,
       "dhcpOption82Policy": dhcpOption82Policy,
       "dhcpOption82RemoteIDMode": dhcpOption82RemoteIDMode,
       "dhcpOption82RemoteIDString": dhcpOption82RemoteIDString,
       "dhcpOption82EncodeFormat": dhcpOption82EncodeFormat,
       "dhcpOption82RelayServerAddrTable": dhcpOption82RelayServerAddrTable,
       "dhcpOption82RelayServerAddrEntry": dhcpOption82RelayServerAddrEntry,
       "dhcpOption82RelayServerAddrIndex": dhcpOption82RelayServerAddrIndex,
       "dhcpOption82RelayServerAddrServerIp": dhcpOption82RelayServerAddrServerIp,
       "pingMgt": pingMgt,
       "pingIpAddress": pingIpAddress,
       "pingPacketSize": pingPacketSize,
       "pingCompleted": pingCompleted,
       "pingAction": pingAction,
       "pingProbeCount": pingProbeCount,
       "pingSentPackets": pingSentPackets,
       "pingReceivedPackets": pingReceivedPackets,
       "pingPacketLossRate": pingPacketLossRate,
       "pingHistoryTable": pingHistoryTable,
       "pingHistoryEntry": pingHistoryEntry,
       "pingHistoryIndex": pingHistoryIndex,
       "pingHistoryResponse": pingHistoryResponse,
       "arpCacheDeleteAll": arpCacheDeleteAll,
       "vlanMgt": vlanMgt,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanAddressMethod": vlanAddressMethod,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortIndex": vlanPortIndex,
       "vlanPortMode": vlanPortMode,
       "vlanPortPrivateVlanType": vlanPortPrivateVlanType,
       "voiceVlanMgt": voiceVlanMgt,
       "voiceVlanOuiTable": voiceVlanOuiTable,
       "voiceVlanOuiEntry": voiceVlanOuiEntry,
       "voiceVlanOuiAddress": voiceVlanOuiAddress,
       "voiceVlanOuiMask": voiceVlanOuiMask,
       "voiceVlanOuiDescription": voiceVlanOuiDescription,
       "voiceVlanOuiStatus": voiceVlanOuiStatus,
       "voiceVlanEnabledId": voiceVlanEnabledId,
       "voiceVlanAgingTime": voiceVlanAgingTime,
       "voiceVlanPortTable": voiceVlanPortTable,
       "voiceVlanPortEntry": voiceVlanPortEntry,
       "voiceVlanPortIfIndex": voiceVlanPortIfIndex,
       "voiceVlanPortMode": voiceVlanPortMode,
       "voiceVlanPortSecurity": voiceVlanPortSecurity,
       "voiceVlanPortPriority": voiceVlanPortPriority,
       "voiceVlanPortRuleOui": voiceVlanPortRuleOui,
       "voiceVlanPortRuleLldp": voiceVlanPortRuleLldp,
       "voiceVlanPortRemainAge": voiceVlanPortRemainAge,
       "dot1vProtocolExPortTable": dot1vProtocolExPortTable,
       "dot1vProtocolExPortEntry": dot1vProtocolExPortEntry,
       "dot1vProtocolExPortGroupPriority": dot1vProtocolExPortGroupPriority,
       "macVlanTable": macVlanTable,
       "macVlanEntry": macVlanEntry,
       "macVlanMacAddress": macVlanMacAddress,
       "macVlanId": macVlanId,
       "macVlanPriority": macVlanPriority,
       "macVlanStatus": macVlanStatus,
       "macVlanMacMask": macVlanMacMask,
       "macVlanClearAction": macVlanClearAction,
       "subnetVlanTable": subnetVlanTable,
       "subnetVlanEntry": subnetVlanEntry,
       "subnetVlanIpAddress": subnetVlanIpAddress,
       "subnetVlanMask": subnetVlanMask,
       "subnetVlanId": subnetVlanId,
       "subnetVlanPriority": subnetVlanPriority,
       "subnetVlanStatus": subnetVlanStatus,
       "subnetVlanClearAction": subnetVlanClearAction,
       "vlanStaticExtTable": vlanStaticExtTable,
       "vlanStaticExtEntry": vlanStaticExtEntry,
       "vlanStaticExtRspanStatus": vlanStaticExtRspanStatus,
       "vlanStaticTable": vlanStaticTable,
       "vlanStaticEntry": vlanStaticEntry,
       "vlanStaticIndex": vlanStaticIndex,
       "vlanStaticInterfaceType": vlanStaticInterfaceType,
       "priorityMgt": priorityMgt,
       "prioWrrPortTable": prioWrrPortTable,
       "prioWrrPortEntry": prioWrrPortEntry,
       "prioWrrPortIfIndex": prioWrrPortIfIndex,
       "prioWrrPortTrafficClass": prioWrrPortTrafficClass,
       "prioWrrPortWeight": prioWrrPortWeight,
       "prioWrrPortStrictStatus": prioWrrPortStrictStatus,
       "prioSchedModePortTable": prioSchedModePortTable,
       "prioSchedModePortEntry": prioSchedModePortEntry,
       "prioSchedModePortIndex": prioSchedModePortIndex,
       "prioSchedModePort": prioSchedModePort,
       "trapDestMgt": trapDestMgt,
       "trapVar": trapVar,
       "trapIpFilterRejectMode": trapIpFilterRejectMode,
       "trapIpFilterRejectIp": trapIpFilterRejectIp,
       "trapVarMacAddr": trapVarMacAddr,
       "trapVarLoginUserName": trapVarLoginUserName,
       "trapVarSessionType": trapVarSessionType,
       "trapVarLoginInetAddressType": trapVarLoginInetAddressType,
       "trapVarLoginInetAddress": trapVarLoginInetAddress,
       "trapIpFilterRejectInetAddressType": trapIpFilterRejectInetAddressType,
       "trapIpFilterRejectInetAddress": trapIpFilterRejectInetAddress,
       "trapAutoUpgradeResult": trapAutoUpgradeResult,
       "trapAutoUpgradeNewVer": trapAutoUpgradeNewVer,
       "trapIfIndex": trapIfIndex,
       "trapVlanId": trapVlanId,
       "trapDhcpClientPortIfIndex": trapDhcpClientPortIfIndex,
       "trapDhcpServerIpAddress": trapDhcpServerIpAddress,
       "trapSfpThresholdAlarmWarnIfIndex": trapSfpThresholdAlarmWarnIfIndex,
       "trapSfpThresholdAlarmWarnType": trapSfpThresholdAlarmWarnType,
       "trapUdldPortShutdownReason": trapUdldPortShutdownReason,
       "trapDhcpServerMacAddress": trapDhcpServerMacAddress,
       "trapMacNotifyAction": trapMacNotifyAction,
       "qosMgt": qosMgt,
       "rateLimitMgt": rateLimitMgt,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rlPortIndex": rlPortIndex,
       "rlPortInputStatus": rlPortInputStatus,
       "rlPortOutputStatus": rlPortOutputStatus,
       "rlPortInputLimitInKilo": rlPortInputLimitInKilo,
       "rlPortOutputLimitInKilo": rlPortOutputLimitInKilo,
       "rlPortLimitInKiloResolution": rlPortLimitInKiloResolution,
       "cosMgt": cosMgt,
       "prioIfClassificationModeTable": prioIfClassificationModeTable,
       "prioIfClassificationModeEntry": prioIfClassificationModeEntry,
       "prioIfClassificationModeIf": prioIfClassificationModeIf,
       "prioIfClassificationModeStatus": prioIfClassificationModeStatus,
       "prioCosToDscpTable": prioCosToDscpTable,
       "prioCosToDscpEntry": prioCosToDscpEntry,
       "prioCosToDscpIfValue": prioCosToDscpIfValue,
       "prioCosToDscpCosValue": prioCosToDscpCosValue,
       "prioCosToDscpCFIValue": prioCosToDscpCFIValue,
       "prioCosToDscpPhbValue": prioCosToDscpPhbValue,
       "prioDscpToDscpTable": prioDscpToDscpTable,
       "prioDscpToDscpEntry": prioDscpToDscpEntry,
       "prioDscpToDscpIfValue": prioDscpToDscpIfValue,
       "prioDscpToDscpIngressDscpValue": prioDscpToDscpIngressDscpValue,
       "prioDscpToDscpPhbValue": prioDscpToDscpPhbValue,
       "diffServMgt": diffServMgt,
       "diffServPolicyMapTable": diffServPolicyMapTable,
       "diffServPolicyMapEntry": diffServPolicyMapEntry,
       "diffServPolicyMapIndex": diffServPolicyMapIndex,
       "diffServPolicyMapName": diffServPolicyMapName,
       "diffServPolicyMapDescription": diffServPolicyMapDescription,
       "diffServPolicyMapElementIndexList": diffServPolicyMapElementIndexList,
       "diffServPolicyMapStatus": diffServPolicyMapStatus,
       "diffServPolicyMapAttachCtl": diffServPolicyMapAttachCtl,
       "diffServPolicyMapAttachCtlIndex": diffServPolicyMapAttachCtlIndex,
       "diffServPolicyMapAttachCtlElementIndex": diffServPolicyMapAttachCtlElementIndex,
       "diffServPolicyMapAttachCtlAction": diffServPolicyMapAttachCtlAction,
       "diffServPolicyMapElementTable": diffServPolicyMapElementTable,
       "diffServPolicyMapElementEntry": diffServPolicyMapElementEntry,
       "diffServPolicyMapElementIndex": diffServPolicyMapElementIndex,
       "diffServPolicyMapElementClassMapIndex": diffServPolicyMapElementClassMapIndex,
       "diffServPolicyMapElementMeterIndex": diffServPolicyMapElementMeterIndex,
       "diffServPolicyMapElementActionIndex": diffServPolicyMapElementActionIndex,
       "diffServPolicyMapElementStatus": diffServPolicyMapElementStatus,
       "diffServClassMapTable": diffServClassMapTable,
       "diffServClassMapEntry": diffServClassMapEntry,
       "diffServClassMapIndex": diffServClassMapIndex,
       "diffServClassMapName": diffServClassMapName,
       "diffServClassMapDescription": diffServClassMapDescription,
       "diffServClassMapMatchType": diffServClassMapMatchType,
       "diffServClassMapElementIndexTypeList": diffServClassMapElementIndexTypeList,
       "diffServClassMapElementIndexList": diffServClassMapElementIndexList,
       "diffServClassMapStatus": diffServClassMapStatus,
       "diffServClassMapAttachCtl": diffServClassMapAttachCtl,
       "diffServClassMapAttachCtlIndex": diffServClassMapAttachCtlIndex,
       "diffServClassMapAttachCtlElementIndexType": diffServClassMapAttachCtlElementIndexType,
       "diffServClassMapAttachCtlElementIndex": diffServClassMapAttachCtlElementIndex,
       "diffServClassMapAttachCtlAction": diffServClassMapAttachCtlAction,
       "diffServAclTable": diffServAclTable,
       "diffServAclEntry": diffServAclEntry,
       "diffServAclIndex": diffServAclIndex,
       "diffServAclName": diffServAclName,
       "diffServAclType": diffServAclType,
       "diffServAclAceIndexList": diffServAclAceIndexList,
       "diffServAclStatus": diffServAclStatus,
       "diffServAclAttachCtl": diffServAclAttachCtl,
       "diffServAclAttachCtlIndex": diffServAclAttachCtlIndex,
       "diffServAclAttachCtlAceType": diffServAclAttachCtlAceType,
       "diffServAclAttachCtlAceIndex": diffServAclAttachCtlAceIndex,
       "diffServAclAttachCtlAction": diffServAclAttachCtlAction,
       "diffServIpAceTable": diffServIpAceTable,
       "diffServIpAceEntry": diffServIpAceEntry,
       "diffServIpAceIndex": diffServIpAceIndex,
       "diffServIpAceType": diffServIpAceType,
       "diffServIpAceAccess": diffServIpAceAccess,
       "diffServIpAceSourceIpAddr": diffServIpAceSourceIpAddr,
       "diffServIpAceSourceIpAddrBitmask": diffServIpAceSourceIpAddrBitmask,
       "diffServIpAceDestIpAddr": diffServIpAceDestIpAddr,
       "diffServIpAceDestIpAddrBitmask": diffServIpAceDestIpAddrBitmask,
       "diffServIpAceProtocol": diffServIpAceProtocol,
       "diffServIpAcePrec": diffServIpAcePrec,
       "diffServIpAceDscp": diffServIpAceDscp,
       "diffServIpAceSourcePortOp": diffServIpAceSourcePortOp,
       "diffServIpAceMinSourcePort": diffServIpAceMinSourcePort,
       "diffServIpAceSourcePortBitmask": diffServIpAceSourcePortBitmask,
       "diffServIpAceDestPortOp": diffServIpAceDestPortOp,
       "diffServIpAceMinDestPort": diffServIpAceMinDestPort,
       "diffServIpAceDestPortBitmask": diffServIpAceDestPortBitmask,
       "diffServIpAceControlCode": diffServIpAceControlCode,
       "diffServIpAceControlCodeBitmask": diffServIpAceControlCodeBitmask,
       "diffServIpAceStatus": diffServIpAceStatus,
       "diffServMacAceTable": diffServMacAceTable,
       "diffServMacAceEntry": diffServMacAceEntry,
       "diffServMacAceIndex": diffServMacAceIndex,
       "diffServMacAceAccess": diffServMacAceAccess,
       "diffServMacAcePktformat": diffServMacAcePktformat,
       "diffServMacAceSourceMacAddr": diffServMacAceSourceMacAddr,
       "diffServMacAceSourceMacAddrBitmask": diffServMacAceSourceMacAddrBitmask,
       "diffServMacAceDestMacAddr": diffServMacAceDestMacAddr,
       "diffServMacAceDestMacAddrBitmask": diffServMacAceDestMacAddrBitmask,
       "diffServMacAceVidOp": diffServMacAceVidOp,
       "diffServMacAceMinVid": diffServMacAceMinVid,
       "diffServMacAceVidBitmask": diffServMacAceVidBitmask,
       "diffServMacAceEtherTypeOp": diffServMacAceEtherTypeOp,
       "diffServMacAceEtherTypeBitmask": diffServMacAceEtherTypeBitmask,
       "diffServMacAceMinEtherType": diffServMacAceMinEtherType,
       "diffServMacAceStatus": diffServMacAceStatus,
       "diffServMacAceCosOp": diffServMacAceCosOp,
       "diffServMacAceCosBitmask": diffServMacAceCosBitmask,
       "diffServMacAceMinCos": diffServMacAceMinCos,
       "diffServActionTable": diffServActionTable,
       "diffServActionEntry": diffServActionEntry,
       "diffServActionIndex": diffServActionIndex,
       "diffServActionList": diffServActionList,
       "diffServActionPktNewPri": diffServActionPktNewPri,
       "diffServActionPktNewPhb": diffServActionPktNewPhb,
       "diffServActionStatus": diffServActionStatus,
       "diffServActionPktNewDscp": diffServActionPktNewDscp,
       "diffServMeterTable": diffServMeterTable,
       "diffServMeterEntry": diffServMeterEntry,
       "diffServMeterIndex": diffServMeterIndex,
       "diffServMeterModel": diffServMeterModel,
       "diffServMeterRate": diffServMeterRate,
       "diffServMeterStatus": diffServMeterStatus,
       "diffServIpv6AceTable": diffServIpv6AceTable,
       "diffServIpv6AceEntry": diffServIpv6AceEntry,
       "diffServIpv6AceIndex": diffServIpv6AceIndex,
       "diffServIpv6AceType": diffServIpv6AceType,
       "diffServIpv6AceAccess": diffServIpv6AceAccess,
       "diffServIpv6AceSourceIpAddr": diffServIpv6AceSourceIpAddr,
       "diffServIpv6AceSourceIpAddrPrefixLen": diffServIpv6AceSourceIpAddrPrefixLen,
       "diffServIpv6AceDestIpAddr": diffServIpv6AceDestIpAddr,
       "diffServIpv6AceDestIpAddrPrefixLen": diffServIpv6AceDestIpAddrPrefixLen,
       "diffServIpv6AceNextHeader": diffServIpv6AceNextHeader,
       "diffServIpv6AceDscp": diffServIpv6AceDscp,
       "diffServIpv6AceStatus": diffServIpv6AceStatus,
       "diffServIpv6AceSourcePortOp": diffServIpv6AceSourcePortOp,
       "diffServIpv6AceSourcePort": diffServIpv6AceSourcePort,
       "diffServIpv6AceSourcePortBitmask": diffServIpv6AceSourcePortBitmask,
       "diffServIpv6AceDestPortOp": diffServIpv6AceDestPortOp,
       "diffServIpv6AceDestPort": diffServIpv6AceDestPort,
       "diffServIpv6AceDestPortBitmask": diffServIpv6AceDestPortBitmask,
       "diffServArpAceTable": diffServArpAceTable,
       "diffServArpAceEntry": diffServArpAceEntry,
       "diffServArpAceIndex": diffServArpAceIndex,
       "diffServArpAceAction": diffServArpAceAction,
       "diffServArpAcePktType": diffServArpAcePktType,
       "diffServArpAceSourceIpAddr": diffServArpAceSourceIpAddr,
       "diffServArpAceSourceIpAddrBitmask": diffServArpAceSourceIpAddrBitmask,
       "diffServArpAceDestIpAddr": diffServArpAceDestIpAddr,
       "diffServArpAceDestIpAddrBitmask": diffServArpAceDestIpAddrBitmask,
       "diffServArpAceSourceMacAddr": diffServArpAceSourceMacAddr,
       "diffServArpAceSourceMacAddrBitmask": diffServArpAceSourceMacAddrBitmask,
       "diffServArpAceDestMacAddr": diffServArpAceDestMacAddr,
       "diffServArpAceDestMacAddrBitmask": diffServArpAceDestMacAddrBitmask,
       "diffServArpAceLogStatus": diffServArpAceLogStatus,
       "diffServArpAceStatus": diffServArpAceStatus,
       "diffServArpTable": diffServArpTable,
       "diffServArpEntry": diffServArpEntry,
       "diffServArpAclName": diffServArpAclName,
       "diffServAclHwCounterTable": diffServAclHwCounterTable,
       "diffServAclHwCounterEntry": diffServAclHwCounterEntry,
       "diffServAclHwCounterIfIndex": diffServAclHwCounterIfIndex,
       "diffServAclHwCounterDirection": diffServAclHwCounterDirection,
       "diffServAclHwCounterAclIndex": diffServAclHwCounterAclIndex,
       "diffServAclHwCounterAceIndex": diffServAclHwCounterAceIndex,
       "diffServAclHwCounterAceHitCount": diffServAclHwCounterAceHitCount,
       "diffServPolicyMapPortTable": diffServPolicyMapPortTable,
       "diffServPolicyMapPortEntry": diffServPolicyMapPortEntry,
       "diffServPolicyMapPortIfIndex": diffServPolicyMapPortIfIndex,
       "diffServPolicyMapPortDirection": diffServPolicyMapPortDirection,
       "diffServPolicyMapPortPolicyMapIndex": diffServPolicyMapPortPolicyMapIndex,
       "diffServPolicyMapPortStatus": diffServPolicyMapPortStatus,
       "diffServAccessGroupTable": diffServAccessGroupTable,
       "diffServAccessGroupEntry": diffServAccessGroupEntry,
       "diffServAccessGroupIfIndex": diffServAccessGroupIfIndex,
       "diffServAccessGroupDirection": diffServAccessGroupDirection,
       "diffServAccessGroupType": diffServAccessGroupType,
       "diffServAccessGroupAclIndex": diffServAccessGroupAclIndex,
       "diffServAccessGroupTimeRangeName": diffServAccessGroupTimeRangeName,
       "diffServAccessGroupCounterStatus": diffServAccessGroupCounterStatus,
       "diffServAccessGroupStatus": diffServAccessGroupStatus,
       "diffServTcamTable": diffServTcamTable,
       "diffServTcamEntry": diffServTcamEntry,
       "diffServTcamUnit": diffServTcamUnit,
       "diffServTcamDevice": diffServTcamDevice,
       "diffServTcamPool": diffServTcamPool,
       "diffServTcamPoolCapability": diffServTcamPoolCapability,
       "diffServTcamTotal": diffServTcamTotal,
       "diffServTcamFree": diffServTcamFree,
       "diffServTcamUsed": diffServTcamUsed,
       "securityMgt": securityMgt,
       "privateVlanMgt": privateVlanMgt,
       "privateVlanStatus": privateVlanStatus,
       "privateVlanUplinkPorts": privateVlanUplinkPorts,
       "privateVlanDownlinkPorts": privateVlanDownlinkPorts,
       "privateVlanVlanTable": privateVlanVlanTable,
       "privateVlanVlanEntry": privateVlanVlanEntry,
       "privateVlanVlanIndex": privateVlanVlanIndex,
       "privateVlanVlanType": privateVlanVlanType,
       "privateVlanAssoicatedPrimaryVlan": privateVlanAssoicatedPrimaryVlan,
       "privateVlanPrivatePortTable": privateVlanPrivatePortTable,
       "privateVlanPrivatePortEntry": privateVlanPrivatePortEntry,
       "privateVlanPrivatePortIfIndex": privateVlanPrivatePortIfIndex,
       "privateVlanPrivatePortSecondaryVlan": privateVlanPrivatePortSecondaryVlan,
       "privateVlanPromPortTable": privateVlanPromPortTable,
       "privateVlanPromPortEntry": privateVlanPromPortEntry,
       "privateVlanPromPortIfIndex": privateVlanPromPortIfIndex,
       "privateVlanPromPortPrimaryVlanId": privateVlanPromPortPrimaryVlanId,
       "privateVlanPromPortSecondaryRemap": privateVlanPromPortSecondaryRemap,
       "privateVlanPromPortSecondaryRemap2k": privateVlanPromPortSecondaryRemap2k,
       "privateVlanPromPortSecondaryRemap3k": privateVlanPromPortSecondaryRemap3k,
       "privateVlanPromPortSecondaryRemap4k": privateVlanPromPortSecondaryRemap4k,
       "privateVlanSessionTable": privateVlanSessionTable,
       "privateVlanSessionEntry": privateVlanSessionEntry,
       "privateVlanSessionId": privateVlanSessionId,
       "privateVlanSessionUplinkPorts": privateVlanSessionUplinkPorts,
       "privateVlanSessionDownlinkPorts": privateVlanSessionDownlinkPorts,
       "privateVlanSessionStatus": privateVlanSessionStatus,
       "privateVlanUplinkToUplink": privateVlanUplinkToUplink,
       "portSecurityMgt": portSecurityMgt,
       "portSecPortTable": portSecPortTable,
       "portSecPortEntry": portSecPortEntry,
       "portSecPortIndex": portSecPortIndex,
       "portSecPortStatus": portSecPortStatus,
       "portSecAction": portSecAction,
       "portSecMaxMacCount": portSecMaxMacCount,
       "portSecMacAsPermanentMgt": portSecMacAsPermanentMgt,
       "portSecMacAsPermanentPortIndex": portSecMacAsPermanentPortIndex,
       "portSecMacAsPermanentAction": portSecMacAsPermanentAction,
       "radiusMgt": radiusMgt,
       "radiusServerGlobalAuthPort": radiusServerGlobalAuthPort,
       "radiusServerGlobalAcctPort": radiusServerGlobalAcctPort,
       "radiusServerGlobalKey": radiusServerGlobalKey,
       "radiusServerGlobalRetransmit": radiusServerGlobalRetransmit,
       "radiusServerGlobalTimeout": radiusServerGlobalTimeout,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusServerIndex": radiusServerIndex,
       "radiusServerAddress": radiusServerAddress,
       "radiusServerAuthPortNumber": radiusServerAuthPortNumber,
       "radiusServerAcctPortNumber": radiusServerAcctPortNumber,
       "radiusServerKey": radiusServerKey,
       "radiusServerRetransmit": radiusServerRetransmit,
       "radiusServerTimeout": radiusServerTimeout,
       "radiusServerStatus": radiusServerStatus,
       "tacacsMgt": tacacsMgt,
       "tacacsPlusServerGlobalPortNumber": tacacsPlusServerGlobalPortNumber,
       "tacacsPlusServerGlobalKey": tacacsPlusServerGlobalKey,
       "tacacsPlusServerTable": tacacsPlusServerTable,
       "tacacsPlusServerEntry": tacacsPlusServerEntry,
       "tacacsPlusServerIndex": tacacsPlusServerIndex,
       "tacacsPlusServerAddress": tacacsPlusServerAddress,
       "tacacsPlusServerPortNumber": tacacsPlusServerPortNumber,
       "tacacsPlusServerKey": tacacsPlusServerKey,
       "tacacsPlusServerStatus": tacacsPlusServerStatus,
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
       "sshConnStatus": sshConnStatus,
       "sshConnUserName": sshConnUserName,
       "sshDisconnect": sshDisconnect,
       "sshConnEncryptionTypeStr": sshConnEncryptionTypeStr,
       "sshKeySize": sshKeySize,
       "sshRsaHostKey1": sshRsaHostKey1,
       "sshRsaHostKey2": sshRsaHostKey2,
       "sshRsaHostKey3": sshRsaHostKey3,
       "sshRsaHostKey4": sshRsaHostKey4,
       "sshRsaHostKey5": sshRsaHostKey5,
       "sshRsaHostKey6": sshRsaHostKey6,
       "sshRsaHostKey7": sshRsaHostKey7,
       "sshRsaHostKey8": sshRsaHostKey8,
       "sshDsaHostKey1": sshDsaHostKey1,
       "sshDsaHostKey2": sshDsaHostKey2,
       "sshDsaHostKey3": sshDsaHostKey3,
       "sshDsaHostKey4": sshDsaHostKey4,
       "sshDsaHostKey5": sshDsaHostKey5,
       "sshDsaHostKey6": sshDsaHostKey6,
       "sshDsaHostKey7": sshDsaHostKey7,
       "sshDsaHostKey8": sshDsaHostKey8,
       "sshHostKeyGenAction": sshHostKeyGenAction,
       "sshHostKeyGenStatus": sshHostKeyGenStatus,
       "sshHostKeySaveAction": sshHostKeySaveAction,
       "sshHostKeySaveStatus": sshHostKeySaveStatus,
       "sshHostKeyDelAction": sshHostKeyDelAction,
       "sshUserTable": sshUserTable,
       "sshUserEntry": sshUserEntry,
       "sshUserName": sshUserName,
       "sshUserRsaKey1": sshUserRsaKey1,
       "sshUserRsaKey2": sshUserRsaKey2,
       "sshUserRsaKey3": sshUserRsaKey3,
       "sshUserRsaKey4": sshUserRsaKey4,
       "sshUserRsaKey5": sshUserRsaKey5,
       "sshUserRsaKey6": sshUserRsaKey6,
       "sshUserRsaKey7": sshUserRsaKey7,
       "sshUserRsaKey8": sshUserRsaKey8,
       "sshUserDsaKey1": sshUserDsaKey1,
       "sshUserDsaKey2": sshUserDsaKey2,
       "sshUserDsaKey3": sshUserDsaKey3,
       "sshUserDsaKey4": sshUserDsaKey4,
       "sshUserDsaKey5": sshUserDsaKey5,
       "sshUserDsaKey6": sshUserDsaKey6,
       "sshUserDsaKey7": sshUserDsaKey7,
       "sshUserDsaKey8": sshUserDsaKey8,
       "sshUserKeyDelAction": sshUserKeyDelAction,
       "sshRsaHostKeySHA1FingerPrint": sshRsaHostKeySHA1FingerPrint,
       "sshRsaHostKeyMD5FingerPrint": sshRsaHostKeyMD5FingerPrint,
       "sshDsaHostKeySHA1FingerPrint": sshDsaHostKeySHA1FingerPrint,
       "sshDsaHostKeyMD5FingerPrint": sshDsaHostKeyMD5FingerPrint,
       "ipFilterMgt": ipFilterMgt,
       "ipFilterSnmpInetTable": ipFilterSnmpInetTable,
       "ipFilterSnmpInetEntry": ipFilterSnmpInetEntry,
       "ipFilterSnmpInetAddressType": ipFilterSnmpInetAddressType,
       "ipFilterSnmpInetAddressStart": ipFilterSnmpInetAddressStart,
       "ipFilterSnmpInetAddressEnd": ipFilterSnmpInetAddressEnd,
       "ipFilterSnmpInetStatus": ipFilterSnmpInetStatus,
       "ipFilterHttpInetTable": ipFilterHttpInetTable,
       "ipFilterHttpInetEntry": ipFilterHttpInetEntry,
       "ipFilterHttpInetAddressType": ipFilterHttpInetAddressType,
       "ipFilterHttpInetAddressStart": ipFilterHttpInetAddressStart,
       "ipFilterHttpInetAddressEnd": ipFilterHttpInetAddressEnd,
       "ipFilterHttpInetStatus": ipFilterHttpInetStatus,
       "ipFilterTelnetInetTable": ipFilterTelnetInetTable,
       "ipFilterTelnetInetEntry": ipFilterTelnetInetEntry,
       "ipFilterTelnetInetAddressType": ipFilterTelnetInetAddressType,
       "ipFilterTelnetInetAddressStart": ipFilterTelnetInetAddressStart,
       "ipFilterTelnetInetAddressEnd": ipFilterTelnetInetAddressEnd,
       "ipFilterTelnetInetStatus": ipFilterTelnetInetStatus,
       "ipFilterAllClientCtl": ipFilterAllClientCtl,
       "ipFilterAllClientCtlInetAddressType": ipFilterAllClientCtlInetAddressType,
       "ipFilterAllClientCtlInetAddressStart": ipFilterAllClientCtlInetAddressStart,
       "ipFilterAllClientCtlInetAddressEnd": ipFilterAllClientCtlInetAddressEnd,
       "ipFilterAllClientCtlAction": ipFilterAllClientCtlAction,
       "userAuthMgt": userAuthMgt,
       "userAuthEnablePassword": userAuthEnablePassword,
       "userAuthMethod": userAuthMethod,
       "userAuthTable": userAuthTable,
       "userAuthEntry": userAuthEntry,
       "userAuthUserName": userAuthUserName,
       "userAuthPassword": userAuthPassword,
       "userAuthPrivilege": userAuthPrivilege,
       "userAuthPublicKey": userAuthPublicKey,
       "userAuthStatus": userAuthStatus,
       "dot1xMgt": dot1xMgt,
       "dot1xAuthConfigExtTable": dot1xAuthConfigExtTable,
       "dot1xAuthConfigExtEntry": dot1xAuthConfigExtEntry,
       "dot1xAuthConfigExtOperMode": dot1xAuthConfigExtOperMode,
       "dot1xAuthConfigExtMultiHostMaxCnt": dot1xAuthConfigExtMultiHostMaxCnt,
       "dot1xAuthConfigExtPortIntrusionAction": dot1xAuthConfigExtPortIntrusionAction,
       "aaaMgt": aaaMgt,
       "aaaMethodTable": aaaMethodTable,
       "aaaMethodEntry": aaaMethodEntry,
       "aaaMethodIndex": aaaMethodIndex,
       "aaaMethodName": aaaMethodName,
       "aaaMethodGroupName": aaaMethodGroupName,
       "aaaMethodMode": aaaMethodMode,
       "aaaMethodStatus": aaaMethodStatus,
       "aaaMethodClientType": aaaMethodClientType,
       "aaaMethodPrivilegeLevel": aaaMethodPrivilegeLevel,
       "aaaRadiusGroupTable": aaaRadiusGroupTable,
       "aaaRadiusGroupEntry": aaaRadiusGroupEntry,
       "aaaRadiusGroupIndex": aaaRadiusGroupIndex,
       "aaaRadiusGroupServerBitMap": aaaRadiusGroupServerBitMap,
       "aaaRadiusGroupName": aaaRadiusGroupName,
       "aaaRadiusGroupStatus": aaaRadiusGroupStatus,
       "aaaTacacsPlusGroupTable": aaaTacacsPlusGroupTable,
       "aaaTacacsPlusGroupEntry": aaaTacacsPlusGroupEntry,
       "aaaTacacsPlusGroupIndex": aaaTacacsPlusGroupIndex,
       "aaaTacacsPlusGroupServerBitMap": aaaTacacsPlusGroupServerBitMap,
       "aaaTacacsPlusGroupName": aaaTacacsPlusGroupName,
       "aaaTacacsPlusGroupStatus": aaaTacacsPlusGroupStatus,
       "aaaUpdate": aaaUpdate,
       "aaaAccountTable": aaaAccountTable,
       "aaaAccountEntry": aaaAccountEntry,
       "aaaAccountIfIndex": aaaAccountIfIndex,
       "aaaAccountMethodName": aaaAccountMethodName,
       "aaaAccountProtocol": aaaAccountProtocol,
       "aaaAccountStatus": aaaAccountStatus,
       "aaaCommandPrivilegesTable": aaaCommandPrivilegesTable,
       "aaaCommandPrivilegesEntry": aaaCommandPrivilegesEntry,
       "aaaCommandPrivilegesLevel": aaaCommandPrivilegesLevel,
       "aaaCommandPrivilegesInterfaceIndex": aaaCommandPrivilegesInterfaceIndex,
       "aaaCommandPrivilegesMethodName": aaaCommandPrivilegesMethodName,
       "aaaAccExecTable": aaaAccExecTable,
       "aaaAccExecEntry": aaaAccExecEntry,
       "aaaAccExecIndex": aaaAccExecIndex,
       "aaaAccExecMethodName": aaaAccExecMethodName,
       "networkAccessMgt": networkAccessMgt,
       "networkAccessPortTable": networkAccessPortTable,
       "networkAccessPortEntry": networkAccessPortEntry,
       "networkAccessPortPortIndex": networkAccessPortPortIndex,
       "networkAccessPortDynamicVlan": networkAccessPortDynamicVlan,
       "networkAccessPortMacFilter": networkAccessPortMacFilter,
       "networkAccessPortGuestVlan": networkAccessPortGuestVlan,
       "networkAccessPortDynamicQos": networkAccessPortDynamicQos,
       "networkAccessClearMacAddressMgt": networkAccessClearMacAddressMgt,
       "networkAccessClearMacAddressAttribute": networkAccessClearMacAddressAttribute,
       "networkAccessClearMacAddressMacAddress": networkAccessClearMacAddressMacAddress,
       "networkAccessClearMacAddressPort": networkAccessClearMacAddressPort,
       "networkAccessClearMacAddressAction": networkAccessClearMacAddressAction,
       "networkAccessMacAddressTable": networkAccessMacAddressTable,
       "networkAccessMacAddressEntry": networkAccessMacAddressEntry,
       "networkAccessMacAddressAddress": networkAccessMacAddressAddress,
       "networkAccessMacAddressPort": networkAccessMacAddressPort,
       "networkAccessMacAddressInetAddressType": networkAccessMacAddressInetAddressType,
       "networkAccessMacAddressRadiusServerInetAddress": networkAccessMacAddressRadiusServerInetAddress,
       "networkAccessMacAddressTime": networkAccessMacAddressTime,
       "networkAccessMacAddressAttribute": networkAccessMacAddressAttribute,
       "networkAccessAging": networkAccessAging,
       "networkAccessMacFilterWithMaskTable": networkAccessMacFilterWithMaskTable,
       "networkAccessMacFilterWithMaskEntry": networkAccessMacFilterWithMaskEntry,
       "networkAccessMacFilterWithMaskID": networkAccessMacFilterWithMaskID,
       "networkAccessMacFilterWithMaskMacAddress": networkAccessMacFilterWithMaskMacAddress,
       "networkAccessMacFilterWithMaskMacAddressMask": networkAccessMacFilterWithMaskMacAddressMask,
       "networkAccessMacFilterWithMaskStatus": networkAccessMacFilterWithMaskStatus,
       "dosMgt": dosMgt,
       "system": system,
       "dosSmurf": dosSmurf,
       "dosSmurfStatus": dosSmurfStatus,
       "dosTcpNullScan": dosTcpNullScan,
       "dosTcpNullScanStatus": dosTcpNullScanStatus,
       "dosTcpSynFinScan": dosTcpSynFinScan,
       "dosTcpSynFinScanStatus": dosTcpSynFinScanStatus,
       "dosTcpXmasScan": dosTcpXmasScan,
       "dosTcpXmasScanStatus": dosTcpXmasScanStatus,
       "dosTcpUdpPortZero": dosTcpUdpPortZero,
       "dosTcpUdpPortZeroStatus": dosTcpUdpPortZeroStatus,
       "sysLogMgt": sysLogMgt,
       "sysLogStatus": sysLogStatus,
       "sysLogHistoryFlashLevel": sysLogHistoryFlashLevel,
       "sysLogHistoryRamLevel": sysLogHistoryRamLevel,
       "remoteLogMgt": remoteLogMgt,
       "remoteLogStatus": remoteLogStatus,
       "remoteLogLevel": remoteLogLevel,
       "remoteLogFacilityType": remoteLogFacilityType,
       "remoteLogServerInetTable": remoteLogServerInetTable,
       "remoteLogServerInetEntry": remoteLogServerInetEntry,
       "remoteLogServerInetAddressType": remoteLogServerInetAddressType,
       "remoteLogServerInetAddress": remoteLogServerInetAddress,
       "remoteLogServerStatus": remoteLogServerStatus,
       "remoteLogServerUdpPort": remoteLogServerUdpPort,
       "smtpMgt": smtpMgt,
       "smtpStatus": smtpStatus,
       "smtpSeverityLevel": smtpSeverityLevel,
       "smtpSourceEMail": smtpSourceEMail,
       "smtpServerIpTable": smtpServerIpTable,
       "smtpServerIpEntry": smtpServerIpEntry,
       "smtpServerIp": smtpServerIp,
       "smtpServerIpStatus": smtpServerIpStatus,
       "smtpDestEMailTable": smtpDestEMailTable,
       "smtpDestEMailEntry": smtpDestEMailEntry,
       "smtpDestEMail": smtpDestEMail,
       "smtpDestEMailStatus": smtpDestEMailStatus,
       "sysLogCommandLogStatus": sysLogCommandLogStatus,
       "lineMgt": lineMgt,
       "consoleMgt": consoleMgt,
       "consoleDataBits": consoleDataBits,
       "consoleParity": consoleParity,
       "consoleBaudRate": consoleBaudRate,
       "consoleStopBits": consoleStopBits,
       "consoleExecTimeout": consoleExecTimeout,
       "consolePasswordThreshold": consolePasswordThreshold,
       "consoleSilentTime": consoleSilentTime,
       "consoleLoginResponseTimeout": consoleLoginResponseTimeout,
       "telnetMgt": telnetMgt,
       "telnetStatus": telnetStatus,
       "telnetPortNumber": telnetPortNumber,
       "vtyMgt": vtyMgt,
       "vtyExecTimeout": vtyExecTimeout,
       "vtyPasswordThreshold": vtyPasswordThreshold,
       "vtyLoginResponseTimeout": vtyLoginResponseTimeout,
       "vtyMaxSession": vtyMaxSession,
       "vtySilentTime": vtySilentTime,
       "sysTimeMgt": sysTimeMgt,
       "sntpMgt": sntpMgt,
       "sntpStatus": sntpStatus,
       "sntpServiceMode": sntpServiceMode,
       "sntpPollInterval": sntpPollInterval,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerIndex": sntpServerIndex,
       "sntpServerInetAddressType": sntpServerInetAddressType,
       "sntpServerInetAddress": sntpServerInetAddress,
       "sntpServerStatus": sntpServerStatus,
       "sysCurrentTime": sysCurrentTime,
       "sysTimeZone": sysTimeZone,
       "sysTimeZoneName": sysTimeZoneName,
       "ntpMgt": ntpMgt,
       "ntpStatus": ntpStatus,
       "ntpServiceMode": ntpServiceMode,
       "ntpPollInterval": ntpPollInterval,
       "ntpAuthenticateStatus": ntpAuthenticateStatus,
       "ntpServerTable": ntpServerTable,
       "ntpServerEntry": ntpServerEntry,
       "ntpServerIpAddress": ntpServerIpAddress,
       "ntpServerVersion": ntpServerVersion,
       "ntpServerKeyId": ntpServerKeyId,
       "ntpServerStatus": ntpServerStatus,
       "ntpAuthKeyTable": ntpAuthKeyTable,
       "ntpAuthKeyEntry": ntpAuthKeyEntry,
       "ntpAuthKeyId": ntpAuthKeyId,
       "ntpAuthKeyWord": ntpAuthKeyWord,
       "ntpAuthKeyStatus": ntpAuthKeyStatus,
       "fileMgt": fileMgt,
       "fileCopyMgt": fileCopyMgt,
       "fileCopySrcOperType": fileCopySrcOperType,
       "fileCopySrcFileName": fileCopySrcFileName,
       "fileCopyDestOperType": fileCopyDestOperType,
       "fileCopyDestFileName": fileCopyDestFileName,
       "fileCopyFileType": fileCopyFileType,
       "fileCopyUnitId": fileCopyUnitId,
       "fileCopyAction": fileCopyAction,
       "fileCopyStatus": fileCopyStatus,
       "fileCopyServerInetAddressType": fileCopyServerInetAddressType,
       "fileCopyServerInetAddress": fileCopyServerInetAddress,
       "fileCopyServerUserName": fileCopyServerUserName,
       "fileCopyServerPassword": fileCopyServerPassword,
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
       "fileAutoDownloadResultTable": fileAutoDownloadResultTable,
       "fileAutoDownloadResultEntry": fileAutoDownloadResultEntry,
       "fileAutoDownloadResultUnitID": fileAutoDownloadResultUnitID,
       "fileAutoDownloadResultAction": fileAutoDownloadResultAction,
       "fileAutoDownloadResultStatus": fileAutoDownloadResultStatus,
       "poeMgt": poeMgt,
       "pethPseMainExtTable": pethPseMainExtTable,
       "pethPseMainExtEntry": pethPseMainExtEntry,
       "pethPseMainExtDllPowerType": pethPseMainExtDllPowerType,
       "pethPseMainExtDllPowerSource": pethPseMainExtDllPowerSource,
       "pethPsePortExtTable": pethPsePortExtTable,
       "pethPsePortExtEntry": pethPsePortExtEntry,
       "pethPsePortExtMirroredDllPdRequestedPowerValue": pethPsePortExtMirroredDllPdRequestedPowerValue,
       "pethPsePortExtDllPseAllocatedPowerValue": pethPsePortExtDllPseAllocatedPowerValue,
       "pethPsePortTimeRange": pethPsePortTimeRange,
       "pethPsePortTimeRangeStatus": pethPsePortTimeRangeStatus,
       "pethPsePortExtMaximumPowerValue": pethPsePortExtMaximumPowerValue,
       "pethPsePortExtUsedPowerValue": pethPsePortExtUsedPowerValue,
       "stormMgt": stormMgt,
       "mcastStormMgt": mcastStormMgt,
       "mcastStormTable": mcastStormTable,
       "mcastStormEntry": mcastStormEntry,
       "mcastStormIfIndex": mcastStormIfIndex,
       "mcastStormStatus": mcastStormStatus,
       "mcastStormPktRate": mcastStormPktRate,
       "mcastStormPktRateResolution": mcastStormPktRateResolution,
       "bcastStormMgt": bcastStormMgt,
       "bcastStormTable": bcastStormTable,
       "bcastStormEntry": bcastStormEntry,
       "bcastStormIfIndex": bcastStormIfIndex,
       "bcastStormStatus": bcastStormStatus,
       "bcastStormPktRate": bcastStormPktRate,
       "bcastStormPktRateResolution": bcastStormPktRateResolution,
       "unknownUcastStormMgt": unknownUcastStormMgt,
       "unknownUcastStormTable": unknownUcastStormTable,
       "unknownUcastStormEntry": unknownUcastStormEntry,
       "unknownUcastStormIfIndex": unknownUcastStormIfIndex,
       "unknownUcastStormStatus": unknownUcastStormStatus,
       "unknownUcastStormPktRate": unknownUcastStormPktRate,
       "unknownUcastStormPktRateResolution": unknownUcastStormPktRateResolution,
       "atcMgt": atcMgt,
       "atcBcastStormTcApplyTime": atcBcastStormTcApplyTime,
       "atcBcastStormTcReleaseTime": atcBcastStormTcReleaseTime,
       "atcBcastStormTable": atcBcastStormTable,
       "atcBcastStormEntry": atcBcastStormEntry,
       "atcBcastStormIfIndex": atcBcastStormIfIndex,
       "atcBcastStormEnable": atcBcastStormEnable,
       "atcBcastStormAutoRelease": atcBcastStormAutoRelease,
       "atcBcastStormSampleType": atcBcastStormSampleType,
       "atcBcastStormCurrentTrafficRate": atcBcastStormCurrentTrafficRate,
       "atcBcastStormAlarmFireThreshold": atcBcastStormAlarmFireThreshold,
       "atcBcastStormAlarmClearThreshold": atcBcastStormAlarmClearThreshold,
       "atcBcastStormTcAction": atcBcastStormTcAction,
       "atcBcastStormAlarmFireTrapStatus": atcBcastStormAlarmFireTrapStatus,
       "atcBcastStormAlarmClearTrapStatus": atcBcastStormAlarmClearTrapStatus,
       "atcBcastStormTcApplyTrapStatus": atcBcastStormTcApplyTrapStatus,
       "atcBcastStormTcReleaseTrapStatus": atcBcastStormTcReleaseTrapStatus,
       "atcMcastStormTcApplyTime": atcMcastStormTcApplyTime,
       "atcMcastStormTcReleaseTime": atcMcastStormTcReleaseTime,
       "atcMcastStormTable": atcMcastStormTable,
       "atcMcastStormEntry": atcMcastStormEntry,
       "atcMcastStormIfIndex": atcMcastStormIfIndex,
       "atcMcastStormEnable": atcMcastStormEnable,
       "atcMcastStormAutoRelease": atcMcastStormAutoRelease,
       "atcMcastStormSampleType": atcMcastStormSampleType,
       "atcMcastStormCurrentTrafficRate": atcMcastStormCurrentTrafficRate,
       "atcMcastStormAlarmFireThreshold": atcMcastStormAlarmFireThreshold,
       "atcMcastStormAlarmClearThreshold": atcMcastStormAlarmClearThreshold,
       "atcMcastStormTcAction": atcMcastStormTcAction,
       "atcMcastStormAlarmFireTrapStatus": atcMcastStormAlarmFireTrapStatus,
       "atcMcastStormAlarmClearTrapStatus": atcMcastStormAlarmClearTrapStatus,
       "atcMcastStormTcApplyTrapStatus": atcMcastStormTcApplyTrapStatus,
       "atcMcastStormTcReleaseTrapStatus": atcMcastStormTcReleaseTrapStatus,
       "sysResourceMgt": sysResourceMgt,
       "cpuStatus": cpuStatus,
       "cpuCurrentUti": cpuCurrentUti,
       "cpuStatMaxUti": cpuStatMaxUti,
       "cpuStatAvgUti": cpuStatAvgUti,
       "cpuPeakTime": cpuPeakTime,
       "cpuPeakDuration": cpuPeakDuration,
       "cpuUtiRisingThreshold": cpuUtiRisingThreshold,
       "cpuUtiFallingThreshold": cpuUtiFallingThreshold,
       "memoryStatus": memoryStatus,
       "memoryTotal": memoryTotal,
       "memoryAllocated": memoryAllocated,
       "memoryFreed": memoryFreed,
       "memoryFreedInPercent": memoryFreedInPercent,
       "memoryUtiRisingThreshold": memoryUtiRisingThreshold,
       "memoryUtiFallingThreshold": memoryUtiFallingThreshold,
       "taskCpuTable": taskCpuTable,
       "taskCpuEntry": taskCpuEntry,
       "taskCpuName": taskCpuName,
       "taskCpuCurrentUti": taskCpuCurrentUti,
       "taskCpuStatMaxUti": taskCpuStatMaxUti,
       "taskCpuStatAvgUti": taskCpuStatAvgUti,
       "cpuGuard": cpuGuard,
       "cpuGuardStatus": cpuGuardStatus,
       "cpuGuardHighWatermark": cpuGuardHighWatermark,
       "cpuGuardLowWatermark": cpuGuardLowWatermark,
       "cpuGuardMaxThreshold": cpuGuardMaxThreshold,
       "cpuGuardMinThreshold": cpuGuardMinThreshold,
       "cpuGuardTrapStatus": cpuGuardTrapStatus,
       "cpuGuardCurrentThreshold": cpuGuardCurrentThreshold,
       "mvrMgt": mvrMgt,
       "mvrForwardingPriority": mvrForwardingPriority,
       "mvrDomainTable": mvrDomainTable,
       "mvrDomainEntry": mvrDomainEntry,
       "mvrDomainId": mvrDomainId,
       "mvrDomainStatus": mvrDomainStatus,
       "mvrDomainRunningStatus": mvrDomainRunningStatus,
       "mvrDomainVlanId": mvrDomainVlanId,
       "mvrDomainUpstreamSourceIp": mvrDomainUpstreamSourceIp,
       "mvrDomainClearDynamicGroups": mvrDomainClearDynamicGroups,
       "mvrDomainPortTable": mvrDomainPortTable,
       "mvrDomainPortEntry": mvrDomainPortEntry,
       "mvrPortDomainId": mvrPortDomainId,
       "mvrDomainIfIndex": mvrDomainIfIndex,
       "mvrDomainPortType": mvrDomainPortType,
       "mvrDomainPortImmediateLeave": mvrDomainPortImmediateLeave,
       "mvrDomainPortActive": mvrDomainPortActive,
       "mvrDomainPortImmediateLeaveByHostIp": mvrDomainPortImmediateLeaveByHostIp,
       "mvrProfileTable": mvrProfileTable,
       "mvrProfileCtlTable": mvrProfileCtlTable,
       "mvrProfileCtlEntry": mvrProfileCtlEntry,
       "mvrProfileCtlId": mvrProfileCtlId,
       "mvrProfileName": mvrProfileName,
       "mvrProfileCtlAction": mvrProfileCtlAction,
       "mvrProfileGroupCtlTable": mvrProfileGroupCtlTable,
       "mvrProfileGroupCtlEntry": mvrProfileGroupCtlEntry,
       "mvrProfileGropuCtlProfileId": mvrProfileGropuCtlProfileId,
       "mvrProfileGroupCtlId": mvrProfileGroupCtlId,
       "mvrProfileGroupStartIPAddress": mvrProfileGroupStartIPAddress,
       "mvrProfileGroupEndIPAddress": mvrProfileGroupEndIPAddress,
       "mvrProfileGroupCtlAction": mvrProfileGroupCtlAction,
       "mvrDomainAssociatedProfileTable": mvrDomainAssociatedProfileTable,
       "mvrDomainAssociatedProfileEntry": mvrDomainAssociatedProfileEntry,
       "mvrProfileDomainId": mvrProfileDomainId,
       "mvrProfileId": mvrProfileId,
       "mvrProfileAction": mvrProfileAction,
       "mvrDomainGroupStaticTable": mvrDomainGroupStaticTable,
       "mvrDomainGroupStaticEntry": mvrDomainGroupStaticEntry,
       "mvrGroupStaticDomainId": mvrGroupStaticDomainId,
       "mvrDomainGroupStaticAddress": mvrDomainGroupStaticAddress,
       "mvrDomainGroupStaticReceiverVlan": mvrDomainGroupStaticReceiverVlan,
       "mvrDomainGroupStaticPorts": mvrDomainGroupStaticPorts,
       "mvrDomainGroupCurrentTable": mvrDomainGroupCurrentTable,
       "mvrDomainGroupCurrentEntry": mvrDomainGroupCurrentEntry,
       "mvrGroupCurrenDomainId": mvrGroupCurrenDomainId,
       "mvrDomainGroupCurrentAddress": mvrDomainGroupCurrentAddress,
       "mvrDomainGroupCurrentReceiverVlan": mvrDomainGroupCurrentReceiverVlan,
       "mvrDomainGroupCurrentPorts": mvrDomainGroupCurrentPorts,
       "mvrProxySwitching": mvrProxySwitching,
       "mvrRobustnessValue": mvrRobustnessValue,
       "mvrProxyQueryInterval": mvrProxyQueryInterval,
       "mvrSourcePortmode": mvrSourcePortmode,
       "mvrPortStatisticsTable": mvrPortStatisticsTable,
       "mvrPortStatisticsEntry": mvrPortStatisticsEntry,
       "mvrPortStatisticsDomainId": mvrPortStatisticsDomainId,
       "mvrPortStatisticsPortIndex": mvrPortStatisticsPortIndex,
       "mvrPortStatisticsNumGroups": mvrPortStatisticsNumGroups,
       "mvrPortStatisticsNumJoinSend": mvrPortStatisticsNumJoinSend,
       "mvrPortStatisticsNumJoins": mvrPortStatisticsNumJoins,
       "mvrPortStatisticsNumJoinSuccess": mvrPortStatisticsNumJoinSuccess,
       "mvrPortStatisticsNumLeavesSend": mvrPortStatisticsNumLeavesSend,
       "mvrPortStatisticsNumLeaves": mvrPortStatisticsNumLeaves,
       "mvrPortStatisticsNumGeneralQuerySend": mvrPortStatisticsNumGeneralQuerySend,
       "mvrPortStatisticsNumGeneralQueryRecevied": mvrPortStatisticsNumGeneralQueryRecevied,
       "mvrPortStatisticsNumSepcificQuerySend": mvrPortStatisticsNumSepcificQuerySend,
       "mvrPortStatisticsNumSpecificQueryReceived": mvrPortStatisticsNumSpecificQueryReceived,
       "mvrPortStatisticsNumInvalidReport": mvrPortStatisticsNumInvalidReport,
       "mvrPortStatisticsClearStatistics": mvrPortStatisticsClearStatistics,
       "mvrVlanStatisticsTable": mvrVlanStatisticsTable,
       "mvrVlanStatisticsEntry": mvrVlanStatisticsEntry,
       "mvrVlanStatisticsDomainId": mvrVlanStatisticsDomainId,
       "mvrVlanStatisticsVlanId": mvrVlanStatisticsVlanId,
       "mvrVlanStatisticsNumGroups": mvrVlanStatisticsNumGroups,
       "mvrVlanStatisticsNumJoinSend": mvrVlanStatisticsNumJoinSend,
       "mvrVlanStatisticsNumJoins": mvrVlanStatisticsNumJoins,
       "mvrVlanStatisticsNumJoinSuccess": mvrVlanStatisticsNumJoinSuccess,
       "mvrVlanStatisticsNumLeavesSend": mvrVlanStatisticsNumLeavesSend,
       "mvrVlanStatisticsNumLeaves": mvrVlanStatisticsNumLeaves,
       "mvrVlanStatisticsNumGeneralQuerySend": mvrVlanStatisticsNumGeneralQuerySend,
       "mvrVlanStatisticsNumGeneralQueryRecevied": mvrVlanStatisticsNumGeneralQueryRecevied,
       "mvrVlanStatisticsNumSepcificQuerySend": mvrVlanStatisticsNumSepcificQuerySend,
       "mvrVlanStatisticsNumSpecificQueryReceived": mvrVlanStatisticsNumSpecificQueryReceived,
       "mvrVlanStatisticsNumInvalidReport": mvrVlanStatisticsNumInvalidReport,
       "mvrVlanStatisticsClearStatistics": mvrVlanStatisticsClearStatistics,
       "dhcpSnoopMgt": dhcpSnoopMgt,
       "dhcpSnoopGlobal": dhcpSnoopGlobal,
       "dhcpSnoopEnable": dhcpSnoopEnable,
       "dhcpSnoopVerifyMacAddressEnable": dhcpSnoopVerifyMacAddressEnable,
       "dhcpSnoopInformationOptionEnable": dhcpSnoopInformationOptionEnable,
       "dhcpSnoopInformationOptionPolicy": dhcpSnoopInformationOptionPolicy,
       "dhcpSnoopBindingsTableCtlAction": dhcpSnoopBindingsTableCtlAction,
       "dhcpSnoopLimitRate": dhcpSnoopLimitRate,
       "dhcpSnoopInformationOptionEncodeFormat": dhcpSnoopInformationOptionEncodeFormat,
       "dhcpSnoopVlan": dhcpSnoopVlan,
       "dhcpSnoopVlanConfigTable": dhcpSnoopVlanConfigTable,
       "dhcpSnoopVlanConfigEntry": dhcpSnoopVlanConfigEntry,
       "dhcpSnoopVlanIndex": dhcpSnoopVlanIndex,
       "dhcpSnoopVlanEnable": dhcpSnoopVlanEnable,
       "dhcpSnoopInterface": dhcpSnoopInterface,
       "dhcpSnoopPortConfigTable": dhcpSnoopPortConfigTable,
       "dhcpSnoopPortConfigEntry": dhcpSnoopPortConfigEntry,
       "dhcpSnoopPortIfIndex": dhcpSnoopPortIfIndex,
       "dhcpSnoopPortTrustEnable": dhcpSnoopPortTrustEnable,
       "dhcpSnoopPortMaxNumber": dhcpSnoopPortMaxNumber,
       "dhcpSnoopBindings": dhcpSnoopBindings,
       "dhcpSnoopBindingsTable": dhcpSnoopBindingsTable,
       "dhcpSnoopBindingsEntry": dhcpSnoopBindingsEntry,
       "dhcpSnoopBindingsVlanIndex": dhcpSnoopBindingsVlanIndex,
       "dhcpSnoopBindingsMacAddress": dhcpSnoopBindingsMacAddress,
       "dhcpSnoopBindingsAddrType": dhcpSnoopBindingsAddrType,
       "dhcpSnoopBindingsEntryType": dhcpSnoopBindingsEntryType,
       "dhcpSnoopBindingsIpAddress": dhcpSnoopBindingsIpAddress,
       "dhcpSnoopBindingsPortIfIndex": dhcpSnoopBindingsPortIfIndex,
       "dhcpSnoopBindingsLeaseTime": dhcpSnoopBindingsLeaseTime,
       "dhcpSnoopStatistics": dhcpSnoopStatistics,
       "dhcpSnoopTotalForwardedPkts": dhcpSnoopTotalForwardedPkts,
       "dhcpSnoopUntrustedPortDroppedPkts": dhcpSnoopUntrustedPortDroppedPkts,
       "ipSrcGuardMgt": ipSrcGuardMgt,
       "ipSrcGuardConfigTable": ipSrcGuardConfigTable,
       "ipSrcGuardConfigEntry": ipSrcGuardConfigEntry,
       "ipSrcGuardPortIfIndex": ipSrcGuardPortIfIndex,
       "ipSrcGuardMode": ipSrcGuardMode,
       "ipSrcGuardAclTable": ipSrcGuardAclTable,
       "ipSrcGuardAclEntry": ipSrcGuardAclEntry,
       "ipSrcGuardAclBindingIpAddress": ipSrcGuardAclBindingIpAddress,
       "ipSrcGuardAclBindingMacAddress": ipSrcGuardAclBindingMacAddress,
       "ipSrcGuardAclBindingEntryType": ipSrcGuardAclBindingEntryType,
       "ipSrcGuardAclBindingVlanIndex": ipSrcGuardAclBindingVlanIndex,
       "ipSrcGuardAclBindingPortIfIndex": ipSrcGuardAclBindingPortIfIndex,
       "ipSrcGuardAclBindingStatus": ipSrcGuardAclBindingStatus,
       "mldSnoopMgt": mldSnoopMgt,
       "mldSnoopStatus": mldSnoopStatus,
       "mldSnoopQuerier": mldSnoopQuerier,
       "mldSnoopRobustness": mldSnoopRobustness,
       "mldSnoopQueryInterval": mldSnoopQueryInterval,
       "mldSnoopQueryMaxResponseTime": mldSnoopQueryMaxResponseTime,
       "mldSnoopRouterPortExpireTime": mldSnoopRouterPortExpireTime,
       "mldSnoopVersion": mldSnoopVersion,
       "mldSnoopUnknownMcastMode": mldSnoopUnknownMcastMode,
       "mldSnoopRouterCurrentTable": mldSnoopRouterCurrentTable,
       "mldSnoopRouterCurrentEntry": mldSnoopRouterCurrentEntry,
       "mldSnoopRouterCurrentVlanIndex": mldSnoopRouterCurrentVlanIndex,
       "mldSnoopRouterCurrentPorts": mldSnoopRouterCurrentPorts,
       "mldSnoopRouterStaticTable": mldSnoopRouterStaticTable,
       "mldSnoopRouterStaticEntry": mldSnoopRouterStaticEntry,
       "mldSnoopRouterStaticVlanIndex": mldSnoopRouterStaticVlanIndex,
       "mldSnoopRouterStaticPorts": mldSnoopRouterStaticPorts,
       "mldSnoopRouterStaticStatus": mldSnoopRouterStaticStatus,
       "mldSnoopMulticastCurrentTable": mldSnoopMulticastCurrentTable,
       "mldSnoopMulticastCurrentEntry": mldSnoopMulticastCurrentEntry,
       "mldSnoopMulticastCurrentVlanIndex": mldSnoopMulticastCurrentVlanIndex,
       "mldSnoopMulticastCurrentIpAddress": mldSnoopMulticastCurrentIpAddress,
       "mldSnoopMulticastCurrentSourceIpAddress": mldSnoopMulticastCurrentSourceIpAddress,
       "mldSnoopMulticastCurrentPorts": mldSnoopMulticastCurrentPorts,
       "mldSnoopMulticastStaticTable": mldSnoopMulticastStaticTable,
       "mldSnoopMulticastStaticEntry": mldSnoopMulticastStaticEntry,
       "mldSnoopMulticastStaticVlanIndex": mldSnoopMulticastStaticVlanIndex,
       "mldSnoopMulticastStaticIpAddress": mldSnoopMulticastStaticIpAddress,
       "mldSnoopMulticastStaticPorts": mldSnoopMulticastStaticPorts,
       "mldSnoopMulticastStaticStatus": mldSnoopMulticastStaticStatus,
       "mldSnoopCurrentVlanTable": mldSnoopCurrentVlanTable,
       "mldSnoopCurrentVlanEntry": mldSnoopCurrentVlanEntry,
       "mldSnoopCurrentVlanIndex": mldSnoopCurrentVlanIndex,
       "mldSnoopCurrentVlanImmediateLeave": mldSnoopCurrentVlanImmediateLeave,
       "mldSnoopCurrentVlanImmediateLeaveByHostIp": mldSnoopCurrentVlanImmediateLeaveByHostIp,
       "mldSnoopProxyReporting": mldSnoopProxyReporting,
       "mldSnoopUnsolicitedReportInterval": mldSnoopUnsolicitedReportInterval,
       "mldSnoopPortTable": mldSnoopPortTable,
       "mldSnoopPortEntry": mldSnoopPortEntry,
       "mldSnoopPortIndex": mldSnoopPortIndex,
       "mldSnoopQueryDrop": mldSnoopQueryDrop,
       "mldSnoopMulticastDataDrop": mldSnoopMulticastDataDrop,
       "mldSnoopPortNumGroups": mldSnoopPortNumGroups,
       "mldSnoopPortNumJoinSend": mldSnoopPortNumJoinSend,
       "mldSnoopPortNumJoins": mldSnoopPortNumJoins,
       "mldSnoopPortNumJoinSuccess": mldSnoopPortNumJoinSuccess,
       "mldSnoopPortNumLeavesSend": mldSnoopPortNumLeavesSend,
       "mldSnoopPortNumLeaves": mldSnoopPortNumLeaves,
       "mldSnoopPortNumGeneralQuerySend": mldSnoopPortNumGeneralQuerySend,
       "mldSnoopPortNumGeneralQueryRecevied": mldSnoopPortNumGeneralQueryRecevied,
       "mldSnoopPortNumSepcificQuerySend": mldSnoopPortNumSepcificQuerySend,
       "mldsnoopPortNumSpecificQueryReceived": mldsnoopPortNumSpecificQueryReceived,
       "mldSnoopPortNumInvalidReport": mldSnoopPortNumInvalidReport,
       "mldSnoopPortClearStatistics": mldSnoopPortClearStatistics,
       "mldSnoopFilterStatus": mldSnoopFilterStatus,
       "mldSnoopProfileTable": mldSnoopProfileTable,
       "mldSnoopProfileEntry": mldSnoopProfileEntry,
       "mldSnoopProfileId": mldSnoopProfileId,
       "mldSnoopProfileAction": mldSnoopProfileAction,
       "mldSnoopProfileStatus": mldSnoopProfileStatus,
       "mldSnoopProfileCtl": mldSnoopProfileCtl,
       "mldSnoopProfileCtlId": mldSnoopProfileCtlId,
       "mldSnoopProfileCtlInetAddressType": mldSnoopProfileCtlInetAddressType,
       "mldSnoopProfileCtlStartInetAddress": mldSnoopProfileCtlStartInetAddress,
       "mldSnoopProfileCtlEndInetAddress": mldSnoopProfileCtlEndInetAddress,
       "mldSnoopProfileCtlAction": mldSnoopProfileCtlAction,
       "mldSnoopProfileRangeTable": mldSnoopProfileRangeTable,
       "mldSnoopProfileRangeEntry": mldSnoopProfileRangeEntry,
       "mldSnoopProfileRangeProfileId": mldSnoopProfileRangeProfileId,
       "mldSnoopProfileRangeInetAddressType": mldSnoopProfileRangeInetAddressType,
       "mldSnoopProfileRangeStartInetAddress": mldSnoopProfileRangeStartInetAddress,
       "mldSnoopProfileRangeEndInetAddress": mldSnoopProfileRangeEndInetAddress,
       "mldSnoopProfileRangeAction": mldSnoopProfileRangeAction,
       "mldSnoopFilterPortTable": mldSnoopFilterPortTable,
       "mldSnoopFilterPortEntry": mldSnoopFilterPortEntry,
       "mldSnoopFilterPortIndex": mldSnoopFilterPortIndex,
       "mldSnoopFilterPortProfileId": mldSnoopFilterPortProfileId,
       "mldSnoopThrottlePortTable": mldSnoopThrottlePortTable,
       "mldSnoopThrottlePortEntry": mldSnoopThrottlePortEntry,
       "mldSnoopThrottlePortIndex": mldSnoopThrottlePortIndex,
       "mldSnoopThrottlePortRunningStatus": mldSnoopThrottlePortRunningStatus,
       "mldSnoopThrottlePortAction": mldSnoopThrottlePortAction,
       "mldSnoopThrottlePortMaxGroups": mldSnoopThrottlePortMaxGroups,
       "mldSnoopThrottlePortCurrentGroups": mldSnoopThrottlePortCurrentGroups,
       "mldSnoopClearDynamicGroups": mldSnoopClearDynamicGroups,
       "mldSnoopVlanTable": mldSnoopVlanTable,
       "mldSnoopVlanEntry": mldSnoopVlanEntry,
       "mldSnoopVlanIndex": mldSnoopVlanIndex,
       "mldSnoopVlanNumGroups": mldSnoopVlanNumGroups,
       "mldSnoopVlanNumJoinSend": mldSnoopVlanNumJoinSend,
       "mldSnoopVlanNumJoins": mldSnoopVlanNumJoins,
       "mldSnoopVlanNumJoinSuccess": mldSnoopVlanNumJoinSuccess,
       "mldSnoopVlanNumLeavesSend": mldSnoopVlanNumLeavesSend,
       "mldSnoopVlanNumLeaves": mldSnoopVlanNumLeaves,
       "mldSnoopVlanNumGeneralQuerySend": mldSnoopVlanNumGeneralQuerySend,
       "mldSnoopVlanNumGeneralQueryRecevied": mldSnoopVlanNumGeneralQueryRecevied,
       "mldSnoopVlanNumSepcificQuerySend": mldSnoopVlanNumSepcificQuerySend,
       "mldsnoopVlanNumSpecificQueryReceived": mldsnoopVlanNumSpecificQueryReceived,
       "mldSnoopVlanNumInvalidReport": mldSnoopVlanNumInvalidReport,
       "mldSnoopVlanClearStatistics": mldSnoopVlanClearStatistics,
       "dynamicArpInspectionMgt": dynamicArpInspectionMgt,
       "daiGlobal": daiGlobal,
       "daiGlobalStatus": daiGlobalStatus,
       "daiGlobalSrcMacValidation": daiGlobalSrcMacValidation,
       "daiGlobalDestMacValidation": daiGlobalDestMacValidation,
       "daiGlobalIpAddrValidation": daiGlobalIpAddrValidation,
       "daiGlobalLogNumber": daiGlobalLogNumber,
       "daiGlobalLogInterval": daiGlobalLogInterval,
       "daiGlobalAdditionalValidStatus": daiGlobalAdditionalValidStatus,
       "daiGlobalIpAddrValidationAllowZeros": daiGlobalIpAddrValidationAllowZeros,
       "daiVlan": daiVlan,
       "daiVlanTable": daiVlanTable,
       "daiVlanEntry": daiVlanEntry,
       "daiVlanIndex": daiVlanIndex,
       "daiVlanStatus": daiVlanStatus,
       "daiVlanArpAclName": daiVlanArpAclName,
       "daiVlanArpAclStatus": daiVlanArpAclStatus,
       "daiInterface": daiInterface,
       "daiPortTable": daiPortTable,
       "daiPortEntry": daiPortEntry,
       "daiPortIfIndex": daiPortIfIndex,
       "daiPortTrustStatus": daiPortTrustStatus,
       "daiPortRateLimit": daiPortRateLimit,
       "daiLog": daiLog,
       "daiLogTable": daiLogTable,
       "daiLogEntry": daiLogEntry,
       "daiLogIndex": daiLogIndex,
       "daiLogVlan": daiLogVlan,
       "daiLogPort": daiLogPort,
       "daiLogSrcIpAddress": daiLogSrcIpAddress,
       "daiLogDestIpAddress": daiLogDestIpAddress,
       "daiLogSrcMacAddress": daiLogSrcMacAddress,
       "daiLogDestMacAddress": daiLogDestMacAddress,
       "daiStatistics": daiStatistics,
       "daiTotalReceivedPkts": daiTotalReceivedPkts,
       "daiTotalDroppedPkts": daiTotalDroppedPkts,
       "daiTotalProcessedPkts": daiTotalProcessedPkts,
       "daiTotalSrcMacDroppedPkts": daiTotalSrcMacDroppedPkts,
       "daiTotalDestMacDroppedPkts": daiTotalDestMacDroppedPkts,
       "daiTotalIpAddrDroppedPkts": daiTotalIpAddrDroppedPkts,
       "daiTotalArpAclDroppedPkts": daiTotalArpAclDroppedPkts,
       "daiTotalDhcpSnoopingDroppedPkts": daiTotalDhcpSnoopingDroppedPkts,
       "timeRangeMgt": timeRangeMgt,
       "timeRangeTable": timeRangeTable,
       "timeRangeEntry": timeRangeEntry,
       "timeRangeIndex": timeRangeIndex,
       "timeRangeName": timeRangeName,
       "timeRangeStatus": timeRangeStatus,
       "timeRangePeriodicTable": timeRangePeriodicTable,
       "timeRangePeriodicEntry": timeRangePeriodicEntry,
       "timeRangePeriodicTimeRangeIndex": timeRangePeriodicTimeRangeIndex,
       "timeRangePeriodicStartDaysOfTheWeek": timeRangePeriodicStartDaysOfTheWeek,
       "timeRangePeriodicStartHours": timeRangePeriodicStartHours,
       "timeRangePeriodicStartMinutes": timeRangePeriodicStartMinutes,
       "timeRangePeriodicEndDaysOfTheWeek": timeRangePeriodicEndDaysOfTheWeek,
       "timeRangePeriodicEndHours": timeRangePeriodicEndHours,
       "timeRangePeriodicEndMinutes": timeRangePeriodicEndMinutes,
       "timeRangePeriodicStatus": timeRangePeriodicStatus,
       "timeRangeAbsoluteTable": timeRangeAbsoluteTable,
       "timeRangeAbsoluteEntry": timeRangeAbsoluteEntry,
       "timeRangeAbsoluteTimeRangeIndex": timeRangeAbsoluteTimeRangeIndex,
       "timeRangeAbsoluteStartYears": timeRangeAbsoluteStartYears,
       "timeRangeAbsoluteStartMonths": timeRangeAbsoluteStartMonths,
       "timeRangeAbsoluteStartDays": timeRangeAbsoluteStartDays,
       "timeRangeAbsoluteStartHours": timeRangeAbsoluteStartHours,
       "timeRangeAbsoluteStartMinutes": timeRangeAbsoluteStartMinutes,
       "timeRangeAbsoluteEndYears": timeRangeAbsoluteEndYears,
       "timeRangeAbsoluteEndMonths": timeRangeAbsoluteEndMonths,
       "timeRangeAbsoluteEndDays": timeRangeAbsoluteEndDays,
       "timeRangeAbsoluteEndHours": timeRangeAbsoluteEndHours,
       "timeRangeAbsoluteEndMinutes": timeRangeAbsoluteEndMinutes,
       "timeRangeAbsoluteStatus": timeRangeAbsoluteStatus,
       "lbdMgt": lbdMgt,
       "lbdGlobal": lbdGlobal,
       "lbdGlobalStatus": lbdGlobalStatus,
       "lbdTransmitInterval": lbdTransmitInterval,
       "lbdRecoverTime": lbdRecoverTime,
       "lbdMode": lbdMode,
       "lbdAction": lbdAction,
       "lbdTrap": lbdTrap,
       "lbdInterface": lbdInterface,
       "lbdPortTable": lbdPortTable,
       "lbdPortEntry": lbdPortEntry,
       "lbdPortIfIndex": lbdPortIfIndex,
       "lbdPortAdminState": lbdPortAdminState,
       "lbdPortOperState": lbdPortOperState,
       "lbdPortLoopedVlan": lbdPortLoopedVlan,
       "ecs2100-28ppNotifications": ecs2100_28ppNotifications,
       "ecs2100-28ppTraps": ecs2100_28ppTraps,
       "ecs2100-28ppTrapsPrefix": ecs2100_28ppTrapsPrefix,
       "swPowerStatusChangeTrap": swPowerStatusChangeTrap,
       "swPortSecurityTrap": swPortSecurityTrap,
       "swIpFilterRejectTrap": swIpFilterRejectTrap,
       "pethPsePortOnOffNotification": pethPsePortOnOffNotification,
       "pethPsePortPowerMaintenanceStatusNotification": pethPsePortPowerMaintenanceStatusNotification,
       "pethMainPowerUsageOnNotification": pethMainPowerUsageOnNotification,
       "pethMainPowerUsageOffNotification": pethMainPowerUsageOffNotification,
       "swAtcBcastStormAlarmFireTrap": swAtcBcastStormAlarmFireTrap,
       "swAtcBcastStormAlarmClearTrap": swAtcBcastStormAlarmClearTrap,
       "swAtcBcastStormTcApplyTrap": swAtcBcastStormTcApplyTrap,
       "swAtcBcastStormTcReleaseTrap": swAtcBcastStormTcReleaseTrap,
       "swAtcMcastStormAlarmFireTrap": swAtcMcastStormAlarmFireTrap,
       "swAtcMcastStormAlarmClearTrap": swAtcMcastStormAlarmClearTrap,
       "swAtcMcastStormTcApplyTrap": swAtcMcastStormTcApplyTrap,
       "swAtcMcastStormTcReleaseTrap": swAtcMcastStormTcReleaseTrap,
       "stpBpduGuardPortShutdownTrap": stpBpduGuardPortShutdownTrap,
       "swLoopbackDetectionTrap": swLoopbackDetectionTrap,
       "networkAccessPortLinkDetectionTrap": networkAccessPortLinkDetectionTrap,
       "dot1agCfmMepUpTrap": dot1agCfmMepUpTrap,
       "dot1agCfmMepDownTrap": dot1agCfmMepDownTrap,
       "dot1agCfmConfigFailTrap": dot1agCfmConfigFailTrap,
       "dot1agCfmLoopFindTrap": dot1agCfmLoopFindTrap,
       "dot1agCfmMepUnknownTrap": dot1agCfmMepUnknownTrap,
       "dot1agCfmMepMissingTrap": dot1agCfmMepMissingTrap,
       "dot1agCfmMaUpTrap": dot1agCfmMaUpTrap,
       "autoUpgradeTrap": autoUpgradeTrap,
       "swCpuUtiRisingNotification": swCpuUtiRisingNotification,
       "swCpuUtiFallingNotification": swCpuUtiFallingNotification,
       "swMemoryUtiRisingThresholdNotification": swMemoryUtiRisingThresholdNotification,
       "swMemoryUtiFallingThresholdNotification": swMemoryUtiFallingThresholdNotification,
       "dhcpRogueServerAttackTrap": dhcpRogueServerAttackTrap,
       "macNotificationTrap": macNotificationTrap,
       "lbdDetectionTrap": lbdDetectionTrap,
       "lbdRecoveryTrap": lbdRecoveryTrap,
       "sfpThresholdAlarmWarnTrap": sfpThresholdAlarmWarnTrap,
       "udldPortShutdownTrap": udldPortShutdownTrap,
       "userAuthenticationFailureTrap": userAuthenticationFailureTrap,
       "userAuthenticationSuccessTrap": userAuthenticationSuccessTrap,
       "loginTrap": loginTrap,
       "logoutTrap": logoutTrap,
       "fileCopyTrap": fileCopyTrap,
       "userauthCreateUserTrap": userauthCreateUserTrap,
       "userauthDeleteUserTrap": userauthDeleteUserTrap,
       "userauthModifyUserPrivilegeTrap": userauthModifyUserPrivilegeTrap,
       "cpuGuardControlTrap": cpuGuardControlTrap,
       "cpuGuardReleaseTrap": cpuGuardReleaseTrap,
       "ecs2100-10t": ecs2100_10t,
       "ecs2100-10pe": ecs2100_10pe,
       "ecs2100-10p": ecs2100_10p,
       "ecs2100-28t": ecs2100_28t,
       "ecs2100-28p": ecs2100_28p,
       "ecs2100-28pp": ecs2100_28pp,
       "ecs2100-52t": ecs2100_52t,
       "ecs2110-26t": ecs2110_26t}
)
