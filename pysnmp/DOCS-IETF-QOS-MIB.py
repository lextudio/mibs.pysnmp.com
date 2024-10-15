# SNMP MIB module (DOCS-IETF-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-IETF-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:39 2024
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

(DscpOrAny,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "DscpOrAny")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

docsIetfQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 127)
)
docsIetfQosMIB.setRevisions(
        ("2006-01-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DocsIetfQosRfMacIfDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )



class DocsIetfQosBitRate(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class DocsIetfQosSchedulingType(Integer32, TextualConvention):
    status = "current"
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
        *(("bestEffort", 2),
          ("nonRealTimePollingService", 3),
          ("realTimePollingService", 4),
          ("undefined", 1),
          ("unsolictedGrantService", 6),
          ("unsolictedGrantServiceWithAD", 5))
    )



# MIB Managed Objects in the order of their OIDs

_DocsIetfQosNotifications_ObjectIdentity = ObjectIdentity
docsIetfQosNotifications = _DocsIetfQosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 127, 0)
)
_DocsIetfQosMIBObjects_ObjectIdentity = ObjectIdentity
docsIetfQosMIBObjects = _DocsIetfQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 127, 1)
)
_DocsIetfQosPktClassTable_Object = MibTable
docsIetfQosPktClassTable = _DocsIetfQosPktClassTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1)
)
if mibBuilder.loadTexts:
    docsIetfQosPktClassTable.setStatus("current")
_DocsIetfQosPktClassEntry_Object = MibTableRow
docsIetfQosPktClassEntry = _DocsIetfQosPktClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1)
)
docsIetfQosPktClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowId"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosPktClassId"),
)
if mibBuilder.loadTexts:
    docsIetfQosPktClassEntry.setStatus("current")


class _DocsIetfQosPktClassId_Type(Unsigned32):
    """Custom type docsIetfQosPktClassId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsIetfQosPktClassId_Type.__name__ = "Unsigned32"
_DocsIetfQosPktClassId_Object = MibTableColumn
docsIetfQosPktClassId = _DocsIetfQosPktClassId_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 1),
    _DocsIetfQosPktClassId_Type()
)
docsIetfQosPktClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosPktClassId.setStatus("current")
_DocsIetfQosPktClassDirection_Type = DocsIetfQosRfMacIfDirection
_DocsIetfQosPktClassDirection_Object = MibTableColumn
docsIetfQosPktClassDirection = _DocsIetfQosPktClassDirection_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 2),
    _DocsIetfQosPktClassDirection_Type()
)
docsIetfQosPktClassDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassDirection.setStatus("current")


class _DocsIetfQosPktClassPriority_Type(Integer32):
    """Custom type docsIetfQosPktClassPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIetfQosPktClassPriority_Type.__name__ = "Integer32"
_DocsIetfQosPktClassPriority_Object = MibTableColumn
docsIetfQosPktClassPriority = _DocsIetfQosPktClassPriority_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 3),
    _DocsIetfQosPktClassPriority_Type()
)
docsIetfQosPktClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassPriority.setStatus("current")


class _DocsIetfQosPktClassIpTosLow_Type(OctetString):
    """Custom type docsIetfQosPktClassIpTosLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsIetfQosPktClassIpTosLow_Type.__name__ = "OctetString"
_DocsIetfQosPktClassIpTosLow_Object = MibTableColumn
docsIetfQosPktClassIpTosLow = _DocsIetfQosPktClassIpTosLow_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 4),
    _DocsIetfQosPktClassIpTosLow_Type()
)
docsIetfQosPktClassIpTosLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassIpTosLow.setStatus("current")


class _DocsIetfQosPktClassIpTosHigh_Type(OctetString):
    """Custom type docsIetfQosPktClassIpTosHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsIetfQosPktClassIpTosHigh_Type.__name__ = "OctetString"
_DocsIetfQosPktClassIpTosHigh_Object = MibTableColumn
docsIetfQosPktClassIpTosHigh = _DocsIetfQosPktClassIpTosHigh_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 5),
    _DocsIetfQosPktClassIpTosHigh_Type()
)
docsIetfQosPktClassIpTosHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassIpTosHigh.setStatus("current")


class _DocsIetfQosPktClassIpTosMask_Type(OctetString):
    """Custom type docsIetfQosPktClassIpTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsIetfQosPktClassIpTosMask_Type.__name__ = "OctetString"
_DocsIetfQosPktClassIpTosMask_Object = MibTableColumn
docsIetfQosPktClassIpTosMask = _DocsIetfQosPktClassIpTosMask_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 6),
    _DocsIetfQosPktClassIpTosMask_Type()
)
docsIetfQosPktClassIpTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassIpTosMask.setStatus("current")


class _DocsIetfQosPktClassIpProtocol_Type(Integer32):
    """Custom type docsIetfQosPktClassIpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 258),
    )


_DocsIetfQosPktClassIpProtocol_Type.__name__ = "Integer32"
_DocsIetfQosPktClassIpProtocol_Object = MibTableColumn
docsIetfQosPktClassIpProtocol = _DocsIetfQosPktClassIpProtocol_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 7),
    _DocsIetfQosPktClassIpProtocol_Type()
)
docsIetfQosPktClassIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassIpProtocol.setStatus("current")
_DocsIetfQosPktClassInetAddressType_Type = InetAddressType
_DocsIetfQosPktClassInetAddressType_Object = MibTableColumn
docsIetfQosPktClassInetAddressType = _DocsIetfQosPktClassInetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 8),
    _DocsIetfQosPktClassInetAddressType_Type()
)
docsIetfQosPktClassInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassInetAddressType.setStatus("current")
_DocsIetfQosPktClassInetSourceAddr_Type = InetAddress
_DocsIetfQosPktClassInetSourceAddr_Object = MibTableColumn
docsIetfQosPktClassInetSourceAddr = _DocsIetfQosPktClassInetSourceAddr_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 9),
    _DocsIetfQosPktClassInetSourceAddr_Type()
)
docsIetfQosPktClassInetSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassInetSourceAddr.setStatus("current")
_DocsIetfQosPktClassInetSourceMask_Type = InetAddress
_DocsIetfQosPktClassInetSourceMask_Object = MibTableColumn
docsIetfQosPktClassInetSourceMask = _DocsIetfQosPktClassInetSourceMask_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 10),
    _DocsIetfQosPktClassInetSourceMask_Type()
)
docsIetfQosPktClassInetSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassInetSourceMask.setStatus("current")
_DocsIetfQosPktClassInetDestAddr_Type = InetAddress
_DocsIetfQosPktClassInetDestAddr_Object = MibTableColumn
docsIetfQosPktClassInetDestAddr = _DocsIetfQosPktClassInetDestAddr_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 11),
    _DocsIetfQosPktClassInetDestAddr_Type()
)
docsIetfQosPktClassInetDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassInetDestAddr.setStatus("current")
_DocsIetfQosPktClassInetDestMask_Type = InetAddress
_DocsIetfQosPktClassInetDestMask_Object = MibTableColumn
docsIetfQosPktClassInetDestMask = _DocsIetfQosPktClassInetDestMask_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 12),
    _DocsIetfQosPktClassInetDestMask_Type()
)
docsIetfQosPktClassInetDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassInetDestMask.setStatus("current")
_DocsIetfQosPktClassSourcePortStart_Type = InetPortNumber
_DocsIetfQosPktClassSourcePortStart_Object = MibTableColumn
docsIetfQosPktClassSourcePortStart = _DocsIetfQosPktClassSourcePortStart_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 13),
    _DocsIetfQosPktClassSourcePortStart_Type()
)
docsIetfQosPktClassSourcePortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassSourcePortStart.setStatus("current")
_DocsIetfQosPktClassSourcePortEnd_Type = InetPortNumber
_DocsIetfQosPktClassSourcePortEnd_Object = MibTableColumn
docsIetfQosPktClassSourcePortEnd = _DocsIetfQosPktClassSourcePortEnd_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 14),
    _DocsIetfQosPktClassSourcePortEnd_Type()
)
docsIetfQosPktClassSourcePortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassSourcePortEnd.setStatus("current")
_DocsIetfQosPktClassDestPortStart_Type = InetPortNumber
_DocsIetfQosPktClassDestPortStart_Object = MibTableColumn
docsIetfQosPktClassDestPortStart = _DocsIetfQosPktClassDestPortStart_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 15),
    _DocsIetfQosPktClassDestPortStart_Type()
)
docsIetfQosPktClassDestPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassDestPortStart.setStatus("current")
_DocsIetfQosPktClassDestPortEnd_Type = InetPortNumber
_DocsIetfQosPktClassDestPortEnd_Object = MibTableColumn
docsIetfQosPktClassDestPortEnd = _DocsIetfQosPktClassDestPortEnd_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 16),
    _DocsIetfQosPktClassDestPortEnd_Type()
)
docsIetfQosPktClassDestPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassDestPortEnd.setStatus("current")
_DocsIetfQosPktClassDestMacAddr_Type = MacAddress
_DocsIetfQosPktClassDestMacAddr_Object = MibTableColumn
docsIetfQosPktClassDestMacAddr = _DocsIetfQosPktClassDestMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 17),
    _DocsIetfQosPktClassDestMacAddr_Type()
)
docsIetfQosPktClassDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassDestMacAddr.setStatus("current")
_DocsIetfQosPktClassDestMacMask_Type = MacAddress
_DocsIetfQosPktClassDestMacMask_Object = MibTableColumn
docsIetfQosPktClassDestMacMask = _DocsIetfQosPktClassDestMacMask_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 18),
    _DocsIetfQosPktClassDestMacMask_Type()
)
docsIetfQosPktClassDestMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassDestMacMask.setStatus("current")
_DocsIetfQosPktClassSourceMacAddr_Type = MacAddress
_DocsIetfQosPktClassSourceMacAddr_Object = MibTableColumn
docsIetfQosPktClassSourceMacAddr = _DocsIetfQosPktClassSourceMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 19),
    _DocsIetfQosPktClassSourceMacAddr_Type()
)
docsIetfQosPktClassSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassSourceMacAddr.setStatus("current")


class _DocsIetfQosPktClassEnetProtocolType_Type(Integer32):
    """Custom type docsIetfQosPktClassEnetProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 4),
          ("dsap", 2),
          ("ethertype", 1),
          ("mac", 3),
          ("none", 0))
    )


_DocsIetfQosPktClassEnetProtocolType_Type.__name__ = "Integer32"
_DocsIetfQosPktClassEnetProtocolType_Object = MibTableColumn
docsIetfQosPktClassEnetProtocolType = _DocsIetfQosPktClassEnetProtocolType_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 20),
    _DocsIetfQosPktClassEnetProtocolType_Type()
)
docsIetfQosPktClassEnetProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassEnetProtocolType.setStatus("current")


class _DocsIetfQosPktClassEnetProtocol_Type(Integer32):
    """Custom type docsIetfQosPktClassEnetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosPktClassEnetProtocol_Type.__name__ = "Integer32"
_DocsIetfQosPktClassEnetProtocol_Object = MibTableColumn
docsIetfQosPktClassEnetProtocol = _DocsIetfQosPktClassEnetProtocol_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 21),
    _DocsIetfQosPktClassEnetProtocol_Type()
)
docsIetfQosPktClassEnetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassEnetProtocol.setStatus("current")


class _DocsIetfQosPktClassUserPriLow_Type(Integer32):
    """Custom type docsIetfQosPktClassUserPriLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsIetfQosPktClassUserPriLow_Type.__name__ = "Integer32"
_DocsIetfQosPktClassUserPriLow_Object = MibTableColumn
docsIetfQosPktClassUserPriLow = _DocsIetfQosPktClassUserPriLow_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 22),
    _DocsIetfQosPktClassUserPriLow_Type()
)
docsIetfQosPktClassUserPriLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassUserPriLow.setStatus("current")


class _DocsIetfQosPktClassUserPriHigh_Type(Integer32):
    """Custom type docsIetfQosPktClassUserPriHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsIetfQosPktClassUserPriHigh_Type.__name__ = "Integer32"
