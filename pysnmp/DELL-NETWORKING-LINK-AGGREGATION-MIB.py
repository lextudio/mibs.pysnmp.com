# SNMP MIB module (DELL-NETWORKING-LINK-AGGREGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-LINK-AGGREGATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:56 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

(PortList,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-TC",
    "PortList")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dellNetLinkAggMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2)
)
dellNetLinkAggMib.setRevisions(
        ("2013-04-16 00:00",
         "2012-11-26 00:00",
         "2011-07-04 00:00",
         "2003-08-01 00:00",
         "2002-03-12 00:00",
         "2001-03-01 00:00",
         "2000-11-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DellNetLacpKey(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class DellNetLacpState(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_DellNetLinkAggObjects_ObjectIdentity = ObjectIdentity
dellNetLinkAggObjects = _DellNetLinkAggObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1)
)
_DellNetdot3dAgg_ObjectIdentity = ObjectIdentity
dellNetdot3dAgg = _DellNetdot3dAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1)
)
_Dot3aAggConfigTable_Object = MibTable
dot3aAggConfigTable = _Dot3aAggConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot3aAggConfigTable.setStatus("current")
_Dot3aAggConfigEntry_Object = MibTableRow
dot3aAggConfigEntry = _Dot3aAggConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1)
)
dot3aAggConfigEntry.setIndexNames(
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgId"),
)
if mibBuilder.loadTexts:
    dot3aAggConfigEntry.setStatus("current")
_Dot3aAggCfgId_Type = Unsigned32
_Dot3aAggCfgId_Object = MibTableColumn
dot3aAggCfgId = _Dot3aAggCfgId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 1),
    _Dot3aAggCfgId_Type()
)
dot3aAggCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggCfgId.setStatus("current")
_Dot3aAggCfgMacAddr_Type = MacAddress
_Dot3aAggCfgMacAddr_Object = MibTableColumn
dot3aAggCfgMacAddr = _Dot3aAggCfgMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 2),
    _Dot3aAggCfgMacAddr_Type()
)
dot3aAggCfgMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgMacAddr.setStatus("current")
_Dot3aAggCfgIfIndex_Type = Unsigned32
_Dot3aAggCfgIfIndex_Object = MibTableColumn
dot3aAggCfgIfIndex = _Dot3aAggCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 3),
    _Dot3aAggCfgIfIndex_Type()
)
dot3aAggCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgIfIndex.setStatus("current")
_Dot3aAggCfgNumPorts_Type = Unsigned32
_Dot3aAggCfgNumPorts_Object = MibTableColumn
dot3aAggCfgNumPorts = _Dot3aAggCfgNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 4),
    _Dot3aAggCfgNumPorts_Type()
)
dot3aAggCfgNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgNumPorts.setStatus("current")
_Dot3aAggCfgPortList_Type = PortList
_Dot3aAggCfgPortList_Object = MibTableColumn
dot3aAggCfgPortList = _Dot3aAggCfgPortList_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 5),
    _Dot3aAggCfgPortList_Type()
)
dot3aAggCfgPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgPortList.setStatus("deprecated")
_Dot3aAggCfgPortListString_Type = OctetString
_Dot3aAggCfgPortListString_Object = MibTableColumn
dot3aAggCfgPortListString = _Dot3aAggCfgPortListString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 6),
    _Dot3aAggCfgPortListString_Type()
)
dot3aAggCfgPortListString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgPortListString.setStatus("current")
_Dot3aAggCfgLacpSupported_Type = TruthValue
_Dot3aAggCfgLacpSupported_Object = MibTableColumn
dot3aAggCfgLacpSupported = _Dot3aAggCfgLacpSupported_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 7),
    _Dot3aAggCfgLacpSupported_Type()
)
dot3aAggCfgLacpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgLacpSupported.setStatus("current")


