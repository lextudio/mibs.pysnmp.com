# SNMP MIB module (CHIPCONC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHIPCONC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:45 2024
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

(DisplayString,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "DisplayString")

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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Chipcom_ObjectIdentity = ObjectIdentity
chipcom = _Chipcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49)
)
_Chipmib02_ObjectIdentity = ObjectIdentity
chipmib02 = _Chipmib02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2)
)
_ChipGen_ObjectIdentity = ObjectIdentity
chipGen = _ChipGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 1)
)
_ChipEcho_ObjectIdentity = ObjectIdentity
chipEcho = _ChipEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 2)
)
_ChipProducts_ObjectIdentity = ObjectIdentity
chipProducts = _ChipProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3)
)
_Online_ObjectIdentity = ObjectIdentity
online = _Online_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1)
)
_OlAgents_ObjectIdentity = ObjectIdentity
olAgents = _OlAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1)
)
_OlAgentsMySlot_Type = Integer32
_OlAgentsMySlot_Object = MibScalar
olAgentsMySlot = _OlAgentsMySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 1),
    _OlAgentsMySlot_Type()
)
olAgentsMySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsMySlot.setStatus("mandatory")


class _OlAgentsMasterReset_Type(Integer32):
    """Custom type olAgentsMasterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_OlAgentsMasterReset_Type.__name__ = "Integer32"
_OlAgentsMasterReset_Object = MibScalar
olAgentsMasterReset = _OlAgentsMasterReset_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 2),
    _OlAgentsMasterReset_Type()
)
olAgentsMasterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olAgentsMasterReset.setStatus("mandatory")
_OlAgentsTable_Object = MibTable
olAgentsTable = _OlAgentsTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    olAgentsTable.setStatus("mandatory")
_OlAgentsEntry_Object = MibTableRow
olAgentsEntry = _OlAgentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1)
)
olAgentsEntry.setIndexNames(
    (0, "CHIPCONC-MIB", "olAgentsSlotIndex"),
)
if mibBuilder.loadTexts:
    olAgentsEntry.setStatus("mandatory")
_OlAgentsSlotIndex_Type = Integer32
_OlAgentsSlotIndex_Object = MibTableColumn
olAgentsSlotIndex = _OlAgentsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 1),
    _OlAgentsSlotIndex_Type()
)
olAgentsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsSlotIndex.setStatus("mandatory")


class _OlAgentsStationAddr_Type(OctetString):
    """Custom type olAgentsStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OlAgentsStationAddr_Type.__name__ = "OctetString"
_OlAgentsStationAddr_Object = MibTableColumn
olAgentsStationAddr = _OlAgentsStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 2),
    _OlAgentsStationAddr_Type()
)
olAgentsStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsStationAddr.setStatus("mandatory")
_OlAgentsIpAddress_Type = IpAddress
_OlAgentsIpAddress_Object = MibTableColumn
olAgentsIpAddress = _OlAgentsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 3),
    _OlAgentsIpAddress_Type()
)
olAgentsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsIpAddress.setStatus("mandatory")


class _OlAgentsMasterStatus_Type(Integer32):
    """Custom type olAgentsMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("electing", 3),
          ("master", 1),
          ("non-master", 2))
    )


_OlAgentsMasterStatus_Type.__name__ = "Integer32"
_OlAgentsMasterStatus_Object = MibTableColumn
olAgentsMasterStatus = _OlAgentsMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 4),
    _OlAgentsMasterStatus_Type()
)
olAgentsMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olAgentsMasterStatus.setStatus("mandatory")


class _OlAgentsMasterPriority_Type(Integer32):
    """Custom type olAgentsMasterPriority based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("never", 11),
          ("nine", 9),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_OlAgentsMasterPriority_Type.__name__ = "Integer32"
_OlAgentsMasterPriority_Object = MibTableColumn
olAgentsMasterPriority = _OlAgentsMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1, 3, 1, 5),
    _OlAgentsMasterPriority_Type()
)
olAgentsMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olAgentsMasterPriority.setStatus("mandatory")
_OlConc_ObjectIdentity = ObjectIdentity
olConc = _OlConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2)
)


class _OlConcType_Type(Integer32):
    """Custom type olConcType based on Integer32"""
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
        *(("online-seventeen-slot", 1),
          ("online-six-slot", 2),
          ("online-six-slot-ft", 3),
          ("online-six-slot-ft-hc", 5),
          ("online-six-slot-hc", 4))
    )


_OlConcType_Type.__name__ = "Integer32"
_OlConcType_Object = MibScalar
olConcType = _OlConcType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2, 1),
    _OlConcType_Type()
)
olConcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olConcType.setStatus("mandatory")


class _OlConcReset_Type(Integer32):
    """Custom type olConcReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_OlConcReset_Type.__name__ = "Integer32"
_OlConcReset_Object = MibScalar
olConcReset = _OlConcReset_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2, 2),
    _OlConcReset_Type()
)
olConcReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olConcReset.setStatus("mandatory")
_OlConcNumSlots_Type = Integer32
_OlConcNumSlots_Object = MibScalar
olConcNumSlots = _OlConcNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2, 3),
    _OlConcNumSlots_Type()
)
olConcNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olConcNumSlots.setStatus("mandatory")


class _OlConcProfile_Type(OctetString):
    """Custom type olConcProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_OlConcProfile_Type.__name__ = "OctetString"
_OlConcProfile_Object = MibScalar
olConcProfile = _OlConcProfile_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2, 4),
    _OlConcProfile_Type()
)
olConcProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olConcProfile.setStatus("mandatory")
_OlEnv_ObjectIdentity = ObjectIdentity
olEnv = _OlEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3)
)


class _OlEnvTempStatus_Type(Integer32):
    """Custom type olEnvTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_OlEnvTempStatus_Type.__name__ = "Integer32"
_OlEnvTempStatus_Object = MibScalar
olEnvTempStatus = _OlEnvTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 1),
    _OlEnvTempStatus_Type()
)
olEnvTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvTempStatus.setStatus("mandatory")
_OlEnvPSCapacity_Type = Integer32
_OlEnvPSCapacity_Object = MibScalar
olEnvPSCapacity = _OlEnvPSCapacity_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 2),
    _OlEnvPSCapacity_Type()
)
olEnvPSCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvPSCapacity.setStatus("mandatory")
_OlEnvPSTable_Object = MibTable
olEnvPSTable = _OlEnvPSTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    olEnvPSTable.setStatus("mandatory")
_OlEnvPSEntry_Object = MibTableRow
olEnvPSEntry = _OlEnvPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3, 1)
)
olEnvPSEntry.setIndexNames(
    (0, "CHIPCONC-MIB", "olEnvPSIndex"),
)
if mibBuilder.loadTexts:
    olEnvPSEntry.setStatus("mandatory")
_OlEnvPSIndex_Type = Integer32
_OlEnvPSIndex_Object = MibTableColumn
olEnvPSIndex = _OlEnvPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3, 1, 1),
    _OlEnvPSIndex_Type()
)
olEnvPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvPSIndex.setStatus("mandatory")


class _OlEnvPSAdminState_Type(Integer32):
    """Custom type olEnvPSAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("standby", 2))
    )


