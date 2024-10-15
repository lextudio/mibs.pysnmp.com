# SNMP MIB module (NSTACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSTACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:36 2024
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



class PortsBitmap(OctetString):
    """Custom type PortsBitmap based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbsStackInfo_ObjectIdentity = ObjectIdentity
nbsStackInfo = _NbsStackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4)
)
_NbsStackSlotCapacity_Type = Integer32
_NbsStackSlotCapacity_Object = MibScalar
nbsStackSlotCapacity = _NbsStackSlotCapacity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 1),
    _NbsStackSlotCapacity_Type()
)
nbsStackSlotCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotCapacity.setStatus("mandatory")
_NbsStackSlotsTableSize_Type = Integer32
_NbsStackSlotsTableSize_Object = MibScalar
nbsStackSlotsTableSize = _NbsStackSlotsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 2),
    _NbsStackSlotsTableSize_Type()
)
nbsStackSlotsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotsTableSize.setStatus("mandatory")
_NbsStackPortsCapacity_Type = Integer32
_NbsStackPortsCapacity_Object = MibScalar
nbsStackPortsCapacity = _NbsStackPortsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 3),
    _NbsStackPortsCapacity_Type()
)
nbsStackPortsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackPortsCapacity.setStatus("mandatory")
_NbsStackSlotPortsCapacity_Type = Integer32
_NbsStackSlotPortsCapacity_Object = MibScalar
nbsStackSlotPortsCapacity = _NbsStackSlotPortsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 4),
    _NbsStackSlotPortsCapacity_Type()
)
nbsStackSlotPortsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotPortsCapacity.setStatus("mandatory")
_NbsStackSlotTable_Object = MibTable
nbsStackSlotTable = _NbsStackSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5)
)
if mibBuilder.loadTexts:
    nbsStackSlotTable.setStatus("mandatory")
_NbsStackSlotEntry_Object = MibTableRow
nbsStackSlotEntry = _NbsStackSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1)
)
nbsStackSlotEntry.setIndexNames(
    (0, "NSTACK-MIB", "nbsStackSlotIndex"),
)
if mibBuilder.loadTexts:
    nbsStackSlotEntry.setStatus("mandatory")
_NbsStackSlotIndex_Type = Integer32
_NbsStackSlotIndex_Object = MibTableColumn
nbsStackSlotIndex = _NbsStackSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 1),
    _NbsStackSlotIndex_Type()
)
nbsStackSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotIndex.setStatus("mandatory")


class _NbsStackSlotType_Type(Integer32):
    """Custom type nbsStackSlotType based on Integer32"""
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
        *(("agentSlot", 10),
          ("empty", 1),
          ("eth0Ports100TPand2Ports100FO", 42),
          ("eth10Ports100FO", 7),
          ("eth16Ports10or100TP", 8),
          ("eth1Port1000FORED", 39),
          ("eth1Port100or1000TP", 38),
          ("eth1Ports1000FOMM", 15),
          ("eth1Ports1000FOSM", 16),
          ("eth1Ports1000MTRJ", 44),
          ("eth1StackPorts100or1000TP", 45),
          ("eth20Ports10or100TP", 5),
          ("eth2Ports1000FO", 24),
          ("eth2Ports1000FOMM", 17),
          ("eth2Ports1000FOSM", 18),
          ("eth2Ports100FO", 23),
          ("eth2Ports100FOMM", 13),
          ("eth2Ports100FOSM", 14),
          ("eth2Ports10FL", 36),
          ("eth40Ports10TP", 6),
          ("eth4Ports1000FO", 9),
          ("eth4Ports100FO", 27),
          ("eth4Ports100FOMM", 25),
          ("eth4Ports100FOSM", 26),
          ("eth4Ports100LC", 34),
          ("eth4Ports100MTRJ", 29),
          ("eth4Ports100TPand0Ports100FO", 43),
          ("eth4Ports100TPand1Port100FO", 41),
          ("eth4Ports100TPand2Ports100FO", 40),
          ("eth4Ports100VF", 31),
          ("eth4Ports10FL", 37),
          ("eth4Ports10or100TP", 28),
          ("eth8Ports100LC", 35),
          ("eth8Ports100MTRJ", 30),
          ("eth8Ports100VF", 32),
          ("eth8Ports10or100TP", 12),
          ("ethGigaBitService", 33),
          ("routingEngine", 11),
          ("stackableSlotNH2025", 20),
          ("stackableSlotNoLink", 19),
          ("stackableSlotReserve1", 21),
          ("stackableSlotReserve2", 22),
          ("standAlone", 3),
          ("universal", 4),
          ("unknown", 2))
    )


_NbsStackSlotType_Type.__name__ = "Integer32"
_NbsStackSlotType_Object = MibTableColumn
nbsStackSlotType = _NbsStackSlotType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 2),
    _NbsStackSlotType_Type()
)
nbsStackSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotType.setStatus("mandatory")


class _NbsStackSlotMgmtStatus_Type(Integer32):
    """Custom type nbsStackSlotMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_NbsStackSlotMgmtStatus_Type.__name__ = "Integer32"