class _Dot3aAggCfgOperStatus_Type(Integer32):
    """Custom type dot3aAggCfgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Dot3aAggCfgOperStatus_Type.__name__ = "Integer32"
_Dot3aAggCfgOperStatus_Object = MibTableColumn
dot3aAggCfgOperStatus = _Dot3aAggCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 8),
    _Dot3aAggCfgOperStatus_Type()
)
dot3aAggCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgOperStatus.setStatus("current")
_Dot3aAggStaticTable_Object = MibTable
dot3aAggStaticTable = _Dot3aAggStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot3aAggStaticTable.setStatus("current")
_Dot3aAggStaticEntry_Object = MibTableRow
dot3aAggStaticEntry = _Dot3aAggStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1)
)
dot3aAggStaticEntry.setIndexNames(
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggIndex"),
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggVlanId"),
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggMacAddr"),
)
if mibBuilder.loadTexts:
    dot3aAggStaticEntry.setStatus("deprecated")
_Dot3aAggIndex_Type = Unsigned32
_Dot3aAggIndex_Object = MibTableColumn
dot3aAggIndex = _Dot3aAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 1),
    _Dot3aAggIndex_Type()
)
dot3aAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggIndex.setStatus("deprecated")
_Dot3aAggVlanId_Type = Unsigned32
_Dot3aAggVlanId_Object = MibTableColumn
dot3aAggVlanId = _Dot3aAggVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 2),
    _Dot3aAggVlanId_Type()
)
dot3aAggVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggVlanId.setStatus("deprecated")
_Dot3aAggMacAddr_Type = MacAddress
_Dot3aAggMacAddr_Object = MibTableColumn
dot3aAggMacAddr = _Dot3aAggMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 3),
    _Dot3aAggMacAddr_Type()
)
dot3aAggMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggMacAddr.setStatus("deprecated")


class _Dot3aAggStatus_Type(Integer32):
    """Custom type dot3aAggStatus based on Integer32"""
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


_Dot3aAggStatus_Type.__name__ = "Integer32"
_Dot3aAggStatus_Object = MibTableColumn
dot3aAggStatus = _Dot3aAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 4),
    _Dot3aAggStatus_Type()
)
dot3aAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggStatus.setStatus("deprecated")
_Dot3aAggDistributedPort_Type = OctetString
_Dot3aAggDistributedPort_Object = MibTableColumn
dot3aAggDistributedPort = _Dot3aAggDistributedPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 5),
    _Dot3aAggDistributedPort_Type()
)
dot3aAggDistributedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggDistributedPort.setStatus("deprecated")
_Dot3aAggFdbTable_Object = MibTable
dot3aAggFdbTable = _Dot3aAggFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dot3aAggFdbTable.setStatus("current")
_Dot3aAggFdbEntry_Object = MibTableRow
dot3aAggFdbEntry = _Dot3aAggFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1)
)
dot3aAggFdbEntry.setIndexNames(
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggFdbIndex"),
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggFdbVlanId"),
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggFdbMacAddr"),
)
if mibBuilder.loadTexts:
    dot3aAggFdbEntry.setStatus("deprecated")
_Dot3aAggFdbIndex_Type = Unsigned32
_Dot3aAggFdbIndex_Object = MibTableColumn
dot3aAggFdbIndex = _Dot3aAggFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 1),
    _Dot3aAggFdbIndex_Type()
)
dot3aAggFdbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggFdbIndex.setStatus("deprecated")
_Dot3aAggFdbVlanId_Type = Unsigned32
_Dot3aAggFdbVlanId_Object = MibTableColumn
dot3aAggFdbVlanId = _Dot3aAggFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 2),
    _Dot3aAggFdbVlanId_Type()
)
dot3aAggFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggFdbVlanId.setStatus("deprecated")
_Dot3aAggFdbMacAddr_Type = MacAddress
_Dot3aAggFdbMacAddr_Object = MibTableColumn
dot3aAggFdbMacAddr = _Dot3aAggFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 3),
    _Dot3aAggFdbMacAddr_Type()
)
dot3aAggFdbMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aAggFdbMacAddr.setStatus("deprecated")


class _Dot3aAggFdbStatus_Type(Integer32):
    """Custom type dot3aAggFdbStatus based on Integer32"""
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


_Dot3aAggFdbStatus_Type.__name__ = "Integer32"
_Dot3aAggFdbStatus_Object = MibTableColumn
dot3aAggFdbStatus = _Dot3aAggFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 4),
    _Dot3aAggFdbStatus_Type()
)
dot3aAggFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggFdbStatus.setStatus("deprecated")
_Dot3aAggFdbDistributedPort_Type = OctetString
_Dot3aAggFdbDistributedPort_Object = MibTableColumn
dot3aAggFdbDistributedPort = _Dot3aAggFdbDistributedPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 5),
    _Dot3aAggFdbDistributedPort_Type()
)
dot3aAggFdbDistributedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggFdbDistributedPort.setStatus("deprecated")
_Dot3aCurAggStaticTable_Object = MibTable
dot3aCurAggStaticTable = _Dot3aCurAggStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dot3aCurAggStaticTable.setStatus("current")
_Dot3aCurAggStaticEntry_Object = MibTableRow
dot3aCurAggStaticEntry = _Dot3aCurAggStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1)
)
dot3aCurAggStaticEntry.setIndexNames(
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggVlanId"),
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggMacAddr"),
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggIndex"),
)
if mibBuilder.loadTexts:
    dot3aCurAggStaticEntry.setStatus("current")
_Dot3aCurAggVlanId_Type = Unsigned32
_Dot3aCurAggVlanId_Object = MibTableColumn
dot3aCurAggVlanId = _Dot3aCurAggVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 1),
    _Dot3aCurAggVlanId_Type()
)
dot3aCurAggVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggVlanId.setStatus("current")
_Dot3aCurAggMacAddr_Type = MacAddress
_Dot3aCurAggMacAddr_Object = MibTableColumn
dot3aCurAggMacAddr = _Dot3aCurAggMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 2),
    _Dot3aCurAggMacAddr_Type()
)
dot3aCurAggMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggMacAddr.setStatus("current")
_Dot3aCurAggIndex_Type = Unsigned32
_Dot3aCurAggIndex_Object = MibTableColumn
dot3aCurAggIndex = _Dot3aCurAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 3),
    _Dot3aCurAggIndex_Type()
)
dot3aCurAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggIndex.setStatus("current")


class _Dot3aCurAggStatus_Type(Integer32):
    """Custom type dot3aCurAggStatus based on Integer32"""
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


_Dot3aCurAggStatus_Type.__name__ = "Integer32"
_Dot3aCurAggStatus_Object = MibTableColumn
dot3aCurAggStatus = _Dot3aCurAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 4),
    _Dot3aCurAggStatus_Type()
)
dot3aCurAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggStatus.setStatus("current")
_Dot3aCurAggFdbTable_Object = MibTable
dot3aCurAggFdbTable = _Dot3aCurAggFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dot3aCurAggFdbTable.setStatus("current")
_Dot3aCurAggFdbEntry_Object = MibTableRow
dot3aCurAggFdbEntry = _Dot3aCurAggFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1)
)
dot3aCurAggFdbEntry.setIndexNames(
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggFdbVlanId"),
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggFdbMacAddr"),
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggFdbIndex"),
)
if mibBuilder.loadTexts:
    dot3aCurAggFdbEntry.setStatus("current")
_Dot3aCurAggFdbVlanId_Type = Unsigned32
_Dot3aCurAggFdbVlanId_Object = MibTableColumn
dot3aCurAggFdbVlanId = _Dot3aCurAggFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 1),
    _Dot3aCurAggFdbVlanId_Type()
)
dot3aCurAggFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggFdbVlanId.setStatus("current")
_Dot3aCurAggFdbMacAddr_Type = MacAddress
_Dot3aCurAggFdbMacAddr_Object = MibTableColumn
dot3aCurAggFdbMacAddr = _Dot3aCurAggFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 2),
    _Dot3aCurAggFdbMacAddr_Type()
)
dot3aCurAggFdbMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggFdbMacAddr.setStatus("current")
_Dot3aCurAggFdbIndex_Type = Unsigned32
_Dot3aCurAggFdbIndex_Object = MibTableColumn
dot3aCurAggFdbIndex = _Dot3aCurAggFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 3),
    _Dot3aCurAggFdbIndex_Type()
)
dot3aCurAggFdbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCurAggFdbIndex.setStatus("current")


class _Dot3aCurAggFdbStatus_Type(Integer32):
    """Custom type dot3aCurAggFdbStatus based on Integer32"""
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


_Dot3aCurAggFdbStatus_Type.__name__ = "Integer32"
_Dot3aCurAggFdbStatus_Object = MibTableColumn
dot3aCurAggFdbStatus = _Dot3aCurAggFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 4),
    _Dot3aCurAggFdbStatus_Type()
)
dot3aCurAggFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggFdbStatus.setStatus("current")
_Dot3aCommonAggFdbTable_Object = MibTable
dot3aCommonAggFdbTable = _Dot3aCommonAggFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dot3aCommonAggFdbTable.setStatus("current")
_Dot3aCommonAggFdbEntry_Object = MibTableRow
dot3aCommonAggFdbEntry = _Dot3aCommonAggFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1)
)
dot3aCommonAggFdbEntry.setIndexNames(
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbIndex"),
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbVlanId"),
)
if mibBuilder.loadTexts:
    dot3aCommonAggFdbEntry.setStatus("current")
_Dot3aCommonAggFdbIndex_Type = Unsigned32
_Dot3aCommonAggFdbIndex_Object = MibTableColumn
dot3aCommonAggFdbIndex = _Dot3aCommonAggFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 1),
    _Dot3aCommonAggFdbIndex_Type()
)
dot3aCommonAggFdbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbIndex.setStatus("current")
_Dot3aCommonAggFdbVlanId_Type = Unsigned32
_Dot3aCommonAggFdbVlanId_Object = MibTableColumn
dot3aCommonAggFdbVlanId = _Dot3aCommonAggFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 2),
    _Dot3aCommonAggFdbVlanId_Type()
)
dot3aCommonAggFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbVlanId.setStatus("current")


class _Dot3aCommonAggFdbTagConfig_Type(Integer32):
    """Custom type dot3aCommonAggFdbTagConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_Dot3aCommonAggFdbTagConfig_Type.__name__ = "Integer32"
