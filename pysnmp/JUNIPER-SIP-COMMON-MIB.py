# SNMP MIB module (JUNIPER-SIP-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-SIP-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:11 2024
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

(jnxVoip,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxVoip")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

jnxSipCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxSip_ObjectIdentity = ObjectIdentity
jnxSip = _JnxSip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2)
)
_JnxSipCommonMIBObjects_ObjectIdentity = ObjectIdentity
jnxSipCommonMIBObjects = _JnxSipCommonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1)
)
_JnxSipCommonCfgTable_Object = MibTable
jnxSipCommonCfgTable = _JnxSipCommonCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSipCommonCfgTable.setStatus("current")
_JnxSipCommonCfgEntry_Object = MibTableRow
jnxSipCommonCfgEntry = _JnxSipCommonCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1)
)
jnxSipCommonCfgEntry.setIndexNames(
    (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCfgApplName"),
)
if mibBuilder.loadTexts:
    jnxSipCommonCfgEntry.setStatus("current")
_JnxSipCfgApplName_Type = DisplayString
_JnxSipCfgApplName_Object = MibTableColumn
jnxSipCfgApplName = _JnxSipCfgApplName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 1),
    _JnxSipCfgApplName_Type()
)
jnxSipCfgApplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSipCfgApplName.setStatus("current")
_JnxSipCommonCfgProtocolVersion_Type = SnmpAdminString
_JnxSipCommonCfgProtocolVersion_Object = MibTableColumn
jnxSipCommonCfgProtocolVersion = _JnxSipCommonCfgProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 2),
    _JnxSipCommonCfgProtocolVersion_Type()
)
jnxSipCommonCfgProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgProtocolVersion.setStatus("current")


class _JnxSipCommonCfgServiceOperStatus_Type(Integer32):
    """Custom type jnxSipCommonCfgServiceOperStatus based on Integer32"""
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
          ("unknown", 1),
          ("up", 2))
    )


_JnxSipCommonCfgServiceOperStatus_Type.__name__ = "Integer32"
_JnxSipCommonCfgServiceOperStatus_Object = MibTableColumn
jnxSipCommonCfgServiceOperStatus = _JnxSipCommonCfgServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 3),
    _JnxSipCommonCfgServiceOperStatus_Type()
)
jnxSipCommonCfgServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgServiceOperStatus.setStatus("current")
_JnxSipCommonCfgServiceStartTime_Type = TimeTicks
_JnxSipCommonCfgServiceStartTime_Object = MibTableColumn
jnxSipCommonCfgServiceStartTime = _JnxSipCommonCfgServiceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 4),
    _JnxSipCommonCfgServiceStartTime_Type()
)
jnxSipCommonCfgServiceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgServiceStartTime.setStatus("current")
_JnxSipCommonCfgServiceLastChange_Type = TimeTicks
_JnxSipCommonCfgServiceLastChange_Object = MibTableColumn
jnxSipCommonCfgServiceLastChange = _JnxSipCommonCfgServiceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 5),
    _JnxSipCommonCfgServiceLastChange_Type()
)
jnxSipCommonCfgServiceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgServiceLastChange.setStatus("current")
_JnxSipCommonCfgOrganization_Type = SnmpAdminString
_JnxSipCommonCfgOrganization_Object = MibTableColumn
jnxSipCommonCfgOrganization = _JnxSipCommonCfgOrganization_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 6),
    _JnxSipCommonCfgOrganization_Type()
)
jnxSipCommonCfgOrganization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgOrganization.setStatus("current")


class _JnxSipCommonCfgMaxTransactions_Type(Unsigned32):
    """Custom type jnxSipCommonCfgMaxTransactions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxSipCommonCfgMaxTransactions_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgMaxTransactions_Object = MibTableColumn
jnxSipCommonCfgMaxTransactions = _JnxSipCommonCfgMaxTransactions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 7),
    _JnxSipCommonCfgMaxTransactions_Type()
)
jnxSipCommonCfgMaxTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgMaxTransactions.setStatus("current")


class _JnxSipCommonCfgEntityType_Type(Bits):
    """Custom type jnxSipCommonCfgEntityType based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("proxyServer", 2),
          ("redirectServer", 3),
          ("registrarServer", 4),
          ("userAgent", 1))
    )

