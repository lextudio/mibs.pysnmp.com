# SNMP MIB module (SIP-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIP-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:20 2024
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

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

(SipTCEntityRole,
 SipTCMethodName,
 SipTCOptionTagHeaders,
 SipTCTransportProtocol) = mibBuilder.importSymbols(
    "SIP-TC-MIB",
    "SipTCEntityRole",
    "SipTCMethodName",
    "SipTCOptionTagHeaders",
    "SipTCTransportProtocol")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

sipCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 149)
)
sipCommonMIB.setRevisions(
        ("2007-04-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipCommonMIBNotifications_ObjectIdentity = ObjectIdentity
sipCommonMIBNotifications = _SipCommonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 0)
)
_SipCommonMIBObjects_ObjectIdentity = ObjectIdentity
sipCommonMIBObjects = _SipCommonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1)
)
_SipCommonCfgBase_ObjectIdentity = ObjectIdentity
sipCommonCfgBase = _SipCommonCfgBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1, 1)
)
_SipCommonCfgTable_Object = MibTable
sipCommonCfgTable = _SipCommonCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sipCommonCfgTable.setStatus("current")
_SipCommonCfgEntry_Object = MibTableRow
sipCommonCfgEntry = _SipCommonCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1)
)
sipCommonCfgEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipCommonCfgEntry.setStatus("current")
_SipCommonCfgProtocolVersion_Type = SnmpAdminString
_SipCommonCfgProtocolVersion_Object = MibTableColumn
sipCommonCfgProtocolVersion = _SipCommonCfgProtocolVersion_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 1),
    _SipCommonCfgProtocolVersion_Type()
)
sipCommonCfgProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgProtocolVersion.setStatus("current")


class _SipCommonCfgServiceOperStatus_Type(Integer32):
    """Custom type sipCommonCfgServiceOperStatus based on Integer32"""
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
        *(("congested", 4),
          ("down", 3),
          ("quiescing", 6),
          ("restarting", 5),
          ("testing", 7),
          ("unknown", 1),
          ("up", 2))
    )


_SipCommonCfgServiceOperStatus_Type.__name__ = "Integer32"
_SipCommonCfgServiceOperStatus_Object = MibTableColumn
sipCommonCfgServiceOperStatus = _SipCommonCfgServiceOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 2),
    _SipCommonCfgServiceOperStatus_Type()
)
sipCommonCfgServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgServiceOperStatus.setStatus("current")
_SipCommonCfgServiceStartTime_Type = TimeTicks
_SipCommonCfgServiceStartTime_Object = MibTableColumn
sipCommonCfgServiceStartTime = _SipCommonCfgServiceStartTime_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 3),
    _SipCommonCfgServiceStartTime_Type()
)
sipCommonCfgServiceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgServiceStartTime.setStatus("current")
_SipCommonCfgServiceLastChange_Type = TimeTicks
_SipCommonCfgServiceLastChange_Object = MibTableColumn
sipCommonCfgServiceLastChange = _SipCommonCfgServiceLastChange_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 4),
    _SipCommonCfgServiceLastChange_Type()
)
sipCommonCfgServiceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgServiceLastChange.setStatus("current")
_SipCommonCfgOrganization_Type = SnmpAdminString
_SipCommonCfgOrganization_Object = MibTableColumn
sipCommonCfgOrganization = _SipCommonCfgOrganization_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 5),
    _SipCommonCfgOrganization_Type()
)
sipCommonCfgOrganization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgOrganization.setStatus("current")


class _SipCommonCfgMaxTransactions_Type(Unsigned32):
    """Custom type sipCommonCfgMaxTransactions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipCommonCfgMaxTransactions_Type.__name__ = "Unsigned32"
_SipCommonCfgMaxTransactions_Object = MibTableColumn
sipCommonCfgMaxTransactions = _SipCommonCfgMaxTransactions_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 6),
    _SipCommonCfgMaxTransactions_Type()
)
sipCommonCfgMaxTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgMaxTransactions.setStatus("current")


class _SipCommonCfgServiceNotifEnable_Type(Bits):
    """Custom type sipCommonCfgServiceNotifEnable based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("sipCommonServiceColdStart", 0),
          ("sipCommonServiceStatusChanged", 2),
          ("sipCommonServiceWarmStart", 1))
    )

_SipCommonCfgServiceNotifEnable_Type.__name__ = "Bits"
_SipCommonCfgServiceNotifEnable_Object = MibTableColumn
sipCommonCfgServiceNotifEnable = _SipCommonCfgServiceNotifEnable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 7),
    _SipCommonCfgServiceNotifEnable_Type()
)
sipCommonCfgServiceNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonCfgServiceNotifEnable.setStatus("current")
_SipCommonCfgEntityType_Type = SipTCEntityRole
_SipCommonCfgEntityType_Object = MibTableColumn
sipCommonCfgEntityType = _SipCommonCfgEntityType_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 1, 1, 8),
    _SipCommonCfgEntityType_Type()
)
sipCommonCfgEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgEntityType.setStatus("current")
_SipCommonPortTable_Object = MibTable
sipCommonPortTable = _SipCommonPortTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sipCommonPortTable.setStatus("current")
_SipCommonPortEntry_Object = MibTableRow
sipCommonPortEntry = _SipCommonPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 2, 1)
)
sipCommonPortEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-COMMON-MIB", "sipCommonPort"),
)
if mibBuilder.loadTexts:
    sipCommonPortEntry.setStatus("current")


class _SipCommonPort_Type(InetPortNumber):
    """Custom type sipCommonPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SipCommonPort_Type.__name__ = "InetPortNumber"
_SipCommonPort_Object = MibTableColumn
sipCommonPort = _SipCommonPort_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 2, 1, 1),
    _SipCommonPort_Type()
)
sipCommonPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipCommonPort.setStatus("current")
_SipCommonPortTransportRcv_Type = SipTCTransportProtocol
_SipCommonPortTransportRcv_Object = MibTableColumn
sipCommonPortTransportRcv = _SipCommonPortTransportRcv_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 2, 1, 2),
    _SipCommonPortTransportRcv_Type()
)
sipCommonPortTransportRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonPortTransportRcv.setStatus("current")
_SipCommonOptionTagTable_Object = MibTable
sipCommonOptionTagTable = _SipCommonOptionTagTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sipCommonOptionTagTable.setStatus("current")
_SipCommonOptionTagEntry_Object = MibTableRow
sipCommonOptionTagEntry = _SipCommonOptionTagEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 3, 1)
)
sipCommonOptionTagEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-COMMON-MIB", "sipCommonOptionTagIndex"),
)
if mibBuilder.loadTexts:
    sipCommonOptionTagEntry.setStatus("current")


class _SipCommonOptionTagIndex_Type(Unsigned32):
    """Custom type sipCommonOptionTagIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipCommonOptionTagIndex_Type.__name__ = "Unsigned32"