_Dot3aCommonAggFdbTagConfig_Object = MibTableColumn
dot3aCommonAggFdbTagConfig = _Dot3aCommonAggFdbTagConfig_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 3),
    _Dot3aCommonAggFdbTagConfig_Type()
)
dot3aCommonAggFdbTagConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbTagConfig.setStatus("current")


class _Dot3aCommonAggFdbStatus_Type(Integer32):
    """Custom type dot3aCommonAggFdbStatus based on Integer32"""
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


_Dot3aCommonAggFdbStatus_Type.__name__ = "Integer32"
_Dot3aCommonAggFdbStatus_Object = MibTableColumn
dot3aCommonAggFdbStatus = _Dot3aCommonAggFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 4),
    _Dot3aCommonAggFdbStatus_Type()
)
dot3aCommonAggFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbStatus.setStatus("current")
_Dot3adAggPortTable_Object = MibTable
dot3adAggPortTable = _Dot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    dot3adAggPortTable.setStatus("current")
_Dot3adAggPortEntry_Object = MibTableRow
dot3adAggPortEntry = _Dot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1)
)
dot3adAggPortEntry.setIndexNames(
    (0, "DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortEntry.setStatus("current")
_Dot3adAggPortIndex_Type = Unsigned32
_Dot3adAggPortIndex_Object = MibTableColumn
dot3adAggPortIndex = _Dot3adAggPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 1),
    _Dot3adAggPortIndex_Type()
)
dot3adAggPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adAggPortIndex.setStatus("current")
_Dot3adAggPortActorOperKey_Type = DellNetLacpKey
_Dot3adAggPortActorOperKey_Object = MibTableColumn
dot3adAggPortActorOperKey = _Dot3adAggPortActorOperKey_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 2),
    _Dot3adAggPortActorOperKey_Type()
)
dot3adAggPortActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorOperKey.setStatus("current")
_Dot3adAggPortPartnerOperKey_Type = DellNetLacpKey
_Dot3adAggPortPartnerOperKey_Object = MibTableColumn
dot3adAggPortPartnerOperKey = _Dot3adAggPortPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 3),
    _Dot3adAggPortPartnerOperKey_Type()
)
dot3adAggPortPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperKey.setStatus("current")
_Dot3adAggPortActorAdminState_Type = DellNetLacpState
_Dot3adAggPortActorAdminState_Object = MibTableColumn
dot3adAggPortActorAdminState = _Dot3adAggPortActorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 4),
    _Dot3adAggPortActorAdminState_Type()
)
dot3adAggPortActorAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorAdminState.setStatus("current")
_Dot3adAggPortActorOperState_Type = DellNetLacpState
_Dot3adAggPortActorOperState_Object = MibTableColumn
dot3adAggPortActorOperState = _Dot3adAggPortActorOperState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 5),
    _Dot3adAggPortActorOperState_Type()
)
dot3adAggPortActorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorOperState.setStatus("current")
_Dot3adAggPortPartnerAdminState_Type = DellNetLacpState
_Dot3adAggPortPartnerAdminState_Object = MibTableColumn
dot3adAggPortPartnerAdminState = _Dot3adAggPortPartnerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 6),
    _Dot3adAggPortPartnerAdminState_Type()
)
dot3adAggPortPartnerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminState.setStatus("current")
_Dot3adAggPortPartnerOperState_Type = DellNetLacpState
_Dot3adAggPortPartnerOperState_Object = MibTableColumn
dot3adAggPortPartnerOperState = _Dot3adAggPortPartnerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 7, 1, 7),
    _Dot3adAggPortPartnerOperState_Type()
)
dot3adAggPortPartnerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperState.setStatus("current")
_DellNetLinkAggMgmt_ObjectIdentity = ObjectIdentity
dellNetLinkAggMgmt = _DellNetLinkAggMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 2)
)


