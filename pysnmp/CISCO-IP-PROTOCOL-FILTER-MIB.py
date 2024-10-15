# SNMP MIB module (CISCO-IP-PROTOCOL-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-PROTOCOL-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:43 2024
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

(CfgFilterGroupName,) = mibBuilder.importSymbols(
    "CISCO-FILTER-GROUP-MIB",
    "CfgFilterGroupName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SyslogSeverity,) = mibBuilder.importSymbols(
    "CISCO-SYSLOG-MIB",
    "SyslogSeverity")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIpProtocolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 278)
)
ciscoIpProtocolMIB.setRevisions(
        ("2005-04-20 00:00",
         "2003-06-16 00:00",
         "2002-07-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CippfIpFilterProfileName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIpProtocolFilterMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIpProtocolFilterMIBNotifs = _CiscoIpProtocolFilterMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 0)
)
_CiscoIpProtocolFilterMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIpProtocolFilterMIBObjects = _CiscoIpProtocolFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1)
)
_CippfIpFilterConfig_ObjectIdentity = ObjectIdentity
cippfIpFilterConfig = _CippfIpFilterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1)
)
_CippfIpProfileTable_Object = MibTable
cippfIpProfileTable = _CippfIpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cippfIpProfileTable.setStatus("current")
_CippfIpProfileEntry_Object = MibTableRow
cippfIpProfileEntry = _CippfIpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 1, 1)
)
cippfIpProfileEntry.setIndexNames(
    (0, "CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpProfileName"),
)
if mibBuilder.loadTexts:
    cippfIpProfileEntry.setStatus("current")
_CippfIpProfileName_Type = CippfIpFilterProfileName
_CippfIpProfileName_Object = MibTableColumn
cippfIpProfileName = _CippfIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 1, 1, 1),
    _CippfIpProfileName_Type()
)
cippfIpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cippfIpProfileName.setStatus("current")


class _CippfIpProfileType_Type(Integer32):
    """Custom type cippfIpProfileType based on Integer32"""
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
        *(("extended", 2),
          ("extendedIPv6", 3),
          ("simple", 1))
    )


_CippfIpProfileType_Type.__name__ = "Integer32"
_CippfIpProfileType_Object = MibTableColumn
cippfIpProfileType = _CippfIpProfileType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 1, 1, 2),
    _CippfIpProfileType_Type()
)
cippfIpProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpProfileType.setStatus("current")


class _CippfIpProfileLastFilterIndex_Type(Unsigned32):
    """Custom type cippfIpProfileLastFilterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CippfIpProfileLastFilterIndex_Type.__name__ = "Unsigned32"
_CippfIpProfileLastFilterIndex_Object = MibTableColumn
cippfIpProfileLastFilterIndex = _CippfIpProfileLastFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 1, 1, 3),
    _CippfIpProfileLastFilterIndex_Type()
)
cippfIpProfileLastFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cippfIpProfileLastFilterIndex.setStatus("current")
_CippfIpProfileStatus_Type = RowStatus
_CippfIpProfileStatus_Object = MibTableColumn
cippfIpProfileStatus = _CippfIpProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 1, 1, 4),
    _CippfIpProfileStatus_Type()
)
cippfIpProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpProfileStatus.setStatus("current")
_CippfIfIpProfileTable_Object = MibTable
cippfIfIpProfileTable = _CippfIfIpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cippfIfIpProfileTable.setStatus("current")
_CippfIfIpProfileEntry_Object = MibTableRow
cippfIfIpProfileEntry = _CippfIfIpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 2, 1)
)
cippfIfIpProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIfIpProfileDirection"),
)
if mibBuilder.loadTexts:
    cippfIfIpProfileEntry.setStatus("current")


class _CippfIfIpProfileDirection_Type(Integer32):
    """Custom type cippfIfIpProfileDirection based on Integer32"""
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
        *(("inbound", 1),
          ("inboundIPv6", 3),
          ("outbound", 2),
          ("outboundIPv6", 4))
    )


_CippfIfIpProfileDirection_Type.__name__ = "Integer32"
_CippfIfIpProfileDirection_Object = MibTableColumn
cippfIfIpProfileDirection = _CippfIfIpProfileDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 2, 1, 1),
    _CippfIfIpProfileDirection_Type()
)
cippfIfIpProfileDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cippfIfIpProfileDirection.setStatus("current")
_CippfIfIpProfileName_Type = CippfIpFilterProfileName
_CippfIfIpProfileName_Object = MibTableColumn
cippfIfIpProfileName = _CippfIfIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 2, 1, 2),
    _CippfIfIpProfileName_Type()
)
cippfIfIpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIfIpProfileName.setStatus("current")
_CippfIfIpProfileStatus_Type = RowStatus
_CippfIfIpProfileStatus_Object = MibTableColumn
cippfIfIpProfileStatus = _CippfIfIpProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 2, 1, 3),
    _CippfIfIpProfileStatus_Type()
)
cippfIfIpProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIfIpProfileStatus.setStatus("current")
_CippfIpFilterTable_Object = MibTable
cippfIpFilterTable = _CippfIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cippfIpFilterTable.setStatus("current")
_CippfIpFilterEntry_Object = MibTableRow
cippfIpFilterEntry = _CippfIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1)
)
cippfIpFilterEntry.setIndexNames(
    (0, "CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpProfileName"),
    (0, "CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterIndex"),
)
if mibBuilder.loadTexts:
    cippfIpFilterEntry.setStatus("current")


class _CippfIpFilterIndex_Type(Unsigned32):
    """Custom type cippfIpFilterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CippfIpFilterIndex_Type.__name__ = "Unsigned32"
