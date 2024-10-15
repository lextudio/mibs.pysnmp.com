# SNMP MIB module (DOCS-QOS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-QOS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:31 2024
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

(DocsL2vpnIfList,
 clabProjDocsis) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "DocsL2vpnIfList",
    "clabProjDocsis")

(DscpOrAny,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "DscpOrAny")

(AttrAggrRuleMask,
 AttributeMask,
 ChId,
 ChSetId,
 ChannelList,
 Dsid,
 IfDirection) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "AttrAggrRuleMask",
    "AttributeMask",
    "ChId",
    "ChSetId",
    "ChannelList",
    "Dsid",
    "IfDirection")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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

docsQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21)
)
docsQosMib.setRevisions(
        ("2016-08-18 00:00",
         "2016-05-05 00:00",
         "2015-04-08 00:00",
         "2014-07-29 00:00",
         "2012-08-09 00:00",
         "2012-03-29 00:00",
         "2011-02-10 00:00",
         "2009-10-02 00:00",
         "2009-05-29 00:00",
         "2009-01-21 00:00",
         "2008-05-22 00:00",
         "2007-12-06 00:00",
         "2007-08-03 00:00",
         "2007-05-18 00:00",
         "2006-12-07 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BitRate(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class SchedulingType(Integer32, TextualConvention):
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

_DocsQosMibObjects_ObjectIdentity = ObjectIdentity
docsQosMibObjects = _DocsQosMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1)
)
_DocsQosPktClassTable_Object = MibTable
docsQosPktClassTable = _DocsQosPktClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1)
)
if mibBuilder.loadTexts:
    docsQosPktClassTable.setStatus("current")
_DocsQosPktClassEntry_Object = MibTableRow
docsQosPktClassEntry = _DocsQosPktClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1)
)
docsQosPktClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS3-MIB", "docsQosPktClassId"),
)
if mibBuilder.loadTexts:
    docsQosPktClassEntry.setStatus("current")


class _DocsQosPktClassId_Type(Unsigned32):
    """Custom type docsQosPktClassId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsQosPktClassId_Type.__name__ = "Unsigned32"
_DocsQosPktClassId_Object = MibTableColumn
docsQosPktClassId = _DocsQosPktClassId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 1),
    _DocsQosPktClassId_Type()
)
docsQosPktClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosPktClassId.setStatus("current")
_DocsQosPktClassDirection_Type = IfDirection
_DocsQosPktClassDirection_Object = MibTableColumn
docsQosPktClassDirection = _DocsQosPktClassDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 2),
    _DocsQosPktClassDirection_Type()
)
docsQosPktClassDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDirection.setStatus("current")


class _DocsQosPktClassPriority_Type(Unsigned32):
    """Custom type docsQosPktClassPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosPktClassPriority_Type.__name__ = "Unsigned32"
_DocsQosPktClassPriority_Object = MibTableColumn
docsQosPktClassPriority = _DocsQosPktClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 3),
    _DocsQosPktClassPriority_Type()
)
docsQosPktClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassPriority.setStatus("current")


class _DocsQosPktClassIpTosLow_Type(OctetString):
    """Custom type docsQosPktClassIpTosLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosPktClassIpTosLow_Type.__name__ = "OctetString"
_DocsQosPktClassIpTosLow_Object = MibTableColumn
docsQosPktClassIpTosLow = _DocsQosPktClassIpTosLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 4),
    _DocsQosPktClassIpTosLow_Type()
)
docsQosPktClassIpTosLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpTosLow.setStatus("current")


class _DocsQosPktClassIpTosHigh_Type(OctetString):
    """Custom type docsQosPktClassIpTosHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosPktClassIpTosHigh_Type.__name__ = "OctetString"
_DocsQosPktClassIpTosHigh_Object = MibTableColumn
docsQosPktClassIpTosHigh = _DocsQosPktClassIpTosHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 5),
    _DocsQosPktClassIpTosHigh_Type()
)
docsQosPktClassIpTosHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpTosHigh.setStatus("current")


class _DocsQosPktClassIpTosMask_Type(OctetString):
    """Custom type docsQosPktClassIpTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosPktClassIpTosMask_Type.__name__ = "OctetString"
_DocsQosPktClassIpTosMask_Object = MibTableColumn
docsQosPktClassIpTosMask = _DocsQosPktClassIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 6),
    _DocsQosPktClassIpTosMask_Type()
)
docsQosPktClassIpTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpTosMask.setStatus("current")


class _DocsQosPktClassIpProtocol_Type(Unsigned32):
    """Custom type docsQosPktClassIpProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 258),
    )


_DocsQosPktClassIpProtocol_Type.__name__ = "Unsigned32"
_DocsQosPktClassIpProtocol_Object = MibTableColumn
docsQosPktClassIpProtocol = _DocsQosPktClassIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 7),
    _DocsQosPktClassIpProtocol_Type()
)
docsQosPktClassIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpProtocol.setStatus("current")
_DocsQosPktClassIpSourceAddr_Type = InetAddress
_DocsQosPktClassIpSourceAddr_Object = MibTableColumn
docsQosPktClassIpSourceAddr = _DocsQosPktClassIpSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 8),
    _DocsQosPktClassIpSourceAddr_Type()
)
docsQosPktClassIpSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpSourceAddr.setStatus("current")
_DocsQosPktClassIpSourceMask_Type = InetAddress
_DocsQosPktClassIpSourceMask_Object = MibTableColumn
docsQosPktClassIpSourceMask = _DocsQosPktClassIpSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 9),
    _DocsQosPktClassIpSourceMask_Type()
)
docsQosPktClassIpSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpSourceMask.setStatus("current")
_DocsQosPktClassIpDestAddr_Type = InetAddress
_DocsQosPktClassIpDestAddr_Object = MibTableColumn
docsQosPktClassIpDestAddr = _DocsQosPktClassIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 10),
    _DocsQosPktClassIpDestAddr_Type()
)
docsQosPktClassIpDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpDestAddr.setStatus("current")
_DocsQosPktClassIpDestMask_Type = InetAddress
_DocsQosPktClassIpDestMask_Object = MibTableColumn
docsQosPktClassIpDestMask = _DocsQosPktClassIpDestMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 11),
    _DocsQosPktClassIpDestMask_Type()
)
docsQosPktClassIpDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpDestMask.setStatus("current")
_DocsQosPktClassSourcePortStart_Type = InetPortNumber
_DocsQosPktClassSourcePortStart_Object = MibTableColumn
docsQosPktClassSourcePortStart = _DocsQosPktClassSourcePortStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 12),
    _DocsQosPktClassSourcePortStart_Type()
)
docsQosPktClassSourcePortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassSourcePortStart.setStatus("current")
_DocsQosPktClassSourcePortEnd_Type = InetPortNumber
_DocsQosPktClassSourcePortEnd_Object = MibTableColumn
docsQosPktClassSourcePortEnd = _DocsQosPktClassSourcePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 13),
    _DocsQosPktClassSourcePortEnd_Type()
)
docsQosPktClassSourcePortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassSourcePortEnd.setStatus("current")
_DocsQosPktClassDestPortStart_Type = InetPortNumber
_DocsQosPktClassDestPortStart_Object = MibTableColumn
docsQosPktClassDestPortStart = _DocsQosPktClassDestPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 14),
    _DocsQosPktClassDestPortStart_Type()
)
docsQosPktClassDestPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDestPortStart.setStatus("current")
_DocsQosPktClassDestPortEnd_Type = InetPortNumber
_DocsQosPktClassDestPortEnd_Object = MibTableColumn
docsQosPktClassDestPortEnd = _DocsQosPktClassDestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 15),
    _DocsQosPktClassDestPortEnd_Type()
)
docsQosPktClassDestPortEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDestPortEnd.setStatus("current")
_DocsQosPktClassDestMacAddr_Type = MacAddress
_DocsQosPktClassDestMacAddr_Object = MibTableColumn
docsQosPktClassDestMacAddr = _DocsQosPktClassDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 16),
    _DocsQosPktClassDestMacAddr_Type()
)
docsQosPktClassDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDestMacAddr.setStatus("current")
_DocsQosPktClassDestMacMask_Type = MacAddress
_DocsQosPktClassDestMacMask_Object = MibTableColumn
docsQosPktClassDestMacMask = _DocsQosPktClassDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 17),
    _DocsQosPktClassDestMacMask_Type()
)
docsQosPktClassDestMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassDestMacMask.setStatus("current")
_DocsQosPktClassSourceMacAddr_Type = MacAddress
_DocsQosPktClassSourceMacAddr_Object = MibTableColumn
docsQosPktClassSourceMacAddr = _DocsQosPktClassSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 18),
    _DocsQosPktClassSourceMacAddr_Type()
)
docsQosPktClassSourceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassSourceMacAddr.setStatus("current")


class _DocsQosPktClassEnetProtocolType_Type(Integer32):
    """Custom type docsQosPktClassEnetProtocolType based on Integer32"""
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


_DocsQosPktClassEnetProtocolType_Type.__name__ = "Integer32"
_DocsQosPktClassEnetProtocolType_Object = MibTableColumn
docsQosPktClassEnetProtocolType = _DocsQosPktClassEnetProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 19),
    _DocsQosPktClassEnetProtocolType_Type()
)
docsQosPktClassEnetProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassEnetProtocolType.setStatus("current")


class _DocsQosPktClassEnetProtocol_Type(Unsigned32):
    """Custom type docsQosPktClassEnetProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosPktClassEnetProtocol_Type.__name__ = "Unsigned32"
_DocsQosPktClassEnetProtocol_Object = MibTableColumn
docsQosPktClassEnetProtocol = _DocsQosPktClassEnetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 20),
    _DocsQosPktClassEnetProtocol_Type()
)
docsQosPktClassEnetProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassEnetProtocol.setStatus("current")


class _DocsQosPktClassUserPriLow_Type(Unsigned32):
    """Custom type docsQosPktClassUserPriLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsQosPktClassUserPriLow_Type.__name__ = "Unsigned32"
_DocsQosPktClassUserPriLow_Object = MibTableColumn
docsQosPktClassUserPriLow = _DocsQosPktClassUserPriLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 22),
    _DocsQosPktClassUserPriLow_Type()
)
docsQosPktClassUserPriLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassUserPriLow.setStatus("current")


class _DocsQosPktClassUserPriHigh_Type(Unsigned32):
    """Custom type docsQosPktClassUserPriHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsQosPktClassUserPriHigh_Type.__name__ = "Unsigned32"
_DocsQosPktClassUserPriHigh_Object = MibTableColumn
docsQosPktClassUserPriHigh = _DocsQosPktClassUserPriHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 23),
    _DocsQosPktClassUserPriHigh_Type()
)
docsQosPktClassUserPriHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassUserPriHigh.setStatus("current")


class _DocsQosPktClassVlanId_Type(Unsigned32):
    """Custom type docsQosPktClassVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_DocsQosPktClassVlanId_Type.__name__ = "Unsigned32"
_DocsQosPktClassVlanId_Object = MibTableColumn
docsQosPktClassVlanId = _DocsQosPktClassVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 24),
    _DocsQosPktClassVlanId_Type()
)
docsQosPktClassVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassVlanId.setStatus("current")


class _DocsQosPktClassState_Type(Integer32):
    """Custom type docsQosPktClassState based on Integer32"""
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


_DocsQosPktClassState_Type.__name__ = "Integer32"
_DocsQosPktClassState_Object = MibTableColumn
docsQosPktClassState = _DocsQosPktClassState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 25),
    _DocsQosPktClassState_Type()
)
docsQosPktClassState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassState.setStatus("current")
_DocsQosPktClassPkts_Type = Counter64
_DocsQosPktClassPkts_Object = MibTableColumn
docsQosPktClassPkts = _DocsQosPktClassPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 26),
    _DocsQosPktClassPkts_Type()
)
docsQosPktClassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassPkts.setStatus("current")


class _DocsQosPktClassBitMap_Type(Bits):
    """Custom type docsQosPktClassBitMap based on Bits"""
    namedValues = NamedValues(
        *(("activationState", 1),
          ("cmInterfaceMask", 18),
          ("destMac", 12),
          ("destPortEnd", 11),
          ("destPortStart", 10),
          ("ethertype", 14),
          ("flowLabel", 17),
          ("icmpTypeHigh", 20),
          ("icmpTypeLow", 19),
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

_DocsQosPktClassBitMap_Type.__name__ = "Bits"
_DocsQosPktClassBitMap_Object = MibTableColumn
docsQosPktClassBitMap = _DocsQosPktClassBitMap_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 27),
    _DocsQosPktClassBitMap_Type()
)
docsQosPktClassBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassBitMap.setStatus("current")
_DocsQosPktClassIpAddrType_Type = InetAddressType
_DocsQosPktClassIpAddrType_Object = MibTableColumn
docsQosPktClassIpAddrType = _DocsQosPktClassIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 28),
    _DocsQosPktClassIpAddrType_Type()
)
docsQosPktClassIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIpAddrType.setStatus("current")


class _DocsQosPktClassFlowLabel_Type(Unsigned32):
    """Custom type docsQosPktClassFlowLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_DocsQosPktClassFlowLabel_Type.__name__ = "Unsigned32"
_DocsQosPktClassFlowLabel_Object = MibTableColumn
docsQosPktClassFlowLabel = _DocsQosPktClassFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 29),
    _DocsQosPktClassFlowLabel_Type()
)
docsQosPktClassFlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassFlowLabel.setStatus("current")
_DocsQosPktClassCmInterfaceMask_Type = DocsL2vpnIfList
_DocsQosPktClassCmInterfaceMask_Object = MibTableColumn
docsQosPktClassCmInterfaceMask = _DocsQosPktClassCmInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 30),
    _DocsQosPktClassCmInterfaceMask_Type()
)
docsQosPktClassCmInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassCmInterfaceMask.setStatus("current")


class _DocsQosPktClassIcmpTypeLow_Type(Unsigned32):
    """Custom type docsQosPktClassIcmpTypeLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosPktClassIcmpTypeLow_Type.__name__ = "Unsigned32"
_DocsQosPktClassIcmpTypeLow_Object = MibTableColumn
docsQosPktClassIcmpTypeLow = _DocsQosPktClassIcmpTypeLow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 31),
    _DocsQosPktClassIcmpTypeLow_Type()
)
docsQosPktClassIcmpTypeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIcmpTypeLow.setStatus("current")


class _DocsQosPktClassIcmpTypeHigh_Type(Unsigned32):
    """Custom type docsQosPktClassIcmpTypeHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosPktClassIcmpTypeHigh_Type.__name__ = "Unsigned32"
_DocsQosPktClassIcmpTypeHigh_Object = MibTableColumn
docsQosPktClassIcmpTypeHigh = _DocsQosPktClassIcmpTypeHigh_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 1, 1, 32),
    _DocsQosPktClassIcmpTypeHigh_Type()
)
docsQosPktClassIcmpTypeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPktClassIcmpTypeHigh.setStatus("current")
_DocsQosParamSetTable_Object = MibTable
docsQosParamSetTable = _DocsQosParamSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2)
)
if mibBuilder.loadTexts:
    docsQosParamSetTable.setStatus("current")
_DocsQosParamSetEntry_Object = MibTableRow
docsQosParamSetEntry = _DocsQosParamSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1)
)
docsQosParamSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosParamSetType"),
    (0, "DOCS-QOS3-MIB", "docsQosParamSetServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosParamSetEntry.setStatus("current")


class _DocsQosParamSetServiceClassName_Type(SnmpAdminString):
    """Custom type docsQosParamSetServiceClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DocsQosParamSetServiceClassName_Type.__name__ = "SnmpAdminString"
_DocsQosParamSetServiceClassName_Object = MibTableColumn
docsQosParamSetServiceClassName = _DocsQosParamSetServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 4),
    _DocsQosParamSetServiceClassName_Type()
)
docsQosParamSetServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetServiceClassName.setStatus("current")


class _DocsQosParamSetPriority_Type(Unsigned32):
    """Custom type docsQosParamSetPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsQosParamSetPriority_Type.__name__ = "Unsigned32"
_DocsQosParamSetPriority_Object = MibTableColumn
docsQosParamSetPriority = _DocsQosParamSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 5),
    _DocsQosParamSetPriority_Type()
)
docsQosParamSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetPriority.setStatus("current")
_DocsQosParamSetMaxTrafficRate_Type = BitRate
_DocsQosParamSetMaxTrafficRate_Object = MibTableColumn
docsQosParamSetMaxTrafficRate = _DocsQosParamSetMaxTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 6),
    _DocsQosParamSetMaxTrafficRate_Type()
)
docsQosParamSetMaxTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTrafficRate.setUnits("bps")
_DocsQosParamSetMaxTrafficBurst_Type = Unsigned32
_DocsQosParamSetMaxTrafficBurst_Object = MibTableColumn
docsQosParamSetMaxTrafficBurst = _DocsQosParamSetMaxTrafficBurst_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 7),
    _DocsQosParamSetMaxTrafficBurst_Type()
)
docsQosParamSetMaxTrafficBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTrafficBurst.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTrafficBurst.setUnits("bytes")
_DocsQosParamSetMinReservedRate_Type = BitRate
_DocsQosParamSetMinReservedRate_Object = MibTableColumn
docsQosParamSetMinReservedRate = _DocsQosParamSetMinReservedRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 8),
    _DocsQosParamSetMinReservedRate_Type()
)
docsQosParamSetMinReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMinReservedRate.setUnits("bps")


class _DocsQosParamSetMinReservedPkt_Type(Unsigned32):
    """Custom type docsQosParamSetMinReservedPkt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetMinReservedPkt_Type.__name__ = "Unsigned32"
_DocsQosParamSetMinReservedPkt_Object = MibTableColumn
docsQosParamSetMinReservedPkt = _DocsQosParamSetMinReservedPkt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 9),
    _DocsQosParamSetMinReservedPkt_Type()
)
docsQosParamSetMinReservedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMinReservedPkt.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMinReservedPkt.setUnits("bytes")


class _DocsQosParamSetActiveTimeout_Type(Unsigned32):
    """Custom type docsQosParamSetActiveTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetActiveTimeout_Type.__name__ = "Unsigned32"
_DocsQosParamSetActiveTimeout_Object = MibTableColumn
docsQosParamSetActiveTimeout = _DocsQosParamSetActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 10),
    _DocsQosParamSetActiveTimeout_Type()
)
docsQosParamSetActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetActiveTimeout.setUnits("seconds")


class _DocsQosParamSetAdmittedTimeout_Type(Unsigned32):
    """Custom type docsQosParamSetAdmittedTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetAdmittedTimeout_Type.__name__ = "Unsigned32"
_DocsQosParamSetAdmittedTimeout_Object = MibTableColumn
docsQosParamSetAdmittedTimeout = _DocsQosParamSetAdmittedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 11),
    _DocsQosParamSetAdmittedTimeout_Type()
)
docsQosParamSetAdmittedTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetAdmittedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetAdmittedTimeout.setUnits("seconds")


class _DocsQosParamSetMaxConcatBurst_Type(Unsigned32):
    """Custom type docsQosParamSetMaxConcatBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetMaxConcatBurst_Type.__name__ = "Unsigned32"
_DocsQosParamSetMaxConcatBurst_Object = MibTableColumn
docsQosParamSetMaxConcatBurst = _DocsQosParamSetMaxConcatBurst_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 12),
    _DocsQosParamSetMaxConcatBurst_Type()
)
docsQosParamSetMaxConcatBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxConcatBurst.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMaxConcatBurst.setUnits("bytes")
_DocsQosParamSetSchedulingType_Type = SchedulingType
_DocsQosParamSetSchedulingType_Object = MibTableColumn
docsQosParamSetSchedulingType = _DocsQosParamSetSchedulingType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 13),
    _DocsQosParamSetSchedulingType_Type()
)
docsQosParamSetSchedulingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetSchedulingType.setStatus("current")
_DocsQosParamSetNomPollInterval_Type = Unsigned32
_DocsQosParamSetNomPollInterval_Object = MibTableColumn
docsQosParamSetNomPollInterval = _DocsQosParamSetNomPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 14),
    _DocsQosParamSetNomPollInterval_Type()
)
docsQosParamSetNomPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetNomPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetNomPollInterval.setUnits("microseconds")
_DocsQosParamSetTolPollJitter_Type = Unsigned32
_DocsQosParamSetTolPollJitter_Object = MibTableColumn
docsQosParamSetTolPollJitter = _DocsQosParamSetTolPollJitter_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 15),
    _DocsQosParamSetTolPollJitter_Type()
)
docsQosParamSetTolPollJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetTolPollJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetTolPollJitter.setUnits("microseconds")


class _DocsQosParamSetUnsolicitGrantSize_Type(Unsigned32):
    """Custom type docsQosParamSetUnsolicitGrantSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetUnsolicitGrantSize_Type.__name__ = "Unsigned32"
_DocsQosParamSetUnsolicitGrantSize_Object = MibTableColumn
docsQosParamSetUnsolicitGrantSize = _DocsQosParamSetUnsolicitGrantSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 16),
    _DocsQosParamSetUnsolicitGrantSize_Type()
)
docsQosParamSetUnsolicitGrantSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetUnsolicitGrantSize.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetUnsolicitGrantSize.setUnits("bytes")
_DocsQosParamSetNomGrantInterval_Type = Unsigned32
_DocsQosParamSetNomGrantInterval_Object = MibTableColumn
docsQosParamSetNomGrantInterval = _DocsQosParamSetNomGrantInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 17),
    _DocsQosParamSetNomGrantInterval_Type()
)
docsQosParamSetNomGrantInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetNomGrantInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetNomGrantInterval.setUnits("microseconds")
_DocsQosParamSetTolGrantJitter_Type = Unsigned32
_DocsQosParamSetTolGrantJitter_Object = MibTableColumn
docsQosParamSetTolGrantJitter = _DocsQosParamSetTolGrantJitter_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 18),
    _DocsQosParamSetTolGrantJitter_Type()
)
docsQosParamSetTolGrantJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetTolGrantJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetTolGrantJitter.setUnits("microseconds")


