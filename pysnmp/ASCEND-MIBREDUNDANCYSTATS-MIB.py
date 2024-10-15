# SNMP MIB module (ASCEND-MIBREDUNDANCYSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBREDUNDANCYSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:07 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibredundancyStatsProfile_ObjectIdentity = ObjectIdentity
mibredundancyStatsProfile = _MibredundancyStatsProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 17)
)
_MibredundancyStatsProfileTable_Object = MibTable
mibredundancyStatsProfileTable = _MibredundancyStatsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 1)
)
if mibBuilder.loadTexts:
    mibredundancyStatsProfileTable.setStatus("mandatory")
_MibredundancyStatsProfileEntry_Object = MibTableRow
mibredundancyStatsProfileEntry = _MibredundancyStatsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 1, 1)
)
mibredundancyStatsProfileEntry.setIndexNames(
    (0, "ASCEND-MIBREDUNDANCYSTATS-MIB", "redundancyStatsProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibredundancyStatsProfileEntry.setStatus("mandatory")
_RedundancyStatsProfile_Index_o_Type = Integer32
_RedundancyStatsProfile_Index_o_Object = MibScalar
redundancyStatsProfile_Index_o = _RedundancyStatsProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 1, 1, 1),
    _RedundancyStatsProfile_Index_o_Type()
)
redundancyStatsProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_Index_o.setStatus("mandatory")


class _RedundancyStatsProfile_Action_o_Type(Integer32):
    """Custom type redundancyStatsProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_RedundancyStatsProfile_Action_o_Type.__name__ = "Integer32"
_RedundancyStatsProfile_Action_o_Object = MibScalar
redundancyStatsProfile_Action_o = _RedundancyStatsProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 1, 1, 2),
    _RedundancyStatsProfile_Action_o_Type()
)
redundancyStatsProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyStatsProfile_Action_o.setStatus("mandatory")
_MibredundancyStatsProfile_ContextStatsTable_Object = MibTable
mibredundancyStatsProfile_ContextStatsTable = _MibredundancyStatsProfile_ContextStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2)
)
if mibBuilder.loadTexts:
    mibredundancyStatsProfile_ContextStatsTable.setStatus("mandatory")
_MibredundancyStatsProfile_ContextStatsEntry_Object = MibTableRow
mibredundancyStatsProfile_ContextStatsEntry = _MibredundancyStatsProfile_ContextStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1)
)
mibredundancyStatsProfile_ContextStatsEntry.setIndexNames(
    (0, "ASCEND-MIBREDUNDANCYSTATS-MIB", "redundancyStatsProfile-ContextStats-Index-o"),
    (0, "ASCEND-MIBREDUNDANCYSTATS-MIB", "redundancyStatsProfile-ContextStats-Index1-o"),
)
if mibBuilder.loadTexts:
    mibredundancyStatsProfile_ContextStatsEntry.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_Index_o_Type = Integer32
_RedundancyStatsProfile_ContextStats_Index_o_Object = MibScalar
redundancyStatsProfile_ContextStats_Index_o = _RedundancyStatsProfile_ContextStats_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 1),
    _RedundancyStatsProfile_ContextStats_Index_o_Type()
)
redundancyStatsProfile_ContextStats_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_Index_o.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_Index1_o_Type = Integer32
_RedundancyStatsProfile_ContextStats_Index1_o_Object = MibScalar
redundancyStatsProfile_ContextStats_Index1_o = _RedundancyStatsProfile_ContextStats_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 2),
    _RedundancyStatsProfile_ContextStats_Index1_o_Type()
)
redundancyStatsProfile_ContextStats_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_Index1_o.setStatus("mandatory")


class _RedundancyStatsProfile_ContextStats_State_Type(Integer32):
    """Custom type redundancyStatsProfile_ContextStats_State based on Integer32"""
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
        *(("dead", 13),
          ("inauguration", 8),
          ("initial", 1),
          ("loadContext", 2),
          ("loading", 10),
          ("localPost", 4),
          ("monitoring", 12),
          ("primaryToOperational", 9),
          ("remotePost", 5),
          ("restrictRedundancy", 14),
          ("secondaryToOperational", 11),
          ("selecting", 6),
          ("selectionComplete", 7),
          ("startPost", 3))
    )


_RedundancyStatsProfile_ContextStats_State_Type.__name__ = "Integer32"
_RedundancyStatsProfile_ContextStats_State_Object = MibScalar
redundancyStatsProfile_ContextStats_State = _RedundancyStatsProfile_ContextStats_State_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 3),
    _RedundancyStatsProfile_ContextStats_State_Type()
)
redundancyStatsProfile_ContextStats_State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_State.setStatus("mandatory")


class _RedundancyStatsProfile_ContextStats_Function_Type(Integer32):
    """Custom type redundancyStatsProfile_ContextStats_Function based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noFunction", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_RedundancyStatsProfile_ContextStats_Function_Type.__name__ = "Integer32"
