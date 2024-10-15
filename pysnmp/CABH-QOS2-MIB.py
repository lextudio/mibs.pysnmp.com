# SNMP MIB module (CABH-QOS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CABH-QOS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:08 2024
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

(clabProjCableHome,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjCableHome")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cabhQos2Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8)
)
cabhQos2Mib.setRevisions(
        ("2005-04-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CabhQos2Mib2Notifications_ObjectIdentity = ObjectIdentity
cabhQos2Mib2Notifications = _CabhQos2Mib2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 0)
)
_CabhQos2MibObjects_ObjectIdentity = ObjectIdentity
cabhQos2MibObjects = _CabhQos2MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1)
)
_CabhQos2Base_ObjectIdentity = ObjectIdentity
cabhQos2Base = _CabhQos2Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 1)
)
_CabhQos2SetToFactory_Type = TruthValue
_CabhQos2SetToFactory_Object = MibScalar
cabhQos2SetToFactory = _CabhQos2SetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 1, 1),
    _CabhQos2SetToFactory_Type()
)
cabhQos2SetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhQos2SetToFactory.setStatus("current")
_CabhQos2LastSetToFactory_Type = TimeStamp
_CabhQos2LastSetToFactory_Object = MibScalar
cabhQos2LastSetToFactory = _CabhQos2LastSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 1, 2),
    _CabhQos2LastSetToFactory_Type()
)
cabhQos2LastSetToFactory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhQos2LastSetToFactory.setStatus("current")
_CabhQos2PsIfAttributes_ObjectIdentity = ObjectIdentity
cabhQos2PsIfAttributes = _CabhQos2PsIfAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2)
)
_CabhQos2PsIfAttribTable_Object = MibTable
cabhQos2PsIfAttribTable = _CabhQos2PsIfAttribTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cabhQos2PsIfAttribTable.setStatus("current")
_CabhQos2PsIfAttribEntry_Object = MibTableRow
cabhQos2PsIfAttribEntry = _CabhQos2PsIfAttribEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2, 1, 1)
)
cabhQos2PsIfAttribEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cabhQos2PsIfAttribEntry.setStatus("current")


class _CabhQos2PsIfAttribNumPriorities_Type(Unsigned32):
    """Custom type cabhQos2PsIfAttribNumPriorities based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CabhQos2PsIfAttribNumPriorities_Type.__name__ = "Unsigned32"
_CabhQos2PsIfAttribNumPriorities_Object = MibTableColumn
cabhQos2PsIfAttribNumPriorities = _CabhQos2PsIfAttribNumPriorities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2, 1, 1, 1),
    _CabhQos2PsIfAttribNumPriorities_Type()
)
cabhQos2PsIfAttribNumPriorities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhQos2PsIfAttribNumPriorities.setStatus("current")


class _CabhQos2PsIfAttribNumQueues_Type(Unsigned32):
    """Custom type cabhQos2PsIfAttribNumQueues based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CabhQos2PsIfAttribNumQueues_Type.__name__ = "Unsigned32"
_CabhQos2PsIfAttribNumQueues_Object = MibTableColumn
cabhQos2PsIfAttribNumQueues = _CabhQos2PsIfAttribNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 2, 1, 1, 2),
    _CabhQos2PsIfAttribNumQueues_Type()
)
cabhQos2PsIfAttribNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhQos2PsIfAttribNumQueues.setStatus("current")
_CabhQos2PolicyHolderObjects_ObjectIdentity = ObjectIdentity
cabhQos2PolicyHolderObjects = _CabhQos2PolicyHolderObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3)
)


class _CabhQos2PolicyHolderEnabled_Type(TruthValue):
    """Custom type cabhQos2PolicyHolderEnabled based on TruthValue"""


_CabhQos2PolicyHolderEnabled_Object = MibScalar
cabhQos2PolicyHolderEnabled = _CabhQos2PolicyHolderEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 1),
    _CabhQos2PolicyHolderEnabled_Type()
)
cabhQos2PolicyHolderEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhQos2PolicyHolderEnabled.setStatus("current")


