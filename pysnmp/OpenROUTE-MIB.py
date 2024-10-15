# SNMP MIB module (OpenROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OpenROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:55 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(proElsTrapEvent,
 proElsTrapSeqs,
 proElsTrapSubSystem) = mibBuilder.importSymbols(
    "PROTEON-MIB",
    "proElsTrapEvent",
    "proElsTrapSeqs",
    "proElsTrapSubSystem")

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



class ProElsMsgLogLevel(Integer32):
    """Custom type ProElsMsgLogLevel based on Integer32"""
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
        *(("other", 1),
          ("proMsgLevelAll", 16),
          ("proMsgLevelAlways", 14),
          ("proMsgLevelCEError", 5),
          ("proMsgLevelCIError", 3),
          ("proMsgLevelCInfo", 8),
          ("proMsgLevelCTrace", 12),
          ("proMsgLevelError", 6),
          ("proMsgLevelInfo", 9),
          ("proMsgLevelPTrace", 10),
          ("proMsgLevelStandard", 15),
          ("proMsgLevelTrace", 13),
          ("proMsgLevelUEError", 4),
          ("proMsgLevelUIError", 2),
          ("proMsgLevelUInfo", 7),
          ("proMsgLevelUTrace", 11))
    )





class ProElsLogStatus(Integer32):
    """Custom type ProElsLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proElsLogDisabled", 1),
          ("proElsLogEnabled", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Proteon_ObjectIdentity = ObjectIdentity
proteon = _Proteon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1)
)
_ProAdmin_ObjectIdentity = ObjectIdentity
proAdmin = _ProAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1)
)
_ProSysObjId_ObjectIdentity = ObjectIdentity
proSysObjId = _ProSysObjId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1)
)
_ProElsTrapVar1_ObjectIdentity = ObjectIdentity
proElsTrapVar1 = _ProElsTrapVar1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 5)
)
_ProElsTrapVar2_ObjectIdentity = ObjectIdentity
proElsTrapVar2 = _ProElsTrapVar2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 6)
)
_ProElsTrapVar3_ObjectIdentity = ObjectIdentity
proElsTrapVar3 = _ProElsTrapVar3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 7)
)
_ProElsTrapVar4_ObjectIdentity = ObjectIdentity
proElsTrapVar4 = _ProElsTrapVar4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 8)
)
_ProElsTrapVar5_ObjectIdentity = ObjectIdentity
proElsTrapVar5 = _ProElsTrapVar5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 9)
)
_ProElsTrapVar6_ObjectIdentity = ObjectIdentity
proElsTrapVar6 = _ProElsTrapVar6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 10)
)
_ProElsTrapVar7_ObjectIdentity = ObjectIdentity
proElsTrapVar7 = _ProElsTrapVar7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 11)
)
_ProElsTrapVar8_ObjectIdentity = ObjectIdentity
proElsTrapVar8 = _ProElsTrapVar8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 12)
)
_ProElsTrapVar9_ObjectIdentity = ObjectIdentity
proElsTrapVar9 = _ProElsTrapVar9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 13)
)
_ProSysObjIdP4100_ObjectIdentity = ObjectIdentity
proSysObjIdP4100 = _ProSysObjIdP4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 41)
)
_ProSysObjIdP4200_ObjectIdentity = ObjectIdentity
proSysObjIdP4200 = _ProSysObjIdP4200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 42)
)
_ProSysObjIdDNX300_ObjectIdentity = ObjectIdentity
proSysObjIdDNX300 = _ProSysObjIdDNX300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 43)
)
_ProSysObjIdCNX400_ObjectIdentity = ObjectIdentity
proSysObjIdCNX400 = _ProSysObjIdCNX400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 44)
)
_ProSysObjIdCNX600_ObjectIdentity = ObjectIdentity
proSysObjIdCNX600 = _ProSysObjIdCNX600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 46)
)
_ProSysObjIdRBX200_ObjectIdentity = ObjectIdentity
proSysObjIdRBX200 = _ProSysObjIdRBX200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 47)
)
_ProSysObjIdCNX500_ObjectIdentity = ObjectIdentity
proSysObjIdCNX500 = _ProSysObjIdCNX500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 49)
)
_ProSysObjIdRBX250_ObjectIdentity = ObjectIdentity
proSysObjIdRBX250 = _ProSysObjIdRBX250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 50)
)
_ProSysObjIdBOSS3Slot_ObjectIdentity = ObjectIdentity
proSysObjIdBOSS3Slot = _ProSysObjIdBOSS3Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 53)
)
_ProSysObjIdBOSSs90_ObjectIdentity = ObjectIdentity
proSysObjIdBOSSs90 = _ProSysObjIdBOSSs90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 54)
)
_ProSysObjIdGT60_ObjectIdentity = ObjectIdentity
proSysObjIdGT60 = _ProSysObjIdGT60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 55)
)
_ProSysObjIdGT62_ObjectIdentity = ObjectIdentity
proSysObjIdGT62 = _ProSysObjIdGT62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 56)
)
_ProSysObjIdGT100_ObjectIdentity = ObjectIdentity
proSysObjIdGT100 = _ProSysObjIdGT100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 57)
)
_ProSysObjIdGTAM_ObjectIdentity = ObjectIdentity
proSysObjIdGTAM = _ProSysObjIdGTAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 58)
)
_ProSysObjIdGT70_ObjectIdentity = ObjectIdentity
proSysObjIdGT70 = _ProSysObjIdGT70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 59)
)
_ProSysObjIdGT72_ObjectIdentity = ObjectIdentity
proSysObjIdGT72 = _ProSysObjIdGT72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 60)
)
_ProSysObjIdGT60_SEC_ObjectIdentity = ObjectIdentity
proSysObjIdGT60_SEC = _ProSysObjIdGT60_SEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 61)
)
_ProSysObjIdGT70_SEC_ObjectIdentity = ObjectIdentity
proSysObjIdGT70_SEC = _ProSysObjIdGT70_SEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 62)
)
_ProSysObjIdGT65_ObjectIdentity = ObjectIdentity
proSysObjIdGT65 = _ProSysObjIdGT65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 63)
)
_ProSysObjIdGT75_ObjectIdentity = ObjectIdentity
proSysObjIdGT75 = _ProSysObjIdGT75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 64)
)
_ProSysObjIdCSX900ER_ObjectIdentity = ObjectIdentity
proSysObjIdCSX900ER = _ProSysObjIdCSX900ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 65)
)
_ProSysObjIdGTX_1000_ObjectIdentity = ObjectIdentity
proSysObjIdGTX_1000 = _ProSysObjIdGTX_1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 66)
)
_ProSysObjIdDRAGON_ObjectIdentity = ObjectIdentity
proSysObjIdDRAGON = _ProSysObjIdDRAGON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 67)
)
_ProSysObjIdDRAGONPRO_ObjectIdentity = ObjectIdentity
proSysObjIdDRAGONPRO = _ProSysObjIdDRAGONPRO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 68)
)
_ProSysObjIdGTE2_ObjectIdentity = ObjectIdentity
proSysObjIdGTE2 = _ProSysObjIdGTE2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 69)
)
_ProSysObjIdGT50_ObjectIdentity = ObjectIdentity
proSysObjIdGT50 = _ProSysObjIdGT50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 1, 70)
)
_ProStatus_ObjectIdentity = ObjectIdentity
proStatus = _ProStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 2)
)
_ProStatusReloadTime_Type = TimeTicks
_ProStatusReloadTime_Object = MibScalar
proStatusReloadTime = _ProStatusReloadTime_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 2, 1),
    _ProStatusReloadTime_Type()
)
proStatusReloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proStatusReloadTime.setStatus("mandatory")
_ProStatusStarts_Type = Counter32
_ProStatusStarts_Object = MibScalar
proStatusStarts = _ProStatusStarts_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 2, 2),
    _ProStatusStarts_Type()
)
proStatusStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proStatusStarts.setStatus("mandatory")
_ProStatusCrashes_Type = Counter32
_ProStatusCrashes_Object = MibScalar
proStatusCrashes = _ProStatusCrashes_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 2, 3),
    _ProStatusCrashes_Type()
)
proStatusCrashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proStatusCrashes.setStatus("mandatory")
_ProStatusCrashMsg_Type = DisplayString
_ProStatusCrashMsg_Object = MibScalar
proStatusCrashMsg = _ProStatusCrashMsg_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 2, 4),
    _ProStatusCrashMsg_Type()
)
proStatusCrashMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proStatusCrashMsg.setStatus("mandatory")
_ProPriv_ObjectIdentity = ObjectIdentity
proPriv = _ProPriv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1, 5)
)
_ProActionReset_Type = Integer32
_ProActionReset_Object = MibScalar
proActionReset = _ProActionReset_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 5, 2),
    _ProActionReset_Type()
)
proActionReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proActionReset.setStatus("mandatory")
_ProSyslogServer_Type = IpAddress
_ProSyslogServer_Object = MibScalar
proSyslogServer = _ProSyslogServer_Object(
    (1, 3, 6, 1, 4, 1, 1, 1, 5, 5),
    _ProSyslogServer_Type()
)
proSyslogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proSyslogServer.setStatus("mandatory")
_ProSystem_ObjectIdentity = ObjectIdentity
proSystem = _ProSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6)
)
_ProResource_ObjectIdentity = ObjectIdentity
proResource = _ProResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 1)
)
_ProResMemory_ObjectIdentity = ObjectIdentity
proResMemory = _ProResMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1)
)
_ProResMemHeap_ObjectIdentity = ObjectIdentity
proResMemHeap = _ProResMemHeap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 1)
)
_ProResMemHeapTotal_Type = Integer32
_ProResMemHeapTotal_Object = MibScalar
proResMemHeapTotal = _ProResMemHeapTotal_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 1, 1),
    _ProResMemHeapTotal_Type()
)
proResMemHeapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemHeapTotal.setStatus("mandatory")
_ProResMemHeapReserve_Type = Integer32
_ProResMemHeapReserve_Object = MibScalar
proResMemHeapReserve = _ProResMemHeapReserve_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 1, 2),
    _ProResMemHeapReserve_Type()
)
proResMemHeapReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemHeapReserve.setStatus("mandatory")
_ProResMemHeapNeverAlloc_Type = Integer32
_ProResMemHeapNeverAlloc_Object = MibScalar
proResMemHeapNeverAlloc = _ProResMemHeapNeverAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 1, 3),
    _ProResMemHeapNeverAlloc_Type()
)
proResMemHeapNeverAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemHeapNeverAlloc.setStatus("mandatory")
_ProResMemHeapPermAlloc_Type = Integer32
_ProResMemHeapPermAlloc_Object = MibScalar
proResMemHeapPermAlloc = _ProResMemHeapPermAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 1, 4),
    _ProResMemHeapPermAlloc_Type()
)
proResMemHeapPermAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemHeapPermAlloc.setStatus("mandatory")
_ProResMemHeapTempAlloc_Type = Integer32
_ProResMemHeapTempAlloc_Object = MibScalar
proResMemHeapTempAlloc = _ProResMemHeapTempAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 1, 5),
    _ProResMemHeapTempAlloc_Type()
)
proResMemHeapTempAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemHeapTempAlloc.setStatus("mandatory")
_ProResMemHeapPrevAlloc_Type = Integer32
_ProResMemHeapPrevAlloc_Object = MibScalar
proResMemHeapPrevAlloc = _ProResMemHeapPrevAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 1, 6),
    _ProResMemHeapPrevAlloc_Type()
)
proResMemHeapPrevAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemHeapPrevAlloc.setStatus("mandatory")
_ProResMemBuf_ObjectIdentity = ObjectIdentity
proResMemBuf = _ProResMemBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 2)
)
_ProResMemBufTotal_Type = Integer32
_ProResMemBufTotal_Object = MibScalar
proResMemBufTotal = _ProResMemBufTotal_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 2, 1),
    _ProResMemBufTotal_Type()
)
proResMemBufTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemBufTotal.setStatus("mandatory")
_ProResMemBufReserve_Type = Integer32
_ProResMemBufReserve_Object = MibScalar
proResMemBufReserve = _ProResMemBufReserve_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 2, 2),
    _ProResMemBufReserve_Type()
)
proResMemBufReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemBufReserve.setStatus("mandatory")
_ProResMemBufNeverAlloc_Type = Integer32
_ProResMemBufNeverAlloc_Object = MibScalar
proResMemBufNeverAlloc = _ProResMemBufNeverAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 2, 3),
    _ProResMemBufNeverAlloc_Type()
)
proResMemBufNeverAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemBufNeverAlloc.setStatus("mandatory")
_ProResMemBufPermAlloc_Type = Integer32
_ProResMemBufPermAlloc_Object = MibScalar
proResMemBufPermAlloc = _ProResMemBufPermAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 1, 2, 4),
    _ProResMemBufPermAlloc_Type()
)
proResMemBufPermAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResMemBufPermAlloc.setStatus("mandatory")
_ProResBuffers_ObjectIdentity = ObjectIdentity
proResBuffers = _ProResBuffers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2)
)
_ProResBufGlobal_ObjectIdentity = ObjectIdentity
proResBufGlobal = _ProResBufGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 1)
)
_ProResBufGlobalTotal_Type = Integer32
_ProResBufGlobalTotal_Object = MibScalar
proResBufGlobalTotal = _ProResBufGlobalTotal_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 1, 1),
    _ProResBufGlobalTotal_Type()
)
proResBufGlobalTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResBufGlobalTotal.setStatus("mandatory")
_ProResBufGlobalFree_Type = Integer32
_ProResBufGlobalFree_Object = MibScalar
proResBufGlobalFree = _ProResBufGlobalFree_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 1, 2),
    _ProResBufGlobalFree_Type()
)
proResBufGlobalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResBufGlobalFree.setStatus("mandatory")
_ProResBufGlobalFair_Type = Integer32
_ProResBufGlobalFair_Object = MibScalar
proResBufGlobalFair = _ProResBufGlobalFair_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 1, 3),
    _ProResBufGlobalFair_Type()
)
proResBufGlobalFair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResBufGlobalFair.setStatus("mandatory")
_ProResBufGlobalLow_Type = Integer32
_ProResBufGlobalLow_Object = MibScalar
proResBufGlobalLow = _ProResBufGlobalLow_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 1, 4),
    _ProResBufGlobalLow_Type()
)
proResBufGlobalLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResBufGlobalLow.setStatus("mandatory")
_ProResBufTable_Object = MibTable
proResBufTable = _ProResBufTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    proResBufTable.setStatus("mandatory")
_ProResBufTableEntry_Object = MibTableRow
proResBufTableEntry = _ProResBufTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 2, 1)
)
proResBufTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    proResBufTableEntry.setStatus("mandatory")
_ProResInputBufsReq_Type = Integer32
_ProResInputBufsReq_Object = MibTableColumn
proResInputBufsReq = _ProResInputBufsReq_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 2, 1, 1),
    _ProResInputBufsReq_Type()
)
proResInputBufsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResInputBufsReq.setStatus("mandatory")
_ProResInputBufsAlloc_Type = Integer32
_ProResInputBufsAlloc_Object = MibTableColumn
proResInputBufsAlloc = _ProResInputBufsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 2, 1, 2),
    _ProResInputBufsAlloc_Type()
)
proResInputBufsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResInputBufsAlloc.setStatus("mandatory")
_ProResInputBufsLow_Type = Integer32
_ProResInputBufsLow_Object = MibTableColumn
proResInputBufsLow = _ProResInputBufsLow_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 2, 1, 3),
    _ProResInputBufsLow_Type()
)
proResInputBufsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResInputBufsLow.setStatus("mandatory")
_ProResInputBufsCurrent_Type = Integer32
_ProResInputBufsCurrent_Object = MibTableColumn
proResInputBufsCurrent = _ProResInputBufsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 2, 1, 4),
    _ProResInputBufsCurrent_Type()
)
proResInputBufsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResInputBufsCurrent.setStatus("mandatory")
_ProResInputBufsSize_Type = Integer32
_ProResInputBufsSize_Object = MibTableColumn
proResInputBufsSize = _ProResInputBufsSize_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 2, 1, 5),
    _ProResInputBufsSize_Type()
)
proResInputBufsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResInputBufsSize.setStatus("mandatory")
_ProResInputBufsTotalBytes_Type = Integer32
_ProResInputBufsTotalBytes_Object = MibTableColumn
proResInputBufsTotalBytes = _ProResInputBufsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 1, 2, 2, 1, 6),
    _ProResInputBufsTotalBytes_Type()
)
proResInputBufsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proResInputBufsTotalBytes.setStatus("mandatory")
_ProEls_ObjectIdentity = ObjectIdentity
proEls = _ProEls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 2)
)
_ProElsGeneric_ObjectIdentity = ObjectIdentity
proElsGeneric = _ProElsGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 1)
)
_ProElsPin_Type = Integer32
_ProElsPin_Object = MibScalar
proElsPin = _ProElsPin_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 1, 1),
    _ProElsPin_Type()
)
proElsPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsPin.setStatus("mandatory")
_ProElsDroppeds_Type = Counter32
_ProElsDroppeds_Object = MibScalar
proElsDroppeds = _ProElsDroppeds_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 1, 2),
    _ProElsDroppeds_Type()
)
proElsDroppeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsDroppeds.setStatus("mandatory")


class _ProElsTimestamp_Type(Integer32):
    """Custom type proElsTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("proTSOff", 1),
          ("proTSSysUpTime", 2),
          ("proTSTimeOfDay", 3))
    )