class _DocsQosParamSetGrantsPerInterval_Type(Unsigned32):
    """Custom type docsQosParamSetGrantsPerInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DocsQosParamSetGrantsPerInterval_Type.__name__ = "Unsigned32"
_DocsQosParamSetGrantsPerInterval_Object = MibTableColumn
docsQosParamSetGrantsPerInterval = _DocsQosParamSetGrantsPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 19),
    _DocsQosParamSetGrantsPerInterval_Type()
)
docsQosParamSetGrantsPerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetGrantsPerInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetGrantsPerInterval.setUnits("dataGrants")


class _DocsQosParamSetTosAndMask_Type(OctetString):
    """Custom type docsQosParamSetTosAndMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosParamSetTosAndMask_Type.__name__ = "OctetString"
_DocsQosParamSetTosAndMask_Object = MibTableColumn
docsQosParamSetTosAndMask = _DocsQosParamSetTosAndMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 20),
    _DocsQosParamSetTosAndMask_Type()
)
docsQosParamSetTosAndMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetTosAndMask.setStatus("current")


class _DocsQosParamSetTosOrMask_Type(OctetString):
    """Custom type docsQosParamSetTosOrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosParamSetTosOrMask_Type.__name__ = "OctetString"
_DocsQosParamSetTosOrMask_Object = MibTableColumn
docsQosParamSetTosOrMask = _DocsQosParamSetTosOrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 21),
    _DocsQosParamSetTosOrMask_Type()
)
docsQosParamSetTosOrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetTosOrMask.setStatus("current")
_DocsQosParamSetMaxLatency_Type = Unsigned32
_DocsQosParamSetMaxLatency_Object = MibTableColumn
docsQosParamSetMaxLatency = _DocsQosParamSetMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 22),
    _DocsQosParamSetMaxLatency_Type()
)
docsQosParamSetMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMaxLatency.setUnits("microseconds")


class _DocsQosParamSetType_Type(Integer32):
    """Custom type docsQosParamSetType based on Integer32"""
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


_DocsQosParamSetType_Type.__name__ = "Integer32"
_DocsQosParamSetType_Object = MibTableColumn
docsQosParamSetType = _DocsQosParamSetType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 23),
    _DocsQosParamSetType_Type()
)
docsQosParamSetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosParamSetType.setStatus("current")


class _DocsQosParamSetRequestPolicyOct_Type(OctetString):
    """Custom type docsQosParamSetRequestPolicyOct based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DocsQosParamSetRequestPolicyOct_Type.__name__ = "OctetString"
_DocsQosParamSetRequestPolicyOct_Object = MibTableColumn
docsQosParamSetRequestPolicyOct = _DocsQosParamSetRequestPolicyOct_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 24),
    _DocsQosParamSetRequestPolicyOct_Type()
)
docsQosParamSetRequestPolicyOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetRequestPolicyOct.setStatus("current")


class _DocsQosParamSetBitMap_Type(Bits):
    """Custom type docsQosParamSetBitMap based on Bits"""
    namedValues = NamedValues(
        *(("activeTimeout", 5),
          ("admittedTimeout", 6),
          ("applicationId", 21),
          ("aqmEnabled", 33),
          ("aqmLatencyTarget", 34),
          ("attrAggrMask", 20),
          ("dataRateUnit", 35),
          ("dsResequencing", 29),
          ("forbiddenAttrMask", 19),
          ("grantsPerInterval", 15),
          ("maxConcatBurst", 7),
          ("maxLatency", 17),
          ("maxOutstandingBytesPerSidCluster", 25),
          ("maxReqPerSidCluster", 24),
          ("maxTotalBytesReqPerSidCluster", 26),
          ("maxTrafficBurst", 2),
          ("maxTrafficRate", 1),
          ("maximumBuffer", 32),
          ("maximumTimeInSidCluster", 27),
          ("minReservedPkt", 4),
          ("minReservedRate", 3),
          ("minimumBuffer", 30),
          ("multipBytesReq", 23),
          ("multipCntnReqWindow", 22),
          ("nomGrantInterval", 13),
          ("nomPollInterval", 10),
          ("peakTrafficRate", 28),
          ("requestPolicy", 9),
          ("requiredAttrMask", 18),
          ("schedulingType", 8),
          ("targetBuffer", 31),
          ("tolGrantJitter", 14),
          ("tolPollJitter", 11),
          ("tosOverwrite", 16),
          ("trafficPriority", 0),
          ("unsolicitGrantSize", 12))
    )

_DocsQosParamSetBitMap_Type.__name__ = "Bits"
_DocsQosParamSetBitMap_Object = MibTableColumn
docsQosParamSetBitMap = _DocsQosParamSetBitMap_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 25),
    _DocsQosParamSetBitMap_Type()
)
docsQosParamSetBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetBitMap.setStatus("current")


class _DocsQosParamSetServiceFlowId_Type(Unsigned32):
    """Custom type docsQosParamSetServiceFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsQosParamSetServiceFlowId_Type.__name__ = "Unsigned32"
_DocsQosParamSetServiceFlowId_Object = MibTableColumn
docsQosParamSetServiceFlowId = _DocsQosParamSetServiceFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 26),
    _DocsQosParamSetServiceFlowId_Type()
)
docsQosParamSetServiceFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosParamSetServiceFlowId.setStatus("current")
_DocsQosParamSetRequiredAttrMask_Type = AttributeMask
_DocsQosParamSetRequiredAttrMask_Object = MibTableColumn
docsQosParamSetRequiredAttrMask = _DocsQosParamSetRequiredAttrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 27),
    _DocsQosParamSetRequiredAttrMask_Type()
)
docsQosParamSetRequiredAttrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetRequiredAttrMask.setStatus("current")
_DocsQosParamSetForbiddenAttrMask_Type = AttributeMask
_DocsQosParamSetForbiddenAttrMask_Object = MibTableColumn
docsQosParamSetForbiddenAttrMask = _DocsQosParamSetForbiddenAttrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 28),
    _DocsQosParamSetForbiddenAttrMask_Type()
)
docsQosParamSetForbiddenAttrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetForbiddenAttrMask.setStatus("current")
_DocsQosParamSetAttrAggrRuleMask_Type = AttrAggrRuleMask
_DocsQosParamSetAttrAggrRuleMask_Object = MibTableColumn
docsQosParamSetAttrAggrRuleMask = _DocsQosParamSetAttrAggrRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 29),
    _DocsQosParamSetAttrAggrRuleMask_Type()
)
docsQosParamSetAttrAggrRuleMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetAttrAggrRuleMask.setStatus("current")
_DocsQosParamSetAppId_Type = Unsigned32
_DocsQosParamSetAppId_Object = MibTableColumn
docsQosParamSetAppId = _DocsQosParamSetAppId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 30),
    _DocsQosParamSetAppId_Type()
)
docsQosParamSetAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetAppId.setStatus("current")


class _DocsQosParamSetMultiplierContentionReqWindow_Type(Unsigned32):
    """Custom type docsQosParamSetMultiplierContentionReqWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 12),
    )


_DocsQosParamSetMultiplierContentionReqWindow_Type.__name__ = "Unsigned32"
_DocsQosParamSetMultiplierContentionReqWindow_Object = MibTableColumn
docsQosParamSetMultiplierContentionReqWindow = _DocsQosParamSetMultiplierContentionReqWindow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 31),
    _DocsQosParamSetMultiplierContentionReqWindow_Type()
)
docsQosParamSetMultiplierContentionReqWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMultiplierContentionReqWindow.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMultiplierContentionReqWindow.setUnits("eighths")


class _DocsQosParamSetMultiplierBytesReq_Type(Unsigned32):
    """Custom type docsQosParamSetMultiplierBytesReq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
    )


_DocsQosParamSetMultiplierBytesReq_Type.__name__ = "Unsigned32"
_DocsQosParamSetMultiplierBytesReq_Object = MibTableColumn
docsQosParamSetMultiplierBytesReq = _DocsQosParamSetMultiplierBytesReq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 32),
    _DocsQosParamSetMultiplierBytesReq_Type()
)
docsQosParamSetMultiplierBytesReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMultiplierBytesReq.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMultiplierBytesReq.setUnits("requests")


class _DocsQosParamSetMaxReqPerSidCluster_Type(Unsigned32):
    """Custom type docsQosParamSetMaxReqPerSidCluster based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosParamSetMaxReqPerSidCluster_Type.__name__ = "Unsigned32"
_DocsQosParamSetMaxReqPerSidCluster_Object = MibTableColumn
docsQosParamSetMaxReqPerSidCluster = _DocsQosParamSetMaxReqPerSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 33),
    _DocsQosParamSetMaxReqPerSidCluster_Type()
)
docsQosParamSetMaxReqPerSidCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxReqPerSidCluster.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsQosParamSetMaxReqPerSidCluster.setUnits("bytes")
_DocsQosParamSetMaxOutstandingBytesPerSidCluster_Type = Unsigned32
_DocsQosParamSetMaxOutstandingBytesPerSidCluster_Object = MibTableColumn
docsQosParamSetMaxOutstandingBytesPerSidCluster = _DocsQosParamSetMaxOutstandingBytesPerSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 34),
    _DocsQosParamSetMaxOutstandingBytesPerSidCluster_Type()
)
docsQosParamSetMaxOutstandingBytesPerSidCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxOutstandingBytesPerSidCluster.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsQosParamSetMaxOutstandingBytesPerSidCluster.setUnits("bytes")
_DocsQosParamSetMaxTotBytesReqPerSidCluster_Type = Unsigned32
_DocsQosParamSetMaxTotBytesReqPerSidCluster_Object = MibTableColumn
docsQosParamSetMaxTotBytesReqPerSidCluster = _DocsQosParamSetMaxTotBytesReqPerSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 35),
    _DocsQosParamSetMaxTotBytesReqPerSidCluster_Type()
)
docsQosParamSetMaxTotBytesReqPerSidCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTotBytesReqPerSidCluster.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTotBytesReqPerSidCluster.setUnits("bytes")


class _DocsQosParamSetMaxTimeInSidCluster_Type(Unsigned32):
    """Custom type docsQosParamSetMaxTimeInSidCluster based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosParamSetMaxTimeInSidCluster_Type.__name__ = "Unsigned32"
_DocsQosParamSetMaxTimeInSidCluster_Object = MibTableColumn
docsQosParamSetMaxTimeInSidCluster = _DocsQosParamSetMaxTimeInSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 36),
    _DocsQosParamSetMaxTimeInSidCluster_Type()
)
docsQosParamSetMaxTimeInSidCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTimeInSidCluster.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsQosParamSetMaxTimeInSidCluster.setUnits("milliseconds")
_DocsQosParamSetPeakTrafficRate_Type = Unsigned32
_DocsQosParamSetPeakTrafficRate_Object = MibTableColumn
docsQosParamSetPeakTrafficRate = _DocsQosParamSetPeakTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 37),
    _DocsQosParamSetPeakTrafficRate_Type()
)
docsQosParamSetPeakTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetPeakTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetPeakTrafficRate.setUnits("bps")


class _DocsQosParamSetDsResequencing_Type(Integer32):
    """Custom type docsQosParamSetDsResequencing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noResequencingDsid", 1),
          ("notApplicable", 2),
          ("resequencingDsidIfBonded", 0))
    )


_DocsQosParamSetDsResequencing_Type.__name__ = "Integer32"
_DocsQosParamSetDsResequencing_Object = MibTableColumn
docsQosParamSetDsResequencing = _DocsQosParamSetDsResequencing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 38),
    _DocsQosParamSetDsResequencing_Type()
)
docsQosParamSetDsResequencing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetDsResequencing.setStatus("current")


class _DocsQosParamSetMinimumBuffer_Type(Unsigned32):
    """Custom type docsQosParamSetMinimumBuffer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosParamSetMinimumBuffer_Type.__name__ = "Unsigned32"
_DocsQosParamSetMinimumBuffer_Object = MibTableColumn
docsQosParamSetMinimumBuffer = _DocsQosParamSetMinimumBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 39),
    _DocsQosParamSetMinimumBuffer_Type()
)
docsQosParamSetMinimumBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMinimumBuffer.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMinimumBuffer.setUnits("bytes")


class _DocsQosParamSetTargetBuffer_Type(Unsigned32):
    """Custom type docsQosParamSetTargetBuffer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosParamSetTargetBuffer_Type.__name__ = "Unsigned32"
_DocsQosParamSetTargetBuffer_Object = MibTableColumn
docsQosParamSetTargetBuffer = _DocsQosParamSetTargetBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 40),
    _DocsQosParamSetTargetBuffer_Type()
)
docsQosParamSetTargetBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetTargetBuffer.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetTargetBuffer.setUnits("bytes")


class _DocsQosParamSetMaximumBuffer_Type(Unsigned32):
    """Custom type docsQosParamSetMaximumBuffer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosParamSetMaximumBuffer_Type.__name__ = "Unsigned32"
_DocsQosParamSetMaximumBuffer_Object = MibTableColumn
docsQosParamSetMaximumBuffer = _DocsQosParamSetMaximumBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 41),
    _DocsQosParamSetMaximumBuffer_Type()
)
docsQosParamSetMaximumBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetMaximumBuffer.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetMaximumBuffer.setUnits("bytes")
_DocsQosParamSetAqmDisabled_Type = TruthValue
_DocsQosParamSetAqmDisabled_Object = MibTableColumn
docsQosParamSetAqmDisabled = _DocsQosParamSetAqmDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 42),
    _DocsQosParamSetAqmDisabled_Type()
)
docsQosParamSetAqmDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetAqmDisabled.setStatus("current")


class _DocsQosParamSetAqmLatencyTarget_Type(Unsigned32):
    """Custom type docsQosParamSetAqmLatencyTarget based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_DocsQosParamSetAqmLatencyTarget_Type.__name__ = "Unsigned32"
_DocsQosParamSetAqmLatencyTarget_Object = MibTableColumn
docsQosParamSetAqmLatencyTarget = _DocsQosParamSetAqmLatencyTarget_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 43),
    _DocsQosParamSetAqmLatencyTarget_Type()
)
docsQosParamSetAqmLatencyTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetAqmLatencyTarget.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetAqmLatencyTarget.setUnits("milliseconds")
_DocsQosParamSetHCMaxTrafficRate_Type = CounterBasedGauge64
_DocsQosParamSetHCMaxTrafficRate_Object = MibTableColumn
docsQosParamSetHCMaxTrafficRate = _DocsQosParamSetHCMaxTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 44),
    _DocsQosParamSetHCMaxTrafficRate_Type()
)
docsQosParamSetHCMaxTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetHCMaxTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetHCMaxTrafficRate.setUnits("bps")
_DocsQosParamSetHCMinReservedRate_Type = CounterBasedGauge64
_DocsQosParamSetHCMinReservedRate_Object = MibTableColumn
docsQosParamSetHCMinReservedRate = _DocsQosParamSetHCMinReservedRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 45),
    _DocsQosParamSetHCMinReservedRate_Type()
)
docsQosParamSetHCMinReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetHCMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetHCMinReservedRate.setUnits("bps")
_DocsQosParamSetHCPeakTrafficRate_Type = CounterBasedGauge64
_DocsQosParamSetHCPeakTrafficRate_Object = MibTableColumn
docsQosParamSetHCPeakTrafficRate = _DocsQosParamSetHCPeakTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 46),
    _DocsQosParamSetHCPeakTrafficRate_Type()
)
docsQosParamSetHCPeakTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetHCPeakTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosParamSetHCPeakTrafficRate.setUnits("bps")


class _DocsQosParamSetAqmAlgInUse_Type(Integer32):
    """Custom type docsQosParamSetAqmAlgInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("docsisPIE", 3),
          ("other", 2),
          ("unknown", 1))
    )


_DocsQosParamSetAqmAlgInUse_Type.__name__ = "Integer32"
_DocsQosParamSetAqmAlgInUse_Object = MibTableColumn
docsQosParamSetAqmAlgInUse = _DocsQosParamSetAqmAlgInUse_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 2, 1, 47),
    _DocsQosParamSetAqmAlgInUse_Type()
)
docsQosParamSetAqmAlgInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosParamSetAqmAlgInUse.setStatus("current")
_DocsQosServiceFlowTable_Object = MibTable
docsQosServiceFlowTable = _DocsQosServiceFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3)
)
if mibBuilder.loadTexts:
    docsQosServiceFlowTable.setStatus("current")
_DocsQosServiceFlowEntry_Object = MibTableRow
docsQosServiceFlowEntry = _DocsQosServiceFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1)
)
docsQosServiceFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosServiceFlowEntry.setStatus("current")
_DocsQosServiceFlowId_Type = Unsigned32
_DocsQosServiceFlowId_Object = MibTableColumn
docsQosServiceFlowId = _DocsQosServiceFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 1),
    _DocsQosServiceFlowId_Type()
)
docsQosServiceFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosServiceFlowId.setStatus("current")


class _DocsQosServiceFlowSID_Type(Unsigned32):
    """Custom type docsQosServiceFlowSID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_DocsQosServiceFlowSID_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowSID_Object = MibTableColumn
docsQosServiceFlowSID = _DocsQosServiceFlowSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 6),
    _DocsQosServiceFlowSID_Type()
)
docsQosServiceFlowSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowSID.setStatus("current")
_DocsQosServiceFlowDirection_Type = IfDirection
_DocsQosServiceFlowDirection_Object = MibTableColumn
docsQosServiceFlowDirection = _DocsQosServiceFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 7),
    _DocsQosServiceFlowDirection_Type()
)
docsQosServiceFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowDirection.setStatus("current")
_DocsQosServiceFlowPrimary_Type = TruthValue
_DocsQosServiceFlowPrimary_Object = MibTableColumn
docsQosServiceFlowPrimary = _DocsQosServiceFlowPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 8),
    _DocsQosServiceFlowPrimary_Type()
)
docsQosServiceFlowPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPrimary.setStatus("current")


class _DocsQosServiceFlowParamSetTypeStatus_Type(Bits):
    """Custom type docsQosServiceFlowParamSetTypeStatus based on Bits"""
    namedValues = NamedValues(
        *(("active", 0),
          ("admitted", 1),
          ("provisioned", 2))
    )

_DocsQosServiceFlowParamSetTypeStatus_Type.__name__ = "Bits"
_DocsQosServiceFlowParamSetTypeStatus_Object = MibTableColumn
docsQosServiceFlowParamSetTypeStatus = _DocsQosServiceFlowParamSetTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 9),
    _DocsQosServiceFlowParamSetTypeStatus_Type()
)
docsQosServiceFlowParamSetTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowParamSetTypeStatus.setStatus("current")
_DocsQosServiceFlowChSetId_Type = ChSetId
_DocsQosServiceFlowChSetId_Object = MibTableColumn
docsQosServiceFlowChSetId = _DocsQosServiceFlowChSetId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 10),
    _DocsQosServiceFlowChSetId_Type()
)
docsQosServiceFlowChSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowChSetId.setStatus("current")
_DocsQosServiceFlowAttrAssignSuccess_Type = TruthValue
_DocsQosServiceFlowAttrAssignSuccess_Object = MibTableColumn
docsQosServiceFlowAttrAssignSuccess = _DocsQosServiceFlowAttrAssignSuccess_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 11),
    _DocsQosServiceFlowAttrAssignSuccess_Type()
)
docsQosServiceFlowAttrAssignSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowAttrAssignSuccess.setStatus("current")
_DocsQosServiceFlowDsid_Type = Dsid
_DocsQosServiceFlowDsid_Object = MibTableColumn
docsQosServiceFlowDsid = _DocsQosServiceFlowDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 12),
    _DocsQosServiceFlowDsid_Type()
)
docsQosServiceFlowDsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowDsid.setStatus("current")


class _DocsQosServiceFlowMaxReqPerSidCluster_Type(Unsigned32):
    """Custom type docsQosServiceFlowMaxReqPerSidCluster based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosServiceFlowMaxReqPerSidCluster_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowMaxReqPerSidCluster_Object = MibTableColumn
docsQosServiceFlowMaxReqPerSidCluster = _DocsQosServiceFlowMaxReqPerSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 13),
    _DocsQosServiceFlowMaxReqPerSidCluster_Type()
)
docsQosServiceFlowMaxReqPerSidCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowMaxReqPerSidCluster.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowMaxReqPerSidCluster.setUnits("bytes")
_DocsQosServiceFlowMaxOutstandingBytesPerSidCluster_Type = Unsigned32
_DocsQosServiceFlowMaxOutstandingBytesPerSidCluster_Object = MibTableColumn
docsQosServiceFlowMaxOutstandingBytesPerSidCluster = _DocsQosServiceFlowMaxOutstandingBytesPerSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 14),
    _DocsQosServiceFlowMaxOutstandingBytesPerSidCluster_Type()
)
docsQosServiceFlowMaxOutstandingBytesPerSidCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowMaxOutstandingBytesPerSidCluster.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowMaxOutstandingBytesPerSidCluster.setUnits("bytes")
_DocsQosServiceFlowMaxTotBytesReqPerSidCluster_Type = Unsigned32
_DocsQosServiceFlowMaxTotBytesReqPerSidCluster_Object = MibTableColumn
docsQosServiceFlowMaxTotBytesReqPerSidCluster = _DocsQosServiceFlowMaxTotBytesReqPerSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 15),
    _DocsQosServiceFlowMaxTotBytesReqPerSidCluster_Type()
)
docsQosServiceFlowMaxTotBytesReqPerSidCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowMaxTotBytesReqPerSidCluster.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowMaxTotBytesReqPerSidCluster.setUnits("bytes")


class _DocsQosServiceFlowMaxTimeInSidCluster_Type(Unsigned32):
    """Custom type docsQosServiceFlowMaxTimeInSidCluster based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceFlowMaxTimeInSidCluster_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowMaxTimeInSidCluster_Object = MibTableColumn
docsQosServiceFlowMaxTimeInSidCluster = _DocsQosServiceFlowMaxTimeInSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 16),
    _DocsQosServiceFlowMaxTimeInSidCluster_Type()
)
docsQosServiceFlowMaxTimeInSidCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowMaxTimeInSidCluster.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowMaxTimeInSidCluster.setUnits("milliseconds")