_SipCommonOptionTagIndex_Object = MibTableColumn
sipCommonOptionTagIndex = _SipCommonOptionTagIndex_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 3, 1, 1),
    _SipCommonOptionTagIndex_Type()
)
sipCommonOptionTagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipCommonOptionTagIndex.setStatus("current")
_SipCommonOptionTag_Type = SnmpAdminString
_SipCommonOptionTag_Object = MibTableColumn
sipCommonOptionTag = _SipCommonOptionTag_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 3, 1, 2),
    _SipCommonOptionTag_Type()
)
sipCommonOptionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonOptionTag.setStatus("current")
_SipCommonOptionTagHeaderField_Type = SipTCOptionTagHeaders
_SipCommonOptionTagHeaderField_Object = MibTableColumn
sipCommonOptionTagHeaderField = _SipCommonOptionTagHeaderField_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 3, 1, 3),
    _SipCommonOptionTagHeaderField_Type()
)
sipCommonOptionTagHeaderField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonOptionTagHeaderField.setStatus("current")
_SipCommonMethodSupportedTable_Object = MibTable
sipCommonMethodSupportedTable = _SipCommonMethodSupportedTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sipCommonMethodSupportedTable.setStatus("current")
_SipCommonMethodSupportedEntry_Object = MibTableRow
sipCommonMethodSupportedEntry = _SipCommonMethodSupportedEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 4, 1)
)
sipCommonMethodSupportedEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-COMMON-MIB", "sipCommonMethodSupportedIndex"),
)
if mibBuilder.loadTexts:
    sipCommonMethodSupportedEntry.setStatus("current")


class _SipCommonMethodSupportedIndex_Type(Unsigned32):
    """Custom type sipCommonMethodSupportedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipCommonMethodSupportedIndex_Type.__name__ = "Unsigned32"
_SipCommonMethodSupportedIndex_Object = MibTableColumn
sipCommonMethodSupportedIndex = _SipCommonMethodSupportedIndex_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 4, 1, 1),
    _SipCommonMethodSupportedIndex_Type()
)
sipCommonMethodSupportedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipCommonMethodSupportedIndex.setStatus("current")
_SipCommonMethodSupportedName_Type = SipTCMethodName
_SipCommonMethodSupportedName_Object = MibTableColumn
sipCommonMethodSupportedName = _SipCommonMethodSupportedName_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 1, 4, 1, 2),
    _SipCommonMethodSupportedName_Type()
)
sipCommonMethodSupportedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonMethodSupportedName.setStatus("current")
_SipCommonCfgTimer_ObjectIdentity = ObjectIdentity
sipCommonCfgTimer = _SipCommonCfgTimer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1, 2)
)
_SipCommonCfgTimerTable_Object = MibTable
sipCommonCfgTimerTable = _SipCommonCfgTimerTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sipCommonCfgTimerTable.setStatus("current")
_SipCommonCfgTimerEntry_Object = MibTableRow
sipCommonCfgTimerEntry = _SipCommonCfgTimerEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1)
)
sipCommonCfgTimerEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipCommonCfgTimerEntry.setStatus("current")


class _SipCommonCfgTimerA_Type(Unsigned32):
    """Custom type sipCommonCfgTimerA based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SipCommonCfgTimerA_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerA_Object = MibTableColumn
sipCommonCfgTimerA = _SipCommonCfgTimerA_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 1),
    _SipCommonCfgTimerA_Type()
)
sipCommonCfgTimerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerA.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerA.setUnits("milliseconds")


class _SipCommonCfgTimerB_Type(Unsigned32):
    """Custom type sipCommonCfgTimerB based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 300000),
    )


_SipCommonCfgTimerB_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerB_Object = MibTableColumn
sipCommonCfgTimerB = _SipCommonCfgTimerB_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 2),
    _SipCommonCfgTimerB_Type()
)
sipCommonCfgTimerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerB.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerB.setUnits("milliseconds")


class _SipCommonCfgTimerC_Type(Unsigned32):
    """Custom type sipCommonCfgTimerC based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180000, 300000),
    )


_SipCommonCfgTimerC_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerC_Object = MibTableColumn
sipCommonCfgTimerC = _SipCommonCfgTimerC_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 3),
    _SipCommonCfgTimerC_Type()
)
sipCommonCfgTimerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerC.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerC.setUnits("milliseconds")


class _SipCommonCfgTimerD_Type(Unsigned32):
    """Custom type sipCommonCfgTimerD based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_SipCommonCfgTimerD_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerD_Object = MibTableColumn
sipCommonCfgTimerD = _SipCommonCfgTimerD_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 4),
    _SipCommonCfgTimerD_Type()
)
sipCommonCfgTimerD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerD.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerD.setUnits("milliseconds")


class _SipCommonCfgTimerE_Type(Unsigned32):
    """Custom type sipCommonCfgTimerE based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SipCommonCfgTimerE_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerE_Object = MibTableColumn
sipCommonCfgTimerE = _SipCommonCfgTimerE_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 5),
    _SipCommonCfgTimerE_Type()
)
sipCommonCfgTimerE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerE.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerE.setUnits("milliseconds")


class _SipCommonCfgTimerF_Type(Unsigned32):
    """Custom type sipCommonCfgTimerF based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 300000),
    )


_SipCommonCfgTimerF_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerF_Object = MibTableColumn
sipCommonCfgTimerF = _SipCommonCfgTimerF_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 6),
    _SipCommonCfgTimerF_Type()
)
sipCommonCfgTimerF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerF.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerF.setUnits("milliseconds")


class _SipCommonCfgTimerG_Type(Unsigned32):
    """Custom type sipCommonCfgTimerG based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SipCommonCfgTimerG_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerG_Object = MibTableColumn
sipCommonCfgTimerG = _SipCommonCfgTimerG_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 7),
    _SipCommonCfgTimerG_Type()
)
sipCommonCfgTimerG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerG.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerG.setUnits("milliseconds")


class _SipCommonCfgTimerH_Type(Unsigned32):
    """Custom type sipCommonCfgTimerH based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 300000),
    )


_SipCommonCfgTimerH_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerH_Object = MibTableColumn
sipCommonCfgTimerH = _SipCommonCfgTimerH_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 8),
    _SipCommonCfgTimerH_Type()
)
sipCommonCfgTimerH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerH.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerH.setUnits("milliseconds")


class _SipCommonCfgTimerI_Type(Unsigned32):
    """Custom type sipCommonCfgTimerI based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SipCommonCfgTimerI_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerI_Object = MibTableColumn