_OlEnvPSAdminState_Type.__name__ = "Integer32"
_OlEnvPSAdminState_Object = MibTableColumn
olEnvPSAdminState = _OlEnvPSAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3, 1, 2),
    _OlEnvPSAdminState_Type()
)
olEnvPSAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olEnvPSAdminState.setStatus("mandatory")


class _OlEnvPSOperStatus_Type(Integer32):
    """Custom type olEnvPSOperStatus based on Integer32"""
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
        *(("active", 1),
          ("faulty", 3),
          ("not-installed", 4),
          ("standby", 2))
    )


_OlEnvPSOperStatus_Type.__name__ = "Integer32"
_OlEnvPSOperStatus_Object = MibTableColumn
olEnvPSOperStatus = _OlEnvPSOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 3, 1, 3),
    _OlEnvPSOperStatus_Type()
)
olEnvPSOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvPSOperStatus.setStatus("mandatory")


class _OlEnvFanStatus_Type(Integer32):
    """Custom type olEnvFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 3),
          ("not-installed", 4),
          ("okay", 1),
          ("unknown", 5))
    )


_OlEnvFanStatus_Type.__name__ = "Integer32"
_OlEnvFanStatus_Object = MibScalar
olEnvFanStatus = _OlEnvFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3, 4),
    _OlEnvFanStatus_Type()
)
olEnvFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olEnvFanStatus.setStatus("mandatory")
_OlModules_ObjectIdentity = ObjectIdentity
olModules = _OlModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4)
)
_OlModTable_Object = MibTable
olModTable = _OlModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    olModTable.setStatus("mandatory")
_OlModEntry_Object = MibTableRow
olModEntry = _OlModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1)
)
olModEntry.setIndexNames(
    (0, "CHIPCONC-MIB", "olModSlotIndex"),
)
if mibBuilder.loadTexts:
    olModEntry.setStatus("mandatory")
_OlModSlotIndex_Type = Integer32
_OlModSlotIndex_Object = MibTableColumn
olModSlotIndex = _OlModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 1),
    _OlModSlotIndex_Type()
)
olModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModSlotIndex.setStatus("mandatory")


class _OlModType_Type(Integer32):
    """Custom type olModType based on Integer32"""
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
              33)
        )
    )
    namedValues = NamedValues(
        *(("module-50nnM-CTL", 3),
          ("module-50nnM-HCTL", 33),
          ("module-50nnM-RCTL", 23),
          ("module-51nnB-EE", 9),
          ("module-51nnI-x", 31),
          ("module-51nnM-AUIF", 12),
          ("module-51nnM-AUIM", 13),
          ("module-51nnM-BNC", 8),
          ("module-51nnM-FB", 24),
          ("module-51nnM-FBP", 16),
          ("module-51nnM-FIB", 5),
          ("module-51nnM-FL", 22),
          ("module-51nnM-FP", 15),
          ("module-51nnM-MGT", 4),
          ("module-51nnM-TP", 7),
          ("module-51nnM-TPCL", 29),
          ("module-51nnM-TPL", 17),
          ("module-51nnM-TPPL", 18),
          ("module-51nnM-TS", 21),
          ("module-51nnM-UTP", 6),
          ("module-51nnR-EE", 11),
          ("module-51nnR-ES", 10),
          ("module-5208M-TP", 14),
          ("module-52nnB-TT", 30),
          ("module-52nnM-FR", 20),
          ("module-52nnM-MGT", 32),
          ("module-52nnM-TP", 19),
          ("module-53nnM-FBMIC", 26),
          ("module-53nnM-FIBST", 27),
          ("module-53nnM-MGT", 25),
          ("module-53nnM-STP", 28),
          ("module-unknown", 2),
          ("module-unmanageable", 1))
    )


_OlModType_Type.__name__ = "Integer32"
_OlModType_Object = MibTableColumn
olModType = _OlModType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 2),
    _OlModType_Type()
)
olModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModType.setStatus("mandatory")


class _OlModClass_Type(Integer32):
    """Custom type olModClass based on Integer32"""
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
        *(("controller", 1),
          ("ethernet-connswitching-media", 10),
          ("ethernet-interconnect", 4),
          ("ethernet-media", 3),
          ("ethernet-mgmt", 2),
          ("ethernet-portswitching-media", 5),
          ("fddi-media", 8),
          ("fddi-mgmt", 12),
          ("terminal-server", 7),
          ("token-ring-interconnect", 11),
          ("token-ring-media", 6),
          ("token-ring-mgmt", 9))
    )


_OlModClass_Type.__name__ = "Integer32"
_OlModClass_Object = MibTableColumn
olModClass = _OlModClass_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 3),
    _OlModClass_Type()
)
olModClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModClass.setStatus("mandatory")


class _OlModDescr_Type(DisplayString):
    """Custom type olModDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_OlModDescr_Type.__name__ = "DisplayString"
_OlModDescr_Object = MibTableColumn
olModDescr = _OlModDescr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 4),
    _OlModDescr_Type()
)
olModDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModDescr.setStatus("mandatory")


class _OlModVersion_Type(DisplayString):
    """Custom type olModVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OlModVersion_Type.__name__ = "DisplayString"
_OlModVersion_Object = MibTableColumn
olModVersion = _OlModVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 5),
    _OlModVersion_Type()
)
olModVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModVersion.setStatus("mandatory")


class _OlModVendor_Type(Integer32):
    """Custom type olModVendor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("chipcom", 1),
          ("cisco", 2),
          ("datability", 5),
          ("ibm", 6),
          ("intellicom", 9),
          ("pilkington", 3),
          ("raycom", 7),
          ("retix", 8))
    )


_OlModVendor_Type.__name__ = "Integer32"
_OlModVendor_Object = MibTableColumn
olModVendor = _OlModVendor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 6),
    _OlModVendor_Type()
)
olModVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModVendor.setStatus("mandatory")


class _OlModResetModule_Type(Integer32):
    """Custom type olModResetModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_OlModResetModule_Type.__name__ = "Integer32"
_OlModResetModule_Object = MibTableColumn
olModResetModule = _OlModResetModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 7),
    _OlModResetModule_Type()
)
olModResetModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olModResetModule.setStatus("mandatory")


class _OlModConfigToDips_Type(Integer32):
    """Custom type olModConfigToDips based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configure", 2),
          ("noConfigure", 1))
    )


_OlModConfigToDips_Type.__name__ = "Integer32"
_OlModConfigToDips_Object = MibTableColumn
olModConfigToDips = _OlModConfigToDips_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 8),
    _OlModConfigToDips_Type()
)
olModConfigToDips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olModConfigToDips.setStatus("mandatory")


class _OlModConfigured_Type(Integer32):
    """Custom type olModConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("notConfigured", 1))
    )


_OlModConfigured_Type.__name__ = "Integer32"
_OlModConfigured_Object = MibTableColumn
olModConfigured = _OlModConfigured_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 9),
    _OlModConfigured_Type()
)
olModConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModConfigured.setStatus("mandatory")


class _OlModNetwork_Type(Integer32):
    """Custom type olModNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("fddi-1", 16),
          ("fddi-2", 17),
          ("fddi-3", 18),
          ("fddi-4", 19),
          ("front-panel", 5),
          ("isolated", 2),
          ("isolated-1", 21),
          ("isolated-2", 22),
          ("other", 1),
          ("per-connector", 20),
          ("port-switching", 3),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlModNetwork_Type.__name__ = "Integer32"
