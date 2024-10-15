# SNMP MIB module (CTRON-SSR-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SSR-HARDWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:40 2024
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

(ssrMibs,) = mibBuilder.importSymbols(
    "CTRON-SSR-SMI-MIB",
    "ssrMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hardwareMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200)
)
hardwareMIB.setRevisions(
        ("2000-07-17 00:00",
         "2000-07-15 00:00",
         "2000-05-31 00:00",
         "2000-03-20 00:00",
         "1999-12-30 00:00",
         "1999-01-20 00:00",
         "1998-08-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SSRInterfaceIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class SSRModuleType(Integer32, TextualConvention):
    status = "current"
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
              15,
              16,
              17,
              20,
              21,
              22,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              503,
              504,
              505,
              506,
              507)
        )
    )
    namedValues = NamedValues(
        *(("atm155", 24),
          ("cmts1x4port", 15),
          ("controlModule", 1),
          ("controlModule2", 11),
          ("controlModule3", 17),
          ("ether100FX", 3),
          ("ether100TX", 2),
          ("ether100TX16port", 21),
          ("fddi2port", 16),
          ("gigabit6K2PBP", 30),
          ("gigabitFX2PGBIC", 29),
          ("gigabitFX4P", 27),
          ("gigabitFX4PGBIC", 28),
          ("gigabitLLX", 9),
          ("gigabitLLX2P", 12),
          ("gigabitLX", 5),
          ("gigabitSX", 4),
          ("gigabitTX", 22),
          ("hssi", 7),
          ("none", 10),
          ("rbControlModule", 507),
          ("rbEther100TC32P", 506),
          ("rbEther100TX24P", 505),
          ("rbGigabit4PGBIC", 504),
          ("rbGigabit8PGBIC", 503),
          ("serial2port", 13),
          ("serial4port", 6),
          ("serial4portCE", 20),
          ("sonet2PortOc12", 26),
          ("sonet4PortOc3", 25),
          ("unknown", 8))
    )



class SSRModuleStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )



class SSRPortType(Integer32, TextualConvention):
    status = "current"
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
        *(("cmt", 9),
          ("ds1", 7),
          ("ds3", 8),
          ("e1", 10),
          ("e3", 11),
          ("etherFast", 1),
          ("fddi", 12),
          ("gigEther", 2),
          ("hssi", 3),
          ("serial", 4),
          ("sonet", 6),
          ("unknown", 5))
    )



class SSRPortConnectorType(Integer32, TextualConvention):
    status = "current"
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("aui", 9),
          ("bncf", 21),
          ("bncm", 22),
          ("db15f", 4),
          ("db15m", 3),
          ("db25f", 6),
          ("db25m", 5),
          ("db9f", 2),
          ("db9m", 1),
          ("eia530", 13),
          ("empty", 0),
          ("fiberMTRjMM", 19),
          ("fiberMTRjSM", 20),
          ("fiberScMM", 11),
          ("fiberScSM", 18),
          ("fiberScSMLH", 24),
          ("ftypef", 10),
          ("hssi", 16),
          ("rj11", 7),
          ("rj21", 23),
          ("rj45", 8),
          ("rs44x", 14),
          ("unknown", 17),
          ("v35", 12),
          ("x21", 15))
    )



class SSRserviceType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )



class SSRmemorySize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )



class SSRSwitchingFabricInfo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class SSRCmLedState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class SSRBackupCMState(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 5),
          ("inactive", 2),
          ("notInstalled", 4),
          ("standby", 3),
          ("unknown", 1))
    )



class PowerSupplyBits(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SysHwGroup_ObjectIdentity = ObjectIdentity
sysHwGroup = _SysHwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1)
)