_CippfIpFilterIndex_Object = MibTableColumn
cippfIpFilterIndex = _CippfIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 1),
    _CippfIpFilterIndex_Type()
)
cippfIpFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cippfIpFilterIndex.setStatus("current")


class _CippfIpFilterOrderPosition_Type(Unsigned32):
    """Custom type cippfIpFilterOrderPosition based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CippfIpFilterOrderPosition_Type.__name__ = "Unsigned32"
_CippfIpFilterOrderPosition_Object = MibTableColumn
cippfIpFilterOrderPosition = _CippfIpFilterOrderPosition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 2),
    _CippfIpFilterOrderPosition_Type()
)
cippfIpFilterOrderPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterOrderPosition.setStatus("current")


class _CippfIpFilterAction_Type(Integer32):
    """Custom type cippfIpFilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_CippfIpFilterAction_Type.__name__ = "Integer32"
_CippfIpFilterAction_Object = MibTableColumn
cippfIpFilterAction = _CippfIpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 3),
    _CippfIpFilterAction_Type()
)
cippfIpFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterAction.setStatus("current")
_CippfIpFilterAddressType_Type = InetAddressType
_CippfIpFilterAddressType_Object = MibTableColumn
cippfIpFilterAddressType = _CippfIpFilterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 4),
    _CippfIpFilterAddressType_Type()
)
cippfIpFilterAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterAddressType.setStatus("current")


class _CippfIpFilterSrcAddress_Type(InetAddress):
    """Custom type cippfIpFilterSrcAddress based on InetAddress"""
    defaultValue = OctetString("0")


_CippfIpFilterSrcAddress_Object = MibTableColumn
cippfIpFilterSrcAddress = _CippfIpFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 5),
    _CippfIpFilterSrcAddress_Type()
)
cippfIpFilterSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterSrcAddress.setStatus("current")


class _CippfIpFilterSrcMask_Type(InetAddress):
    """Custom type cippfIpFilterSrcMask based on InetAddress"""
    defaultHexValue = "ffffffff"


_CippfIpFilterSrcMask_Object = MibTableColumn
cippfIpFilterSrcMask = _CippfIpFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 6),
    _CippfIpFilterSrcMask_Type()
)
cippfIpFilterSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterSrcMask.setStatus("current")


class _CippfIpFilterDestAddress_Type(InetAddress):
    """Custom type cippfIpFilterDestAddress based on InetAddress"""
    defaultValue = OctetString("0")


