# SNMP MIB module (CISCO-ITP-GSP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-GSP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:26 2024
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

(cgspInstNetwork,) = mibBuilder.importSymbols(
    "CISCO-ITP-GSP-MIB",
    "cgspInstNetwork")

(CItpTcAclId,
 CItpTcLinkSLC,
 CItpTcLinksetId,
 CItpTcNetworkName,
 CItpTcPointCode,
 CItpTcXuaName) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcAclId",
    "CItpTcLinkSLC",
    "CItpTcLinksetId",
    "CItpTcNetworkName",
    "CItpTcPointCode",
    "CItpTcXuaName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoGsp2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332)
)
ciscoGsp2MIB.setRevisions(
        ("2008-07-09 00:00",
         "2007-12-18 00:00",
         "2004-05-26 00:00",
         "2003-08-07 00:00",
         "2003-03-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Cgsp2TcQosClass(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Cgsp2EventIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CItpTcContextId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CItpTcContextType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("asp", 6),
          ("cs7link", 1),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoGsp2MIBNotifs_ObjectIdentity = ObjectIdentity
ciscoGsp2MIBNotifs = _CiscoGsp2MIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 0)
)
_CiscoGsp2MIBObjects_ObjectIdentity = ObjectIdentity
ciscoGsp2MIBObjects = _CiscoGsp2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1)
)
_Cgsp2Events_ObjectIdentity = ObjectIdentity
cgsp2Events = _Cgsp2Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1)
)
_Cgsp2EventTable_Object = MibTable
cgsp2EventTable = _Cgsp2EventTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cgsp2EventTable.setStatus("current")
_Cgsp2EventTableEntry_Object = MibTableRow
cgsp2EventTableEntry = _Cgsp2EventTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1)
)
cgsp2EventTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventType"),
)
if mibBuilder.loadTexts:
    cgsp2EventTableEntry.setStatus("current")


class _Cgsp2EventType_Type(Integer32):
    """Custom type cgsp2EventType based on Integer32"""
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
        *(("as", 1),
          ("asp", 2),
          ("mtp3", 3),
          ("pc", 4))
    )


_Cgsp2EventType_Type.__name__ = "Integer32"
_Cgsp2EventType_Object = MibTableColumn
cgsp2EventType = _Cgsp2EventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 1),
    _Cgsp2EventType_Type()
)
cgsp2EventType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2EventType.setStatus("current")
_Cgsp2EventLoggedEvents_Type = Counter32
_Cgsp2EventLoggedEvents_Object = MibTableColumn
cgsp2EventLoggedEvents = _Cgsp2EventLoggedEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 2),
    _Cgsp2EventLoggedEvents_Type()
)
cgsp2EventLoggedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventLoggedEvents.setStatus("current")
_Cgsp2EventDroppedEvents_Type = Counter32
_Cgsp2EventDroppedEvents_Object = MibTableColumn
cgsp2EventDroppedEvents = _Cgsp2EventDroppedEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 3),
    _Cgsp2EventDroppedEvents_Type()
)
cgsp2EventDroppedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventDroppedEvents.setStatus("current")


class _Cgsp2EventMaxEntries_Type(Unsigned32):
    """Custom type cgsp2EventMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cgsp2EventMaxEntries_Type.__name__ = "Unsigned32"
_Cgsp2EventMaxEntries_Object = MibTableColumn
cgsp2EventMaxEntries = _Cgsp2EventMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 4),
    _Cgsp2EventMaxEntries_Type()
)
cgsp2EventMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsp2EventMaxEntries.setStatus("current")


class _Cgsp2EventMaxEntriesAllowed_Type(Unsigned32):
    """Custom type cgsp2EventMaxEntriesAllowed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cgsp2EventMaxEntriesAllowed_Type.__name__ = "Unsigned32"
_Cgsp2EventMaxEntriesAllowed_Object = MibTableColumn
cgsp2EventMaxEntriesAllowed = _Cgsp2EventMaxEntriesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 1, 1, 5),
    _Cgsp2EventMaxEntriesAllowed_Type()
)
cgsp2EventMaxEntriesAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventMaxEntriesAllowed.setStatus("current")
_Cgsp2EventAsTable_Object = MibTable
cgsp2EventAsTable = _Cgsp2EventAsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cgsp2EventAsTable.setStatus("current")
_Cgsp2EventAsTableEntry_Object = MibTableRow
cgsp2EventAsTableEntry = _Cgsp2EventAsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1)
)
cgsp2EventAsTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventAsName"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventAsIndex"),
)
if mibBuilder.loadTexts:
    cgsp2EventAsTableEntry.setStatus("current")