class _SysHwNumSlots_Type(Integer32):
    """Custom type sysHwNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SysHwNumSlots_Type.__name__ = "Integer32"
_SysHwNumSlots_Object = MibScalar
sysHwNumSlots = _SysHwNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 1),
    _SysHwNumSlots_Type()
)
sysHwNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwNumSlots.setStatus("current")
_SysHwModuleTable_Object = MibTable
sysHwModuleTable = _SysHwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sysHwModuleTable.setStatus("current")
_SysHwModuleEntry_Object = MibTableRow
sysHwModuleEntry = _SysHwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1)
)
sysHwModuleEntry.setIndexNames(
    (0, "CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"),
)
if mibBuilder.loadTexts:
    sysHwModuleEntry.setStatus("current")


class _SysHwModuleSlotNumber_Type(Integer32):
    """Custom type sysHwModuleSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_SysHwModuleSlotNumber_Type.__name__ = "Integer32"
_SysHwModuleSlotNumber_Object = MibTableColumn
sysHwModuleSlotNumber = _SysHwModuleSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 1),
    _SysHwModuleSlotNumber_Type()
)
sysHwModuleSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwModuleSlotNumber.setStatus("current")
_SysHwModuleType_Type = SSRModuleType
_SysHwModuleType_Object = MibTableColumn
sysHwModuleType = _SysHwModuleType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 2),
    _SysHwModuleType_Type()
)
sysHwModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwModuleType.setStatus("current")


class _SysHwModuleDesc_Type(OctetString):
    """Custom type sysHwModuleDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysHwModuleDesc_Type.__name__ = "OctetString"
_SysHwModuleDesc_Object = MibTableColumn
sysHwModuleDesc = _SysHwModuleDesc_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 3),
    _SysHwModuleDesc_Type()
)
sysHwModuleDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwModuleDesc.setStatus("current")


class _SysHwModuleNumPorts_Type(Integer32):
    """Custom type sysHwModuleNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SysHwModuleNumPorts_Type.__name__ = "Integer32"
_SysHwModuleNumPorts_Object = MibTableColumn
sysHwModuleNumPorts = _SysHwModuleNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 4),
    _SysHwModuleNumPorts_Type()
)
sysHwModuleNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwModuleNumPorts.setStatus("current")


class _SysHwModuleVersion_Type(OctetString):
    """Custom type sysHwModuleVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SysHwModuleVersion_Type.__name__ = "OctetString"
_SysHwModuleVersion_Object = MibTableColumn
sysHwModuleVersion = _SysHwModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 5),
    _SysHwModuleVersion_Type()
)
sysHwModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwModuleVersion.setStatus("current")
_SysHwModuleMemory_Type = SSRmemorySize
_SysHwModuleMemory_Object = MibTableColumn
sysHwModuleMemory = _SysHwModuleMemory_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 6),
    _SysHwModuleMemory_Type()
)
sysHwModuleMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwModuleMemory.setStatus("current")
_SysHwModuleService_Type = SSRserviceType
_SysHwModuleService_Object = MibTableColumn
sysHwModuleService = _SysHwModuleService_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 8),
    _SysHwModuleService_Type()
)
sysHwModuleService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwModuleService.setStatus("current")
_SysHwModuleStatus_Type = SSRModuleStatus
_SysHwModuleStatus_Object = MibTableColumn
sysHwModuleStatus = _SysHwModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 2, 1, 9),
    _SysHwModuleStatus_Type()
)
sysHwModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwModuleStatus.setStatus("current")
_SysHwPortTable_Object = MibTable
sysHwPortTable = _SysHwPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sysHwPortTable.setStatus("current")
_SysHwPortEntry_Object = MibTableRow
sysHwPortEntry = _SysHwPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1)
)
sysHwPortEntry.setIndexNames(
    (0, "CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"),
    (0, "CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"),
)
if mibBuilder.loadTexts:
    sysHwPortEntry.setStatus("current")


class _SysHwPortSlotNumber_Type(Integer32):
    """Custom type sysHwPortSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysHwPortSlotNumber_Type.__name__ = "Integer32"