class _DocsQosServiceFlowBufferSize_Type(Unsigned32):
    """Custom type docsQosServiceFlowBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosServiceFlowBufferSize_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowBufferSize_Object = MibTableColumn
docsQosServiceFlowBufferSize = _DocsQosServiceFlowBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 17),
    _DocsQosServiceFlowBufferSize_Type()
)
docsQosServiceFlowBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowBufferSize.setUnits("bytes")
_DocsQosServiceFlowIatcProfileName_Type = SnmpAdminString
_DocsQosServiceFlowIatcProfileName_Object = MibTableColumn
docsQosServiceFlowIatcProfileName = _DocsQosServiceFlowIatcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 3, 1, 18),
    _DocsQosServiceFlowIatcProfileName_Type()
)
docsQosServiceFlowIatcProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowIatcProfileName.setStatus("current")
_DocsQosServiceFlowStatsTable_Object = MibTable
docsQosServiceFlowStatsTable = _DocsQosServiceFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4)
)
if mibBuilder.loadTexts:
    docsQosServiceFlowStatsTable.setStatus("current")
_DocsQosServiceFlowStatsEntry_Object = MibTableRow
docsQosServiceFlowStatsEntry = _DocsQosServiceFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4, 1)
)
docsQosServiceFlowStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosServiceFlowStatsEntry.setStatus("current")
_DocsQosServiceFlowPkts_Type = Counter64
_DocsQosServiceFlowPkts_Object = MibTableColumn
docsQosServiceFlowPkts = _DocsQosServiceFlowPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4, 1, 1),
    _DocsQosServiceFlowPkts_Type()
)
docsQosServiceFlowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowPkts.setUnits("packets")
_DocsQosServiceFlowOctets_Type = Counter64
_DocsQosServiceFlowOctets_Object = MibTableColumn
docsQosServiceFlowOctets = _DocsQosServiceFlowOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4, 1, 2),
    _DocsQosServiceFlowOctets_Type()
)
docsQosServiceFlowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowOctets.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowOctets.setUnits("bytes")
_DocsQosServiceFlowTimeCreated_Type = TimeStamp
_DocsQosServiceFlowTimeCreated_Object = MibTableColumn
docsQosServiceFlowTimeCreated = _DocsQosServiceFlowTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4, 1, 3),
    _DocsQosServiceFlowTimeCreated_Type()
)
docsQosServiceFlowTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowTimeCreated.setStatus("current")
_DocsQosServiceFlowTimeActive_Type = Counter32
_DocsQosServiceFlowTimeActive_Object = MibTableColumn
docsQosServiceFlowTimeActive = _DocsQosServiceFlowTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4, 1, 4),
    _DocsQosServiceFlowTimeActive_Type()
)
docsQosServiceFlowTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowTimeActive.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowTimeActive.setUnits("seconds")
_DocsQosServiceFlowPHSUnknowns_Type = Counter32
_DocsQosServiceFlowPHSUnknowns_Object = MibTableColumn
docsQosServiceFlowPHSUnknowns = _DocsQosServiceFlowPHSUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4, 1, 5),
    _DocsQosServiceFlowPHSUnknowns_Type()
)
docsQosServiceFlowPHSUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPHSUnknowns.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowPHSUnknowns.setUnits("packets")
_DocsQosServiceFlowPolicedDropPkts_Type = Counter32
_DocsQosServiceFlowPolicedDropPkts_Object = MibTableColumn
docsQosServiceFlowPolicedDropPkts = _DocsQosServiceFlowPolicedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4, 1, 6),
    _DocsQosServiceFlowPolicedDropPkts_Type()
)
docsQosServiceFlowPolicedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPolicedDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowPolicedDropPkts.setUnits("packets")
_DocsQosServiceFlowPolicedDelayPkts_Type = Counter32
_DocsQosServiceFlowPolicedDelayPkts_Object = MibTableColumn
docsQosServiceFlowPolicedDelayPkts = _DocsQosServiceFlowPolicedDelayPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4, 1, 7),
    _DocsQosServiceFlowPolicedDelayPkts_Type()
)
docsQosServiceFlowPolicedDelayPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowPolicedDelayPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowPolicedDelayPkts.setUnits("packets")
_DocsQosServiceFlowAqmDroppedPkts_Type = Counter64
_DocsQosServiceFlowAqmDroppedPkts_Object = MibTableColumn
docsQosServiceFlowAqmDroppedPkts = _DocsQosServiceFlowAqmDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 4, 1, 8),
    _DocsQosServiceFlowAqmDroppedPkts_Type()
)
docsQosServiceFlowAqmDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowAqmDroppedPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowAqmDroppedPkts.setUnits("packets")
_DocsQosUpstreamStatsTable_Object = MibTable
docsQosUpstreamStatsTable = _DocsQosUpstreamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 5)
)
if mibBuilder.loadTexts:
    docsQosUpstreamStatsTable.setStatus("current")
_DocsQosUpstreamStatsEntry_Object = MibTableRow
docsQosUpstreamStatsEntry = _DocsQosUpstreamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 5, 1)
)
docsQosUpstreamStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosSID"),
)
if mibBuilder.loadTexts:
    docsQosUpstreamStatsEntry.setStatus("current")


class _DocsQosSID_Type(Unsigned32):
    """Custom type docsQosSID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsQosSID_Type.__name__ = "Unsigned32"
_DocsQosSID_Object = MibTableColumn
docsQosSID = _DocsQosSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 5, 1, 1),
    _DocsQosSID_Type()
)
docsQosSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosSID.setStatus("current")
_DocsQosUpstreamFragments_Type = Counter32
_DocsQosUpstreamFragments_Object = MibTableColumn
docsQosUpstreamFragments = _DocsQosUpstreamFragments_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 5, 1, 2),
    _DocsQosUpstreamFragments_Type()
)
docsQosUpstreamFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosUpstreamFragments.setStatus("current")
if mibBuilder.loadTexts:
    docsQosUpstreamFragments.setUnits("fragments")
_DocsQosUpstreamFragDiscards_Type = Counter32
_DocsQosUpstreamFragDiscards_Object = MibTableColumn
docsQosUpstreamFragDiscards = _DocsQosUpstreamFragDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 5, 1, 3),
    _DocsQosUpstreamFragDiscards_Type()
)
docsQosUpstreamFragDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosUpstreamFragDiscards.setStatus("current")
if mibBuilder.loadTexts:
    docsQosUpstreamFragDiscards.setUnits("fragments")
_DocsQosUpstreamConcatBursts_Type = Counter32
_DocsQosUpstreamConcatBursts_Object = MibTableColumn
docsQosUpstreamConcatBursts = _DocsQosUpstreamConcatBursts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 5, 1, 4),
    _DocsQosUpstreamConcatBursts_Type()
)
docsQosUpstreamConcatBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosUpstreamConcatBursts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosUpstreamConcatBursts.setUnits("headers")
_DocsQosDynamicServiceStatsTable_Object = MibTable
docsQosDynamicServiceStatsTable = _DocsQosDynamicServiceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6)
)
if mibBuilder.loadTexts:
    docsQosDynamicServiceStatsTable.setStatus("current")
_DocsQosDynamicServiceStatsEntry_Object = MibTableRow
docsQosDynamicServiceStatsEntry = _DocsQosDynamicServiceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1)
)
docsQosDynamicServiceStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosIfDirection"),
)
if mibBuilder.loadTexts:
    docsQosDynamicServiceStatsEntry.setStatus("current")
_DocsQosIfDirection_Type = IfDirection
_DocsQosIfDirection_Object = MibTableColumn
docsQosIfDirection = _DocsQosIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 1),
    _DocsQosIfDirection_Type()
)
docsQosIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosIfDirection.setStatus("current")
_DocsQosDSAReqs_Type = Counter32
_DocsQosDSAReqs_Object = MibTableColumn
docsQosDSAReqs = _DocsQosDSAReqs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 2),
    _DocsQosDSAReqs_Type()
)
docsQosDSAReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSAReqs.setStatus("current")
_DocsQosDSARsps_Type = Counter32
_DocsQosDSARsps_Object = MibTableColumn
docsQosDSARsps = _DocsQosDSARsps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 3),
    _DocsQosDSARsps_Type()
)
docsQosDSARsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSARsps.setStatus("current")
_DocsQosDSAAcks_Type = Counter32
_DocsQosDSAAcks_Object = MibTableColumn
docsQosDSAAcks = _DocsQosDSAAcks_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 4),
    _DocsQosDSAAcks_Type()
)
docsQosDSAAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSAAcks.setStatus("current")
_DocsQosDSCReqs_Type = Counter32
_DocsQosDSCReqs_Object = MibTableColumn
docsQosDSCReqs = _DocsQosDSCReqs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 5),
    _DocsQosDSCReqs_Type()
)
docsQosDSCReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSCReqs.setStatus("current")
_DocsQosDSCRsps_Type = Counter32
_DocsQosDSCRsps_Object = MibTableColumn
docsQosDSCRsps = _DocsQosDSCRsps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 6),
    _DocsQosDSCRsps_Type()
)
docsQosDSCRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSCRsps.setStatus("current")
_DocsQosDSCAcks_Type = Counter32
_DocsQosDSCAcks_Object = MibTableColumn
docsQosDSCAcks = _DocsQosDSCAcks_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 7),
    _DocsQosDSCAcks_Type()
)
docsQosDSCAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSCAcks.setStatus("current")
_DocsQosDSDReqs_Type = Counter32
_DocsQosDSDReqs_Object = MibTableColumn
docsQosDSDReqs = _DocsQosDSDReqs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 8),
    _DocsQosDSDReqs_Type()
)
docsQosDSDReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSDReqs.setStatus("current")
_DocsQosDSDRsps_Type = Counter32
_DocsQosDSDRsps_Object = MibTableColumn
docsQosDSDRsps = _DocsQosDSDRsps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 9),
    _DocsQosDSDRsps_Type()
)
docsQosDSDRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDSDRsps.setStatus("current")
_DocsQosDynamicAdds_Type = Counter32
_DocsQosDynamicAdds_Object = MibTableColumn
docsQosDynamicAdds = _DocsQosDynamicAdds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 10),
    _DocsQosDynamicAdds_Type()
)
docsQosDynamicAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicAdds.setStatus("current")
_DocsQosDynamicAddFails_Type = Counter32
_DocsQosDynamicAddFails_Object = MibTableColumn
docsQosDynamicAddFails = _DocsQosDynamicAddFails_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 11),
    _DocsQosDynamicAddFails_Type()
)
docsQosDynamicAddFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicAddFails.setStatus("current")
_DocsQosDynamicChanges_Type = Counter32
_DocsQosDynamicChanges_Object = MibTableColumn
docsQosDynamicChanges = _DocsQosDynamicChanges_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 12),
    _DocsQosDynamicChanges_Type()
)
docsQosDynamicChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicChanges.setStatus("current")
_DocsQosDynamicChangeFails_Type = Counter32
_DocsQosDynamicChangeFails_Object = MibTableColumn
docsQosDynamicChangeFails = _DocsQosDynamicChangeFails_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 13),
    _DocsQosDynamicChangeFails_Type()
)
docsQosDynamicChangeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicChangeFails.setStatus("current")
_DocsQosDynamicDeletes_Type = Counter32
_DocsQosDynamicDeletes_Object = MibTableColumn
docsQosDynamicDeletes = _DocsQosDynamicDeletes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 14),
    _DocsQosDynamicDeletes_Type()
)
docsQosDynamicDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicDeletes.setStatus("current")
_DocsQosDynamicDeleteFails_Type = Counter32
_DocsQosDynamicDeleteFails_Object = MibTableColumn
docsQosDynamicDeleteFails = _DocsQosDynamicDeleteFails_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 15),
    _DocsQosDynamicDeleteFails_Type()
)
docsQosDynamicDeleteFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDynamicDeleteFails.setStatus("current")
_DocsQosDCCReqs_Type = Counter32
_DocsQosDCCReqs_Object = MibTableColumn
docsQosDCCReqs = _DocsQosDCCReqs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 16),
    _DocsQosDCCReqs_Type()
)
docsQosDCCReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCReqs.setStatus("current")
_DocsQosDCCRsps_Type = Counter32
_DocsQosDCCRsps_Object = MibTableColumn
docsQosDCCRsps = _DocsQosDCCRsps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 17),
    _DocsQosDCCRsps_Type()
)
docsQosDCCRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCRsps.setStatus("current")
_DocsQosDCCAcks_Type = Counter32
_DocsQosDCCAcks_Object = MibTableColumn
docsQosDCCAcks = _DocsQosDCCAcks_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 18),
    _DocsQosDCCAcks_Type()
)
docsQosDCCAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCAcks.setStatus("current")
_DocsQosDCCs_Type = Counter32
_DocsQosDCCs_Object = MibTableColumn
docsQosDCCs = _DocsQosDCCs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 19),
    _DocsQosDCCs_Type()
)
docsQosDCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCs.setStatus("current")
_DocsQosDCCFails_Type = Counter32
_DocsQosDCCFails_Object = MibTableColumn
docsQosDCCFails = _DocsQosDCCFails_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 20),
    _DocsQosDCCFails_Type()
)
docsQosDCCFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCFails.setStatus("current")
_DocsQosDCCRspDeparts_Type = Counter32
_DocsQosDCCRspDeparts_Object = MibTableColumn
docsQosDCCRspDeparts = _DocsQosDCCRspDeparts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 21),
    _DocsQosDCCRspDeparts_Type()
)
docsQosDCCRspDeparts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCRspDeparts.setStatus("current")
_DocsQosDCCRspArrives_Type = Counter32
_DocsQosDCCRspArrives_Object = MibTableColumn
docsQosDCCRspArrives = _DocsQosDCCRspArrives_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 22),
    _DocsQosDCCRspArrives_Type()
)
docsQosDCCRspArrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDCCRspArrives.setStatus("current")
_DocsQosDbcReqs_Type = Counter32
_DocsQosDbcReqs_Object = MibTableColumn
docsQosDbcReqs = _DocsQosDbcReqs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 23),
    _DocsQosDbcReqs_Type()
)
docsQosDbcReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDbcReqs.setStatus("current")
_DocsQosDbcRsps_Type = Counter32
_DocsQosDbcRsps_Object = MibTableColumn
docsQosDbcRsps = _DocsQosDbcRsps_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 24),
    _DocsQosDbcRsps_Type()
)
docsQosDbcRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDbcRsps.setStatus("current")
_DocsQosDbcAcks_Type = Counter32
_DocsQosDbcAcks_Object = MibTableColumn
docsQosDbcAcks = _DocsQosDbcAcks_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 25),
    _DocsQosDbcAcks_Type()
)
docsQosDbcAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDbcAcks.setStatus("current")
_DocsQosDbcSuccesses_Type = Counter32
_DocsQosDbcSuccesses_Object = MibTableColumn
docsQosDbcSuccesses = _DocsQosDbcSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 26),
    _DocsQosDbcSuccesses_Type()
)
docsQosDbcSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDbcSuccesses.setStatus("current")
_DocsQosDbcFails_Type = Counter32
_DocsQosDbcFails_Object = MibTableColumn
docsQosDbcFails = _DocsQosDbcFails_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 27),
    _DocsQosDbcFails_Type()
)
docsQosDbcFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDbcFails.setStatus("current")
_DocsQosDbcPartial_Type = Counter32
_DocsQosDbcPartial_Object = MibTableColumn
docsQosDbcPartial = _DocsQosDbcPartial_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 6, 1, 28),
    _DocsQosDbcPartial_Type()
)
docsQosDbcPartial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosDbcPartial.setStatus("current")
_DocsQosServiceFlowLogTable_Object = MibTable
docsQosServiceFlowLogTable = _DocsQosServiceFlowLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7)
)
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTable.setStatus("current")
_DocsQosServiceFlowLogEntry_Object = MibTableRow
docsQosServiceFlowLogEntry = _DocsQosServiceFlowLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1)
)
docsQosServiceFlowLogEntry.setIndexNames(
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowLogIndex"),
)
if mibBuilder.loadTexts:
    docsQosServiceFlowLogEntry.setStatus("current")


class _DocsQosServiceFlowLogIndex_Type(Unsigned32):
    """Custom type docsQosServiceFlowLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsQosServiceFlowLogIndex_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowLogIndex_Object = MibTableColumn
docsQosServiceFlowLogIndex = _DocsQosServiceFlowLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 1),
    _DocsQosServiceFlowLogIndex_Type()
)
docsQosServiceFlowLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogIndex.setStatus("current")
_DocsQosServiceFlowLogIfIndex_Type = InterfaceIndex
_DocsQosServiceFlowLogIfIndex_Object = MibTableColumn
docsQosServiceFlowLogIfIndex = _DocsQosServiceFlowLogIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 2),
    _DocsQosServiceFlowLogIfIndex_Type()
)
docsQosServiceFlowLogIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogIfIndex.setStatus("current")


class _DocsQosServiceFlowLogSFID_Type(Unsigned32):
    """Custom type docsQosServiceFlowLogSFID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsQosServiceFlowLogSFID_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowLogSFID_Object = MibTableColumn
docsQosServiceFlowLogSFID = _DocsQosServiceFlowLogSFID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 3),
    _DocsQosServiceFlowLogSFID_Type()
)
docsQosServiceFlowLogSFID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogSFID.setStatus("current")
_DocsQosServiceFlowLogCmMac_Type = MacAddress
_DocsQosServiceFlowLogCmMac_Object = MibTableColumn
docsQosServiceFlowLogCmMac = _DocsQosServiceFlowLogCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 4),
    _DocsQosServiceFlowLogCmMac_Type()
)
docsQosServiceFlowLogCmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogCmMac.setStatus("current")
_DocsQosServiceFlowLogPkts_Type = Counter64
_DocsQosServiceFlowLogPkts_Object = MibTableColumn
docsQosServiceFlowLogPkts = _DocsQosServiceFlowLogPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 5),
    _DocsQosServiceFlowLogPkts_Type()
)
docsQosServiceFlowLogPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPkts.setUnits("packets")
_DocsQosServiceFlowLogOctets_Type = Counter64
_DocsQosServiceFlowLogOctets_Object = MibTableColumn
docsQosServiceFlowLogOctets = _DocsQosServiceFlowLogOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 6),
    _DocsQosServiceFlowLogOctets_Type()
)
docsQosServiceFlowLogOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogOctets.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogOctets.setUnits("bytes")
_DocsQosServiceFlowLogTimeDeleted_Type = TimeStamp
_DocsQosServiceFlowLogTimeDeleted_Object = MibTableColumn
docsQosServiceFlowLogTimeDeleted = _DocsQosServiceFlowLogTimeDeleted_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 7),
    _DocsQosServiceFlowLogTimeDeleted_Type()
)
docsQosServiceFlowLogTimeDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTimeDeleted.setStatus("current")
_DocsQosServiceFlowLogTimeCreated_Type = TimeStamp
_DocsQosServiceFlowLogTimeCreated_Object = MibTableColumn
docsQosServiceFlowLogTimeCreated = _DocsQosServiceFlowLogTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 8),
    _DocsQosServiceFlowLogTimeCreated_Type()
)
docsQosServiceFlowLogTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTimeCreated.setStatus("current")
_DocsQosServiceFlowLogTimeActive_Type = Counter32
_DocsQosServiceFlowLogTimeActive_Object = MibTableColumn
docsQosServiceFlowLogTimeActive = _DocsQosServiceFlowLogTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 9),
    _DocsQosServiceFlowLogTimeActive_Type()
)
docsQosServiceFlowLogTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTimeActive.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogTimeActive.setUnits("seconds")
_DocsQosServiceFlowLogDirection_Type = IfDirection
_DocsQosServiceFlowLogDirection_Object = MibTableColumn
docsQosServiceFlowLogDirection = _DocsQosServiceFlowLogDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 11),
    _DocsQosServiceFlowLogDirection_Type()
)
docsQosServiceFlowLogDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogDirection.setStatus("current")
_DocsQosServiceFlowLogPrimary_Type = TruthValue
_DocsQosServiceFlowLogPrimary_Object = MibTableColumn
docsQosServiceFlowLogPrimary = _DocsQosServiceFlowLogPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 12),
    _DocsQosServiceFlowLogPrimary_Type()
)
docsQosServiceFlowLogPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPrimary.setStatus("current")


class _DocsQosServiceFlowLogServiceClassName_Type(SnmpAdminString):
    """Custom type docsQosServiceFlowLogServiceClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DocsQosServiceFlowLogServiceClassName_Type.__name__ = "SnmpAdminString"
_DocsQosServiceFlowLogServiceClassName_Object = MibTableColumn
docsQosServiceFlowLogServiceClassName = _DocsQosServiceFlowLogServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 13),
    _DocsQosServiceFlowLogServiceClassName_Type()
)
docsQosServiceFlowLogServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogServiceClassName.setStatus("current")
_DocsQosServiceFlowLogPolicedDropPkts_Type = Counter32
_DocsQosServiceFlowLogPolicedDropPkts_Object = MibTableColumn
docsQosServiceFlowLogPolicedDropPkts = _DocsQosServiceFlowLogPolicedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 14),
    _DocsQosServiceFlowLogPolicedDropPkts_Type()
)
docsQosServiceFlowLogPolicedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPolicedDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPolicedDropPkts.setUnits("packets")
_DocsQosServiceFlowLogPolicedDelayPkts_Type = Counter32
_DocsQosServiceFlowLogPolicedDelayPkts_Object = MibTableColumn
docsQosServiceFlowLogPolicedDelayPkts = _DocsQosServiceFlowLogPolicedDelayPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 15),
    _DocsQosServiceFlowLogPolicedDelayPkts_Type()
)
docsQosServiceFlowLogPolicedDelayPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPolicedDelayPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogPolicedDelayPkts.setUnits("packets")


class _DocsQosServiceFlowLogControl_Type(Integer32):
    """Custom type docsQosServiceFlowLogControl based on Integer32"""
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


_DocsQosServiceFlowLogControl_Type.__name__ = "Integer32"
_DocsQosServiceFlowLogControl_Object = MibTableColumn
docsQosServiceFlowLogControl = _DocsQosServiceFlowLogControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 7, 1, 16),
    _DocsQosServiceFlowLogControl_Type()
)
docsQosServiceFlowLogControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsQosServiceFlowLogControl.setStatus("current")
_DocsQosServiceClassTable_Object = MibTable
docsQosServiceClassTable = _DocsQosServiceClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8)
)
if mibBuilder.loadTexts:
    docsQosServiceClassTable.setStatus("current")
_DocsQosServiceClassEntry_Object = MibTableRow
docsQosServiceClassEntry = _DocsQosServiceClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1)
)
docsQosServiceClassEntry.setIndexNames(
    (0, "DOCS-QOS3-MIB", "docsQosServiceClassName"),
)
if mibBuilder.loadTexts:
    docsQosServiceClassEntry.setStatus("current")


class _DocsQosServiceClassName_Type(SnmpAdminString):
    """Custom type docsQosServiceClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DocsQosServiceClassName_Type.__name__ = "SnmpAdminString"