sipCommonCfgTimerI = _SipCommonCfgTimerI_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 9),
    _SipCommonCfgTimerI_Type()
)
sipCommonCfgTimerI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerI.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerI.setUnits("milliseconds")


class _SipCommonCfgTimerJ_Type(Unsigned32):
    """Custom type sipCommonCfgTimerJ based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 300000),
    )


_SipCommonCfgTimerJ_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerJ_Object = MibTableColumn
sipCommonCfgTimerJ = _SipCommonCfgTimerJ_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 10),
    _SipCommonCfgTimerJ_Type()
)
sipCommonCfgTimerJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerJ.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerJ.setUnits("milliseconds")


class _SipCommonCfgTimerK_Type(Unsigned32):
    """Custom type sipCommonCfgTimerK based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SipCommonCfgTimerK_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerK_Object = MibTableColumn
sipCommonCfgTimerK = _SipCommonCfgTimerK_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 11),
    _SipCommonCfgTimerK_Type()
)
sipCommonCfgTimerK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerK.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerK.setUnits("milliseconds")


class _SipCommonCfgTimerT1_Type(Unsigned32):
    """Custom type sipCommonCfgTimerT1 based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_SipCommonCfgTimerT1_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerT1_Object = MibTableColumn
sipCommonCfgTimerT1 = _SipCommonCfgTimerT1_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 12),
    _SipCommonCfgTimerT1_Type()
)
sipCommonCfgTimerT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerT1.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerT1.setUnits("milliseconds")


class _SipCommonCfgTimerT2_Type(Unsigned32):
    """Custom type sipCommonCfgTimerT2 based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_SipCommonCfgTimerT2_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerT2_Object = MibTableColumn
sipCommonCfgTimerT2 = _SipCommonCfgTimerT2_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 13),
    _SipCommonCfgTimerT2_Type()
)
sipCommonCfgTimerT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerT2.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerT2.setUnits("milliseconds")


class _SipCommonCfgTimerT4_Type(Unsigned32):
    """Custom type sipCommonCfgTimerT4 based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_SipCommonCfgTimerT4_Type.__name__ = "Unsigned32"
_SipCommonCfgTimerT4_Object = MibTableColumn
sipCommonCfgTimerT4 = _SipCommonCfgTimerT4_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 2, 1, 1, 14),
    _SipCommonCfgTimerT4_Type()
)
sipCommonCfgTimerT4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonCfgTimerT4.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonCfgTimerT4.setUnits("milliseconds")
_SipCommonSummaryStats_ObjectIdentity = ObjectIdentity
sipCommonSummaryStats = _SipCommonSummaryStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1, 3)
)
_SipCommonSummaryStatsTable_Object = MibTable
sipCommonSummaryStatsTable = _SipCommonSummaryStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sipCommonSummaryStatsTable.setStatus("current")
_SipCommonSummaryStatsEntry_Object = MibTableRow
sipCommonSummaryStatsEntry = _SipCommonSummaryStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1)
)
sipCommonSummaryStatsEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipCommonSummaryStatsEntry.setStatus("current")
_SipCommonSummaryInRequests_Type = Counter32
_SipCommonSummaryInRequests_Object = MibTableColumn
sipCommonSummaryInRequests = _SipCommonSummaryInRequests_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 1),
    _SipCommonSummaryInRequests_Type()
)
sipCommonSummaryInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonSummaryInRequests.setStatus("current")
_SipCommonSummaryOutRequests_Type = Counter32
_SipCommonSummaryOutRequests_Object = MibTableColumn
sipCommonSummaryOutRequests = _SipCommonSummaryOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 2),
    _SipCommonSummaryOutRequests_Type()
)
sipCommonSummaryOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonSummaryOutRequests.setStatus("current")
_SipCommonSummaryInResponses_Type = Counter32
_SipCommonSummaryInResponses_Object = MibTableColumn
sipCommonSummaryInResponses = _SipCommonSummaryInResponses_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 3),
    _SipCommonSummaryInResponses_Type()
)
sipCommonSummaryInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonSummaryInResponses.setStatus("current")
_SipCommonSummaryOutResponses_Type = Counter32
_SipCommonSummaryOutResponses_Object = MibTableColumn
sipCommonSummaryOutResponses = _SipCommonSummaryOutResponses_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 4),
    _SipCommonSummaryOutResponses_Type()
)
sipCommonSummaryOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonSummaryOutResponses.setStatus("current")
_SipCommonSummaryTotalTransactions_Type = Counter32
_SipCommonSummaryTotalTransactions_Object = MibTableColumn
sipCommonSummaryTotalTransactions = _SipCommonSummaryTotalTransactions_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 5),
    _SipCommonSummaryTotalTransactions_Type()
)
sipCommonSummaryTotalTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonSummaryTotalTransactions.setStatus("current")
_SipCommonSummaryDisconTime_Type = TimeStamp
_SipCommonSummaryDisconTime_Object = MibTableColumn
sipCommonSummaryDisconTime = _SipCommonSummaryDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 3, 1, 1, 6),
    _SipCommonSummaryDisconTime_Type()
)
sipCommonSummaryDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonSummaryDisconTime.setStatus("current")
_SipCommonMethodStats_ObjectIdentity = ObjectIdentity
sipCommonMethodStats = _SipCommonMethodStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1, 4)
)
_SipCommonMethodStatsTable_Object = MibTable
sipCommonMethodStatsTable = _SipCommonMethodStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sipCommonMethodStatsTable.setStatus("current")
_SipCommonMethodStatsEntry_Object = MibTableRow
sipCommonMethodStatsEntry = _SipCommonMethodStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1)
)
sipCommonMethodStatsEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-COMMON-MIB", "sipCommonMethodStatsName"),
)
if mibBuilder.loadTexts:
    sipCommonMethodStatsEntry.setStatus("current")
_SipCommonMethodStatsName_Type = SipTCMethodName
_SipCommonMethodStatsName_Object = MibTableColumn
sipCommonMethodStatsName = _SipCommonMethodStatsName_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1, 1),
    _SipCommonMethodStatsName_Type()
)
sipCommonMethodStatsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipCommonMethodStatsName.setStatus("current")
_SipCommonMethodStatsOutbounds_Type = Counter32
_SipCommonMethodStatsOutbounds_Object = MibTableColumn
sipCommonMethodStatsOutbounds = _SipCommonMethodStatsOutbounds_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1, 2),
    _SipCommonMethodStatsOutbounds_Type()
)
sipCommonMethodStatsOutbounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonMethodStatsOutbounds.setStatus("current")
_SipCommonMethodStatsInbounds_Type = Counter32
_SipCommonMethodStatsInbounds_Object = MibTableColumn
sipCommonMethodStatsInbounds = _SipCommonMethodStatsInbounds_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1, 3),
    _SipCommonMethodStatsInbounds_Type()
)
sipCommonMethodStatsInbounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonMethodStatsInbounds.setStatus("current")
_SipCommonMethodStatsDisconTime_Type = TimeStamp
_SipCommonMethodStatsDisconTime_Object = MibTableColumn
sipCommonMethodStatsDisconTime = _SipCommonMethodStatsDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 4, 1, 1, 4),
    _SipCommonMethodStatsDisconTime_Type()
)
sipCommonMethodStatsDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonMethodStatsDisconTime.setStatus("current")
_SipCommonStatusCode_ObjectIdentity = ObjectIdentity
sipCommonStatusCode = _SipCommonStatusCode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1, 5)
)
_SipCommonStatusCodeTable_Object = MibTable
sipCommonStatusCodeTable = _SipCommonStatusCodeTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sipCommonStatusCodeTable.setStatus("current")
_SipCommonStatusCodeEntry_Object = MibTableRow
sipCommonStatusCodeEntry = _SipCommonStatusCodeEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1)
)
sipCommonStatusCodeEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-COMMON-MIB", "sipCommonStatusCodeMethod"),
    (0, "SIP-COMMON-MIB", "sipCommonStatusCodeValue"),
)
if mibBuilder.loadTexts:
    sipCommonStatusCodeEntry.setStatus("current")
_SipCommonStatusCodeMethod_Type = SipTCMethodName
_SipCommonStatusCodeMethod_Object = MibTableColumn
sipCommonStatusCodeMethod = _SipCommonStatusCodeMethod_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 1),
    _SipCommonStatusCodeMethod_Type()
)
sipCommonStatusCodeMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipCommonStatusCodeMethod.setStatus("current")


class _SipCommonStatusCodeValue_Type(Unsigned32):
    """Custom type sipCommonStatusCodeValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_SipCommonStatusCodeValue_Type.__name__ = "Unsigned32"