_OlModNetwork_Object = MibTableColumn
olModNetwork = _OlModNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 10),
    _OlModNetwork_Type()
)
olModNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olModNetwork.setStatus("mandatory")


class _OlModNetworkType_Type(Integer32):
    """Custom type olModNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 5),
          ("fddi", 7),
          ("other", 1),
          ("port-switching", 3),
          ("serial", 8),
          ("token-ring", 6))
    )


_OlModNetworkType_Type.__name__ = "Integer32"
_OlModNetworkType_Object = MibTableColumn
olModNetworkType = _OlModNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 11),
    _OlModNetworkType_Type()
)
olModNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModNetworkType.setStatus("mandatory")


class _OlModStatus_Type(Integer32):
    """Custom type olModStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("booting", 20),
          ("fatalError", 10),
          ("okay", 1),
          ("partial-failure", 21))
    )


_OlModStatus_Type.__name__ = "Integer32"
_OlModStatus_Object = MibTableColumn
olModStatus = _OlModStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 12),
    _OlModStatus_Type()
)
olModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModStatus.setStatus("mandatory")
_OlModNumPorts_Type = Integer32
_OlModNumPorts_Object = MibTableColumn
olModNumPorts = _OlModNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 13),
    _OlModNumPorts_Type()
)
olModNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModNumPorts.setStatus("mandatory")
_OlModNumTrunks_Type = Integer32
_OlModNumTrunks_Object = MibTableColumn
olModNumTrunks = _OlModNumTrunks_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 1, 1, 14),
    _OlModNumTrunks_Type()
)
olModNumTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModNumTrunks.setStatus("mandatory")
_OlPortTable_Object = MibTable
olPortTable = _OlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    olPortTable.setStatus("mandatory")
_OlPortEntry_Object = MibTableRow
olPortEntry = _OlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1)
)
olPortEntry.setIndexNames(
    (0, "CHIPCONC-MIB", "olPortSlotIndex"),
    (0, "CHIPCONC-MIB", "olPortIndex"),
)
if mibBuilder.loadTexts:
    olPortEntry.setStatus("mandatory")
_OlPortSlotIndex_Type = Integer32
_OlPortSlotIndex_Object = MibTableColumn
olPortSlotIndex = _OlPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 1),
    _OlPortSlotIndex_Type()
)
olPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortSlotIndex.setStatus("mandatory")
_OlPortIndex_Type = Integer32
_OlPortIndex_Object = MibTableColumn
olPortIndex = _OlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 2),
    _OlPortIndex_Type()
)
olPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortIndex.setStatus("mandatory")


class _OlPortType_Type(Integer32):
    """Custom type olPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("logical", 1),
          ("media", 2),
          ("virtual", 5))
    )


_OlPortType_Type.__name__ = "Integer32"
_OlPortType_Object = MibTableColumn
olPortType = _OlPortType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 3),
    _OlPortType_Type()
)
olPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortType.setStatus("mandatory")


class _OlPortConnector_Type(Integer32):
    """Custom type olPortConnector based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("backPlane", 1),
          ("bnc", 2),
          ("db-50", 6),
          ("db-9", 10),
          ("faui", 3),
          ("fddi-lc", 12),
          ("fddi-mic", 14),
          ("fddi-st", 13),
          ("fiber", 5),
          ("maui", 4),
          ("rj45", 8),
          ("rj45S", 9),
          ("telco", 7),
          ("virtual", 11))
    )


_OlPortConnector_Type.__name__ = "Integer32"
_OlPortConnector_Object = MibTableColumn
olPortConnector = _OlPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 4),
    _OlPortConnector_Type()
)
olPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortConnector.setStatus("mandatory")


class _OlPortStatus_Type(Integer32):
    """Custom type olPortStatus based on Integer32"""
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
              19,
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
        *(("backup-link", 24),
          ("beacon", 27),
          ("connecting", 23),
          ("fatalError", 10),
          ("fifoOverrun", 8),
          ("fifoUnderrun", 9),
          ("invalidData", 6),
          ("jabber", 3),
          ("linkFailure", 2),
          ("lowLight", 7),
          ("macRemoved", 29),
          ("mjlp", 12),
          ("noCable", 13),
          ("noPhantom", 15),
          ("noSquelch", 14),
          ("notInserted", 30),
          ("off", 22),
          ("okay", 1),
          ("okay-standby", 19),
          ("partition", 11),
          ("remoteJabber", 5),
          ("remoteLinkFailure", 4),
          ("security-breach", 25),
          ("speedMismatch", 31),
          ("unknownStatus", 26),
          ("wireFault", 28))
    )


_OlPortStatus_Type.__name__ = "Integer32"
_OlPortStatus_Object = MibTableColumn
olPortStatus = _OlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 5),
    _OlPortStatus_Type()
)
olPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortStatus.setStatus("mandatory")


class _OlPortAdminState_Type(Integer32):
    """Custom type olPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("local", 6),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("redundant-rfs", 5),
          ("remote", 7),
          ("remote-diagnostics", 8),
          ("unknown", 9))
    )


_OlPortAdminState_Type.__name__ = "Integer32"
_OlPortAdminState_Object = MibTableColumn
olPortAdminState = _OlPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 6),
    _OlPortAdminState_Type()
)
olPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olPortAdminState.setStatus("mandatory")


class _OlPortNetwork_Type(Integer32):
    """Custom type olPortNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("fddi-1", 16),
          ("fddi-2", 17),
          ("fddi-3", 18),
          ("fddi-4", 19),
          ("front-panel", 5),
          ("isolated", 2),
          ("isolated-1", 21),
          ("isolated-2", 22),
          ("other", 1),
          ("per-connector", 20),
          ("per-module", 4),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlPortNetwork_Type.__name__ = "Integer32"
_OlPortNetwork_Object = MibTableColumn
olPortNetwork = _OlPortNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 7),
    _OlPortNetwork_Type()
)
olPortNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olPortNetwork.setStatus("mandatory")


class _OlPortNetworkType_Type(Integer32):
    """Custom type olPortNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 5),
          ("fddi", 7),
          ("other", 1),
          ("serial", 8),
          ("token-ring", 6))
    )


_OlPortNetworkType_Type.__name__ = "Integer32"
_OlPortNetworkType_Object = MibTableColumn
olPortNetworkType = _OlPortNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 2, 1, 8),
    _OlPortNetworkType_Type()
)
olPortNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olPortNetworkType.setStatus("mandatory")
_OlTrunkTable_Object = MibTable
olTrunkTable = _OlTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    olTrunkTable.setStatus("mandatory")
_OlTrunkEntry_Object = MibTableRow
olTrunkEntry = _OlTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1)
)
olTrunkEntry.setIndexNames(
    (0, "CHIPCONC-MIB", "olTrunkSlotIndex"),
    (0, "CHIPCONC-MIB", "olTrunkIndex"),
)
if mibBuilder.loadTexts:
    olTrunkEntry.setStatus("mandatory")
_OlTrunkSlotIndex_Type = Integer32
_OlTrunkSlotIndex_Object = MibTableColumn
olTrunkSlotIndex = _OlTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 1),
    _OlTrunkSlotIndex_Type()
)
olTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkSlotIndex.setStatus("mandatory")
_OlTrunkIndex_Type = Integer32
_OlTrunkIndex_Object = MibTableColumn
olTrunkIndex = _OlTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 2),
    _OlTrunkIndex_Type()
)
olTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkIndex.setStatus("mandatory")


class _OlTrunkType_Type(Integer32):
    """Custom type olTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("backplaneIn", 6),
          ("backplaneOut", 7),
          ("other", 1),
          ("ringIn", 3),
          ("ringOut", 4))
    )