_DocsQosServiceClassName_Object = MibTableColumn
docsQosServiceClassName = _DocsQosServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 1),
    _DocsQosServiceClassName_Type()
)
docsQosServiceClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosServiceClassName.setStatus("current")
_DocsQosServiceClassStatus_Type = RowStatus
_DocsQosServiceClassStatus_Object = MibTableColumn
docsQosServiceClassStatus = _DocsQosServiceClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 3),
    _DocsQosServiceClassStatus_Type()
)
docsQosServiceClassStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassStatus.setStatus("current")


class _DocsQosServiceClassPriority_Type(Unsigned32):
    """Custom type docsQosServiceClassPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsQosServiceClassPriority_Type.__name__ = "Unsigned32"
_DocsQosServiceClassPriority_Object = MibTableColumn
docsQosServiceClassPriority = _DocsQosServiceClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 4),
    _DocsQosServiceClassPriority_Type()
)
docsQosServiceClassPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassPriority.setStatus("current")


class _DocsQosServiceClassMaxTrafficRate_Type(BitRate):
    """Custom type docsQosServiceClassMaxTrafficRate based on BitRate"""
    defaultValue = 0


_DocsQosServiceClassMaxTrafficRate_Object = MibTableColumn
docsQosServiceClassMaxTrafficRate = _DocsQosServiceClassMaxTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 5),
    _DocsQosServiceClassMaxTrafficRate_Type()
)
docsQosServiceClassMaxTrafficRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTrafficRate.setUnits("bps")


class _DocsQosServiceClassMaxTrafficBurst_Type(Unsigned32):
    """Custom type docsQosServiceClassMaxTrafficBurst based on Unsigned32"""
    defaultValue = 3044


_DocsQosServiceClassMaxTrafficBurst_Object = MibTableColumn
docsQosServiceClassMaxTrafficBurst = _DocsQosServiceClassMaxTrafficBurst_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 6),
    _DocsQosServiceClassMaxTrafficBurst_Type()
)
docsQosServiceClassMaxTrafficBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTrafficBurst.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTrafficBurst.setUnits("bytes")


class _DocsQosServiceClassMinReservedRate_Type(BitRate):
    """Custom type docsQosServiceClassMinReservedRate based on BitRate"""
    defaultValue = 0


_DocsQosServiceClassMinReservedRate_Object = MibTableColumn
docsQosServiceClassMinReservedRate = _DocsQosServiceClassMinReservedRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 7),
    _DocsQosServiceClassMinReservedRate_Type()
)
docsQosServiceClassMinReservedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMinReservedRate.setUnits("bps")


class _DocsQosServiceClassMinReservedPkt_Type(Unsigned32):
    """Custom type docsQosServiceClassMinReservedPkt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassMinReservedPkt_Type.__name__ = "Unsigned32"
_DocsQosServiceClassMinReservedPkt_Object = MibTableColumn
docsQosServiceClassMinReservedPkt = _DocsQosServiceClassMinReservedPkt_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 8),
    _DocsQosServiceClassMinReservedPkt_Type()
)
docsQosServiceClassMinReservedPkt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMinReservedPkt.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMinReservedPkt.setUnits("bytes")


class _DocsQosServiceClassMaxConcatBurst_Type(Unsigned32):
    """Custom type docsQosServiceClassMaxConcatBurst based on Unsigned32"""
    defaultValue = 1522

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassMaxConcatBurst_Type.__name__ = "Unsigned32"
_DocsQosServiceClassMaxConcatBurst_Object = MibTableColumn
docsQosServiceClassMaxConcatBurst = _DocsQosServiceClassMaxConcatBurst_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 9),
    _DocsQosServiceClassMaxConcatBurst_Type()
)
docsQosServiceClassMaxConcatBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxConcatBurst.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxConcatBurst.setUnits("bytes")


class _DocsQosServiceClassNomPollInterval_Type(Unsigned32):
    """Custom type docsQosServiceClassNomPollInterval based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassNomPollInterval_Object = MibTableColumn
docsQosServiceClassNomPollInterval = _DocsQosServiceClassNomPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 10),
    _DocsQosServiceClassNomPollInterval_Type()
)
docsQosServiceClassNomPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassNomPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassNomPollInterval.setUnits("microseconds")


class _DocsQosServiceClassTolPollJitter_Type(Unsigned32):
    """Custom type docsQosServiceClassTolPollJitter based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassTolPollJitter_Object = MibTableColumn
docsQosServiceClassTolPollJitter = _DocsQosServiceClassTolPollJitter_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 11),
    _DocsQosServiceClassTolPollJitter_Type()
)
docsQosServiceClassTolPollJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassTolPollJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassTolPollJitter.setUnits("microseconds")


class _DocsQosServiceClassUnsolicitGrantSize_Type(Unsigned32):
    """Custom type docsQosServiceClassUnsolicitGrantSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassUnsolicitGrantSize_Type.__name__ = "Unsigned32"
_DocsQosServiceClassUnsolicitGrantSize_Object = MibTableColumn
docsQosServiceClassUnsolicitGrantSize = _DocsQosServiceClassUnsolicitGrantSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 12),
    _DocsQosServiceClassUnsolicitGrantSize_Type()
)
docsQosServiceClassUnsolicitGrantSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassUnsolicitGrantSize.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassUnsolicitGrantSize.setUnits("bytes")


class _DocsQosServiceClassNomGrantInterval_Type(Unsigned32):
    """Custom type docsQosServiceClassNomGrantInterval based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassNomGrantInterval_Object = MibTableColumn
docsQosServiceClassNomGrantInterval = _DocsQosServiceClassNomGrantInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 13),
    _DocsQosServiceClassNomGrantInterval_Type()
)
docsQosServiceClassNomGrantInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassNomGrantInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassNomGrantInterval.setUnits("microseconds")


class _DocsQosServiceClassTolGrantJitter_Type(Unsigned32):
    """Custom type docsQosServiceClassTolGrantJitter based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassTolGrantJitter_Object = MibTableColumn
docsQosServiceClassTolGrantJitter = _DocsQosServiceClassTolGrantJitter_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 14),
    _DocsQosServiceClassTolGrantJitter_Type()
)
docsQosServiceClassTolGrantJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassTolGrantJitter.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassTolGrantJitter.setUnits("microseconds")


class _DocsQosServiceClassGrantsPerInterval_Type(Unsigned32):
    """Custom type docsQosServiceClassGrantsPerInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DocsQosServiceClassGrantsPerInterval_Type.__name__ = "Unsigned32"
_DocsQosServiceClassGrantsPerInterval_Object = MibTableColumn
docsQosServiceClassGrantsPerInterval = _DocsQosServiceClassGrantsPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 15),
    _DocsQosServiceClassGrantsPerInterval_Type()
)
docsQosServiceClassGrantsPerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassGrantsPerInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassGrantsPerInterval.setUnits("dataGrants")


class _DocsQosServiceClassMaxLatency_Type(Unsigned32):
    """Custom type docsQosServiceClassMaxLatency based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassMaxLatency_Object = MibTableColumn
docsQosServiceClassMaxLatency = _DocsQosServiceClassMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 16),
    _DocsQosServiceClassMaxLatency_Type()
)
docsQosServiceClassMaxLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxLatency.setUnits("microseconds")


class _DocsQosServiceClassActiveTimeout_Type(Unsigned32):
    """Custom type docsQosServiceClassActiveTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassActiveTimeout_Type.__name__ = "Unsigned32"
_DocsQosServiceClassActiveTimeout_Object = MibTableColumn
docsQosServiceClassActiveTimeout = _DocsQosServiceClassActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 17),
    _DocsQosServiceClassActiveTimeout_Type()
)
docsQosServiceClassActiveTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassActiveTimeout.setUnits("seconds")


class _DocsQosServiceClassAdmittedTimeout_Type(Unsigned32):
    """Custom type docsQosServiceClassAdmittedTimeout based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassAdmittedTimeout_Type.__name__ = "Unsigned32"
_DocsQosServiceClassAdmittedTimeout_Object = MibTableColumn
docsQosServiceClassAdmittedTimeout = _DocsQosServiceClassAdmittedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 18),
    _DocsQosServiceClassAdmittedTimeout_Type()
)
docsQosServiceClassAdmittedTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassAdmittedTimeout.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassAdmittedTimeout.setUnits("seconds")


class _DocsQosServiceClassSchedulingType_Type(SchedulingType):
    """Custom type docsQosServiceClassSchedulingType based on SchedulingType"""


_DocsQosServiceClassSchedulingType_Object = MibTableColumn
docsQosServiceClassSchedulingType = _DocsQosServiceClassSchedulingType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 19),
    _DocsQosServiceClassSchedulingType_Type()
)
docsQosServiceClassSchedulingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassSchedulingType.setStatus("current")


class _DocsQosServiceClassRequestPolicy_Type(OctetString):
    """Custom type docsQosServiceClassRequestPolicy based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DocsQosServiceClassRequestPolicy_Type.__name__ = "OctetString"
_DocsQosServiceClassRequestPolicy_Object = MibTableColumn
docsQosServiceClassRequestPolicy = _DocsQosServiceClassRequestPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 20),
    _DocsQosServiceClassRequestPolicy_Type()
)
docsQosServiceClassRequestPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassRequestPolicy.setStatus("current")


class _DocsQosServiceClassTosAndMask_Type(OctetString):
    """Custom type docsQosServiceClassTosAndMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosServiceClassTosAndMask_Type.__name__ = "OctetString"
_DocsQosServiceClassTosAndMask_Object = MibTableColumn
docsQosServiceClassTosAndMask = _DocsQosServiceClassTosAndMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 21),
    _DocsQosServiceClassTosAndMask_Type()
)
docsQosServiceClassTosAndMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassTosAndMask.setStatus("current")


class _DocsQosServiceClassTosOrMask_Type(OctetString):
    """Custom type docsQosServiceClassTosOrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsQosServiceClassTosOrMask_Type.__name__ = "OctetString"
_DocsQosServiceClassTosOrMask_Object = MibTableColumn
docsQosServiceClassTosOrMask = _DocsQosServiceClassTosOrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 22),
    _DocsQosServiceClassTosOrMask_Type()
)
docsQosServiceClassTosOrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassTosOrMask.setStatus("current")


class _DocsQosServiceClassDirection_Type(IfDirection):
    """Custom type docsQosServiceClassDirection based on IfDirection"""


_DocsQosServiceClassDirection_Object = MibTableColumn
docsQosServiceClassDirection = _DocsQosServiceClassDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 23),
    _DocsQosServiceClassDirection_Type()
)
docsQosServiceClassDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassDirection.setStatus("current")


class _DocsQosServiceClassStorageType_Type(StorageType):
    """Custom type docsQosServiceClassStorageType based on StorageType"""


_DocsQosServiceClassStorageType_Object = MibTableColumn
docsQosServiceClassStorageType = _DocsQosServiceClassStorageType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 24),
    _DocsQosServiceClassStorageType_Type()
)
docsQosServiceClassStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassStorageType.setStatus("current")


class _DocsQosServiceClassDSCPOverwrite_Type(DscpOrAny):
    """Custom type docsQosServiceClassDSCPOverwrite based on DscpOrAny"""
    defaultValue = -1


_DocsQosServiceClassDSCPOverwrite_Object = MibTableColumn
docsQosServiceClassDSCPOverwrite = _DocsQosServiceClassDSCPOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 25),
    _DocsQosServiceClassDSCPOverwrite_Type()
)
docsQosServiceClassDSCPOverwrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassDSCPOverwrite.setStatus("current")


class _DocsQosServiceClassRequiredAttrMask_Type(AttributeMask):
    """Custom type docsQosServiceClassRequiredAttrMask based on AttributeMask"""
    defaultHexValue = "000"


_DocsQosServiceClassRequiredAttrMask_Object = MibTableColumn
docsQosServiceClassRequiredAttrMask = _DocsQosServiceClassRequiredAttrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 26),
    _DocsQosServiceClassRequiredAttrMask_Type()
)
docsQosServiceClassRequiredAttrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassRequiredAttrMask.setStatus("current")


class _DocsQosServiceClassForbiddenAttrMask_Type(AttributeMask):
    """Custom type docsQosServiceClassForbiddenAttrMask based on AttributeMask"""
    defaultHexValue = "000"


_DocsQosServiceClassForbiddenAttrMask_Object = MibTableColumn
docsQosServiceClassForbiddenAttrMask = _DocsQosServiceClassForbiddenAttrMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 27),
    _DocsQosServiceClassForbiddenAttrMask_Type()
)
docsQosServiceClassForbiddenAttrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassForbiddenAttrMask.setStatus("current")


class _DocsQosServiceClassAttrAggrRuleMask_Type(AttrAggrRuleMask):
    """Custom type docsQosServiceClassAttrAggrRuleMask based on AttrAggrRuleMask"""
    defaultHexValue = "00000000"


_DocsQosServiceClassAttrAggrRuleMask_Object = MibTableColumn
docsQosServiceClassAttrAggrRuleMask = _DocsQosServiceClassAttrAggrRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 28),
    _DocsQosServiceClassAttrAggrRuleMask_Type()
)
docsQosServiceClassAttrAggrRuleMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassAttrAggrRuleMask.setStatus("current")
_DocsQosServiceClassAppId_Type = Unsigned32
_DocsQosServiceClassAppId_Object = MibTableColumn
docsQosServiceClassAppId = _DocsQosServiceClassAppId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 29),
    _DocsQosServiceClassAppId_Type()
)
docsQosServiceClassAppId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassAppId.setStatus("current")


class _DocsQosServiceClassMultiplierContentionReqWindow_Type(Unsigned32):
    """Custom type docsQosServiceClassMultiplierContentionReqWindow based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 12),
    )


_DocsQosServiceClassMultiplierContentionReqWindow_Type.__name__ = "Unsigned32"
_DocsQosServiceClassMultiplierContentionReqWindow_Object = MibTableColumn
docsQosServiceClassMultiplierContentionReqWindow = _DocsQosServiceClassMultiplierContentionReqWindow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 30),
    _DocsQosServiceClassMultiplierContentionReqWindow_Type()
)
docsQosServiceClassMultiplierContentionReqWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMultiplierContentionReqWindow.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMultiplierContentionReqWindow.setUnits("eighths")


class _DocsQosServiceClassMultiplierBytesReq_Type(Unsigned32):
    """Custom type docsQosServiceClassMultiplierBytesReq based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
    )


_DocsQosServiceClassMultiplierBytesReq_Type.__name__ = "Unsigned32"
_DocsQosServiceClassMultiplierBytesReq_Object = MibTableColumn
docsQosServiceClassMultiplierBytesReq = _DocsQosServiceClassMultiplierBytesReq_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 31),
    _DocsQosServiceClassMultiplierBytesReq_Type()
)
docsQosServiceClassMultiplierBytesReq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMultiplierBytesReq.setStatus("current")


class _DocsQosServiceClassMaxReqPerSidCluster_Type(Unsigned32):
    """Custom type docsQosServiceClassMaxReqPerSidCluster based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosServiceClassMaxReqPerSidCluster_Type.__name__ = "Unsigned32"
_DocsQosServiceClassMaxReqPerSidCluster_Object = MibTableColumn
docsQosServiceClassMaxReqPerSidCluster = _DocsQosServiceClassMaxReqPerSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 32),
    _DocsQosServiceClassMaxReqPerSidCluster_Type()
)
docsQosServiceClassMaxReqPerSidCluster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxReqPerSidCluster.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxReqPerSidCluster.setUnits("requests")


class _DocsQosServiceClassMaxOutstandingBytesPerSidCluster_Type(Unsigned32):
    """Custom type docsQosServiceClassMaxOutstandingBytesPerSidCluster based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassMaxOutstandingBytesPerSidCluster_Object = MibTableColumn
docsQosServiceClassMaxOutstandingBytesPerSidCluster = _DocsQosServiceClassMaxOutstandingBytesPerSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 33),
    _DocsQosServiceClassMaxOutstandingBytesPerSidCluster_Type()
)
docsQosServiceClassMaxOutstandingBytesPerSidCluster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxOutstandingBytesPerSidCluster.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxOutstandingBytesPerSidCluster.setUnits("bytes")


class _DocsQosServiceClassMaxTotBytesReqPerSidCluster_Type(Unsigned32):
    """Custom type docsQosServiceClassMaxTotBytesReqPerSidCluster based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassMaxTotBytesReqPerSidCluster_Object = MibTableColumn
docsQosServiceClassMaxTotBytesReqPerSidCluster = _DocsQosServiceClassMaxTotBytesReqPerSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 34),
    _DocsQosServiceClassMaxTotBytesReqPerSidCluster_Type()
)
docsQosServiceClassMaxTotBytesReqPerSidCluster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTotBytesReqPerSidCluster.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTotBytesReqPerSidCluster.setUnits("bytes")


class _DocsQosServiceClassMaxTimeInSidCluster_Type(Unsigned32):
    """Custom type docsQosServiceClassMaxTimeInSidCluster based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosServiceClassMaxTimeInSidCluster_Type.__name__ = "Unsigned32"
_DocsQosServiceClassMaxTimeInSidCluster_Object = MibTableColumn
docsQosServiceClassMaxTimeInSidCluster = _DocsQosServiceClassMaxTimeInSidCluster_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 35),
    _DocsQosServiceClassMaxTimeInSidCluster_Type()
)
docsQosServiceClassMaxTimeInSidCluster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTimeInSidCluster.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsQosServiceClassMaxTimeInSidCluster.setUnits("milliseconds")


class _DocsQosServiceClassPeakTrafficRate_Type(Unsigned32):
    """Custom type docsQosServiceClassPeakTrafficRate based on Unsigned32"""
    defaultValue = 0


_DocsQosServiceClassPeakTrafficRate_Object = MibTableColumn
docsQosServiceClassPeakTrafficRate = _DocsQosServiceClassPeakTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 36),
    _DocsQosServiceClassPeakTrafficRate_Type()
)
docsQosServiceClassPeakTrafficRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassPeakTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassPeakTrafficRate.setUnits("bps")


class _DocsQosServiceClassDsResequencing_Type(Integer32):
    """Custom type docsQosServiceClassDsResequencing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noResequencingDsid", 1),
          ("resequencingDsid", 0))
    )


_DocsQosServiceClassDsResequencing_Type.__name__ = "Integer32"
_DocsQosServiceClassDsResequencing_Object = MibTableColumn
docsQosServiceClassDsResequencing = _DocsQosServiceClassDsResequencing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 37),
    _DocsQosServiceClassDsResequencing_Type()
)
docsQosServiceClassDsResequencing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassDsResequencing.setStatus("current")


class _DocsQosServiceClassMinimumBuffer_Type(Unsigned32):
    """Custom type docsQosServiceClassMinimumBuffer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosServiceClassMinimumBuffer_Type.__name__ = "Unsigned32"
_DocsQosServiceClassMinimumBuffer_Object = MibTableColumn
docsQosServiceClassMinimumBuffer = _DocsQosServiceClassMinimumBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 38),
    _DocsQosServiceClassMinimumBuffer_Type()
)
docsQosServiceClassMinimumBuffer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMinimumBuffer.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMinimumBuffer.setUnits("bytes")


class _DocsQosServiceClassTargetBuffer_Type(Unsigned32):
    """Custom type docsQosServiceClassTargetBuffer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosServiceClassTargetBuffer_Type.__name__ = "Unsigned32"
_DocsQosServiceClassTargetBuffer_Object = MibTableColumn
docsQosServiceClassTargetBuffer = _DocsQosServiceClassTargetBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 39),
    _DocsQosServiceClassTargetBuffer_Type()
)
docsQosServiceClassTargetBuffer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassTargetBuffer.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassTargetBuffer.setUnits("bytes")


class _DocsQosServiceClassMaximumBuffer_Type(Unsigned32):
    """Custom type docsQosServiceClassMaximumBuffer based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DocsQosServiceClassMaximumBuffer_Type.__name__ = "Unsigned32"
_DocsQosServiceClassMaximumBuffer_Object = MibTableColumn
docsQosServiceClassMaximumBuffer = _DocsQosServiceClassMaximumBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 40),
    _DocsQosServiceClassMaximumBuffer_Type()
)
docsQosServiceClassMaximumBuffer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosServiceClassMaximumBuffer.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassMaximumBuffer.setUnits("bytes")
_DocsQosServiceClassAqmDisabled_Type = TruthValue
_DocsQosServiceClassAqmDisabled_Object = MibTableColumn
docsQosServiceClassAqmDisabled = _DocsQosServiceClassAqmDisabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 42),
    _DocsQosServiceClassAqmDisabled_Type()
)
docsQosServiceClassAqmDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceClassAqmDisabled.setStatus("current")


