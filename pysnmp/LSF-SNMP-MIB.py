# SNMP MIB module (LSF-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LSF-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:25 2024
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

_Platform_ObjectIdentity = ObjectIdentity
platform = _Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2766)
)
_LsfAgent_ObjectIdentity = ObjectIdentity
lsfAgent = _LsfAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2766, 100)
)
_LsfHosts_ObjectIdentity = ObjectIdentity
lsfHosts = _LsfHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1)
)
_LsfStaticTable_Object = MibTable
lsfStaticTable = _LsfStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1)
)
if mibBuilder.loadTexts:
    lsfStaticTable.setStatus("mandatory")
_LsfStaticEntry_Object = MibTableRow
lsfStaticEntry = _LsfStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1)
)
lsfStaticEntry.setIndexNames(
    (0, "LSF-SNMP-MIB", "lsfStaticIpIndex"),
)
if mibBuilder.loadTexts:
    lsfStaticEntry.setStatus("mandatory")
_LsfStaticIpIndex_Type = IpAddress
_LsfStaticIpIndex_Object = MibTableColumn
lsfStaticIpIndex = _LsfStaticIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 1),
    _LsfStaticIpIndex_Type()
)
lsfStaticIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfStaticIpIndex.setStatus("mandatory")


class _LsfHostName_Type(DisplayString):
    """Custom type lsfHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsfHostName_Type.__name__ = "DisplayString"
_LsfHostName_Object = MibTableColumn
lsfHostName = _LsfHostName_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 2),
    _LsfHostName_Type()
)
lsfHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfHostName.setStatus("mandatory")


class _LsfType_Type(DisplayString):
    """Custom type lsfType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsfType_Type.__name__ = "DisplayString"
_LsfType_Object = MibTableColumn
lsfType = _LsfType_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 3),
    _LsfType_Type()
)
lsfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfType.setStatus("mandatory")


class _LsfModel_Type(DisplayString):
    """Custom type lsfModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsfModel_Type.__name__ = "DisplayString"
_LsfModel_Object = MibTableColumn
lsfModel = _LsfModel_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 4),
    _LsfModel_Type()
)
lsfModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfModel.setStatus("mandatory")
_LsfCPUFactor_Type = Integer32
_LsfCPUFactor_Object = MibTableColumn
lsfCPUFactor = _LsfCPUFactor_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 5),
    _LsfCPUFactor_Type()
)
lsfCPUFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfCPUFactor.setStatus("mandatory")
_LsfNumCPU_Type = Integer32
_LsfNumCPU_Object = MibTableColumn
lsfNumCPU = _LsfNumCPU_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 6),
    _LsfNumCPU_Type()
)
lsfNumCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfNumCPU.setStatus("mandatory")
_LsfMaxMemory_Type = Integer32
_LsfMaxMemory_Object = MibTableColumn
lsfMaxMemory = _LsfMaxMemory_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 7),
    _LsfMaxMemory_Type()
)
lsfMaxMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfMaxMemory.setStatus("mandatory")
_LsfMaxSwap_Type = Integer32
_LsfMaxSwap_Object = MibTableColumn
lsfMaxSwap = _LsfMaxSwap_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 8),
    _LsfMaxSwap_Type()
)
lsfMaxSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfMaxSwap.setStatus("mandatory")
_LsfMaxTempSpace_Type = Integer32
_LsfMaxTempSpace_Object = MibTableColumn
lsfMaxTempSpace = _LsfMaxTempSpace_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 9),
    _LsfMaxTempSpace_Type()
)
lsfMaxTempSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfMaxTempSpace.setStatus("mandatory")
_LsfExecutionPriority_Type = Integer32
_LsfExecutionPriority_Object = MibTableColumn
lsfExecutionPriority = _LsfExecutionPriority_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 10),
    _LsfExecutionPriority_Type()
)
lsfExecutionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfExecutionPriority.setStatus("mandatory")


class _LsfIsServer_Type(Integer32):
    """Custom type lsfIsServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LsfIsServer_Type.__name__ = "Integer32"
_LsfIsServer_Object = MibTableColumn
lsfIsServer = _LsfIsServer_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 11),
    _LsfIsServer_Type()
)
lsfIsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfIsServer.setStatus("mandatory")


