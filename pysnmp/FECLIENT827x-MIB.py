# SNMP MIB module (FECLIENT827x-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FECLIENT827x-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:49 2024
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

(proElsSubSysEventMsg,) = mibBuilder.importSymbols(
    "PROTEON-MIB",
    "proElsSubSysEventMsg")

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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_NwaysMSS_ObjectIdentity = ObjectIdentity
nwaysMSS = _NwaysMSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118)
)
_IbmMSSClientMIB_ObjectIdentity = ObjectIdentity
ibmMSSClientMIB = _IbmMSSClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4)
)
_Fe827xNotificationGroup_ObjectIdentity = ObjectIdentity
fe827xNotificationGroup = _Fe827xNotificationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 0)
)
_Fe827xMIBObjectGroup_ObjectIdentity = ObjectIdentity
fe827xMIBObjectGroup = _Fe827xMIBObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1)
)
_Fe827xProdGroup_ObjectIdentity = ObjectIdentity
fe827xProdGroup = _Fe827xProdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1)
)


class _Fe827xResetFlag_Type(Integer32):
    """Custom type fe827xResetFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 1),
          ("reboot", 2))
    )


_Fe827xResetFlag_Type.__name__ = "Integer32"
_Fe827xResetFlag_Object = MibScalar
fe827xResetFlag = _Fe827xResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 1),
    _Fe827xResetFlag_Type()
)
fe827xResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fe827xResetFlag.setStatus("mandatory")
_Fe827xDRAMInstalled_Type = Integer32
_Fe827xDRAMInstalled_Object = MibScalar
fe827xDRAMInstalled = _Fe827xDRAMInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 2),
    _Fe827xDRAMInstalled_Type()
)
fe827xDRAMInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xDRAMInstalled.setStatus("mandatory")
_Fe827xCacheInstalled_Type = Integer32
_Fe827xCacheInstalled_Object = MibScalar
fe827xCacheInstalled = _Fe827xCacheInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 3),
    _Fe827xCacheInstalled_Type()
)
fe827xCacheInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xCacheInstalled.setStatus("mandatory")
_Fe827xFlashInstalled_Type = Integer32
_Fe827xFlashInstalled_Object = MibScalar
fe827xFlashInstalled = _Fe827xFlashInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 4),
    _Fe827xFlashInstalled_Type()
)
fe827xFlashInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xFlashInstalled.setStatus("mandatory")
_Fe827xSRAMInstalled_Type = Integer32
_Fe827xSRAMInstalled_Object = MibScalar
fe827xSRAMInstalled = _Fe827xSRAMInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 5),
    _Fe827xSRAMInstalled_Type()
)
fe827xSRAMInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xSRAMInstalled.setStatus("mandatory")


class _Fe827xNotifyStatus_Type(Integer32):
    """Custom type fe827xNotifyStatus based on Integer32"""
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


_Fe827xNotifyStatus_Type.__name__ = "Integer32"
_Fe827xNotifyStatus_Object = MibScalar
fe827xNotifyStatus = _Fe827xNotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 6),
    _Fe827xNotifyStatus_Type()
)
fe827xNotifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fe827xNotifyStatus.setStatus("mandatory")
_Fe827xSwitchIPAddr_Type = IpAddress
_Fe827xSwitchIPAddr_Object = MibScalar
fe827xSwitchIPAddr = _Fe827xSwitchIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 7),
    _Fe827xSwitchIPAddr_Type()
)
fe827xSwitchIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xSwitchIPAddr.setStatus("mandatory")
_Fe827xSwitchSlotNum_Type = Integer32
_Fe827xSwitchSlotNum_Object = MibScalar
fe827xSwitchSlotNum = _Fe827xSwitchSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 8),
    _Fe827xSwitchSlotNum_Type()
)
fe827xSwitchSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xSwitchSlotNum.setStatus("mandatory")
_Fe827xSwitchPortNum_Type = Integer32
_Fe827xSwitchPortNum_Object = MibScalar
fe827xSwitchPortNum = _Fe827xSwitchPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 1, 9),
    _Fe827xSwitchPortNum_Type()
)
fe827xSwitchPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xSwitchPortNum.setStatus("mandatory")
_Fe827xPCIAdapterGroup_ObjectIdentity = ObjectIdentity
fe827xPCIAdapterGroup = _Fe827xPCIAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2)
)
_Fe827xPCINumSlot_Type = Integer32
_Fe827xPCINumSlot_Object = MibScalar
fe827xPCINumSlot = _Fe827xPCINumSlot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 1),
    _Fe827xPCINumSlot_Type()
)
fe827xPCINumSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xPCINumSlot.setStatus("mandatory")
_Fe827xPCIAdapTable_Object = MibTable
fe827xPCIAdapTable = _Fe827xPCIAdapTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fe827xPCIAdapTable.setStatus("mandatory")
_Fe827xPCIAdapEntry_Object = MibTableRow
fe827xPCIAdapEntry = _Fe827xPCIAdapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1)
)
fe827xPCIAdapEntry.setIndexNames(
    (0, "FECLIENT827x-MIB", "fe827xPCIAdapSlotNum"),
)
if mibBuilder.loadTexts:
    fe827xPCIAdapEntry.setStatus("mandatory")
_Fe827xPCIAdapSlotNum_Type = Integer32
_Fe827xPCIAdapSlotNum_Object = MibTableColumn
fe827xPCIAdapSlotNum = _Fe827xPCIAdapSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 1),
    _Fe827xPCIAdapSlotNum_Type()
)
fe827xPCIAdapSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fe827xPCIAdapSlotNum.setStatus("mandatory")


class _Fe827xPCIAdapType_Type(Integer32):
    """Custom type fe827xPCIAdapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("unknown", 1))
    )