_SysHwPortSlotNumber_Object = MibTableColumn
sysHwPortSlotNumber = _SysHwPortSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 1),
    _SysHwPortSlotNumber_Type()
)
sysHwPortSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwPortSlotNumber.setStatus("current")


class _SysHwPortNumber_Type(Integer32):
    """Custom type sysHwPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysHwPortNumber_Type.__name__ = "Integer32"
_SysHwPortNumber_Object = MibTableColumn
sysHwPortNumber = _SysHwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 2),
    _SysHwPortNumber_Type()
)
sysHwPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwPortNumber.setStatus("current")
_SysHwPortType_Type = SSRPortType
_SysHwPortType_Object = MibTableColumn
sysHwPortType = _SysHwPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 3),
    _SysHwPortType_Type()
)
sysHwPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwPortType.setStatus("current")
_SysHwPortConnectorType_Type = SSRPortConnectorType
_SysHwPortConnectorType_Object = MibTableColumn
sysHwPortConnectorType = _SysHwPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 4),
    _SysHwPortConnectorType_Type()
)
sysHwPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwPortConnectorType.setStatus("current")
_SysHwPortIfIndex_Type = SSRInterfaceIndex
_SysHwPortIfIndex_Object = MibTableColumn
sysHwPortIfIndex = _SysHwPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 3, 1, 5),
    _SysHwPortIfIndex_Type()
)
sysHwPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwPortIfIndex.setStatus("current")
_SysHwPowerSupply_Type = PowerSupplyBits
_SysHwPowerSupply_Object = MibScalar
sysHwPowerSupply = _SysHwPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 4),
    _SysHwPowerSupply_Type()
)
sysHwPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwPowerSupply.setStatus("current")


class _SysHwFan_Type(Integer32):
    """Custom type sysHwFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notWorking", 2),
          ("unknown", 3),
          ("working", 1))
    )


_SysHwFan_Type.__name__ = "Integer32"
_SysHwFan_Object = MibScalar
sysHwFan = _SysHwFan_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 5),
    _SysHwFan_Type()
)
sysHwFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwFan.setStatus("current")


class _SysHwTemperature_Type(Integer32):
    """Custom type sysHwTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("outOfRange", 2),
          ("unknown", 3))
    )


_SysHwTemperature_Type.__name__ = "Integer32"
_SysHwTemperature_Object = MibScalar
sysHwTemperature = _SysHwTemperature_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 6),
    _SysHwTemperature_Type()
)
sysHwTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwTemperature.setStatus("current")


class _SysHwChassisId_Type(OctetString):
    """Custom type sysHwChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysHwChassisId_Type.__name__ = "OctetString"