_JnxSipCommonCfgEntityType_Type.__name__ = "Bits"
_JnxSipCommonCfgEntityType_Object = MibTableColumn
jnxSipCommonCfgEntityType = _JnxSipCommonCfgEntityType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 1, 1, 8),
    _JnxSipCommonCfgEntityType_Type()
)
jnxSipCommonCfgEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgEntityType.setStatus("current")
_JnxSipCommonPortTable_Object = MibTable
jnxSipCommonPortTable = _JnxSipCommonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxSipCommonPortTable.setStatus("current")
_JnxSipCommonPortEntry_Object = MibTableRow
jnxSipCommonPortEntry = _JnxSipCommonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2, 1)
)
jnxSipCommonPortEntry.setIndexNames(
    (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipPortApplName"),
    (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCommonPort"),
)
if mibBuilder.loadTexts:
    jnxSipCommonPortEntry.setStatus("current")
_JnxSipPortApplName_Type = DisplayString
_JnxSipPortApplName_Object = MibTableColumn
jnxSipPortApplName = _JnxSipPortApplName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2, 1, 1),
    _JnxSipPortApplName_Type()
)
jnxSipPortApplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSipPortApplName.setStatus("current")


class _JnxSipCommonPort_Type(InetPortNumber):
    """Custom type jnxSipCommonPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxSipCommonPort_Type.__name__ = "InetPortNumber"
_JnxSipCommonPort_Object = MibTableColumn
jnxSipCommonPort = _JnxSipCommonPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2, 1, 2),
    _JnxSipCommonPort_Type()
)
jnxSipCommonPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSipCommonPort.setStatus("current")


class _JnxSipCommonPortTransportRcv_Type(Bits):
    """Custom type jnxSipCommonPortTransportRcv based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("sctp", 3),
          ("tcp", 2),
          ("tlsSctp", 5),
          ("tlsTcp", 4),
          ("udp", 1))
    )

_JnxSipCommonPortTransportRcv_Type.__name__ = "Bits"
_JnxSipCommonPortTransportRcv_Object = MibTableColumn
jnxSipCommonPortTransportRcv = _JnxSipCommonPortTransportRcv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 2, 1, 3),
    _JnxSipCommonPortTransportRcv_Type()
)
jnxSipCommonPortTransportRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonPortTransportRcv.setStatus("current")
_JnxSipCommonOptionTagTable_Object = MibTable
jnxSipCommonOptionTagTable = _JnxSipCommonOptionTagTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxSipCommonOptionTagTable.setStatus("current")
_JnxSipCommonOptionTagEntry_Object = MibTableRow
jnxSipCommonOptionTagEntry = _JnxSipCommonOptionTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1)
)
jnxSipCommonOptionTagEntry.setIndexNames(
    (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipOptionTagApplName"),
    (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCommonOptionTagIndex"),
)
if mibBuilder.loadTexts:
    jnxSipCommonOptionTagEntry.setStatus("current")
_JnxSipOptionTagApplName_Type = DisplayString
_JnxSipOptionTagApplName_Object = MibTableColumn
jnxSipOptionTagApplName = _JnxSipOptionTagApplName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1, 1),
    _JnxSipOptionTagApplName_Type()
)
jnxSipOptionTagApplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSipOptionTagApplName.setStatus("current")