_DocsIetfQosPktClassUserPriHigh_Object = MibTableColumn
docsIetfQosPktClassUserPriHigh = _DocsIetfQosPktClassUserPriHigh_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 23),
    _DocsIetfQosPktClassUserPriHigh_Type()
)
docsIetfQosPktClassUserPriHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassUserPriHigh.setStatus("current")


class _DocsIetfQosPktClassVlanId_Type(Integer32):
    """Custom type docsIetfQosPktClassVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_DocsIetfQosPktClassVlanId_Type.__name__ = "Integer32"
_DocsIetfQosPktClassVlanId_Object = MibTableColumn
docsIetfQosPktClassVlanId = _DocsIetfQosPktClassVlanId_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 24),
    _DocsIetfQosPktClassVlanId_Type()
)
docsIetfQosPktClassVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassVlanId.setStatus("current")
_DocsIetfQosPktClassStateActive_Type = TruthValue
_DocsIetfQosPktClassStateActive_Object = MibTableColumn
docsIetfQosPktClassStateActive = _DocsIetfQosPktClassStateActive_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 25),
    _DocsIetfQosPktClassStateActive_Type()
)
docsIetfQosPktClassStateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassStateActive.setStatus("current")
_DocsIetfQosPktClassPkts_Type = Counter64
_DocsIetfQosPktClassPkts_Object = MibTableColumn
docsIetfQosPktClassPkts = _DocsIetfQosPktClassPkts_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 26),
    _DocsIetfQosPktClassPkts_Type()
)
docsIetfQosPktClassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassPkts.setStatus("current")


class _DocsIetfQosPktClassBitMap_Type(Bits):
    """Custom type docsIetfQosPktClassBitMap based on Bits"""
    namedValues = NamedValues(
        *(("activationState", 1),
          ("destMac", 12),
          ("destPortEnd", 11),
          ("destPortStart", 10),
          ("ethertype", 14),
          ("ipDestAddr", 6),
          ("ipDestMask", 7),
          ("ipProtocol", 3),
          ("ipSourceAddr", 4),
          ("ipSourceMask", 5),
          ("ipTos", 2),
          ("rulePriority", 0),
          ("sourceMac", 13),
          ("sourcePortEnd", 9),
          ("sourcePortStart", 8),
          ("userPri", 15),
          ("vlanId", 16))
    )

_DocsIetfQosPktClassBitMap_Type.__name__ = "Bits"
_DocsIetfQosPktClassBitMap_Object = MibTableColumn
docsIetfQosPktClassBitMap = _DocsIetfQosPktClassBitMap_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 1, 1, 27),
    _DocsIetfQosPktClassBitMap_Type()
)
docsIetfQosPktClassBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPktClassBitMap.setStatus("current")
_DocsIetfQosParamSetTable_Object = MibTable
docsIetfQosParamSetTable = _DocsIetfQosParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2)
)
if mibBuilder.loadTexts:
    docsIetfQosParamSetTable.setStatus("current")
_DocsIetfQosParamSetEntry_Object = MibTableRow
docsIetfQosParamSetEntry = _DocsIetfQosParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1)
)
docsIetfQosParamSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowId"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosParamSetType"),
)
if mibBuilder.loadTexts:
    docsIetfQosParamSetEntry.setStatus("current")
_DocsIetfQosParamSetServiceClassName_Type = SnmpAdminString
_DocsIetfQosParamSetServiceClassName_Object = MibTableColumn
docsIetfQosParamSetServiceClassName = _DocsIetfQosParamSetServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 1),
    _DocsIetfQosParamSetServiceClassName_Type()
)
docsIetfQosParamSetServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetServiceClassName.setStatus("current")


class _DocsIetfQosParamSetPriority_Type(Integer32):
    """Custom type docsIetfQosParamSetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsIetfQosParamSetPriority_Type.__name__ = "Integer32"
_DocsIetfQosParamSetPriority_Object = MibTableColumn
docsIetfQosParamSetPriority = _DocsIetfQosParamSetPriority_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 2),
    _DocsIetfQosParamSetPriority_Type()
)
docsIetfQosParamSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetPriority.setStatus("current")
_DocsIetfQosParamSetMaxTrafficRate_Type = DocsIetfQosBitRate
_DocsIetfQosParamSetMaxTrafficRate_Object = MibTableColumn
docsIetfQosParamSetMaxTrafficRate = _DocsIetfQosParamSetMaxTrafficRate_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 3),
    _DocsIetfQosParamSetMaxTrafficRate_Type()
)
docsIetfQosParamSetMaxTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetMaxTrafficRate.setStatus("current")
_DocsIetfQosParamSetMaxTrafficBurst_Type = Unsigned32
_DocsIetfQosParamSetMaxTrafficBurst_Object = MibTableColumn
docsIetfQosParamSetMaxTrafficBurst = _DocsIetfQosParamSetMaxTrafficBurst_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 4),
    _DocsIetfQosParamSetMaxTrafficBurst_Type()
)
docsIetfQosParamSetMaxTrafficBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetMaxTrafficBurst.setStatus("current")
_DocsIetfQosParamSetMinReservedRate_Type = DocsIetfQosBitRate
_DocsIetfQosParamSetMinReservedRate_Object = MibTableColumn
docsIetfQosParamSetMinReservedRate = _DocsIetfQosParamSetMinReservedRate_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 5),
    _DocsIetfQosParamSetMinReservedRate_Type()
)
docsIetfQosParamSetMinReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetMinReservedRate.setStatus("current")


class _DocsIetfQosParamSetMinReservedPkt_Type(Integer32):
    """Custom type docsIetfQosParamSetMinReservedPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosParamSetMinReservedPkt_Type.__name__ = "Integer32"
_DocsIetfQosParamSetMinReservedPkt_Object = MibTableColumn
docsIetfQosParamSetMinReservedPkt = _DocsIetfQosParamSetMinReservedPkt_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 6),
    _DocsIetfQosParamSetMinReservedPkt_Type()
)
docsIetfQosParamSetMinReservedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetMinReservedPkt.setStatus("current")


class _DocsIetfQosParamSetActiveTimeout_Type(Integer32):
    """Custom type docsIetfQosParamSetActiveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosParamSetActiveTimeout_Type.__name__ = "Integer32"
_DocsIetfQosParamSetActiveTimeout_Object = MibTableColumn
docsIetfQosParamSetActiveTimeout = _DocsIetfQosParamSetActiveTimeout_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 7),
    _DocsIetfQosParamSetActiveTimeout_Type()
)
docsIetfQosParamSetActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosParamSetActiveTimeout.setUnits("seconds")


class _DocsIetfQosParamSetAdmittedTimeout_Type(Integer32):
    """Custom type docsIetfQosParamSetAdmittedTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosParamSetAdmittedTimeout_Type.__name__ = "Integer32"
_DocsIetfQosParamSetAdmittedTimeout_Object = MibTableColumn
docsIetfQosParamSetAdmittedTimeout = _DocsIetfQosParamSetAdmittedTimeout_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 8),
    _DocsIetfQosParamSetAdmittedTimeout_Type()
)
docsIetfQosParamSetAdmittedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetAdmittedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosParamSetAdmittedTimeout.setUnits("seconds")


class _DocsIetfQosParamSetMaxConcatBurst_Type(Integer32):
    """Custom type docsIetfQosParamSetMaxConcatBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosParamSetMaxConcatBurst_Type.__name__ = "Integer32"
_DocsIetfQosParamSetMaxConcatBurst_Object = MibTableColumn
docsIetfQosParamSetMaxConcatBurst = _DocsIetfQosParamSetMaxConcatBurst_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 9),
    _DocsIetfQosParamSetMaxConcatBurst_Type()
)
docsIetfQosParamSetMaxConcatBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetMaxConcatBurst.setStatus("current")
_DocsIetfQosParamSetSchedulingType_Type = DocsIetfQosSchedulingType
_DocsIetfQosParamSetSchedulingType_Object = MibTableColumn
docsIetfQosParamSetSchedulingType = _DocsIetfQosParamSetSchedulingType_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 10),
    _DocsIetfQosParamSetSchedulingType_Type()
)
docsIetfQosParamSetSchedulingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetSchedulingType.setStatus("current")
_DocsIetfQosParamSetNomPollInterval_Type = Unsigned32
_DocsIetfQosParamSetNomPollInterval_Object = MibTableColumn
docsIetfQosParamSetNomPollInterval = _DocsIetfQosParamSetNomPollInterval_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 11),
    _DocsIetfQosParamSetNomPollInterval_Type()
)
docsIetfQosParamSetNomPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetNomPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosParamSetNomPollInterval.setUnits("microseconds")
_DocsIetfQosParamSetTolPollJitter_Type = Unsigned32
_DocsIetfQosParamSetTolPollJitter_Object = MibTableColumn
docsIetfQosParamSetTolPollJitter = _DocsIetfQosParamSetTolPollJitter_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 12),
    _DocsIetfQosParamSetTolPollJitter_Type()
)
docsIetfQosParamSetTolPollJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetTolPollJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosParamSetTolPollJitter.setUnits("microseconds")


class _DocsIetfQosParamSetUnsolicitGrantSize_Type(Integer32):
    """Custom type docsIetfQosParamSetUnsolicitGrantSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosParamSetUnsolicitGrantSize_Type.__name__ = "Integer32"
_DocsIetfQosParamSetUnsolicitGrantSize_Object = MibTableColumn
docsIetfQosParamSetUnsolicitGrantSize = _DocsIetfQosParamSetUnsolicitGrantSize_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 13),
    _DocsIetfQosParamSetUnsolicitGrantSize_Type()
)
docsIetfQosParamSetUnsolicitGrantSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetUnsolicitGrantSize.setStatus("current")
_DocsIetfQosParamSetNomGrantInterval_Type = Unsigned32
_DocsIetfQosParamSetNomGrantInterval_Object = MibTableColumn
docsIetfQosParamSetNomGrantInterval = _DocsIetfQosParamSetNomGrantInterval_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 14),
    _DocsIetfQosParamSetNomGrantInterval_Type()
)
docsIetfQosParamSetNomGrantInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetNomGrantInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosParamSetNomGrantInterval.setUnits("microseconds")
_DocsIetfQosParamSetTolGrantJitter_Type = Unsigned32
_DocsIetfQosParamSetTolGrantJitter_Object = MibTableColumn
docsIetfQosParamSetTolGrantJitter = _DocsIetfQosParamSetTolGrantJitter_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 15),
    _DocsIetfQosParamSetTolGrantJitter_Type()
)
docsIetfQosParamSetTolGrantJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetTolGrantJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosParamSetTolGrantJitter.setUnits("microseconds")


class _DocsIetfQosParamSetGrantsPerInterval_Type(Integer32):
    """Custom type docsIetfQosParamSetGrantsPerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DocsIetfQosParamSetGrantsPerInterval_Type.__name__ = "Integer32"
_DocsIetfQosParamSetGrantsPerInterval_Object = MibTableColumn
docsIetfQosParamSetGrantsPerInterval = _DocsIetfQosParamSetGrantsPerInterval_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 16),
    _DocsIetfQosParamSetGrantsPerInterval_Type()
)
docsIetfQosParamSetGrantsPerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetGrantsPerInterval.setStatus("current")