_OlTrunkType_Type.__name__ = "Integer32"
_OlTrunkType_Object = MibTableColumn
olTrunkType = _OlTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 3),
    _OlTrunkType_Type()
)
olTrunkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkType.setStatus("mandatory")


class _OlTrunkConnector_Type(Integer32):
    """Custom type olTrunkConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("backplane", 1),
          ("fiber", 5),
          ("rj45S", 9))
    )


_OlTrunkConnector_Type.__name__ = "Integer32"
_OlTrunkConnector_Object = MibTableColumn
olTrunkConnector = _OlTrunkConnector_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 4),
    _OlTrunkConnector_Type()
)
olTrunkConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkConnector.setStatus("mandatory")


class _OlTrunkStatus_Type(Integer32):
    """Custom type olTrunkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              13,
              14,
              16,
              17,
              18,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("beacon", 27),
          ("fatalError", 10),
          ("invalidConfig", 18),
          ("linkFailure", 2),
          ("lostLock", 16),
          ("noCable", 13),
          ("noSquelch", 14),
          ("okay", 1),
          ("upstreamNeighborLost", 17),
          ("wireFault", 28))
    )


_OlTrunkStatus_Type.__name__ = "Integer32"
_OlTrunkStatus_Object = MibTableColumn
olTrunkStatus = _OlTrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 5),
    _OlTrunkStatus_Type()
)
olTrunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkStatus.setStatus("mandatory")


class _OlTrunkAdminState_Type(Integer32):
    """Custom type olTrunkAdminState based on Integer32"""
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


_OlTrunkAdminState_Type.__name__ = "Integer32"
_OlTrunkAdminState_Object = MibTableColumn
olTrunkAdminState = _OlTrunkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 6),
    _OlTrunkAdminState_Type()
)
olTrunkAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olTrunkAdminState.setStatus("mandatory")


class _OlTrunkWrapState_Type(Integer32):
    """Custom type olTrunkWrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unwrapped", 2),
          ("wrapped", 1))
    )


_OlTrunkWrapState_Type.__name__ = "Integer32"
_OlTrunkWrapState_Object = MibTableColumn
olTrunkWrapState = _OlTrunkWrapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 7),
    _OlTrunkWrapState_Type()
)
olTrunkWrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkWrapState.setStatus("mandatory")


class _OlTrunkNeighbor_Type(Integer32):
    """Custom type olTrunkNeighbor based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("external", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_OlTrunkNeighbor_Type.__name__ = "Integer32"
_OlTrunkNeighbor_Object = MibTableColumn
olTrunkNeighbor = _OlTrunkNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 3, 1, 8),
    _OlTrunkNeighbor_Type()
)
olTrunkNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olTrunkNeighbor.setStatus("mandatory")
_OlSpecMods_ObjectIdentity = ObjectIdentity
olSpecMods = _OlSpecMods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4)
)
_Ol50nnMCTL_ObjectIdentity = ObjectIdentity
ol50nnMCTL = _Ol50nnMCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3)
)
_Ol51nnMMGT_ObjectIdentity = ObjectIdentity
ol51nnMMGT = _Ol51nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4)
)
_Ol51nnMFIB_ObjectIdentity = ObjectIdentity
ol51nnMFIB = _Ol51nnMFIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5)
)
_Ol51nnMUTP_ObjectIdentity = ObjectIdentity
ol51nnMUTP = _Ol51nnMUTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6)
)
_Ol51nnMTP_ObjectIdentity = ObjectIdentity
ol51nnMTP = _Ol51nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7)
)
_Ol51nnMBNC_ObjectIdentity = ObjectIdentity
ol51nnMBNC = _Ol51nnMBNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8)
)
_Ol51nnBEE_ObjectIdentity = ObjectIdentity
ol51nnBEE = _Ol51nnBEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9)
)
_Ol51nnRES_ObjectIdentity = ObjectIdentity
ol51nnRES = _Ol51nnRES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10)
)
_Ol51nnREE_ObjectIdentity = ObjectIdentity
ol51nnREE = _Ol51nnREE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11)
)
_Ol51nnMAUIF_ObjectIdentity = ObjectIdentity
ol51nnMAUIF = _Ol51nnMAUIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12)
)
_Ol51nnMAUIM_ObjectIdentity = ObjectIdentity
ol51nnMAUIM = _Ol51nnMAUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13)
)
_Ol5208MTP_ObjectIdentity = ObjectIdentity
ol5208MTP = _Ol5208MTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14)
)
_Ol51nnMFP_ObjectIdentity = ObjectIdentity
ol51nnMFP = _Ol51nnMFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15)
)
_Ol51nnMFBP_ObjectIdentity = ObjectIdentity
ol51nnMFBP = _Ol51nnMFBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16)
)
_Ol51nnMTPL_ObjectIdentity = ObjectIdentity
ol51nnMTPL = _Ol51nnMTPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17)
)
_Ol51nnMTPPL_ObjectIdentity = ObjectIdentity
ol51nnMTPPL = _Ol51nnMTPPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18)
)
_Ol52nnMTP_ObjectIdentity = ObjectIdentity
ol52nnMTP = _Ol52nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19)
)
_Ol52nnMFR_ObjectIdentity = ObjectIdentity
ol52nnMFR = _Ol52nnMFR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20)
)
_Ol51nnMTS_ObjectIdentity = ObjectIdentity
ol51nnMTS = _Ol51nnMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21)
)
_Ol51nnMFL_ObjectIdentity = ObjectIdentity
ol51nnMFL = _Ol51nnMFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22)
)
_Ol50nnMRCTL_ObjectIdentity = ObjectIdentity
ol50nnMRCTL = _Ol50nnMRCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23)
)
_Ol51nnMFB_ObjectIdentity = ObjectIdentity
ol51nnMFB = _Ol51nnMFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24)
)
_Ol53nnMMGT_ObjectIdentity = ObjectIdentity
ol53nnMMGT = _Ol53nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25)
)
_Ol53nnMFBMIC_ObjectIdentity = ObjectIdentity
ol53nnMFBMIC = _Ol53nnMFBMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26)
)
_Ol53nnMFIBST_ObjectIdentity = ObjectIdentity
ol53nnMFIBST = _Ol53nnMFIBST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27)
)
_Ol53nnMSTP_ObjectIdentity = ObjectIdentity
ol53nnMSTP = _Ol53nnMSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28)
)
_Ol51nnMTPCL_ObjectIdentity = ObjectIdentity
ol51nnMTPCL = _Ol51nnMTPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29)
)
_Ol52nnBTT_ObjectIdentity = ObjectIdentity
ol52nnBTT = _Ol52nnBTT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30)
)
_Ol51nnIx_ObjectIdentity = ObjectIdentity
ol51nnIx = _Ol51nnIx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31)
)
_Ol52nnMMGT_ObjectIdentity = ObjectIdentity
ol52nnMMGT = _Ol52nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32)
)
_Ol50nnMHCTL_ObjectIdentity = ObjectIdentity
ol50nnMHCTL = _Ol50nnMHCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33)
)
_OlModSummaryTable_Object = MibTable
olModSummaryTable = _OlModSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 5)
)
if mibBuilder.loadTexts:
    olModSummaryTable.setStatus("mandatory")