_SysHwChassisId_Object = MibScalar
sysHwChassisId = _SysHwChassisId_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 7),
    _SysHwChassisId_Type()
)
sysHwChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwChassisId.setStatus("current")
_SysHwTotalInOctets_Type = Counter64
_SysHwTotalInOctets_Object = MibScalar
sysHwTotalInOctets = _SysHwTotalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 10),
    _SysHwTotalInOctets_Type()
)
sysHwTotalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwTotalInOctets.setStatus("deprecated")
_SysHwTotalOutOctets_Type = Counter64
_SysHwTotalOutOctets_Object = MibScalar
sysHwTotalOutOctets = _SysHwTotalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 11),
    _SysHwTotalOutOctets_Type()
)
sysHwTotalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwTotalOutOctets.setStatus("deprecated")
_SysHwTotalInFrames_Type = Counter64
_SysHwTotalInFrames_Object = MibScalar
sysHwTotalInFrames = _SysHwTotalInFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 12),
    _SysHwTotalInFrames_Type()
)
sysHwTotalInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwTotalInFrames.setStatus("deprecated")
_SysHwTotalOutFrames_Type = Counter64
_SysHwTotalOutFrames_Object = MibScalar
sysHwTotalOutFrames = _SysHwTotalOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 13),
    _SysHwTotalOutFrames_Type()
)
sysHwTotalOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwTotalOutFrames.setStatus("deprecated")
_SysHwTotalL2SwitchedFrames_Type = Counter64
_SysHwTotalL2SwitchedFrames_Object = MibScalar
sysHwTotalL2SwitchedFrames = _SysHwTotalL2SwitchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 14),
    _SysHwTotalL2SwitchedFrames_Type()
)
sysHwTotalL2SwitchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwTotalL2SwitchedFrames.setStatus("deprecated")
_SysHwTotalL3SwitchedFrames_Type = Counter64
_SysHwTotalL3SwitchedFrames_Object = MibScalar
sysHwTotalL3SwitchedFrames = _SysHwTotalL3SwitchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 15),
    _SysHwTotalL3SwitchedFrames_Type()
)
sysHwTotalL3SwitchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwTotalL3SwitchedFrames.setStatus("deprecated")
_SysHwSwitchingFabric_Type = SSRSwitchingFabricInfo
_SysHwSwitchingFabric_Object = MibScalar
sysHwSwitchingFabric = _SysHwSwitchingFabric_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 19),
    _SysHwSwitchingFabric_Type()
)
sysHwSwitchingFabric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwSwitchingFabric.setStatus("current")
_SysHwControlModuleLED_Type = SSRCmLedState
_SysHwControlModuleLED_Object = MibScalar
sysHwControlModuleLED = _SysHwControlModuleLED_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 20),
    _SysHwControlModuleLED_Type()
)
sysHwControlModuleLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwControlModuleLED.setStatus("current")
_SysHwControlModuleBackupState_Type = SSRBackupCMState
_SysHwControlModuleBackupState_Object = MibScalar
sysHwControlModuleBackupState = _SysHwControlModuleBackupState_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 21),
    _SysHwControlModuleBackupState_Type()
)
sysHwControlModuleBackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwControlModuleBackupState.setStatus("current")
_SysHwLastHotSwapEvent_Type = TimeTicks
_SysHwLastHotSwapEvent_Object = MibScalar
sysHwLastHotSwapEvent = _SysHwLastHotSwapEvent_Object(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 1, 22),
    _SysHwLastHotSwapEvent_Type()
)
sysHwLastHotSwapEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwLastHotSwapEvent.setStatus("current")
_HwConformance_ObjectIdentity = ObjectIdentity
hwConformance = _HwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2)
)
_HwCompliances_ObjectIdentity = ObjectIdentity
hwCompliances = _HwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 1)
)
_HwGroups_ObjectIdentity = ObjectIdentity
hwGroups = _HwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2)
)

# Managed Objects groups

hwConfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 1)
)
hwConfGroupV10.setObjects(
      *(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalInOctets"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalOutOctets"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalInFrames"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalOutFrames"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalL2SwitchedFrames"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTotalL3SwitchedFrames"))
)
if mibBuilder.loadTexts:
    hwConfGroupV10.setStatus("deprecated")

hwConfGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2)
)
hwConfGroupV11.setObjects(
      *(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleMemory"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleService"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwSwitchingFabric"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleLED"))
)
if mibBuilder.loadTexts:
    hwConfGroupV11.setStatus("deprecated")

hwConfGroupV12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 3)
)
hwConfGroupV12.setObjects(
      *(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleMemory"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleService"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleStatus"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwSwitchingFabric"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleLED"))
)
if mibBuilder.loadTexts:
    hwConfGroupV12.setStatus("deprecated")

hwConfGroupV30 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 4)
)
hwConfGroupV30.setObjects(
      *(("CTRON-SSR-HARDWARE-MIB", "sysHwNumSlots"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleSlotNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleDesc"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleNumPorts"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleVersion"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleMemory"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleService"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwModuleStatus"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortSlotNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortNumber"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortConnectorType"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPortIfIndex"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwPowerSupply"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwFan"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwTemperature"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwChassisId"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwSwitchingFabric"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleLED"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwControlModuleBackupState"),
        ("CTRON-SSR-HARDWARE-MIB", "sysHwLastHotSwapEvent"))
)
if mibBuilder.loadTexts:
    hwConfGroupV30.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwComplianceV10.setStatus(
        "deprecated"
    )