_CippfIpFilterDestAddress_Object = MibTableColumn
cippfIpFilterDestAddress = _CippfIpFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 7),
    _CippfIpFilterDestAddress_Type()
)
cippfIpFilterDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterDestAddress.setStatus("current")


class _CippfIpFilterDestMask_Type(InetAddress):
    """Custom type cippfIpFilterDestMask based on InetAddress"""
    defaultHexValue = "ffffffff"


_CippfIpFilterDestMask_Object = MibTableColumn
cippfIpFilterDestMask = _CippfIpFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 8),
    _CippfIpFilterDestMask_Type()
)
cippfIpFilterDestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterDestMask.setStatus("current")


class _CippfIpFilterProtocol_Type(Integer32):
    """Custom type cippfIpFilterProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CippfIpFilterProtocol_Type.__name__ = "Integer32"
_CippfIpFilterProtocol_Object = MibTableColumn
cippfIpFilterProtocol = _CippfIpFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 9),
    _CippfIpFilterProtocol_Type()
)
cippfIpFilterProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterProtocol.setStatus("current")


class _CippfIpFilterSrcPortLow_Type(InetPortNumber):
    """Custom type cippfIpFilterSrcPortLow based on InetPortNumber"""
    defaultValue = 0


_CippfIpFilterSrcPortLow_Object = MibTableColumn
cippfIpFilterSrcPortLow = _CippfIpFilterSrcPortLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 10),
    _CippfIpFilterSrcPortLow_Type()
)
cippfIpFilterSrcPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterSrcPortLow.setStatus("current")


class _CippfIpFilterSrcPortHigh_Type(InetPortNumber):
    """Custom type cippfIpFilterSrcPortHigh based on InetPortNumber"""
    defaultValue = 65535


_CippfIpFilterSrcPortHigh_Object = MibTableColumn
cippfIpFilterSrcPortHigh = _CippfIpFilterSrcPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 11),
    _CippfIpFilterSrcPortHigh_Type()
)
cippfIpFilterSrcPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterSrcPortHigh.setStatus("current")


class _CippfIpFilterDestPortLow_Type(InetPortNumber):
    """Custom type cippfIpFilterDestPortLow based on InetPortNumber"""
    defaultValue = 0


_CippfIpFilterDestPortLow_Object = MibTableColumn
cippfIpFilterDestPortLow = _CippfIpFilterDestPortLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 12),
    _CippfIpFilterDestPortLow_Type()
)
cippfIpFilterDestPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterDestPortLow.setStatus("current")


class _CippfIpFilterDestPortHigh_Type(InetPortNumber):
    """Custom type cippfIpFilterDestPortHigh based on InetPortNumber"""
    defaultValue = 65535


_CippfIpFilterDestPortHigh_Object = MibTableColumn
cippfIpFilterDestPortHigh = _CippfIpFilterDestPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 13),
    _CippfIpFilterDestPortHigh_Type()
)
cippfIpFilterDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterDestPortHigh.setStatus("current")


class _CippfIpFilterPrecedence_Type(Integer32):
    """Custom type cippfIpFilterPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("any", -1),
          ("critical", 5),
          ("flash", 3),
          ("flashOverride", 4),
          ("immediate", 2),
          ("internet", 6),
          ("network", 7),
          ("priority", 1),
          ("routine", 0))
    )


_CippfIpFilterPrecedence_Type.__name__ = "Integer32"
_CippfIpFilterPrecedence_Object = MibTableColumn
cippfIpFilterPrecedence = _CippfIpFilterPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 14),
    _CippfIpFilterPrecedence_Type()
)
cippfIpFilterPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterPrecedence.setStatus("current")