_OlModSummaryEntry_Object = MibTableRow
olModSummaryEntry = _OlModSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 5, 1)
)
olModSummaryEntry.setIndexNames(
    (0, "CHIPCONC-MIB", "olModSummarySlotIndex"),
)
if mibBuilder.loadTexts:
    olModSummaryEntry.setStatus("mandatory")
_OlModSummarySlotIndex_Type = Integer32
_OlModSummarySlotIndex_Object = MibTableColumn
olModSummarySlotIndex = _OlModSummarySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 5, 1, 1),
    _OlModSummarySlotIndex_Type()
)
olModSummarySlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModSummarySlotIndex.setStatus("mandatory")


class _OlModSummaryInfo_Type(OctetString):
    """Custom type olModSummaryInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_OlModSummaryInfo_Type.__name__ = "OctetString"
_OlModSummaryInfo_Object = MibTableColumn
olModSummaryInfo = _OlModSummaryInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 5, 1, 2),
    _OlModSummaryInfo_Type()
)
olModSummaryInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olModSummaryInfo.setStatus("mandatory")
_OlNets_ObjectIdentity = ObjectIdentity
olNets = _OlNets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5)
)
_OlNet_ObjectIdentity = ObjectIdentity
olNet = _OlNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1)
)
_OlEnet_ObjectIdentity = ObjectIdentity
olEnet = _OlEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2)
)
_OlTRnet_ObjectIdentity = ObjectIdentity
olTRnet = _OlTRnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3)
)
_OlFDDInet_ObjectIdentity = ObjectIdentity
olFDDInet = _OlFDDInet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4)
)
_OlGroups_ObjectIdentity = ObjectIdentity
olGroups = _OlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6)
)
_OlGroupPortTable_Object = MibTable
olGroupPortTable = _OlGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    olGroupPortTable.setStatus("mandatory")
_OlGroupPortEntry_Object = MibTableRow
olGroupPortEntry = _OlGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1, 1)
)
olGroupPortEntry.setIndexNames(
    (0, "CHIPCONC-MIB", "olGroupPortSlotIndex"),
    (0, "CHIPCONC-MIB", "olGroupPortIndex"),
)
if mibBuilder.loadTexts:
    olGroupPortEntry.setStatus("mandatory")
_OlGroupPortSlotIndex_Type = Integer32
_OlGroupPortSlotIndex_Object = MibTableColumn
olGroupPortSlotIndex = _OlGroupPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1, 1, 1),
    _OlGroupPortSlotIndex_Type()
)
olGroupPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupPortSlotIndex.setStatus("mandatory")
_OlGroupPortIndex_Type = Integer32
_OlGroupPortIndex_Object = MibTableColumn
olGroupPortIndex = _OlGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1, 1, 2),
    _OlGroupPortIndex_Type()
)
olGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupPortIndex.setStatus("mandatory")


class _OlGroupPortGroupID_Type(OctetString):
    """Custom type olGroupPortGroupID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OlGroupPortGroupID_Type.__name__ = "OctetString"
_OlGroupPortGroupID_Object = MibTableColumn
olGroupPortGroupID = _OlGroupPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 1, 1, 3),
    _OlGroupPortGroupID_Type()
)
olGroupPortGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupPortGroupID.setStatus("mandatory")
_OlGroupSummaryTable_Object = MibTable
olGroupSummaryTable = _OlGroupSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    olGroupSummaryTable.setStatus("mandatory")
_OlGroupSummaryEntry_Object = MibTableRow
olGroupSummaryEntry = _OlGroupSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2, 1)
)
olGroupSummaryEntry.setIndexNames(
    (0, "CHIPCONC-MIB", "olGroupSummaryGroupID"),
    (0, "CHIPCONC-MIB", "olGroupSummaryIndex"),
)
if mibBuilder.loadTexts:
    olGroupSummaryEntry.setStatus("mandatory")


class _OlGroupSummaryGroupID_Type(Integer32):
    """Custom type olGroupSummaryGroupID based on Integer32"""
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
        *(("group-1", 1),
          ("group-2", 2),
          ("group-3", 3),
          ("group-4", 4),
          ("group-5", 5),
          ("group-6", 6),
          ("group-7", 7),
          ("group-8", 8))
    )


_OlGroupSummaryGroupID_Type.__name__ = "Integer32"
_OlGroupSummaryGroupID_Object = MibTableColumn
olGroupSummaryGroupID = _OlGroupSummaryGroupID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2, 1, 1),
    _OlGroupSummaryGroupID_Type()
)
olGroupSummaryGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupSummaryGroupID.setStatus("mandatory")
_OlGroupSummaryIndex_Type = Integer32
_OlGroupSummaryIndex_Object = MibTableColumn
olGroupSummaryIndex = _OlGroupSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2, 1, 2),
    _OlGroupSummaryIndex_Type()
)
olGroupSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupSummaryIndex.setStatus("mandatory")


class _OlGroupSummaryPorts_Type(OctetString):
    """Custom type olGroupSummaryPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_OlGroupSummaryPorts_Type.__name__ = "OctetString"
_OlGroupSummaryPorts_Object = MibTableColumn
olGroupSummaryPorts = _OlGroupSummaryPorts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 2, 1, 3),
    _OlGroupSummaryPorts_Type()
)
olGroupSummaryPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olGroupSummaryPorts.setStatus("mandatory")
_OlGroupSet_ObjectIdentity = ObjectIdentity
olGroupSet = _OlGroupSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3)
)


class _OlGroupSetAction_Type(Integer32):
    """Custom type olGroupSetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add-ports", 1),
          ("clear-ports", 2),
          ("set-admin-state", 3))
    )


_OlGroupSetAction_Type.__name__ = "Integer32"
_OlGroupSetAction_Object = MibScalar
olGroupSetAction = _OlGroupSetAction_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 1),
    _OlGroupSetAction_Type()
)
olGroupSetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetAction.setStatus("mandatory")