class _CabhQos2PolicyAdmissionControl_Type(Integer32):
    """Custom type cabhQos2PolicyAdmissionControl based on Integer32"""
    defaultValue = 2

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


_CabhQos2PolicyAdmissionControl_Type.__name__ = "Integer32"
_CabhQos2PolicyAdmissionControl_Object = MibScalar
cabhQos2PolicyAdmissionControl = _CabhQos2PolicyAdmissionControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 2),
    _CabhQos2PolicyAdmissionControl_Type()
)
cabhQos2PolicyAdmissionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhQos2PolicyAdmissionControl.setStatus("current")


class _CabhQos2NumActivePolicyHolder_Type(Gauge32):
    """Custom type cabhQos2NumActivePolicyHolder based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CabhQos2NumActivePolicyHolder_Type.__name__ = "Gauge32"
_CabhQos2NumActivePolicyHolder_Object = MibScalar
cabhQos2NumActivePolicyHolder = _CabhQos2NumActivePolicyHolder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 3),
    _CabhQos2NumActivePolicyHolder_Type()
)
cabhQos2NumActivePolicyHolder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhQos2NumActivePolicyHolder.setStatus("current")
_CabhQos2PolicyTable_Object = MibTable
cabhQos2PolicyTable = _CabhQos2PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cabhQos2PolicyTable.setStatus("current")
_CabhQos2PolicyEntry_Object = MibTableRow
cabhQos2PolicyEntry = _CabhQos2PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1)
)
cabhQos2PolicyEntry.setIndexNames(
    (0, "CABH-QOS2-MIB", "cabhQos2PolicyOwner"),
    (0, "CABH-QOS2-MIB", "cabhQos2PolicyOwnerRuleId"),
)
if mibBuilder.loadTexts:
    cabhQos2PolicyEntry.setStatus("current")


class _CabhQos2PolicyOwner_Type(Integer32):
    """Custom type cabhQos2PolicyOwner based on Integer32"""
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
        *(("homeUser", 2),
          ("operatorForHomeUser", 3),
          ("operatorOnly", 1),
          ("upnp", 4))
    )


_CabhQos2PolicyOwner_Type.__name__ = "Integer32"
_CabhQos2PolicyOwner_Object = MibTableColumn
cabhQos2PolicyOwner = _CabhQos2PolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 1),
    _CabhQos2PolicyOwner_Type()
)
cabhQos2PolicyOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhQos2PolicyOwner.setStatus("current")


class _CabhQos2PolicyOwnerRuleId_Type(Unsigned32):
    """Custom type cabhQos2PolicyOwnerRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CabhQos2PolicyOwnerRuleId_Type.__name__ = "Unsigned32"
_CabhQos2PolicyOwnerRuleId_Object = MibTableColumn
cabhQos2PolicyOwnerRuleId = _CabhQos2PolicyOwnerRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 2),
    _CabhQos2PolicyOwnerRuleId_Type()
)
cabhQos2PolicyOwnerRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhQos2PolicyOwnerRuleId.setStatus("current")


class _CabhQos2PolicyRuleOrder_Type(Unsigned32):
    """Custom type cabhQos2PolicyRuleOrder based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CabhQos2PolicyRuleOrder_Type.__name__ = "Unsigned32"
_CabhQos2PolicyRuleOrder_Object = MibTableColumn
cabhQos2PolicyRuleOrder = _CabhQos2PolicyRuleOrder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 3),
    _CabhQos2PolicyRuleOrder_Type()
)
cabhQos2PolicyRuleOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyRuleOrder.setStatus("current")


class _CabhQos2PolicyAppDomain_Type(SnmpAdminString):
    """Custom type cabhQos2PolicyAppDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhQos2PolicyAppDomain_Type.__name__ = "SnmpAdminString"
_CabhQos2PolicyAppDomain_Object = MibTableColumn
cabhQos2PolicyAppDomain = _CabhQos2PolicyAppDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 4),
    _CabhQos2PolicyAppDomain_Type()
)
cabhQos2PolicyAppDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyAppDomain.setStatus("current")