class _DocsIetfQosParamSetTosAndMask_Type(OctetString):
    """Custom type docsIetfQosParamSetTosAndMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsIetfQosParamSetTosAndMask_Type.__name__ = "OctetString"
_DocsIetfQosParamSetTosAndMask_Object = MibTableColumn
docsIetfQosParamSetTosAndMask = _DocsIetfQosParamSetTosAndMask_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 17),
    _DocsIetfQosParamSetTosAndMask_Type()
)
docsIetfQosParamSetTosAndMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetTosAndMask.setStatus("current")


class _DocsIetfQosParamSetTosOrMask_Type(OctetString):
    """Custom type docsIetfQosParamSetTosOrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsIetfQosParamSetTosOrMask_Type.__name__ = "OctetString"
_DocsIetfQosParamSetTosOrMask_Object = MibTableColumn
docsIetfQosParamSetTosOrMask = _DocsIetfQosParamSetTosOrMask_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 18),
    _DocsIetfQosParamSetTosOrMask_Type()
)
docsIetfQosParamSetTosOrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetTosOrMask.setStatus("current")
_DocsIetfQosParamSetMaxLatency_Type = Unsigned32
_DocsIetfQosParamSetMaxLatency_Object = MibTableColumn
docsIetfQosParamSetMaxLatency = _DocsIetfQosParamSetMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 19),
    _DocsIetfQosParamSetMaxLatency_Type()
)
docsIetfQosParamSetMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosParamSetMaxLatency.setUnits("microseconds")


class _DocsIetfQosParamSetType_Type(Integer32):
    """Custom type docsIetfQosParamSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("admitted", 2),
          ("provisioned", 3))
    )


_DocsIetfQosParamSetType_Type.__name__ = "Integer32"
_DocsIetfQosParamSetType_Object = MibTableColumn
docsIetfQosParamSetType = _DocsIetfQosParamSetType_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 20),
    _DocsIetfQosParamSetType_Type()
)
docsIetfQosParamSetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosParamSetType.setStatus("current")


class _DocsIetfQosParamSetRequestPolicyOct_Type(OctetString):
    """Custom type docsIetfQosParamSetRequestPolicyOct based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DocsIetfQosParamSetRequestPolicyOct_Type.__name__ = "OctetString"
_DocsIetfQosParamSetRequestPolicyOct_Object = MibTableColumn
docsIetfQosParamSetRequestPolicyOct = _DocsIetfQosParamSetRequestPolicyOct_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 21),
    _DocsIetfQosParamSetRequestPolicyOct_Type()
)
docsIetfQosParamSetRequestPolicyOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetRequestPolicyOct.setStatus("current")


class _DocsIetfQosParamSetBitMap_Type(Bits):
    """Custom type docsIetfQosParamSetBitMap based on Bits"""
    namedValues = NamedValues(
        *(("activeTimeout", 5),
          ("admittedTimeout", 6),
          ("grantsPerInterval", 15),
          ("maxConcatBurst", 7),
          ("maxLatency", 17),
          ("maxTrafficBurst", 2),
          ("maxTrafficRate", 1),
          ("minReservedPkt", 4),
          ("minReservedRate", 3),
          ("nomGrantInterval", 13),
          ("nomPollInterval", 10),
          ("requestPolicy", 9),
          ("schedulingType", 8),
          ("tolGrantJitter", 14),
          ("tolPollJitter", 11),
          ("tosOverwrite", 16),
          ("trafficPriority", 0),
          ("unsolicitGrantSize", 12))
    )

_DocsIetfQosParamSetBitMap_Type.__name__ = "Bits"
_DocsIetfQosParamSetBitMap_Object = MibTableColumn
docsIetfQosParamSetBitMap = _DocsIetfQosParamSetBitMap_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 2, 1, 22),
    _DocsIetfQosParamSetBitMap_Type()
)
docsIetfQosParamSetBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosParamSetBitMap.setStatus("current")
_DocsIetfQosServiceFlowTable_Object = MibTable
docsIetfQosServiceFlowTable = _DocsIetfQosServiceFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 3)
)
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowTable.setStatus("current")
_DocsIetfQosServiceFlowEntry_Object = MibTableRow
docsIetfQosServiceFlowEntry = _DocsIetfQosServiceFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 3, 1)
)
docsIetfQosServiceFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowEntry.setStatus("current")


class _DocsIetfQosServiceFlowId_Type(Unsigned32):
    """Custom type docsIetfQosServiceFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIetfQosServiceFlowId_Type.__name__ = "Unsigned32"
_DocsIetfQosServiceFlowId_Object = MibTableColumn
docsIetfQosServiceFlowId = _DocsIetfQosServiceFlowId_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 3, 1, 1),
    _DocsIetfQosServiceFlowId_Type()
)
docsIetfQosServiceFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowId.setStatus("current")


class _DocsIetfQosServiceFlowSID_Type(Unsigned32):
    """Custom type docsIetfQosServiceFlowSID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsIetfQosServiceFlowSID_Type.__name__ = "Unsigned32"
_DocsIetfQosServiceFlowSID_Object = MibTableColumn
docsIetfQosServiceFlowSID = _DocsIetfQosServiceFlowSID_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 3, 1, 2),
    _DocsIetfQosServiceFlowSID_Type()
)
docsIetfQosServiceFlowSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowSID.setStatus("current")
_DocsIetfQosServiceFlowDirection_Type = DocsIetfQosRfMacIfDirection
_DocsIetfQosServiceFlowDirection_Object = MibTableColumn
docsIetfQosServiceFlowDirection = _DocsIetfQosServiceFlowDirection_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 3, 1, 3),
    _DocsIetfQosServiceFlowDirection_Type()
)
docsIetfQosServiceFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowDirection.setStatus("current")
_DocsIetfQosServiceFlowPrimary_Type = TruthValue
_DocsIetfQosServiceFlowPrimary_Object = MibTableColumn
docsIetfQosServiceFlowPrimary = _DocsIetfQosServiceFlowPrimary_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 3, 1, 4),
    _DocsIetfQosServiceFlowPrimary_Type()
)
docsIetfQosServiceFlowPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowPrimary.setStatus("current")
_DocsIetfQosServiceFlowStatsTable_Object = MibTable
docsIetfQosServiceFlowStatsTable = _DocsIetfQosServiceFlowStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 4)
)
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowStatsTable.setStatus("current")
_DocsIetfQosServiceFlowStatsEntry_Object = MibTableRow
docsIetfQosServiceFlowStatsEntry = _DocsIetfQosServiceFlowStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 4, 1)
)
docsIetfQosServiceFlowStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowStatsEntry.setStatus("current")
_DocsIetfQosServiceFlowPkts_Type = Counter64
_DocsIetfQosServiceFlowPkts_Object = MibTableColumn
docsIetfQosServiceFlowPkts = _DocsIetfQosServiceFlowPkts_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 4, 1, 1),
    _DocsIetfQosServiceFlowPkts_Type()
)
docsIetfQosServiceFlowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowPkts.setStatus("current")
_DocsIetfQosServiceFlowOctets_Type = Counter64
_DocsIetfQosServiceFlowOctets_Object = MibTableColumn
docsIetfQosServiceFlowOctets = _DocsIetfQosServiceFlowOctets_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 4, 1, 2),
    _DocsIetfQosServiceFlowOctets_Type()
)
docsIetfQosServiceFlowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowOctets.setStatus("current")
_DocsIetfQosServiceFlowTimeCreated_Type = TimeStamp
_DocsIetfQosServiceFlowTimeCreated_Object = MibTableColumn
docsIetfQosServiceFlowTimeCreated = _DocsIetfQosServiceFlowTimeCreated_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 4, 1, 3),
    _DocsIetfQosServiceFlowTimeCreated_Type()
)
docsIetfQosServiceFlowTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowTimeCreated.setStatus("current")
_DocsIetfQosServiceFlowTimeActive_Type = Counter32
_DocsIetfQosServiceFlowTimeActive_Object = MibTableColumn
docsIetfQosServiceFlowTimeActive = _DocsIetfQosServiceFlowTimeActive_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 4, 1, 4),
    _DocsIetfQosServiceFlowTimeActive_Type()
)
docsIetfQosServiceFlowTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowTimeActive.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowTimeActive.setUnits("seconds")
_DocsIetfQosServiceFlowPHSUnknowns_Type = Counter32
_DocsIetfQosServiceFlowPHSUnknowns_Object = MibTableColumn
docsIetfQosServiceFlowPHSUnknowns = _DocsIetfQosServiceFlowPHSUnknowns_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 4, 1, 5),
    _DocsIetfQosServiceFlowPHSUnknowns_Type()
)
docsIetfQosServiceFlowPHSUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowPHSUnknowns.setStatus("current")
_DocsIetfQosServiceFlowPolicedDropPkts_Type = Counter32
_DocsIetfQosServiceFlowPolicedDropPkts_Object = MibTableColumn
docsIetfQosServiceFlowPolicedDropPkts = _DocsIetfQosServiceFlowPolicedDropPkts_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 4, 1, 6),
    _DocsIetfQosServiceFlowPolicedDropPkts_Type()
)
docsIetfQosServiceFlowPolicedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowPolicedDropPkts.setStatus("current")
_DocsIetfQosServiceFlowPolicedDelayPkts_Type = Counter32
_DocsIetfQosServiceFlowPolicedDelayPkts_Object = MibTableColumn
docsIetfQosServiceFlowPolicedDelayPkts = _DocsIetfQosServiceFlowPolicedDelayPkts_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 4, 1, 7),
    _DocsIetfQosServiceFlowPolicedDelayPkts_Type()
)
docsIetfQosServiceFlowPolicedDelayPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowPolicedDelayPkts.setStatus("current")
_DocsIetfQosUpstreamStatsTable_Object = MibTable
docsIetfQosUpstreamStatsTable = _DocsIetfQosUpstreamStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 5)
)
if mibBuilder.loadTexts:
    docsIetfQosUpstreamStatsTable.setStatus("current")
_DocsIetfQosUpstreamStatsEntry_Object = MibTableRow
docsIetfQosUpstreamStatsEntry = _DocsIetfQosUpstreamStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 5, 1)
)
docsIetfQosUpstreamStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosSID"),
)
if mibBuilder.loadTexts:
    docsIetfQosUpstreamStatsEntry.setStatus("current")