_NbsStackSlotMgmtStatus_Object = MibTableColumn
nbsStackSlotMgmtStatus = _NbsStackSlotMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 3),
    _NbsStackSlotMgmtStatus_Type()
)
nbsStackSlotMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotMgmtStatus.setStatus("mandatory")
_NbsStackSlotPortsMaxNumber_Type = Integer32
_NbsStackSlotPortsMaxNumber_Object = MibTableColumn
nbsStackSlotPortsMaxNumber = _NbsStackSlotPortsMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 4),
    _NbsStackSlotPortsMaxNumber_Type()
)
nbsStackSlotPortsMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotPortsMaxNumber.setStatus("mandatory")
_NbsStackSlotPortsNumber_Type = Integer32
_NbsStackSlotPortsNumber_Object = MibTableColumn
nbsStackSlotPortsNumber = _NbsStackSlotPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 5),
    _NbsStackSlotPortsNumber_Type()
)
nbsStackSlotPortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotPortsNumber.setStatus("mandatory")
_NbsStackSlotFirstPort_Type = Integer32
_NbsStackSlotFirstPort_Object = MibTableColumn
nbsStackSlotFirstPort = _NbsStackSlotFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 6),
    _NbsStackSlotFirstPort_Type()
)
nbsStackSlotFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotFirstPort.setStatus("mandatory")


class _NbsStackSlotOperStatus_Type(Integer32):
    """Custom type nbsStackSlotOperStatus based on Integer32"""
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
        *(("changing", 4),
          ("disabled", 3),
          ("enabled", 2),
          ("switchedOff", 1))
    )


_NbsStackSlotOperStatus_Type.__name__ = "Integer32"
_NbsStackSlotOperStatus_Object = MibTableColumn
nbsStackSlotOperStatus = _NbsStackSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 7),
    _NbsStackSlotOperStatus_Type()
)
nbsStackSlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotOperStatus.setStatus("mandatory")


class _NbsStackSlotAdminStatus_Type(Integer32):
    """Custom type nbsStackSlotAdminStatus based on Integer32"""
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


_NbsStackSlotAdminStatus_Type.__name__ = "Integer32"
_NbsStackSlotAdminStatus_Object = MibTableColumn
nbsStackSlotAdminStatus = _NbsStackSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 8),
    _NbsStackSlotAdminStatus_Type()
)
nbsStackSlotAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsStackSlotAdminStatus.setStatus("mandatory")


class _NbsStackSlotRedundantPSMode_Type(Integer32):
    """Custom type nbsStackSlotRedundantPSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("notConnected", 1))
    )


_NbsStackSlotRedundantPSMode_Type.__name__ = "Integer32"
_NbsStackSlotRedundantPSMode_Object = MibTableColumn
nbsStackSlotRedundantPSMode = _NbsStackSlotRedundantPSMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 9),
    _NbsStackSlotRedundantPSMode_Type()
)
nbsStackSlotRedundantPSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotRedundantPSMode.setStatus("mandatory")
_NbsStackSlotUplinkModulesNumber_Type = Integer32
_NbsStackSlotUplinkModulesNumber_Object = MibTableColumn
nbsStackSlotUplinkModulesNumber = _NbsStackSlotUplinkModulesNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 10),
    _NbsStackSlotUplinkModulesNumber_Type()
)
nbsStackSlotUplinkModulesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplinkModulesNumber.setStatus("mandatory")


class _NbsStackSlotReset_Type(Integer32):
    """Custom type nbsStackSlotReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("running", 1))
    )