_ProElsTimestamp_Type.__name__ = "Integer32"
_ProElsTimestamp_Object = MibScalar
proElsTimestamp = _ProElsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 1, 3),
    _ProElsTimestamp_Type()
)
proElsTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsTimestamp.setStatus("mandatory")


class _ProElsAction_Type(Integer32):
    """Custom type proElsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("proElsActionClear", 2),
          ("proElsActionDefault", 3))
    )


_ProElsAction_Type.__name__ = "Integer32"
_ProElsAction_Object = MibScalar
proElsAction = _ProElsAction_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 1, 4),
    _ProElsAction_Type()
)
proElsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsAction.setStatus("mandatory")


class _ProElsTrapVersion_Type(Integer32):
    """Custom type proElsTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proElsTrapVersionV1", 1),
          ("proElsTrapVersionV2", 2))
    )


_ProElsTrapVersion_Type.__name__ = "Integer32"
_ProElsTrapVersion_Object = MibScalar
proElsTrapVersion = _ProElsTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 1, 5),
    _ProElsTrapVersion_Type()
)
proElsTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsTrapVersion.setStatus("mandatory")
_ProElsSubSysTable_Object = MibTable
proElsSubSysTable = _ProElsSubSysTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    proElsSubSysTable.setStatus("mandatory")
_ProElsSubSysTableEntry_Object = MibTableRow
proElsSubSysTableEntry = _ProElsSubSysTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1)
)
proElsSubSysTableEntry.setIndexNames(
    (0, "OpenROUTE-MIB", "proElsSubSysIndex"),
)
if mibBuilder.loadTexts:
    proElsSubSysTableEntry.setStatus("mandatory")