class _DocsIetfQosSID_Type(Unsigned32):
    """Custom type docsIetfQosSID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsIetfQosSID_Type.__name__ = "Unsigned32"
_DocsIetfQosSID_Object = MibTableColumn
docsIetfQosSID = _DocsIetfQosSID_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 5, 1, 1),
    _DocsIetfQosSID_Type()
)
docsIetfQosSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosSID.setStatus("current")
_DocsIetfQosUpstreamFragments_Type = Counter32
_DocsIetfQosUpstreamFragments_Object = MibTableColumn
docsIetfQosUpstreamFragments = _DocsIetfQosUpstreamFragments_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 5, 1, 2),
    _DocsIetfQosUpstreamFragments_Type()
)
docsIetfQosUpstreamFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosUpstreamFragments.setStatus("current")
_DocsIetfQosUpstreamFragDiscards_Type = Counter32
_DocsIetfQosUpstreamFragDiscards_Object = MibTableColumn
docsIetfQosUpstreamFragDiscards = _DocsIetfQosUpstreamFragDiscards_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 5, 1, 3),
    _DocsIetfQosUpstreamFragDiscards_Type()
)
docsIetfQosUpstreamFragDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosUpstreamFragDiscards.setStatus("current")
_DocsIetfQosUpstreamConcatBursts_Type = Counter32
_DocsIetfQosUpstreamConcatBursts_Object = MibTableColumn
docsIetfQosUpstreamConcatBursts = _DocsIetfQosUpstreamConcatBursts_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 5, 1, 4),
    _DocsIetfQosUpstreamConcatBursts_Type()
)
docsIetfQosUpstreamConcatBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosUpstreamConcatBursts.setStatus("current")
_DocsIetfQosDynamicServiceStatsTable_Object = MibTable
docsIetfQosDynamicServiceStatsTable = _DocsIetfQosDynamicServiceStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6)
)
if mibBuilder.loadTexts:
    docsIetfQosDynamicServiceStatsTable.setStatus("current")
_DocsIetfQosDynamicServiceStatsEntry_Object = MibTableRow
docsIetfQosDynamicServiceStatsEntry = _DocsIetfQosDynamicServiceStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1)
)
docsIetfQosDynamicServiceStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosIfDirection"),
)
if mibBuilder.loadTexts:
    docsIetfQosDynamicServiceStatsEntry.setStatus("current")
_DocsIetfQosIfDirection_Type = DocsIetfQosRfMacIfDirection
_DocsIetfQosIfDirection_Object = MibTableColumn
docsIetfQosIfDirection = _DocsIetfQosIfDirection_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 1),
    _DocsIetfQosIfDirection_Type()
)
docsIetfQosIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosIfDirection.setStatus("current")
_DocsIetfQosDSAReqs_Type = Counter32
_DocsIetfQosDSAReqs_Object = MibTableColumn
docsIetfQosDSAReqs = _DocsIetfQosDSAReqs_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 2),
    _DocsIetfQosDSAReqs_Type()
)
docsIetfQosDSAReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDSAReqs.setStatus("current")
_DocsIetfQosDSARsps_Type = Counter32
_DocsIetfQosDSARsps_Object = MibTableColumn
docsIetfQosDSARsps = _DocsIetfQosDSARsps_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 3),
    _DocsIetfQosDSARsps_Type()
)
docsIetfQosDSARsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDSARsps.setStatus("current")
_DocsIetfQosDSAAcks_Type = Counter32
_DocsIetfQosDSAAcks_Object = MibTableColumn
docsIetfQosDSAAcks = _DocsIetfQosDSAAcks_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 4),
    _DocsIetfQosDSAAcks_Type()
)
docsIetfQosDSAAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDSAAcks.setStatus("current")
_DocsIetfQosDSCReqs_Type = Counter32
_DocsIetfQosDSCReqs_Object = MibTableColumn
docsIetfQosDSCReqs = _DocsIetfQosDSCReqs_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 5),
    _DocsIetfQosDSCReqs_Type()
)
docsIetfQosDSCReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDSCReqs.setStatus("current")
_DocsIetfQosDSCRsps_Type = Counter32
_DocsIetfQosDSCRsps_Object = MibTableColumn
docsIetfQosDSCRsps = _DocsIetfQosDSCRsps_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 6),
    _DocsIetfQosDSCRsps_Type()
)
docsIetfQosDSCRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDSCRsps.setStatus("current")
_DocsIetfQosDSCAcks_Type = Counter32
_DocsIetfQosDSCAcks_Object = MibTableColumn
docsIetfQosDSCAcks = _DocsIetfQosDSCAcks_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 7),
    _DocsIetfQosDSCAcks_Type()
)
docsIetfQosDSCAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDSCAcks.setStatus("current")
_DocsIetfQosDSDReqs_Type = Counter32
_DocsIetfQosDSDReqs_Object = MibTableColumn
docsIetfQosDSDReqs = _DocsIetfQosDSDReqs_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 8),
    _DocsIetfQosDSDReqs_Type()
)
docsIetfQosDSDReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDSDReqs.setStatus("current")
_DocsIetfQosDSDRsps_Type = Counter32
_DocsIetfQosDSDRsps_Object = MibTableColumn
docsIetfQosDSDRsps = _DocsIetfQosDSDRsps_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 9),
    _DocsIetfQosDSDRsps_Type()
)
docsIetfQosDSDRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDSDRsps.setStatus("current")
_DocsIetfQosDynamicAdds_Type = Counter32
_DocsIetfQosDynamicAdds_Object = MibTableColumn
docsIetfQosDynamicAdds = _DocsIetfQosDynamicAdds_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 10),
    _DocsIetfQosDynamicAdds_Type()
)
docsIetfQosDynamicAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDynamicAdds.setStatus("current")
_DocsIetfQosDynamicAddFails_Type = Counter32
_DocsIetfQosDynamicAddFails_Object = MibTableColumn
docsIetfQosDynamicAddFails = _DocsIetfQosDynamicAddFails_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 11),
    _DocsIetfQosDynamicAddFails_Type()
)
docsIetfQosDynamicAddFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDynamicAddFails.setStatus("current")
_DocsIetfQosDynamicChanges_Type = Counter32
_DocsIetfQosDynamicChanges_Object = MibTableColumn
docsIetfQosDynamicChanges = _DocsIetfQosDynamicChanges_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 12),
    _DocsIetfQosDynamicChanges_Type()
)
docsIetfQosDynamicChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDynamicChanges.setStatus("current")
_DocsIetfQosDynamicChangeFails_Type = Counter32
_DocsIetfQosDynamicChangeFails_Object = MibTableColumn
docsIetfQosDynamicChangeFails = _DocsIetfQosDynamicChangeFails_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 13),
    _DocsIetfQosDynamicChangeFails_Type()
)
docsIetfQosDynamicChangeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDynamicChangeFails.setStatus("current")
_DocsIetfQosDynamicDeletes_Type = Counter32
_DocsIetfQosDynamicDeletes_Object = MibTableColumn
docsIetfQosDynamicDeletes = _DocsIetfQosDynamicDeletes_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 14),
    _DocsIetfQosDynamicDeletes_Type()
)
docsIetfQosDynamicDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDynamicDeletes.setStatus("current")
_DocsIetfQosDynamicDeleteFails_Type = Counter32
_DocsIetfQosDynamicDeleteFails_Object = MibTableColumn
docsIetfQosDynamicDeleteFails = _DocsIetfQosDynamicDeleteFails_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 15),
    _DocsIetfQosDynamicDeleteFails_Type()
)
docsIetfQosDynamicDeleteFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDynamicDeleteFails.setStatus("current")
_DocsIetfQosDCCReqs_Type = Counter32
_DocsIetfQosDCCReqs_Object = MibTableColumn
docsIetfQosDCCReqs = _DocsIetfQosDCCReqs_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 16),
    _DocsIetfQosDCCReqs_Type()
)
docsIetfQosDCCReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDCCReqs.setStatus("current")
_DocsIetfQosDCCRsps_Type = Counter32
_DocsIetfQosDCCRsps_Object = MibTableColumn
docsIetfQosDCCRsps = _DocsIetfQosDCCRsps_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 17),
    _DocsIetfQosDCCRsps_Type()
)
docsIetfQosDCCRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDCCRsps.setStatus("current")
_DocsIetfQosDCCAcks_Type = Counter32
_DocsIetfQosDCCAcks_Object = MibTableColumn
docsIetfQosDCCAcks = _DocsIetfQosDCCAcks_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 18),
    _DocsIetfQosDCCAcks_Type()
)
docsIetfQosDCCAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDCCAcks.setStatus("current")
_DocsIetfQosDCCs_Type = Counter32
_DocsIetfQosDCCs_Object = MibTableColumn
docsIetfQosDCCs = _DocsIetfQosDCCs_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 19),
    _DocsIetfQosDCCs_Type()
)
docsIetfQosDCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDCCs.setStatus("current")
_DocsIetfQosDCCFails_Type = Counter32
_DocsIetfQosDCCFails_Object = MibTableColumn
docsIetfQosDCCFails = _DocsIetfQosDCCFails_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 6, 1, 20),
    _DocsIetfQosDCCFails_Type()
)
docsIetfQosDCCFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosDCCFails.setStatus("current")
_DocsIetfQosServiceFlowLogTable_Object = MibTable
docsIetfQosServiceFlowLogTable = _DocsIetfQosServiceFlowLogTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7)
)
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogTable.setStatus("current")
_DocsIetfQosServiceFlowLogEntry_Object = MibTableRow
docsIetfQosServiceFlowLogEntry = _DocsIetfQosServiceFlowLogEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1)
)
docsIetfQosServiceFlowLogEntry.setIndexNames(
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogIndex"),
)
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogEntry.setStatus("current")


class _DocsIetfQosServiceFlowLogIndex_Type(Unsigned32):
    """Custom type docsIetfQosServiceFlowLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIetfQosServiceFlowLogIndex_Type.__name__ = "Unsigned32"
_DocsIetfQosServiceFlowLogIndex_Object = MibTableColumn
docsIetfQosServiceFlowLogIndex = _DocsIetfQosServiceFlowLogIndex_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 1),
    _DocsIetfQosServiceFlowLogIndex_Type()
)
docsIetfQosServiceFlowLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogIndex.setStatus("current")
_DocsIetfQosServiceFlowLogIfIndex_Type = InterfaceIndex
_DocsIetfQosServiceFlowLogIfIndex_Object = MibTableColumn
docsIetfQosServiceFlowLogIfIndex = _DocsIetfQosServiceFlowLogIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 2),
    _DocsIetfQosServiceFlowLogIfIndex_Type()
)
docsIetfQosServiceFlowLogIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogIfIndex.setStatus("current")