_NbsStackSlotReset_Type.__name__ = "Integer32"
_NbsStackSlotReset_Object = MibTableColumn
nbsStackSlotReset = _NbsStackSlotReset_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 11),
    _NbsStackSlotReset_Type()
)
nbsStackSlotReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsStackSlotReset.setStatus("mandatory")
_NbsStackSlotIp_Type = IpAddress
_NbsStackSlotIp_Object = MibTableColumn
nbsStackSlotIp = _NbsStackSlotIp_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 12),
    _NbsStackSlotIp_Type()
)
nbsStackSlotIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotIp.setStatus("mandatory")
_NbsStackSlotHwVers_Type = Integer32
_NbsStackSlotHwVers_Object = MibTableColumn
nbsStackSlotHwVers = _NbsStackSlotHwVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 13),
    _NbsStackSlotHwVers_Type()
)
nbsStackSlotHwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotHwVers.setStatus("mandatory")
_NbsStackSlotSwVers_Type = Integer32
_NbsStackSlotSwVers_Object = MibTableColumn
nbsStackSlotSwVers = _NbsStackSlotSwVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 5, 1, 14),
    _NbsStackSlotSwVers_Type()
)
nbsStackSlotSwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotSwVers.setStatus("mandatory")
_NbsStackSlotUplTable_Object = MibTable
nbsStackSlotUplTable = _NbsStackSlotUplTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6)
)
if mibBuilder.loadTexts:
    nbsStackSlotUplTable.setStatus("mandatory")
_NbsStackSlotUplEntry_Object = MibTableRow
nbsStackSlotUplEntry = _NbsStackSlotUplEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1)
)
nbsStackSlotUplEntry.setIndexNames(
    (0, "NSTACK-MIB", "nbsStackSlotNumber"),
    (0, "NSTACK-MIB", "nbsStackSlotUplNumber"),
)
if mibBuilder.loadTexts:
    nbsStackSlotUplEntry.setStatus("mandatory")
_NbsStackSlotNumber_Type = Integer32
_NbsStackSlotNumber_Object = MibTableColumn
nbsStackSlotNumber = _NbsStackSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 1),
    _NbsStackSlotNumber_Type()
)
nbsStackSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotNumber.setStatus("mandatory")
_NbsStackSlotUplNumber_Type = Integer32
_NbsStackSlotUplNumber_Object = MibTableColumn
nbsStackSlotUplNumber = _NbsStackSlotUplNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 2),
    _NbsStackSlotUplNumber_Type()
)
nbsStackSlotUplNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplNumber.setStatus("mandatory")


class _NbsStackSlotUplType_Type(Integer32):
    """Custom type nbsStackSlotUplType based on Integer32"""
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
              39)
        )
    )
    namedValues = NamedValues(
        *(("upl0TP2FO", 36),
          ("upl1ATM", 14),
          ("upl1FDDI", 15),
          ("upl1FO", 7),
          ("upl1GER", 33),
          ("upl1GigaMM", 3),
          ("upl1GigaMTRJ", 38),
          ("upl1GigaSM", 4),
          ("upl1GigaStackTP", 39),
          ("upl1GigaTP", 32),
          ("upl1TP", 8),
          ("upl2FL", 30),
          ("upl2FO", 21),
          ("upl2FOMM", 9),
          ("upl2FOSM", 10),
          ("upl2Giga", 22),
          ("upl2GigaMM", 5),
          ("upl2GigaSM", 6),
          ("upl4FL", 31),
          ("upl4FO", 23),
          ("upl4FOMM", 11),
          ("upl4FOSM", 12),
          ("upl4LC", 28),
          ("upl4MTRJ", 24),
          ("upl4TP", 20),
          ("upl4TP0FO", 37),
          ("upl4TP1FO", 35),
          ("upl4TP2FO", 34),
          ("upl4VF", 26),
          ("upl8LC", 29),
          ("upl8MTRJ", 25),
          ("upl8TP", 13),
          ("upl8VF", 27),
          ("uplAbsent", 1),
          ("uplStackModuleNH2025", 17),
          ("uplStackModuleNoLink", 16),
          ("uplStackModuleReserve1", 18),
          ("uplStackModuleReserve2", 19),
          ("uplUnknown", 2))
    )