_SipCommonStatusCodeValue_Object = MibTableColumn
sipCommonStatusCodeValue = _SipCommonStatusCodeValue_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 2),
    _SipCommonStatusCodeValue_Type()
)
sipCommonStatusCodeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipCommonStatusCodeValue.setStatus("current")
_SipCommonStatusCodeIns_Type = Counter32
_SipCommonStatusCodeIns_Object = MibTableColumn
sipCommonStatusCodeIns = _SipCommonStatusCodeIns_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 3),
    _SipCommonStatusCodeIns_Type()
)
sipCommonStatusCodeIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatusCodeIns.setStatus("current")
_SipCommonStatusCodeOuts_Type = Counter32
_SipCommonStatusCodeOuts_Object = MibTableColumn
sipCommonStatusCodeOuts = _SipCommonStatusCodeOuts_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 4),
    _SipCommonStatusCodeOuts_Type()
)
sipCommonStatusCodeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatusCodeOuts.setStatus("current")
_SipCommonStatusCodeRowStatus_Type = RowStatus
_SipCommonStatusCodeRowStatus_Object = MibTableColumn
sipCommonStatusCodeRowStatus = _SipCommonStatusCodeRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 5),
    _SipCommonStatusCodeRowStatus_Type()
)
sipCommonStatusCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipCommonStatusCodeRowStatus.setStatus("current")
_SipCommonStatusCodeDisconTime_Type = TimeStamp
_SipCommonStatusCodeDisconTime_Object = MibTableColumn
sipCommonStatusCodeDisconTime = _SipCommonStatusCodeDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 1, 1, 6),
    _SipCommonStatusCodeDisconTime_Type()
)
sipCommonStatusCodeDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatusCodeDisconTime.setStatus("current")
_SipCommonStatusCodeNotifTable_Object = MibTable
sipCommonStatusCodeNotifTable = _SipCommonStatusCodeNotifTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 2)
)
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifTable.setStatus("current")
_SipCommonStatusCodeNotifEntry_Object = MibTableRow
sipCommonStatusCodeNotifEntry = _SipCommonStatusCodeNotifEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifEntry.setStatus("current")


class _SipCommonStatusCodeNotifSend_Type(TruthValue):
    """Custom type sipCommonStatusCodeNotifSend based on TruthValue"""


_SipCommonStatusCodeNotifSend_Object = MibTableColumn
sipCommonStatusCodeNotifSend = _SipCommonStatusCodeNotifSend_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1, 1),
    _SipCommonStatusCodeNotifSend_Type()
)
sipCommonStatusCodeNotifSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifSend.setStatus("current")


class _SipCommonStatusCodeNotifEmitMode_Type(Integer32):
    """Custom type sipCommonStatusCodeNotifEmitMode based on Integer32"""
    defaultValue = 2

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
          ("oneShot", 2),
          ("triggered", 3))
    )


_SipCommonStatusCodeNotifEmitMode_Type.__name__ = "Integer32"
_SipCommonStatusCodeNotifEmitMode_Object = MibTableColumn
sipCommonStatusCodeNotifEmitMode = _SipCommonStatusCodeNotifEmitMode_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1, 2),
    _SipCommonStatusCodeNotifEmitMode_Type()
)
sipCommonStatusCodeNotifEmitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifEmitMode.setStatus("current")


class _SipCommonStatusCodeNotifThresh_Type(Unsigned32):
    """Custom type sipCommonStatusCodeNotifThresh based on Unsigned32"""
    defaultValue = 500


_SipCommonStatusCodeNotifThresh_Object = MibTableColumn
sipCommonStatusCodeNotifThresh = _SipCommonStatusCodeNotifThresh_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1, 3),
    _SipCommonStatusCodeNotifThresh_Type()
)
sipCommonStatusCodeNotifThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifThresh.setStatus("current")


class _SipCommonStatusCodeNotifInterval_Type(Unsigned32):
    """Custom type sipCommonStatusCodeNotifInterval based on Unsigned32"""
    defaultValue = 60


_SipCommonStatusCodeNotifInterval_Object = MibTableColumn
sipCommonStatusCodeNotifInterval = _SipCommonStatusCodeNotifInterval_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 5, 2, 1, 4),
    _SipCommonStatusCodeNotifInterval_Type()
)
sipCommonStatusCodeNotifInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifInterval.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifInterval.setUnits("seconds")
_SipCommonStatsTrans_ObjectIdentity = ObjectIdentity
sipCommonStatsTrans = _SipCommonStatsTrans_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1, 6)
)
_SipCommonTransCurrentTable_Object = MibTable
sipCommonTransCurrentTable = _SipCommonTransCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sipCommonTransCurrentTable.setStatus("current")
_SipCommonTransCurrentEntry_Object = MibTableRow
sipCommonTransCurrentEntry = _SipCommonTransCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 6, 1, 1)
)
sipCommonTransCurrentEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipCommonTransCurrentEntry.setStatus("current")