class _OlGroupSetGroupID_Type(Integer32):
    """Custom type olGroupSetGroupID based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("all-groups", 255),
          ("group-1", 1),
          ("group-2", 2),
          ("group-3", 3),
          ("group-4", 4),
          ("group-5", 5),
          ("group-6", 6),
          ("group-7", 7),
          ("group-8", 8))
    )


_OlGroupSetGroupID_Type.__name__ = "Integer32"
_OlGroupSetGroupID_Object = MibScalar
olGroupSetGroupID = _OlGroupSetGroupID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 2),
    _OlGroupSetGroupID_Type()
)
olGroupSetGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetGroupID.setStatus("mandatory")
_OlGroupSetSlotIndex_Type = Integer32
_OlGroupSetSlotIndex_Object = MibScalar
olGroupSetSlotIndex = _OlGroupSetSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 3),
    _OlGroupSetSlotIndex_Type()
)
olGroupSetSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetSlotIndex.setStatus("mandatory")
_OlGroupSetPortIndex_Type = Integer32
_OlGroupSetPortIndex_Object = MibScalar
olGroupSetPortIndex = _OlGroupSetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 4),
    _OlGroupSetPortIndex_Type()
)
olGroupSetPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetPortIndex.setStatus("mandatory")


class _OlGroupSetAdminState_Type(Integer32):
    """Custom type olGroupSetAdminState based on Integer32"""
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


_OlGroupSetAdminState_Type.__name__ = "Integer32"
_OlGroupSetAdminState_Object = MibScalar
olGroupSetAdminState = _OlGroupSetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6, 3, 5),
    _OlGroupSetAdminState_Type()
)
olGroupSetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olGroupSetAdminState.setStatus("mandatory")
_OlAlarm_ObjectIdentity = ObjectIdentity
olAlarm = _OlAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7)
)
_OlThresh_ObjectIdentity = ObjectIdentity
olThresh = _OlThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1)
)
_OlThreshControl_ObjectIdentity = ObjectIdentity
olThreshControl = _OlThreshControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1)
)
_OlThreshTotalEntries_Type = Integer32
_OlThreshTotalEntries_Object = MibScalar
olThreshTotalEntries = _OlThreshTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1, 1),
    _OlThreshTotalEntries_Type()
)
olThreshTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshTotalEntries.setStatus("mandatory")
_OlThreshMaxEntries_Type = Integer32
_OlThreshMaxEntries_Object = MibScalar
olThreshMaxEntries = _OlThreshMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1, 2),
    _OlThreshMaxEntries_Type()
)
olThreshMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshMaxEntries.setStatus("mandatory")
_OlThreshLastCreatedIndex_Type = Integer32
_OlThreshLastCreatedIndex_Object = MibScalar
olThreshLastCreatedIndex = _OlThreshLastCreatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1, 3),
    _OlThreshLastCreatedIndex_Type()
)
olThreshLastCreatedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshLastCreatedIndex.setStatus("mandatory")


class _OlThreshAllMode_Type(Integer32):
    """Custom type olThreshAllMode based on Integer32"""
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
          ("disable", 2),
          ("enable", 1))
    )


_OlThreshAllMode_Type.__name__ = "Integer32"
_OlThreshAllMode_Object = MibScalar
olThreshAllMode = _OlThreshAllMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1, 4),
    _OlThreshAllMode_Type()
)
olThreshAllMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshAllMode.setStatus("mandatory")
_OlThreshTable_Object = MibTable
olThreshTable = _OlThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    olThreshTable.setStatus("mandatory")
_OlThreshEntry_Object = MibTableRow
olThreshEntry = _OlThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1)
)
olThreshEntry.setIndexNames(
    (0, "CHIPCONC-MIB", "olThreshIndex"),
)
if mibBuilder.loadTexts:
    olThreshEntry.setStatus("mandatory")
_OlThreshIndex_Type = Integer32
_OlThreshIndex_Object = MibTableColumn
olThreshIndex = _OlThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 1),
    _OlThreshIndex_Type()
)
olThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshIndex.setStatus("mandatory")


class _OlThreshMode_Type(Integer32):
    """Custom type olThreshMode based on Integer32"""
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
          ("disable", 2),
          ("enable", 1))
    )


_OlThreshMode_Type.__name__ = "Integer32"
_OlThreshMode_Object = MibTableColumn
olThreshMode = _OlThreshMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 2),
    _OlThreshMode_Type()
)
olThreshMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshMode.setStatus("mandatory")


class _OlThreshDescription_Type(DisplayString):
    """Custom type olThreshDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_OlThreshDescription_Type.__name__ = "DisplayString"
_OlThreshDescription_Object = MibTableColumn
olThreshDescription = _OlThreshDescription_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 3),
    _OlThreshDescription_Type()
)
olThreshDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshDescription.setStatus("mandatory")
_OlThreshObjectIdentifier_Type = ObjectIdentifier
_OlThreshObjectIdentifier_Object = MibTableColumn
olThreshObjectIdentifier = _OlThreshObjectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 4),
    _OlThreshObjectIdentifier_Type()
)
olThreshObjectIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshObjectIdentifier.setStatus("mandatory")


class _OlThreshStatCategory_Type(Integer32):
    """Custom type olThreshStatCategory based on Integer32"""
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
        *(("network", 2),
          ("other", 1),
          ("port", 3),
          ("station", 4))
    )


_OlThreshStatCategory_Type.__name__ = "Integer32"
_OlThreshStatCategory_Object = MibTableColumn
olThreshStatCategory = _OlThreshStatCategory_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 5),
    _OlThreshStatCategory_Type()
)
olThreshStatCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatCategory.setStatus("mandatory")


class _OlThreshStatType_Type(Integer32):
    """Custom type olThreshStatType based on Integer32"""
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
        *(("broadcast-frames", 4),
          ("error-frames", 6),
          ("frames", 2),
          ("multicast-frames", 5),
          ("octets", 3),
          ("other", 1),
          ("tr-net-hard-errors", 8),
          ("tr-net-soft-errors", 7))
    )


_OlThreshStatType_Type.__name__ = "Integer32"
_OlThreshStatType_Object = MibTableColumn
olThreshStatType = _OlThreshStatType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 6),
    _OlThreshStatType_Type()
)
olThreshStatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatType.setStatus("mandatory")


class _OlThreshStatNetID_Type(Integer32):
    """Custom type olThreshStatNetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("agent-network", 255),
          ("isolated", 2),
          ("other", 1),
          ("token-ring-1", 9),
          ("token-ring-2", 10),
          ("token-ring-3", 11),
          ("token-ring-4", 12),
          ("token-ring-5", 13),
          ("token-ring-6", 14),
          ("token-ring-7", 15))
    )


_OlThreshStatNetID_Type.__name__ = "Integer32"
_OlThreshStatNetID_Object = MibTableColumn
olThreshStatNetID = _OlThreshStatNetID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 7),
    _OlThreshStatNetID_Type()
)
olThreshStatNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatNetID.setStatus("mandatory")
_OlThreshStatSlotIndex_Type = Integer32
_OlThreshStatSlotIndex_Object = MibTableColumn
olThreshStatSlotIndex = _OlThreshStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 8),
    _OlThreshStatSlotIndex_Type()
)
olThreshStatSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatSlotIndex.setStatus("mandatory")
_OlThreshStatPortIndex_Type = Integer32
_OlThreshStatPortIndex_Object = MibTableColumn
olThreshStatPortIndex = _OlThreshStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 9),
    _OlThreshStatPortIndex_Type()
)
olThreshStatPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatPortIndex.setStatus("mandatory")
_OlThreshStatStationAddr_Type = MacAddress
_OlThreshStatStationAddr_Object = MibTableColumn
olThreshStatStationAddr = _OlThreshStatStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 10),
    _OlThreshStatStationAddr_Type()
)
olThreshStatStationAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshStatStationAddr.setStatus("mandatory")
_OlThreshInterval_Type = Integer32
_OlThreshInterval_Object = MibTableColumn
olThreshInterval = _OlThreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 11),
    _OlThreshInterval_Type()
)
olThreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshInterval.setStatus("mandatory")


class _OlThreshCondition_Type(Integer32):
    """Custom type olThreshCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delta-above", 1)
    )