_NbsStackSlotUplType_Type.__name__ = "Integer32"
_NbsStackSlotUplType_Object = MibTableColumn
nbsStackSlotUplType = _NbsStackSlotUplType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 3),
    _NbsStackSlotUplType_Type()
)
nbsStackSlotUplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplType.setStatus("mandatory")
_NbsStackSlotUplSwVers_Type = Integer32
_NbsStackSlotUplSwVers_Object = MibTableColumn
nbsStackSlotUplSwVers = _NbsStackSlotUplSwVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 4),
    _NbsStackSlotUplSwVers_Type()
)
nbsStackSlotUplSwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplSwVers.setStatus("mandatory")
_NbsStackSlotUplHwVers_Type = Integer32
_NbsStackSlotUplHwVers_Object = MibTableColumn
nbsStackSlotUplHwVers = _NbsStackSlotUplHwVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 5),
    _NbsStackSlotUplHwVers_Type()
)
nbsStackSlotUplHwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplHwVers.setStatus("mandatory")
_NbsStackSlotUplNPorts_Type = Integer32
_NbsStackSlotUplNPorts_Object = MibTableColumn
nbsStackSlotUplNPorts = _NbsStackSlotUplNPorts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 6),
    _NbsStackSlotUplNPorts_Type()
)
nbsStackSlotUplNPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplNPorts.setStatus("mandatory")
_NbsStackSlotUplFirstPort_Type = Integer32
_NbsStackSlotUplFirstPort_Object = MibTableColumn
nbsStackSlotUplFirstPort = _NbsStackSlotUplFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 7),
    _NbsStackSlotUplFirstPort_Type()
)
nbsStackSlotUplFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplFirstPort.setStatus("mandatory")
_NbsStackSlotUplPortsMask_Type = PortsBitmap
_NbsStackSlotUplPortsMask_Object = MibTableColumn
nbsStackSlotUplPortsMask = _NbsStackSlotUplPortsMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 8),
    _NbsStackSlotUplPortsMask_Type()
)
nbsStackSlotUplPortsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplPortsMask.setStatus("mandatory")


class _NbsStackSlotUplStatus_Type(Integer32):
    """Custom type nbsStackSlotUplStatus based on Integer32"""
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


_NbsStackSlotUplStatus_Type.__name__ = "Integer32"
_NbsStackSlotUplStatus_Object = MibTableColumn
nbsStackSlotUplStatus = _NbsStackSlotUplStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 9),
    _NbsStackSlotUplStatus_Type()
)
nbsStackSlotUplStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplStatus.setStatus("mandatory")
_NbsStackSlotUplHwDescr_Type = DisplayString
_NbsStackSlotUplHwDescr_Object = MibTableColumn
nbsStackSlotUplHwDescr = _NbsStackSlotUplHwDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 10),
    _NbsStackSlotUplHwDescr_Type()
)
nbsStackSlotUplHwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplHwDescr.setStatus("mandatory")
_NbsStackSlotUplSwDescr_Type = DisplayString
_NbsStackSlotUplSwDescr_Object = MibTableColumn
nbsStackSlotUplSwDescr = _NbsStackSlotUplSwDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 6, 1, 11),
    _NbsStackSlotUplSwDescr_Type()
)
nbsStackSlotUplSwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotUplSwDescr.setStatus("mandatory")
_NbsStackSpecSlotTable_Object = MibTable
nbsStackSpecSlotTable = _NbsStackSpecSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 7)
)
if mibBuilder.loadTexts:
    nbsStackSpecSlotTable.setStatus("mandatory")