class _SipCommonTransCurrentactions_Type(Gauge32):
    """Custom type sipCommonTransCurrentactions based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipCommonTransCurrentactions_Type.__name__ = "Gauge32"
_SipCommonTransCurrentactions_Object = MibTableColumn
sipCommonTransCurrentactions = _SipCommonTransCurrentactions_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 6, 1, 1, 1),
    _SipCommonTransCurrentactions_Type()
)
sipCommonTransCurrentactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonTransCurrentactions.setStatus("current")
_SipCommonStatsRetry_ObjectIdentity = ObjectIdentity
sipCommonStatsRetry = _SipCommonStatsRetry_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1, 7)
)
_SipCommonStatsRetryTable_Object = MibTable
sipCommonStatsRetryTable = _SipCommonStatsRetryTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 7, 1)
)
if mibBuilder.loadTexts:
    sipCommonStatsRetryTable.setStatus("current")
_SipCommonStatsRetryEntry_Object = MibTableRow
sipCommonStatsRetryEntry = _SipCommonStatsRetryEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1)
)
sipCommonStatsRetryEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-COMMON-MIB", "sipCommonStatsRetryMethod"),
)
if mibBuilder.loadTexts:
    sipCommonStatsRetryEntry.setStatus("current")
_SipCommonStatsRetryMethod_Type = SipTCMethodName
_SipCommonStatsRetryMethod_Object = MibTableColumn
sipCommonStatsRetryMethod = _SipCommonStatsRetryMethod_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 1),
    _SipCommonStatsRetryMethod_Type()
)
sipCommonStatsRetryMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipCommonStatsRetryMethod.setStatus("current")
_SipCommonStatsRetries_Type = Counter32
_SipCommonStatsRetries_Object = MibTableColumn
sipCommonStatsRetries = _SipCommonStatsRetries_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 2),
    _SipCommonStatsRetries_Type()
)
sipCommonStatsRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatsRetries.setStatus("current")
_SipCommonStatsRetryFinalResponses_Type = Counter32
_SipCommonStatsRetryFinalResponses_Object = MibTableColumn
sipCommonStatsRetryFinalResponses = _SipCommonStatsRetryFinalResponses_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 3),
    _SipCommonStatsRetryFinalResponses_Type()
)
sipCommonStatsRetryFinalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatsRetryFinalResponses.setStatus("current")
_SipCommonStatsRetryNonFinalResponses_Type = Counter32
_SipCommonStatsRetryNonFinalResponses_Object = MibTableColumn
sipCommonStatsRetryNonFinalResponses = _SipCommonStatsRetryNonFinalResponses_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 4),
    _SipCommonStatsRetryNonFinalResponses_Type()
)
sipCommonStatsRetryNonFinalResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatsRetryNonFinalResponses.setStatus("current")
_SipCommonStatsRetryDisconTime_Type = TimeStamp
_SipCommonStatsRetryDisconTime_Object = MibTableColumn
sipCommonStatsRetryDisconTime = _SipCommonStatsRetryDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 7, 1, 1, 5),
    _SipCommonStatsRetryDisconTime_Type()
)
sipCommonStatsRetryDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonStatsRetryDisconTime.setStatus("current")
_SipCommonOtherStats_ObjectIdentity = ObjectIdentity
sipCommonOtherStats = _SipCommonOtherStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1, 8)
)
_SipCommonOtherStatsTable_Object = MibTable
sipCommonOtherStatsTable = _SipCommonOtherStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 8, 1)
)
if mibBuilder.loadTexts:
    sipCommonOtherStatsTable.setStatus("current")
_SipCommonOtherStatsEntry_Object = MibTableRow
sipCommonOtherStatsEntry = _SipCommonOtherStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1)
)
sipCommonOtherStatsEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipCommonOtherStatsEntry.setStatus("current")
_SipCommonOtherStatsNumUnsupportedUris_Type = Counter32
_SipCommonOtherStatsNumUnsupportedUris_Object = MibTableColumn
sipCommonOtherStatsNumUnsupportedUris = _SipCommonOtherStatsNumUnsupportedUris_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1, 1),
    _SipCommonOtherStatsNumUnsupportedUris_Type()
)
sipCommonOtherStatsNumUnsupportedUris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonOtherStatsNumUnsupportedUris.setStatus("current")
_SipCommonOtherStatsNumUnsupportedMethods_Type = Counter32
_SipCommonOtherStatsNumUnsupportedMethods_Object = MibTableColumn
sipCommonOtherStatsNumUnsupportedMethods = _SipCommonOtherStatsNumUnsupportedMethods_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1, 2),
    _SipCommonOtherStatsNumUnsupportedMethods_Type()
)
sipCommonOtherStatsNumUnsupportedMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonOtherStatsNumUnsupportedMethods.setStatus("current")
_SipCommonOtherStatsOtherwiseDiscardedMsgs_Type = Counter32
_SipCommonOtherStatsOtherwiseDiscardedMsgs_Object = MibTableColumn
sipCommonOtherStatsOtherwiseDiscardedMsgs = _SipCommonOtherStatsOtherwiseDiscardedMsgs_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1, 3),
    _SipCommonOtherStatsOtherwiseDiscardedMsgs_Type()
)
sipCommonOtherStatsOtherwiseDiscardedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonOtherStatsOtherwiseDiscardedMsgs.setStatus("current")
_SipCommonOtherStatsDisconTime_Type = TimeStamp
_SipCommonOtherStatsDisconTime_Object = MibTableColumn
sipCommonOtherStatsDisconTime = _SipCommonOtherStatsDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 8, 1, 1, 4),
    _SipCommonOtherStatsDisconTime_Type()
)
sipCommonOtherStatsDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipCommonOtherStatsDisconTime.setStatus("current")
_SipCommonNotifObjects_ObjectIdentity = ObjectIdentity
sipCommonNotifObjects = _SipCommonNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 1, 9)
)
_SipCommonStatusCodeNotifTo_Type = SnmpAdminString
_SipCommonStatusCodeNotifTo_Object = MibScalar
sipCommonStatusCodeNotifTo = _SipCommonStatusCodeNotifTo_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 9, 1),
    _SipCommonStatusCodeNotifTo_Type()
)
sipCommonStatusCodeNotifTo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifTo.setStatus("current")
_SipCommonStatusCodeNotifFrom_Type = SnmpAdminString
_SipCommonStatusCodeNotifFrom_Object = MibScalar
sipCommonStatusCodeNotifFrom = _SipCommonStatusCodeNotifFrom_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 9, 2),
    _SipCommonStatusCodeNotifFrom_Type()
)
sipCommonStatusCodeNotifFrom.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifFrom.setStatus("current")
_SipCommonStatusCodeNotifCallId_Type = SnmpAdminString
_SipCommonStatusCodeNotifCallId_Object = MibScalar
sipCommonStatusCodeNotifCallId = _SipCommonStatusCodeNotifCallId_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 9, 3),
    _SipCommonStatusCodeNotifCallId_Type()
)
sipCommonStatusCodeNotifCallId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifCallId.setStatus("current")
_SipCommonStatusCodeNotifCSeq_Type = Unsigned32
_SipCommonStatusCodeNotifCSeq_Object = MibScalar
sipCommonStatusCodeNotifCSeq = _SipCommonStatusCodeNotifCSeq_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 9, 4),
    _SipCommonStatusCodeNotifCSeq_Type()
)
sipCommonStatusCodeNotifCSeq.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifCSeq.setStatus("current")


class _SipCommonNotifApplIndex_Type(Unsigned32):
    """Custom type sipCommonNotifApplIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SipCommonNotifApplIndex_Type.__name__ = "Unsigned32"