class _JnxSipCommonOptionTagIndex_Type(Unsigned32):
    """Custom type jnxSipCommonOptionTagIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxSipCommonOptionTagIndex_Type.__name__ = "Unsigned32"
_JnxSipCommonOptionTagIndex_Object = MibTableColumn
jnxSipCommonOptionTagIndex = _JnxSipCommonOptionTagIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1, 2),
    _JnxSipCommonOptionTagIndex_Type()
)
jnxSipCommonOptionTagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSipCommonOptionTagIndex.setStatus("current")
_JnxSipCommonOptionTag_Type = SnmpAdminString
_JnxSipCommonOptionTag_Object = MibTableColumn
jnxSipCommonOptionTag = _JnxSipCommonOptionTag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1, 3),
    _JnxSipCommonOptionTag_Type()
)
jnxSipCommonOptionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonOptionTag.setStatus("current")


class _JnxSipCommonOptionTagHeaderField_Type(Bits):
    """Custom type jnxSipCommonOptionTagHeaderField based on Bits"""
    namedValues = NamedValues(
        *(("proxyRequire", 1),
          ("require", 0),
          ("supported", 2),
          ("unsupported", 3))
    )

_JnxSipCommonOptionTagHeaderField_Type.__name__ = "Bits"
_JnxSipCommonOptionTagHeaderField_Object = MibTableColumn
jnxSipCommonOptionTagHeaderField = _JnxSipCommonOptionTagHeaderField_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 3, 1, 4),
    _JnxSipCommonOptionTagHeaderField_Type()
)
jnxSipCommonOptionTagHeaderField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonOptionTagHeaderField.setStatus("current")
_JnxSipCommonMethodSupportedTable_Object = MibTable
jnxSipCommonMethodSupportedTable = _JnxSipCommonMethodSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxSipCommonMethodSupportedTable.setStatus("current")
_JnxSipCommonMethodSupportedEntry_Object = MibTableRow
jnxSipCommonMethodSupportedEntry = _JnxSipCommonMethodSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4, 1)
)
jnxSipCommonMethodSupportedEntry.setIndexNames(
    (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipMethodSupportedApplName"),
    (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCommonMethodSupportedIndex"),
)
if mibBuilder.loadTexts:
    jnxSipCommonMethodSupportedEntry.setStatus("current")
_JnxSipMethodSupportedApplName_Type = DisplayString
_JnxSipMethodSupportedApplName_Object = MibTableColumn
jnxSipMethodSupportedApplName = _JnxSipMethodSupportedApplName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4, 1, 1),
    _JnxSipMethodSupportedApplName_Type()
)
jnxSipMethodSupportedApplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSipMethodSupportedApplName.setStatus("current")


class _JnxSipCommonMethodSupportedIndex_Type(Unsigned32):
    """Custom type jnxSipCommonMethodSupportedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxSipCommonMethodSupportedIndex_Type.__name__ = "Unsigned32"
_JnxSipCommonMethodSupportedIndex_Object = MibTableColumn
jnxSipCommonMethodSupportedIndex = _JnxSipCommonMethodSupportedIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4, 1, 2),
    _JnxSipCommonMethodSupportedIndex_Type()
)
jnxSipCommonMethodSupportedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSipCommonMethodSupportedIndex.setStatus("current")