class _LsfHostResources_Type(DisplayString):
    """Custom type lsfHostResources based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsfHostResources_Type.__name__ = "DisplayString"
_LsfHostResources_Object = MibTableColumn
lsfHostResources = _LsfHostResources_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 1, 1, 12),
    _LsfHostResources_Type()
)
lsfHostResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfHostResources.setStatus("mandatory")
_LsfDynamicTable_Object = MibTable
lsfDynamicTable = _LsfDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2)
)
if mibBuilder.loadTexts:
    lsfDynamicTable.setStatus("mandatory")
_LsfDynamicEntry_Object = MibTableRow
lsfDynamicEntry = _LsfDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1)
)
lsfDynamicEntry.setIndexNames(
    (0, "LSF-SNMP-MIB", "lsfDynamicIpIndex"),
)
if mibBuilder.loadTexts:
    lsfDynamicEntry.setStatus("mandatory")
_LsfDynamicIpIndex_Type = IpAddress
_LsfDynamicIpIndex_Object = MibTableColumn
lsfDynamicIpIndex = _LsfDynamicIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 1),
    _LsfDynamicIpIndex_Type()
)
lsfDynamicIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfDynamicIpIndex.setStatus("mandatory")


class _LsfHostStatus_Type(Integer32):
    """Custom type lsfHostStatus based on Integer32"""
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
        *(("busy", 3),
          ("lockU", 4),
          ("lockUW", 6),
          ("lockW", 5),
          ("ok", 1),
          ("resDown", 2),
          ("unavail", 7),
          ("unlicensed", 8))
    )


_LsfHostStatus_Type.__name__ = "Integer32"
_LsfHostStatus_Object = MibTableColumn
lsfHostStatus = _LsfHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 2),
    _LsfHostStatus_Type()
)
lsfHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsfHostStatus.setStatus("mandatory")
_LsfFifteenSecondRunQueue_Type = Integer32
_LsfFifteenSecondRunQueue_Object = MibTableColumn
lsfFifteenSecondRunQueue = _LsfFifteenSecondRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 3),
    _LsfFifteenSecondRunQueue_Type()
)
lsfFifteenSecondRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfFifteenSecondRunQueue.setStatus("mandatory")
_LsfOneMinuteRunQueue_Type = Integer32
_LsfOneMinuteRunQueue_Object = MibTableColumn
lsfOneMinuteRunQueue = _LsfOneMinuteRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 4),
    _LsfOneMinuteRunQueue_Type()
)
lsfOneMinuteRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfOneMinuteRunQueue.setStatus("mandatory")
_LsfFifteenMinuteRunQueue_Type = Integer32
_LsfFifteenMinuteRunQueue_Object = MibTableColumn
lsfFifteenMinuteRunQueue = _LsfFifteenMinuteRunQueue_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 5),
    _LsfFifteenMinuteRunQueue_Type()
)
lsfFifteenMinuteRunQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfFifteenMinuteRunQueue.setStatus("mandatory")
_LsfCPUUtilization_Type = Integer32
_LsfCPUUtilization_Object = MibTableColumn
lsfCPUUtilization = _LsfCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 6),
    _LsfCPUUtilization_Type()
)
lsfCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfCPUUtilization.setStatus("mandatory")
_LsfPagingRate_Type = Integer32
_LsfPagingRate_Object = MibTableColumn
lsfPagingRate = _LsfPagingRate_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 7),
    _LsfPagingRate_Type()
)
lsfPagingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfPagingRate.setStatus("mandatory")
_LsfIoRate_Type = Integer32
_LsfIoRate_Object = MibTableColumn
lsfIoRate = _LsfIoRate_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 8),
    _LsfIoRate_Type()
)
lsfIoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfIoRate.setStatus("mandatory")
_LsfLoginSessions_Type = Integer32
_LsfLoginSessions_Object = MibTableColumn
lsfLoginSessions = _LsfLoginSessions_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 9),
    _LsfLoginSessions_Type()
)
lsfLoginSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfLoginSessions.setStatus("mandatory")
_LsfIdleTime_Type = Integer32
_LsfIdleTime_Object = MibTableColumn
lsfIdleTime = _LsfIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 10),
    _LsfIdleTime_Type()
)
lsfIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfIdleTime.setStatus("mandatory")
_LsfFreeMemory_Type = Integer32
_LsfFreeMemory_Object = MibTableColumn
lsfFreeMemory = _LsfFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 11),
    _LsfFreeMemory_Type()
)
lsfFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfFreeMemory.setStatus("mandatory")
_LsfFreeSwap_Type = Integer32
_LsfFreeSwap_Object = MibTableColumn
lsfFreeSwap = _LsfFreeSwap_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 12),
    _LsfFreeSwap_Type()
)
lsfFreeSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfFreeSwap.setStatus("mandatory")
_LsfFreeTempSpace_Type = Integer32
_LsfFreeTempSpace_Object = MibTableColumn
lsfFreeTempSpace = _LsfFreeTempSpace_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 2, 1, 13),
    _LsfFreeTempSpace_Type()
)
lsfFreeTempSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfFreeTempSpace.setStatus("mandatory")
_LsfNumClusterHosts_Type = Integer32
_LsfNumClusterHosts_Object = MibScalar
lsfNumClusterHosts = _LsfNumClusterHosts_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 1, 3),
    _LsfNumClusterHosts_Type()
)
lsfNumClusterHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfNumClusterHosts.setStatus("mandatory")
_LsfResources_ObjectIdentity = ObjectIdentity
lsfResources = _LsfResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2766, 100, 2)
)
_LsfNumericTable_Object = MibTable
lsfNumericTable = _LsfNumericTable_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 2, 1)
)
if mibBuilder.loadTexts:
    lsfNumericTable.setStatus("mandatory")
_LsfNumericEntry_Object = MibTableRow
lsfNumericEntry = _LsfNumericEntry_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1)
)
lsfNumericEntry.setIndexNames(
    (0, "LSF-SNMP-MIB", "lsfNumericIndex"),
    (0, "LSF-SNMP-MIB", "lsfNumericIP"),
)
if mibBuilder.loadTexts:
    lsfNumericEntry.setStatus("mandatory")
_LsfNumericIndex_Type = Integer32
_LsfNumericIndex_Object = MibTableColumn
lsfNumericIndex = _LsfNumericIndex_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 1),
    _LsfNumericIndex_Type()
)
lsfNumericIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfNumericIndex.setStatus("mandatory")
_LsfNumericIP_Type = IpAddress
_LsfNumericIP_Object = MibScalar
lsfNumericIP = _LsfNumericIP_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 2),
    _LsfNumericIP_Type()
)
lsfNumericIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfNumericIP.setStatus("mandatory")


class _LsfNumericLocation_Type(DisplayString):
    """Custom type lsfNumericLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsfNumericLocation_Type.__name__ = "DisplayString"