_Cgsp2EventAsName_Type = CItpTcXuaName
_Cgsp2EventAsName_Object = MibTableColumn
cgsp2EventAsName = _Cgsp2EventAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1, 1),
    _Cgsp2EventAsName_Type()
)
cgsp2EventAsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2EventAsName.setStatus("current")
_Cgsp2EventAsIndex_Type = Cgsp2EventIndex
_Cgsp2EventAsIndex_Object = MibTableColumn
cgsp2EventAsIndex = _Cgsp2EventAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1, 2),
    _Cgsp2EventAsIndex_Type()
)
cgsp2EventAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2EventAsIndex.setStatus("current")


class _Cgsp2EventAsText_Type(SnmpAdminString):
    """Custom type cgsp2EventAsText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cgsp2EventAsText_Type.__name__ = "SnmpAdminString"
_Cgsp2EventAsText_Object = MibTableColumn
cgsp2EventAsText = _Cgsp2EventAsText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1, 3),
    _Cgsp2EventAsText_Type()
)
cgsp2EventAsText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventAsText.setStatus("current")
_Cgsp2EventAsTimestamp_Type = TimeStamp
_Cgsp2EventAsTimestamp_Object = MibTableColumn
cgsp2EventAsTimestamp = _Cgsp2EventAsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 2, 1, 4),
    _Cgsp2EventAsTimestamp_Type()
)
cgsp2EventAsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventAsTimestamp.setStatus("current")
_Cgsp2EventAspTable_Object = MibTable
cgsp2EventAspTable = _Cgsp2EventAspTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cgsp2EventAspTable.setStatus("current")
_Cgsp2EventAspTableEntry_Object = MibTableRow
cgsp2EventAspTableEntry = _Cgsp2EventAspTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1)
)
cgsp2EventAspTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventAspName"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventAspIndex"),
)
if mibBuilder.loadTexts:
    cgsp2EventAspTableEntry.setStatus("current")
_Cgsp2EventAspName_Type = CItpTcXuaName
_Cgsp2EventAspName_Object = MibTableColumn
cgsp2EventAspName = _Cgsp2EventAspName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1, 1),
    _Cgsp2EventAspName_Type()
)
cgsp2EventAspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2EventAspName.setStatus("current")
_Cgsp2EventAspIndex_Type = Cgsp2EventIndex
_Cgsp2EventAspIndex_Object = MibTableColumn
cgsp2EventAspIndex = _Cgsp2EventAspIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1, 2),
    _Cgsp2EventAspIndex_Type()
)
cgsp2EventAspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2EventAspIndex.setStatus("current")


class _Cgsp2EventAspText_Type(SnmpAdminString):
    """Custom type cgsp2EventAspText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cgsp2EventAspText_Type.__name__ = "SnmpAdminString"
_Cgsp2EventAspText_Object = MibTableColumn
cgsp2EventAspText = _Cgsp2EventAspText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1, 3),
    _Cgsp2EventAspText_Type()
)
cgsp2EventAspText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventAspText.setStatus("current")
_Cgsp2EventAspTimestamp_Type = TimeStamp
_Cgsp2EventAspTimestamp_Object = MibTableColumn
cgsp2EventAspTimestamp = _Cgsp2EventAspTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 3, 1, 4),
    _Cgsp2EventAspTimestamp_Type()
)
cgsp2EventAspTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventAspTimestamp.setStatus("current")
_Cgsp2EventMtp3Table_Object = MibTable
cgsp2EventMtp3Table = _Cgsp2EventMtp3Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cgsp2EventMtp3Table.setStatus("current")
_Cgsp2EventMtp3TableEntry_Object = MibTableRow
cgsp2EventMtp3TableEntry = _Cgsp2EventMtp3TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4, 1)
)
cgsp2EventMtp3TableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventMtp3Index"),
)
if mibBuilder.loadTexts:
    cgsp2EventMtp3TableEntry.setStatus("current")
_Cgsp2EventMtp3Index_Type = Cgsp2EventIndex
_Cgsp2EventMtp3Index_Object = MibTableColumn
cgsp2EventMtp3Index = _Cgsp2EventMtp3Index_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4, 1, 1),
    _Cgsp2EventMtp3Index_Type()
)
cgsp2EventMtp3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2EventMtp3Index.setStatus("current")