class _CabhQos2PolicyAppName_Type(SnmpAdminString):
    """Custom type cabhQos2PolicyAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhQos2PolicyAppName_Type.__name__ = "SnmpAdminString"
_CabhQos2PolicyAppName_Object = MibTableColumn
cabhQos2PolicyAppName = _CabhQos2PolicyAppName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 5),
    _CabhQos2PolicyAppName_Type()
)
cabhQos2PolicyAppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyAppName.setStatus("current")


class _CabhQos2PolicyServiceProvDomain_Type(SnmpAdminString):
    """Custom type cabhQos2PolicyServiceProvDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhQos2PolicyServiceProvDomain_Type.__name__ = "SnmpAdminString"
_CabhQos2PolicyServiceProvDomain_Object = MibTableColumn
cabhQos2PolicyServiceProvDomain = _CabhQos2PolicyServiceProvDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 6),
    _CabhQos2PolicyServiceProvDomain_Type()
)
cabhQos2PolicyServiceProvDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyServiceProvDomain.setStatus("current")


class _CabhQos2PolicyServiceName_Type(SnmpAdminString):
    """Custom type cabhQos2PolicyServiceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhQos2PolicyServiceName_Type.__name__ = "SnmpAdminString"
_CabhQos2PolicyServiceName_Object = MibTableColumn
cabhQos2PolicyServiceName = _CabhQos2PolicyServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 7),
    _CabhQos2PolicyServiceName_Type()
)
cabhQos2PolicyServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyServiceName.setStatus("current")


class _CabhQos2PolicyPortDomain_Type(SnmpAdminString):
    """Custom type cabhQos2PolicyPortDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhQos2PolicyPortDomain_Type.__name__ = "SnmpAdminString"
_CabhQos2PolicyPortDomain_Object = MibTableColumn
cabhQos2PolicyPortDomain = _CabhQos2PolicyPortDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 8),
    _CabhQos2PolicyPortDomain_Type()
)
cabhQos2PolicyPortDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyPortDomain.setStatus("current")


class _CabhQos2PolicyPortNumber_Type(InetPortNumber):
    """Custom type cabhQos2PolicyPortNumber based on InetPortNumber"""
    defaultValue = 0


_CabhQos2PolicyPortNumber_Object = MibTableColumn
cabhQos2PolicyPortNumber = _CabhQos2PolicyPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 9),
    _CabhQos2PolicyPortNumber_Type()
)
cabhQos2PolicyPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyPortNumber.setStatus("current")


class _CabhQos2PolicyIpType_Type(InetAddressType):
    """Custom type cabhQos2PolicyIpType based on InetAddressType"""


_CabhQos2PolicyIpType_Object = MibTableColumn
cabhQos2PolicyIpType = _CabhQos2PolicyIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 10),
    _CabhQos2PolicyIpType_Type()
)
cabhQos2PolicyIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyIpType.setStatus("current")