_NbsStackSpecSlotEntry_Object = MibTableRow
nbsStackSpecSlotEntry = _NbsStackSpecSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 7, 1)
)
nbsStackSpecSlotEntry.setIndexNames(
    (0, "NSTACK-MIB", "nbsStackSlotSpecNumber"),
    (0, "NSTACK-MIB", "nbsStackSlotSpecUplNumber"),
)
if mibBuilder.loadTexts:
    nbsStackSpecSlotEntry.setStatus("mandatory")
_NbsStackSlotSpecNumber_Type = Integer32
_NbsStackSlotSpecNumber_Object = MibTableColumn
nbsStackSlotSpecNumber = _NbsStackSlotSpecNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 7, 1, 1),
    _NbsStackSlotSpecNumber_Type()
)
nbsStackSlotSpecNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotSpecNumber.setStatus("mandatory")
_NbsStackSlotSpecUplNumber_Type = Integer32
_NbsStackSlotSpecUplNumber_Object = MibTableColumn
nbsStackSlotSpecUplNumber = _NbsStackSlotSpecUplNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 7, 1, 2),
    _NbsStackSlotSpecUplNumber_Type()
)
nbsStackSlotSpecUplNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotSpecUplNumber.setStatus("mandatory")


class _NbsStackSlotSpecUplRedundantMode_Type(Integer32):
    """Custom type nbsStackSlotSpecUplRedundantMode based on Integer32"""
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
        *(("autoRedundant", 3),
          ("manualLeftRedundant", 4),
          ("manualRightRedundant", 5),
          ("other", 1),
          ("specialRedundant", 2))
    )


_NbsStackSlotSpecUplRedundantMode_Type.__name__ = "Integer32"
_NbsStackSlotSpecUplRedundantMode_Object = MibTableColumn
nbsStackSlotSpecUplRedundantMode = _NbsStackSlotSpecUplRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 7, 1, 3),
    _NbsStackSlotSpecUplRedundantMode_Type()
)
nbsStackSlotSpecUplRedundantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsStackSlotSpecUplRedundantMode.setStatus("mandatory")


class _NbsStackSlotSpecUplLeftLinkLed_Type(Integer32):
    """Custom type nbsStackSlotSpecUplLeftLinkLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_NbsStackSlotSpecUplLeftLinkLed_Type.__name__ = "Integer32"
_NbsStackSlotSpecUplLeftLinkLed_Object = MibTableColumn
nbsStackSlotSpecUplLeftLinkLed = _NbsStackSlotSpecUplLeftLinkLed_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 7, 1, 4),
    _NbsStackSlotSpecUplLeftLinkLed_Type()
)
nbsStackSlotSpecUplLeftLinkLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotSpecUplLeftLinkLed.setStatus("mandatory")


class _NbsStackSlotSpecUplLeftActivityLed_Type(Integer32):
    """Custom type nbsStackSlotSpecUplLeftActivityLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_NbsStackSlotSpecUplLeftActivityLed_Type.__name__ = "Integer32"
_NbsStackSlotSpecUplLeftActivityLed_Object = MibTableColumn
nbsStackSlotSpecUplLeftActivityLed = _NbsStackSlotSpecUplLeftActivityLed_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 7, 1, 5),
    _NbsStackSlotSpecUplLeftActivityLed_Type()
)
nbsStackSlotSpecUplLeftActivityLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotSpecUplLeftActivityLed.setStatus("mandatory")


class _NbsStackSlotSpecUplRightLinkLed_Type(Integer32):
    """Custom type nbsStackSlotSpecUplRightLinkLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_NbsStackSlotSpecUplRightLinkLed_Type.__name__ = "Integer32"
_NbsStackSlotSpecUplRightLinkLed_Object = MibTableColumn
nbsStackSlotSpecUplRightLinkLed = _NbsStackSlotSpecUplRightLinkLed_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 7, 1, 6),
    _NbsStackSlotSpecUplRightLinkLed_Type()
)
nbsStackSlotSpecUplRightLinkLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotSpecUplRightLinkLed.setStatus("mandatory")


class _NbsStackSlotSpecUplRightActivityLed_Type(Integer32):
    """Custom type nbsStackSlotSpecUplRightActivityLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_NbsStackSlotSpecUplRightActivityLed_Type.__name__ = "Integer32"