_Fe827xPCIAdapType_Type.__name__ = "Integer32"
_Fe827xPCIAdapType_Object = MibTableColumn
fe827xPCIAdapType = _Fe827xPCIAdapType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 2),
    _Fe827xPCIAdapType_Type()
)
fe827xPCIAdapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xPCIAdapType.setStatus("mandatory")


class _Fe827xPCIAdapConfigType_Type(Integer32):
    """Custom type fe827xPCIAdapConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("notConfigured", 1))
    )


_Fe827xPCIAdapConfigType_Type.__name__ = "Integer32"
_Fe827xPCIAdapConfigType_Object = MibTableColumn
fe827xPCIAdapConfigType = _Fe827xPCIAdapConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 3),
    _Fe827xPCIAdapConfigType_Type()
)
fe827xPCIAdapConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xPCIAdapConfigType.setStatus("mandatory")


class _Fe827xPCIAdapATMMediaType_Type(Integer32):
    """Custom type fe827xPCIAdapATMMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mmf", 3),
          ("smf", 2),
          ("unknown", 1))
    )


_Fe827xPCIAdapATMMediaType_Type.__name__ = "Integer32"
_Fe827xPCIAdapATMMediaType_Object = MibTableColumn
fe827xPCIAdapATMMediaType = _Fe827xPCIAdapATMMediaType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 4),
    _Fe827xPCIAdapATMMediaType_Type()
)
fe827xPCIAdapATMMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xPCIAdapATMMediaType.setStatus("mandatory")


class _Fe827xPCIAdapOperStatus_Type(Integer32):
    """Custom type fe827xPCIAdapOperStatus based on Integer32"""
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
        *(("disablePending", 8),
          ("disabled", 9),
          ("doesNotApply", 5),
          ("enablePending", 6),
          ("enabled", 7),
          ("missConfigured", 10),
          ("notConfigured", 2),
          ("notPresent", 3),
          ("unavailable", 4),
          ("unknown", 1))
    )


_Fe827xPCIAdapOperStatus_Type.__name__ = "Integer32"
_Fe827xPCIAdapOperStatus_Object = MibTableColumn
fe827xPCIAdapOperStatus = _Fe827xPCIAdapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 5),
    _Fe827xPCIAdapOperStatus_Type()
)
fe827xPCIAdapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xPCIAdapOperStatus.setStatus("mandatory")


class _Fe827xPCIAdapDiagStatus_Type(Integer32):
    """Custom type fe827xPCIAdapDiagStatus based on Integer32"""
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
        *(("active", 4),
          ("auto", 1),
          ("idle", 3),
          ("inactive", 2))
    )