class _DocsIetfQosServiceFlowLogSFID_Type(Unsigned32):
    """Custom type docsIetfQosServiceFlowLogSFID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIetfQosServiceFlowLogSFID_Type.__name__ = "Unsigned32"
_DocsIetfQosServiceFlowLogSFID_Object = MibTableColumn
docsIetfQosServiceFlowLogSFID = _DocsIetfQosServiceFlowLogSFID_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 3),
    _DocsIetfQosServiceFlowLogSFID_Type()
)
docsIetfQosServiceFlowLogSFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogSFID.setStatus("current")
_DocsIetfQosServiceFlowLogCmMac_Type = MacAddress
_DocsIetfQosServiceFlowLogCmMac_Object = MibTableColumn
docsIetfQosServiceFlowLogCmMac = _DocsIetfQosServiceFlowLogCmMac_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 4),
    _DocsIetfQosServiceFlowLogCmMac_Type()
)
docsIetfQosServiceFlowLogCmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogCmMac.setStatus("current")
_DocsIetfQosServiceFlowLogPkts_Type = Counter64
_DocsIetfQosServiceFlowLogPkts_Object = MibTableColumn
docsIetfQosServiceFlowLogPkts = _DocsIetfQosServiceFlowLogPkts_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 5),
    _DocsIetfQosServiceFlowLogPkts_Type()
)
docsIetfQosServiceFlowLogPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogPkts.setStatus("current")
_DocsIetfQosServiceFlowLogOctets_Type = Counter64
_DocsIetfQosServiceFlowLogOctets_Object = MibTableColumn
docsIetfQosServiceFlowLogOctets = _DocsIetfQosServiceFlowLogOctets_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 6),
    _DocsIetfQosServiceFlowLogOctets_Type()
)
docsIetfQosServiceFlowLogOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogOctets.setStatus("current")
_DocsIetfQosServiceFlowLogTimeDeleted_Type = TimeStamp
_DocsIetfQosServiceFlowLogTimeDeleted_Object = MibTableColumn
docsIetfQosServiceFlowLogTimeDeleted = _DocsIetfQosServiceFlowLogTimeDeleted_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 7),
    _DocsIetfQosServiceFlowLogTimeDeleted_Type()
)
docsIetfQosServiceFlowLogTimeDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogTimeDeleted.setStatus("current")
_DocsIetfQosServiceFlowLogTimeCreated_Type = TimeStamp
_DocsIetfQosServiceFlowLogTimeCreated_Object = MibTableColumn
docsIetfQosServiceFlowLogTimeCreated = _DocsIetfQosServiceFlowLogTimeCreated_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 8),
    _DocsIetfQosServiceFlowLogTimeCreated_Type()
)
docsIetfQosServiceFlowLogTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogTimeCreated.setStatus("current")
_DocsIetfQosServiceFlowLogTimeActive_Type = Counter32
_DocsIetfQosServiceFlowLogTimeActive_Object = MibTableColumn
docsIetfQosServiceFlowLogTimeActive = _DocsIetfQosServiceFlowLogTimeActive_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 9),
    _DocsIetfQosServiceFlowLogTimeActive_Type()
)
docsIetfQosServiceFlowLogTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogTimeActive.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogTimeActive.setUnits("seconds")
_DocsIetfQosServiceFlowLogDirection_Type = DocsIetfQosRfMacIfDirection
_DocsIetfQosServiceFlowLogDirection_Object = MibTableColumn
docsIetfQosServiceFlowLogDirection = _DocsIetfQosServiceFlowLogDirection_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 10),
    _DocsIetfQosServiceFlowLogDirection_Type()
)
docsIetfQosServiceFlowLogDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogDirection.setStatus("current")
_DocsIetfQosServiceFlowLogPrimary_Type = TruthValue
_DocsIetfQosServiceFlowLogPrimary_Object = MibTableColumn
docsIetfQosServiceFlowLogPrimary = _DocsIetfQosServiceFlowLogPrimary_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 11),
    _DocsIetfQosServiceFlowLogPrimary_Type()
)
docsIetfQosServiceFlowLogPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogPrimary.setStatus("current")
_DocsIetfQosServiceFlowLogServiceClassName_Type = SnmpAdminString
_DocsIetfQosServiceFlowLogServiceClassName_Object = MibTableColumn
docsIetfQosServiceFlowLogServiceClassName = _DocsIetfQosServiceFlowLogServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 12),
    _DocsIetfQosServiceFlowLogServiceClassName_Type()
)
docsIetfQosServiceFlowLogServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogServiceClassName.setStatus("current")
_DocsIetfQosServiceFlowLogPolicedDropPkts_Type = Counter32
_DocsIetfQosServiceFlowLogPolicedDropPkts_Object = MibTableColumn
docsIetfQosServiceFlowLogPolicedDropPkts = _DocsIetfQosServiceFlowLogPolicedDropPkts_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 13),
    _DocsIetfQosServiceFlowLogPolicedDropPkts_Type()
)
docsIetfQosServiceFlowLogPolicedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogPolicedDropPkts.setStatus("current")
_DocsIetfQosServiceFlowLogPolicedDelayPkts_Type = Counter32
_DocsIetfQosServiceFlowLogPolicedDelayPkts_Object = MibTableColumn
docsIetfQosServiceFlowLogPolicedDelayPkts = _DocsIetfQosServiceFlowLogPolicedDelayPkts_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 14),
    _DocsIetfQosServiceFlowLogPolicedDelayPkts_Type()
)
docsIetfQosServiceFlowLogPolicedDelayPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogPolicedDelayPkts.setStatus("current")


class _DocsIetfQosServiceFlowLogControl_Type(Integer32):
    """Custom type docsIetfQosServiceFlowLogControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_DocsIetfQosServiceFlowLogControl_Type.__name__ = "Integer32"
_DocsIetfQosServiceFlowLogControl_Object = MibTableColumn
docsIetfQosServiceFlowLogControl = _DocsIetfQosServiceFlowLogControl_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 7, 1, 15),
    _DocsIetfQosServiceFlowLogControl_Type()
)
docsIetfQosServiceFlowLogControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIetfQosServiceFlowLogControl.setStatus("current")
_DocsIetfQosServiceClassTable_Object = MibTable
docsIetfQosServiceClassTable = _DocsIetfQosServiceClassTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8)
)
if mibBuilder.loadTexts:
    docsIetfQosServiceClassTable.setStatus("current")
_DocsIetfQosServiceClassEntry_Object = MibTableRow
docsIetfQosServiceClassEntry = _DocsIetfQosServiceClassEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1)
)
docsIetfQosServiceClassEntry.setIndexNames(
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassName"),
)
if mibBuilder.loadTexts:
    docsIetfQosServiceClassEntry.setStatus("current")


class _DocsIetfQosServiceClassName_Type(SnmpAdminString):
    """Custom type docsIetfQosServiceClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DocsIetfQosServiceClassName_Type.__name__ = "SnmpAdminString"
_DocsIetfQosServiceClassName_Object = MibTableColumn
docsIetfQosServiceClassName = _DocsIetfQosServiceClassName_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 1),
    _DocsIetfQosServiceClassName_Type()
)
docsIetfQosServiceClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassName.setStatus("current")
_DocsIetfQosServiceClassStatus_Type = RowStatus
_DocsIetfQosServiceClassStatus_Object = MibTableColumn
docsIetfQosServiceClassStatus = _DocsIetfQosServiceClassStatus_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 2),
    _DocsIetfQosServiceClassStatus_Type()
)
docsIetfQosServiceClassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassStatus.setStatus("current")


class _DocsIetfQosServiceClassPriority_Type(Integer32):
    """Custom type docsIetfQosServiceClassPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsIetfQosServiceClassPriority_Type.__name__ = "Integer32"
_DocsIetfQosServiceClassPriority_Object = MibTableColumn
docsIetfQosServiceClassPriority = _DocsIetfQosServiceClassPriority_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 3),
    _DocsIetfQosServiceClassPriority_Type()
)
docsIetfQosServiceClassPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassPriority.setStatus("current")


class _DocsIetfQosServiceClassMaxTrafficRate_Type(DocsIetfQosBitRate):
    """Custom type docsIetfQosServiceClassMaxTrafficRate based on DocsIetfQosBitRate"""
    defaultValue = 0


_DocsIetfQosServiceClassMaxTrafficRate_Object = MibTableColumn
docsIetfQosServiceClassMaxTrafficRate = _DocsIetfQosServiceClassMaxTrafficRate_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 4),
    _DocsIetfQosServiceClassMaxTrafficRate_Type()
)
docsIetfQosServiceClassMaxTrafficRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassMaxTrafficRate.setStatus("current")


class _DocsIetfQosServiceClassMaxTrafficBurst_Type(Unsigned32):
    """Custom type docsIetfQosServiceClassMaxTrafficBurst based on Unsigned32"""
    defaultValue = 3044


_DocsIetfQosServiceClassMaxTrafficBurst_Object = MibTableColumn
docsIetfQosServiceClassMaxTrafficBurst = _DocsIetfQosServiceClassMaxTrafficBurst_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 5),
    _DocsIetfQosServiceClassMaxTrafficBurst_Type()
)
docsIetfQosServiceClassMaxTrafficBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassMaxTrafficBurst.setStatus("current")


class _DocsIetfQosServiceClassMinReservedRate_Type(DocsIetfQosBitRate):
    """Custom type docsIetfQosServiceClassMinReservedRate based on DocsIetfQosBitRate"""
    defaultValue = 0


_DocsIetfQosServiceClassMinReservedRate_Object = MibTableColumn
docsIetfQosServiceClassMinReservedRate = _DocsIetfQosServiceClassMinReservedRate_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 6),
    _DocsIetfQosServiceClassMinReservedRate_Type()
)
docsIetfQosServiceClassMinReservedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassMinReservedRate.setStatus("current")


class _DocsIetfQosServiceClassMinReservedPkt_Type(Integer32):
    """Custom type docsIetfQosServiceClassMinReservedPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosServiceClassMinReservedPkt_Type.__name__ = "Integer32"
_DocsIetfQosServiceClassMinReservedPkt_Object = MibTableColumn
docsIetfQosServiceClassMinReservedPkt = _DocsIetfQosServiceClassMinReservedPkt_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 7),
    _DocsIetfQosServiceClassMinReservedPkt_Type()
)
docsIetfQosServiceClassMinReservedPkt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassMinReservedPkt.setStatus("current")


class _DocsIetfQosServiceClassMaxConcatBurst_Type(Integer32):
    """Custom type docsIetfQosServiceClassMaxConcatBurst based on Integer32"""
    defaultValue = 1522

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosServiceClassMaxConcatBurst_Type.__name__ = "Integer32"
_DocsIetfQosServiceClassMaxConcatBurst_Object = MibTableColumn
docsIetfQosServiceClassMaxConcatBurst = _DocsIetfQosServiceClassMaxConcatBurst_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 8),
    _DocsIetfQosServiceClassMaxConcatBurst_Type()
)
docsIetfQosServiceClassMaxConcatBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassMaxConcatBurst.setStatus("current")


class _DocsIetfQosServiceClassNomPollInterval_Type(Unsigned32):
    """Custom type docsIetfQosServiceClassNomPollInterval based on Unsigned32"""
    defaultValue = 0


_DocsIetfQosServiceClassNomPollInterval_Object = MibTableColumn
docsIetfQosServiceClassNomPollInterval = _DocsIetfQosServiceClassNomPollInterval_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 9),
    _DocsIetfQosServiceClassNomPollInterval_Type()
)
docsIetfQosServiceClassNomPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassNomPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassNomPollInterval.setUnits("microseconds")


class _DocsIetfQosServiceClassTolPollJitter_Type(Unsigned32):
    """Custom type docsIetfQosServiceClassTolPollJitter based on Unsigned32"""
    defaultValue = 0


_DocsIetfQosServiceClassTolPollJitter_Object = MibTableColumn
docsIetfQosServiceClassTolPollJitter = _DocsIetfQosServiceClassTolPollJitter_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 10),
    _DocsIetfQosServiceClassTolPollJitter_Type()
)
docsIetfQosServiceClassTolPollJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassTolPollJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassTolPollJitter.setUnits("microseconds")


class _DocsIetfQosServiceClassUnsolicitGrantSize_Type(Integer32):
    """Custom type docsIetfQosServiceClassUnsolicitGrantSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosServiceClassUnsolicitGrantSize_Type.__name__ = "Integer32"
_DocsIetfQosServiceClassUnsolicitGrantSize_Object = MibTableColumn
docsIetfQosServiceClassUnsolicitGrantSize = _DocsIetfQosServiceClassUnsolicitGrantSize_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 11),
    _DocsIetfQosServiceClassUnsolicitGrantSize_Type()
)
docsIetfQosServiceClassUnsolicitGrantSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassUnsolicitGrantSize.setStatus("current")


class _DocsIetfQosServiceClassNomGrantInterval_Type(Unsigned32):
    """Custom type docsIetfQosServiceClassNomGrantInterval based on Unsigned32"""
    defaultValue = 0


_DocsIetfQosServiceClassNomGrantInterval_Object = MibTableColumn
docsIetfQosServiceClassNomGrantInterval = _DocsIetfQosServiceClassNomGrantInterval_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 12),
    _DocsIetfQosServiceClassNomGrantInterval_Type()
)
docsIetfQosServiceClassNomGrantInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassNomGrantInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassNomGrantInterval.setUnits("microseconds")


class _DocsIetfQosServiceClassTolGrantJitter_Type(Unsigned32):
    """Custom type docsIetfQosServiceClassTolGrantJitter based on Unsigned32"""
    defaultValue = 0


_DocsIetfQosServiceClassTolGrantJitter_Object = MibTableColumn
docsIetfQosServiceClassTolGrantJitter = _DocsIetfQosServiceClassTolGrantJitter_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 13),
    _DocsIetfQosServiceClassTolGrantJitter_Type()
)
docsIetfQosServiceClassTolGrantJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassTolGrantJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassTolGrantJitter.setUnits("microseconds")


