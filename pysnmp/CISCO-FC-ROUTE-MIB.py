# SNMP MIB module (CISCO-FC-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FC-ROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:17 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcAddressId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcAddressId",
    "VsanIndex")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoFcRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 284)
)
ciscoFcRouteMIB.setRevisions(
        ("2003-09-04 00:00",
         "2002-11-01 00:00",
         "2002-10-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFcRouteMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFcRouteMIBObjects = _CiscoFcRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1)
)
_FcRouteConfig_ObjectIdentity = ObjectIdentity
fcRouteConfig = _FcRouteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1)
)
_FcRouteLastChangeTime_Type = TimeStamp
_FcRouteLastChangeTime_Object = MibScalar
fcRouteLastChangeTime = _FcRouteLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 1),
    _FcRouteLastChangeTime_Type()
)
fcRouteLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRouteLastChangeTime.setStatus("current")


class _FcRoutePreference_Type(Unsigned32):
    """Custom type fcRoutePreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FcRoutePreference_Type.__name__ = "Unsigned32"
_FcRoutePreference_Object = MibScalar
fcRoutePreference = _FcRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 2),
    _FcRoutePreference_Type()
)
fcRoutePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcRoutePreference.setStatus("current")


class _FcRouteVerifyAction_Type(Integer32):
    """Custom type fcRouteVerifyAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("verify", 2))
    )


_FcRouteVerifyAction_Type.__name__ = "Integer32"
_FcRouteVerifyAction_Object = MibScalar
fcRouteVerifyAction = _FcRouteVerifyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 3),
    _FcRouteVerifyAction_Type()
)
fcRouteVerifyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcRouteVerifyAction.setStatus("current")


class _FcRouteVerifyType_Type(Integer32):
    """Custom type fcRouteVerifyType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fibHardware", 3),
          ("fibShadow", 2),
          ("pss", 1))
    )


_FcRouteVerifyType_Type.__name__ = "Integer32"
_FcRouteVerifyType_Object = MibScalar
fcRouteVerifyType = _FcRouteVerifyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 4),
    _FcRouteVerifyType_Type()
)
fcRouteVerifyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcRouteVerifyType.setStatus("current")
_FcRouteVerifyModule_Type = PhysicalIndex
_FcRouteVerifyModule_Object = MibScalar
fcRouteVerifyModule = _FcRouteVerifyModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 5),
    _FcRouteVerifyModule_Type()
)
fcRouteVerifyModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcRouteVerifyModule.setStatus("current")


class _FcRouteVerifyVsanID_Type(VsanIndex):
    """Custom type fcRouteVerifyVsanID based on VsanIndex"""
    subtypeSpec = VsanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_FcRouteVerifyVsanID_Type.__name__ = "VsanIndex"
_FcRouteVerifyVsanID_Object = MibScalar
fcRouteVerifyVsanID = _FcRouteVerifyVsanID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 6),
    _FcRouteVerifyVsanID_Type()
)
fcRouteVerifyVsanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcRouteVerifyVsanID.setStatus("current")


class _FcRouteVerifyRouteType_Type(Integer32):
    """Custom type fcRouteVerifyRouteType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("label", 3),
          ("multicast", 2),
          ("unicast", 1))
    )


_FcRouteVerifyRouteType_Type.__name__ = "Integer32"
_FcRouteVerifyRouteType_Object = MibScalar
fcRouteVerifyRouteType = _FcRouteVerifyRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 7),
    _FcRouteVerifyRouteType_Type()
)
fcRouteVerifyRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcRouteVerifyRouteType.setStatus("current")
_FcRouteVerifyResult_Type = SnmpAdminString
_FcRouteVerifyResult_Object = MibScalar
fcRouteVerifyResult = _FcRouteVerifyResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 8),
    _FcRouteVerifyResult_Type()
)
fcRouteVerifyResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRouteVerifyResult.setStatus("current")
_FcRouteVerifyLock_Type = TestAndIncr
_FcRouteVerifyLock_Object = MibScalar
fcRouteVerifyLock = _FcRouteVerifyLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 9),
    _FcRouteVerifyLock_Type()
)
fcRouteVerifyLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcRouteVerifyLock.setStatus("current")
_FcRouteTable_Object = MibTable
fcRouteTable = _FcRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10)
)
if mibBuilder.loadTexts:
    fcRouteTable.setStatus("current")