class _Cgsp2EventMtp3Text_Type(SnmpAdminString):
    """Custom type cgsp2EventMtp3Text based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cgsp2EventMtp3Text_Type.__name__ = "SnmpAdminString"
_Cgsp2EventMtp3Text_Object = MibTableColumn
cgsp2EventMtp3Text = _Cgsp2EventMtp3Text_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4, 1, 2),
    _Cgsp2EventMtp3Text_Type()
)
cgsp2EventMtp3Text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventMtp3Text.setStatus("current")
_Cgsp2EventMtp3Timestamp_Type = TimeStamp
_Cgsp2EventMtp3Timestamp_Object = MibTableColumn
cgsp2EventMtp3Timestamp = _Cgsp2EventMtp3Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 4, 1, 3),
    _Cgsp2EventMtp3Timestamp_Type()
)
cgsp2EventMtp3Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventMtp3Timestamp.setStatus("current")
_Cgsp2EventPcTable_Object = MibTable
cgsp2EventPcTable = _Cgsp2EventPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cgsp2EventPcTable.setStatus("current")
_Cgsp2EventPcTableEntry_Object = MibTableRow
cgsp2EventPcTableEntry = _Cgsp2EventPcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1)
)
cgsp2EventPcTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventPc"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2EventPcIndex"),
)
if mibBuilder.loadTexts:
    cgsp2EventPcTableEntry.setStatus("current")
_Cgsp2EventPc_Type = CItpTcPointCode
_Cgsp2EventPc_Object = MibTableColumn
cgsp2EventPc = _Cgsp2EventPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1, 1),
    _Cgsp2EventPc_Type()
)
cgsp2EventPc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2EventPc.setStatus("current")
_Cgsp2EventPcIndex_Type = Cgsp2EventIndex
_Cgsp2EventPcIndex_Object = MibTableColumn
cgsp2EventPcIndex = _Cgsp2EventPcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1, 2),
    _Cgsp2EventPcIndex_Type()
)
cgsp2EventPcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2EventPcIndex.setStatus("current")


class _Cgsp2EventPcText_Type(SnmpAdminString):
    """Custom type cgsp2EventPcText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cgsp2EventPcText_Type.__name__ = "SnmpAdminString"
_Cgsp2EventPcText_Object = MibTableColumn
cgsp2EventPcText = _Cgsp2EventPcText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1, 3),
    _Cgsp2EventPcText_Type()
)
cgsp2EventPcText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventPcText.setStatus("current")
_Cgsp2EventPcTimestamp_Type = TimeStamp
_Cgsp2EventPcTimestamp_Object = MibTableColumn
cgsp2EventPcTimestamp = _Cgsp2EventPcTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 1, 5, 1, 4),
    _Cgsp2EventPcTimestamp_Type()
)
cgsp2EventPcTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2EventPcTimestamp.setStatus("current")
_Cgsp2Qos_ObjectIdentity = ObjectIdentity
cgsp2Qos = _Cgsp2Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2)
)
_Cgsp2QosTable_Object = MibTable
cgsp2QosTable = _Cgsp2QosTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cgsp2QosTable.setStatus("current")
_Cgsp2QosTableEntry_Object = MibTableRow
cgsp2QosTableEntry = _Cgsp2QosTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1)
)
cgsp2QosTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2QosClass"),
)
if mibBuilder.loadTexts:
    cgsp2QosTableEntry.setStatus("current")
_Cgsp2QosClass_Type = Cgsp2TcQosClass
_Cgsp2QosClass_Object = MibTableColumn
cgsp2QosClass = _Cgsp2QosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 1),
    _Cgsp2QosClass_Type()
)
cgsp2QosClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2QosClass.setStatus("current")


class _Cgsp2QosType_Type(Integer32):
    """Custom type cgsp2QosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipDscp", 2),
          ("ipPrecedence", 1))
    )


_Cgsp2QosType_Type.__name__ = "Integer32"
_Cgsp2QosType_Object = MibTableColumn
cgsp2QosType = _Cgsp2QosType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 2),
    _Cgsp2QosType_Type()
)
cgsp2QosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsp2QosType.setStatus("current")


class _Cgsp2QosPrecedenceValue_Type(Integer32):
    """Custom type cgsp2QosPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_Cgsp2QosPrecedenceValue_Type.__name__ = "Integer32"
_Cgsp2QosPrecedenceValue_Object = MibTableColumn
cgsp2QosPrecedenceValue = _Cgsp2QosPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 3),
    _Cgsp2QosPrecedenceValue_Type()
)
cgsp2QosPrecedenceValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsp2QosPrecedenceValue.setStatus("current")