class _CippfIpFilterTos_Type(Integer32):
    """Custom type cippfIpFilterTos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_CippfIpFilterTos_Type.__name__ = "Integer32"
_CippfIpFilterTos_Object = MibTableColumn
cippfIpFilterTos = _CippfIpFilterTos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 15),
    _CippfIpFilterTos_Type()
)
cippfIpFilterTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterTos.setStatus("current")


class _CippfIpFilterLogEnabled_Type(TruthValue):
    """Custom type cippfIpFilterLogEnabled based on TruthValue"""


_CippfIpFilterLogEnabled_Object = MibTableColumn
cippfIpFilterLogEnabled = _CippfIpFilterLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 16),
    _CippfIpFilterLogEnabled_Type()
)
cippfIpFilterLogEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterLogEnabled.setStatus("current")
_CippfIpFilterStatus_Type = RowStatus
_CippfIpFilterStatus_Object = MibTableColumn
cippfIpFilterStatus = _CippfIpFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 17),
    _CippfIpFilterStatus_Type()
)
cippfIpFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterStatus.setStatus("current")


class _CippfIpFilterICMPType_Type(Integer32):
    """Custom type cippfIpFilterICMPType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CippfIpFilterICMPType_Type.__name__ = "Integer32"
_CippfIpFilterICMPType_Object = MibTableColumn
cippfIpFilterICMPType = _CippfIpFilterICMPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 18),
    _CippfIpFilterICMPType_Type()
)
cippfIpFilterICMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterICMPType.setStatus("current")


class _CippfIpFilterTCPEstablished_Type(TruthValue):
    """Custom type cippfIpFilterTCPEstablished based on TruthValue"""


_CippfIpFilterTCPEstablished_Object = MibTableColumn
cippfIpFilterTCPEstablished = _CippfIpFilterTCPEstablished_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 19),
    _CippfIpFilterTCPEstablished_Type()
)
cippfIpFilterTCPEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterTCPEstablished.setStatus("current")


class _CippfIpFilterFragments_Type(TruthValue):
    """Custom type cippfIpFilterFragments based on TruthValue"""


_CippfIpFilterFragments_Object = MibTableColumn
cippfIpFilterFragments = _CippfIpFilterFragments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 20),
    _CippfIpFilterFragments_Type()
)
cippfIpFilterFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterFragments.setStatus("current")