class _JnxSipCommonMethodSupportedName_Type(OctetString):
    """Custom type jnxSipCommonMethodSupportedName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_JnxSipCommonMethodSupportedName_Type.__name__ = "OctetString"
_JnxSipCommonMethodSupportedName_Object = MibTableColumn
jnxSipCommonMethodSupportedName = _JnxSipCommonMethodSupportedName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 4, 1, 3),
    _JnxSipCommonMethodSupportedName_Type()
)
jnxSipCommonMethodSupportedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonMethodSupportedName.setStatus("current")
_JnxSipCommonCfgTimerTable_Object = MibTable
jnxSipCommonCfgTimerTable = _JnxSipCommonCfgTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerTable.setStatus("current")
_JnxSipCommonCfgTimerEntry_Object = MibTableRow
jnxSipCommonCfgTimerEntry = _JnxSipCommonCfgTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1)
)
jnxSipCommonCfgTimerEntry.setIndexNames(
    (0, "JUNIPER-SIP-COMMON-MIB", "jnxSipCfgTimerApplName"),
)
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerEntry.setStatus("current")
_JnxSipCfgTimerApplName_Type = DisplayString
_JnxSipCfgTimerApplName_Object = MibTableColumn
jnxSipCfgTimerApplName = _JnxSipCfgTimerApplName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 1),
    _JnxSipCfgTimerApplName_Type()
)
jnxSipCfgTimerApplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSipCfgTimerApplName.setStatus("current")


class _JnxSipCommonCfgTimerA_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerA based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_JnxSipCommonCfgTimerA_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerA_Object = MibTableColumn
jnxSipCommonCfgTimerA = _JnxSipCommonCfgTimerA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 2),
    _JnxSipCommonCfgTimerA_Type()
)
jnxSipCommonCfgTimerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerA.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerA.setUnits("milliseconds")


class _JnxSipCommonCfgTimerB_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerB based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 300000),
    )


_JnxSipCommonCfgTimerB_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerB_Object = MibTableColumn
jnxSipCommonCfgTimerB = _JnxSipCommonCfgTimerB_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 3),
    _JnxSipCommonCfgTimerB_Type()
)
jnxSipCommonCfgTimerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerB.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerB.setUnits("milliseconds")


class _JnxSipCommonCfgTimerC_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerC based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180000, 300000),
    )


_JnxSipCommonCfgTimerC_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerC_Object = MibTableColumn
jnxSipCommonCfgTimerC = _JnxSipCommonCfgTimerC_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 4),
    _JnxSipCommonCfgTimerC_Type()
)
jnxSipCommonCfgTimerC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerC.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerC.setUnits("milliseconds")


class _JnxSipCommonCfgTimerD_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerD based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_JnxSipCommonCfgTimerD_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerD_Object = MibTableColumn
jnxSipCommonCfgTimerD = _JnxSipCommonCfgTimerD_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 5),
    _JnxSipCommonCfgTimerD_Type()
)
jnxSipCommonCfgTimerD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerD.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerD.setUnits("milliseconds")


class _JnxSipCommonCfgTimerE_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerE based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_JnxSipCommonCfgTimerE_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerE_Object = MibTableColumn
jnxSipCommonCfgTimerE = _JnxSipCommonCfgTimerE_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 6),
    _JnxSipCommonCfgTimerE_Type()
)
jnxSipCommonCfgTimerE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerE.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerE.setUnits("milliseconds")


class _JnxSipCommonCfgTimerF_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerF based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 300000),
    )


_JnxSipCommonCfgTimerF_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerF_Object = MibTableColumn
jnxSipCommonCfgTimerF = _JnxSipCommonCfgTimerF_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 7),
    _JnxSipCommonCfgTimerF_Type()
)
jnxSipCommonCfgTimerF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerF.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerF.setUnits("milliseconds")


class _JnxSipCommonCfgTimerG_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerG based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_JnxSipCommonCfgTimerG_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerG_Object = MibTableColumn
jnxSipCommonCfgTimerG = _JnxSipCommonCfgTimerG_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 8),
    _JnxSipCommonCfgTimerG_Type()
)
jnxSipCommonCfgTimerG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerG.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerG.setUnits("milliseconds")


class _JnxSipCommonCfgTimerH_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerH based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 300000),
    )


_JnxSipCommonCfgTimerH_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerH_Object = MibTableColumn
jnxSipCommonCfgTimerH = _JnxSipCommonCfgTimerH_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 9),
    _JnxSipCommonCfgTimerH_Type()
)
jnxSipCommonCfgTimerH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerH.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerH.setUnits("milliseconds")


class _JnxSipCommonCfgTimerI_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerI based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_JnxSipCommonCfgTimerI_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerI_Object = MibTableColumn
jnxSipCommonCfgTimerI = _JnxSipCommonCfgTimerI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 10),
    _JnxSipCommonCfgTimerI_Type()
)
jnxSipCommonCfgTimerI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerI.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerI.setUnits("milliseconds")


class _JnxSipCommonCfgTimerJ_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerJ based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32000, 300000),
    )


_JnxSipCommonCfgTimerJ_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerJ_Object = MibTableColumn
jnxSipCommonCfgTimerJ = _JnxSipCommonCfgTimerJ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 11),
    _JnxSipCommonCfgTimerJ_Type()
)
jnxSipCommonCfgTimerJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerJ.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerJ.setUnits("milliseconds")


class _JnxSipCommonCfgTimerK_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerK based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_JnxSipCommonCfgTimerK_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerK_Object = MibTableColumn
jnxSipCommonCfgTimerK = _JnxSipCommonCfgTimerK_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 12),
    _JnxSipCommonCfgTimerK_Type()
)
jnxSipCommonCfgTimerK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerK.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerK.setUnits("milliseconds")


class _JnxSipCommonCfgTimerT1_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerT1 based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_JnxSipCommonCfgTimerT1_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerT1_Object = MibTableColumn
jnxSipCommonCfgTimerT1 = _JnxSipCommonCfgTimerT1_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 13),
    _JnxSipCommonCfgTimerT1_Type()
)
jnxSipCommonCfgTimerT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerT1.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerT1.setUnits("milliseconds")


class _JnxSipCommonCfgTimerT2_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerT2 based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_JnxSipCommonCfgTimerT2_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerT2_Object = MibTableColumn
jnxSipCommonCfgTimerT2 = _JnxSipCommonCfgTimerT2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 14),
    _JnxSipCommonCfgTimerT2_Type()
)
jnxSipCommonCfgTimerT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerT2.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerT2.setUnits("milliseconds")


class _JnxSipCommonCfgTimerT4_Type(Unsigned32):
    """Custom type jnxSipCommonCfgTimerT4 based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 10000),
    )