_LsfNumericLocation_Object = MibTableColumn
lsfNumericLocation = _LsfNumericLocation_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 3),
    _LsfNumericLocation_Type()
)
lsfNumericLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfNumericLocation.setStatus("mandatory")


class _LsfNumericName_Type(DisplayString):
    """Custom type lsfNumericName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsfNumericName_Type.__name__ = "DisplayString"
_LsfNumericName_Object = MibTableColumn
lsfNumericName = _LsfNumericName_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 4),
    _LsfNumericName_Type()
)
lsfNumericName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfNumericName.setStatus("mandatory")


class _LsfNumericOrder_Type(Integer32):
    """Custom type lsfNumericOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 1),
          ("descending", 2))
    )


_LsfNumericOrder_Type.__name__ = "Integer32"
_LsfNumericOrder_Object = MibTableColumn
lsfNumericOrder = _LsfNumericOrder_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 5),
    _LsfNumericOrder_Type()
)
lsfNumericOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfNumericOrder.setStatus("mandatory")
_LsfNumericValue_Type = Integer32
_LsfNumericValue_Object = MibTableColumn
lsfNumericValue = _LsfNumericValue_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 2, 1, 1, 6),
    _LsfNumericValue_Type()
)
lsfNumericValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfNumericValue.setStatus("mandatory")
_LsfBatch_ObjectIdentity = ObjectIdentity
lsfBatch = _LsfBatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3)
)
_LsbHostTable_Object = MibTable
lsbHostTable = _LsbHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1)
)
if mibBuilder.loadTexts:
    lsbHostTable.setStatus("mandatory")
_LsbHostEntry_Object = MibTableRow
lsbHostEntry = _LsbHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1)
)
lsbHostEntry.setIndexNames(
    (0, "LSF-SNMP-MIB", "lsbHostIp"),
)
if mibBuilder.loadTexts:
    lsbHostEntry.setStatus("mandatory")
_LsbHostIp_Type = IpAddress
_LsbHostIp_Object = MibTableColumn
lsbHostIp = _LsbHostIp_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 1),
    _LsbHostIp_Type()
)
lsbHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbHostIp.setStatus("mandatory")