_FcRouteEntry_Object = MibTableRow
fcRouteEntry = _FcRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1)
)
fcRouteEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FC-ROUTE-MIB", "fcRouteDestAddrId"),
    (0, "CISCO-FC-ROUTE-MIB", "fcRouteDestMask"),
    (0, "CISCO-FC-ROUTE-MIB", "fcRouteProto"),
    (0, "CISCO-FC-ROUTE-MIB", "fcRouteInterface"),
)
if mibBuilder.loadTexts:
    fcRouteEntry.setStatus("current")
_FcRouteDestAddrId_Type = FcAddressId
_FcRouteDestAddrId_Object = MibTableColumn
fcRouteDestAddrId = _FcRouteDestAddrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1, 1),
    _FcRouteDestAddrId_Type()
)
fcRouteDestAddrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcRouteDestAddrId.setStatus("current")
_FcRouteDestMask_Type = FcAddressId
_FcRouteDestMask_Object = MibTableColumn
fcRouteDestMask = _FcRouteDestMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1, 2),
    _FcRouteDestMask_Type()
)
fcRouteDestMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcRouteDestMask.setStatus("current")


class _FcRouteProto_Type(Integer32):
    """Custom type fcRouteProto based on Integer32"""
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
        *(("fspf", 4),
          ("local", 2),
          ("mpls", 5),
          ("multicast", 6),
          ("netmgmt", 3),
          ("other", 1))
    )


_FcRouteProto_Type.__name__ = "Integer32"
_FcRouteProto_Object = MibTableColumn
fcRouteProto = _FcRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1, 3),
    _FcRouteProto_Type()
)
fcRouteProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcRouteProto.setStatus("current")
_FcRouteInterface_Type = InterfaceIndex
_FcRouteInterface_Object = MibTableColumn
fcRouteInterface = _FcRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1, 4),
    _FcRouteInterface_Type()
)
fcRouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcRouteInterface.setStatus("current")


class _FcRouteDomainId_Type(Unsigned32):
    """Custom type fcRouteDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 239),
    )


_FcRouteDomainId_Type.__name__ = "Unsigned32"
_FcRouteDomainId_Object = MibTableColumn
fcRouteDomainId = _FcRouteDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1, 5),
    _FcRouteDomainId_Type()
)
fcRouteDomainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteDomainId.setStatus("current")


class _FcRouteMetric_Type(Unsigned32):
    """Custom type fcRouteMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_FcRouteMetric_Type.__name__ = "Unsigned32"
_FcRouteMetric_Object = MibTableColumn
fcRouteMetric = _FcRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1, 6),
    _FcRouteMetric_Type()
)
fcRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteMetric.setStatus("current")


class _FcRouteType_Type(Integer32):
    """Custom type fcRouteType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_FcRouteType_Type.__name__ = "Integer32"
_FcRouteType_Object = MibTableColumn
fcRouteType = _FcRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1, 7),
    _FcRouteType_Type()
)
fcRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteType.setStatus("current")


class _FcRoutePermanent_Type(TruthValue):
    """Custom type fcRoutePermanent based on TruthValue"""


_FcRoutePermanent_Object = MibTableColumn
fcRoutePermanent = _FcRoutePermanent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1, 8),
    _FcRoutePermanent_Type()
)
fcRoutePermanent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRoutePermanent.setStatus("current")
_FcRouteRowStatus_Type = RowStatus
_FcRouteRowStatus_Object = MibTableColumn
fcRouteRowStatus = _FcRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 1, 10, 1, 9),
    _FcRouteRowStatus_Type()
)
fcRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteRowStatus.setStatus("current")
_FcRouteStatistics_ObjectIdentity = ObjectIdentity
fcRouteStatistics = _FcRouteStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2)
)
_FcRouteFlowStatTable_Object = MibTable
fcRouteFlowStatTable = _FcRouteFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fcRouteFlowStatTable.setStatus("current")
_FcRouteFlowStatEntry_Object = MibTableRow
fcRouteFlowStatEntry = _FcRouteFlowStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1)
)
fcRouteFlowStatEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-FC-ROUTE-MIB", "fcRouteFlowIndex"),
)
if mibBuilder.loadTexts:
    fcRouteFlowStatEntry.setStatus("current")


class _FcRouteFlowIndex_Type(Unsigned32):
    """Custom type fcRouteFlowIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FcRouteFlowIndex_Type.__name__ = "Unsigned32"
_FcRouteFlowIndex_Object = MibTableColumn
fcRouteFlowIndex = _FcRouteFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 1),
    _FcRouteFlowIndex_Type()
)
fcRouteFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcRouteFlowIndex.setStatus("current")