_Fe827xPCIAdapDiagStatus_Type.__name__ = "Integer32"
_Fe827xPCIAdapDiagStatus_Object = MibTableColumn
fe827xPCIAdapDiagStatus = _Fe827xPCIAdapDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 6),
    _Fe827xPCIAdapDiagStatus_Type()
)
fe827xPCIAdapDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xPCIAdapDiagStatus.setStatus("mandatory")


class _Fe827xPCIAdapNetworkStatus_Type(Integer32):
    """Custom type fe827xPCIAdapNetworkStatus based on Integer32"""
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
        *(("doesNotApply", 5),
          ("down", 3),
          ("testing", 4),
          ("unknown", 1),
          ("up", 2))
    )


_Fe827xPCIAdapNetworkStatus_Type.__name__ = "Integer32"
_Fe827xPCIAdapNetworkStatus_Object = MibTableColumn
fe827xPCIAdapNetworkStatus = _Fe827xPCIAdapNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 7),
    _Fe827xPCIAdapNetworkStatus_Type()
)
fe827xPCIAdapNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xPCIAdapNetworkStatus.setStatus("mandatory")


class _Fe827xPCIAdapFaultStatus_Type(Integer32):
    """Custom type fe827xPCIAdapFaultStatus based on Integer32"""
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
        *(("isolated", 3),
          ("noFault", 2),
          ("nonIsolated", 4),
          ("unknown", 1))
    )


_Fe827xPCIAdapFaultStatus_Type.__name__ = "Integer32"
_Fe827xPCIAdapFaultStatus_Object = MibTableColumn
fe827xPCIAdapFaultStatus = _Fe827xPCIAdapFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 2, 2, 1, 8),
    _Fe827xPCIAdapFaultStatus_Type()
)
fe827xPCIAdapFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xPCIAdapFaultStatus.setStatus("mandatory")
_Fe827xStatGroup_ObjectIdentity = ObjectIdentity
fe827xStatGroup = _Fe827xStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3)
)
_Fe827xStatTable_Object = MibTable
fe827xStatTable = _Fe827xStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fe827xStatTable.setStatus("mandatory")
_Fe827xStatEntry_Object = MibTableRow
fe827xStatEntry = _Fe827xStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1, 1)
)
fe827xStatEntry.setIndexNames(
    (0, "FECLIENT827x-MIB", "fe827xStatQueueNum"),
)
if mibBuilder.loadTexts:
    fe827xStatEntry.setStatus("mandatory")
_Fe827xStatQueueNum_Type = Integer32
_Fe827xStatQueueNum_Object = MibTableColumn
fe827xStatQueueNum = _Fe827xStatQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1, 1, 1),
    _Fe827xStatQueueNum_Type()
)
fe827xStatQueueNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fe827xStatQueueNum.setStatus("mandatory")
_Fe827xStatFramesSent_Type = Counter32
_Fe827xStatFramesSent_Object = MibTableColumn
fe827xStatFramesSent = _Fe827xStatFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1, 1, 2),
    _Fe827xStatFramesSent_Type()
)
fe827xStatFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xStatFramesSent.setStatus("mandatory")
_Fe827xStatFramesReceived_Type = Counter32
_Fe827xStatFramesReceived_Object = MibTableColumn
fe827xStatFramesReceived = _Fe827xStatFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 3, 1, 1, 3),
    _Fe827xStatFramesReceived_Type()
)
fe827xStatFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xStatFramesReceived.setStatus("mandatory")
_Fe827xSwitchGroup_ObjectIdentity = ObjectIdentity
fe827xSwitchGroup = _Fe827xSwitchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 4)
)
_Fe827xDomainIfTable_Object = MibTable
fe827xDomainIfTable = _Fe827xDomainIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fe827xDomainIfTable.setStatus("mandatory")
_Fe827xDomainIfEntry_Object = MibTableRow
fe827xDomainIfEntry = _Fe827xDomainIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 4, 1, 1)
)
fe827xDomainIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fe827xDomainIfEntry.setStatus("mandatory")
_Fe827xSwitchDomainNum_Type = Integer32
_Fe827xSwitchDomainNum_Object = MibTableColumn
fe827xSwitchDomainNum = _Fe827xSwitchDomainNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 1, 4, 1, 1, 1),
    _Fe827xSwitchDomainNum_Type()
)
fe827xSwitchDomainNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fe827xSwitchDomainNum.setStatus("mandatory")
_Fe827xMIBConformanceGroup_ObjectIdentity = ObjectIdentity
fe827xMIBConformanceGroup = _Fe827xMIBConformanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2)
)
_FeMIBGroups_ObjectIdentity = ObjectIdentity
feMIBGroups = _FeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2, 1)
)
_FeGroup_ObjectIdentity = ObjectIdentity
feGroup = _FeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2, 1, 1)
)
_FeMIBCompliances_ObjectIdentity = ObjectIdentity
feMIBCompliances = _FeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2, 2)
)
_FeMIBCompliance_ObjectIdentity = ObjectIdentity
feMIBCompliance = _FeMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 2, 2, 1)
)