class _Cgsp2QosIpDscp_Type(Integer32):
    """Custom type cgsp2QosIpDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_Cgsp2QosIpDscp_Type.__name__ = "Integer32"
_Cgsp2QosIpDscp_Object = MibTableColumn
cgsp2QosIpDscp = _Cgsp2QosIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 4),
    _Cgsp2QosIpDscp_Type()
)
cgsp2QosIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsp2QosIpDscp.setStatus("current")


class _Cgsp2QosAclId_Type(CItpTcAclId):
    """Custom type cgsp2QosAclId based on CItpTcAclId"""
    defaultValue = 0


_Cgsp2QosAclId_Object = MibTableColumn
cgsp2QosAclId = _Cgsp2QosAclId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 5),
    _Cgsp2QosAclId_Type()
)
cgsp2QosAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsp2QosAclId.setStatus("current")
_Cgsp2QosRowStatus_Type = RowStatus
_Cgsp2QosRowStatus_Object = MibTableColumn
cgsp2QosRowStatus = _Cgsp2QosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 2, 1, 1, 6),
    _Cgsp2QosRowStatus_Type()
)
cgsp2QosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsp2QosRowStatus.setStatus("current")
_Cgsp2LocalPeer_ObjectIdentity = ObjectIdentity
cgsp2LocalPeer = _Cgsp2LocalPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3)
)
_Cgsp2LocalPeerTable_Object = MibTable
cgsp2LocalPeerTable = _Cgsp2LocalPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cgsp2LocalPeerTable.setStatus("current")
_Cgsp2LocalPeerTableEntry_Object = MibTableRow
cgsp2LocalPeerTableEntry = _Cgsp2LocalPeerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1)
)
cgsp2LocalPeerTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerPort"),
)
if mibBuilder.loadTexts:
    cgsp2LocalPeerTableEntry.setStatus("current")
_Cgsp2LocalPeerPort_Type = InetPortNumber
_Cgsp2LocalPeerPort_Object = MibTableColumn
cgsp2LocalPeerPort = _Cgsp2LocalPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1, 1),
    _Cgsp2LocalPeerPort_Type()
)
cgsp2LocalPeerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2LocalPeerPort.setStatus("current")


class _Cgsp2LocalPeerSlotNumber_Type(Integer32):
    """Custom type cgsp2LocalPeerSlotNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_Cgsp2LocalPeerSlotNumber_Type.__name__ = "Integer32"
_Cgsp2LocalPeerSlotNumber_Object = MibTableColumn
cgsp2LocalPeerSlotNumber = _Cgsp2LocalPeerSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1, 2),
    _Cgsp2LocalPeerSlotNumber_Type()
)
cgsp2LocalPeerSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2LocalPeerSlotNumber.setStatus("current")
_Cgsp2LocalPeerRowStatus_Type = RowStatus
_Cgsp2LocalPeerRowStatus_Object = MibTableColumn
cgsp2LocalPeerRowStatus = _Cgsp2LocalPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1, 3),
    _Cgsp2LocalPeerRowStatus_Type()
)
cgsp2LocalPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsp2LocalPeerRowStatus.setStatus("current")


class _Cgsp2LocalPeerProcessorNumber_Type(Integer32):
    """Custom type cgsp2LocalPeerProcessorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cgsp2LocalPeerProcessorNumber_Type.__name__ = "Integer32"
_Cgsp2LocalPeerProcessorNumber_Object = MibTableColumn
cgsp2LocalPeerProcessorNumber = _Cgsp2LocalPeerProcessorNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 1, 1, 4),
    _Cgsp2LocalPeerProcessorNumber_Type()
)
cgsp2LocalPeerProcessorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2LocalPeerProcessorNumber.setStatus("current")
_Cgsp2LpIpAddrTable_Object = MibTable
cgsp2LpIpAddrTable = _Cgsp2LpIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cgsp2LpIpAddrTable.setStatus("current")
_Cgsp2LpIpAddrTableEntry_Object = MibTableRow
cgsp2LpIpAddrTableEntry = _Cgsp2LpIpAddrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1)
)
cgsp2LpIpAddrTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerPort"),
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2LpIpAddressNumber"),
)
if mibBuilder.loadTexts:
    cgsp2LpIpAddrTableEntry.setStatus("current")


class _Cgsp2LpIpAddressNumber_Type(Unsigned32):
    """Custom type cgsp2LpIpAddressNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cgsp2LpIpAddressNumber_Type.__name__ = "Unsigned32"