class _DocsQosServiceClassAqmLatencyTarget_Type(Unsigned32):
    """Custom type docsQosServiceClassAqmLatencyTarget based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_DocsQosServiceClassAqmLatencyTarget_Type.__name__ = "Unsigned32"
_DocsQosServiceClassAqmLatencyTarget_Object = MibTableColumn
docsQosServiceClassAqmLatencyTarget = _DocsQosServiceClassAqmLatencyTarget_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 43),
    _DocsQosServiceClassAqmLatencyTarget_Type()
)
docsQosServiceClassAqmLatencyTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceClassAqmLatencyTarget.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassAqmLatencyTarget.setUnits("milliseconds")
_DocsQosServiceClassHCMaxTrafficRate_Type = CounterBasedGauge64
_DocsQosServiceClassHCMaxTrafficRate_Object = MibTableColumn
docsQosServiceClassHCMaxTrafficRate = _DocsQosServiceClassHCMaxTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 44),
    _DocsQosServiceClassHCMaxTrafficRate_Type()
)
docsQosServiceClassHCMaxTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceClassHCMaxTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassHCMaxTrafficRate.setUnits("bps")
_DocsQosServiceClassHCMinReservedRate_Type = CounterBasedGauge64
_DocsQosServiceClassHCMinReservedRate_Object = MibTableColumn
docsQosServiceClassHCMinReservedRate = _DocsQosServiceClassHCMinReservedRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 45),
    _DocsQosServiceClassHCMinReservedRate_Type()
)
docsQosServiceClassHCMinReservedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceClassHCMinReservedRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassHCMinReservedRate.setUnits("bps")
_DocsQosServiceClassHCPeakTrafficRate_Type = CounterBasedGauge64
_DocsQosServiceClassHCPeakTrafficRate_Object = MibTableColumn
docsQosServiceClassHCPeakTrafficRate = _DocsQosServiceClassHCPeakTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 8, 1, 46),
    _DocsQosServiceClassHCPeakTrafficRate_Type()
)
docsQosServiceClassHCPeakTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceClassHCPeakTrafficRate.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceClassHCPeakTrafficRate.setUnits("bps")
_DocsQosPHSTable_Object = MibTable
docsQosPHSTable = _DocsQosPHSTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 10)
)
if mibBuilder.loadTexts:
    docsQosPHSTable.setStatus("obsolete")
_DocsQosPHSEntry_Object = MibTableRow
docsQosPHSEntry = _DocsQosPHSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 10, 1)
)
docsQosPHSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS3-MIB", "docsQosPktClassId"),
)
if mibBuilder.loadTexts:
    docsQosPHSEntry.setStatus("obsolete")


class _DocsQosPHSField_Type(OctetString):
    """Custom type docsQosPHSField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DocsQosPHSField_Type.__name__ = "OctetString"
_DocsQosPHSField_Object = MibTableColumn
docsQosPHSField = _DocsQosPHSField_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 10, 1, 2),
    _DocsQosPHSField_Type()
)
docsQosPHSField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSField.setStatus("obsolete")


class _DocsQosPHSMask_Type(OctetString):
    """Custom type docsQosPHSMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsQosPHSMask_Type.__name__ = "OctetString"
_DocsQosPHSMask_Object = MibTableColumn
docsQosPHSMask = _DocsQosPHSMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 10, 1, 3),
    _DocsQosPHSMask_Type()
)
docsQosPHSMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSMask.setStatus("obsolete")


class _DocsQosPHSSize_Type(Unsigned32):
    """Custom type docsQosPHSSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsQosPHSSize_Type.__name__ = "Unsigned32"
_DocsQosPHSSize_Object = MibTableColumn
docsQosPHSSize = _DocsQosPHSSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 10, 1, 4),
    _DocsQosPHSSize_Type()
)
docsQosPHSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    docsQosPHSSize.setUnits("bytes")
_DocsQosPHSVerify_Type = TruthValue
_DocsQosPHSVerify_Object = MibTableColumn
docsQosPHSVerify = _DocsQosPHSVerify_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 10, 1, 5),
    _DocsQosPHSVerify_Type()
)
docsQosPHSVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSVerify.setStatus("obsolete")


class _DocsQosPHSIndex_Type(Unsigned32):
    """Custom type docsQosPHSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsQosPHSIndex_Type.__name__ = "Unsigned32"
_DocsQosPHSIndex_Object = MibTableColumn
docsQosPHSIndex = _DocsQosPHSIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 10, 1, 7),
    _DocsQosPHSIndex_Type()
)
docsQosPHSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosPHSIndex.setStatus("obsolete")
_DocsQosCmtsMacToSrvFlowTable_Object = MibTable
docsQosCmtsMacToSrvFlowTable = _DocsQosCmtsMacToSrvFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 11)
)
if mibBuilder.loadTexts:
    docsQosCmtsMacToSrvFlowTable.setStatus("current")
_DocsQosCmtsMacToSrvFlowEntry_Object = MibTableRow
docsQosCmtsMacToSrvFlowEntry = _DocsQosCmtsMacToSrvFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 11, 1)
)
docsQosCmtsMacToSrvFlowEntry.setIndexNames(
    (0, "DOCS-QOS3-MIB", "docsQosCmtsCmMac"),
    (0, "DOCS-QOS3-MIB", "docsQosCmtsServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosCmtsMacToSrvFlowEntry.setStatus("current")
_DocsQosCmtsCmMac_Type = MacAddress
_DocsQosCmtsCmMac_Object = MibTableColumn
docsQosCmtsCmMac = _DocsQosCmtsCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 11, 1, 1),
    _DocsQosCmtsCmMac_Type()
)
docsQosCmtsCmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmtsCmMac.setStatus("current")


class _DocsQosCmtsServiceFlowId_Type(Unsigned32):
    """Custom type docsQosCmtsServiceFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsQosCmtsServiceFlowId_Type.__name__ = "Unsigned32"
_DocsQosCmtsServiceFlowId_Object = MibTableColumn
docsQosCmtsServiceFlowId = _DocsQosCmtsServiceFlowId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 11, 1, 2),
    _DocsQosCmtsServiceFlowId_Type()
)
docsQosCmtsServiceFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmtsServiceFlowId.setStatus("current")
_DocsQosCmtsIfIndex_Type = InterfaceIndex
_DocsQosCmtsIfIndex_Object = MibTableColumn
docsQosCmtsIfIndex = _DocsQosCmtsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 11, 1, 3),
    _DocsQosCmtsIfIndex_Type()
)
docsQosCmtsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsIfIndex.setStatus("current")
_DocsQosServiceFlowSidClusterTable_Object = MibTable
docsQosServiceFlowSidClusterTable = _DocsQosServiceFlowSidClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 12)
)
if mibBuilder.loadTexts:
    docsQosServiceFlowSidClusterTable.setStatus("current")
_DocsQosServiceFlowSidClusterEntry_Object = MibTableRow
docsQosServiceFlowSidClusterEntry = _DocsQosServiceFlowSidClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 12, 1)
)
docsQosServiceFlowSidClusterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowSidClusterId"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowSidClusterUcid"),
)
if mibBuilder.loadTexts:
    docsQosServiceFlowSidClusterEntry.setStatus("current")


class _DocsQosServiceFlowSidClusterId_Type(Unsigned32):
    """Custom type docsQosServiceFlowSidClusterId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DocsQosServiceFlowSidClusterId_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowSidClusterId_Object = MibTableColumn
docsQosServiceFlowSidClusterId = _DocsQosServiceFlowSidClusterId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 12, 1, 1),
    _DocsQosServiceFlowSidClusterId_Type()
)
docsQosServiceFlowSidClusterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosServiceFlowSidClusterId.setStatus("current")


class _DocsQosServiceFlowSidClusterUcid_Type(ChId):
    """Custom type docsQosServiceFlowSidClusterUcid based on ChId"""
    subtypeSpec = ChId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DocsQosServiceFlowSidClusterUcid_Type.__name__ = "ChId"
_DocsQosServiceFlowSidClusterUcid_Object = MibTableColumn
docsQosServiceFlowSidClusterUcid = _DocsQosServiceFlowSidClusterUcid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 12, 1, 2),
    _DocsQosServiceFlowSidClusterUcid_Type()
)
docsQosServiceFlowSidClusterUcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosServiceFlowSidClusterUcid.setStatus("current")


class _DocsQosServiceFlowSidClusterSid_Type(Unsigned32):
    """Custom type docsQosServiceFlowSidClusterSid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_DocsQosServiceFlowSidClusterSid_Type.__name__ = "Unsigned32"
_DocsQosServiceFlowSidClusterSid_Object = MibTableColumn
docsQosServiceFlowSidClusterSid = _DocsQosServiceFlowSidClusterSid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 12, 1, 3),
    _DocsQosServiceFlowSidClusterSid_Type()
)
docsQosServiceFlowSidClusterSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowSidClusterSid.setStatus("current")
_DocsQosGrpServiceFlowTable_Object = MibTable
docsQosGrpServiceFlowTable = _DocsQosGrpServiceFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 13)
)
if mibBuilder.loadTexts:
    docsQosGrpServiceFlowTable.setStatus("current")
_DocsQosGrpServiceFlowEntry_Object = MibTableRow
docsQosGrpServiceFlowEntry = _DocsQosGrpServiceFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 13, 1)
)
docsQosGrpServiceFlowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosGrpServiceFlowEntry.setStatus("current")
_DocsQosGrpServiceFlowIsDef_Type = TruthValue
_DocsQosGrpServiceFlowIsDef_Object = MibTableColumn
docsQosGrpServiceFlowIsDef = _DocsQosGrpServiceFlowIsDef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 13, 1, 1),
    _DocsQosGrpServiceFlowIsDef_Type()
)
docsQosGrpServiceFlowIsDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosGrpServiceFlowIsDef.setStatus("current")


class _DocsQosGrpServiceFlowQosConfigId_Type(Unsigned32):
    """Custom type docsQosGrpServiceFlowQosConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosGrpServiceFlowQosConfigId_Type.__name__ = "Unsigned32"
_DocsQosGrpServiceFlowQosConfigId_Object = MibTableColumn
docsQosGrpServiceFlowQosConfigId = _DocsQosGrpServiceFlowQosConfigId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 13, 1, 2),
    _DocsQosGrpServiceFlowQosConfigId_Type()
)
docsQosGrpServiceFlowQosConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosGrpServiceFlowQosConfigId.setStatus("current")


class _DocsQosGrpServiceFlowNumSess_Type(Unsigned32):
    """Custom type docsQosGrpServiceFlowNumSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsQosGrpServiceFlowNumSess_Type.__name__ = "Unsigned32"
_DocsQosGrpServiceFlowNumSess_Object = MibTableColumn
docsQosGrpServiceFlowNumSess = _DocsQosGrpServiceFlowNumSess_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 13, 1, 3),
    _DocsQosGrpServiceFlowNumSess_Type()
)
docsQosGrpServiceFlowNumSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosGrpServiceFlowNumSess.setStatus("current")
if mibBuilder.loadTexts:
    docsQosGrpServiceFlowNumSess.setUnits("sessions")
_DocsQosGrpServiceFlowSrcAddr_Type = InetAddress
_DocsQosGrpServiceFlowSrcAddr_Object = MibTableColumn
docsQosGrpServiceFlowSrcAddr = _DocsQosGrpServiceFlowSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 13, 1, 4),
    _DocsQosGrpServiceFlowSrcAddr_Type()
)
docsQosGrpServiceFlowSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosGrpServiceFlowSrcAddr.setStatus("current")
_DocsQosGrpServiceFlowGrpAddr_Type = InetAddress
_DocsQosGrpServiceFlowGrpAddr_Object = MibTableColumn
docsQosGrpServiceFlowGrpAddr = _DocsQosGrpServiceFlowGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 13, 1, 5),
    _DocsQosGrpServiceFlowGrpAddr_Type()
)
docsQosGrpServiceFlowGrpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosGrpServiceFlowGrpAddr.setStatus("current")
_DocsQosGrpServiceFlowAddrType_Type = InetAddressType
_DocsQosGrpServiceFlowAddrType_Object = MibTableColumn
docsQosGrpServiceFlowAddrType = _DocsQosGrpServiceFlowAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 13, 1, 6),
    _DocsQosGrpServiceFlowAddrType_Type()
)
docsQosGrpServiceFlowAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosGrpServiceFlowAddrType.setStatus("current")
_DocsQosGrpPktClassTable_Object = MibTable
docsQosGrpPktClassTable = _DocsQosGrpPktClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 14)
)
if mibBuilder.loadTexts:
    docsQosGrpPktClassTable.setStatus("current")
_DocsQosGrpPktClassEntry_Object = MibTableRow
docsQosGrpPktClassEntry = _DocsQosGrpPktClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 14, 1)
)
docsQosGrpPktClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
    (0, "DOCS-QOS3-MIB", "docsQosPktClassId"),
)
if mibBuilder.loadTexts:
    docsQosGrpPktClassEntry.setStatus("current")


class _DocsQosGrpPktClassGrpConfigId_Type(Unsigned32):
    """Custom type docsQosGrpPktClassGrpConfigId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_DocsQosGrpPktClassGrpConfigId_Type.__name__ = "Unsigned32"
_DocsQosGrpPktClassGrpConfigId_Object = MibTableColumn
docsQosGrpPktClassGrpConfigId = _DocsQosGrpPktClassGrpConfigId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 14, 1, 1),
    _DocsQosGrpPktClassGrpConfigId_Type()
)
docsQosGrpPktClassGrpConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosGrpPktClassGrpConfigId.setStatus("current")
_DocsQosUpChCounterExtTable_Object = MibTable
docsQosUpChCounterExtTable = _DocsQosUpChCounterExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 15)
)
if mibBuilder.loadTexts:
    docsQosUpChCounterExtTable.setStatus("current")
_DocsQosUpChCounterExtEntry_Object = MibTableRow
docsQosUpChCounterExtEntry = _DocsQosUpChCounterExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 15, 1)
)
docsQosUpChCounterExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsQosUpChCounterExtEntry.setStatus("current")
_DocsQosUpChCounterExtSgmtValids_Type = Counter32
_DocsQosUpChCounterExtSgmtValids_Object = MibTableColumn
docsQosUpChCounterExtSgmtValids = _DocsQosUpChCounterExtSgmtValids_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 15, 1, 1),
    _DocsQosUpChCounterExtSgmtValids_Type()
)
docsQosUpChCounterExtSgmtValids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosUpChCounterExtSgmtValids.setStatus("current")
if mibBuilder.loadTexts:
    docsQosUpChCounterExtSgmtValids.setUnits("segments")
_DocsQosUpChCounterExtSgmtDiscards_Type = Counter32
_DocsQosUpChCounterExtSgmtDiscards_Object = MibTableColumn
docsQosUpChCounterExtSgmtDiscards = _DocsQosUpChCounterExtSgmtDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 15, 1, 2),
    _DocsQosUpChCounterExtSgmtDiscards_Type()
)
docsQosUpChCounterExtSgmtDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosUpChCounterExtSgmtDiscards.setStatus("current")
if mibBuilder.loadTexts:
    docsQosUpChCounterExtSgmtDiscards.setUnits("segments")
_DocsQosServiceFlowCcfStatsTable_Object = MibTable
docsQosServiceFlowCcfStatsTable = _DocsQosServiceFlowCcfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 16)
)
if mibBuilder.loadTexts:
    docsQosServiceFlowCcfStatsTable.setStatus("current")
_DocsQosServiceFlowCcfStatsEntry_Object = MibTableRow
docsQosServiceFlowCcfStatsEntry = _DocsQosServiceFlowCcfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 16, 1)
)
docsQosServiceFlowCcfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosServiceFlowCcfStatsEntry.setStatus("current")
_DocsQosServiceFlowCcfStatsSgmtValids_Type = Counter32
_DocsQosServiceFlowCcfStatsSgmtValids_Object = MibTableColumn
docsQosServiceFlowCcfStatsSgmtValids = _DocsQosServiceFlowCcfStatsSgmtValids_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 16, 1, 1),
    _DocsQosServiceFlowCcfStatsSgmtValids_Type()
)
docsQosServiceFlowCcfStatsSgmtValids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowCcfStatsSgmtValids.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowCcfStatsSgmtValids.setUnits("segments")
_DocsQosServiceFlowCcfStatsSgmtLost_Type = Counter32
_DocsQosServiceFlowCcfStatsSgmtLost_Object = MibTableColumn
docsQosServiceFlowCcfStatsSgmtLost = _DocsQosServiceFlowCcfStatsSgmtLost_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 16, 1, 2),
    _DocsQosServiceFlowCcfStatsSgmtLost_Type()
)
docsQosServiceFlowCcfStatsSgmtLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosServiceFlowCcfStatsSgmtLost.setStatus("current")
if mibBuilder.loadTexts:
    docsQosServiceFlowCcfStatsSgmtLost.setUnits("segments")
_DocsQosCmServiceUsStatsTable_Object = MibTable
docsQosCmServiceUsStatsTable = _DocsQosCmServiceUsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 17)
)
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsTable.setStatus("current")
_DocsQosCmServiceUsStatsEntry_Object = MibTableRow
docsQosCmServiceUsStatsEntry = _DocsQosCmServiceUsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 17, 1)
)
docsQosCmServiceUsStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceFlowId"),
)
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsEntry.setStatus("current")
_DocsQosCmServiceUsStatsTxSlotsImmed_Type = Counter32
_DocsQosCmServiceUsStatsTxSlotsImmed_Object = MibTableColumn
docsQosCmServiceUsStatsTxSlotsImmed = _DocsQosCmServiceUsStatsTxSlotsImmed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 17, 1, 1),
    _DocsQosCmServiceUsStatsTxSlotsImmed_Type()
)
docsQosCmServiceUsStatsTxSlotsImmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsTxSlotsImmed.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsTxSlotsImmed.setUnits("mini-slots")
_DocsQosCmServiceUsStatsTxSlotsDed_Type = Counter32
_DocsQosCmServiceUsStatsTxSlotsDed_Object = MibTableColumn
docsQosCmServiceUsStatsTxSlotsDed = _DocsQosCmServiceUsStatsTxSlotsDed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 17, 1, 2),
    _DocsQosCmServiceUsStatsTxSlotsDed_Type()
)
docsQosCmServiceUsStatsTxSlotsDed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsTxSlotsDed.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsTxSlotsDed.setUnits("mini-slots")
_DocsQosCmServiceUsStatsTxRetries_Type = Counter32
_DocsQosCmServiceUsStatsTxRetries_Object = MibTableColumn
docsQosCmServiceUsStatsTxRetries = _DocsQosCmServiceUsStatsTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 17, 1, 3),
    _DocsQosCmServiceUsStatsTxRetries_Type()
)
docsQosCmServiceUsStatsTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsTxRetries.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsTxRetries.setUnits("attempts")
_DocsQosCmServiceUsStatsTxExceededs_Type = Counter32
_DocsQosCmServiceUsStatsTxExceededs_Object = MibTableColumn
docsQosCmServiceUsStatsTxExceededs = _DocsQosCmServiceUsStatsTxExceededs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 17, 1, 4),
    _DocsQosCmServiceUsStatsTxExceededs_Type()
)
docsQosCmServiceUsStatsTxExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsTxExceededs.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsTxExceededs.setUnits("attempts")
_DocsQosCmServiceUsStatsRqRetries_Type = Counter32
_DocsQosCmServiceUsStatsRqRetries_Object = MibTableColumn
docsQosCmServiceUsStatsRqRetries = _DocsQosCmServiceUsStatsRqRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 17, 1, 5),
    _DocsQosCmServiceUsStatsRqRetries_Type()
)
docsQosCmServiceUsStatsRqRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsRqRetries.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsRqRetries.setUnits("attempts")
_DocsQosCmServiceUsStatsRqExceededs_Type = Counter32
_DocsQosCmServiceUsStatsRqExceededs_Object = MibTableColumn
docsQosCmServiceUsStatsRqExceededs = _DocsQosCmServiceUsStatsRqExceededs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 17, 1, 6),
    _DocsQosCmServiceUsStatsRqExceededs_Type()
)
docsQosCmServiceUsStatsRqExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsRqExceededs.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsRqExceededs.setUnits("attempts")
_DocsQosCmServiceUsStatsSgmts_Type = Counter32
_DocsQosCmServiceUsStatsSgmts_Object = MibTableColumn
docsQosCmServiceUsStatsSgmts = _DocsQosCmServiceUsStatsSgmts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 17, 1, 7),
    _DocsQosCmServiceUsStatsSgmts_Type()
)
docsQosCmServiceUsStatsSgmts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsSgmts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmServiceUsStatsSgmts.setUnits("segments")
_DocsQosCmtsDsidTable_Object = MibTable
docsQosCmtsDsidTable = _DocsQosCmtsDsidTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 18)
)
if mibBuilder.loadTexts:
    docsQosCmtsDsidTable.setStatus("current")
_DocsQosCmtsDsidEntry_Object = MibTableRow
docsQosCmtsDsidEntry = _DocsQosCmtsDsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 18, 1)
)
docsQosCmtsDsidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosCmtsDsidDsid"),
)
if mibBuilder.loadTexts:
    docsQosCmtsDsidEntry.setStatus("current")
_DocsQosCmtsDsidDsid_Type = Dsid
_DocsQosCmtsDsidDsid_Object = MibTableColumn
docsQosCmtsDsidDsid = _DocsQosCmtsDsidDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 18, 1, 1),
    _DocsQosCmtsDsidDsid_Type()
)
docsQosCmtsDsidDsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmtsDsidDsid.setStatus("current")


class _DocsQosCmtsDsidUsage_Type(Bits):
    """Custom type docsQosCmtsDsidUsage based on Bits"""
    namedValues = NamedValues(
        *(("bonding", 3),
          ("multicastCapable", 1),
          ("multicastReplication", 2),
          ("resequencing", 0))
    )

_DocsQosCmtsDsidUsage_Type.__name__ = "Bits"
_DocsQosCmtsDsidUsage_Object = MibTableColumn
docsQosCmtsDsidUsage = _DocsQosCmtsDsidUsage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 18, 1, 2),
    _DocsQosCmtsDsidUsage_Type()
)
docsQosCmtsDsidUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsDsidUsage.setStatus("current")
_DocsQosCmtsDsidDsChSet_Type = ChSetId
_DocsQosCmtsDsidDsChSet_Object = MibTableColumn
docsQosCmtsDsidDsChSet = _DocsQosCmtsDsidDsChSet_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 18, 1, 3),
    _DocsQosCmtsDsidDsChSet_Type()
)
docsQosCmtsDsidDsChSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsDsidDsChSet.setStatus("current")


class _DocsQosCmtsDsidReseqWaitTime_Type(Unsigned32):
    """Custom type docsQosCmtsDsidReseqWaitTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 180),
    )


_DocsQosCmtsDsidReseqWaitTime_Type.__name__ = "Unsigned32"
_DocsQosCmtsDsidReseqWaitTime_Object = MibTableColumn
docsQosCmtsDsidReseqWaitTime = _DocsQosCmtsDsidReseqWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 18, 1, 4),
    _DocsQosCmtsDsidReseqWaitTime_Type()
)
docsQosCmtsDsidReseqWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsDsidReseqWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmtsDsidReseqWaitTime.setUnits("hundredMicroseconds")