class _DocsIetfQosServiceClassGrantsPerInterval_Type(Integer32):
    """Custom type docsIetfQosServiceClassGrantsPerInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DocsIetfQosServiceClassGrantsPerInterval_Type.__name__ = "Integer32"
_DocsIetfQosServiceClassGrantsPerInterval_Object = MibTableColumn
docsIetfQosServiceClassGrantsPerInterval = _DocsIetfQosServiceClassGrantsPerInterval_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 14),
    _DocsIetfQosServiceClassGrantsPerInterval_Type()
)
docsIetfQosServiceClassGrantsPerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassGrantsPerInterval.setStatus("current")


class _DocsIetfQosServiceClassMaxLatency_Type(Unsigned32):
    """Custom type docsIetfQosServiceClassMaxLatency based on Unsigned32"""
    defaultValue = 0


_DocsIetfQosServiceClassMaxLatency_Object = MibTableColumn
docsIetfQosServiceClassMaxLatency = _DocsIetfQosServiceClassMaxLatency_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 15),
    _DocsIetfQosServiceClassMaxLatency_Type()
)
docsIetfQosServiceClassMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassMaxLatency.setUnits("microseconds")


class _DocsIetfQosServiceClassActiveTimeout_Type(Integer32):
    """Custom type docsIetfQosServiceClassActiveTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosServiceClassActiveTimeout_Type.__name__ = "Integer32"
_DocsIetfQosServiceClassActiveTimeout_Object = MibTableColumn
docsIetfQosServiceClassActiveTimeout = _DocsIetfQosServiceClassActiveTimeout_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 16),
    _DocsIetfQosServiceClassActiveTimeout_Type()
)
docsIetfQosServiceClassActiveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassActiveTimeout.setUnits("seconds")


class _DocsIetfQosServiceClassAdmittedTimeout_Type(Integer32):
    """Custom type docsIetfQosServiceClassAdmittedTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsIetfQosServiceClassAdmittedTimeout_Type.__name__ = "Integer32"
_DocsIetfQosServiceClassAdmittedTimeout_Object = MibTableColumn
docsIetfQosServiceClassAdmittedTimeout = _DocsIetfQosServiceClassAdmittedTimeout_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 17),
    _DocsIetfQosServiceClassAdmittedTimeout_Type()
)
docsIetfQosServiceClassAdmittedTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassAdmittedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassAdmittedTimeout.setUnits("seconds")


class _DocsIetfQosServiceClassSchedulingType_Type(DocsIetfQosSchedulingType):
    """Custom type docsIetfQosServiceClassSchedulingType based on DocsIetfQosSchedulingType"""


_DocsIetfQosServiceClassSchedulingType_Object = MibTableColumn
docsIetfQosServiceClassSchedulingType = _DocsIetfQosServiceClassSchedulingType_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 18),
    _DocsIetfQosServiceClassSchedulingType_Type()
)
docsIetfQosServiceClassSchedulingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassSchedulingType.setStatus("current")


class _DocsIetfQosServiceClassRequestPolicy_Type(OctetString):
    """Custom type docsIetfQosServiceClassRequestPolicy based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DocsIetfQosServiceClassRequestPolicy_Type.__name__ = "OctetString"
_DocsIetfQosServiceClassRequestPolicy_Object = MibTableColumn
docsIetfQosServiceClassRequestPolicy = _DocsIetfQosServiceClassRequestPolicy_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 19),
    _DocsIetfQosServiceClassRequestPolicy_Type()
)
docsIetfQosServiceClassRequestPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassRequestPolicy.setStatus("current")


class _DocsIetfQosServiceClassTosAndMask_Type(OctetString):
    """Custom type docsIetfQosServiceClassTosAndMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsIetfQosServiceClassTosAndMask_Type.__name__ = "OctetString"
_DocsIetfQosServiceClassTosAndMask_Object = MibTableColumn
docsIetfQosServiceClassTosAndMask = _DocsIetfQosServiceClassTosAndMask_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 20),
    _DocsIetfQosServiceClassTosAndMask_Type()
)
docsIetfQosServiceClassTosAndMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassTosAndMask.setStatus("current")


class _DocsIetfQosServiceClassTosOrMask_Type(OctetString):
    """Custom type docsIetfQosServiceClassTosOrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsIetfQosServiceClassTosOrMask_Type.__name__ = "OctetString"
_DocsIetfQosServiceClassTosOrMask_Object = MibTableColumn
docsIetfQosServiceClassTosOrMask = _DocsIetfQosServiceClassTosOrMask_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 21),
    _DocsIetfQosServiceClassTosOrMask_Type()
)
docsIetfQosServiceClassTosOrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassTosOrMask.setStatus("current")


class _DocsIetfQosServiceClassDirection_Type(DocsIetfQosRfMacIfDirection):
    """Custom type docsIetfQosServiceClassDirection based on DocsIetfQosRfMacIfDirection"""


_DocsIetfQosServiceClassDirection_Object = MibTableColumn
docsIetfQosServiceClassDirection = _DocsIetfQosServiceClassDirection_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 22),
    _DocsIetfQosServiceClassDirection_Type()
)
docsIetfQosServiceClassDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassDirection.setStatus("current")


class _DocsIetfQosServiceClassStorageType_Type(StorageType):
    """Custom type docsIetfQosServiceClassStorageType based on StorageType"""


_DocsIetfQosServiceClassStorageType_Object = MibTableColumn
docsIetfQosServiceClassStorageType = _DocsIetfQosServiceClassStorageType_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 23),
    _DocsIetfQosServiceClassStorageType_Type()
)
docsIetfQosServiceClassStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassStorageType.setStatus("current")


class _DocsIetfQosServiceClassDSCPOverwrite_Type(DscpOrAny):
    """Custom type docsIetfQosServiceClassDSCPOverwrite based on DscpOrAny"""
    defaultValue = -1


_DocsIetfQosServiceClassDSCPOverwrite_Object = MibTableColumn
docsIetfQosServiceClassDSCPOverwrite = _DocsIetfQosServiceClassDSCPOverwrite_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 8, 1, 24),
    _DocsIetfQosServiceClassDSCPOverwrite_Type()
)
docsIetfQosServiceClassDSCPOverwrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassDSCPOverwrite.setStatus("current")
_DocsIetfQosServiceClassPolicyTable_Object = MibTable
docsIetfQosServiceClassPolicyTable = _DocsIetfQosServiceClassPolicyTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 9)
)
if mibBuilder.loadTexts:
    docsIetfQosServiceClassPolicyTable.setStatus("current")
_DocsIetfQosServiceClassPolicyEntry_Object = MibTableRow
docsIetfQosServiceClassPolicyEntry = _DocsIetfQosServiceClassPolicyEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 9, 1)
)
docsIetfQosServiceClassPolicyEntry.setIndexNames(
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassPolicyIndex"),
)
if mibBuilder.loadTexts:
    docsIetfQosServiceClassPolicyEntry.setStatus("current")


class _DocsIetfQosServiceClassPolicyIndex_Type(Unsigned32):
    """Custom type docsIetfQosServiceClassPolicyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsIetfQosServiceClassPolicyIndex_Type.__name__ = "Unsigned32"
_DocsIetfQosServiceClassPolicyIndex_Object = MibTableColumn
docsIetfQosServiceClassPolicyIndex = _DocsIetfQosServiceClassPolicyIndex_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 9, 1, 1),
    _DocsIetfQosServiceClassPolicyIndex_Type()
)
docsIetfQosServiceClassPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassPolicyIndex.setStatus("current")
_DocsIetfQosServiceClassPolicyName_Type = SnmpAdminString
_DocsIetfQosServiceClassPolicyName_Object = MibTableColumn
docsIetfQosServiceClassPolicyName = _DocsIetfQosServiceClassPolicyName_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 9, 1, 2),
    _DocsIetfQosServiceClassPolicyName_Type()
)
docsIetfQosServiceClassPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassPolicyName.setStatus("current")


class _DocsIetfQosServiceClassPolicyRulePriority_Type(Integer32):
    """Custom type docsIetfQosServiceClassPolicyRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIetfQosServiceClassPolicyRulePriority_Type.__name__ = "Integer32"
_DocsIetfQosServiceClassPolicyRulePriority_Object = MibTableColumn
docsIetfQosServiceClassPolicyRulePriority = _DocsIetfQosServiceClassPolicyRulePriority_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 9, 1, 3),
    _DocsIetfQosServiceClassPolicyRulePriority_Type()
)
docsIetfQosServiceClassPolicyRulePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassPolicyRulePriority.setStatus("current")
_DocsIetfQosServiceClassPolicyStatus_Type = RowStatus
_DocsIetfQosServiceClassPolicyStatus_Object = MibTableColumn
docsIetfQosServiceClassPolicyStatus = _DocsIetfQosServiceClassPolicyStatus_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 9, 1, 4),
    _DocsIetfQosServiceClassPolicyStatus_Type()
)
docsIetfQosServiceClassPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassPolicyStatus.setStatus("current")


class _DocsIetfQosServiceClassPolicyStorageType_Type(StorageType):
    """Custom type docsIetfQosServiceClassPolicyStorageType based on StorageType"""


_DocsIetfQosServiceClassPolicyStorageType_Object = MibTableColumn
docsIetfQosServiceClassPolicyStorageType = _DocsIetfQosServiceClassPolicyStorageType_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 9, 1, 5),
    _DocsIetfQosServiceClassPolicyStorageType_Type()
)
docsIetfQosServiceClassPolicyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsIetfQosServiceClassPolicyStorageType.setStatus("current")
_DocsIetfQosPHSTable_Object = MibTable
docsIetfQosPHSTable = _DocsIetfQosPHSTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 10)
)
if mibBuilder.loadTexts:
    docsIetfQosPHSTable.setStatus("current")
_DocsIetfQosPHSEntry_Object = MibTableRow
docsIetfQosPHSEntry = _DocsIetfQosPHSEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 10, 1)
)
docsIetfQosPHSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowId"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosPktClassId"),
)
if mibBuilder.loadTexts:
    docsIetfQosPHSEntry.setStatus("current")


class _DocsIetfQosPHSField_Type(OctetString):
    """Custom type docsIetfQosPHSField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DocsIetfQosPHSField_Type.__name__ = "OctetString"
_DocsIetfQosPHSField_Object = MibTableColumn
docsIetfQosPHSField = _DocsIetfQosPHSField_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 10, 1, 1),
    _DocsIetfQosPHSField_Type()
)
docsIetfQosPHSField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPHSField.setStatus("current")


class _DocsIetfQosPHSMask_Type(OctetString):
    """Custom type docsIetfQosPHSMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsIetfQosPHSMask_Type.__name__ = "OctetString"
_DocsIetfQosPHSMask_Object = MibTableColumn
docsIetfQosPHSMask = _DocsIetfQosPHSMask_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 10, 1, 2),
    _DocsIetfQosPHSMask_Type()
)
docsIetfQosPHSMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPHSMask.setStatus("current")


class _DocsIetfQosPHSSize_Type(Integer32):
    """Custom type docsIetfQosPHSSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsIetfQosPHSSize_Type.__name__ = "Integer32"
_DocsIetfQosPHSSize_Object = MibTableColumn
docsIetfQosPHSSize = _DocsIetfQosPHSSize_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 10, 1, 3),
    _DocsIetfQosPHSSize_Type()
)
docsIetfQosPHSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPHSSize.setStatus("current")
_DocsIetfQosPHSVerify_Type = TruthValue
_DocsIetfQosPHSVerify_Object = MibTableColumn
docsIetfQosPHSVerify = _DocsIetfQosPHSVerify_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 10, 1, 4),
    _DocsIetfQosPHSVerify_Type()
)
docsIetfQosPHSVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPHSVerify.setStatus("current")


class _DocsIetfQosPHSIndex_Type(Integer32):
    """Custom type docsIetfQosPHSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsIetfQosPHSIndex_Type.__name__ = "Integer32"