class _LsbHostName_Type(DisplayString):
    """Custom type lsbHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbHostName_Type.__name__ = "DisplayString"
_LsbHostName_Object = MibTableColumn
lsbHostName = _LsbHostName_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 2),
    _LsbHostName_Type()
)
lsbHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbHostName.setStatus("mandatory")


class _LsbHostStatus_Type(Integer32):
    """Custom type lsbHostStatus based on Integer32"""
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
        *(("closed", 4),
          ("ok", 1),
          ("unavail", 2),
          ("unlicensed", 5),
          ("unreach", 3))
    )


_LsbHostStatus_Type.__name__ = "Integer32"
_LsbHostStatus_Object = MibTableColumn
lsbHostStatus = _LsbHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 3),
    _LsbHostStatus_Type()
)
lsbHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsbHostStatus.setStatus("mandatory")
_LsbHostUserJobLimit_Type = Integer32
_LsbHostUserJobLimit_Object = MibTableColumn
lsbHostUserJobLimit = _LsbHostUserJobLimit_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 4),
    _LsbHostUserJobLimit_Type()
)
lsbHostUserJobLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbHostUserJobLimit.setStatus("mandatory")
_LsbHostMaximumJobs_Type = Integer32
_LsbHostMaximumJobs_Object = MibTableColumn
lsbHostMaximumJobs = _LsbHostMaximumJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 5),
    _LsbHostMaximumJobs_Type()
)
lsbHostMaximumJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbHostMaximumJobs.setStatus("mandatory")
_LsbHostNumberOfJobs_Type = Integer32
_LsbHostNumberOfJobs_Object = MibTableColumn
lsbHostNumberOfJobs = _LsbHostNumberOfJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 6),
    _LsbHostNumberOfJobs_Type()
)
lsbHostNumberOfJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbHostNumberOfJobs.setStatus("mandatory")
_LsbHostRunningJobs_Type = Integer32
_LsbHostRunningJobs_Object = MibTableColumn
lsbHostRunningJobs = _LsbHostRunningJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 7),
    _LsbHostRunningJobs_Type()
)
lsbHostRunningJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbHostRunningJobs.setStatus("mandatory")
_LsbSystemSuspendedJobs_Type = Integer32
_LsbSystemSuspendedJobs_Object = MibScalar
lsbSystemSuspendedJobs = _LsbSystemSuspendedJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 8),
    _LsbSystemSuspendedJobs_Type()
)
lsbSystemSuspendedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbSystemSuspendedJobs.setStatus("mandatory")
_LsbUserSuspendedJobs_Type = Integer32
_LsbUserSuspendedJobs_Object = MibScalar
lsbUserSuspendedJobs = _LsbUserSuspendedJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 9),
    _LsbUserSuspendedJobs_Type()
)
lsbUserSuspendedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbUserSuspendedJobs.setStatus("mandatory")
_LsbHostReservedJobSlots_Type = Integer32
_LsbHostReservedJobSlots_Object = MibTableColumn
lsbHostReservedJobSlots = _LsbHostReservedJobSlots_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 1, 1, 10),
    _LsbHostReservedJobSlots_Type()
)
lsbHostReservedJobSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbHostReservedJobSlots.setStatus("mandatory")
_LsbQueueTable_Object = MibTable
lsbQueueTable = _LsbQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2)
)
if mibBuilder.loadTexts:
    lsbQueueTable.setStatus("mandatory")
_LsbQueueEntry_Object = MibTableRow
lsbQueueEntry = _LsbQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1)
)
lsbQueueEntry.setIndexNames(
    (0, "LSF-SNMP-MIB", "lsbQueueIndex"),
)
if mibBuilder.loadTexts:
    lsbQueueEntry.setStatus("mandatory")
_LsbQueueIndex_Type = Integer32
_LsbQueueIndex_Object = MibTableColumn
lsbQueueIndex = _LsbQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 1),
    _LsbQueueIndex_Type()
)
lsbQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueIndex.setStatus("mandatory")


class _LsbQueueName_Type(DisplayString):
    """Custom type lsbQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbQueueName_Type.__name__ = "DisplayString"
_LsbQueueName_Object = MibTableColumn
lsbQueueName = _LsbQueueName_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 2),
    _LsbQueueName_Type()
)
lsbQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueName.setStatus("mandatory")
_LsbQueuePriority_Type = Integer32
_LsbQueuePriority_Object = MibTableColumn
lsbQueuePriority = _LsbQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 3),
    _LsbQueuePriority_Type()
)
lsbQueuePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueuePriority.setStatus("mandatory")