_RedundancyStatsProfile_ContextStats_Function_Object = MibScalar
redundancyStatsProfile_ContextStats_Function = _RedundancyStatsProfile_ContextStats_Function_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 4),
    _RedundancyStatsProfile_ContextStats_Function_Type()
)
redundancyStatsProfile_ContextStats_Function.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_Function.setStatus("mandatory")


class _RedundancyStatsProfile_ContextStats_SelectReason_Type(Integer32):
    """Custom type redundancyStatsProfile_ContextStats_SelectReason based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("communicationLoss", 32),
          ("contentionResolution", 30),
          ("deferToRunningPrimary", 2),
          ("localCrash", 7),
          ("localCrashHistory", 22),
          ("localLocalLocalError", 9),
          ("localLocalLocalErrorHistory", 24),
          ("localMatchesChassis", 13),
          ("localPrimaryPreference", 5),
          ("localPrimaryResources", 16),
          ("localRemoteLocalError", 11),
          ("localRemoteLocalErrorHistory", 26),
          ("localSecondaryResources", 18),
          ("localSlotNumber", 28),
          ("noReason", 1),
          ("noRunningPrimary", 3),
          ("priorLocalPrimary", 20),
          ("priorPairFunction", 15),
          ("priorRemotePrimary", 21),
          ("remoteCrash", 8),
          ("remoteCrashHistory", 23),
          ("remoteLocalLocalError", 10),
          ("remoteLocalLocalErrorHistory", 25),
          ("remoteMatchesChassis", 14),
          ("remotePrimaryPreference", 6),
          ("remotePrimaryResources", 17),
          ("remoteRemoteLocalError", 12),
          ("remoteRemoteLocalErrorHistory", 27),
          ("remoteSecondaryResources", 19),
          ("remoteSlotNumber", 29),
          ("singleControllerOperation", 4),
          ("unableToAcquireBuses", 31))
    )


_RedundancyStatsProfile_ContextStats_SelectReason_Type.__name__ = "Integer32"
_RedundancyStatsProfile_ContextStats_SelectReason_Object = MibScalar
redundancyStatsProfile_ContextStats_SelectReason = _RedundancyStatsProfile_ContextStats_SelectReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 5),
    _RedundancyStatsProfile_ContextStats_SelectReason_Type()
)
redundancyStatsProfile_ContextStats_SelectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_SelectReason.setStatus("mandatory")


class _RedundancyStatsProfile_ContextStats_PriorFunction_Type(Integer32):
    """Custom type redundancyStatsProfile_ContextStats_PriorFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noFunction", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_RedundancyStatsProfile_ContextStats_PriorFunction_Type.__name__ = "Integer32"
_RedundancyStatsProfile_ContextStats_PriorFunction_Object = MibScalar
redundancyStatsProfile_ContextStats_PriorFunction = _RedundancyStatsProfile_ContextStats_PriorFunction_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 6),
    _RedundancyStatsProfile_ContextStats_PriorFunction_Type()
)
redundancyStatsProfile_ContextStats_PriorFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_PriorFunction.setStatus("mandatory")


class _RedundancyStatsProfile_ContextStats_LastReboot_Type(Integer32):
    """Custom type redundancyStatsProfile_ContextStats_LastReboot based on Integer32"""
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
        *(("crash", 1),
          ("localManualReboot", 6),
          ("localReportLocalError", 2),
          ("localReportRemoteError", 4),
          ("numberOfRebootTypes", 9),
          ("primaryOperationalReboot", 10),
          ("redundantControllerSwitchCmd", 8),
          ("remoteManualReboot", 7),
          ("remoteReportLocalError", 3),
          ("remoteReportRemoteError", 5),
          ("secondaryOperationalReboot", 11))
    )