class _CippfIpFilterICMPCode_Type(Integer32):
    """Custom type cippfIpFilterICMPCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CippfIpFilterICMPCode_Type.__name__ = "Integer32"
_CippfIpFilterICMPCode_Object = MibTableColumn
cippfIpFilterICMPCode = _CippfIpFilterICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 21),
    _CippfIpFilterICMPCode_Type()
)
cippfIpFilterICMPCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterICMPCode.setStatus("current")
_CippfIpFilterSrcIPGroupName_Type = CfgFilterGroupName
_CippfIpFilterSrcIPGroupName_Object = MibTableColumn
cippfIpFilterSrcIPGroupName = _CippfIpFilterSrcIPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 22),
    _CippfIpFilterSrcIPGroupName_Type()
)
cippfIpFilterSrcIPGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterSrcIPGroupName.setStatus("current")
_CippfIpFilterDstIPGroupName_Type = CfgFilterGroupName
_CippfIpFilterDstIPGroupName_Object = MibTableColumn
cippfIpFilterDstIPGroupName = _CippfIpFilterDstIPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 23),
    _CippfIpFilterDstIPGroupName_Type()
)
cippfIpFilterDstIPGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterDstIPGroupName.setStatus("current")
_CippfIpFilterProtocolGroupName_Type = CfgFilterGroupName
_CippfIpFilterProtocolGroupName_Object = MibTableColumn
cippfIpFilterProtocolGroupName = _CippfIpFilterProtocolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 24),
    _CippfIpFilterProtocolGroupName_Type()
)
cippfIpFilterProtocolGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterProtocolGroupName.setStatus("current")
_CippfIpFilterSrcServiceGroupName_Type = CfgFilterGroupName
_CippfIpFilterSrcServiceGroupName_Object = MibTableColumn
cippfIpFilterSrcServiceGroupName = _CippfIpFilterSrcServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 25),
    _CippfIpFilterSrcServiceGroupName_Type()
)
cippfIpFilterSrcServiceGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterSrcServiceGroupName.setStatus("current")
_CippfIpFilterDstServiceGroupName_Type = CfgFilterGroupName
_CippfIpFilterDstServiceGroupName_Object = MibTableColumn
cippfIpFilterDstServiceGroupName = _CippfIpFilterDstServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 26),
    _CippfIpFilterDstServiceGroupName_Type()
)
cippfIpFilterDstServiceGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterDstServiceGroupName.setStatus("current")
_CippfIpFilterICMPGroupName_Type = CfgFilterGroupName
_CippfIpFilterICMPGroupName_Object = MibTableColumn
cippfIpFilterICMPGroupName = _CippfIpFilterICMPGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 3, 1, 27),
    _CippfIpFilterICMPGroupName_Type()
)
cippfIpFilterICMPGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterICMPGroupName.setStatus("current")
_CippfIpFilterExtTable_Object = MibTable
cippfIpFilterExtTable = _CippfIpFilterExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cippfIpFilterExtTable.setStatus("current")
_CippfIpFilterExtEntry_Object = MibTableRow
cippfIpFilterExtEntry = _CippfIpFilterExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cippfIpFilterExtEntry.setStatus("current")
_CippfIpFilterExtDescription_Type = SnmpAdminString
_CippfIpFilterExtDescription_Object = MibTableColumn
cippfIpFilterExtDescription = _CippfIpFilterExtDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 4, 1, 1),
    _CippfIpFilterExtDescription_Type()
)
cippfIpFilterExtDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterExtDescription.setStatus("current")


class _CippfIpFilterExtLogLevel_Type(SyslogSeverity):
    """Custom type cippfIpFilterExtLogLevel based on SyslogSeverity"""


_CippfIpFilterExtLogLevel_Object = MibTableColumn
cippfIpFilterExtLogLevel = _CippfIpFilterExtLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 4, 1, 2),
    _CippfIpFilterExtLogLevel_Type()
)
cippfIpFilterExtLogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterExtLogLevel.setStatus("current")


class _CippfIpFilterExtLogInterval_Type(Unsigned32):
    """Custom type cippfIpFilterExtLogInterval based on Unsigned32"""
    defaultValue = 300


_CippfIpFilterExtLogInterval_Object = MibTableColumn
cippfIpFilterExtLogInterval = _CippfIpFilterExtLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 1, 4, 1, 3),
    _CippfIpFilterExtLogInterval_Type()
)
cippfIpFilterExtLogInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cippfIpFilterExtLogInterval.setStatus("current")
if mibBuilder.loadTexts:
    cippfIpFilterExtLogInterval.setUnits("seconds")
_CippfIpFilterStats_ObjectIdentity = ObjectIdentity
cippfIpFilterStats = _CippfIpFilterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 2)
)
_CippfIpFilterStatsTable_Object = MibTable
cippfIpFilterStatsTable = _CippfIpFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cippfIpFilterStatsTable.setStatus("current")
_CippfIpFilterStatsEntry_Object = MibTableRow
cippfIpFilterStatsEntry = _CippfIpFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 2, 1, 1)
)
cippfIpFilterStatsEntry.setIndexNames(
    (0, "CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpProfileName"),
    (0, "CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterIndex"),
)
if mibBuilder.loadTexts:
    cippfIpFilterStatsEntry.setStatus("current")
_CippfIpFilterHits_Type = Counter64
_CippfIpFilterHits_Object = MibTableColumn
cippfIpFilterHits = _CippfIpFilterHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 1, 2, 1, 1, 1),
    _CippfIpFilterHits_Type()
)
cippfIpFilterHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cippfIpFilterHits.setStatus("current")
_CiscoIpProtocolFilterMIBConform_ObjectIdentity = ObjectIdentity
ciscoIpProtocolFilterMIBConform = _CiscoIpProtocolFilterMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2)
)
_CiscoIpProtocolFilterMIBCompl_ObjectIdentity = ObjectIdentity
ciscoIpProtocolFilterMIBCompl = _CiscoIpProtocolFilterMIBCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 1)
)
_CiscoIpProtocolFilterMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIpProtocolFilterMIBGroups = _CiscoIpProtocolFilterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 2)
)
cippfIpFilterEntry.registerAugmentions(
    ("CISCO-IP-PROTOCOL-FILTER-MIB",
     "cippfIpFilterExtEntry")
)
cippfIpFilterExtEntry.setIndexNames(*cippfIpFilterEntry.getIndexNames())

# Managed Objects groups

ciscoIpProtocolFilteringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 2, 1)
)
ciscoIpProtocolFilteringGroup.setObjects(
      *(("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpProfileType"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpProfileLastFilterIndex"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpProfileStatus"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIfIpProfileName"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIfIpProfileStatus"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterOrderPosition"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterAction"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterAddressType"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterSrcAddress"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterSrcMask"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterDestAddress"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterDestMask"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterProtocol"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterSrcPortLow"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterSrcPortHigh"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterDestPortLow"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterDestPortHigh"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterPrecedence"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterTos"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterLogEnabled"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterStatus"))
)
if mibBuilder.loadTexts:
    ciscoIpProtocolFilteringGroup.setStatus("current")

ciscoIpProtocolFilterGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 2, 2)
)
ciscoIpProtocolFilterGroup2.setObjects(
      *(("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterICMPType"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterTCPEstablished"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterFragments"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterICMPCode"))
)
if mibBuilder.loadTexts:
    ciscoIpProtocolFilterGroup2.setStatus("current")

ciscoIpProtocolFilterExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 2, 4)
)
ciscoIpProtocolFilterExtGroup.setObjects(
      *(("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterExtDescription"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterExtLogLevel"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterExtLogInterval"))
)
if mibBuilder.loadTexts:
    ciscoIpProtocolFilterExtGroup.setStatus("current")

ciscoIpProtocolFilterObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 2, 5)
)
ciscoIpProtocolFilterObjectGroup.setObjects(
      *(("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterSrcIPGroupName"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterDstIPGroupName"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterProtocolGroupName"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterSrcServiceGroupName"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterDstServiceGroupName"),
        ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterICMPGroupName"))
)
if mibBuilder.loadTexts:
    ciscoIpProtocolFilterObjectGroup.setStatus("current")

ciscoIpProtocolFilterStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 2, 6)
)
ciscoIpProtocolFilterStatsGroup.setObjects(
    ("CISCO-IP-PROTOCOL-FILTER-MIB", "cippfIpFilterHits")
)
if mibBuilder.loadTexts:
    ciscoIpProtocolFilterStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIpProtocolMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIpProtocolMIBCompliance.setStatus(
        "deprecated"
    )

ciscoIpProtocolMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIpProtocolMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoIpProtocolMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 278, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoIpProtocolMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-PROTOCOL-FILTER-MIB",
    **{"CippfIpFilterProfileName": CippfIpFilterProfileName,
       "ciscoIpProtocolMIB": ciscoIpProtocolMIB,
       "ciscoIpProtocolFilterMIBNotifs": ciscoIpProtocolFilterMIBNotifs,
       "ciscoIpProtocolFilterMIBObjects": ciscoIpProtocolFilterMIBObjects,
       "cippfIpFilterConfig": cippfIpFilterConfig,
       "cippfIpProfileTable": cippfIpProfileTable,
       "cippfIpProfileEntry": cippfIpProfileEntry,
       "cippfIpProfileName": cippfIpProfileName,
       "cippfIpProfileType": cippfIpProfileType,
       "cippfIpProfileLastFilterIndex": cippfIpProfileLastFilterIndex,
       "cippfIpProfileStatus": cippfIpProfileStatus,
       "cippfIfIpProfileTable": cippfIfIpProfileTable,
       "cippfIfIpProfileEntry": cippfIfIpProfileEntry,
       "cippfIfIpProfileDirection": cippfIfIpProfileDirection,
       "cippfIfIpProfileName": cippfIfIpProfileName,
       "cippfIfIpProfileStatus": cippfIfIpProfileStatus,
       "cippfIpFilterTable": cippfIpFilterTable,
       "cippfIpFilterEntry": cippfIpFilterEntry,
       "cippfIpFilterIndex": cippfIpFilterIndex,
       "cippfIpFilterOrderPosition": cippfIpFilterOrderPosition,
       "cippfIpFilterAction": cippfIpFilterAction,
       "cippfIpFilterAddressType": cippfIpFilterAddressType,
       "cippfIpFilterSrcAddress": cippfIpFilterSrcAddress,
       "cippfIpFilterSrcMask": cippfIpFilterSrcMask,
       "cippfIpFilterDestAddress": cippfIpFilterDestAddress,
       "cippfIpFilterDestMask": cippfIpFilterDestMask,
       "cippfIpFilterProtocol": cippfIpFilterProtocol,
       "cippfIpFilterSrcPortLow": cippfIpFilterSrcPortLow,
       "cippfIpFilterSrcPortHigh": cippfIpFilterSrcPortHigh,
       "cippfIpFilterDestPortLow": cippfIpFilterDestPortLow,
       "cippfIpFilterDestPortHigh": cippfIpFilterDestPortHigh,
       "cippfIpFilterPrecedence": cippfIpFilterPrecedence,
       "cippfIpFilterTos": cippfIpFilterTos,
       "cippfIpFilterLogEnabled": cippfIpFilterLogEnabled,
       "cippfIpFilterStatus": cippfIpFilterStatus,
       "cippfIpFilterICMPType": cippfIpFilterICMPType,
       "cippfIpFilterTCPEstablished": cippfIpFilterTCPEstablished,
       "cippfIpFilterFragments": cippfIpFilterFragments,
       "cippfIpFilterICMPCode": cippfIpFilterICMPCode,
       "cippfIpFilterSrcIPGroupName": cippfIpFilterSrcIPGroupName,
       "cippfIpFilterDstIPGroupName": cippfIpFilterDstIPGroupName,
       "cippfIpFilterProtocolGroupName": cippfIpFilterProtocolGroupName,
       "cippfIpFilterSrcServiceGroupName": cippfIpFilterSrcServiceGroupName,
       "cippfIpFilterDstServiceGroupName": cippfIpFilterDstServiceGroupName,
       "cippfIpFilterICMPGroupName": cippfIpFilterICMPGroupName,
       "cippfIpFilterExtTable": cippfIpFilterExtTable,
       "cippfIpFilterExtEntry": cippfIpFilterExtEntry,
       "cippfIpFilterExtDescription": cippfIpFilterExtDescription,
       "cippfIpFilterExtLogLevel": cippfIpFilterExtLogLevel,
       "cippfIpFilterExtLogInterval": cippfIpFilterExtLogInterval,
       "cippfIpFilterStats": cippfIpFilterStats,
       "cippfIpFilterStatsTable": cippfIpFilterStatsTable,
       "cippfIpFilterStatsEntry": cippfIpFilterStatsEntry,
       "cippfIpFilterHits": cippfIpFilterHits,
       "ciscoIpProtocolFilterMIBConform": ciscoIpProtocolFilterMIBConform,
       "ciscoIpProtocolFilterMIBCompl": ciscoIpProtocolFilterMIBCompl,
       "ciscoIpProtocolMIBCompliance": ciscoIpProtocolMIBCompliance,
       "ciscoIpProtocolMIBComplianceRev1": ciscoIpProtocolMIBComplianceRev1,
       "ciscoIpProtocolMIBComplianceRev2": ciscoIpProtocolMIBComplianceRev2,
       "ciscoIpProtocolFilterMIBGroups": ciscoIpProtocolFilterMIBGroups,
       "ciscoIpProtocolFilteringGroup": ciscoIpProtocolFilteringGroup,
       "ciscoIpProtocolFilterGroup2": ciscoIpProtocolFilterGroup2,
       "ciscoIpProtocolFilterExtGroup": ciscoIpProtocolFilterExtGroup,
       "ciscoIpProtocolFilterObjectGroup": ciscoIpProtocolFilterObjectGroup,
       "ciscoIpProtocolFilterStatsGroup": ciscoIpProtocolFilterStatsGroup}
)