class _ProElsSubSysIndex_Type(Integer32):
    """Custom type proElsSubSysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
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
              25,
              30,
              31,
              35,
              40,
              41,
              42,
              43,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              60,
              70,
              71,
              72,
              73,
              74,
              75,
              80,
              81,
              82,
              83,
              84,
              85,
              87,
              88,
              89,
              90,
              92,
              95,
              96,
              97,
              98,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108)
        )
    )
    namedValues = NamedValues(
        *(("proElsSubSysIndexAp2", 53),
          ("proElsSubSysIndexApl", 50),
          ("proElsSubSysIndexArp", 5),
          ("proElsSubSysIndexArpa", 80),
          ("proElsSubSysIndexAtr", 89),
          ("proElsSubSysIndexBgp", 104),
          ("proElsSubSysIndexBoss", 106),
          ("proElsSubSysIndexBr", 74),
          ("proElsSubSysIndexBtp", 14),
          ("proElsSubSysIndexDds", 55),
          ("proElsSubSysIndexDls", 107),
          ("proElsSubSysIndexDn", 25),
          ("proElsSubSysIndexDnav", 43),
          ("proElsSubSysIndexEgp", 16),
          ("proElsSubSysIndexEsis", 41),
          ("proElsSubSysIndexEth", 81),
          ("proElsSubSysIndexFddi", 88),
          ("proElsSubSysIndexFr", 92),
          ("proElsSubSysIndexGw", 1),
          ("proElsSubSysIndexIcmp", 11),
          ("proElsSubSysIndexIp", 10),
          ("proElsSubSysIndexIppn", 100),
          ("proElsSubSysIndexIpx", 35),
          ("proElsSubSysIndexIsis", 42),
          ("proElsSubSysIndexIso", 40),
          ("proElsSubSysIndexLlc", 103),
          ("proElsSubSysIndexLnm", 102),
          ("proElsSubSysIndexMan", 87),
          ("proElsSubSysIndexMcf", 105),
          ("proElsSubSysIndexMspf", 18),
          ("proElsSubSysIndexPn", 82),
          ("proElsSubSysIndexPpp", 95),
          ("proElsSubSysIndexR2mp", 56),
          ("proElsSubSysIndexRip", 15),
          ("proElsSubSysIndexRtmp", 52),
          ("proElsSubSysIndexSdlc", 75),
          ("proElsSubSysIndexSl", 83),
          ("proElsSubSysIndexSnmp", 21),
          ("proElsSubSysIndexSpf", 17),
          ("proElsSubSysIndexSrb", 70),
          ("proElsSubSysIndexSrly", 90),
          ("proElsSubSysIndexSrt", 72),
          ("proElsSubSysIndexStb", 71),
          ("proElsSubSysIndexStp", 73),
          ("proElsSubSysIndexTcp", 12),
          ("proElsSubSysIndexTftp", 19),
          ("proElsSubSysIndexTkr", 84),
          ("proElsSubSysIndexTn", 20),
          ("proElsSubSysIndexUdp", 13),
          ("proElsSubSysIndexV25b", 108),
          ("proElsSubSysIndexVn", 60),
          ("proElsSubSysIndexWrs", 101),
          ("proElsSubSysIndexX25", 85),
          ("proElsSubSysIndexX251", 96),
          ("proElsSubSysIndexX252", 97),
          ("proElsSubSysIndexX253", 98),
          ("proElsSubSysIndexXn", 30),
          ("proElsSubSysIndexXns", 31),
          ("proElsSubSysIndexZip", 51),
          ("proElsSubSysIndexZip2", 54))
    )


_ProElsSubSysIndex_Type.__name__ = "Integer32"
_ProElsSubSysIndex_Object = MibTableColumn
proElsSubSysIndex = _ProElsSubSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1, 1),
    _ProElsSubSysIndex_Type()
)
proElsSubSysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsSubSysIndex.setStatus("mandatory")


class _ProElsSubSysDescr_Type(DisplayString):
    """Custom type proElsSubSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ProElsSubSysDescr_Type.__name__ = "DisplayString"