class _Dot3aClearFdb_Type(Integer32):
    """Custom type dot3aClearFdb based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Dot3aClearFdb_Type.__name__ = "Integer32"
_Dot3aClearFdb_Object = MibScalar
dot3aClearFdb = _Dot3aClearFdb_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 2, 1),
    _Dot3aClearFdb_Type()
)
dot3aClearFdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3aClearFdb.setStatus("current")
_DellNetLinkAggAlarms_ObjectIdentity = ObjectIdentity
dellNetLinkAggAlarms = _DellNetLinkAggAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2)
)
_DellNetDot3adAggNotifications_ObjectIdentity = ObjectIdentity
dellNetDot3adAggNotifications = _DellNetDot3adAggNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 0)
)
_DellNetLinkBundleNotifications_ObjectIdentity = ObjectIdentity
dellNetLinkBundleNotifications = _DellNetLinkBundleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 1)
)


class _LinkBundleType_Type(Integer32):
    """Custom type linkBundleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecmpBundle", 1),
          ("lagBundle", 2))
    )


_LinkBundleType_Type.__name__ = "Integer32"
_LinkBundleType_Object = MibScalar
linkBundleType = _LinkBundleType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 2),
    _LinkBundleType_Type()
)
linkBundleType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    linkBundleType.setStatus("current")
_LinkBundleNumber_Type = Integer32
_LinkBundleNumber_Object = MibScalar
linkBundleNumber = _LinkBundleNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 3),
    _LinkBundleNumber_Type()
)
linkBundleNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    linkBundleNumber.setStatus("current")
_DellNetLinkAggMibConformance_ObjectIdentity = ObjectIdentity
dellNetLinkAggMibConformance = _DellNetLinkAggMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3)
)
_DellNetLinkAggMibCompliances_ObjectIdentity = ObjectIdentity
dellNetLinkAggMibCompliances = _DellNetLinkAggMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 1)
)
_DellNetLinkAggMibGroups_ObjectIdentity = ObjectIdentity
dellNetLinkAggMibGroups = _DellNetLinkAggMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2)
)