_RedundancyStatsProfile_ContextStats_LastReboot_Type.__name__ = "Integer32"
_RedundancyStatsProfile_ContextStats_LastReboot_Object = MibScalar
redundancyStatsProfile_ContextStats_LastReboot = _RedundancyStatsProfile_ContextStats_LastReboot_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 7),
    _RedundancyStatsProfile_ContextStats_LastReboot_Type()
)
redundancyStatsProfile_ContextStats_LastReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_LastReboot.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_Local_SerialNumber_Type = Integer32
_RedundancyStatsProfile_ContextStats_Local_SerialNumber_Object = MibScalar
redundancyStatsProfile_ContextStats_Local_SerialNumber = _RedundancyStatsProfile_ContextStats_Local_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 8),
    _RedundancyStatsProfile_ContextStats_Local_SerialNumber_Type()
)
redundancyStatsProfile_ContextStats_Local_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_Local_SerialNumber.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_Pair_SerialNumber_Type = Integer32
_RedundancyStatsProfile_ContextStats_Pair_SerialNumber_Object = MibScalar
redundancyStatsProfile_ContextStats_Pair_SerialNumber = _RedundancyStatsProfile_ContextStats_Pair_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 9),
    _RedundancyStatsProfile_ContextStats_Pair_SerialNumber_Type()
)
redundancyStatsProfile_ContextStats_Pair_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_Pair_SerialNumber.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_ChassisSerialNumber_Type = Integer32
_RedundancyStatsProfile_ContextStats_ChassisSerialNumber_Object = MibScalar
redundancyStatsProfile_ContextStats_ChassisSerialNumber = _RedundancyStatsProfile_ContextStats_ChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 11),
    _RedundancyStatsProfile_ContextStats_ChassisSerialNumber_Type()
)
redundancyStatsProfile_ContextStats_ChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_ChassisSerialNumber.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_InitializationTime_Type = Integer32
_RedundancyStatsProfile_ContextStats_InitializationTime_Object = MibScalar
redundancyStatsProfile_ContextStats_InitializationTime = _RedundancyStatsProfile_ContextStats_InitializationTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 12),
    _RedundancyStatsProfile_ContextStats_InitializationTime_Type()
)
redundancyStatsProfile_ContextStats_InitializationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_InitializationTime.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_PostStart_Type = Integer32
_RedundancyStatsProfile_ContextStats_PostStart_Object = MibScalar
redundancyStatsProfile_ContextStats_PostStart = _RedundancyStatsProfile_ContextStats_PostStart_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 13),
    _RedundancyStatsProfile_ContextStats_PostStart_Type()
)
redundancyStatsProfile_ContextStats_PostStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_PostStart.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_PostEnd_Type = Integer32
_RedundancyStatsProfile_ContextStats_PostEnd_Object = MibScalar
redundancyStatsProfile_ContextStats_PostEnd = _RedundancyStatsProfile_ContextStats_PostEnd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 14),
    _RedundancyStatsProfile_ContextStats_PostEnd_Type()
)
redundancyStatsProfile_ContextStats_PostEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_PostEnd.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_SelectionStart_Type = Integer32
_RedundancyStatsProfile_ContextStats_SelectionStart_Object = MibScalar
redundancyStatsProfile_ContextStats_SelectionStart = _RedundancyStatsProfile_ContextStats_SelectionStart_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 15),
    _RedundancyStatsProfile_ContextStats_SelectionStart_Type()
)
redundancyStatsProfile_ContextStats_SelectionStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_SelectionStart.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_SelectionEnd_Type = Integer32
_RedundancyStatsProfile_ContextStats_SelectionEnd_Object = MibScalar
redundancyStatsProfile_ContextStats_SelectionEnd = _RedundancyStatsProfile_ContextStats_SelectionEnd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 16),
    _RedundancyStatsProfile_ContextStats_SelectionEnd_Type()
)
redundancyStatsProfile_ContextStats_SelectionEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_SelectionEnd.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_LoadStart_Type = Integer32
_RedundancyStatsProfile_ContextStats_LoadStart_Object = MibScalar
redundancyStatsProfile_ContextStats_LoadStart = _RedundancyStatsProfile_ContextStats_LoadStart_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 17),
    _RedundancyStatsProfile_ContextStats_LoadStart_Type()
)
redundancyStatsProfile_ContextStats_LoadStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_LoadStart.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_LoadEnd_Type = Integer32
_RedundancyStatsProfile_ContextStats_LoadEnd_Object = MibScalar
redundancyStatsProfile_ContextStats_LoadEnd = _RedundancyStatsProfile_ContextStats_LoadEnd_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 18),
    _RedundancyStatsProfile_ContextStats_LoadEnd_Type()
)
redundancyStatsProfile_ContextStats_LoadEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_LoadEnd.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_InaugurationTime_Type = Integer32
_RedundancyStatsProfile_ContextStats_InaugurationTime_Object = MibScalar
redundancyStatsProfile_ContextStats_InaugurationTime = _RedundancyStatsProfile_ContextStats_InaugurationTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 19),
    _RedundancyStatsProfile_ContextStats_InaugurationTime_Type()
)
redundancyStatsProfile_ContextStats_InaugurationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_InaugurationTime.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_LastSent_Type = Integer32
_RedundancyStatsProfile_ContextStats_LastSent_Object = MibScalar
redundancyStatsProfile_ContextStats_LastSent = _RedundancyStatsProfile_ContextStats_LastSent_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 20),
    _RedundancyStatsProfile_ContextStats_LastSent_Type()
)
redundancyStatsProfile_ContextStats_LastSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_LastSent.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_LastReceived_Type = Integer32
_RedundancyStatsProfile_ContextStats_LastReceived_Object = MibScalar
redundancyStatsProfile_ContextStats_LastReceived = _RedundancyStatsProfile_ContextStats_LastReceived_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 21),
    _RedundancyStatsProfile_ContextStats_LastReceived_Type()
)
redundancyStatsProfile_ContextStats_LastReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_LastReceived.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_LastProfileSync_Type = Integer32
_RedundancyStatsProfile_ContextStats_LastProfileSync_Object = MibScalar
redundancyStatsProfile_ContextStats_LastProfileSync = _RedundancyStatsProfile_ContextStats_LastProfileSync_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 22),
    _RedundancyStatsProfile_ContextStats_LastProfileSync_Type()
)
redundancyStatsProfile_ContextStats_LastProfileSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_LastProfileSync.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_LastCodeSync_Type = Integer32
_RedundancyStatsProfile_ContextStats_LastCodeSync_Object = MibScalar
redundancyStatsProfile_ContextStats_LastCodeSync = _RedundancyStatsProfile_ContextStats_LastCodeSync_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 23),
    _RedundancyStatsProfile_ContextStats_LastCodeSync_Type()
)
redundancyStatsProfile_ContextStats_LastCodeSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_LastCodeSync.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_LastLogRecv_Type = Integer32
_RedundancyStatsProfile_ContextStats_LastLogRecv_Object = MibScalar
redundancyStatsProfile_ContextStats_LastLogRecv = _RedundancyStatsProfile_ContextStats_LastLogRecv_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 24),
    _RedundancyStatsProfile_ContextStats_LastLogRecv_Type()
)
redundancyStatsProfile_ContextStats_LastLogRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_LastLogRecv.setStatus("mandatory")
_RedundancyStatsProfile_ContextStats_UpdateTime_Type = Integer32
_RedundancyStatsProfile_ContextStats_UpdateTime_Object = MibScalar
redundancyStatsProfile_ContextStats_UpdateTime = _RedundancyStatsProfile_ContextStats_UpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 17, 2, 1, 25),
    _RedundancyStatsProfile_ContextStats_UpdateTime_Type()
)
redundancyStatsProfile_ContextStats_UpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatsProfile_ContextStats_UpdateTime.setStatus("mandatory")
_MibredundancyStatistics_ObjectIdentity = ObjectIdentity
mibredundancyStatistics = _MibredundancyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 104)
)
_MibredundancyStatisticsTable_Object = MibTable
mibredundancyStatisticsTable = _MibredundancyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 104, 1)
)
if mibBuilder.loadTexts:
    mibredundancyStatisticsTable.setStatus("mandatory")