_ProElsSubSysDescr_Object = MibTableColumn
proElsSubSysDescr = _ProElsSubSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1, 2),
    _ProElsSubSysDescr_Type()
)
proElsSubSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsSubSysDescr.setStatus("mandatory")
_ProElsSubSysNumEvents_Type = Integer32
_ProElsSubSysNumEvents_Object = MibTableColumn
proElsSubSysNumEvents = _ProElsSubSysNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1, 3),
    _ProElsSubSysNumEvents_Type()
)
proElsSubSysNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsSubSysNumEvents.setStatus("mandatory")
_ProElsSubSysDisplayEnable_Type = ProElsMsgLogLevel
_ProElsSubSysDisplayEnable_Object = MibTableColumn
proElsSubSysDisplayEnable = _ProElsSubSysDisplayEnable_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1, 4),
    _ProElsSubSysDisplayEnable_Type()
)
proElsSubSysDisplayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsSubSysDisplayEnable.setStatus("mandatory")
_ProElsSubSysDisplayDisable_Type = ProElsMsgLogLevel
_ProElsSubSysDisplayDisable_Object = MibTableColumn
proElsSubSysDisplayDisable = _ProElsSubSysDisplayDisable_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1, 5),
    _ProElsSubSysDisplayDisable_Type()
)
proElsSubSysDisplayDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsSubSysDisplayDisable.setStatus("mandatory")
_ProElsSubSysTrapEnable_Type = ProElsMsgLogLevel
_ProElsSubSysTrapEnable_Object = MibTableColumn
proElsSubSysTrapEnable = _ProElsSubSysTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1, 6),
    _ProElsSubSysTrapEnable_Type()
)
proElsSubSysTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsSubSysTrapEnable.setStatus("mandatory")
_ProElsSubSysTrapDisable_Type = ProElsMsgLogLevel
_ProElsSubSysTrapDisable_Object = MibTableColumn
proElsSubSysTrapDisable = _ProElsSubSysTrapDisable_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1, 7),
    _ProElsSubSysTrapDisable_Type()
)
proElsSubSysTrapDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsSubSysTrapDisable.setStatus("mandatory")
_ProElsSubSysCurrDisplayLevel_Type = Integer32
_ProElsSubSysCurrDisplayLevel_Object = MibTableColumn
proElsSubSysCurrDisplayLevel = _ProElsSubSysCurrDisplayLevel_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1, 8),
    _ProElsSubSysCurrDisplayLevel_Type()
)
proElsSubSysCurrDisplayLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsSubSysCurrDisplayLevel.setStatus("mandatory")
_ProElsSubSysCurrTrapLevel_Type = Integer32
_ProElsSubSysCurrTrapLevel_Object = MibTableColumn
proElsSubSysCurrTrapLevel = _ProElsSubSysCurrTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 2, 1, 9),
    _ProElsSubSysCurrTrapLevel_Type()
)
proElsSubSysCurrTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsSubSysCurrTrapLevel.setStatus("mandatory")
_ProElsSubSysEventTable_Object = MibTable
proElsSubSysEventTable = _ProElsSubSysEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    proElsSubSysEventTable.setStatus("mandatory")
_ProElsSubSysEventTableEntry_Object = MibTableRow
proElsSubSysEventTableEntry = _ProElsSubSysEventTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 3, 1)
)
proElsSubSysEventTableEntry.setIndexNames(
    (0, "OpenROUTE-MIB", "proElsSubSysIndex"),
    (0, "OpenROUTE-MIB", "proElsSubSysEventIndex"),
)
if mibBuilder.loadTexts:
    proElsSubSysEventTableEntry.setStatus("mandatory")