_JnxSipCommonCfgTimerT4_Type.__name__ = "Unsigned32"
_JnxSipCommonCfgTimerT4_Object = MibTableColumn
jnxSipCommonCfgTimerT4 = _JnxSipCommonCfgTimerT4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 15, 2, 1, 1, 5, 1, 15),
    _JnxSipCommonCfgTimerT4_Type()
)
jnxSipCommonCfgTimerT4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerT4.setStatus("current")
if mibBuilder.loadTexts:
    jnxSipCommonCfgTimerT4.setUnits("milliseconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SIP-COMMON-MIB",
    **{"jnxSip": jnxSip,
       "jnxSipCommonMIB": jnxSipCommonMIB,
       "jnxSipCommonMIBObjects": jnxSipCommonMIBObjects,
       "jnxSipCommonCfgTable": jnxSipCommonCfgTable,
       "jnxSipCommonCfgEntry": jnxSipCommonCfgEntry,
       "jnxSipCfgApplName": jnxSipCfgApplName,
       "jnxSipCommonCfgProtocolVersion": jnxSipCommonCfgProtocolVersion,
       "jnxSipCommonCfgServiceOperStatus": jnxSipCommonCfgServiceOperStatus,
       "jnxSipCommonCfgServiceStartTime": jnxSipCommonCfgServiceStartTime,
       "jnxSipCommonCfgServiceLastChange": jnxSipCommonCfgServiceLastChange,
       "jnxSipCommonCfgOrganization": jnxSipCommonCfgOrganization,
       "jnxSipCommonCfgMaxTransactions": jnxSipCommonCfgMaxTransactions,
       "jnxSipCommonCfgEntityType": jnxSipCommonCfgEntityType,
       "jnxSipCommonPortTable": jnxSipCommonPortTable,
       "jnxSipCommonPortEntry": jnxSipCommonPortEntry,
       "jnxSipPortApplName": jnxSipPortApplName,
       "jnxSipCommonPort": jnxSipCommonPort,
       "jnxSipCommonPortTransportRcv": jnxSipCommonPortTransportRcv,
       "jnxSipCommonOptionTagTable": jnxSipCommonOptionTagTable,
       "jnxSipCommonOptionTagEntry": jnxSipCommonOptionTagEntry,
       "jnxSipOptionTagApplName": jnxSipOptionTagApplName,
       "jnxSipCommonOptionTagIndex": jnxSipCommonOptionTagIndex,
       "jnxSipCommonOptionTag": jnxSipCommonOptionTag,
       "jnxSipCommonOptionTagHeaderField": jnxSipCommonOptionTagHeaderField,
       "jnxSipCommonMethodSupportedTable": jnxSipCommonMethodSupportedTable,
       "jnxSipCommonMethodSupportedEntry": jnxSipCommonMethodSupportedEntry,
       "jnxSipMethodSupportedApplName": jnxSipMethodSupportedApplName,
       "jnxSipCommonMethodSupportedIndex": jnxSipCommonMethodSupportedIndex,
       "jnxSipCommonMethodSupportedName": jnxSipCommonMethodSupportedName,
       "jnxSipCommonCfgTimerTable": jnxSipCommonCfgTimerTable,
       "jnxSipCommonCfgTimerEntry": jnxSipCommonCfgTimerEntry,
       "jnxSipCfgTimerApplName": jnxSipCfgTimerApplName,
       "jnxSipCommonCfgTimerA": jnxSipCommonCfgTimerA,
       "jnxSipCommonCfgTimerB": jnxSipCommonCfgTimerB,
       "jnxSipCommonCfgTimerC": jnxSipCommonCfgTimerC,
       "jnxSipCommonCfgTimerD": jnxSipCommonCfgTimerD,
       "jnxSipCommonCfgTimerE": jnxSipCommonCfgTimerE,
       "jnxSipCommonCfgTimerF": jnxSipCommonCfgTimerF,
       "jnxSipCommonCfgTimerG": jnxSipCommonCfgTimerG,
       "jnxSipCommonCfgTimerH": jnxSipCommonCfgTimerH,
       "jnxSipCommonCfgTimerI": jnxSipCommonCfgTimerI,
       "jnxSipCommonCfgTimerJ": jnxSipCommonCfgTimerJ,
       "jnxSipCommonCfgTimerK": jnxSipCommonCfgTimerK,
       "jnxSipCommonCfgTimerT1": jnxSipCommonCfgTimerT1,
       "jnxSipCommonCfgTimerT2": jnxSipCommonCfgTimerT2,
       "jnxSipCommonCfgTimerT4": jnxSipCommonCfgTimerT4}
)