class _LsbQueueIsOpen_Type(Integer32):
    """Custom type lsbQueueIsOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )


_LsbQueueIsOpen_Type.__name__ = "Integer32"
_LsbQueueIsOpen_Object = MibTableColumn
lsbQueueIsOpen = _LsbQueueIsOpen_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 4),
    _LsbQueueIsOpen_Type()
)
lsbQueueIsOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsbQueueIsOpen.setStatus("mandatory")


class _LsbQueueIsActive_Type(Integer32):
    """Custom type lsbQueueIsActive based on Integer32"""
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


_LsbQueueIsActive_Type.__name__ = "Integer32"
_LsbQueueIsActive_Object = MibTableColumn
lsbQueueIsActive = _LsbQueueIsActive_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 5),
    _LsbQueueIsActive_Type()
)
lsbQueueIsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsbQueueIsActive.setStatus("mandatory")
_LsbQueueMaximumJobs_Type = Integer32
_LsbQueueMaximumJobs_Object = MibTableColumn
lsbQueueMaximumJobs = _LsbQueueMaximumJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 6),
    _LsbQueueMaximumJobs_Type()
)
lsbQueueMaximumJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueMaximumJobs.setStatus("mandatory")
_LsbQueueUserJobLimit_Type = Integer32
_LsbQueueUserJobLimit_Object = MibTableColumn
lsbQueueUserJobLimit = _LsbQueueUserJobLimit_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 7),
    _LsbQueueUserJobLimit_Type()
)
lsbQueueUserJobLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueUserJobLimit.setStatus("mandatory")
_LsbQueueProcessorJobLimit_Type = Integer32
_LsbQueueProcessorJobLimit_Object = MibTableColumn
lsbQueueProcessorJobLimit = _LsbQueueProcessorJobLimit_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 8),
    _LsbQueueProcessorJobLimit_Type()
)
lsbQueueProcessorJobLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueProcessorJobLimit.setStatus("mandatory")
_LsbQueueHostJobLimit_Type = Integer32
_LsbQueueHostJobLimit_Object = MibTableColumn
lsbQueueHostJobLimit = _LsbQueueHostJobLimit_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 9),
    _LsbQueueHostJobLimit_Type()
)
lsbQueueHostJobLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueHostJobLimit.setStatus("mandatory")
_LsbQueueNumberOfJobs_Type = Integer32
_LsbQueueNumberOfJobs_Object = MibTableColumn
lsbQueueNumberOfJobs = _LsbQueueNumberOfJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 10),
    _LsbQueueNumberOfJobs_Type()
)
lsbQueueNumberOfJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueNumberOfJobs.setStatus("mandatory")
_LsbQueuePendingJobs_Type = Integer32
_LsbQueuePendingJobs_Object = MibTableColumn
lsbQueuePendingJobs = _LsbQueuePendingJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 11),
    _LsbQueuePendingJobs_Type()
)
lsbQueuePendingJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueuePendingJobs.setStatus("mandatory")
_LsbQueueRunningJobs_Type = Integer32
_LsbQueueRunningJobs_Object = MibTableColumn
lsbQueueRunningJobs = _LsbQueueRunningJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 12),
    _LsbQueueRunningJobs_Type()
)
lsbQueueRunningJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueRunningJobs.setStatus("mandatory")
_LsbQueueSystemSuspendedJobs_Type = Integer32
_LsbQueueSystemSuspendedJobs_Object = MibTableColumn
lsbQueueSystemSuspendedJobs = _LsbQueueSystemSuspendedJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 13),
    _LsbQueueSystemSuspendedJobs_Type()
)
lsbQueueSystemSuspendedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueSystemSuspendedJobs.setStatus("mandatory")
_LsbQueueUserSuspendedJobs_Type = Integer32
_LsbQueueUserSuspendedJobs_Object = MibTableColumn
lsbQueueUserSuspendedJobs = _LsbQueueUserSuspendedJobs_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 2, 1, 14),
    _LsbQueueUserSuspendedJobs_Type()
)
lsbQueueUserSuspendedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbQueueUserSuspendedJobs.setStatus("mandatory")
_LsbJobTable_Object = MibTable
lsbJobTable = _LsbJobTable_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3)
)
if mibBuilder.loadTexts:
    lsbJobTable.setStatus("mandatory")
_LsbJobEntry_Object = MibTableRow
lsbJobEntry = _LsbJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1)
)
lsbJobEntry.setIndexNames(
    (0, "LSF-SNMP-MIB", "lsbJobId"),
)
if mibBuilder.loadTexts:
    lsbJobEntry.setStatus("mandatory")
_LsbJobId_Type = Integer32
_LsbJobId_Object = MibTableColumn
lsbJobId = _LsbJobId_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 1),
    _LsbJobId_Type()
)
lsbJobId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobId.setStatus("mandatory")


class _LsbJobName_Type(DisplayString):
    """Custom type lsbJobName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbJobName_Type.__name__ = "DisplayString"
_LsbJobName_Object = MibTableColumn
lsbJobName = _LsbJobName_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 2),
    _LsbJobName_Type()
)
lsbJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobName.setStatus("mandatory")


class _LsbJobUser_Type(DisplayString):
    """Custom type lsbJobUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbJobUser_Type.__name__ = "DisplayString"
_LsbJobUser_Object = MibTableColumn
lsbJobUser = _LsbJobUser_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 3),
    _LsbJobUser_Type()
)
lsbJobUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobUser.setStatus("mandatory")


class _LsbJobQueue_Type(DisplayString):
    """Custom type lsbJobQueue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbJobQueue_Type.__name__ = "DisplayString"