class _CabhQos2PolicyIpProtocol_Type(Unsigned32):
    """Custom type cabhQos2PolicyIpProtocol based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CabhQos2PolicyIpProtocol_Type.__name__ = "Unsigned32"
_CabhQos2PolicyIpProtocol_Object = MibTableColumn
cabhQos2PolicyIpProtocol = _CabhQos2PolicyIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 11),
    _CabhQos2PolicyIpProtocol_Type()
)
cabhQos2PolicyIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyIpProtocol.setStatus("current")


class _CabhQos2PolicySrcIp_Type(InetAddress):
    """Custom type cabhQos2PolicySrcIp based on InetAddress"""
    defaultHexValue = "00000000"


_CabhQos2PolicySrcIp_Object = MibTableColumn
cabhQos2PolicySrcIp = _CabhQos2PolicySrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 12),
    _CabhQos2PolicySrcIp_Type()
)
cabhQos2PolicySrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicySrcIp.setStatus("current")


class _CabhQos2PolicyDestIp_Type(InetAddress):
    """Custom type cabhQos2PolicyDestIp based on InetAddress"""
    defaultHexValue = "00000000"


_CabhQos2PolicyDestIp_Object = MibTableColumn
cabhQos2PolicyDestIp = _CabhQos2PolicyDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 13),
    _CabhQos2PolicyDestIp_Type()
)
cabhQos2PolicyDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyDestIp.setStatus("current")


class _CabhQos2PolicySrcPort_Type(InetPortNumber):
    """Custom type cabhQos2PolicySrcPort based on InetPortNumber"""
    defaultValue = 0


_CabhQos2PolicySrcPort_Object = MibTableColumn
cabhQos2PolicySrcPort = _CabhQos2PolicySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 14),
    _CabhQos2PolicySrcPort_Type()
)
cabhQos2PolicySrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicySrcPort.setStatus("current")


class _CabhQos2PolicyDestPort_Type(InetPortNumber):
    """Custom type cabhQos2PolicyDestPort based on InetPortNumber"""
    defaultValue = 0


_CabhQos2PolicyDestPort_Object = MibTableColumn
cabhQos2PolicyDestPort = _CabhQos2PolicyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 15),
    _CabhQos2PolicyDestPort_Type()
)
cabhQos2PolicyDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyDestPort.setStatus("current")


class _CabhQos2PolicyTraffImpNum_Type(Unsigned32):
    """Custom type cabhQos2PolicyTraffImpNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CabhQos2PolicyTraffImpNum_Type.__name__ = "Unsigned32"
_CabhQos2PolicyTraffImpNum_Object = MibTableColumn
cabhQos2PolicyTraffImpNum = _CabhQos2PolicyTraffImpNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 16),
    _CabhQos2PolicyTraffImpNum_Type()
)
cabhQos2PolicyTraffImpNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyTraffImpNum.setStatus("current")


class _CabhQos2PolicyUserImportance_Type(Unsigned32):
    """Custom type cabhQos2PolicyUserImportance based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CabhQos2PolicyUserImportance_Type.__name__ = "Unsigned32"
_CabhQos2PolicyUserImportance_Object = MibTableColumn
cabhQos2PolicyUserImportance = _CabhQos2PolicyUserImportance_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 17),
    _CabhQos2PolicyUserImportance_Type()
)
cabhQos2PolicyUserImportance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyUserImportance.setStatus("current")
_CabhQos2PolicyRowStatus_Type = RowStatus
_CabhQos2PolicyRowStatus_Object = MibTableColumn
cabhQos2PolicyRowStatus = _CabhQos2PolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 3, 4, 1, 18),
    _CabhQos2PolicyRowStatus_Type()
)
cabhQos2PolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2PolicyRowStatus.setStatus("current")
_CabhQos2DeviceObjects_ObjectIdentity = ObjectIdentity
cabhQos2DeviceObjects = _CabhQos2DeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4)
)
_CabhQos2TrafficClassTable_Object = MibTable
cabhQos2TrafficClassTable = _CabhQos2TrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cabhQos2TrafficClassTable.setStatus("current")
_CabhQos2TrafficClassEntry_Object = MibTableRow
cabhQos2TrafficClassEntry = _CabhQos2TrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1)
)
cabhQos2TrafficClassEntry.setIndexNames(
    (0, "CABH-QOS2-MIB", "cabhQos2TrafficClassMethod"),
    (0, "CABH-QOS2-MIB", "cabhQos2TrafficClassIdx"),
)
if mibBuilder.loadTexts:
    cabhQos2TrafficClassEntry.setStatus("current")


class _CabhQos2TrafficClassMethod_Type(Integer32):
    """Custom type cabhQos2TrafficClassMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("upnp", 2))
    )


_CabhQos2TrafficClassMethod_Type.__name__ = "Integer32"
_CabhQos2TrafficClassMethod_Object = MibTableColumn
cabhQos2TrafficClassMethod = _CabhQos2TrafficClassMethod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 1),
    _CabhQos2TrafficClassMethod_Type()
)
cabhQos2TrafficClassMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassMethod.setStatus("current")