# Managed Objects groups

dellNetLinkAggCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 1)
)
dellNetLinkAggCommonGroup.setObjects(
      *(("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgMacAddr"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgIfIndex"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgNumPorts"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgPortListString"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgLacpSupported"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgOperStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggFdbStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbTagConfig"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aClearFdb"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgPortList"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggDistributedPort"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggFdbStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggFdbDistributedPort"))
)
if mibBuilder.loadTexts:
    dellNetLinkAggCommonGroup.setStatus("deprecated")

dellNetLinkAggCommonGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 2)
)
dellNetLinkAggCommonGroupRev1.setObjects(
      *(("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgMacAddr"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgIfIndex"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgNumPorts"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgPortListString"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgLacpSupported"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aAggCfgOperStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCurAggFdbStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbTagConfig"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbStatus"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3aClearFdb"))
)
if mibBuilder.loadTexts:
    dellNetLinkAggCommonGroupRev1.setStatus("current")

dellNetLinkAggPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 3)
)
dellNetLinkAggPortGroup.setObjects(
      *(("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggPortActorOperKey"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggPortPartnerOperKey"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggPortActorAdminState"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggPortActorOperState"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggPortPartnerAdminState"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggPortPartnerOperState"))
)
if mibBuilder.loadTexts:
    dellNetLinkAggPortGroup.setStatus("current")

dellNetLinkAggAlarmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 5)
)
dellNetLinkAggAlarmObjectGroup.setObjects(
      *(("DELL-NETWORKING-LINK-AGGREGATION-MIB", "linkBundleType"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "linkBundleNumber"))
)
if mibBuilder.loadTexts:
    dellNetLinkAggAlarmObjectGroup.setStatus("current")