_OlThreshCondition_Type.__name__ = "Integer32"
_OlThreshCondition_Object = MibTableColumn
olThreshCondition = _OlThreshCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 12),
    _OlThreshCondition_Type()
)
olThreshCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshCondition.setStatus("mandatory")
_OlThreshValue_Type = Integer32
_OlThreshValue_Object = MibTableColumn
olThreshValue = _OlThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 13),
    _OlThreshValue_Type()
)
olThreshValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshValue.setStatus("mandatory")
_OlThreshCurrentValue_Type = Integer32
_OlThreshCurrentValue_Object = MibTableColumn
olThreshCurrentValue = _OlThreshCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 14),
    _OlThreshCurrentValue_Type()
)
olThreshCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshCurrentValue.setStatus("mandatory")


class _OlThreshStatus_Type(Integer32):
    """Custom type olThreshStatus based on Integer32"""
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
        *(("no-statistic-specified", 1),
          ("not-yet-available", 3),
          ("statistic-not-accessible", 2),
          ("valid", 4))
    )


_OlThreshStatus_Type.__name__ = "Integer32"
_OlThreshStatus_Object = MibTableColumn
olThreshStatus = _OlThreshStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 15),
    _OlThreshStatus_Type()
)
olThreshStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshStatus.setStatus("mandatory")
_OlThreshTimeSinceLastTriggered_Type = TimeTicks
_OlThreshTimeSinceLastTriggered_Object = MibTableColumn
olThreshTimeSinceLastTriggered = _OlThreshTimeSinceLastTriggered_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 16),
    _OlThreshTimeSinceLastTriggered_Type()
)
olThreshTimeSinceLastTriggered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    olThreshTimeSinceLastTriggered.setStatus("mandatory")


class _OlThreshActionType_Type(Integer32):
    """Custom type olThreshActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("trap-only", 1)
    )


_OlThreshActionType_Type.__name__ = "Integer32"
_OlThreshActionType_Object = MibTableColumn
olThreshActionType = _OlThreshActionType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 17),
    _OlThreshActionType_Type()
)
olThreshActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshActionType.setStatus("mandatory")
_OlThreshActionData_Type = Integer32
_OlThreshActionData_Object = MibTableColumn
olThreshActionData = _OlThreshActionData_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 18),
    _OlThreshActionData_Type()
)
olThreshActionData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshActionData.setStatus("mandatory")


class _OlThreshActionPriority_Type(Integer32):
    """Custom type olThreshActionPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_OlThreshActionPriority_Type.__name__ = "Integer32"