class _DocsQosCmtsDsidReseqWarnThrshld_Type(Unsigned32):
    """Custom type docsQosCmtsDsidReseqWarnThrshld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 179),
    )


_DocsQosCmtsDsidReseqWarnThrshld_Type.__name__ = "Unsigned32"
_DocsQosCmtsDsidReseqWarnThrshld_Object = MibTableColumn
docsQosCmtsDsidReseqWarnThrshld = _DocsQosCmtsDsidReseqWarnThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 18, 1, 5),
    _DocsQosCmtsDsidReseqWarnThrshld_Type()
)
docsQosCmtsDsidReseqWarnThrshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsDsidReseqWarnThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmtsDsidReseqWarnThrshld.setUnits("hundredMicroseconds")


class _DocsQosCmtsDsidStatusHldoffTimerSeqOutOfRng_Type(Unsigned32):
    """Custom type docsQosCmtsDsidStatusHldoffTimerSeqOutOfRng based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosCmtsDsidStatusHldoffTimerSeqOutOfRng_Type.__name__ = "Unsigned32"
_DocsQosCmtsDsidStatusHldoffTimerSeqOutOfRng_Object = MibTableColumn
docsQosCmtsDsidStatusHldoffTimerSeqOutOfRng = _DocsQosCmtsDsidStatusHldoffTimerSeqOutOfRng_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 18, 1, 6),
    _DocsQosCmtsDsidStatusHldoffTimerSeqOutOfRng_Type()
)
docsQosCmtsDsidStatusHldoffTimerSeqOutOfRng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsDsidStatusHldoffTimerSeqOutOfRng.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmtsDsidStatusHldoffTimerSeqOutOfRng.setUnits("20milliseconds")


class _DocsQosCmtsDsidCurrentSeqNum_Type(Unsigned32):
    """Custom type docsQosCmtsDsidCurrentSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosCmtsDsidCurrentSeqNum_Type.__name__ = "Unsigned32"
_DocsQosCmtsDsidCurrentSeqNum_Object = MibTableColumn
docsQosCmtsDsidCurrentSeqNum = _DocsQosCmtsDsidCurrentSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 18, 1, 7),
    _DocsQosCmtsDsidCurrentSeqNum_Type()
)
docsQosCmtsDsidCurrentSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsDsidCurrentSeqNum.setStatus("current")
_DocsQosCmtsDebugDsidTable_Object = MibTable
docsQosCmtsDebugDsidTable = _DocsQosCmtsDebugDsidTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 19)
)
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidTable.setStatus("current")
_DocsQosCmtsDebugDsidEntry_Object = MibTableRow
docsQosCmtsDebugDsidEntry = _DocsQosCmtsDebugDsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 19, 1)
)
docsQosCmtsDebugDsidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosCmtsDebugDsidDsid"),
)
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidEntry.setStatus("current")
_DocsQosCmtsDebugDsidDsid_Type = Dsid
_DocsQosCmtsDebugDsidDsid_Object = MibTableColumn
docsQosCmtsDebugDsidDsid = _DocsQosCmtsDebugDsidDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 19, 1, 1),
    _DocsQosCmtsDebugDsidDsid_Type()
)
docsQosCmtsDebugDsidDsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidDsid.setStatus("current")
_DocsQosCmtsDebugDsidRowStatus_Type = RowStatus
_DocsQosCmtsDebugDsidRowStatus_Object = MibTableColumn
docsQosCmtsDebugDsidRowStatus = _DocsQosCmtsDebugDsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 19, 1, 2),
    _DocsQosCmtsDebugDsidRowStatus_Type()
)
docsQosCmtsDebugDsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidRowStatus.setStatus("current")
_DocsQosCmtsDebugDsidStatsTable_Object = MibTable
docsQosCmtsDebugDsidStatsTable = _DocsQosCmtsDebugDsidStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 20)
)
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidStatsTable.setStatus("current")
_DocsQosCmtsDebugDsidStatsEntry_Object = MibTableRow
docsQosCmtsDebugDsidStatsEntry = _DocsQosCmtsDebugDsidStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 20, 1)
)
docsQosCmtsDebugDsidStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosCmtsDebugDsidDsid"),
    (0, "DOCS-QOS3-MIB", "docsQosCmtsDebugDsidStatsDsIfIndex"),
)
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidStatsEntry.setStatus("current")
_DocsQosCmtsDebugDsidStatsDsIfIndex_Type = InterfaceIndex
_DocsQosCmtsDebugDsidStatsDsIfIndex_Object = MibTableColumn
docsQosCmtsDebugDsidStatsDsIfIndex = _DocsQosCmtsDebugDsidStatsDsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 20, 1, 1),
    _DocsQosCmtsDebugDsidStatsDsIfIndex_Type()
)
docsQosCmtsDebugDsidStatsDsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidStatsDsIfIndex.setStatus("current")
_DocsQosCmtsDebugDsidStatsDsidPackets_Type = Counter64
_DocsQosCmtsDebugDsidStatsDsidPackets_Object = MibTableColumn
docsQosCmtsDebugDsidStatsDsidPackets = _DocsQosCmtsDebugDsidStatsDsidPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 20, 1, 2),
    _DocsQosCmtsDebugDsidStatsDsidPackets_Type()
)
docsQosCmtsDebugDsidStatsDsidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidStatsDsidPackets.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidStatsDsidPackets.setUnits("packets")
_DocsQosCmtsDebugDsidStatsDsidOctets_Type = Counter64
_DocsQosCmtsDebugDsidStatsDsidOctets_Object = MibTableColumn
docsQosCmtsDebugDsidStatsDsidOctets = _DocsQosCmtsDebugDsidStatsDsidOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 20, 1, 3),
    _DocsQosCmtsDebugDsidStatsDsidOctets_Type()
)
docsQosCmtsDebugDsidStatsDsidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidStatsDsidOctets.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmtsDebugDsidStatsDsidOctets.setUnits("octets")
_DocsQosCmDsidTable_Object = MibTable
docsQosCmDsidTable = _DocsQosCmDsidTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21)
)
if mibBuilder.loadTexts:
    docsQosCmDsidTable.setStatus("current")
_DocsQosCmDsidEntry_Object = MibTableRow
docsQosCmDsidEntry = _DocsQosCmDsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1)
)
docsQosCmDsidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosCmDsidDsid"),
)
if mibBuilder.loadTexts:
    docsQosCmDsidEntry.setStatus("current")
_DocsQosCmDsidDsid_Type = Dsid
_DocsQosCmDsidDsid_Object = MibTableColumn
docsQosCmDsidDsid = _DocsQosCmDsidDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 1),
    _DocsQosCmDsidDsid_Type()
)
docsQosCmDsidDsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmDsidDsid.setStatus("current")


class _DocsQosCmDsidUsage_Type(Bits):
    """Custom type docsQosCmDsidUsage based on Bits"""
    namedValues = NamedValues(
        *(("multicastCapable", 1),
          ("resequencing", 0))
    )

_DocsQosCmDsidUsage_Type.__name__ = "Bits"
_DocsQosCmDsidUsage_Object = MibTableColumn
docsQosCmDsidUsage = _DocsQosCmDsidUsage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 2),
    _DocsQosCmDsidUsage_Type()
)
docsQosCmDsidUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidUsage.setStatus("current")


class _DocsQosCmDsidNumReseqChs_Type(Unsigned32):
    """Custom type docsQosCmDsidNumReseqChs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_DocsQosCmDsidNumReseqChs_Type.__name__ = "Unsigned32"
_DocsQosCmDsidNumReseqChs_Object = MibTableColumn
docsQosCmDsidNumReseqChs = _DocsQosCmDsidNumReseqChs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 3),
    _DocsQosCmDsidNumReseqChs_Type()
)
docsQosCmDsidNumReseqChs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidNumReseqChs.setStatus("current")


class _DocsQosCmDsidReseqChList_Type(ChannelList):
    """Custom type docsQosCmDsidReseqChList based on ChannelList"""
    subtypeSpec = ChannelList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 255),
    )


_DocsQosCmDsidReseqChList_Type.__name__ = "ChannelList"
_DocsQosCmDsidReseqChList_Object = MibTableColumn
docsQosCmDsidReseqChList = _DocsQosCmDsidReseqChList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 4),
    _DocsQosCmDsidReseqChList_Type()
)
docsQosCmDsidReseqChList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidReseqChList.setStatus("current")


class _DocsQosCmDsidReseqWaitTime_Type(Unsigned32):
    """Custom type docsQosCmDsidReseqWaitTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 180),
    )


_DocsQosCmDsidReseqWaitTime_Type.__name__ = "Unsigned32"
_DocsQosCmDsidReseqWaitTime_Object = MibTableColumn
docsQosCmDsidReseqWaitTime = _DocsQosCmDsidReseqWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 5),
    _DocsQosCmDsidReseqWaitTime_Type()
)
docsQosCmDsidReseqWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidReseqWaitTime.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmDsidReseqWaitTime.setUnits("hundredMicroseconds")


class _DocsQosCmDsidReseqWarnThrshld_Type(Unsigned32):
    """Custom type docsQosCmDsidReseqWarnThrshld based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 179),
    )


_DocsQosCmDsidReseqWarnThrshld_Type.__name__ = "Unsigned32"
_DocsQosCmDsidReseqWarnThrshld_Object = MibTableColumn
docsQosCmDsidReseqWarnThrshld = _DocsQosCmDsidReseqWarnThrshld_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 6),
    _DocsQosCmDsidReseqWarnThrshld_Type()
)
docsQosCmDsidReseqWarnThrshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidReseqWarnThrshld.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmDsidReseqWarnThrshld.setUnits("hundredMicroseconds")


class _DocsQosCmDsidStatusHldoffTimerSeqOutOfRng_Type(Unsigned32):
    """Custom type docsQosCmDsidStatusHldoffTimerSeqOutOfRng based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosCmDsidStatusHldoffTimerSeqOutOfRng_Type.__name__ = "Unsigned32"
_DocsQosCmDsidStatusHldoffTimerSeqOutOfRng_Object = MibTableColumn
docsQosCmDsidStatusHldoffTimerSeqOutOfRng = _DocsQosCmDsidStatusHldoffTimerSeqOutOfRng_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 7),
    _DocsQosCmDsidStatusHldoffTimerSeqOutOfRng_Type()
)
docsQosCmDsidStatusHldoffTimerSeqOutOfRng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidStatusHldoffTimerSeqOutOfRng.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmDsidStatusHldoffTimerSeqOutOfRng.setUnits("20milliseconds")


class _DocsQosCmDsidOutOfRangeDiscards_Type(Unsigned32):
    """Custom type docsQosCmDsidOutOfRangeDiscards based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosCmDsidOutOfRangeDiscards_Type.__name__ = "Unsigned32"
_DocsQosCmDsidOutOfRangeDiscards_Object = MibTableColumn
docsQosCmDsidOutOfRangeDiscards = _DocsQosCmDsidOutOfRangeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 8),
    _DocsQosCmDsidOutOfRangeDiscards_Type()
)
docsQosCmDsidOutOfRangeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidOutOfRangeDiscards.setStatus("current")


class _DocsQosCmDsidNextExpectedSeqNum_Type(Unsigned32):
    """Custom type docsQosCmDsidNextExpectedSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosCmDsidNextExpectedSeqNum_Type.__name__ = "Unsigned32"
_DocsQosCmDsidNextExpectedSeqNum_Object = MibTableColumn
docsQosCmDsidNextExpectedSeqNum = _DocsQosCmDsidNextExpectedSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 9),
    _DocsQosCmDsidNextExpectedSeqNum_Type()
)
docsQosCmDsidNextExpectedSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidNextExpectedSeqNum.setStatus("current")
_DocsQosCmDsidCmInterfaceMask_Type = DocsL2vpnIfList
_DocsQosCmDsidCmInterfaceMask_Object = MibTableColumn
docsQosCmDsidCmInterfaceMask = _DocsQosCmDsidCmInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 10),
    _DocsQosCmDsidCmInterfaceMask_Type()
)
docsQosCmDsidCmInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidCmInterfaceMask.setStatus("current")
_DocsQosCmDsidFwdCmInterfaceMask_Type = DocsL2vpnIfList
_DocsQosCmDsidFwdCmInterfaceMask_Object = MibTableColumn
docsQosCmDsidFwdCmInterfaceMask = _DocsQosCmDsidFwdCmInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 21, 1, 11),
    _DocsQosCmDsidFwdCmInterfaceMask_Type()
)
docsQosCmDsidFwdCmInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidFwdCmInterfaceMask.setStatus("current")
_DocsQosCmDsidStatsTable_Object = MibTable
docsQosCmDsidStatsTable = _DocsQosCmDsidStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 22)
)
if mibBuilder.loadTexts:
    docsQosCmDsidStatsTable.setStatus("current")
_DocsQosCmDsidStatsEntry_Object = MibTableRow
docsQosCmDsidStatsEntry = _DocsQosCmDsidStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 22, 1)
)
docsQosCmDsidStatsEntry.setIndexNames(
    (0, "DOCS-QOS3-MIB", "docsQosCmDsidStatsDsid"),
)
if mibBuilder.loadTexts:
    docsQosCmDsidStatsEntry.setStatus("current")
_DocsQosCmDsidStatsDsid_Type = Dsid
_DocsQosCmDsidStatsDsid_Object = MibTableColumn
docsQosCmDsidStatsDsid = _DocsQosCmDsidStatsDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 22, 1, 1),
    _DocsQosCmDsidStatsDsid_Type()
)
docsQosCmDsidStatsDsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmDsidStatsDsid.setStatus("current")
_DocsQosCmDsidStatsSeqNumMissing_Type = Counter32
_DocsQosCmDsidStatsSeqNumMissing_Object = MibTableColumn
docsQosCmDsidStatsSeqNumMissing = _DocsQosCmDsidStatsSeqNumMissing_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 22, 1, 2),
    _DocsQosCmDsidStatsSeqNumMissing_Type()
)
docsQosCmDsidStatsSeqNumMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidStatsSeqNumMissing.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmDsidStatsSeqNumMissing.setUnits("packets")
_DocsQosCmDsidStatsSkewThreshExceeds_Type = Counter32
_DocsQosCmDsidStatsSkewThreshExceeds_Object = MibTableColumn
docsQosCmDsidStatsSkewThreshExceeds = _DocsQosCmDsidStatsSkewThreshExceeds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 22, 1, 3),
    _DocsQosCmDsidStatsSkewThreshExceeds_Type()
)
docsQosCmDsidStatsSkewThreshExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidStatsSkewThreshExceeds.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmDsidStatsSkewThreshExceeds.setUnits("packets")
_DocsQosCmDsidStatsOutOfRangePackets_Type = Counter32
_DocsQosCmDsidStatsOutOfRangePackets_Object = MibTableColumn
docsQosCmDsidStatsOutOfRangePackets = _DocsQosCmDsidStatsOutOfRangePackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 22, 1, 4),
    _DocsQosCmDsidStatsOutOfRangePackets_Type()
)
docsQosCmDsidStatsOutOfRangePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidStatsOutOfRangePackets.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmDsidStatsOutOfRangePackets.setUnits("packets")
_DocsQosCmDsidStatsNumPackets_Type = Counter64
_DocsQosCmDsidStatsNumPackets_Object = MibTableColumn
docsQosCmDsidStatsNumPackets = _DocsQosCmDsidStatsNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 22, 1, 5),
    _DocsQosCmDsidStatsNumPackets_Type()
)
docsQosCmDsidStatsNumPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidStatsNumPackets.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmDsidStatsNumPackets.setUnits("packets")
_DocsQosCmDsidClientTable_Object = MibTable
docsQosCmDsidClientTable = _DocsQosCmDsidClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 23)
)
if mibBuilder.loadTexts:
    docsQosCmDsidClientTable.setStatus("current")
_DocsQosCmDsidClientEntry_Object = MibTableRow
docsQosCmDsidClientEntry = _DocsQosCmDsidClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 23, 1)
)
docsQosCmDsidClientEntry.setIndexNames(
    (0, "DOCS-QOS3-MIB", "docsQosCmDsidClientDsid"),
    (0, "DOCS-QOS3-MIB", "docsQosCmDsidClientClientMacId"),
)
if mibBuilder.loadTexts:
    docsQosCmDsidClientEntry.setStatus("current")
_DocsQosCmDsidClientDsid_Type = Dsid
_DocsQosCmDsidClientDsid_Object = MibTableColumn
docsQosCmDsidClientDsid = _DocsQosCmDsidClientDsid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 23, 1, 1),
    _DocsQosCmDsidClientDsid_Type()
)
docsQosCmDsidClientDsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmDsidClientDsid.setStatus("current")


class _DocsQosCmDsidClientClientMacId_Type(Unsigned32):
    """Custom type docsQosCmDsidClientClientMacId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DocsQosCmDsidClientClientMacId_Type.__name__ = "Unsigned32"
_DocsQosCmDsidClientClientMacId_Object = MibTableColumn
docsQosCmDsidClientClientMacId = _DocsQosCmDsidClientClientMacId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 23, 1, 2),
    _DocsQosCmDsidClientClientMacId_Type()
)
docsQosCmDsidClientClientMacId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmDsidClientClientMacId.setStatus("current")
_DocsQosCmDsidClientClientMacAddr_Type = MacAddress
_DocsQosCmDsidClientClientMacAddr_Object = MibTableColumn
docsQosCmDsidClientClientMacAddr = _DocsQosCmDsidClientClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 23, 1, 3),
    _DocsQosCmDsidClientClientMacAddr_Type()
)
docsQosCmDsidClientClientMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmDsidClientClientMacAddr.setStatus("current")
_DocsQosCmSystemCfgState_ObjectIdentity = ObjectIdentity
docsQosCmSystemCfgState = _DocsQosCmSystemCfgState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 24)
)
_DocsQosCmSystemCfgStateAqmUsEnable_Type = TruthValue
_DocsQosCmSystemCfgStateAqmUsEnable_Object = MibScalar
docsQosCmSystemCfgStateAqmUsEnable = _DocsQosCmSystemCfgStateAqmUsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 24, 1),
    _DocsQosCmSystemCfgStateAqmUsEnable_Type()
)
docsQosCmSystemCfgStateAqmUsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmSystemCfgStateAqmUsEnable.setStatus("current")