_ProElsSubSysEventIndex_Type = Integer32
_ProElsSubSysEventIndex_Object = MibTableColumn
proElsSubSysEventIndex = _ProElsSubSysEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 3, 1, 1),
    _ProElsSubSysEventIndex_Type()
)
proElsSubSysEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsSubSysEventIndex.setStatus("mandatory")
_ProElsSubSysEventMsg_Type = DisplayString
_ProElsSubSysEventMsg_Object = MibTableColumn
proElsSubSysEventMsg = _ProElsSubSysEventMsg_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 3, 1, 2),
    _ProElsSubSysEventMsg_Type()
)
proElsSubSysEventMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsSubSysEventMsg.setStatus("mandatory")
_ProElsSubSysEventCount_Type = Integer32
_ProElsSubSysEventCount_Object = MibTableColumn
proElsSubSysEventCount = _ProElsSubSysEventCount_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 3, 1, 3),
    _ProElsSubSysEventCount_Type()
)
proElsSubSysEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsSubSysEventCount.setStatus("mandatory")
_ProElsSubSysEventLogLevel_Type = ProElsMsgLogLevel
_ProElsSubSysEventLogLevel_Object = MibTableColumn
proElsSubSysEventLogLevel = _ProElsSubSysEventLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 3, 1, 4),
    _ProElsSubSysEventLogLevel_Type()
)
proElsSubSysEventLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proElsSubSysEventLogLevel.setStatus("mandatory")
_ProElsSubSysEventLogToConsole_Type = ProElsLogStatus
_ProElsSubSysEventLogToConsole_Object = MibTableColumn
proElsSubSysEventLogToConsole = _ProElsSubSysEventLogToConsole_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 3, 1, 5),
    _ProElsSubSysEventLogToConsole_Type()
)
proElsSubSysEventLogToConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsSubSysEventLogToConsole.setStatus("mandatory")
_ProElsSubSysEventLogToTrap_Type = ProElsLogStatus
_ProElsSubSysEventLogToTrap_Object = MibTableColumn
proElsSubSysEventLogToTrap = _ProElsSubSysEventLogToTrap_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 2, 3, 1, 6),
    _ProElsSubSysEventLogToTrap_Type()
)
proElsSubSysEventLogToTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proElsSubSysEventLogToTrap.setStatus("mandatory")
_ProTemp_ObjectIdentity = ObjectIdentity
proTemp = _ProTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 3)
)