_OlThreshActionPriority_Object = MibTableColumn
olThreshActionPriority = _OlThreshActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 2, 1, 19),
    _OlThreshActionPriority_Type()
)
olThreshActionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    olThreshActionPriority.setStatus("mandatory")
_Oebm_ObjectIdentity = ObjectIdentity
oebm = _Oebm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 2)
)
_Midnight_ObjectIdentity = ObjectIdentity
midnight = _Midnight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 3)
)
_WorkGroupHub_ObjectIdentity = ObjectIdentity
workGroupHub = _WorkGroupHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4)
)
_HubSysGroup_ObjectIdentity = ObjectIdentity
hubSysGroup = _HubSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 1)
)
_HardwareGroup_ObjectIdentity = ObjectIdentity
hardwareGroup = _HardwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 2)
)
_SoftwareGroup_ObjectIdentity = ObjectIdentity
softwareGroup = _SoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 3)
)
_HubGroup_ObjectIdentity = ObjectIdentity
hubGroup = _HubGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 4)
)
_BoardGroup_ObjectIdentity = ObjectIdentity
boardGroup = _BoardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 5)
)
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 6)
)
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 7)
)
_Emm_ObjectIdentity = ObjectIdentity
emm = _Emm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 5)
)
_ChipBridge_ObjectIdentity = ObjectIdentity
chipBridge = _ChipBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 6)
)
_Trmm_ObjectIdentity = ObjectIdentity
trmm = _Trmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 7)
)
_Fmm_ObjectIdentity = ObjectIdentity
fmm = _Fmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 8)
)
_Focus1_ObjectIdentity = ObjectIdentity
focus1 = _Focus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 9)
)
_Oeim_ObjectIdentity = ObjectIdentity
oeim = _Oeim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 10)
)
_ChipExperiment_ObjectIdentity = ObjectIdentity
chipExperiment = _ChipExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4)
)
_ChipExpTokenRing_ObjectIdentity = ObjectIdentity
chipExpTokenRing = _ChipExpTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1)
)
_Dot5_ObjectIdentity = ObjectIdentity
dot5 = _Dot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1)
)
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14)
)
_ChipTTY_ObjectIdentity = ObjectIdentity
chipTTY = _ChipTTY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 5)
)
_ChipTFTP_ObjectIdentity = ObjectIdentity
chipTFTP = _ChipTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 6)
)
_ChipDownload_ObjectIdentity = ObjectIdentity
chipDownload = _ChipDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHIPCONC-MIB",
    **{"MacAddress": MacAddress,
       "chipcom": chipcom,
       "chipmib02": chipmib02,
       "chipGen": chipGen,
       "chipEcho": chipEcho,
       "chipProducts": chipProducts,
       "online": online,
       "olAgents": olAgents,
       "olAgentsMySlot": olAgentsMySlot,
       "olAgentsMasterReset": olAgentsMasterReset,
       "olAgentsTable": olAgentsTable,
       "olAgentsEntry": olAgentsEntry,
       "olAgentsSlotIndex": olAgentsSlotIndex,
       "olAgentsStationAddr": olAgentsStationAddr,
       "olAgentsIpAddress": olAgentsIpAddress,
       "olAgentsMasterStatus": olAgentsMasterStatus,
       "olAgentsMasterPriority": olAgentsMasterPriority,
       "olConc": olConc,
       "olConcType": olConcType,
       "olConcReset": olConcReset,
       "olConcNumSlots": olConcNumSlots,
       "olConcProfile": olConcProfile,
       "olEnv": olEnv,
       "olEnvTempStatus": olEnvTempStatus,
       "olEnvPSCapacity": olEnvPSCapacity,
       "olEnvPSTable": olEnvPSTable,
       "olEnvPSEntry": olEnvPSEntry,
       "olEnvPSIndex": olEnvPSIndex,
       "olEnvPSAdminState": olEnvPSAdminState,
       "olEnvPSOperStatus": olEnvPSOperStatus,
       "olEnvFanStatus": olEnvFanStatus,
       "olModules": olModules,
       "olModTable": olModTable,
       "olModEntry": olModEntry,
       "olModSlotIndex": olModSlotIndex,
       "olModType": olModType,
       "olModClass": olModClass,
       "olModDescr": olModDescr,
       "olModVersion": olModVersion,
       "olModVendor": olModVendor,
       "olModResetModule": olModResetModule,
       "olModConfigToDips": olModConfigToDips,
       "olModConfigured": olModConfigured,
       "olModNetwork": olModNetwork,
       "olModNetworkType": olModNetworkType,
       "olModStatus": olModStatus,
       "olModNumPorts": olModNumPorts,
       "olModNumTrunks": olModNumTrunks,
       "olPortTable": olPortTable,
       "olPortEntry": olPortEntry,
       "olPortSlotIndex": olPortSlotIndex,
       "olPortIndex": olPortIndex,
       "olPortType": olPortType,
       "olPortConnector": olPortConnector,
       "olPortStatus": olPortStatus,
       "olPortAdminState": olPortAdminState,
       "olPortNetwork": olPortNetwork,
       "olPortNetworkType": olPortNetworkType,
       "olTrunkTable": olTrunkTable,
       "olTrunkEntry": olTrunkEntry,
       "olTrunkSlotIndex": olTrunkSlotIndex,
       "olTrunkIndex": olTrunkIndex,
       "olTrunkType": olTrunkType,
       "olTrunkConnector": olTrunkConnector,
       "olTrunkStatus": olTrunkStatus,
       "olTrunkAdminState": olTrunkAdminState,
       "olTrunkWrapState": olTrunkWrapState,
       "olTrunkNeighbor": olTrunkNeighbor,
       "olSpecMods": olSpecMods,
       "ol50nnMCTL": ol50nnMCTL,
       "ol51nnMMGT": ol51nnMMGT,
       "ol51nnMFIB": ol51nnMFIB,
       "ol51nnMUTP": ol51nnMUTP,
       "ol51nnMTP": ol51nnMTP,
       "ol51nnMBNC": ol51nnMBNC,
       "ol51nnBEE": ol51nnBEE,
       "ol51nnRES": ol51nnRES,
       "ol51nnREE": ol51nnREE,
       "ol51nnMAUIF": ol51nnMAUIF,
       "ol51nnMAUIM": ol51nnMAUIM,
       "ol5208MTP": ol5208MTP,
       "ol51nnMFP": ol51nnMFP,
       "ol51nnMFBP": ol51nnMFBP,
       "ol51nnMTPL": ol51nnMTPL,
       "ol51nnMTPPL": ol51nnMTPPL,
       "ol52nnMTP": ol52nnMTP,
       "ol52nnMFR": ol52nnMFR,
       "ol51nnMTS": ol51nnMTS,
       "ol51nnMFL": ol51nnMFL,
       "ol50nnMRCTL": ol50nnMRCTL,
       "ol51nnMFB": ol51nnMFB,
       "ol53nnMMGT": ol53nnMMGT,
       "ol53nnMFBMIC": ol53nnMFBMIC,
       "ol53nnMFIBST": ol53nnMFIBST,
       "ol53nnMSTP": ol53nnMSTP,
       "ol51nnMTPCL": ol51nnMTPCL,
       "ol52nnBTT": ol52nnBTT,
       "ol51nnIx": ol51nnIx,
       "ol52nnMMGT": ol52nnMMGT,
       "ol50nnMHCTL": ol50nnMHCTL,
       "olModSummaryTable": olModSummaryTable,
       "olModSummaryEntry": olModSummaryEntry,
       "olModSummarySlotIndex": olModSummarySlotIndex,
       "olModSummaryInfo": olModSummaryInfo,
       "olNets": olNets,
       "olNet": olNet,
       "olEnet": olEnet,
       "olTRnet": olTRnet,
       "olFDDInet": olFDDInet,
       "olGroups": olGroups,
       "olGroupPortTable": olGroupPortTable,
       "olGroupPortEntry": olGroupPortEntry,
       "olGroupPortSlotIndex": olGroupPortSlotIndex,
       "olGroupPortIndex": olGroupPortIndex,
       "olGroupPortGroupID": olGroupPortGroupID,
       "olGroupSummaryTable": olGroupSummaryTable,
       "olGroupSummaryEntry": olGroupSummaryEntry,
       "olGroupSummaryGroupID": olGroupSummaryGroupID,
       "olGroupSummaryIndex": olGroupSummaryIndex,
       "olGroupSummaryPorts": olGroupSummaryPorts,
       "olGroupSet": olGroupSet,
       "olGroupSetAction": olGroupSetAction,
       "olGroupSetGroupID": olGroupSetGroupID,
       "olGroupSetSlotIndex": olGroupSetSlotIndex,
       "olGroupSetPortIndex": olGroupSetPortIndex,
       "olGroupSetAdminState": olGroupSetAdminState,
       "olAlarm": olAlarm,
       "olThresh": olThresh,
       "olThreshControl": olThreshControl,
       "olThreshTotalEntries": olThreshTotalEntries,
       "olThreshMaxEntries": olThreshMaxEntries,
       "olThreshLastCreatedIndex": olThreshLastCreatedIndex,
       "olThreshAllMode": olThreshAllMode,
       "olThreshTable": olThreshTable,
       "olThreshEntry": olThreshEntry,
       "olThreshIndex": olThreshIndex,
       "olThreshMode": olThreshMode,
       "olThreshDescription": olThreshDescription,
       "olThreshObjectIdentifier": olThreshObjectIdentifier,
       "olThreshStatCategory": olThreshStatCategory,
       "olThreshStatType": olThreshStatType,
       "olThreshStatNetID": olThreshStatNetID,
       "olThreshStatSlotIndex": olThreshStatSlotIndex,
       "olThreshStatPortIndex": olThreshStatPortIndex,
       "olThreshStatStationAddr": olThreshStatStationAddr,
       "olThreshInterval": olThreshInterval,
       "olThreshCondition": olThreshCondition,
       "olThreshValue": olThreshValue,
       "olThreshCurrentValue": olThreshCurrentValue,
       "olThreshStatus": olThreshStatus,
       "olThreshTimeSinceLastTriggered": olThreshTimeSinceLastTriggered,
       "olThreshActionType": olThreshActionType,
       "olThreshActionData": olThreshActionData,
       "olThreshActionPriority": olThreshActionPriority,
       "oebm": oebm,
       "midnight": midnight,
       "workGroupHub": workGroupHub,
       "hubSysGroup": hubSysGroup,
       "hardwareGroup": hardwareGroup,
       "softwareGroup": softwareGroup,
       "hubGroup": hubGroup,
       "boardGroup": boardGroup,
       "portGroup": portGroup,
       "alarmGroup": alarmGroup,
       "emm": emm,
       "chipBridge": chipBridge,
       "trmm": trmm,
       "fmm": fmm,
       "focus1": focus1,
       "oeim": oeim,
       "chipExperiment": chipExperiment,
       "chipExpTokenRing": chipExpTokenRing,
       "dot5": dot5,
       "dot1dBridge": dot1dBridge,
       "chipTTY": chipTTY,
       "chipTFTP": chipTFTP,
       "chipDownload": chipDownload}
)