# Managed Objects groups


# Notification objects

fe827xPCIAdapStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 4, 0, 1)
)
fe827xPCIAdapStatusChg.setObjects(
      *(("FECLIENT827x-MIB", "fe827xPCIAdapConfigType"),
        ("FECLIENT827x-MIB", "fe827xPCIAdapOperStatus"),
        ("FECLIENT827x-MIB", "fe827xPCIAdapDiagStatus"),
        ("FECLIENT827x-MIB", "fe827xPCIAdapNetworkStatus"),
        ("FECLIENT827x-MIB", "fe827xPCIAdapFaultStatus"))
)
if mibBuilder.loadTexts:
    fe827xPCIAdapStatusChg.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FECLIENT827x-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "nwaysMSS": nwaysMSS,
       "ibmMSSClientMIB": ibmMSSClientMIB,
       "fe827xNotificationGroup": fe827xNotificationGroup,
       "fe827xPCIAdapStatusChg": fe827xPCIAdapStatusChg,
       "fe827xMIBObjectGroup": fe827xMIBObjectGroup,
       "fe827xProdGroup": fe827xProdGroup,
       "fe827xResetFlag": fe827xResetFlag,
       "fe827xDRAMInstalled": fe827xDRAMInstalled,
       "fe827xCacheInstalled": fe827xCacheInstalled,
       "fe827xFlashInstalled": fe827xFlashInstalled,
       "fe827xSRAMInstalled": fe827xSRAMInstalled,
       "fe827xNotifyStatus": fe827xNotifyStatus,
       "fe827xSwitchIPAddr": fe827xSwitchIPAddr,
       "fe827xSwitchSlotNum": fe827xSwitchSlotNum,
       "fe827xSwitchPortNum": fe827xSwitchPortNum,
       "fe827xPCIAdapterGroup": fe827xPCIAdapterGroup,
       "fe827xPCINumSlot": fe827xPCINumSlot,
       "fe827xPCIAdapTable": fe827xPCIAdapTable,
       "fe827xPCIAdapEntry": fe827xPCIAdapEntry,
       "fe827xPCIAdapSlotNum": fe827xPCIAdapSlotNum,
       "fe827xPCIAdapType": fe827xPCIAdapType,
       "fe827xPCIAdapConfigType": fe827xPCIAdapConfigType,
       "fe827xPCIAdapATMMediaType": fe827xPCIAdapATMMediaType,
       "fe827xPCIAdapOperStatus": fe827xPCIAdapOperStatus,
       "fe827xPCIAdapDiagStatus": fe827xPCIAdapDiagStatus,
       "fe827xPCIAdapNetworkStatus": fe827xPCIAdapNetworkStatus,
       "fe827xPCIAdapFaultStatus": fe827xPCIAdapFaultStatus,
       "fe827xStatGroup": fe827xStatGroup,
       "fe827xStatTable": fe827xStatTable,
       "fe827xStatEntry": fe827xStatEntry,
       "fe827xStatQueueNum": fe827xStatQueueNum,
       "fe827xStatFramesSent": fe827xStatFramesSent,
       "fe827xStatFramesReceived": fe827xStatFramesReceived,
       "fe827xSwitchGroup": fe827xSwitchGroup,
       "fe827xDomainIfTable": fe827xDomainIfTable,
       "fe827xDomainIfEntry": fe827xDomainIfEntry,
       "fe827xSwitchDomainNum": fe827xSwitchDomainNum,
       "fe827xMIBConformanceGroup": fe827xMIBConformanceGroup,
       "feMIBGroups": feMIBGroups,
       "feGroup": feGroup,
       "feMIBCompliances": feMIBCompliances,
       "feMIBCompliance": feMIBCompliance}
)