class _ProTempScale_Type(Integer32):
    """Custom type proTempScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_ProTempScale_Type.__name__ = "Integer32"
_ProTempScale_Object = MibScalar
proTempScale = _ProTempScale_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 1),
    _ProTempScale_Type()
)
proTempScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proTempScale.setStatus("mandatory")
_ProMaxHwTemp_Type = Integer32
_ProMaxHwTemp_Object = MibScalar
proMaxHwTemp = _ProMaxHwTemp_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 2),
    _ProMaxHwTemp_Type()
)
proMaxHwTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proMaxHwTemp.setStatus("mandatory")
_ProMinHwTemp_Type = Integer32
_ProMinHwTemp_Object = MibScalar
proMinHwTemp = _ProMinHwTemp_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 3),
    _ProMinHwTemp_Type()
)
proMinHwTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proMinHwTemp.setStatus("mandatory")


class _ProTempPollPeriod_Type(Integer32):
    """Custom type proTempPollPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_ProTempPollPeriod_Type.__name__ = "Integer32"
_ProTempPollPeriod_Object = MibScalar
proTempPollPeriod = _ProTempPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 4),
    _ProTempPollPeriod_Type()
)
proTempPollPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proTempPollPeriod.setStatus("mandatory")
_ProCurrentTemp_Type = Integer32
_ProCurrentTemp_Object = MibScalar
proCurrentTemp = _ProCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 5),
    _ProCurrentTemp_Type()
)
proCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proCurrentTemp.setStatus("mandatory")
_ProLowTempThreshold_Type = Integer32
_ProLowTempThreshold_Object = MibScalar
proLowTempThreshold = _ProLowTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 6),
    _ProLowTempThreshold_Type()
)
proLowTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proLowTempThreshold.setStatus("mandatory")
_ProHighTempThreshold_Type = Integer32
_ProHighTempThreshold_Object = MibScalar
proHighTempThreshold = _ProHighTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 7),
    _ProHighTempThreshold_Type()
)
proHighTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proHighTempThreshold.setStatus("mandatory")


class _ProTempHysteresis_Type(Integer32):
    """Custom type proTempHysteresis based on Integer32"""
    defaultValue = 5


_ProTempHysteresis_Object = MibScalar
proTempHysteresis = _ProTempHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 8),
    _ProTempHysteresis_Type()
)
proTempHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proTempHysteresis.setStatus("mandatory")


class _ProHighTempCondition_Type(Integer32):
    """Custom type proHighTempCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ProHighTempCondition_Type.__name__ = "Integer32"
_ProHighTempCondition_Object = MibScalar
proHighTempCondition = _ProHighTempCondition_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 9),
    _ProHighTempCondition_Type()
)
proHighTempCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proHighTempCondition.setStatus("mandatory")


class _ProLowTempCondition_Type(Integer32):
    """Custom type proLowTempCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ProLowTempCondition_Type.__name__ = "Integer32"