_SipCommonNotifApplIndex_Object = MibScalar
sipCommonNotifApplIndex = _SipCommonNotifApplIndex_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 9, 5),
    _SipCommonNotifApplIndex_Type()
)
sipCommonNotifApplIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sipCommonNotifApplIndex.setStatus("current")


class _SipCommonNotifSequenceNumber_Type(Unsigned32):
    """Custom type sipCommonNotifSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SipCommonNotifSequenceNumber_Type.__name__ = "Unsigned32"
_SipCommonNotifSequenceNumber_Object = MibScalar
sipCommonNotifSequenceNumber = _SipCommonNotifSequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 149, 1, 9, 6),
    _SipCommonNotifSequenceNumber_Type()
)
sipCommonNotifSequenceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sipCommonNotifSequenceNumber.setStatus("current")
_SipCommonMIBConformance_ObjectIdentity = ObjectIdentity
sipCommonMIBConformance = _SipCommonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 2)
)
_SipCommonMIBCompliances_ObjectIdentity = ObjectIdentity
sipCommonMIBCompliances = _SipCommonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 2, 1)
)
_SipCommonMIBGroups_ObjectIdentity = ObjectIdentity
sipCommonMIBGroups = _SipCommonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 149, 2, 2)
)
sipCommonStatusCodeEntry.registerAugmentions(
    ("SIP-COMMON-MIB",
     "sipCommonStatusCodeNotifEntry")
)
sipCommonStatusCodeNotifEntry.setIndexNames(*sipCommonStatusCodeEntry.getIndexNames())

# Managed Objects groups

sipCommonConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 149, 2, 2, 1)
)
sipCommonConfigGroup.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonCfgProtocolVersion"),
        ("SIP-COMMON-MIB", "sipCommonCfgServiceOperStatus"),
        ("SIP-COMMON-MIB", "sipCommonCfgServiceStartTime"),
        ("SIP-COMMON-MIB", "sipCommonCfgServiceLastChange"),
        ("SIP-COMMON-MIB", "sipCommonPortTransportRcv"),
        ("SIP-COMMON-MIB", "sipCommonOptionTag"),
        ("SIP-COMMON-MIB", "sipCommonOptionTagHeaderField"),
        ("SIP-COMMON-MIB", "sipCommonCfgMaxTransactions"),
        ("SIP-COMMON-MIB", "sipCommonCfgServiceNotifEnable"),
        ("SIP-COMMON-MIB", "sipCommonCfgEntityType"),
        ("SIP-COMMON-MIB", "sipCommonMethodSupportedName"))
)
if mibBuilder.loadTexts:
    sipCommonConfigGroup.setStatus("current")

sipCommonInformationalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 149, 2, 2, 2)
)
sipCommonInformationalGroup.setObjects(
    ("SIP-COMMON-MIB", "sipCommonCfgOrganization")
)
if mibBuilder.loadTexts:
    sipCommonInformationalGroup.setStatus("current")

sipCommonConfigTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 149, 2, 2, 3)
)
sipCommonConfigTimerGroup.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonCfgTimerA"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerB"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerC"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerD"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerE"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerF"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerG"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerH"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerI"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerJ"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerK"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerT1"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerT2"),
        ("SIP-COMMON-MIB", "sipCommonCfgTimerT4"))
)
if mibBuilder.loadTexts:
    sipCommonConfigTimerGroup.setStatus("current")

sipCommonStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 149, 2, 2, 4)
)
sipCommonStatsGroup.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonSummaryInRequests"),
        ("SIP-COMMON-MIB", "sipCommonSummaryOutRequests"),
        ("SIP-COMMON-MIB", "sipCommonSummaryInResponses"),
        ("SIP-COMMON-MIB", "sipCommonSummaryOutResponses"),
        ("SIP-COMMON-MIB", "sipCommonSummaryTotalTransactions"),
        ("SIP-COMMON-MIB", "sipCommonSummaryDisconTime"),
        ("SIP-COMMON-MIB", "sipCommonMethodStatsOutbounds"),
        ("SIP-COMMON-MIB", "sipCommonMethodStatsInbounds"),
        ("SIP-COMMON-MIB", "sipCommonMethodStatsDisconTime"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeIns"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeOuts"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeRowStatus"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeDisconTime"),
        ("SIP-COMMON-MIB", "sipCommonTransCurrentactions"),
        ("SIP-COMMON-MIB", "sipCommonOtherStatsNumUnsupportedUris"),
        ("SIP-COMMON-MIB", "sipCommonOtherStatsNumUnsupportedMethods"),
        ("SIP-COMMON-MIB", "sipCommonOtherStatsOtherwiseDiscardedMsgs"),
        ("SIP-COMMON-MIB", "sipCommonOtherStatsDisconTime"))
)
if mibBuilder.loadTexts:
    sipCommonStatsGroup.setStatus("current")

sipCommonStatsRetryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 149, 2, 2, 5)
)
sipCommonStatsRetryGroup.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonStatsRetries"),
        ("SIP-COMMON-MIB", "sipCommonStatsRetryFinalResponses"),
        ("SIP-COMMON-MIB", "sipCommonStatsRetryNonFinalResponses"),
        ("SIP-COMMON-MIB", "sipCommonStatsRetryDisconTime"))
)
if mibBuilder.loadTexts:
    sipCommonStatsRetryGroup.setStatus("current")

sipCommonStatusCodeNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 149, 2, 2, 7)
)
sipCommonStatusCodeNotifGroup.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonStatusCodeNotifSend"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifEmitMode"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifThresh"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifInterval"))
)
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotifGroup.setStatus("current")

sipCommonNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 149, 2, 2, 8)
)
sipCommonNotifObjectsGroup.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonStatusCodeNotifTo"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifFrom"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifCallId"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifCSeq"),
        ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"),
        ("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"))
)
if mibBuilder.loadTexts:
    sipCommonNotifObjectsGroup.setStatus("current")


# Notification objects

sipCommonStatusCodeNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 149, 0, 1)
)
sipCommonStatusCodeNotif.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"),
        ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifTo"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifFrom"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifCallId"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeNotifCSeq"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeIns"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeOuts"))
)
if mibBuilder.loadTexts:
    sipCommonStatusCodeNotif.setStatus(
        "current"
    )

sipCommonStatusCodeThreshExceededInNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 149, 0, 2)
)
sipCommonStatusCodeThreshExceededInNotif.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"),
        ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeIns"))
)
if mibBuilder.loadTexts:
    sipCommonStatusCodeThreshExceededInNotif.setStatus(
        "current"
    )

sipCommonStatusCodeThreshExceededOutNotif = NotificationType(
    (1, 3, 6, 1, 2, 1, 149, 0, 3)
)
sipCommonStatusCodeThreshExceededOutNotif.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"),
        ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeOuts"))
)
if mibBuilder.loadTexts:
    sipCommonStatusCodeThreshExceededOutNotif.setStatus(
        "current"
    )

sipCommonServiceColdStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 149, 0, 4)
)
sipCommonServiceColdStart.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"),
        ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"),
        ("SIP-COMMON-MIB", "sipCommonCfgServiceStartTime"))
)
if mibBuilder.loadTexts:
    sipCommonServiceColdStart.setStatus(
        "current"
    )

sipCommonServiceWarmStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 149, 0, 5)
)
sipCommonServiceWarmStart.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"),
        ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"),
        ("SIP-COMMON-MIB", "sipCommonCfgServiceLastChange"))
)
if mibBuilder.loadTexts:
    sipCommonServiceWarmStart.setStatus(
        "current"
    )

sipCommonServiceStatusChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 149, 0, 6)
)
sipCommonServiceStatusChanged.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonNotifSequenceNumber"),
        ("SIP-COMMON-MIB", "sipCommonNotifApplIndex"),
        ("SIP-COMMON-MIB", "sipCommonCfgServiceLastChange"),
        ("SIP-COMMON-MIB", "sipCommonCfgServiceOperStatus"))
)
if mibBuilder.loadTexts:
    sipCommonServiceStatusChanged.setStatus(
        "current"
    )


# Notifications groups

sipCommonNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 149, 2, 2, 6)
)
sipCommonNotifGroup.setObjects(
      *(("SIP-COMMON-MIB", "sipCommonStatusCodeNotif"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeThreshExceededInNotif"),
        ("SIP-COMMON-MIB", "sipCommonStatusCodeThreshExceededOutNotif"),
        ("SIP-COMMON-MIB", "sipCommonServiceColdStart"),
        ("SIP-COMMON-MIB", "sipCommonServiceWarmStart"),
        ("SIP-COMMON-MIB", "sipCommonServiceStatusChanged"))
)
if mibBuilder.loadTexts:
    sipCommonNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

sipCommonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 149, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sipCommonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIP-COMMON-MIB",
    **{"sipCommonMIB": sipCommonMIB,
       "sipCommonMIBNotifications": sipCommonMIBNotifications,
       "sipCommonStatusCodeNotif": sipCommonStatusCodeNotif,
       "sipCommonStatusCodeThreshExceededInNotif": sipCommonStatusCodeThreshExceededInNotif,
       "sipCommonStatusCodeThreshExceededOutNotif": sipCommonStatusCodeThreshExceededOutNotif,
       "sipCommonServiceColdStart": sipCommonServiceColdStart,
       "sipCommonServiceWarmStart": sipCommonServiceWarmStart,
       "sipCommonServiceStatusChanged": sipCommonServiceStatusChanged,
       "sipCommonMIBObjects": sipCommonMIBObjects,
       "sipCommonCfgBase": sipCommonCfgBase,
       "sipCommonCfgTable": sipCommonCfgTable,
       "sipCommonCfgEntry": sipCommonCfgEntry,
       "sipCommonCfgProtocolVersion": sipCommonCfgProtocolVersion,
       "sipCommonCfgServiceOperStatus": sipCommonCfgServiceOperStatus,
       "sipCommonCfgServiceStartTime": sipCommonCfgServiceStartTime,
       "sipCommonCfgServiceLastChange": sipCommonCfgServiceLastChange,
       "sipCommonCfgOrganization": sipCommonCfgOrganization,
       "sipCommonCfgMaxTransactions": sipCommonCfgMaxTransactions,
       "sipCommonCfgServiceNotifEnable": sipCommonCfgServiceNotifEnable,
       "sipCommonCfgEntityType": sipCommonCfgEntityType,
       "sipCommonPortTable": sipCommonPortTable,
       "sipCommonPortEntry": sipCommonPortEntry,
       "sipCommonPort": sipCommonPort,
       "sipCommonPortTransportRcv": sipCommonPortTransportRcv,
       "sipCommonOptionTagTable": sipCommonOptionTagTable,
       "sipCommonOptionTagEntry": sipCommonOptionTagEntry,
       "sipCommonOptionTagIndex": sipCommonOptionTagIndex,
       "sipCommonOptionTag": sipCommonOptionTag,
       "sipCommonOptionTagHeaderField": sipCommonOptionTagHeaderField,
       "sipCommonMethodSupportedTable": sipCommonMethodSupportedTable,
       "sipCommonMethodSupportedEntry": sipCommonMethodSupportedEntry,
       "sipCommonMethodSupportedIndex": sipCommonMethodSupportedIndex,
       "sipCommonMethodSupportedName": sipCommonMethodSupportedName,
       "sipCommonCfgTimer": sipCommonCfgTimer,
       "sipCommonCfgTimerTable": sipCommonCfgTimerTable,
       "sipCommonCfgTimerEntry": sipCommonCfgTimerEntry,
       "sipCommonCfgTimerA": sipCommonCfgTimerA,
       "sipCommonCfgTimerB": sipCommonCfgTimerB,
       "sipCommonCfgTimerC": sipCommonCfgTimerC,
       "sipCommonCfgTimerD": sipCommonCfgTimerD,
       "sipCommonCfgTimerE": sipCommonCfgTimerE,
       "sipCommonCfgTimerF": sipCommonCfgTimerF,
       "sipCommonCfgTimerG": sipCommonCfgTimerG,
       "sipCommonCfgTimerH": sipCommonCfgTimerH,
       "sipCommonCfgTimerI": sipCommonCfgTimerI,
       "sipCommonCfgTimerJ": sipCommonCfgTimerJ,
       "sipCommonCfgTimerK": sipCommonCfgTimerK,
       "sipCommonCfgTimerT1": sipCommonCfgTimerT1,
       "sipCommonCfgTimerT2": sipCommonCfgTimerT2,
       "sipCommonCfgTimerT4": sipCommonCfgTimerT4,
       "sipCommonSummaryStats": sipCommonSummaryStats,
       "sipCommonSummaryStatsTable": sipCommonSummaryStatsTable,
       "sipCommonSummaryStatsEntry": sipCommonSummaryStatsEntry,
       "sipCommonSummaryInRequests": sipCommonSummaryInRequests,
       "sipCommonSummaryOutRequests": sipCommonSummaryOutRequests,
       "sipCommonSummaryInResponses": sipCommonSummaryInResponses,
       "sipCommonSummaryOutResponses": sipCommonSummaryOutResponses,
       "sipCommonSummaryTotalTransactions": sipCommonSummaryTotalTransactions,
       "sipCommonSummaryDisconTime": sipCommonSummaryDisconTime,
       "sipCommonMethodStats": sipCommonMethodStats,
       "sipCommonMethodStatsTable": sipCommonMethodStatsTable,
       "sipCommonMethodStatsEntry": sipCommonMethodStatsEntry,
       "sipCommonMethodStatsName": sipCommonMethodStatsName,
       "sipCommonMethodStatsOutbounds": sipCommonMethodStatsOutbounds,
       "sipCommonMethodStatsInbounds": sipCommonMethodStatsInbounds,
       "sipCommonMethodStatsDisconTime": sipCommonMethodStatsDisconTime,
       "sipCommonStatusCode": sipCommonStatusCode,
       "sipCommonStatusCodeTable": sipCommonStatusCodeTable,
       "sipCommonStatusCodeEntry": sipCommonStatusCodeEntry,
       "sipCommonStatusCodeMethod": sipCommonStatusCodeMethod,
       "sipCommonStatusCodeValue": sipCommonStatusCodeValue,
       "sipCommonStatusCodeIns": sipCommonStatusCodeIns,
       "sipCommonStatusCodeOuts": sipCommonStatusCodeOuts,
       "sipCommonStatusCodeRowStatus": sipCommonStatusCodeRowStatus,
       "sipCommonStatusCodeDisconTime": sipCommonStatusCodeDisconTime,
       "sipCommonStatusCodeNotifTable": sipCommonStatusCodeNotifTable,
       "sipCommonStatusCodeNotifEntry": sipCommonStatusCodeNotifEntry,
       "sipCommonStatusCodeNotifSend": sipCommonStatusCodeNotifSend,
       "sipCommonStatusCodeNotifEmitMode": sipCommonStatusCodeNotifEmitMode,
       "sipCommonStatusCodeNotifThresh": sipCommonStatusCodeNotifThresh,
       "sipCommonStatusCodeNotifInterval": sipCommonStatusCodeNotifInterval,
       "sipCommonStatsTrans": sipCommonStatsTrans,
       "sipCommonTransCurrentTable": sipCommonTransCurrentTable,
       "sipCommonTransCurrentEntry": sipCommonTransCurrentEntry,
       "sipCommonTransCurrentactions": sipCommonTransCurrentactions,
       "sipCommonStatsRetry": sipCommonStatsRetry,
       "sipCommonStatsRetryTable": sipCommonStatsRetryTable,
       "sipCommonStatsRetryEntry": sipCommonStatsRetryEntry,
       "sipCommonStatsRetryMethod": sipCommonStatsRetryMethod,
       "sipCommonStatsRetries": sipCommonStatsRetries,
       "sipCommonStatsRetryFinalResponses": sipCommonStatsRetryFinalResponses,
       "sipCommonStatsRetryNonFinalResponses": sipCommonStatsRetryNonFinalResponses,
       "sipCommonStatsRetryDisconTime": sipCommonStatsRetryDisconTime,
       "sipCommonOtherStats": sipCommonOtherStats,
       "sipCommonOtherStatsTable": sipCommonOtherStatsTable,
       "sipCommonOtherStatsEntry": sipCommonOtherStatsEntry,
       "sipCommonOtherStatsNumUnsupportedUris": sipCommonOtherStatsNumUnsupportedUris,
       "sipCommonOtherStatsNumUnsupportedMethods": sipCommonOtherStatsNumUnsupportedMethods,
       "sipCommonOtherStatsOtherwiseDiscardedMsgs": sipCommonOtherStatsOtherwiseDiscardedMsgs,
       "sipCommonOtherStatsDisconTime": sipCommonOtherStatsDisconTime,
       "sipCommonNotifObjects": sipCommonNotifObjects,
       "sipCommonStatusCodeNotifTo": sipCommonStatusCodeNotifTo,
       "sipCommonStatusCodeNotifFrom": sipCommonStatusCodeNotifFrom,
       "sipCommonStatusCodeNotifCallId": sipCommonStatusCodeNotifCallId,
       "sipCommonStatusCodeNotifCSeq": sipCommonStatusCodeNotifCSeq,
       "sipCommonNotifApplIndex": sipCommonNotifApplIndex,
       "sipCommonNotifSequenceNumber": sipCommonNotifSequenceNumber,
       "sipCommonMIBConformance": sipCommonMIBConformance,
       "sipCommonMIBCompliances": sipCommonMIBCompliances,
       "sipCommonCompliance": sipCommonCompliance,
       "sipCommonMIBGroups": sipCommonMIBGroups,
       "sipCommonConfigGroup": sipCommonConfigGroup,
       "sipCommonInformationalGroup": sipCommonInformationalGroup,
       "sipCommonConfigTimerGroup": sipCommonConfigTimerGroup,
       "sipCommonStatsGroup": sipCommonStatsGroup,
       "sipCommonStatsRetryGroup": sipCommonStatsRetryGroup,
       "sipCommonNotifGroup": sipCommonNotifGroup,
       "sipCommonStatusCodeNotifGroup": sipCommonStatusCodeNotifGroup,
       "sipCommonNotifObjectsGroup": sipCommonNotifObjectsGroup}
)