_DocsIetfQosPHSIndex_Object = MibTableColumn
docsIetfQosPHSIndex = _DocsIetfQosPHSIndex_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 10, 1, 5),
    _DocsIetfQosPHSIndex_Type()
)
docsIetfQosPHSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosPHSIndex.setStatus("current")
_DocsIetfQosCmtsMacToSrvFlowTable_Object = MibTable
docsIetfQosCmtsMacToSrvFlowTable = _DocsIetfQosCmtsMacToSrvFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 11)
)
if mibBuilder.loadTexts:
    docsIetfQosCmtsMacToSrvFlowTable.setStatus("current")
_DocsIetfQosCmtsMacToSrvFlowEntry_Object = MibTableRow
docsIetfQosCmtsMacToSrvFlowEntry = _DocsIetfQosCmtsMacToSrvFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 11, 1)
)
docsIetfQosCmtsMacToSrvFlowEntry.setIndexNames(
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosCmtsCmMac"),
    (0, "DOCS-IETF-QOS-MIB", "docsIetfQosCmtsServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsIetfQosCmtsMacToSrvFlowEntry.setStatus("current")
_DocsIetfQosCmtsCmMac_Type = MacAddress
_DocsIetfQosCmtsCmMac_Object = MibTableColumn
docsIetfQosCmtsCmMac = _DocsIetfQosCmtsCmMac_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 11, 1, 1),
    _DocsIetfQosCmtsCmMac_Type()
)
docsIetfQosCmtsCmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosCmtsCmMac.setStatus("current")