_ProLowTempCondition_Object = MibScalar
proLowTempCondition = _ProLowTempCondition_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 10),
    _ProLowTempCondition_Type()
)
proLowTempCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proLowTempCondition.setStatus("mandatory")
_ProHighestTemp_Type = Integer32
_ProHighestTemp_Object = MibScalar
proHighestTemp = _ProHighestTemp_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 11),
    _ProHighestTemp_Type()
)
proHighestTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proHighestTemp.setStatus("mandatory")
_ProHighTempTime_Type = TimeTicks
_ProHighTempTime_Object = MibScalar
proHighTempTime = _ProHighTempTime_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 12),
    _ProHighTempTime_Type()
)
proHighTempTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proHighTempTime.setStatus("mandatory")
_ProLowestTemp_Type = Integer32
_ProLowestTemp_Object = MibScalar
proLowestTemp = _ProLowestTemp_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 13),
    _ProLowestTemp_Type()
)
proLowestTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proLowestTemp.setStatus("mandatory")
_ProLowTempTime_Type = TimeTicks
_ProLowTempTime_Object = MibScalar
proLowTempTime = _ProLowTempTime_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 3, 14),
    _ProLowTempTime_Type()
)
proLowTempTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proLowTempTime.setStatus("mandatory")
_ProConfig_ObjectIdentity = ObjectIdentity
proConfig = _ProConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 4)
)
_ProCfgLoad_ObjectIdentity = ObjectIdentity
proCfgLoad = _ProCfgLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 6, 4, 1)
)


class _ProCfgProtocols_Type(DisplayString):
    """Custom type proCfgProtocols based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProCfgProtocols_Type.__name__ = "DisplayString"
_ProCfgProtocols_Object = MibScalar
proCfgProtocols = _ProCfgProtocols_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 4, 1, 1),
    _ProCfgProtocols_Type()
)
proCfgProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proCfgProtocols.setStatus("mandatory")


class _ProCfgDatalinks_Type(DisplayString):
    """Custom type proCfgDatalinks based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProCfgDatalinks_Type.__name__ = "DisplayString"
_ProCfgDatalinks_Object = MibScalar
proCfgDatalinks = _ProCfgDatalinks_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 4, 1, 2),
    _ProCfgDatalinks_Type()
)
proCfgDatalinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proCfgDatalinks.setStatus("mandatory")