hwComplianceV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hwComplianceV11.setStatus(
        "deprecated"
    )

hwComplianceV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hwComplianceV12.setStatus(
        "deprecated"
    )

hwComplianceV30 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 2501, 1, 200, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hwComplianceV30.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SSR-HARDWARE-MIB",
    **{"SSRInterfaceIndex": SSRInterfaceIndex,
       "SSRModuleType": SSRModuleType,
       "SSRModuleStatus": SSRModuleStatus,
       "SSRPortType": SSRPortType,
       "SSRPortConnectorType": SSRPortConnectorType,
       "SSRserviceType": SSRserviceType,
       "SSRmemorySize": SSRmemorySize,
       "SSRSwitchingFabricInfo": SSRSwitchingFabricInfo,
       "SSRCmLedState": SSRCmLedState,
       "SSRBackupCMState": SSRBackupCMState,
       "PowerSupplyBits": PowerSupplyBits,
       "sysHwGroup": sysHwGroup,
       "sysHwNumSlots": sysHwNumSlots,
       "sysHwModuleTable": sysHwModuleTable,
       "sysHwModuleEntry": sysHwModuleEntry,
       "sysHwModuleSlotNumber": sysHwModuleSlotNumber,
       "sysHwModuleType": sysHwModuleType,
       "sysHwModuleDesc": sysHwModuleDesc,
       "sysHwModuleNumPorts": sysHwModuleNumPorts,
       "sysHwModuleVersion": sysHwModuleVersion,
       "sysHwModuleMemory": sysHwModuleMemory,
       "sysHwModuleService": sysHwModuleService,
       "sysHwModuleStatus": sysHwModuleStatus,
       "sysHwPortTable": sysHwPortTable,
       "sysHwPortEntry": sysHwPortEntry,
       "sysHwPortSlotNumber": sysHwPortSlotNumber,
       "sysHwPortNumber": sysHwPortNumber,
       "sysHwPortType": sysHwPortType,
       "sysHwPortConnectorType": sysHwPortConnectorType,
       "sysHwPortIfIndex": sysHwPortIfIndex,
       "sysHwPowerSupply": sysHwPowerSupply,
       "sysHwFan": sysHwFan,
       "sysHwTemperature": sysHwTemperature,
       "sysHwChassisId": sysHwChassisId,
       "sysHwTotalInOctets": sysHwTotalInOctets,
       "sysHwTotalOutOctets": sysHwTotalOutOctets,
       "sysHwTotalInFrames": sysHwTotalInFrames,
       "sysHwTotalOutFrames": sysHwTotalOutFrames,
       "sysHwTotalL2SwitchedFrames": sysHwTotalL2SwitchedFrames,
       "sysHwTotalL3SwitchedFrames": sysHwTotalL3SwitchedFrames,
       "sysHwSwitchingFabric": sysHwSwitchingFabric,
       "sysHwControlModuleLED": sysHwControlModuleLED,
       "sysHwControlModuleBackupState": sysHwControlModuleBackupState,
       "sysHwLastHotSwapEvent": sysHwLastHotSwapEvent,
       "hardwareMIB": hardwareMIB,
       "hwConformance": hwConformance,
       "hwCompliances": hwCompliances,
       "hwGroups": hwGroups,
       "hwConfGroupV10": hwConfGroupV10,
       "hwComplianceV10": hwComplianceV10,
       "hwConfGroupV11": hwConfGroupV11,
       "hwComplianceV11": hwComplianceV11,
       "hwComplianceV12": hwComplianceV12,
       "hwComplianceV30": hwComplianceV30,
       "hwConfGroupV12": hwConfGroupV12,
       "hwConfGroupV30": hwConfGroupV30}
)