class _DocsIetfQosCmtsServiceFlowId_Type(Unsigned32):
    """Custom type docsIetfQosCmtsServiceFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsIetfQosCmtsServiceFlowId_Type.__name__ = "Unsigned32"
_DocsIetfQosCmtsServiceFlowId_Object = MibTableColumn
docsIetfQosCmtsServiceFlowId = _DocsIetfQosCmtsServiceFlowId_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 11, 1, 2),
    _DocsIetfQosCmtsServiceFlowId_Type()
)
docsIetfQosCmtsServiceFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsIetfQosCmtsServiceFlowId.setStatus("current")
_DocsIetfQosCmtsIfIndex_Type = InterfaceIndex
_DocsIetfQosCmtsIfIndex_Object = MibTableColumn
docsIetfQosCmtsIfIndex = _DocsIetfQosCmtsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 127, 1, 11, 1, 3),
    _DocsIetfQosCmtsIfIndex_Type()
)
docsIetfQosCmtsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIetfQosCmtsIfIndex.setStatus("current")
_DocsIetfQosConformance_ObjectIdentity = ObjectIdentity
docsIetfQosConformance = _DocsIetfQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 127, 2)
)
_DocsIetfQosGroups_ObjectIdentity = ObjectIdentity
docsIetfQosGroups = _DocsIetfQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 127, 2, 1)
)
_DocsIetfQosCompliances_ObjectIdentity = ObjectIdentity
docsIetfQosCompliances = _DocsIetfQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 127, 2, 2)
)

# Managed Objects groups

docsIetfQosBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 127, 2, 1, 1)
)
docsIetfQosBaseGroup.setObjects(
      *(("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassDirection"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassPriority"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassIpTosLow"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassIpTosHigh"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassIpTosMask"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassIpProtocol"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassSourcePortStart"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassSourcePortEnd"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassDestPortStart"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassDestPortEnd"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassDestMacAddr"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassDestMacMask"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassSourceMacAddr"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassEnetProtocolType"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassEnetProtocol"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassUserPriLow"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassUserPriHigh"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassVlanId"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassStateActive"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassPkts"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassBitMap"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassInetAddressType"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassInetSourceAddr"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassInetSourceMask"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassInetDestAddr"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPktClassInetDestMask"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowSID"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowDirection"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowPrimary"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowPkts"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowOctets"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowTimeCreated"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowTimeActive"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowPHSUnknowns"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowPolicedDropPkts"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowPolicedDelayPkts"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDSAReqs"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDSARsps"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDSAAcks"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDSCReqs"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDSCRsps"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDSCAcks"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDSDReqs"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDSDRsps"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDynamicAdds"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDynamicAddFails"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDynamicChanges"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDynamicChangeFails"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDynamicDeletes"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDynamicDeleteFails"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDCCReqs"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDCCRsps"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDCCAcks"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDCCs"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosDCCFails"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPHSField"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPHSMask"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPHSSize"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPHSVerify"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosPHSIndex"))
)
if mibBuilder.loadTexts:
    docsIetfQosBaseGroup.setStatus("current")

docsIetfQosParamSetGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 127, 2, 1, 2)
)
docsIetfQosParamSetGroup.setObjects(
      *(("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetServiceClassName"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetPriority"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetMaxTrafficRate"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetMaxTrafficBurst"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetMinReservedRate"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetMinReservedPkt"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetActiveTimeout"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetAdmittedTimeout"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetMaxConcatBurst"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetSchedulingType"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetNomPollInterval"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetTolPollJitter"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetUnsolicitGrantSize"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetNomGrantInterval"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetTolGrantJitter"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetGrantsPerInterval"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetTosAndMask"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetTosOrMask"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetMaxLatency"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetRequestPolicyOct"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosParamSetBitMap"))
)
if mibBuilder.loadTexts:
    docsIetfQosParamSetGroup.setStatus("current")

docsIetfQosCmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 127, 2, 1, 3)
)
docsIetfQosCmtsGroup.setObjects(
      *(("DOCS-IETF-QOS-MIB", "docsIetfQosUpstreamFragments"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosUpstreamFragDiscards"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosUpstreamConcatBursts"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogIfIndex"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogSFID"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogCmMac"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogPkts"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogOctets"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogTimeDeleted"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogTimeCreated"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogTimeActive"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogDirection"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogPrimary"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogServiceClassName"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogPolicedDropPkts"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogPolicedDelayPkts"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceFlowLogControl"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosCmtsIfIndex"))
)
if mibBuilder.loadTexts:
    docsIetfQosCmtsGroup.setStatus("current")

docsIetfQosSrvClassPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 127, 2, 1, 4)
)
docsIetfQosSrvClassPolicyGroup.setObjects(
      *(("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassPolicyName"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassPolicyRulePriority"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassPolicyStatus"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassPolicyStorageType"))
)
if mibBuilder.loadTexts:
    docsIetfQosSrvClassPolicyGroup.setStatus("current")

docsIetfQosServiceClassGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 127, 2, 1, 5)
)
docsIetfQosServiceClassGroup.setObjects(
      *(("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassStatus"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassPriority"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassMaxTrafficRate"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassMaxTrafficBurst"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassMinReservedRate"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassMinReservedPkt"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassMaxConcatBurst"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassNomPollInterval"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassTolPollJitter"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassUnsolicitGrantSize"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassNomGrantInterval"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassTolGrantJitter"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassGrantsPerInterval"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassMaxLatency"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassActiveTimeout"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassAdmittedTimeout"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassSchedulingType"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassRequestPolicy"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassTosAndMask"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassTosOrMask"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassDirection"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassStorageType"),
        ("DOCS-IETF-QOS-MIB", "docsIetfQosServiceClassDSCPOverwrite"))
)
if mibBuilder.loadTexts:
    docsIetfQosServiceClassGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsIetfQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 127, 2, 2, 1)
)
if mibBuilder.loadTexts:
    docsIetfQosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-IETF-QOS-MIB",
    **{"DocsIetfQosRfMacIfDirection": DocsIetfQosRfMacIfDirection,
       "DocsIetfQosBitRate": DocsIetfQosBitRate,
       "DocsIetfQosSchedulingType": DocsIetfQosSchedulingType,
       "docsIetfQosMIB": docsIetfQosMIB,
       "docsIetfQosNotifications": docsIetfQosNotifications,
       "docsIetfQosMIBObjects": docsIetfQosMIBObjects,
       "docsIetfQosPktClassTable": docsIetfQosPktClassTable,
       "docsIetfQosPktClassEntry": docsIetfQosPktClassEntry,
       "docsIetfQosPktClassId": docsIetfQosPktClassId,
       "docsIetfQosPktClassDirection": docsIetfQosPktClassDirection,
       "docsIetfQosPktClassPriority": docsIetfQosPktClassPriority,
       "docsIetfQosPktClassIpTosLow": docsIetfQosPktClassIpTosLow,
       "docsIetfQosPktClassIpTosHigh": docsIetfQosPktClassIpTosHigh,
       "docsIetfQosPktClassIpTosMask": docsIetfQosPktClassIpTosMask,
       "docsIetfQosPktClassIpProtocol": docsIetfQosPktClassIpProtocol,
       "docsIetfQosPktClassInetAddressType": docsIetfQosPktClassInetAddressType,
       "docsIetfQosPktClassInetSourceAddr": docsIetfQosPktClassInetSourceAddr,
       "docsIetfQosPktClassInetSourceMask": docsIetfQosPktClassInetSourceMask,
       "docsIetfQosPktClassInetDestAddr": docsIetfQosPktClassInetDestAddr,
       "docsIetfQosPktClassInetDestMask": docsIetfQosPktClassInetDestMask,
       "docsIetfQosPktClassSourcePortStart": docsIetfQosPktClassSourcePortStart,
       "docsIetfQosPktClassSourcePortEnd": docsIetfQosPktClassSourcePortEnd,
       "docsIetfQosPktClassDestPortStart": docsIetfQosPktClassDestPortStart,
       "docsIetfQosPktClassDestPortEnd": docsIetfQosPktClassDestPortEnd,
       "docsIetfQosPktClassDestMacAddr": docsIetfQosPktClassDestMacAddr,
       "docsIetfQosPktClassDestMacMask": docsIetfQosPktClassDestMacMask,
       "docsIetfQosPktClassSourceMacAddr": docsIetfQosPktClassSourceMacAddr,
       "docsIetfQosPktClassEnetProtocolType": docsIetfQosPktClassEnetProtocolType,
       "docsIetfQosPktClassEnetProtocol": docsIetfQosPktClassEnetProtocol,
       "docsIetfQosPktClassUserPriLow": docsIetfQosPktClassUserPriLow,
       "docsIetfQosPktClassUserPriHigh": docsIetfQosPktClassUserPriHigh,
       "docsIetfQosPktClassVlanId": docsIetfQosPktClassVlanId,
       "docsIetfQosPktClassStateActive": docsIetfQosPktClassStateActive,
       "docsIetfQosPktClassPkts": docsIetfQosPktClassPkts,
       "docsIetfQosPktClassBitMap": docsIetfQosPktClassBitMap,
       "docsIetfQosParamSetTable": docsIetfQosParamSetTable,
       "docsIetfQosParamSetEntry": docsIetfQosParamSetEntry,
       "docsIetfQosParamSetServiceClassName": docsIetfQosParamSetServiceClassName,
       "docsIetfQosParamSetPriority": docsIetfQosParamSetPriority,
       "docsIetfQosParamSetMaxTrafficRate": docsIetfQosParamSetMaxTrafficRate,
       "docsIetfQosParamSetMaxTrafficBurst": docsIetfQosParamSetMaxTrafficBurst,
       "docsIetfQosParamSetMinReservedRate": docsIetfQosParamSetMinReservedRate,
       "docsIetfQosParamSetMinReservedPkt": docsIetfQosParamSetMinReservedPkt,
       "docsIetfQosParamSetActiveTimeout": docsIetfQosParamSetActiveTimeout,
       "docsIetfQosParamSetAdmittedTimeout": docsIetfQosParamSetAdmittedTimeout,
       "docsIetfQosParamSetMaxConcatBurst": docsIetfQosParamSetMaxConcatBurst,
       "docsIetfQosParamSetSchedulingType": docsIetfQosParamSetSchedulingType,
       "docsIetfQosParamSetNomPollInterval": docsIetfQosParamSetNomPollInterval,
       "docsIetfQosParamSetTolPollJitter": docsIetfQosParamSetTolPollJitter,
       "docsIetfQosParamSetUnsolicitGrantSize": docsIetfQosParamSetUnsolicitGrantSize,
       "docsIetfQosParamSetNomGrantInterval": docsIetfQosParamSetNomGrantInterval,
       "docsIetfQosParamSetTolGrantJitter": docsIetfQosParamSetTolGrantJitter,
       "docsIetfQosParamSetGrantsPerInterval": docsIetfQosParamSetGrantsPerInterval,
       "docsIetfQosParamSetTosAndMask": docsIetfQosParamSetTosAndMask,
       "docsIetfQosParamSetTosOrMask": docsIetfQosParamSetTosOrMask,
       "docsIetfQosParamSetMaxLatency": docsIetfQosParamSetMaxLatency,
       "docsIetfQosParamSetType": docsIetfQosParamSetType,
       "docsIetfQosParamSetRequestPolicyOct": docsIetfQosParamSetRequestPolicyOct,
       "docsIetfQosParamSetBitMap": docsIetfQosParamSetBitMap,
       "docsIetfQosServiceFlowTable": docsIetfQosServiceFlowTable,
       "docsIetfQosServiceFlowEntry": docsIetfQosServiceFlowEntry,
       "docsIetfQosServiceFlowId": docsIetfQosServiceFlowId,
       "docsIetfQosServiceFlowSID": docsIetfQosServiceFlowSID,
       "docsIetfQosServiceFlowDirection": docsIetfQosServiceFlowDirection,
       "docsIetfQosServiceFlowPrimary": docsIetfQosServiceFlowPrimary,
       "docsIetfQosServiceFlowStatsTable": docsIetfQosServiceFlowStatsTable,
       "docsIetfQosServiceFlowStatsEntry": docsIetfQosServiceFlowStatsEntry,
       "docsIetfQosServiceFlowPkts": docsIetfQosServiceFlowPkts,
       "docsIetfQosServiceFlowOctets": docsIetfQosServiceFlowOctets,
       "docsIetfQosServiceFlowTimeCreated": docsIetfQosServiceFlowTimeCreated,
       "docsIetfQosServiceFlowTimeActive": docsIetfQosServiceFlowTimeActive,
       "docsIetfQosServiceFlowPHSUnknowns": docsIetfQosServiceFlowPHSUnknowns,
       "docsIetfQosServiceFlowPolicedDropPkts": docsIetfQosServiceFlowPolicedDropPkts,
       "docsIetfQosServiceFlowPolicedDelayPkts": docsIetfQosServiceFlowPolicedDelayPkts,
       "docsIetfQosUpstreamStatsTable": docsIetfQosUpstreamStatsTable,
       "docsIetfQosUpstreamStatsEntry": docsIetfQosUpstreamStatsEntry,
       "docsIetfQosSID": docsIetfQosSID,
       "docsIetfQosUpstreamFragments": docsIetfQosUpstreamFragments,
       "docsIetfQosUpstreamFragDiscards": docsIetfQosUpstreamFragDiscards,
       "docsIetfQosUpstreamConcatBursts": docsIetfQosUpstreamConcatBursts,
       "docsIetfQosDynamicServiceStatsTable": docsIetfQosDynamicServiceStatsTable,
       "docsIetfQosDynamicServiceStatsEntry": docsIetfQosDynamicServiceStatsEntry,
       "docsIetfQosIfDirection": docsIetfQosIfDirection,
       "docsIetfQosDSAReqs": docsIetfQosDSAReqs,
       "docsIetfQosDSARsps": docsIetfQosDSARsps,
       "docsIetfQosDSAAcks": docsIetfQosDSAAcks,
       "docsIetfQosDSCReqs": docsIetfQosDSCReqs,
       "docsIetfQosDSCRsps": docsIetfQosDSCRsps,
       "docsIetfQosDSCAcks": docsIetfQosDSCAcks,
       "docsIetfQosDSDReqs": docsIetfQosDSDReqs,
       "docsIetfQosDSDRsps": docsIetfQosDSDRsps,
       "docsIetfQosDynamicAdds": docsIetfQosDynamicAdds,
       "docsIetfQosDynamicAddFails": docsIetfQosDynamicAddFails,
       "docsIetfQosDynamicChanges": docsIetfQosDynamicChanges,
       "docsIetfQosDynamicChangeFails": docsIetfQosDynamicChangeFails,
       "docsIetfQosDynamicDeletes": docsIetfQosDynamicDeletes,
       "docsIetfQosDynamicDeleteFails": docsIetfQosDynamicDeleteFails,
       "docsIetfQosDCCReqs": docsIetfQosDCCReqs,
       "docsIetfQosDCCRsps": docsIetfQosDCCRsps,
       "docsIetfQosDCCAcks": docsIetfQosDCCAcks,
       "docsIetfQosDCCs": docsIetfQosDCCs,
       "docsIetfQosDCCFails": docsIetfQosDCCFails,
       "docsIetfQosServiceFlowLogTable": docsIetfQosServiceFlowLogTable,
       "docsIetfQosServiceFlowLogEntry": docsIetfQosServiceFlowLogEntry,
       "docsIetfQosServiceFlowLogIndex": docsIetfQosServiceFlowLogIndex,
       "docsIetfQosServiceFlowLogIfIndex": docsIetfQosServiceFlowLogIfIndex,
       "docsIetfQosServiceFlowLogSFID": docsIetfQosServiceFlowLogSFID,
       "docsIetfQosServiceFlowLogCmMac": docsIetfQosServiceFlowLogCmMac,
       "docsIetfQosServiceFlowLogPkts": docsIetfQosServiceFlowLogPkts,
       "docsIetfQosServiceFlowLogOctets": docsIetfQosServiceFlowLogOctets,
       "docsIetfQosServiceFlowLogTimeDeleted": docsIetfQosServiceFlowLogTimeDeleted,
       "docsIetfQosServiceFlowLogTimeCreated": docsIetfQosServiceFlowLogTimeCreated,
       "docsIetfQosServiceFlowLogTimeActive": docsIetfQosServiceFlowLogTimeActive,
       "docsIetfQosServiceFlowLogDirection": docsIetfQosServiceFlowLogDirection,
       "docsIetfQosServiceFlowLogPrimary": docsIetfQosServiceFlowLogPrimary,
       "docsIetfQosServiceFlowLogServiceClassName": docsIetfQosServiceFlowLogServiceClassName,
       "docsIetfQosServiceFlowLogPolicedDropPkts": docsIetfQosServiceFlowLogPolicedDropPkts,
       "docsIetfQosServiceFlowLogPolicedDelayPkts": docsIetfQosServiceFlowLogPolicedDelayPkts,
       "docsIetfQosServiceFlowLogControl": docsIetfQosServiceFlowLogControl,
       "docsIetfQosServiceClassTable": docsIetfQosServiceClassTable,
       "docsIetfQosServiceClassEntry": docsIetfQosServiceClassEntry,
       "docsIetfQosServiceClassName": docsIetfQosServiceClassName,
       "docsIetfQosServiceClassStatus": docsIetfQosServiceClassStatus,
       "docsIetfQosServiceClassPriority": docsIetfQosServiceClassPriority,
       "docsIetfQosServiceClassMaxTrafficRate": docsIetfQosServiceClassMaxTrafficRate,
       "docsIetfQosServiceClassMaxTrafficBurst": docsIetfQosServiceClassMaxTrafficBurst,
       "docsIetfQosServiceClassMinReservedRate": docsIetfQosServiceClassMinReservedRate,
       "docsIetfQosServiceClassMinReservedPkt": docsIetfQosServiceClassMinReservedPkt,
       "docsIetfQosServiceClassMaxConcatBurst": docsIetfQosServiceClassMaxConcatBurst,
       "docsIetfQosServiceClassNomPollInterval": docsIetfQosServiceClassNomPollInterval,
       "docsIetfQosServiceClassTolPollJitter": docsIetfQosServiceClassTolPollJitter,
       "docsIetfQosServiceClassUnsolicitGrantSize": docsIetfQosServiceClassUnsolicitGrantSize,
       "docsIetfQosServiceClassNomGrantInterval": docsIetfQosServiceClassNomGrantInterval,
       "docsIetfQosServiceClassTolGrantJitter": docsIetfQosServiceClassTolGrantJitter,
       "docsIetfQosServiceClassGrantsPerInterval": docsIetfQosServiceClassGrantsPerInterval,
       "docsIetfQosServiceClassMaxLatency": docsIetfQosServiceClassMaxLatency,
       "docsIetfQosServiceClassActiveTimeout": docsIetfQosServiceClassActiveTimeout,
       "docsIetfQosServiceClassAdmittedTimeout": docsIetfQosServiceClassAdmittedTimeout,
       "docsIetfQosServiceClassSchedulingType": docsIetfQosServiceClassSchedulingType,
       "docsIetfQosServiceClassRequestPolicy": docsIetfQosServiceClassRequestPolicy,
       "docsIetfQosServiceClassTosAndMask": docsIetfQosServiceClassTosAndMask,
       "docsIetfQosServiceClassTosOrMask": docsIetfQosServiceClassTosOrMask,
       "docsIetfQosServiceClassDirection": docsIetfQosServiceClassDirection,
       "docsIetfQosServiceClassStorageType": docsIetfQosServiceClassStorageType,
       "docsIetfQosServiceClassDSCPOverwrite": docsIetfQosServiceClassDSCPOverwrite,
       "docsIetfQosServiceClassPolicyTable": docsIetfQosServiceClassPolicyTable,
       "docsIetfQosServiceClassPolicyEntry": docsIetfQosServiceClassPolicyEntry,
       "docsIetfQosServiceClassPolicyIndex": docsIetfQosServiceClassPolicyIndex,
       "docsIetfQosServiceClassPolicyName": docsIetfQosServiceClassPolicyName,
       "docsIetfQosServiceClassPolicyRulePriority": docsIetfQosServiceClassPolicyRulePriority,
       "docsIetfQosServiceClassPolicyStatus": docsIetfQosServiceClassPolicyStatus,
       "docsIetfQosServiceClassPolicyStorageType": docsIetfQosServiceClassPolicyStorageType,
       "docsIetfQosPHSTable": docsIetfQosPHSTable,
       "docsIetfQosPHSEntry": docsIetfQosPHSEntry,
       "docsIetfQosPHSField": docsIetfQosPHSField,
       "docsIetfQosPHSMask": docsIetfQosPHSMask,
       "docsIetfQosPHSSize": docsIetfQosPHSSize,
       "docsIetfQosPHSVerify": docsIetfQosPHSVerify,
       "docsIetfQosPHSIndex": docsIetfQosPHSIndex,
       "docsIetfQosCmtsMacToSrvFlowTable": docsIetfQosCmtsMacToSrvFlowTable,
       "docsIetfQosCmtsMacToSrvFlowEntry": docsIetfQosCmtsMacToSrvFlowEntry,
       "docsIetfQosCmtsCmMac": docsIetfQosCmtsCmMac,
       "docsIetfQosCmtsServiceFlowId": docsIetfQosCmtsServiceFlowId,
       "docsIetfQosCmtsIfIndex": docsIetfQosCmtsIfIndex,
       "docsIetfQosConformance": docsIetfQosConformance,
       "docsIetfQosGroups": docsIetfQosGroups,
       "docsIetfQosBaseGroup": docsIetfQosBaseGroup,
       "docsIetfQosParamSetGroup": docsIetfQosParamSetGroup,
       "docsIetfQosCmtsGroup": docsIetfQosCmtsGroup,
       "docsIetfQosSrvClassPolicyGroup": docsIetfQosSrvClassPolicyGroup,
       "docsIetfQosServiceClassGroup": docsIetfQosServiceClassGroup,
       "docsIetfQosCompliances": docsIetfQosCompliances,
       "docsIetfQosCompliance": docsIetfQosCompliance}
)