class _CabhQos2TrafficClassIdx_Type(Unsigned32):
    """Custom type cabhQos2TrafficClassIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CabhQos2TrafficClassIdx_Type.__name__ = "Unsigned32"
_CabhQos2TrafficClassIdx_Object = MibTableColumn
cabhQos2TrafficClassIdx = _CabhQos2TrafficClassIdx_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 2),
    _CabhQos2TrafficClassIdx_Type()
)
cabhQos2TrafficClassIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassIdx.setStatus("current")


class _CabhQos2TrafficClassProtocol_Type(Unsigned32):
    """Custom type cabhQos2TrafficClassProtocol based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CabhQos2TrafficClassProtocol_Type.__name__ = "Unsigned32"
_CabhQos2TrafficClassProtocol_Object = MibTableColumn
cabhQos2TrafficClassProtocol = _CabhQos2TrafficClassProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 3),
    _CabhQos2TrafficClassProtocol_Type()
)
cabhQos2TrafficClassProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassProtocol.setStatus("current")


class _CabhQos2TrafficClassIpType_Type(InetAddressType):
    """Custom type cabhQos2TrafficClassIpType based on InetAddressType"""


_CabhQos2TrafficClassIpType_Object = MibTableColumn
cabhQos2TrafficClassIpType = _CabhQos2TrafficClassIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 4),
    _CabhQos2TrafficClassIpType_Type()
)
cabhQos2TrafficClassIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassIpType.setStatus("current")


class _CabhQos2TrafficClassSrcIp_Type(InetAddress):
    """Custom type cabhQos2TrafficClassSrcIp based on InetAddress"""
    defaultHexValue = "00000000"


_CabhQos2TrafficClassSrcIp_Object = MibTableColumn
cabhQos2TrafficClassSrcIp = _CabhQos2TrafficClassSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 5),
    _CabhQos2TrafficClassSrcIp_Type()
)
cabhQos2TrafficClassSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassSrcIp.setStatus("current")


class _CabhQos2TrafficClassDestIp_Type(InetAddress):
    """Custom type cabhQos2TrafficClassDestIp based on InetAddress"""
    defaultHexValue = "00000000"


_CabhQos2TrafficClassDestIp_Object = MibTableColumn
cabhQos2TrafficClassDestIp = _CabhQos2TrafficClassDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 6),
    _CabhQos2TrafficClassDestIp_Type()
)
cabhQos2TrafficClassDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassDestIp.setStatus("current")


class _CabhQos2TrafficClassSrcPort_Type(InetPortNumber):
    """Custom type cabhQos2TrafficClassSrcPort based on InetPortNumber"""
    defaultValue = 0


_CabhQos2TrafficClassSrcPort_Object = MibTableColumn
cabhQos2TrafficClassSrcPort = _CabhQos2TrafficClassSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 7),
    _CabhQos2TrafficClassSrcPort_Type()
)
cabhQos2TrafficClassSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassSrcPort.setStatus("current")


class _CabhQos2TrafficClassDestPort_Type(InetPortNumber):
    """Custom type cabhQos2TrafficClassDestPort based on InetPortNumber"""
    defaultValue = 0


_CabhQos2TrafficClassDestPort_Object = MibTableColumn
cabhQos2TrafficClassDestPort = _CabhQos2TrafficClassDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 8),
    _CabhQos2TrafficClassDestPort_Type()
)
cabhQos2TrafficClassDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassDestPort.setStatus("current")