class _FcRouteFlowType_Type(Bits):
    """Custom type fcRouteFlowType based on Bits"""
    namedValues = NamedValues(
        *(("destId", 1),
          ("port", 3),
          ("srcId", 2),
          ("vsanId", 0))
    )

_FcRouteFlowType_Type.__name__ = "Bits"
_FcRouteFlowType_Object = MibTableColumn
fcRouteFlowType = _FcRouteFlowType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 2),
    _FcRouteFlowType_Type()
)
fcRouteFlowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteFlowType.setStatus("current")


class _FcRouteFlowVsanId_Type(VsanIndex):
    """Custom type fcRouteFlowVsanId based on VsanIndex"""
    subtypeSpec = VsanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_FcRouteFlowVsanId_Type.__name__ = "VsanIndex"
_FcRouteFlowVsanId_Object = MibTableColumn
fcRouteFlowVsanId = _FcRouteFlowVsanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 3),
    _FcRouteFlowVsanId_Type()
)
fcRouteFlowVsanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteFlowVsanId.setStatus("current")
_FcRouteFlowDestId_Type = FcAddressId
_FcRouteFlowDestId_Object = MibTableColumn
fcRouteFlowDestId = _FcRouteFlowDestId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 4),
    _FcRouteFlowDestId_Type()
)
fcRouteFlowDestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteFlowDestId.setStatus("current")
_FcRouteFlowSrcId_Type = FcAddressId
_FcRouteFlowSrcId_Object = MibTableColumn
fcRouteFlowSrcId = _FcRouteFlowSrcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 5),
    _FcRouteFlowSrcId_Type()
)
fcRouteFlowSrcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteFlowSrcId.setStatus("current")
_FcRouteFlowMask_Type = FcAddressId
_FcRouteFlowMask_Object = MibTableColumn
fcRouteFlowMask = _FcRouteFlowMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 6),
    _FcRouteFlowMask_Type()
)
fcRouteFlowMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteFlowMask.setStatus("current")
_FcRouteFlowPort_Type = InterfaceIndex
_FcRouteFlowPort_Object = MibTableColumn
fcRouteFlowPort = _FcRouteFlowPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 7),
    _FcRouteFlowPort_Type()
)
fcRouteFlowPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteFlowPort.setStatus("current")
_FcRouteFlowFrames_Type = Counter64
_FcRouteFlowFrames_Object = MibTableColumn
fcRouteFlowFrames = _FcRouteFlowFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 8),
    _FcRouteFlowFrames_Type()
)
fcRouteFlowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRouteFlowFrames.setStatus("current")
_FcRouteFlowBytes_Type = Counter64
_FcRouteFlowBytes_Object = MibTableColumn
fcRouteFlowBytes = _FcRouteFlowBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 9),
    _FcRouteFlowBytes_Type()
)
fcRouteFlowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRouteFlowBytes.setStatus("current")
_FcRouteFlowCreationTime_Type = TimeStamp
_FcRouteFlowCreationTime_Object = MibTableColumn
fcRouteFlowCreationTime = _FcRouteFlowCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 11),
    _FcRouteFlowCreationTime_Type()
)
fcRouteFlowCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRouteFlowCreationTime.setStatus("current")
_FcRouteFlowRowStatus_Type = RowStatus
_FcRouteFlowRowStatus_Object = MibTableColumn
fcRouteFlowRowStatus = _FcRouteFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 2, 1, 1, 12),
    _FcRouteFlowRowStatus_Type()
)
fcRouteFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fcRouteFlowRowStatus.setStatus("current")
_FcRouteNotification_ObjectIdentity = ObjectIdentity
fcRouteNotification = _FcRouteNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 3)
)
_FcRouteNotifications_ObjectIdentity = ObjectIdentity
fcRouteNotifications = _FcRouteNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 1, 3, 0)
)
_FcRouteMIBConformance_ObjectIdentity = ObjectIdentity
fcRouteMIBConformance = _FcRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 2)
)
_FcRouteMIBCompliances_ObjectIdentity = ObjectIdentity
fcRouteMIBCompliances = _FcRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 2, 1)
)
_FcRouteMIBGroups_ObjectIdentity = ObjectIdentity
fcRouteMIBGroups = _FcRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 2, 2)
)

# Managed Objects groups

fcRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 2, 2, 1)
)
fcRouteGroup.setObjects(
      *(("CISCO-FC-ROUTE-MIB", "fcRouteLastChangeTime"),
        ("CISCO-FC-ROUTE-MIB", "fcRoutePreference"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteVerifyAction"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteVerifyType"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteVerifyModule"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteVerifyVsanID"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteVerifyRouteType"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteVerifyResult"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteVerifyLock"))
)
if mibBuilder.loadTexts:
    fcRouteGroup.setStatus("current")

fcRouteTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 2, 2, 2)
)
fcRouteTableGroup.setObjects(
      *(("CISCO-FC-ROUTE-MIB", "fcRouteDomainId"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteMetric"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteType"),
        ("CISCO-FC-ROUTE-MIB", "fcRoutePermanent"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteRowStatus"))
)
if mibBuilder.loadTexts:
    fcRouteTableGroup.setStatus("current")

fcRouteStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 2, 2, 3)
)
fcRouteStatGroup.setObjects(
      *(("CISCO-FC-ROUTE-MIB", "fcRouteFlowType"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteFlowVsanId"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteFlowDestId"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteFlowSrcId"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteFlowMask"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteFlowPort"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteFlowFrames"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteFlowBytes"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteFlowCreationTime"),
        ("CISCO-FC-ROUTE-MIB", "fcRouteFlowRowStatus"))
)
if mibBuilder.loadTexts:
    fcRouteStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fcRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcRouteMIBCompliance.setStatus(
        "deprecated"
    )

fcRouteMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 284, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fcRouteMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FC-ROUTE-MIB",
    **{"ciscoFcRouteMIB": ciscoFcRouteMIB,
       "ciscoFcRouteMIBObjects": ciscoFcRouteMIBObjects,
       "fcRouteConfig": fcRouteConfig,
       "fcRouteLastChangeTime": fcRouteLastChangeTime,
       "fcRoutePreference": fcRoutePreference,
       "fcRouteVerifyAction": fcRouteVerifyAction,
       "fcRouteVerifyType": fcRouteVerifyType,
       "fcRouteVerifyModule": fcRouteVerifyModule,
       "fcRouteVerifyVsanID": fcRouteVerifyVsanID,
       "fcRouteVerifyRouteType": fcRouteVerifyRouteType,
       "fcRouteVerifyResult": fcRouteVerifyResult,
       "fcRouteVerifyLock": fcRouteVerifyLock,
       "fcRouteTable": fcRouteTable,
       "fcRouteEntry": fcRouteEntry,
       "fcRouteDestAddrId": fcRouteDestAddrId,
       "fcRouteDestMask": fcRouteDestMask,
       "fcRouteProto": fcRouteProto,
       "fcRouteInterface": fcRouteInterface,
       "fcRouteDomainId": fcRouteDomainId,
       "fcRouteMetric": fcRouteMetric,
       "fcRouteType": fcRouteType,
       "fcRoutePermanent": fcRoutePermanent,
       "fcRouteRowStatus": fcRouteRowStatus,
       "fcRouteStatistics": fcRouteStatistics,
       "fcRouteFlowStatTable": fcRouteFlowStatTable,
       "fcRouteFlowStatEntry": fcRouteFlowStatEntry,
       "fcRouteFlowIndex": fcRouteFlowIndex,
       "fcRouteFlowType": fcRouteFlowType,
       "fcRouteFlowVsanId": fcRouteFlowVsanId,
       "fcRouteFlowDestId": fcRouteFlowDestId,
       "fcRouteFlowSrcId": fcRouteFlowSrcId,
       "fcRouteFlowMask": fcRouteFlowMask,
       "fcRouteFlowPort": fcRouteFlowPort,
       "fcRouteFlowFrames": fcRouteFlowFrames,
       "fcRouteFlowBytes": fcRouteFlowBytes,
       "fcRouteFlowCreationTime": fcRouteFlowCreationTime,
       "fcRouteFlowRowStatus": fcRouteFlowRowStatus,
       "fcRouteNotification": fcRouteNotification,
       "fcRouteNotifications": fcRouteNotifications,
       "fcRouteMIBConformance": fcRouteMIBConformance,
       "fcRouteMIBCompliances": fcRouteMIBCompliances,
       "fcRouteMIBCompliance": fcRouteMIBCompliance,
       "fcRouteMIBCompliance1": fcRouteMIBCompliance1,
       "fcRouteMIBGroups": fcRouteMIBGroups,
       "fcRouteGroup": fcRouteGroup,
       "fcRouteTableGroup": fcRouteTableGroup,
       "fcRouteStatGroup": fcRouteStatGroup}
)