_Cgsp2LpIpAddressNumber_Object = MibTableColumn
cgsp2LpIpAddressNumber = _Cgsp2LpIpAddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1, 1),
    _Cgsp2LpIpAddressNumber_Type()
)
cgsp2LpIpAddressNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2LpIpAddressNumber.setStatus("current")
_Cgsp2LpIpAddressType_Type = InetAddressType
_Cgsp2LpIpAddressType_Object = MibTableColumn
cgsp2LpIpAddressType = _Cgsp2LpIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1, 2),
    _Cgsp2LpIpAddressType_Type()
)
cgsp2LpIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsp2LpIpAddressType.setStatus("current")
_Cgsp2LpIpAddress_Type = InetAddress
_Cgsp2LpIpAddress_Object = MibTableColumn
cgsp2LpIpAddress = _Cgsp2LpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1, 3),
    _Cgsp2LpIpAddress_Type()
)
cgsp2LpIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsp2LpIpAddress.setStatus("current")
_Cgsp2LpIpAddressRowStatus_Type = RowStatus
_Cgsp2LpIpAddressRowStatus_Object = MibTableColumn
cgsp2LpIpAddressRowStatus = _Cgsp2LpIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 3, 2, 1, 4),
    _Cgsp2LpIpAddressRowStatus_Type()
)
cgsp2LpIpAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsp2LpIpAddressRowStatus.setStatus("current")
_Cgsp2Mtp3Errors_ObjectIdentity = ObjectIdentity
cgsp2Mtp3Errors = _Cgsp2Mtp3Errors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4)
)
_Cgsp2Mtp3ErrorsTable_Object = MibTable
cgsp2Mtp3ErrorsTable = _Cgsp2Mtp3ErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cgsp2Mtp3ErrorsTable.setStatus("current")
_Cgsp2Mtp3ErrorsTableEntry_Object = MibTableRow
cgsp2Mtp3ErrorsTableEntry = _Cgsp2Mtp3ErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1, 1)
)
cgsp2Mtp3ErrorsTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2Mtp3ErrorsType"),
)
if mibBuilder.loadTexts:
    cgsp2Mtp3ErrorsTableEntry.setStatus("current")


class _Cgsp2Mtp3ErrorsType_Type(Unsigned32):
    """Custom type cgsp2Mtp3ErrorsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cgsp2Mtp3ErrorsType_Type.__name__ = "Unsigned32"
_Cgsp2Mtp3ErrorsType_Object = MibTableColumn
cgsp2Mtp3ErrorsType = _Cgsp2Mtp3ErrorsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1, 1, 1),
    _Cgsp2Mtp3ErrorsType_Type()
)
cgsp2Mtp3ErrorsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2Mtp3ErrorsType.setStatus("current")


class _Cgsp2Mtp3ErrorsDescription_Type(SnmpAdminString):
    """Custom type cgsp2Mtp3ErrorsDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cgsp2Mtp3ErrorsDescription_Type.__name__ = "SnmpAdminString"
_Cgsp2Mtp3ErrorsDescription_Object = MibTableColumn
cgsp2Mtp3ErrorsDescription = _Cgsp2Mtp3ErrorsDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1, 1, 2),
    _Cgsp2Mtp3ErrorsDescription_Type()
)
cgsp2Mtp3ErrorsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2Mtp3ErrorsDescription.setStatus("current")
_Cgsp2Mtp3ErrorsCount_Type = Counter64
_Cgsp2Mtp3ErrorsCount_Object = MibTableColumn
cgsp2Mtp3ErrorsCount = _Cgsp2Mtp3ErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 4, 1, 1, 3),
    _Cgsp2Mtp3ErrorsCount_Type()
)
cgsp2Mtp3ErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2Mtp3ErrorsCount.setStatus("current")
_Cgsp2Operation_ObjectIdentity = ObjectIdentity
cgsp2Operation = _Cgsp2Operation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 5)
)