_LsbJobQueue_Object = MibTableColumn
lsbJobQueue = _LsbJobQueue_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 4),
    _LsbJobQueue_Type()
)
lsbJobQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobQueue.setStatus("mandatory")


class _LsbJobStatus_Type(Integer32):
    """Custom type lsbJobStatus based on Integer32"""
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
        *(("done", 6),
          ("exit", 7),
          ("pending", 1),
          ("psusp", 2),
          ("running", 3),
          ("ssusp", 5),
          ("unknown", 8),
          ("ususp", 4),
          ("zombie", 9))
    )


_LsbJobStatus_Type.__name__ = "Integer32"
_LsbJobStatus_Object = MibTableColumn
lsbJobStatus = _LsbJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 5),
    _LsbJobStatus_Type()
)
lsbJobStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobStatus.setStatus("mandatory")


class _LsbJobSubmissionHost_Type(DisplayString):
    """Custom type lsbJobSubmissionHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbJobSubmissionHost_Type.__name__ = "DisplayString"
_LsbJobSubmissionHost_Object = MibTableColumn
lsbJobSubmissionHost = _LsbJobSubmissionHost_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 6),
    _LsbJobSubmissionHost_Type()
)
lsbJobSubmissionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobSubmissionHost.setStatus("mandatory")


class _LsbJobExecutionHost_Type(DisplayString):
    """Custom type lsbJobExecutionHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbJobExecutionHost_Type.__name__ = "DisplayString"
_LsbJobExecutionHost_Object = MibTableColumn
lsbJobExecutionHost = _LsbJobExecutionHost_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 7),
    _LsbJobExecutionHost_Type()
)
lsbJobExecutionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobExecutionHost.setStatus("mandatory")


class _LsbJobSubmitTime_Type(DisplayString):
    """Custom type lsbJobSubmitTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbJobSubmitTime_Type.__name__ = "DisplayString"
_LsbJobSubmitTime_Object = MibTableColumn
lsbJobSubmitTime = _LsbJobSubmitTime_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 8),
    _LsbJobSubmitTime_Type()
)
lsbJobSubmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobSubmitTime.setStatus("mandatory")


class _LsbJobProcessGroupIds_Type(DisplayString):
    """Custom type lsbJobProcessGroupIds based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbJobProcessGroupIds_Type.__name__ = "DisplayString"
_LsbJobProcessGroupIds_Object = MibTableColumn
lsbJobProcessGroupIds = _LsbJobProcessGroupIds_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 9),
    _LsbJobProcessGroupIds_Type()
)
lsbJobProcessGroupIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobProcessGroupIds.setStatus("mandatory")


class _LsbJobProcessIds_Type(DisplayString):
    """Custom type lsbJobProcessIds based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsbJobProcessIds_Type.__name__ = "DisplayString"
_LsbJobProcessIds_Object = MibTableColumn
lsbJobProcessIds = _LsbJobProcessIds_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 10),
    _LsbJobProcessIds_Type()
)
lsbJobProcessIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobProcessIds.setStatus("mandatory")
_LsbJobCpuUsage_Type = Integer32
_LsbJobCpuUsage_Object = MibTableColumn
lsbJobCpuUsage = _LsbJobCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 11),
    _LsbJobCpuUsage_Type()
)
lsbJobCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobCpuUsage.setStatus("mandatory")
_LsbJobMemoryUsage_Type = Integer32
_LsbJobMemoryUsage_Object = MibTableColumn
lsbJobMemoryUsage = _LsbJobMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 12),
    _LsbJobMemoryUsage_Type()
)
lsbJobMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobMemoryUsage.setStatus("mandatory")
_LsbJobVirtualMemoryUsage_Type = Integer32
_LsbJobVirtualMemoryUsage_Object = MibScalar
lsbJobVirtualMemoryUsage = _LsbJobVirtualMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 3, 3, 1, 13),
    _LsbJobVirtualMemoryUsage_Type()
)
lsbJobVirtualMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsbJobVirtualMemoryUsage.setStatus("mandatory")
_LsfCluster_ObjectIdentity = ObjectIdentity
lsfCluster = _LsfCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2766, 100, 4)
)


class _LsfClusterName_Type(DisplayString):
    """Custom type lsfClusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsfClusterName_Type.__name__ = "DisplayString"
_LsfClusterName_Object = MibScalar
lsfClusterName = _LsfClusterName_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 4, 1),
    _LsfClusterName_Type()
)
lsfClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfClusterName.setStatus("mandatory")