# Notification objects

dot3adAggLacpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 0, 1)
)
dot3adAggLacpStateChange.setObjects(
      *(("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggPortActorOperState"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggPortPartnerOperState"))
)
if mibBuilder.loadTexts:
    dot3adAggLacpStateChange.setStatus(
        "current"
    )

linkBundleImbalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 1, 1)
)
linkBundleImbalance.setObjects(
      *(("DELL-NETWORKING-LINK-AGGREGATION-MIB", "linkBundleType"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "linkBundleNumber"))
)
if mibBuilder.loadTexts:
    linkBundleImbalance.setStatus(
        "current"
    )

linkBundleImbalanceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 1, 2)
)
linkBundleImbalanceClear.setObjects(
      *(("DELL-NETWORKING-LINK-AGGREGATION-MIB", "linkBundleType"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "linkBundleNumber"))
)
if mibBuilder.loadTexts:
    linkBundleImbalanceClear.setStatus(
        "current"
    )


# Notifications groups

dellNetLinkAggNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 2, 4)
)
dellNetLinkAggNotificationGroup.setObjects(
      *(("DELL-NETWORKING-LINK-AGGREGATION-MIB", "dot3adAggLacpStateChange"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "linkBundleImbalance"),
        ("DELL-NETWORKING-LINK-AGGREGATION-MIB", "linkBundleImbalanceClear"))
)
if mibBuilder.loadTexts:
    dellNetLinkAggNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dellNetLinkAggMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetLinkAggMibCompliance.setStatus(
        "deprecated"
    )

dellNetLinkAggMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dellNetLinkAggMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-LINK-AGGREGATION-MIB",
    **{"DellNetLacpKey": DellNetLacpKey,
       "DellNetLacpState": DellNetLacpState,
       "dellNetLinkAggMib": dellNetLinkAggMib,
       "dellNetLinkAggObjects": dellNetLinkAggObjects,
       "dellNetdot3dAgg": dellNetdot3dAgg,
       "dot3aAggConfigTable": dot3aAggConfigTable,
       "dot3aAggConfigEntry": dot3aAggConfigEntry,
       "dot3aAggCfgId": dot3aAggCfgId,
       "dot3aAggCfgMacAddr": dot3aAggCfgMacAddr,
       "dot3aAggCfgIfIndex": dot3aAggCfgIfIndex,
       "dot3aAggCfgNumPorts": dot3aAggCfgNumPorts,
       "dot3aAggCfgPortList": dot3aAggCfgPortList,
       "dot3aAggCfgPortListString": dot3aAggCfgPortListString,
       "dot3aAggCfgLacpSupported": dot3aAggCfgLacpSupported,
       "dot3aAggCfgOperStatus": dot3aAggCfgOperStatus,
       "dot3aAggStaticTable": dot3aAggStaticTable,
       "dot3aAggStaticEntry": dot3aAggStaticEntry,
       "dot3aAggIndex": dot3aAggIndex,
       "dot3aAggVlanId": dot3aAggVlanId,
       "dot3aAggMacAddr": dot3aAggMacAddr,
       "dot3aAggStatus": dot3aAggStatus,
       "dot3aAggDistributedPort": dot3aAggDistributedPort,
       "dot3aAggFdbTable": dot3aAggFdbTable,
       "dot3aAggFdbEntry": dot3aAggFdbEntry,
       "dot3aAggFdbIndex": dot3aAggFdbIndex,
       "dot3aAggFdbVlanId": dot3aAggFdbVlanId,
       "dot3aAggFdbMacAddr": dot3aAggFdbMacAddr,
       "dot3aAggFdbStatus": dot3aAggFdbStatus,
       "dot3aAggFdbDistributedPort": dot3aAggFdbDistributedPort,
       "dot3aCurAggStaticTable": dot3aCurAggStaticTable,
       "dot3aCurAggStaticEntry": dot3aCurAggStaticEntry,
       "dot3aCurAggVlanId": dot3aCurAggVlanId,
       "dot3aCurAggMacAddr": dot3aCurAggMacAddr,
       "dot3aCurAggIndex": dot3aCurAggIndex,
       "dot3aCurAggStatus": dot3aCurAggStatus,
       "dot3aCurAggFdbTable": dot3aCurAggFdbTable,
       "dot3aCurAggFdbEntry": dot3aCurAggFdbEntry,
       "dot3aCurAggFdbVlanId": dot3aCurAggFdbVlanId,
       "dot3aCurAggFdbMacAddr": dot3aCurAggFdbMacAddr,
       "dot3aCurAggFdbIndex": dot3aCurAggFdbIndex,
       "dot3aCurAggFdbStatus": dot3aCurAggFdbStatus,
       "dot3aCommonAggFdbTable": dot3aCommonAggFdbTable,
       "dot3aCommonAggFdbEntry": dot3aCommonAggFdbEntry,
       "dot3aCommonAggFdbIndex": dot3aCommonAggFdbIndex,
       "dot3aCommonAggFdbVlanId": dot3aCommonAggFdbVlanId,
       "dot3aCommonAggFdbTagConfig": dot3aCommonAggFdbTagConfig,
       "dot3aCommonAggFdbStatus": dot3aCommonAggFdbStatus,
       "dot3adAggPortTable": dot3adAggPortTable,
       "dot3adAggPortEntry": dot3adAggPortEntry,
       "dot3adAggPortIndex": dot3adAggPortIndex,
       "dot3adAggPortActorOperKey": dot3adAggPortActorOperKey,
       "dot3adAggPortPartnerOperKey": dot3adAggPortPartnerOperKey,
       "dot3adAggPortActorAdminState": dot3adAggPortActorAdminState,
       "dot3adAggPortActorOperState": dot3adAggPortActorOperState,
       "dot3adAggPortPartnerAdminState": dot3adAggPortPartnerAdminState,
       "dot3adAggPortPartnerOperState": dot3adAggPortPartnerOperState,
       "dellNetLinkAggMgmt": dellNetLinkAggMgmt,
       "dot3aClearFdb": dot3aClearFdb,
       "dellNetLinkAggAlarms": dellNetLinkAggAlarms,
       "dellNetDot3adAggNotifications": dellNetDot3adAggNotifications,
       "dot3adAggLacpStateChange": dot3adAggLacpStateChange,
       "dellNetLinkBundleNotifications": dellNetLinkBundleNotifications,
       "linkBundleImbalance": linkBundleImbalance,
       "linkBundleImbalanceClear": linkBundleImbalanceClear,
       "linkBundleType": linkBundleType,
       "linkBundleNumber": linkBundleNumber,
       "dellNetLinkAggMibConformance": dellNetLinkAggMibConformance,
       "dellNetLinkAggMibCompliances": dellNetLinkAggMibCompliances,
       "dellNetLinkAggMibCompliance": dellNetLinkAggMibCompliance,
       "dellNetLinkAggMibComplianceRev1": dellNetLinkAggMibComplianceRev1,
       "dellNetLinkAggMibGroups": dellNetLinkAggMibGroups,
       "dellNetLinkAggCommonGroup": dellNetLinkAggCommonGroup,
       "dellNetLinkAggCommonGroupRev1": dellNetLinkAggCommonGroupRev1,
       "dellNetLinkAggPortGroup": dellNetLinkAggPortGroup,
       "dellNetLinkAggNotificationGroup": dellNetLinkAggNotificationGroup,
       "dellNetLinkAggAlarmObjectGroup": dellNetLinkAggAlarmObjectGroup}
)