class _Cgsp2OperMtp3Offload_Type(Integer32):
    """Custom type cgsp2OperMtp3Offload based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("offload", 2))
    )


_Cgsp2OperMtp3Offload_Type.__name__ = "Integer32"
_Cgsp2OperMtp3Offload_Object = MibScalar
cgsp2OperMtp3Offload = _Cgsp2OperMtp3Offload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 5, 1),
    _Cgsp2OperMtp3Offload_Type()
)
cgsp2OperMtp3Offload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2OperMtp3Offload.setStatus("current")


class _Cgsp2OperRedundancy_Type(Integer32):
    """Custom type cgsp2OperRedundancy based on Integer32"""
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
        *(("distributed", 3),
          ("local", 2),
          ("none", 1))
    )


_Cgsp2OperRedundancy_Type.__name__ = "Integer32"
_Cgsp2OperRedundancy_Object = MibScalar
cgsp2OperRedundancy = _Cgsp2OperRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 5, 2),
    _Cgsp2OperRedundancy_Type()
)
cgsp2OperRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2OperRedundancy.setStatus("current")
_Cgsp2Context_ObjectIdentity = ObjectIdentity
cgsp2Context = _Cgsp2Context_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6)
)
_Cgsp2ContextTable_Object = MibTable
cgsp2ContextTable = _Cgsp2ContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cgsp2ContextTable.setStatus("current")
_Cgsp2ContextEntry_Object = MibTableRow
cgsp2ContextEntry = _Cgsp2ContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1)
)
cgsp2ContextEntry.setIndexNames(
    (0, "CISCO-ITP-GSP2-MIB", "cgsp2ContextIdentifier"),
)
if mibBuilder.loadTexts:
    cgsp2ContextEntry.setStatus("current")
_Cgsp2ContextIdentifier_Type = CItpTcContextId
_Cgsp2ContextIdentifier_Object = MibTableColumn
cgsp2ContextIdentifier = _Cgsp2ContextIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 1),
    _Cgsp2ContextIdentifier_Type()
)
cgsp2ContextIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsp2ContextIdentifier.setStatus("current")
_Cgsp2ContextType_Type = CItpTcContextType
_Cgsp2ContextType_Object = MibTableColumn
cgsp2ContextType = _Cgsp2ContextType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 2),
    _Cgsp2ContextType_Type()
)
cgsp2ContextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2ContextType.setStatus("current")
_Cgsp2ContextLinksetName_Type = CItpTcLinksetId
_Cgsp2ContextLinksetName_Object = MibTableColumn
cgsp2ContextLinksetName = _Cgsp2ContextLinksetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 3),
    _Cgsp2ContextLinksetName_Type()
)
cgsp2ContextLinksetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2ContextLinksetName.setStatus("current")
_Cgsp2ContextSlc_Type = CItpTcLinkSLC
_Cgsp2ContextSlc_Object = MibTableColumn
cgsp2ContextSlc = _Cgsp2ContextSlc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 4),
    _Cgsp2ContextSlc_Type()
)
cgsp2ContextSlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2ContextSlc.setStatus("current")
_Cgsp2ContextAsName_Type = CItpTcXuaName
_Cgsp2ContextAsName_Object = MibTableColumn
cgsp2ContextAsName = _Cgsp2ContextAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 5),
    _Cgsp2ContextAsName_Type()
)
cgsp2ContextAsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2ContextAsName.setStatus("current")
_Cgsp2ContextAspName_Type = CItpTcXuaName
_Cgsp2ContextAspName_Object = MibTableColumn
cgsp2ContextAspName = _Cgsp2ContextAspName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 6),
    _Cgsp2ContextAspName_Type()
)
cgsp2ContextAspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2ContextAspName.setStatus("current")
_Cgsp2ContextNetworkName_Type = CItpTcNetworkName
_Cgsp2ContextNetworkName_Object = MibTableColumn
cgsp2ContextNetworkName = _Cgsp2ContextNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 1, 6, 1, 1, 7),
    _Cgsp2ContextNetworkName_Type()
)
cgsp2ContextNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsp2ContextNetworkName.setStatus("current")
_CiscoGsp2MIBConform_ObjectIdentity = ObjectIdentity
ciscoGsp2MIBConform = _CiscoGsp2MIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2)
)
_CiscoGsp2MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGsp2MIBCompliances = _CiscoGsp2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1)
)
_CiscoGsp2MIBGroups_ObjectIdentity = ObjectIdentity
ciscoGsp2MIBGroups = _CiscoGsp2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2)
)

# Managed Objects groups

ciscoGsp2EventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 1)
)
ciscoGsp2EventsGroup.setObjects(
      *(("CISCO-ITP-GSP2-MIB", "cgsp2EventLoggedEvents"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventDroppedEvents"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventMaxEntries"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventMaxEntriesAllowed"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventMtp3Text"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventMtp3Timestamp"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventAsText"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventAsTimestamp"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventAspText"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventAspTimestamp"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventPcText"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2EventPcTimestamp"))
)
if mibBuilder.loadTexts:
    ciscoGsp2EventsGroup.setStatus("current")

ciscoGsp2QosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 2)
)
ciscoGsp2QosGroup.setObjects(
      *(("CISCO-ITP-GSP2-MIB", "cgsp2QosType"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2QosPrecedenceValue"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2QosIpDscp"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2QosAclId"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2QosRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsp2QosGroup.setStatus("current")

ciscoGsp2LocalPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 3)
)
ciscoGsp2LocalPeerGroup.setObjects(
      *(("CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerSlotNumber"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerRowStatus"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2LpIpAddressType"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2LpIpAddress"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2LpIpAddressRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsp2LocalPeerGroup.setStatus("current")

ciscoGsp2Mtp3ErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 4)
)
ciscoGsp2Mtp3ErrorsGroup.setObjects(
      *(("CISCO-ITP-GSP2-MIB", "cgsp2Mtp3ErrorsDescription"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2Mtp3ErrorsCount"))
)
if mibBuilder.loadTexts:
    ciscoGsp2Mtp3ErrorsGroup.setStatus("current")

ciscoGsp2OperationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 5)
)
ciscoGsp2OperationGroup.setObjects(
      *(("CISCO-ITP-GSP2-MIB", "cgsp2OperMtp3Offload"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2OperRedundancy"))
)
if mibBuilder.loadTexts:
    ciscoGsp2OperationGroup.setStatus("current")

ciscoGsp2LocalPeerGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 6)
)
ciscoGsp2LocalPeerGroupSup1.setObjects(
    ("CISCO-ITP-GSP2-MIB", "cgsp2LocalPeerProcessorNumber")
)
if mibBuilder.loadTexts:
    ciscoGsp2LocalPeerGroupSup1.setStatus("current")

ciscoGsp2ContextGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 2, 7)
)
ciscoGsp2ContextGroup.setObjects(
      *(("CISCO-ITP-GSP2-MIB", "cgsp2ContextType"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2ContextLinksetName"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2ContextSlc"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2ContextAsName"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2ContextAspName"),
        ("CISCO-ITP-GSP2-MIB", "cgsp2ContextNetworkName"))
)
if mibBuilder.loadTexts:
    ciscoGsp2ContextGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoGsp2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGsp2MIBCompliance.setStatus(
        "deprecated"
    )

ciscoGsp2MIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoGsp2MIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoGsp2MIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoGsp2MIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoGsp2MIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoGsp2MIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoGsp2MIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 332, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoGsp2MIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-GSP2-MIB",
    **{"Cgsp2TcQosClass": Cgsp2TcQosClass,
       "Cgsp2EventIndex": Cgsp2EventIndex,
       "CItpTcContextId": CItpTcContextId,
       "CItpTcContextType": CItpTcContextType,
       "ciscoGsp2MIB": ciscoGsp2MIB,
       "ciscoGsp2MIBNotifs": ciscoGsp2MIBNotifs,
       "ciscoGsp2MIBObjects": ciscoGsp2MIBObjects,
       "cgsp2Events": cgsp2Events,
       "cgsp2EventTable": cgsp2EventTable,
       "cgsp2EventTableEntry": cgsp2EventTableEntry,
       "cgsp2EventType": cgsp2EventType,
       "cgsp2EventLoggedEvents": cgsp2EventLoggedEvents,
       "cgsp2EventDroppedEvents": cgsp2EventDroppedEvents,
       "cgsp2EventMaxEntries": cgsp2EventMaxEntries,
       "cgsp2EventMaxEntriesAllowed": cgsp2EventMaxEntriesAllowed,
       "cgsp2EventAsTable": cgsp2EventAsTable,
       "cgsp2EventAsTableEntry": cgsp2EventAsTableEntry,
       "cgsp2EventAsName": cgsp2EventAsName,
       "cgsp2EventAsIndex": cgsp2EventAsIndex,
       "cgsp2EventAsText": cgsp2EventAsText,
       "cgsp2EventAsTimestamp": cgsp2EventAsTimestamp,
       "cgsp2EventAspTable": cgsp2EventAspTable,
       "cgsp2EventAspTableEntry": cgsp2EventAspTableEntry,
       "cgsp2EventAspName": cgsp2EventAspName,
       "cgsp2EventAspIndex": cgsp2EventAspIndex,
       "cgsp2EventAspText": cgsp2EventAspText,
       "cgsp2EventAspTimestamp": cgsp2EventAspTimestamp,
       "cgsp2EventMtp3Table": cgsp2EventMtp3Table,
       "cgsp2EventMtp3TableEntry": cgsp2EventMtp3TableEntry,
       "cgsp2EventMtp3Index": cgsp2EventMtp3Index,
       "cgsp2EventMtp3Text": cgsp2EventMtp3Text,
       "cgsp2EventMtp3Timestamp": cgsp2EventMtp3Timestamp,
       "cgsp2EventPcTable": cgsp2EventPcTable,
       "cgsp2EventPcTableEntry": cgsp2EventPcTableEntry,
       "cgsp2EventPc": cgsp2EventPc,
       "cgsp2EventPcIndex": cgsp2EventPcIndex,
       "cgsp2EventPcText": cgsp2EventPcText,
       "cgsp2EventPcTimestamp": cgsp2EventPcTimestamp,
       "cgsp2Qos": cgsp2Qos,
       "cgsp2QosTable": cgsp2QosTable,
       "cgsp2QosTableEntry": cgsp2QosTableEntry,
       "cgsp2QosClass": cgsp2QosClass,
       "cgsp2QosType": cgsp2QosType,
       "cgsp2QosPrecedenceValue": cgsp2QosPrecedenceValue,
       "cgsp2QosIpDscp": cgsp2QosIpDscp,
       "cgsp2QosAclId": cgsp2QosAclId,
       "cgsp2QosRowStatus": cgsp2QosRowStatus,
       "cgsp2LocalPeer": cgsp2LocalPeer,
       "cgsp2LocalPeerTable": cgsp2LocalPeerTable,
       "cgsp2LocalPeerTableEntry": cgsp2LocalPeerTableEntry,
       "cgsp2LocalPeerPort": cgsp2LocalPeerPort,
       "cgsp2LocalPeerSlotNumber": cgsp2LocalPeerSlotNumber,
       "cgsp2LocalPeerRowStatus": cgsp2LocalPeerRowStatus,
       "cgsp2LocalPeerProcessorNumber": cgsp2LocalPeerProcessorNumber,
       "cgsp2LpIpAddrTable": cgsp2LpIpAddrTable,
       "cgsp2LpIpAddrTableEntry": cgsp2LpIpAddrTableEntry,
       "cgsp2LpIpAddressNumber": cgsp2LpIpAddressNumber,
       "cgsp2LpIpAddressType": cgsp2LpIpAddressType,
       "cgsp2LpIpAddress": cgsp2LpIpAddress,
       "cgsp2LpIpAddressRowStatus": cgsp2LpIpAddressRowStatus,
       "cgsp2Mtp3Errors": cgsp2Mtp3Errors,
       "cgsp2Mtp3ErrorsTable": cgsp2Mtp3ErrorsTable,
       "cgsp2Mtp3ErrorsTableEntry": cgsp2Mtp3ErrorsTableEntry,
       "cgsp2Mtp3ErrorsType": cgsp2Mtp3ErrorsType,
       "cgsp2Mtp3ErrorsDescription": cgsp2Mtp3ErrorsDescription,
       "cgsp2Mtp3ErrorsCount": cgsp2Mtp3ErrorsCount,
       "cgsp2Operation": cgsp2Operation,
       "cgsp2OperMtp3Offload": cgsp2OperMtp3Offload,
       "cgsp2OperRedundancy": cgsp2OperRedundancy,
       "cgsp2Context": cgsp2Context,
       "cgsp2ContextTable": cgsp2ContextTable,
       "cgsp2ContextEntry": cgsp2ContextEntry,
       "cgsp2ContextIdentifier": cgsp2ContextIdentifier,
       "cgsp2ContextType": cgsp2ContextType,
       "cgsp2ContextLinksetName": cgsp2ContextLinksetName,
       "cgsp2ContextSlc": cgsp2ContextSlc,
       "cgsp2ContextAsName": cgsp2ContextAsName,
       "cgsp2ContextAspName": cgsp2ContextAspName,
       "cgsp2ContextNetworkName": cgsp2ContextNetworkName,
       "ciscoGsp2MIBConform": ciscoGsp2MIBConform,
       "ciscoGsp2MIBCompliances": ciscoGsp2MIBCompliances,
       "ciscoGsp2MIBCompliance": ciscoGsp2MIBCompliance,
       "ciscoGsp2MIBComplianceRev1": ciscoGsp2MIBComplianceRev1,
       "ciscoGsp2MIBComplianceRev2": ciscoGsp2MIBComplianceRev2,
       "ciscoGsp2MIBComplianceRev3": ciscoGsp2MIBComplianceRev3,
       "ciscoGsp2MIBComplianceRev4": ciscoGsp2MIBComplianceRev4,
       "ciscoGsp2MIBGroups": ciscoGsp2MIBGroups,
       "ciscoGsp2EventsGroup": ciscoGsp2EventsGroup,
       "ciscoGsp2QosGroup": ciscoGsp2QosGroup,
       "ciscoGsp2LocalPeerGroup": ciscoGsp2LocalPeerGroup,
       "ciscoGsp2Mtp3ErrorsGroup": ciscoGsp2Mtp3ErrorsGroup,
       "ciscoGsp2OperationGroup": ciscoGsp2OperationGroup,
       "ciscoGsp2LocalPeerGroupSup1": ciscoGsp2LocalPeerGroupSup1,
       "ciscoGsp2ContextGroup": ciscoGsp2ContextGroup}
)