class _CabhQos2TrafficClassImpNum_Type(Unsigned32):
    """Custom type cabhQos2TrafficClassImpNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CabhQos2TrafficClassImpNum_Type.__name__ = "Unsigned32"
_CabhQos2TrafficClassImpNum_Object = MibTableColumn
cabhQos2TrafficClassImpNum = _CabhQos2TrafficClassImpNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 9),
    _CabhQos2TrafficClassImpNum_Type()
)
cabhQos2TrafficClassImpNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassImpNum.setStatus("current")
_CabhQos2TrafficClassRowStatus_Type = RowStatus
_CabhQos2TrafficClassRowStatus_Object = MibTableColumn
cabhQos2TrafficClassRowStatus = _CabhQos2TrafficClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 1, 4, 1, 1, 10),
    _CabhQos2TrafficClassRowStatus_Type()
)
cabhQos2TrafficClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhQos2TrafficClassRowStatus.setStatus("current")
_CabhQos2Conformance_ObjectIdentity = ObjectIdentity
cabhQos2Conformance = _CabhQos2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2)
)
_CabhQos2Compliances_ObjectIdentity = ObjectIdentity
cabhQos2Compliances = _CabhQos2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 1)
)
_CabhQos2Groups_ObjectIdentity = ObjectIdentity
cabhQos2Groups = _CabhQos2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 2)
)

# Managed Objects groups

cabhQos2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 2, 1)
)
cabhQos2Group.setObjects(
      *(("CABH-QOS2-MIB", "cabhQos2SetToFactory"),
        ("CABH-QOS2-MIB", "cabhQos2LastSetToFactory"),
        ("CABH-QOS2-MIB", "cabhQos2PsIfAttribNumPriorities"),
        ("CABH-QOS2-MIB", "cabhQos2PsIfAttribNumQueues"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyHolderEnabled"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyAdmissionControl"),
        ("CABH-QOS2-MIB", "cabhQos2NumActivePolicyHolder"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyRuleOrder"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyAppDomain"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyAppName"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyServiceProvDomain"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyServiceName"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyPortDomain"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyPortNumber"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyIpProtocol"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyIpType"),
        ("CABH-QOS2-MIB", "cabhQos2PolicySrcIp"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyDestIp"),
        ("CABH-QOS2-MIB", "cabhQos2PolicySrcPort"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyDestPort"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyTraffImpNum"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyUserImportance"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyRowStatus"),
        ("CABH-QOS2-MIB", "cabhQos2TrafficClassProtocol"),
        ("CABH-QOS2-MIB", "cabhQos2TrafficClassIpType"),
        ("CABH-QOS2-MIB", "cabhQos2PolicySrcIp"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyDestIp"),
        ("CABH-QOS2-MIB", "cabhQos2PolicySrcPort"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyDestPort"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyTraffImpNum"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyUserImportance"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyRowStatus"))
)
if mibBuilder.loadTexts:
    cabhQos2Group.setStatus("current")

cabhQos2ClassifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 2, 2)
)
cabhQos2ClassifierGroup.setObjects(
      *(("CABH-QOS2-MIB", "cabhQos2TrafficClassProtocol"),
        ("CABH-QOS2-MIB", "cabhQos2TrafficClassIpType"),
        ("CABH-QOS2-MIB", "cabhQos2TrafficClassSrcIp"),
        ("CABH-QOS2-MIB", "cabhQos2TrafficClassDestIp"),
        ("CABH-QOS2-MIB", "cabhQos2TrafficClassSrcPort"),
        ("CABH-QOS2-MIB", "cabhQos2TrafficClassDestPort"),
        ("CABH-QOS2-MIB", "cabhQos2TrafficClassImpNum"),
        ("CABH-QOS2-MIB", "cabhQos2TrafficClassRowStatus"))
)
if mibBuilder.loadTexts:
    cabhQos2ClassifierGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cabhQos2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cabhQos2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABH-QOS2-MIB",
    **{"cabhQos2Mib": cabhQos2Mib,
       "cabhQos2Mib2Notifications": cabhQos2Mib2Notifications,
       "cabhQos2MibObjects": cabhQos2MibObjects,
       "cabhQos2Base": cabhQos2Base,
       "cabhQos2SetToFactory": cabhQos2SetToFactory,
       "cabhQos2LastSetToFactory": cabhQos2LastSetToFactory,
       "cabhQos2PsIfAttributes": cabhQos2PsIfAttributes,
       "cabhQos2PsIfAttribTable": cabhQos2PsIfAttribTable,
       "cabhQos2PsIfAttribEntry": cabhQos2PsIfAttribEntry,
       "cabhQos2PsIfAttribNumPriorities": cabhQos2PsIfAttribNumPriorities,
       "cabhQos2PsIfAttribNumQueues": cabhQos2PsIfAttribNumQueues,
       "cabhQos2PolicyHolderObjects": cabhQos2PolicyHolderObjects,
       "cabhQos2PolicyHolderEnabled": cabhQos2PolicyHolderEnabled,
       "cabhQos2PolicyAdmissionControl": cabhQos2PolicyAdmissionControl,
       "cabhQos2NumActivePolicyHolder": cabhQos2NumActivePolicyHolder,
       "cabhQos2PolicyTable": cabhQos2PolicyTable,
       "cabhQos2PolicyEntry": cabhQos2PolicyEntry,
       "cabhQos2PolicyOwner": cabhQos2PolicyOwner,
       "cabhQos2PolicyOwnerRuleId": cabhQos2PolicyOwnerRuleId,
       "cabhQos2PolicyRuleOrder": cabhQos2PolicyRuleOrder,
       "cabhQos2PolicyAppDomain": cabhQos2PolicyAppDomain,
       "cabhQos2PolicyAppName": cabhQos2PolicyAppName,
       "cabhQos2PolicyServiceProvDomain": cabhQos2PolicyServiceProvDomain,
       "cabhQos2PolicyServiceName": cabhQos2PolicyServiceName,
       "cabhQos2PolicyPortDomain": cabhQos2PolicyPortDomain,
       "cabhQos2PolicyPortNumber": cabhQos2PolicyPortNumber,
       "cabhQos2PolicyIpType": cabhQos2PolicyIpType,
       "cabhQos2PolicyIpProtocol": cabhQos2PolicyIpProtocol,
       "cabhQos2PolicySrcIp": cabhQos2PolicySrcIp,
       "cabhQos2PolicyDestIp": cabhQos2PolicyDestIp,
       "cabhQos2PolicySrcPort": cabhQos2PolicySrcPort,
       "cabhQos2PolicyDestPort": cabhQos2PolicyDestPort,
       "cabhQos2PolicyTraffImpNum": cabhQos2PolicyTraffImpNum,
       "cabhQos2PolicyUserImportance": cabhQos2PolicyUserImportance,
       "cabhQos2PolicyRowStatus": cabhQos2PolicyRowStatus,
       "cabhQos2DeviceObjects": cabhQos2DeviceObjects,
       "cabhQos2TrafficClassTable": cabhQos2TrafficClassTable,
       "cabhQos2TrafficClassEntry": cabhQos2TrafficClassEntry,
       "cabhQos2TrafficClassMethod": cabhQos2TrafficClassMethod,
       "cabhQos2TrafficClassIdx": cabhQos2TrafficClassIdx,
       "cabhQos2TrafficClassProtocol": cabhQos2TrafficClassProtocol,
       "cabhQos2TrafficClassIpType": cabhQos2TrafficClassIpType,
       "cabhQos2TrafficClassSrcIp": cabhQos2TrafficClassSrcIp,
       "cabhQos2TrafficClassDestIp": cabhQos2TrafficClassDestIp,
       "cabhQos2TrafficClassSrcPort": cabhQos2TrafficClassSrcPort,
       "cabhQos2TrafficClassDestPort": cabhQos2TrafficClassDestPort,
       "cabhQos2TrafficClassImpNum": cabhQos2TrafficClassImpNum,
       "cabhQos2TrafficClassRowStatus": cabhQos2TrafficClassRowStatus,
       "cabhQos2Conformance": cabhQos2Conformance,
       "cabhQos2Compliances": cabhQos2Compliances,
       "cabhQos2Compliance": cabhQos2Compliance,
       "cabhQos2Groups": cabhQos2Groups,
       "cabhQos2Group": cabhQos2Group,
       "cabhQos2ClassifierGroup": cabhQos2ClassifierGroup}
)