_MibredundancyStatisticsEntry_Object = MibTableRow
mibredundancyStatisticsEntry = _MibredundancyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 104, 1, 1)
)
mibredundancyStatisticsEntry.setIndexNames(
    (0, "ASCEND-MIBREDUNDANCYSTATS-MIB", "redundancyStatistics-Index-o"),
)
if mibBuilder.loadTexts:
    mibredundancyStatisticsEntry.setStatus("mandatory")
_RedundancyStatistics_Index_o_Type = Integer32
_RedundancyStatistics_Index_o_Object = MibScalar
redundancyStatistics_Index_o = _RedundancyStatistics_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 104, 1, 1, 1),
    _RedundancyStatistics_Index_o_Type()
)
redundancyStatistics_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatistics_Index_o.setStatus("mandatory")
_RedundancyStatistics_SerialNumber_Type = Integer32
_RedundancyStatistics_SerialNumber_Object = MibScalar
redundancyStatistics_SerialNumber = _RedundancyStatistics_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 104, 1, 1, 2),
    _RedundancyStatistics_SerialNumber_Type()
)
redundancyStatistics_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatistics_SerialNumber.setStatus("mandatory")


class _RedundancyStatistics_Action_o_Type(Integer32):
    """Custom type redundancyStatistics_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_RedundancyStatistics_Action_o_Type.__name__ = "Integer32"
_RedundancyStatistics_Action_o_Object = MibScalar
redundancyStatistics_Action_o = _RedundancyStatistics_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 104, 1, 1, 3),
    _RedundancyStatistics_Action_o_Type()
)
redundancyStatistics_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyStatistics_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBREDUNDANCYSTATS-MIB",
    **{"DisplayString": DisplayString,
       "mibredundancyStatsProfile": mibredundancyStatsProfile,
       "mibredundancyStatsProfileTable": mibredundancyStatsProfileTable,
       "mibredundancyStatsProfileEntry": mibredundancyStatsProfileEntry,
       "redundancyStatsProfile-Index-o": redundancyStatsProfile_Index_o,
       "redundancyStatsProfile-Action-o": redundancyStatsProfile_Action_o,
       "mibredundancyStatsProfile-ContextStatsTable": mibredundancyStatsProfile_ContextStatsTable,
       "mibredundancyStatsProfile-ContextStatsEntry": mibredundancyStatsProfile_ContextStatsEntry,
       "redundancyStatsProfile-ContextStats-Index-o": redundancyStatsProfile_ContextStats_Index_o,
       "redundancyStatsProfile-ContextStats-Index1-o": redundancyStatsProfile_ContextStats_Index1_o,
       "redundancyStatsProfile-ContextStats-State": redundancyStatsProfile_ContextStats_State,
       "redundancyStatsProfile-ContextStats-Function": redundancyStatsProfile_ContextStats_Function,
       "redundancyStatsProfile-ContextStats-SelectReason": redundancyStatsProfile_ContextStats_SelectReason,
       "redundancyStatsProfile-ContextStats-PriorFunction": redundancyStatsProfile_ContextStats_PriorFunction,
       "redundancyStatsProfile-ContextStats-LastReboot": redundancyStatsProfile_ContextStats_LastReboot,
       "redundancyStatsProfile-ContextStats-Local-SerialNumber": redundancyStatsProfile_ContextStats_Local_SerialNumber,
       "redundancyStatsProfile-ContextStats-Pair-SerialNumber": redundancyStatsProfile_ContextStats_Pair_SerialNumber,
       "redundancyStatsProfile-ContextStats-ChassisSerialNumber": redundancyStatsProfile_ContextStats_ChassisSerialNumber,
       "redundancyStatsProfile-ContextStats-InitializationTime": redundancyStatsProfile_ContextStats_InitializationTime,
       "redundancyStatsProfile-ContextStats-PostStart": redundancyStatsProfile_ContextStats_PostStart,
       "redundancyStatsProfile-ContextStats-PostEnd": redundancyStatsProfile_ContextStats_PostEnd,
       "redundancyStatsProfile-ContextStats-SelectionStart": redundancyStatsProfile_ContextStats_SelectionStart,
       "redundancyStatsProfile-ContextStats-SelectionEnd": redundancyStatsProfile_ContextStats_SelectionEnd,
       "redundancyStatsProfile-ContextStats-LoadStart": redundancyStatsProfile_ContextStats_LoadStart,
       "redundancyStatsProfile-ContextStats-LoadEnd": redundancyStatsProfile_ContextStats_LoadEnd,
       "redundancyStatsProfile-ContextStats-InaugurationTime": redundancyStatsProfile_ContextStats_InaugurationTime,
       "redundancyStatsProfile-ContextStats-LastSent": redundancyStatsProfile_ContextStats_LastSent,
       "redundancyStatsProfile-ContextStats-LastReceived": redundancyStatsProfile_ContextStats_LastReceived,
       "redundancyStatsProfile-ContextStats-LastProfileSync": redundancyStatsProfile_ContextStats_LastProfileSync,
       "redundancyStatsProfile-ContextStats-LastCodeSync": redundancyStatsProfile_ContextStats_LastCodeSync,
       "redundancyStatsProfile-ContextStats-LastLogRecv": redundancyStatsProfile_ContextStats_LastLogRecv,
       "redundancyStatsProfile-ContextStats-UpdateTime": redundancyStatsProfile_ContextStats_UpdateTime,
       "mibredundancyStatistics": mibredundancyStatistics,
       "mibredundancyStatisticsTable": mibredundancyStatisticsTable,
       "mibredundancyStatisticsEntry": mibredundancyStatisticsEntry,
       "redundancyStatistics-Index-o": redundancyStatistics_Index_o,
       "redundancyStatistics-SerialNumber": redundancyStatistics_SerialNumber,
       "redundancyStatistics-Action-o": redundancyStatistics_Action_o}
)