class _DocsQosCmSystemCfgStateDefaultUsTargetBuffer_Type(Unsigned32):
    """Custom type docsQosCmSystemCfgStateDefaultUsTargetBuffer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsQosCmSystemCfgStateDefaultUsTargetBuffer_Type.__name__ = "Unsigned32"
_DocsQosCmSystemCfgStateDefaultUsTargetBuffer_Object = MibScalar
docsQosCmSystemCfgStateDefaultUsTargetBuffer = _DocsQosCmSystemCfgStateDefaultUsTargetBuffer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 24, 2),
    _DocsQosCmSystemCfgStateDefaultUsTargetBuffer_Type()
)
docsQosCmSystemCfgStateDefaultUsTargetBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmSystemCfgStateDefaultUsTargetBuffer.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmSystemCfgStateDefaultUsTargetBuffer.setUnits("milliseconds")
_DocsQosCmtsIatcProfileStatsTable_Object = MibTable
docsQosCmtsIatcProfileStatsTable = _DocsQosCmtsIatcProfileStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 25)
)
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsTable.setStatus("current")
_DocsQosCmtsIatcProfileStatsEntry_Object = MibTableRow
docsQosCmtsIatcProfileStatsEntry = _DocsQosCmtsIatcProfileStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 25, 1)
)
docsQosCmtsIatcProfileStatsEntry.setIndexNames(
    (0, "DOCS-QOS3-MIB", "docsQosCmtsIatcProfileStatsName"),
)
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsEntry.setStatus("current")
_DocsQosCmtsIatcProfileStatsName_Type = SnmpAdminString
_DocsQosCmtsIatcProfileStatsName_Object = MibTableColumn
docsQosCmtsIatcProfileStatsName = _DocsQosCmtsIatcProfileStatsName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 25, 1, 1),
    _DocsQosCmtsIatcProfileStatsName_Type()
)
docsQosCmtsIatcProfileStatsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsName.setStatus("current")
_DocsQosCmtsIatcProfileStatsIfIndex_Type = Unsigned32
_DocsQosCmtsIatcProfileStatsIfIndex_Object = MibTableColumn
docsQosCmtsIatcProfileStatsIfIndex = _DocsQosCmtsIatcProfileStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 25, 1, 2),
    _DocsQosCmtsIatcProfileStatsIfIndex_Type()
)
docsQosCmtsIatcProfileStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsIfIndex.setStatus("current")
_DocsQosCmtsIatcProfileStatsDirection_Type = IfDirection
_DocsQosCmtsIatcProfileStatsDirection_Object = MibTableColumn
docsQosCmtsIatcProfileStatsDirection = _DocsQosCmtsIatcProfileStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 25, 1, 3),
    _DocsQosCmtsIatcProfileStatsDirection_Type()
)
docsQosCmtsIatcProfileStatsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsDirection.setStatus("current")
_DocsQosCmtsIatcProfileStatsPkts_Type = Counter64
_DocsQosCmtsIatcProfileStatsPkts_Object = MibTableColumn
docsQosCmtsIatcProfileStatsPkts = _DocsQosCmtsIatcProfileStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 25, 1, 4),
    _DocsQosCmtsIatcProfileStatsPkts_Type()
)
docsQosCmtsIatcProfileStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsPkts.setUnits("Packets")
_DocsQosCmtsIatcProfileStatsOctets_Type = Counter64
_DocsQosCmtsIatcProfileStatsOctets_Object = MibTableColumn
docsQosCmtsIatcProfileStatsOctets = _DocsQosCmtsIatcProfileStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 25, 1, 5),
    _DocsQosCmtsIatcProfileStatsOctets_Type()
)
docsQosCmtsIatcProfileStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsOctets.setUnits("Octets")
_DocsQosCmtsIatcProfileStatsPolicedDropPkts_Type = Counter64
_DocsQosCmtsIatcProfileStatsPolicedDropPkts_Object = MibTableColumn
docsQosCmtsIatcProfileStatsPolicedDropPkts = _DocsQosCmtsIatcProfileStatsPolicedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 25, 1, 6),
    _DocsQosCmtsIatcProfileStatsPolicedDropPkts_Type()
)
docsQosCmtsIatcProfileStatsPolicedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsPolicedDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsPolicedDropPkts.setUnits("Packets")
_DocsQosCmtsIatcProfileStatsPolicedDelayPkts_Type = Counter64
_DocsQosCmtsIatcProfileStatsPolicedDelayPkts_Object = MibTableColumn
docsQosCmtsIatcProfileStatsPolicedDelayPkts = _DocsQosCmtsIatcProfileStatsPolicedDelayPkts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 1, 25, 1, 7),
    _DocsQosCmtsIatcProfileStatsPolicedDelayPkts_Type()
)
docsQosCmtsIatcProfileStatsPolicedDelayPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsPolicedDelayPkts.setStatus("current")
if mibBuilder.loadTexts:
    docsQosCmtsIatcProfileStatsPolicedDelayPkts.setUnits("Packets")
_DocsQosMibConformance_ObjectIdentity = ObjectIdentity
docsQosMibConformance = _DocsQosMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2)
)
_DocsQosMibCompliances_ObjectIdentity = ObjectIdentity
docsQosMibCompliances = _DocsQosMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2, 1)
)
_DocsQosMibGroups_ObjectIdentity = ObjectIdentity
docsQosMibGroups = _DocsQosMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2, 2)
)

# Managed Objects groups

docsQosBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2, 2, 1)
)
docsQosBaseGroup.setObjects(
      *(("DOCS-QOS3-MIB", "docsQosPktClassDirection"),
        ("DOCS-QOS3-MIB", "docsQosPktClassPriority"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIpTosLow"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIpTosHigh"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIpTosMask"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIpProtocol"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIpSourceAddr"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIpSourceMask"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIpDestAddr"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIpDestMask"),
        ("DOCS-QOS3-MIB", "docsQosPktClassSourcePortStart"),
        ("DOCS-QOS3-MIB", "docsQosPktClassSourcePortEnd"),
        ("DOCS-QOS3-MIB", "docsQosPktClassDestPortStart"),
        ("DOCS-QOS3-MIB", "docsQosPktClassDestPortEnd"),
        ("DOCS-QOS3-MIB", "docsQosPktClassDestMacAddr"),
        ("DOCS-QOS3-MIB", "docsQosPktClassDestMacMask"),
        ("DOCS-QOS3-MIB", "docsQosPktClassSourceMacAddr"),
        ("DOCS-QOS3-MIB", "docsQosPktClassEnetProtocolType"),
        ("DOCS-QOS3-MIB", "docsQosPktClassEnetProtocol"),
        ("DOCS-QOS3-MIB", "docsQosPktClassUserPriLow"),
        ("DOCS-QOS3-MIB", "docsQosPktClassUserPriHigh"),
        ("DOCS-QOS3-MIB", "docsQosPktClassVlanId"),
        ("DOCS-QOS3-MIB", "docsQosPktClassState"),
        ("DOCS-QOS3-MIB", "docsQosPktClassPkts"),
        ("DOCS-QOS3-MIB", "docsQosPktClassBitMap"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIpAddrType"),
        ("DOCS-QOS3-MIB", "docsQosPktClassFlowLabel"),
        ("DOCS-QOS3-MIB", "docsQosPktClassCmInterfaceMask"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIcmpTypeLow"),
        ("DOCS-QOS3-MIB", "docsQosPktClassIcmpTypeHigh"),
        ("DOCS-QOS3-MIB", "docsQosParamSetServiceClassName"),
        ("DOCS-QOS3-MIB", "docsQosParamSetPriority"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMaxTrafficRate"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMaxTrafficBurst"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMinReservedRate"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMinReservedPkt"),
        ("DOCS-QOS3-MIB", "docsQosParamSetActiveTimeout"),
        ("DOCS-QOS3-MIB", "docsQosParamSetAdmittedTimeout"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMaxConcatBurst"),
        ("DOCS-QOS3-MIB", "docsQosParamSetSchedulingType"),
        ("DOCS-QOS3-MIB", "docsQosParamSetNomPollInterval"),
        ("DOCS-QOS3-MIB", "docsQosParamSetTolPollJitter"),
        ("DOCS-QOS3-MIB", "docsQosParamSetUnsolicitGrantSize"),
        ("DOCS-QOS3-MIB", "docsQosParamSetNomGrantInterval"),
        ("DOCS-QOS3-MIB", "docsQosParamSetTolGrantJitter"),
        ("DOCS-QOS3-MIB", "docsQosParamSetGrantsPerInterval"),
        ("DOCS-QOS3-MIB", "docsQosParamSetTosAndMask"),
        ("DOCS-QOS3-MIB", "docsQosParamSetTosOrMask"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMaxLatency"),
        ("DOCS-QOS3-MIB", "docsQosParamSetRequestPolicyOct"),
        ("DOCS-QOS3-MIB", "docsQosParamSetRequiredAttrMask"),
        ("DOCS-QOS3-MIB", "docsQosParamSetForbiddenAttrMask"),
        ("DOCS-QOS3-MIB", "docsQosParamSetAttrAggrRuleMask"),
        ("DOCS-QOS3-MIB", "docsQosParamSetAppId"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMultiplierContentionReqWindow"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMultiplierBytesReq"),
        ("DOCS-QOS3-MIB", "docsQosParamSetPeakTrafficRate"),
        ("DOCS-QOS3-MIB", "docsQosParamSetDsResequencing"),
        ("DOCS-QOS3-MIB", "docsQosParamSetBitMap"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMinimumBuffer"),
        ("DOCS-QOS3-MIB", "docsQosParamSetTargetBuffer"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMaximumBuffer"),
        ("DOCS-QOS3-MIB", "docsQosParamSetAqmDisabled"),
        ("DOCS-QOS3-MIB", "docsQosParamSetAqmLatencyTarget"),
        ("DOCS-QOS3-MIB", "docsQosParamSetHCMaxTrafficRate"),
        ("DOCS-QOS3-MIB", "docsQosParamSetHCMinReservedRate"),
        ("DOCS-QOS3-MIB", "docsQosParamSetHCPeakTrafficRate"),
        ("DOCS-QOS3-MIB", "docsQosParamSetAqmAlgInUse"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowSID"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowDirection"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowPrimary"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowParamSetTypeStatus"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowChSetId"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowAttrAssignSuccess"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowDsid"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowMaxReqPerSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowMaxOutstandingBytesPerSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowMaxTotBytesReqPerSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowMaxTimeInSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowBufferSize"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowPkts"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowOctets"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowTimeCreated"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowTimeActive"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowPHSUnknowns"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowPolicedDropPkts"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowPolicedDelayPkts"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowAqmDroppedPkts"),
        ("DOCS-QOS3-MIB", "docsQosDSAReqs"),
        ("DOCS-QOS3-MIB", "docsQosDSARsps"),
        ("DOCS-QOS3-MIB", "docsQosDSAAcks"),
        ("DOCS-QOS3-MIB", "docsQosDSCReqs"),
        ("DOCS-QOS3-MIB", "docsQosDSCRsps"),
        ("DOCS-QOS3-MIB", "docsQosDSCAcks"),
        ("DOCS-QOS3-MIB", "docsQosDSDReqs"),
        ("DOCS-QOS3-MIB", "docsQosDSDRsps"),
        ("DOCS-QOS3-MIB", "docsQosDynamicAdds"),
        ("DOCS-QOS3-MIB", "docsQosDynamicAddFails"),
        ("DOCS-QOS3-MIB", "docsQosDynamicChanges"),
        ("DOCS-QOS3-MIB", "docsQosDynamicChangeFails"),
        ("DOCS-QOS3-MIB", "docsQosDynamicDeletes"),
        ("DOCS-QOS3-MIB", "docsQosDynamicDeleteFails"),
        ("DOCS-QOS3-MIB", "docsQosDCCReqs"),
        ("DOCS-QOS3-MIB", "docsQosDCCRsps"),
        ("DOCS-QOS3-MIB", "docsQosDCCAcks"),
        ("DOCS-QOS3-MIB", "docsQosDCCs"),
        ("DOCS-QOS3-MIB", "docsQosDCCFails"),
        ("DOCS-QOS3-MIB", "docsQosDCCRspDeparts"),
        ("DOCS-QOS3-MIB", "docsQosDCCRspArrives"),
        ("DOCS-QOS3-MIB", "docsQosDCCRspDeparts"),
        ("DOCS-QOS3-MIB", "docsQosDCCRspArrives"),
        ("DOCS-QOS3-MIB", "docsQosDbcReqs"),
        ("DOCS-QOS3-MIB", "docsQosDbcRsps"),
        ("DOCS-QOS3-MIB", "docsQosDbcAcks"),
        ("DOCS-QOS3-MIB", "docsQosDbcSuccesses"),
        ("DOCS-QOS3-MIB", "docsQosDbcFails"),
        ("DOCS-QOS3-MIB", "docsQosDbcPartial"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowSidClusterSid"))
)
if mibBuilder.loadTexts:
    docsQosBaseGroup.setStatus("current")

docsQosCmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2, 2, 2)
)
docsQosCmtsGroup.setObjects(
      *(("DOCS-QOS3-MIB", "docsQosUpstreamFragments"),
        ("DOCS-QOS3-MIB", "docsQosUpstreamFragDiscards"),
        ("DOCS-QOS3-MIB", "docsQosUpstreamConcatBursts"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowIatcProfileName"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogIfIndex"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogSFID"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogCmMac"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogPkts"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogOctets"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogTimeDeleted"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogTimeCreated"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogTimeActive"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogDirection"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogPrimary"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogServiceClassName"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogPolicedDropPkts"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogPolicedDelayPkts"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowLogControl"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassStatus"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassPriority"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMaxTrafficRate"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMaxTrafficBurst"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMinReservedRate"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMinReservedPkt"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMaxConcatBurst"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassNomPollInterval"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassTolPollJitter"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassUnsolicitGrantSize"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassNomGrantInterval"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassTolGrantJitter"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassGrantsPerInterval"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMaxLatency"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassActiveTimeout"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassAdmittedTimeout"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassSchedulingType"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassRequestPolicy"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassTosAndMask"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassTosOrMask"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassDirection"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassStorageType"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassDSCPOverwrite"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassRequiredAttrMask"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassForbiddenAttrMask"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassAttrAggrRuleMask"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassAppId"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMultiplierContentionReqWindow"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMultiplierBytesReq"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassPeakTrafficRate"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassDsResequencing"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMinimumBuffer"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassTargetBuffer"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMaximumBuffer"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassAqmDisabled"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassAqmLatencyTarget"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassHCMaxTrafficRate"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassHCMinReservedRate"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassHCPeakTrafficRate"),
        ("DOCS-QOS3-MIB", "docsQosCmtsIfIndex"),
        ("DOCS-QOS3-MIB", "docsQosGrpServiceFlowIsDef"),
        ("DOCS-QOS3-MIB", "docsQosGrpServiceFlowQosConfigId"),
        ("DOCS-QOS3-MIB", "docsQosGrpServiceFlowNumSess"),
        ("DOCS-QOS3-MIB", "docsQosGrpServiceFlowSrcAddr"),
        ("DOCS-QOS3-MIB", "docsQosGrpServiceFlowGrpAddr"),
        ("DOCS-QOS3-MIB", "docsQosGrpServiceFlowAddrType"),
        ("DOCS-QOS3-MIB", "docsQosGrpPktClassGrpConfigId"),
        ("DOCS-QOS3-MIB", "docsQosUpChCounterExtSgmtValids"),
        ("DOCS-QOS3-MIB", "docsQosUpChCounterExtSgmtDiscards"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowCcfStatsSgmtValids"),
        ("DOCS-QOS3-MIB", "docsQosServiceFlowCcfStatsSgmtLost"),
        ("DOCS-QOS3-MIB", "docsQosCmtsDsidUsage"),
        ("DOCS-QOS3-MIB", "docsQosCmtsDsidDsChSet"),
        ("DOCS-QOS3-MIB", "docsQosCmtsDsidReseqWaitTime"),
        ("DOCS-QOS3-MIB", "docsQosCmtsDsidReseqWarnThrshld"),
        ("DOCS-QOS3-MIB", "docsQosCmtsDsidStatusHldoffTimerSeqOutOfRng"),
        ("DOCS-QOS3-MIB", "docsQosCmtsDsidCurrentSeqNum"),
        ("DOCS-QOS3-MIB", "docsQosCmtsDebugDsidRowStatus"),
        ("DOCS-QOS3-MIB", "docsQosCmtsDebugDsidStatsDsidPackets"),
        ("DOCS-QOS3-MIB", "docsQosCmtsDebugDsidStatsDsidOctets"),
        ("DOCS-QOS3-MIB", "docsQosCmtsIatcProfileStatsIfIndex"),
        ("DOCS-QOS3-MIB", "docsQosCmtsIatcProfileStatsDirection"),
        ("DOCS-QOS3-MIB", "docsQosCmtsIatcProfileStatsPkts"),
        ("DOCS-QOS3-MIB", "docsQosCmtsIatcProfileStatsOctets"),
        ("DOCS-QOS3-MIB", "docsQosCmtsIatcProfileStatsPolicedDropPkts"),
        ("DOCS-QOS3-MIB", "docsQosCmtsIatcProfileStatsPolicedDelayPkts"))
)
if mibBuilder.loadTexts:
    docsQosCmtsGroup.setStatus("current")

docsQosCmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2, 2, 3)
)
docsQosCmGroup.setObjects(
      *(("DOCS-QOS3-MIB", "docsQosCmServiceUsStatsTxSlotsImmed"),
        ("DOCS-QOS3-MIB", "docsQosCmServiceUsStatsTxSlotsDed"),
        ("DOCS-QOS3-MIB", "docsQosCmServiceUsStatsTxRetries"),
        ("DOCS-QOS3-MIB", "docsQosCmServiceUsStatsTxExceededs"),
        ("DOCS-QOS3-MIB", "docsQosCmServiceUsStatsRqRetries"),
        ("DOCS-QOS3-MIB", "docsQosCmServiceUsStatsRqExceededs"),
        ("DOCS-QOS3-MIB", "docsQosCmServiceUsStatsSgmts"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidUsage"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidNumReseqChs"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidReseqChList"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidReseqWaitTime"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidReseqWarnThrshld"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidStatusHldoffTimerSeqOutOfRng"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidOutOfRangeDiscards"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidNextExpectedSeqNum"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidCmInterfaceMask"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidFwdCmInterfaceMask"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidStatsSeqNumMissing"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidStatsSkewThreshExceeds"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidStatsOutOfRangePackets"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidStatsNumPackets"),
        ("DOCS-QOS3-MIB", "docsQosCmDsidClientClientMacAddr"),
        ("DOCS-QOS3-MIB", "docsQosCmSystemCfgStateAqmUsEnable"),
        ("DOCS-QOS3-MIB", "docsQosCmSystemCfgStateDefaultUsTargetBuffer"))
)
if mibBuilder.loadTexts:
    docsQosCmGroup.setStatus("current")

docsQosDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2, 2, 4)
)
docsQosDeprecatedGroup.setObjects(
      *(("DOCS-QOS3-MIB", "docsQosParamSetMaxReqPerSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMaxOutstandingBytesPerSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMaxTotBytesReqPerSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosParamSetMaxTimeInSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMaxReqPerSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMaxOutstandingBytesPerSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMaxTotBytesReqPerSidCluster"),
        ("DOCS-QOS3-MIB", "docsQosServiceClassMaxTimeInSidCluster"))
)
if mibBuilder.loadTexts:
    docsQosDeprecatedGroup.setStatus("deprecated")

docsQosObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2, 2, 5)
)
docsQosObsoleteGroup.setObjects(
      *(("DOCS-QOS3-MIB", "docsQosPHSField"),
        ("DOCS-QOS3-MIB", "docsQosPHSMask"),
        ("DOCS-QOS3-MIB", "docsQosPHSSize"),
        ("DOCS-QOS3-MIB", "docsQosPHSVerify"),
        ("DOCS-QOS3-MIB", "docsQosPHSIndex"))
)
if mibBuilder.loadTexts:
    docsQosObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsQosCompliance.setStatus(
        "current"
    )

docsQosDeprecatedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 21, 2, 1, 2)
)
if mibBuilder.loadTexts:
    docsQosDeprecatedCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-QOS3-MIB",
    **{"BitRate": BitRate,
       "SchedulingType": SchedulingType,
       "docsQosMib": docsQosMib,
       "docsQosMibObjects": docsQosMibObjects,
       "docsQosPktClassTable": docsQosPktClassTable,
       "docsQosPktClassEntry": docsQosPktClassEntry,
       "docsQosPktClassId": docsQosPktClassId,
       "docsQosPktClassDirection": docsQosPktClassDirection,
       "docsQosPktClassPriority": docsQosPktClassPriority,
       "docsQosPktClassIpTosLow": docsQosPktClassIpTosLow,
       "docsQosPktClassIpTosHigh": docsQosPktClassIpTosHigh,
       "docsQosPktClassIpTosMask": docsQosPktClassIpTosMask,
       "docsQosPktClassIpProtocol": docsQosPktClassIpProtocol,
       "docsQosPktClassIpSourceAddr": docsQosPktClassIpSourceAddr,
       "docsQosPktClassIpSourceMask": docsQosPktClassIpSourceMask,
       "docsQosPktClassIpDestAddr": docsQosPktClassIpDestAddr,
       "docsQosPktClassIpDestMask": docsQosPktClassIpDestMask,
       "docsQosPktClassSourcePortStart": docsQosPktClassSourcePortStart,
       "docsQosPktClassSourcePortEnd": docsQosPktClassSourcePortEnd,
       "docsQosPktClassDestPortStart": docsQosPktClassDestPortStart,
       "docsQosPktClassDestPortEnd": docsQosPktClassDestPortEnd,
       "docsQosPktClassDestMacAddr": docsQosPktClassDestMacAddr,
       "docsQosPktClassDestMacMask": docsQosPktClassDestMacMask,
       "docsQosPktClassSourceMacAddr": docsQosPktClassSourceMacAddr,
       "docsQosPktClassEnetProtocolType": docsQosPktClassEnetProtocolType,
       "docsQosPktClassEnetProtocol": docsQosPktClassEnetProtocol,
       "docsQosPktClassUserPriLow": docsQosPktClassUserPriLow,
       "docsQosPktClassUserPriHigh": docsQosPktClassUserPriHigh,
       "docsQosPktClassVlanId": docsQosPktClassVlanId,
       "docsQosPktClassState": docsQosPktClassState,
       "docsQosPktClassPkts": docsQosPktClassPkts,
       "docsQosPktClassBitMap": docsQosPktClassBitMap,
       "docsQosPktClassIpAddrType": docsQosPktClassIpAddrType,
       "docsQosPktClassFlowLabel": docsQosPktClassFlowLabel,
       "docsQosPktClassCmInterfaceMask": docsQosPktClassCmInterfaceMask,
       "docsQosPktClassIcmpTypeLow": docsQosPktClassIcmpTypeLow,
       "docsQosPktClassIcmpTypeHigh": docsQosPktClassIcmpTypeHigh,
       "docsQosParamSetTable": docsQosParamSetTable,
       "docsQosParamSetEntry": docsQosParamSetEntry,
       "docsQosParamSetServiceClassName": docsQosParamSetServiceClassName,
       "docsQosParamSetPriority": docsQosParamSetPriority,
       "docsQosParamSetMaxTrafficRate": docsQosParamSetMaxTrafficRate,
       "docsQosParamSetMaxTrafficBurst": docsQosParamSetMaxTrafficBurst,
       "docsQosParamSetMinReservedRate": docsQosParamSetMinReservedRate,
       "docsQosParamSetMinReservedPkt": docsQosParamSetMinReservedPkt,
       "docsQosParamSetActiveTimeout": docsQosParamSetActiveTimeout,
       "docsQosParamSetAdmittedTimeout": docsQosParamSetAdmittedTimeout,
       "docsQosParamSetMaxConcatBurst": docsQosParamSetMaxConcatBurst,
       "docsQosParamSetSchedulingType": docsQosParamSetSchedulingType,
       "docsQosParamSetNomPollInterval": docsQosParamSetNomPollInterval,
       "docsQosParamSetTolPollJitter": docsQosParamSetTolPollJitter,
       "docsQosParamSetUnsolicitGrantSize": docsQosParamSetUnsolicitGrantSize,
       "docsQosParamSetNomGrantInterval": docsQosParamSetNomGrantInterval,
       "docsQosParamSetTolGrantJitter": docsQosParamSetTolGrantJitter,
       "docsQosParamSetGrantsPerInterval": docsQosParamSetGrantsPerInterval,
       "docsQosParamSetTosAndMask": docsQosParamSetTosAndMask,
       "docsQosParamSetTosOrMask": docsQosParamSetTosOrMask,
       "docsQosParamSetMaxLatency": docsQosParamSetMaxLatency,
       "docsQosParamSetType": docsQosParamSetType,
       "docsQosParamSetRequestPolicyOct": docsQosParamSetRequestPolicyOct,
       "docsQosParamSetBitMap": docsQosParamSetBitMap,
       "docsQosParamSetServiceFlowId": docsQosParamSetServiceFlowId,
       "docsQosParamSetRequiredAttrMask": docsQosParamSetRequiredAttrMask,
       "docsQosParamSetForbiddenAttrMask": docsQosParamSetForbiddenAttrMask,
       "docsQosParamSetAttrAggrRuleMask": docsQosParamSetAttrAggrRuleMask,
       "docsQosParamSetAppId": docsQosParamSetAppId,
       "docsQosParamSetMultiplierContentionReqWindow": docsQosParamSetMultiplierContentionReqWindow,
       "docsQosParamSetMultiplierBytesReq": docsQosParamSetMultiplierBytesReq,
       "docsQosParamSetMaxReqPerSidCluster": docsQosParamSetMaxReqPerSidCluster,
       "docsQosParamSetMaxOutstandingBytesPerSidCluster": docsQosParamSetMaxOutstandingBytesPerSidCluster,
       "docsQosParamSetMaxTotBytesReqPerSidCluster": docsQosParamSetMaxTotBytesReqPerSidCluster,
       "docsQosParamSetMaxTimeInSidCluster": docsQosParamSetMaxTimeInSidCluster,
       "docsQosParamSetPeakTrafficRate": docsQosParamSetPeakTrafficRate,
       "docsQosParamSetDsResequencing": docsQosParamSetDsResequencing,
       "docsQosParamSetMinimumBuffer": docsQosParamSetMinimumBuffer,
       "docsQosParamSetTargetBuffer": docsQosParamSetTargetBuffer,
       "docsQosParamSetMaximumBuffer": docsQosParamSetMaximumBuffer,
       "docsQosParamSetAqmDisabled": docsQosParamSetAqmDisabled,
       "docsQosParamSetAqmLatencyTarget": docsQosParamSetAqmLatencyTarget,
       "docsQosParamSetHCMaxTrafficRate": docsQosParamSetHCMaxTrafficRate,
       "docsQosParamSetHCMinReservedRate": docsQosParamSetHCMinReservedRate,
       "docsQosParamSetHCPeakTrafficRate": docsQosParamSetHCPeakTrafficRate,
       "docsQosParamSetAqmAlgInUse": docsQosParamSetAqmAlgInUse,
       "docsQosServiceFlowTable": docsQosServiceFlowTable,
       "docsQosServiceFlowEntry": docsQosServiceFlowEntry,
       "docsQosServiceFlowId": docsQosServiceFlowId,
       "docsQosServiceFlowSID": docsQosServiceFlowSID,
       "docsQosServiceFlowDirection": docsQosServiceFlowDirection,
       "docsQosServiceFlowPrimary": docsQosServiceFlowPrimary,
       "docsQosServiceFlowParamSetTypeStatus": docsQosServiceFlowParamSetTypeStatus,
       "docsQosServiceFlowChSetId": docsQosServiceFlowChSetId,
       "docsQosServiceFlowAttrAssignSuccess": docsQosServiceFlowAttrAssignSuccess,
       "docsQosServiceFlowDsid": docsQosServiceFlowDsid,
       "docsQosServiceFlowMaxReqPerSidCluster": docsQosServiceFlowMaxReqPerSidCluster,
       "docsQosServiceFlowMaxOutstandingBytesPerSidCluster": docsQosServiceFlowMaxOutstandingBytesPerSidCluster,
       "docsQosServiceFlowMaxTotBytesReqPerSidCluster": docsQosServiceFlowMaxTotBytesReqPerSidCluster,
       "docsQosServiceFlowMaxTimeInSidCluster": docsQosServiceFlowMaxTimeInSidCluster,
       "docsQosServiceFlowBufferSize": docsQosServiceFlowBufferSize,
       "docsQosServiceFlowIatcProfileName": docsQosServiceFlowIatcProfileName,
       "docsQosServiceFlowStatsTable": docsQosServiceFlowStatsTable,
       "docsQosServiceFlowStatsEntry": docsQosServiceFlowStatsEntry,
       "docsQosServiceFlowPkts": docsQosServiceFlowPkts,
       "docsQosServiceFlowOctets": docsQosServiceFlowOctets,
       "docsQosServiceFlowTimeCreated": docsQosServiceFlowTimeCreated,
       "docsQosServiceFlowTimeActive": docsQosServiceFlowTimeActive,
       "docsQosServiceFlowPHSUnknowns": docsQosServiceFlowPHSUnknowns,
       "docsQosServiceFlowPolicedDropPkts": docsQosServiceFlowPolicedDropPkts,
       "docsQosServiceFlowPolicedDelayPkts": docsQosServiceFlowPolicedDelayPkts,
       "docsQosServiceFlowAqmDroppedPkts": docsQosServiceFlowAqmDroppedPkts,
       "docsQosUpstreamStatsTable": docsQosUpstreamStatsTable,
       "docsQosUpstreamStatsEntry": docsQosUpstreamStatsEntry,
       "docsQosSID": docsQosSID,
       "docsQosUpstreamFragments": docsQosUpstreamFragments,
       "docsQosUpstreamFragDiscards": docsQosUpstreamFragDiscards,
       "docsQosUpstreamConcatBursts": docsQosUpstreamConcatBursts,
       "docsQosDynamicServiceStatsTable": docsQosDynamicServiceStatsTable,
       "docsQosDynamicServiceStatsEntry": docsQosDynamicServiceStatsEntry,
       "docsQosIfDirection": docsQosIfDirection,
       "docsQosDSAReqs": docsQosDSAReqs,
       "docsQosDSARsps": docsQosDSARsps,
       "docsQosDSAAcks": docsQosDSAAcks,
       "docsQosDSCReqs": docsQosDSCReqs,
       "docsQosDSCRsps": docsQosDSCRsps,
       "docsQosDSCAcks": docsQosDSCAcks,
       "docsQosDSDReqs": docsQosDSDReqs,
       "docsQosDSDRsps": docsQosDSDRsps,
       "docsQosDynamicAdds": docsQosDynamicAdds,
       "docsQosDynamicAddFails": docsQosDynamicAddFails,
       "docsQosDynamicChanges": docsQosDynamicChanges,
       "docsQosDynamicChangeFails": docsQosDynamicChangeFails,
       "docsQosDynamicDeletes": docsQosDynamicDeletes,
       "docsQosDynamicDeleteFails": docsQosDynamicDeleteFails,
       "docsQosDCCReqs": docsQosDCCReqs,
       "docsQosDCCRsps": docsQosDCCRsps,
       "docsQosDCCAcks": docsQosDCCAcks,
       "docsQosDCCs": docsQosDCCs,
       "docsQosDCCFails": docsQosDCCFails,
       "docsQosDCCRspDeparts": docsQosDCCRspDeparts,
       "docsQosDCCRspArrives": docsQosDCCRspArrives,
       "docsQosDbcReqs": docsQosDbcReqs,
       "docsQosDbcRsps": docsQosDbcRsps,
       "docsQosDbcAcks": docsQosDbcAcks,
       "docsQosDbcSuccesses": docsQosDbcSuccesses,
       "docsQosDbcFails": docsQosDbcFails,
       "docsQosDbcPartial": docsQosDbcPartial,
       "docsQosServiceFlowLogTable": docsQosServiceFlowLogTable,
       "docsQosServiceFlowLogEntry": docsQosServiceFlowLogEntry,
       "docsQosServiceFlowLogIndex": docsQosServiceFlowLogIndex,
       "docsQosServiceFlowLogIfIndex": docsQosServiceFlowLogIfIndex,
       "docsQosServiceFlowLogSFID": docsQosServiceFlowLogSFID,
       "docsQosServiceFlowLogCmMac": docsQosServiceFlowLogCmMac,
       "docsQosServiceFlowLogPkts": docsQosServiceFlowLogPkts,
       "docsQosServiceFlowLogOctets": docsQosServiceFlowLogOctets,
       "docsQosServiceFlowLogTimeDeleted": docsQosServiceFlowLogTimeDeleted,
       "docsQosServiceFlowLogTimeCreated": docsQosServiceFlowLogTimeCreated,
       "docsQosServiceFlowLogTimeActive": docsQosServiceFlowLogTimeActive,
       "docsQosServiceFlowLogDirection": docsQosServiceFlowLogDirection,
       "docsQosServiceFlowLogPrimary": docsQosServiceFlowLogPrimary,
       "docsQosServiceFlowLogServiceClassName": docsQosServiceFlowLogServiceClassName,
       "docsQosServiceFlowLogPolicedDropPkts": docsQosServiceFlowLogPolicedDropPkts,
       "docsQosServiceFlowLogPolicedDelayPkts": docsQosServiceFlowLogPolicedDelayPkts,
       "docsQosServiceFlowLogControl": docsQosServiceFlowLogControl,
       "docsQosServiceClassTable": docsQosServiceClassTable,
       "docsQosServiceClassEntry": docsQosServiceClassEntry,
       "docsQosServiceClassName": docsQosServiceClassName,
       "docsQosServiceClassStatus": docsQosServiceClassStatus,
       "docsQosServiceClassPriority": docsQosServiceClassPriority,
       "docsQosServiceClassMaxTrafficRate": docsQosServiceClassMaxTrafficRate,
       "docsQosServiceClassMaxTrafficBurst": docsQosServiceClassMaxTrafficBurst,
       "docsQosServiceClassMinReservedRate": docsQosServiceClassMinReservedRate,
       "docsQosServiceClassMinReservedPkt": docsQosServiceClassMinReservedPkt,
       "docsQosServiceClassMaxConcatBurst": docsQosServiceClassMaxConcatBurst,
       "docsQosServiceClassNomPollInterval": docsQosServiceClassNomPollInterval,
       "docsQosServiceClassTolPollJitter": docsQosServiceClassTolPollJitter,
       "docsQosServiceClassUnsolicitGrantSize": docsQosServiceClassUnsolicitGrantSize,
       "docsQosServiceClassNomGrantInterval": docsQosServiceClassNomGrantInterval,
       "docsQosServiceClassTolGrantJitter": docsQosServiceClassTolGrantJitter,
       "docsQosServiceClassGrantsPerInterval": docsQosServiceClassGrantsPerInterval,
       "docsQosServiceClassMaxLatency": docsQosServiceClassMaxLatency,
       "docsQosServiceClassActiveTimeout": docsQosServiceClassActiveTimeout,
       "docsQosServiceClassAdmittedTimeout": docsQosServiceClassAdmittedTimeout,
       "docsQosServiceClassSchedulingType": docsQosServiceClassSchedulingType,
       "docsQosServiceClassRequestPolicy": docsQosServiceClassRequestPolicy,
       "docsQosServiceClassTosAndMask": docsQosServiceClassTosAndMask,
       "docsQosServiceClassTosOrMask": docsQosServiceClassTosOrMask,
       "docsQosServiceClassDirection": docsQosServiceClassDirection,
       "docsQosServiceClassStorageType": docsQosServiceClassStorageType,
       "docsQosServiceClassDSCPOverwrite": docsQosServiceClassDSCPOverwrite,
       "docsQosServiceClassRequiredAttrMask": docsQosServiceClassRequiredAttrMask,
       "docsQosServiceClassForbiddenAttrMask": docsQosServiceClassForbiddenAttrMask,
       "docsQosServiceClassAttrAggrRuleMask": docsQosServiceClassAttrAggrRuleMask,
       "docsQosServiceClassAppId": docsQosServiceClassAppId,
       "docsQosServiceClassMultiplierContentionReqWindow": docsQosServiceClassMultiplierContentionReqWindow,
       "docsQosServiceClassMultiplierBytesReq": docsQosServiceClassMultiplierBytesReq,
       "docsQosServiceClassMaxReqPerSidCluster": docsQosServiceClassMaxReqPerSidCluster,
       "docsQosServiceClassMaxOutstandingBytesPerSidCluster": docsQosServiceClassMaxOutstandingBytesPerSidCluster,
       "docsQosServiceClassMaxTotBytesReqPerSidCluster": docsQosServiceClassMaxTotBytesReqPerSidCluster,
       "docsQosServiceClassMaxTimeInSidCluster": docsQosServiceClassMaxTimeInSidCluster,
       "docsQosServiceClassPeakTrafficRate": docsQosServiceClassPeakTrafficRate,
       "docsQosServiceClassDsResequencing": docsQosServiceClassDsResequencing,
       "docsQosServiceClassMinimumBuffer": docsQosServiceClassMinimumBuffer,
       "docsQosServiceClassTargetBuffer": docsQosServiceClassTargetBuffer,
       "docsQosServiceClassMaximumBuffer": docsQosServiceClassMaximumBuffer,
       "docsQosServiceClassAqmDisabled": docsQosServiceClassAqmDisabled,
       "docsQosServiceClassAqmLatencyTarget": docsQosServiceClassAqmLatencyTarget,
       "docsQosServiceClassHCMaxTrafficRate": docsQosServiceClassHCMaxTrafficRate,
       "docsQosServiceClassHCMinReservedRate": docsQosServiceClassHCMinReservedRate,
       "docsQosServiceClassHCPeakTrafficRate": docsQosServiceClassHCPeakTrafficRate,
       "docsQosPHSTable": docsQosPHSTable,
       "docsQosPHSEntry": docsQosPHSEntry,
       "docsQosPHSField": docsQosPHSField,
       "docsQosPHSMask": docsQosPHSMask,
       "docsQosPHSSize": docsQosPHSSize,
       "docsQosPHSVerify": docsQosPHSVerify,
       "docsQosPHSIndex": docsQosPHSIndex,
       "docsQosCmtsMacToSrvFlowTable": docsQosCmtsMacToSrvFlowTable,
       "docsQosCmtsMacToSrvFlowEntry": docsQosCmtsMacToSrvFlowEntry,
       "docsQosCmtsCmMac": docsQosCmtsCmMac,
       "docsQosCmtsServiceFlowId": docsQosCmtsServiceFlowId,
       "docsQosCmtsIfIndex": docsQosCmtsIfIndex,
       "docsQosServiceFlowSidClusterTable": docsQosServiceFlowSidClusterTable,
       "docsQosServiceFlowSidClusterEntry": docsQosServiceFlowSidClusterEntry,
       "docsQosServiceFlowSidClusterId": docsQosServiceFlowSidClusterId,
       "docsQosServiceFlowSidClusterUcid": docsQosServiceFlowSidClusterUcid,
       "docsQosServiceFlowSidClusterSid": docsQosServiceFlowSidClusterSid,
       "docsQosGrpServiceFlowTable": docsQosGrpServiceFlowTable,
       "docsQosGrpServiceFlowEntry": docsQosGrpServiceFlowEntry,
       "docsQosGrpServiceFlowIsDef": docsQosGrpServiceFlowIsDef,
       "docsQosGrpServiceFlowQosConfigId": docsQosGrpServiceFlowQosConfigId,
       "docsQosGrpServiceFlowNumSess": docsQosGrpServiceFlowNumSess,
       "docsQosGrpServiceFlowSrcAddr": docsQosGrpServiceFlowSrcAddr,
       "docsQosGrpServiceFlowGrpAddr": docsQosGrpServiceFlowGrpAddr,
       "docsQosGrpServiceFlowAddrType": docsQosGrpServiceFlowAddrType,
       "docsQosGrpPktClassTable": docsQosGrpPktClassTable,
       "docsQosGrpPktClassEntry": docsQosGrpPktClassEntry,
       "docsQosGrpPktClassGrpConfigId": docsQosGrpPktClassGrpConfigId,
       "docsQosUpChCounterExtTable": docsQosUpChCounterExtTable,
       "docsQosUpChCounterExtEntry": docsQosUpChCounterExtEntry,
       "docsQosUpChCounterExtSgmtValids": docsQosUpChCounterExtSgmtValids,
       "docsQosUpChCounterExtSgmtDiscards": docsQosUpChCounterExtSgmtDiscards,
       "docsQosServiceFlowCcfStatsTable": docsQosServiceFlowCcfStatsTable,
       "docsQosServiceFlowCcfStatsEntry": docsQosServiceFlowCcfStatsEntry,
       "docsQosServiceFlowCcfStatsSgmtValids": docsQosServiceFlowCcfStatsSgmtValids,
       "docsQosServiceFlowCcfStatsSgmtLost": docsQosServiceFlowCcfStatsSgmtLost,
       "docsQosCmServiceUsStatsTable": docsQosCmServiceUsStatsTable,
       "docsQosCmServiceUsStatsEntry": docsQosCmServiceUsStatsEntry,
       "docsQosCmServiceUsStatsTxSlotsImmed": docsQosCmServiceUsStatsTxSlotsImmed,
       "docsQosCmServiceUsStatsTxSlotsDed": docsQosCmServiceUsStatsTxSlotsDed,
       "docsQosCmServiceUsStatsTxRetries": docsQosCmServiceUsStatsTxRetries,
       "docsQosCmServiceUsStatsTxExceededs": docsQosCmServiceUsStatsTxExceededs,
       "docsQosCmServiceUsStatsRqRetries": docsQosCmServiceUsStatsRqRetries,
       "docsQosCmServiceUsStatsRqExceededs": docsQosCmServiceUsStatsRqExceededs,
       "docsQosCmServiceUsStatsSgmts": docsQosCmServiceUsStatsSgmts,
       "docsQosCmtsDsidTable": docsQosCmtsDsidTable,
       "docsQosCmtsDsidEntry": docsQosCmtsDsidEntry,
       "docsQosCmtsDsidDsid": docsQosCmtsDsidDsid,
       "docsQosCmtsDsidUsage": docsQosCmtsDsidUsage,
       "docsQosCmtsDsidDsChSet": docsQosCmtsDsidDsChSet,
       "docsQosCmtsDsidReseqWaitTime": docsQosCmtsDsidReseqWaitTime,
       "docsQosCmtsDsidReseqWarnThrshld": docsQosCmtsDsidReseqWarnThrshld,
       "docsQosCmtsDsidStatusHldoffTimerSeqOutOfRng": docsQosCmtsDsidStatusHldoffTimerSeqOutOfRng,
       "docsQosCmtsDsidCurrentSeqNum": docsQosCmtsDsidCurrentSeqNum,
       "docsQosCmtsDebugDsidTable": docsQosCmtsDebugDsidTable,
       "docsQosCmtsDebugDsidEntry": docsQosCmtsDebugDsidEntry,
       "docsQosCmtsDebugDsidDsid": docsQosCmtsDebugDsidDsid,
       "docsQosCmtsDebugDsidRowStatus": docsQosCmtsDebugDsidRowStatus,
       "docsQosCmtsDebugDsidStatsTable": docsQosCmtsDebugDsidStatsTable,
       "docsQosCmtsDebugDsidStatsEntry": docsQosCmtsDebugDsidStatsEntry,
       "docsQosCmtsDebugDsidStatsDsIfIndex": docsQosCmtsDebugDsidStatsDsIfIndex,
       "docsQosCmtsDebugDsidStatsDsidPackets": docsQosCmtsDebugDsidStatsDsidPackets,
       "docsQosCmtsDebugDsidStatsDsidOctets": docsQosCmtsDebugDsidStatsDsidOctets,
       "docsQosCmDsidTable": docsQosCmDsidTable,
       "docsQosCmDsidEntry": docsQosCmDsidEntry,
       "docsQosCmDsidDsid": docsQosCmDsidDsid,
       "docsQosCmDsidUsage": docsQosCmDsidUsage,
       "docsQosCmDsidNumReseqChs": docsQosCmDsidNumReseqChs,
       "docsQosCmDsidReseqChList": docsQosCmDsidReseqChList,
       "docsQosCmDsidReseqWaitTime": docsQosCmDsidReseqWaitTime,
       "docsQosCmDsidReseqWarnThrshld": docsQosCmDsidReseqWarnThrshld,
       "docsQosCmDsidStatusHldoffTimerSeqOutOfRng": docsQosCmDsidStatusHldoffTimerSeqOutOfRng,
       "docsQosCmDsidOutOfRangeDiscards": docsQosCmDsidOutOfRangeDiscards,
       "docsQosCmDsidNextExpectedSeqNum": docsQosCmDsidNextExpectedSeqNum,
       "docsQosCmDsidCmInterfaceMask": docsQosCmDsidCmInterfaceMask,
       "docsQosCmDsidFwdCmInterfaceMask": docsQosCmDsidFwdCmInterfaceMask,
       "docsQosCmDsidStatsTable": docsQosCmDsidStatsTable,
       "docsQosCmDsidStatsEntry": docsQosCmDsidStatsEntry,
       "docsQosCmDsidStatsDsid": docsQosCmDsidStatsDsid,
       "docsQosCmDsidStatsSeqNumMissing": docsQosCmDsidStatsSeqNumMissing,
       "docsQosCmDsidStatsSkewThreshExceeds": docsQosCmDsidStatsSkewThreshExceeds,
       "docsQosCmDsidStatsOutOfRangePackets": docsQosCmDsidStatsOutOfRangePackets,
       "docsQosCmDsidStatsNumPackets": docsQosCmDsidStatsNumPackets,
       "docsQosCmDsidClientTable": docsQosCmDsidClientTable,
       "docsQosCmDsidClientEntry": docsQosCmDsidClientEntry,
       "docsQosCmDsidClientDsid": docsQosCmDsidClientDsid,
       "docsQosCmDsidClientClientMacId": docsQosCmDsidClientClientMacId,
       "docsQosCmDsidClientClientMacAddr": docsQosCmDsidClientClientMacAddr,
       "docsQosCmSystemCfgState": docsQosCmSystemCfgState,
       "docsQosCmSystemCfgStateAqmUsEnable": docsQosCmSystemCfgStateAqmUsEnable,
       "docsQosCmSystemCfgStateDefaultUsTargetBuffer": docsQosCmSystemCfgStateDefaultUsTargetBuffer,
       "docsQosCmtsIatcProfileStatsTable": docsQosCmtsIatcProfileStatsTable,
       "docsQosCmtsIatcProfileStatsEntry": docsQosCmtsIatcProfileStatsEntry,
       "docsQosCmtsIatcProfileStatsName": docsQosCmtsIatcProfileStatsName,
       "docsQosCmtsIatcProfileStatsIfIndex": docsQosCmtsIatcProfileStatsIfIndex,
       "docsQosCmtsIatcProfileStatsDirection": docsQosCmtsIatcProfileStatsDirection,
       "docsQosCmtsIatcProfileStatsPkts": docsQosCmtsIatcProfileStatsPkts,
       "docsQosCmtsIatcProfileStatsOctets": docsQosCmtsIatcProfileStatsOctets,
       "docsQosCmtsIatcProfileStatsPolicedDropPkts": docsQosCmtsIatcProfileStatsPolicedDropPkts,
       "docsQosCmtsIatcProfileStatsPolicedDelayPkts": docsQosCmtsIatcProfileStatsPolicedDelayPkts,
       "docsQosMibConformance": docsQosMibConformance,
       "docsQosMibCompliances": docsQosMibCompliances,
       "docsQosCompliance": docsQosCompliance,
       "docsQosDeprecatedCompliance": docsQosDeprecatedCompliance,
       "docsQosMibGroups": docsQosMibGroups,
       "docsQosBaseGroup": docsQosBaseGroup,
       "docsQosCmtsGroup": docsQosCmtsGroup,
       "docsQosCmGroup": docsQosCmGroup,
       "docsQosDeprecatedGroup": docsQosDeprecatedGroup,
       "docsQosObsoleteGroup": docsQosObsoleteGroup}
)