class _ProCfgFeatures_Type(DisplayString):
    """Custom type proCfgFeatures based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProCfgFeatures_Type.__name__ = "DisplayString"
_ProCfgFeatures_Object = MibScalar
proCfgFeatures = _ProCfgFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1, 6, 4, 1, 3),
    _ProCfgFeatures_Type()
)
proCfgFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proCfgFeatures.setStatus("mandatory")

# Managed Objects groups


# Notification objects

proElsTrapV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1, 0, 1)
)
proElsTrapV1.setObjects(
      *(("PROTEON-MIB", "proElsTrapSeqs"),
        ("PROTEON-MIB", "proElsTrapSubSystem"),
        ("PROTEON-MIB", "proElsTrapEvent"))
)
if mibBuilder.loadTexts:
    proElsTrapV1.setStatus(
        ""
    )

proElsTrapV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1, 0, 2)
)
proElsTrapV2.setObjects(
    ("OpenROUTE-MIB", "proElsSubSysEventMsg")
)
if mibBuilder.loadTexts:
    proElsTrapV2.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OpenROUTE-MIB",
    **{"ProElsMsgLogLevel": ProElsMsgLogLevel,
       "ProElsLogStatus": ProElsLogStatus,
       "proteon": proteon,
       "proElsTrapV1": proElsTrapV1,
       "proElsTrapV2": proElsTrapV2,
       "proAdmin": proAdmin,
       "proSysObjId": proSysObjId,
       "proElsTrapVar1": proElsTrapVar1,
       "proElsTrapVar2": proElsTrapVar2,
       "proElsTrapVar3": proElsTrapVar3,
       "proElsTrapVar4": proElsTrapVar4,
       "proElsTrapVar5": proElsTrapVar5,
       "proElsTrapVar6": proElsTrapVar6,
       "proElsTrapVar7": proElsTrapVar7,
       "proElsTrapVar8": proElsTrapVar8,
       "proElsTrapVar9": proElsTrapVar9,
       "proSysObjIdP4100": proSysObjIdP4100,
       "proSysObjIdP4200": proSysObjIdP4200,
       "proSysObjIdDNX300": proSysObjIdDNX300,
       "proSysObjIdCNX400": proSysObjIdCNX400,
       "proSysObjIdCNX600": proSysObjIdCNX600,
       "proSysObjIdRBX200": proSysObjIdRBX200,
       "proSysObjIdCNX500": proSysObjIdCNX500,
       "proSysObjIdRBX250": proSysObjIdRBX250,
       "proSysObjIdBOSS3Slot": proSysObjIdBOSS3Slot,
       "proSysObjIdBOSSs90": proSysObjIdBOSSs90,
       "proSysObjIdGT60": proSysObjIdGT60,
       "proSysObjIdGT62": proSysObjIdGT62,
       "proSysObjIdGT100": proSysObjIdGT100,
       "proSysObjIdGTAM": proSysObjIdGTAM,
       "proSysObjIdGT70": proSysObjIdGT70,
       "proSysObjIdGT72": proSysObjIdGT72,
       "proSysObjIdGT60-SEC": proSysObjIdGT60_SEC,
       "proSysObjIdGT70-SEC": proSysObjIdGT70_SEC,
       "proSysObjIdGT65": proSysObjIdGT65,
       "proSysObjIdGT75": proSysObjIdGT75,
       "proSysObjIdCSX900ER": proSysObjIdCSX900ER,
       "proSysObjIdGTX-1000": proSysObjIdGTX_1000,
       "proSysObjIdDRAGON": proSysObjIdDRAGON,
       "proSysObjIdDRAGONPRO": proSysObjIdDRAGONPRO,
       "proSysObjIdGTE2": proSysObjIdGTE2,
       "proSysObjIdGT50": proSysObjIdGT50,
       "proStatus": proStatus,
       "proStatusReloadTime": proStatusReloadTime,
       "proStatusStarts": proStatusStarts,
       "proStatusCrashes": proStatusCrashes,
       "proStatusCrashMsg": proStatusCrashMsg,
       "proPriv": proPriv,
       "proActionReset": proActionReset,
       "proSyslogServer": proSyslogServer,
       "proSystem": proSystem,
       "proResource": proResource,
       "proResMemory": proResMemory,
       "proResMemHeap": proResMemHeap,
       "proResMemHeapTotal": proResMemHeapTotal,
       "proResMemHeapReserve": proResMemHeapReserve,
       "proResMemHeapNeverAlloc": proResMemHeapNeverAlloc,
       "proResMemHeapPermAlloc": proResMemHeapPermAlloc,
       "proResMemHeapTempAlloc": proResMemHeapTempAlloc,
       "proResMemHeapPrevAlloc": proResMemHeapPrevAlloc,
       "proResMemBuf": proResMemBuf,
       "proResMemBufTotal": proResMemBufTotal,
       "proResMemBufReserve": proResMemBufReserve,
       "proResMemBufNeverAlloc": proResMemBufNeverAlloc,
       "proResMemBufPermAlloc": proResMemBufPermAlloc,
       "proResBuffers": proResBuffers,
       "proResBufGlobal": proResBufGlobal,
       "proResBufGlobalTotal": proResBufGlobalTotal,
       "proResBufGlobalFree": proResBufGlobalFree,
       "proResBufGlobalFair": proResBufGlobalFair,
       "proResBufGlobalLow": proResBufGlobalLow,
       "proResBufTable": proResBufTable,
       "proResBufTableEntry": proResBufTableEntry,
       "proResInputBufsReq": proResInputBufsReq,
       "proResInputBufsAlloc": proResInputBufsAlloc,
       "proResInputBufsLow": proResInputBufsLow,
       "proResInputBufsCurrent": proResInputBufsCurrent,
       "proResInputBufsSize": proResInputBufsSize,
       "proResInputBufsTotalBytes": proResInputBufsTotalBytes,
       "proEls": proEls,
       "proElsGeneric": proElsGeneric,
       "proElsPin": proElsPin,
       "proElsDroppeds": proElsDroppeds,
       "proElsTimestamp": proElsTimestamp,
       "proElsAction": proElsAction,
       "proElsTrapVersion": proElsTrapVersion,
       "proElsSubSysTable": proElsSubSysTable,
       "proElsSubSysTableEntry": proElsSubSysTableEntry,
       "proElsSubSysIndex": proElsSubSysIndex,
       "proElsSubSysDescr": proElsSubSysDescr,
       "proElsSubSysNumEvents": proElsSubSysNumEvents,
       "proElsSubSysDisplayEnable": proElsSubSysDisplayEnable,
       "proElsSubSysDisplayDisable": proElsSubSysDisplayDisable,
       "proElsSubSysTrapEnable": proElsSubSysTrapEnable,
       "proElsSubSysTrapDisable": proElsSubSysTrapDisable,
       "proElsSubSysCurrDisplayLevel": proElsSubSysCurrDisplayLevel,
       "proElsSubSysCurrTrapLevel": proElsSubSysCurrTrapLevel,
       "proElsSubSysEventTable": proElsSubSysEventTable,
       "proElsSubSysEventTableEntry": proElsSubSysEventTableEntry,
       "proElsSubSysEventIndex": proElsSubSysEventIndex,
       "proElsSubSysEventMsg": proElsSubSysEventMsg,
       "proElsSubSysEventCount": proElsSubSysEventCount,
       "proElsSubSysEventLogLevel": proElsSubSysEventLogLevel,
       "proElsSubSysEventLogToConsole": proElsSubSysEventLogToConsole,
       "proElsSubSysEventLogToTrap": proElsSubSysEventLogToTrap,
       "proTemp": proTemp,
       "proTempScale": proTempScale,
       "proMaxHwTemp": proMaxHwTemp,
       "proMinHwTemp": proMinHwTemp,
       "proTempPollPeriod": proTempPollPeriod,
       "proCurrentTemp": proCurrentTemp,
       "proLowTempThreshold": proLowTempThreshold,
       "proHighTempThreshold": proHighTempThreshold,
       "proTempHysteresis": proTempHysteresis,
       "proHighTempCondition": proHighTempCondition,
       "proLowTempCondition": proLowTempCondition,
       "proHighestTemp": proHighestTemp,
       "proHighTempTime": proHighTempTime,
       "proLowestTemp": proLowestTemp,
       "proLowTempTime": proLowTempTime,
       "proConfig": proConfig,
       "proCfgLoad": proCfgLoad,
       "proCfgProtocols": proCfgProtocols,
       "proCfgDatalinks": proCfgDatalinks,
       "proCfgFeatures": proCfgFeatures}
)