class _LsfMasterName_Type(DisplayString):
    """Custom type lsfMasterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LsfMasterName_Type.__name__ = "DisplayString"
_LsfMasterName_Object = MibScalar
lsfMasterName = _LsfMasterName_Object(
    (1, 3, 6, 1, 4, 1, 2766, 100, 4, 2),
    _LsfMasterName_Type()
)
lsfMasterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsfMasterName.setStatus("mandatory")
_LsfEvents_ObjectIdentity = ObjectIdentity
lsfEvents = _LsfEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2766, 1000)
)

# Managed Objects groups


# Notification objects

lsfLimDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 1)
)
lsfLimDown.setObjects(
      *(("LSF-SNMP-MIB", "lsfClusterName"),
        ("LSF-SNMP-MIB", "lsfHostStatus"))
)
if mibBuilder.loadTexts:
    lsfLimDown.setStatus(
        ""
    )

lsfResDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 2)
)
lsfResDown.setObjects(
      *(("LSF-SNMP-MIB", "lsfClusterName"),
        ("LSF-SNMP-MIB", "lsfHostStatus"))
)
if mibBuilder.loadTexts:
    lsfResDown.setStatus(
        ""
    )

lsfSbdDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 3)
)
lsfSbdDown.setObjects(
      *(("LSF-SNMP-MIB", "lsfClusterName"),
        ("LSF-SNMP-MIB", "lsbHostStatus"))
)
if mibBuilder.loadTexts:
    lsfSbdDown.setStatus(
        ""
    )

lsfHostUnlicensed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 4)
)
lsfHostUnlicensed.setObjects(
      *(("LSF-SNMP-MIB", "lsfClusterName"),
        ("LSF-SNMP-MIB", "lsfHostStatus"))
)
if mibBuilder.loadTexts:
    lsfHostUnlicensed.setStatus(
        ""
    )

lsfMasterElect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 5)
)
lsfMasterElect.setObjects(
      *(("LSF-SNMP-MIB", "lsfClusterName"),
        ("LSF-SNMP-MIB", "lsfHostName"))
)
if mibBuilder.loadTexts:
    lsfMasterElect.setStatus(
        ""
    )

lsfMasterResign = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 6)
)
lsfMasterResign.setObjects(
      *(("LSF-SNMP-MIB", "lsfClusterName"),
        ("LSF-SNMP-MIB", "lsfHostName"))
)
if mibBuilder.loadTexts:
    lsfMasterResign.setStatus(
        ""
    )

lsfMbdUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 7)
)
lsfMbdUp.setObjects(
      *(("LSF-SNMP-MIB", "lsfClusterName"),
        ("LSF-SNMP-MIB", "lsbHostName"))
)
if mibBuilder.loadTexts:
    lsfMbdUp.setStatus(
        ""
    )

lsfMbdDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 8)
)
lsfMbdDown.setObjects(
      *(("LSF-SNMP-MIB", "lsfClusterName"),
        ("LSF-SNMP-MIB", "lsbHostName"))
)
if mibBuilder.loadTexts:
    lsfMbdDown.setStatus(
        ""
    )

lsfMbdReconfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 9)
)
lsfMbdReconfig.setObjects(
      *(("LSF-SNMP-MIB", "lsfClusterName"),
        ("LSF-SNMP-MIB", "lsbHostName"))
)
if mibBuilder.loadTexts:
    lsfMbdReconfig.setStatus(
        ""
    )

lsfWorkdirFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 2766, 1000, 0, 10)
)
lsfWorkdirFull.setObjects(
    ("LSF-SNMP-MIB", "lsfClusterName")
)
if mibBuilder.loadTexts:
    lsfWorkdirFull.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LSF-SNMP-MIB",
    **{"platform": platform,
       "lsfAgent": lsfAgent,
       "lsfHosts": lsfHosts,
       "lsfStaticTable": lsfStaticTable,
       "lsfStaticEntry": lsfStaticEntry,
       "lsfStaticIpIndex": lsfStaticIpIndex,
       "lsfHostName": lsfHostName,
       "lsfType": lsfType,
       "lsfModel": lsfModel,
       "lsfCPUFactor": lsfCPUFactor,
       "lsfNumCPU": lsfNumCPU,
       "lsfMaxMemory": lsfMaxMemory,
       "lsfMaxSwap": lsfMaxSwap,
       "lsfMaxTempSpace": lsfMaxTempSpace,
       "lsfExecutionPriority": lsfExecutionPriority,
       "lsfIsServer": lsfIsServer,
       "lsfHostResources": lsfHostResources,
       "lsfDynamicTable": lsfDynamicTable,
       "lsfDynamicEntry": lsfDynamicEntry,
       "lsfDynamicIpIndex": lsfDynamicIpIndex,
       "lsfHostStatus": lsfHostStatus,
       "lsfFifteenSecondRunQueue": lsfFifteenSecondRunQueue,
       "lsfOneMinuteRunQueue": lsfOneMinuteRunQueue,
       "lsfFifteenMinuteRunQueue": lsfFifteenMinuteRunQueue,
       "lsfCPUUtilization": lsfCPUUtilization,
       "lsfPagingRate": lsfPagingRate,
       "lsfIoRate": lsfIoRate,
       "lsfLoginSessions": lsfLoginSessions,
       "lsfIdleTime": lsfIdleTime,
       "lsfFreeMemory": lsfFreeMemory,
       "lsfFreeSwap": lsfFreeSwap,
       "lsfFreeTempSpace": lsfFreeTempSpace,
       "lsfNumClusterHosts": lsfNumClusterHosts,
       "lsfResources": lsfResources,
       "lsfNumericTable": lsfNumericTable,
       "lsfNumericEntry": lsfNumericEntry,
       "lsfNumericIndex": lsfNumericIndex,
       "lsfNumericIP": lsfNumericIP,
       "lsfNumericLocation": lsfNumericLocation,
       "lsfNumericName": lsfNumericName,
       "lsfNumericOrder": lsfNumericOrder,
       "lsfNumericValue": lsfNumericValue,
       "lsfBatch": lsfBatch,
       "lsbHostTable": lsbHostTable,
       "lsbHostEntry": lsbHostEntry,
       "lsbHostIp": lsbHostIp,
       "lsbHostName": lsbHostName,
       "lsbHostStatus": lsbHostStatus,
       "lsbHostUserJobLimit": lsbHostUserJobLimit,
       "lsbHostMaximumJobs": lsbHostMaximumJobs,
       "lsbHostNumberOfJobs": lsbHostNumberOfJobs,
       "lsbHostRunningJobs": lsbHostRunningJobs,
       "lsbSystemSuspendedJobs": lsbSystemSuspendedJobs,
       "lsbUserSuspendedJobs": lsbUserSuspendedJobs,
       "lsbHostReservedJobSlots": lsbHostReservedJobSlots,
       "lsbQueueTable": lsbQueueTable,
       "lsbQueueEntry": lsbQueueEntry,
       "lsbQueueIndex": lsbQueueIndex,
       "lsbQueueName": lsbQueueName,
       "lsbQueuePriority": lsbQueuePriority,
       "lsbQueueIsOpen": lsbQueueIsOpen,
       "lsbQueueIsActive": lsbQueueIsActive,
       "lsbQueueMaximumJobs": lsbQueueMaximumJobs,
       "lsbQueueUserJobLimit": lsbQueueUserJobLimit,
       "lsbQueueProcessorJobLimit": lsbQueueProcessorJobLimit,
       "lsbQueueHostJobLimit": lsbQueueHostJobLimit,
       "lsbQueueNumberOfJobs": lsbQueueNumberOfJobs,
       "lsbQueuePendingJobs": lsbQueuePendingJobs,
       "lsbQueueRunningJobs": lsbQueueRunningJobs,
       "lsbQueueSystemSuspendedJobs": lsbQueueSystemSuspendedJobs,
       "lsbQueueUserSuspendedJobs": lsbQueueUserSuspendedJobs,
       "lsbJobTable": lsbJobTable,
       "lsbJobEntry": lsbJobEntry,
       "lsbJobId": lsbJobId,
       "lsbJobName": lsbJobName,
       "lsbJobUser": lsbJobUser,
       "lsbJobQueue": lsbJobQueue,
       "lsbJobStatus": lsbJobStatus,
       "lsbJobSubmissionHost": lsbJobSubmissionHost,
       "lsbJobExecutionHost": lsbJobExecutionHost,
       "lsbJobSubmitTime": lsbJobSubmitTime,
       "lsbJobProcessGroupIds": lsbJobProcessGroupIds,
       "lsbJobProcessIds": lsbJobProcessIds,
       "lsbJobCpuUsage": lsbJobCpuUsage,
       "lsbJobMemoryUsage": lsbJobMemoryUsage,
       "lsbJobVirtualMemoryUsage": lsbJobVirtualMemoryUsage,
       "lsfCluster": lsfCluster,
       "lsfClusterName": lsfClusterName,
       "lsfMasterName": lsfMasterName,
       "lsfEvents": lsfEvents,
       "lsfLimDown": lsfLimDown,
       "lsfResDown": lsfResDown,
       "lsfSbdDown": lsfSbdDown,
       "lsfHostUnlicensed": lsfHostUnlicensed,
       "lsfMasterElect": lsfMasterElect,
       "lsfMasterResign": lsfMasterResign,
       "lsfMbdUp": lsfMbdUp,
       "lsfMbdDown": lsfMbdDown,
       "lsfMbdReconfig": lsfMbdReconfig,
       "lsfWorkdirFull": lsfWorkdirFull}
)