_NbsStackSlotSpecUplRightActivityLed_Object = MibTableColumn
nbsStackSlotSpecUplRightActivityLed = _NbsStackSlotSpecUplRightActivityLed_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 4, 7, 1, 7),
    _NbsStackSlotSpecUplRightActivityLed_Type()
)
nbsStackSlotSpecUplRightActivityLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsStackSlotSpecUplRightActivityLed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSTACK-MIB",
    **{"PortsBitmap": PortsBitmap,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbsStackInfo": nbsStackInfo,
       "nbsStackSlotCapacity": nbsStackSlotCapacity,
       "nbsStackSlotsTableSize": nbsStackSlotsTableSize,
       "nbsStackPortsCapacity": nbsStackPortsCapacity,
       "nbsStackSlotPortsCapacity": nbsStackSlotPortsCapacity,
       "nbsStackSlotTable": nbsStackSlotTable,
       "nbsStackSlotEntry": nbsStackSlotEntry,
       "nbsStackSlotIndex": nbsStackSlotIndex,
       "nbsStackSlotType": nbsStackSlotType,
       "nbsStackSlotMgmtStatus": nbsStackSlotMgmtStatus,
       "nbsStackSlotPortsMaxNumber": nbsStackSlotPortsMaxNumber,
       "nbsStackSlotPortsNumber": nbsStackSlotPortsNumber,
       "nbsStackSlotFirstPort": nbsStackSlotFirstPort,
       "nbsStackSlotOperStatus": nbsStackSlotOperStatus,
       "nbsStackSlotAdminStatus": nbsStackSlotAdminStatus,
       "nbsStackSlotRedundantPSMode": nbsStackSlotRedundantPSMode,
       "nbsStackSlotUplinkModulesNumber": nbsStackSlotUplinkModulesNumber,
       "nbsStackSlotReset": nbsStackSlotReset,
       "nbsStackSlotIp": nbsStackSlotIp,
       "nbsStackSlotHwVers": nbsStackSlotHwVers,
       "nbsStackSlotSwVers": nbsStackSlotSwVers,
       "nbsStackSlotUplTable": nbsStackSlotUplTable,
       "nbsStackSlotUplEntry": nbsStackSlotUplEntry,
       "nbsStackSlotNumber": nbsStackSlotNumber,
       "nbsStackSlotUplNumber": nbsStackSlotUplNumber,
       "nbsStackSlotUplType": nbsStackSlotUplType,
       "nbsStackSlotUplSwVers": nbsStackSlotUplSwVers,
       "nbsStackSlotUplHwVers": nbsStackSlotUplHwVers,
       "nbsStackSlotUplNPorts": nbsStackSlotUplNPorts,
       "nbsStackSlotUplFirstPort": nbsStackSlotUplFirstPort,
       "nbsStackSlotUplPortsMask": nbsStackSlotUplPortsMask,
       "nbsStackSlotUplStatus": nbsStackSlotUplStatus,
       "nbsStackSlotUplHwDescr": nbsStackSlotUplHwDescr,
       "nbsStackSlotUplSwDescr": nbsStackSlotUplSwDescr,
       "nbsStackSpecSlotTable": nbsStackSpecSlotTable,
       "nbsStackSpecSlotEntry": nbsStackSpecSlotEntry,
       "nbsStackSlotSpecNumber": nbsStackSlotSpecNumber,
       "nbsStackSlotSpecUplNumber": nbsStackSlotSpecUplNumber,
       "nbsStackSlotSpecUplRedundantMode": nbsStackSlotSpecUplRedundantMode,
       "nbsStackSlotSpecUplLeftLinkLed": nbsStackSlotSpecUplLeftLinkLed,
       "nbsStackSlotSpecUplLeftActivityLed": nbsStackSlotSpecUplLeftActivityLed,
       "nbsStackSlotSpecUplRightLinkLed": nbsStackSlotSpecUplRightLinkLed,
       "nbsStackSlotSpecUplRightActivityLed": nbsStackSlotSpecUplRightActivityLed}
)
