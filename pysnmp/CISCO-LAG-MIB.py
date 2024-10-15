# SNMP MIB module (CISCO-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:53 2024
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

(CiscoInterfaceIndexList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoInterfaceIndexList")

(dot3adAggPortEntry,
 dot3adAggPortListEntry) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggPortEntry",
    "dot3adAggPortListEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225)
)
ciscoLagMIB.setRevisions(
        ("2014-01-14 00:00",
         "2010-10-20 00:00",
         "2009-11-19 00:00",
         "2008-01-08 00:00",
         "2006-06-21 00:00",
         "2004-06-11 00:00",
         "2002-12-13 00:00",
         "2002-01-02 00:00",
         "2001-10-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClagDistributionProtocol(Integer32, TextualConvention):
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
        *(("ip", 1),
          ("ipPort", 6),
          ("mac", 2),
          ("port", 3),
          ("vlanIp", 5),
          ("vlanIpPort", 4))
    )



class ClagDistributionAddressMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("destination", 2),
          ("source", 1))
    )



class ClagDistributionMplsProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("label", 1),
          ("labelIp", 2))
    )



class ClagAggregationProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 1),
          ("pagp", 2))
    )



class ClagPortAdminStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 3),
          ("off", 1),
          ("on", 2),
          ("passive", 4))
    )



# MIB Managed Objects in the order of their OIDs

_ClagMIBObjects_ObjectIdentity = ObjectIdentity
clagMIBObjects = _ClagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1)
)
_ClagGlobalConfigObjects_ObjectIdentity = ObjectIdentity
clagGlobalConfigObjects = _ClagGlobalConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1)
)
_ClagAggDistributionProtocol_Type = ClagDistributionProtocol
_ClagAggDistributionProtocol_Object = MibScalar
clagAggDistributionProtocol = _ClagAggDistributionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 1),
    _ClagAggDistributionProtocol_Type()
)
clagAggDistributionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggDistributionProtocol.setStatus("current")
_ClagAggDistributionAddressMode_Type = ClagDistributionAddressMode
_ClagAggDistributionAddressMode_Object = MibScalar
clagAggDistributionAddressMode = _ClagAggDistributionAddressMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 2),
    _ClagAggDistributionAddressMode_Type()
)
clagAggDistributionAddressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggDistributionAddressMode.setStatus("current")
_ClagAggDistributionMplsProtocol_Type = ClagDistributionMplsProtocol
_ClagAggDistributionMplsProtocol_Object = MibScalar
clagAggDistributionMplsProtocol = _ClagAggDistributionMplsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 3),
    _ClagAggDistributionMplsProtocol_Type()
)
clagAggDistributionMplsProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggDistributionMplsProtocol.setStatus("current")
_ClagAggMaxAggregators_Type = Unsigned32
_ClagAggMaxAggregators_Object = MibScalar
clagAggMaxAggregators = _ClagAggMaxAggregators_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 4),
    _ClagAggMaxAggregators_Type()
)
clagAggMaxAggregators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clagAggMaxAggregators.setStatus("current")


class _ClagAggHashDistMethodGlobalConfig_Type(Integer32):
    """Custom type clagAggHashDistMethodGlobalConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("fixed", 2))
    )


_ClagAggHashDistMethodGlobalConfig_Type.__name__ = "Integer32"
_ClagAggHashDistMethodGlobalConfig_Object = MibScalar
clagAggHashDistMethodGlobalConfig = _ClagAggHashDistMethodGlobalConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 5),
    _ClagAggHashDistMethodGlobalConfig_Type()
)
clagAggHashDistMethodGlobalConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggHashDistMethodGlobalConfig.setStatus("current")
_ClagAgg_ObjectIdentity = ObjectIdentity
clagAgg = _ClagAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2)
)
_ClagAggProtocolTable_Object = MibTable
clagAggProtocolTable = _ClagAggProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clagAggProtocolTable.setStatus("current")
_ClagAggProtocolEntry_Object = MibTableRow
clagAggProtocolEntry = _ClagAggProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2, 1, 1)
)
clagAggProtocolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    clagAggProtocolEntry.setStatus("current")
_ClagAggProtocolType_Type = ClagAggregationProtocol
_ClagAggProtocolType_Object = MibTableColumn
clagAggProtocolType = _ClagAggProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2, 1, 1, 1),
    _ClagAggProtocolType_Type()
)
clagAggProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggProtocolType.setStatus("current")
_ClagAggPort_ObjectIdentity = ObjectIdentity
clagAggPort = _ClagAggPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3)
)
_ClagAggPortTable_Object = MibTable
clagAggPortTable = _ClagAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clagAggPortTable.setStatus("current")
_ClagAggPortEntry_Object = MibTableRow
clagAggPortEntry = _ClagAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    clagAggPortEntry.setStatus("current")
_ClagAggPortAdminStatus_Type = ClagPortAdminStatus
_ClagAggPortAdminStatus_Object = MibTableColumn
clagAggPortAdminStatus = _ClagAggPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1, 1, 1),
    _ClagAggPortAdminStatus_Type()
)
clagAggPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggPortAdminStatus.setStatus("current")


class _ClagAggPortRate_Type(Integer32):
    """Custom type clagAggPortRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("normal", 2))
    )


_ClagAggPortRate_Type.__name__ = "Integer32"
_ClagAggPortRate_Object = MibTableColumn
clagAggPortRate = _ClagAggPortRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1, 1, 2),
    _ClagAggPortRate_Type()
)
clagAggPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggPortRate.setStatus("current")
_ClagAggPortList_ObjectIdentity = ObjectIdentity
clagAggPortList = _ClagAggPortList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4)
)
_ClagAggPortListTable_Object = MibTable
clagAggPortListTable = _ClagAggPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1)
)
if mibBuilder.loadTexts:
    clagAggPortListTable.setStatus("current")
_ClagAggPortListEntry_Object = MibTableRow
clagAggPortListEntry = _ClagAggPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    clagAggPortListEntry.setStatus("current")


class _ClagAggPortListPorts_Type(OctetString):
    """Custom type clagAggPortListPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_ClagAggPortListPorts_Type.__name__ = "OctetString"
_ClagAggPortListPorts_Object = MibTableColumn
clagAggPortListPorts = _ClagAggPortListPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1, 1, 1),
    _ClagAggPortListPorts_Type()
)
clagAggPortListPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clagAggPortListPorts.setStatus("current")
_ClagAggPortListInterfaceIndexList_Type = CiscoInterfaceIndexList
_ClagAggPortListInterfaceIndexList_Object = MibTableColumn
clagAggPortListInterfaceIndexList = _ClagAggPortListInterfaceIndexList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1, 1, 2),
    _ClagAggPortListInterfaceIndexList_Type()
)
clagAggPortListInterfaceIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clagAggPortListInterfaceIndexList.setStatus("current")
_ClagAggChannelIntf_ObjectIdentity = ObjectIdentity
clagAggChannelIntf = _ClagAggChannelIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5)
)
_ClagAggChannelIfTable_Object = MibTable
clagAggChannelIfTable = _ClagAggChannelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1)
)
if mibBuilder.loadTexts:
    clagAggChannelIfTable.setStatus("current")
_ClagAggChannelIfEntry_Object = MibTableRow
clagAggChannelIfEntry = _ClagAggChannelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1)
)
clagAggChannelIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    clagAggChannelIfEntry.setStatus("current")
_ClagAggChannelIfFastSwitchOver_Type = TruthValue
_ClagAggChannelIfFastSwitchOver_Object = MibTableColumn
clagAggChannelIfFastSwitchOver = _ClagAggChannelIfFastSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 1),
    _ClagAggChannelIfFastSwitchOver_Type()
)
clagAggChannelIfFastSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggChannelIfFastSwitchOver.setStatus("current")


class _ClagAggChannelIfMaxBundle_Type(Unsigned32):
    """Custom type clagAggChannelIfMaxBundle based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ClagAggChannelIfMaxBundle_Type.__name__ = "Unsigned32"
_ClagAggChannelIfMaxBundle_Object = MibTableColumn
clagAggChannelIfMaxBundle = _ClagAggChannelIfMaxBundle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 2),
    _ClagAggChannelIfMaxBundle_Type()
)
clagAggChannelIfMaxBundle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggChannelIfMaxBundle.setStatus("current")
_ClagAggChannelIfMinLink_Type = Unsigned32
_ClagAggChannelIfMinLink_Object = MibTableColumn
clagAggChannelIfMinLink = _ClagAggChannelIfMinLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 3),
    _ClagAggChannelIfMinLink_Type()
)
clagAggChannelIfMinLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggChannelIfMinLink.setStatus("current")


class _ClagAggChannelIfHashDistAdminMethod_Type(Integer32):
    """Custom type clagAggChannelIfHashDistAdminMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 3),
          ("none", 1))
    )


_ClagAggChannelIfHashDistAdminMethod_Type.__name__ = "Integer32"
_ClagAggChannelIfHashDistAdminMethod_Object = MibTableColumn
clagAggChannelIfHashDistAdminMethod = _ClagAggChannelIfHashDistAdminMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 4),
    _ClagAggChannelIfHashDistAdminMethod_Type()
)
clagAggChannelIfHashDistAdminMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clagAggChannelIfHashDistAdminMethod.setStatus("current")


class _ClagAggChannelIfHashDistOperMethod_Type(Integer32):
    """Custom type clagAggChannelIfHashDistOperMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 3),
          ("other", 1))
    )


_ClagAggChannelIfHashDistOperMethod_Type.__name__ = "Integer32"
_ClagAggChannelIfHashDistOperMethod_Object = MibTableColumn
clagAggChannelIfHashDistOperMethod = _ClagAggChannelIfHashDistOperMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 5),
    _ClagAggChannelIfHashDistOperMethod_Type()
)
clagAggChannelIfHashDistOperMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clagAggChannelIfHashDistOperMethod.setStatus("current")
_ClagMIBNotifications_ObjectIdentity = ObjectIdentity
clagMIBNotifications = _ClagMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 2)
)
_ClagMIBConformance_ObjectIdentity = ObjectIdentity
clagMIBConformance = _ClagMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3)
)
_ClagMIBCompliances_ObjectIdentity = ObjectIdentity
clagMIBCompliances = _ClagMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1)
)
_ClagMIBGroups_ObjectIdentity = ObjectIdentity
clagMIBGroups = _ClagMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2)
)
dot3adAggPortEntry.registerAugmentions(
    ("CISCO-LAG-MIB",
     "clagAggPortEntry")
)
clagAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
dot3adAggPortListEntry.registerAugmentions(
    ("CISCO-LAG-MIB",
     "clagAggPortListEntry")
)
clagAggPortListEntry.setIndexNames(*dot3adAggPortListEntry.getIndexNames())

# Managed Objects groups

clagAggProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 1)
)
clagAggProtocolGroup.setObjects(
    ("CISCO-LAG-MIB", "clagAggProtocolType")
)
if mibBuilder.loadTexts:
    clagAggProtocolGroup.setStatus("current")

clagAggPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 2)
)
clagAggPortGroup.setObjects(
    ("CISCO-LAG-MIB", "clagAggPortAdminStatus")
)
if mibBuilder.loadTexts:
    clagAggPortGroup.setStatus("current")

clagAggDistributionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 3)
)
clagAggDistributionGroup.setObjects(
      *(("CISCO-LAG-MIB", "clagAggDistributionProtocol"),
        ("CISCO-LAG-MIB", "clagAggDistributionAddressMode"))
)
if mibBuilder.loadTexts:
    clagAggDistributionGroup.setStatus("current")

clagAggDistributionMplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 4)
)
clagAggDistributionMplsGroup.setObjects(
    ("CISCO-LAG-MIB", "clagAggDistributionMplsProtocol")
)
if mibBuilder.loadTexts:
    clagAggDistributionMplsGroup.setStatus("current")

clagAggPortListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 5)
)
clagAggPortListGroup.setObjects(
    ("CISCO-LAG-MIB", "clagAggPortListPorts")
)
if mibBuilder.loadTexts:
    clagAggPortListGroup.setStatus("current")

clagAggMaxAggregatorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 6)
)
clagAggMaxAggregatorsGroup.setObjects(
    ("CISCO-LAG-MIB", "clagAggMaxAggregators")
)
if mibBuilder.loadTexts:
    clagAggMaxAggregatorsGroup.setStatus("current")

clagAggRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 7)
)
clagAggRateGroup.setObjects(
    ("CISCO-LAG-MIB", "clagAggPortRate")
)
if mibBuilder.loadTexts:
    clagAggRateGroup.setStatus("current")

clagAggChannelIfLacpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 8)
)
clagAggChannelIfLacpGroup.setObjects(
      *(("CISCO-LAG-MIB", "clagAggChannelIfFastSwitchOver"),
        ("CISCO-LAG-MIB", "clagAggChannelIfMaxBundle"))
)
if mibBuilder.loadTexts:
    clagAggChannelIfLacpGroup.setStatus("current")

clagAggChannelIfHashDistMethodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 9)
)
clagAggChannelIfHashDistMethodGroup.setObjects(
      *(("CISCO-LAG-MIB", "clagAggChannelIfHashDistAdminMethod"),
        ("CISCO-LAG-MIB", "clagAggChannelIfHashDistOperMethod"))
)
if mibBuilder.loadTexts:
    clagAggChannelIfHashDistMethodGroup.setStatus("current")

clagAggHashDistGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 10)
)
clagAggHashDistGlobalGroup.setObjects(
    ("CISCO-LAG-MIB", "clagAggHashDistMethodGlobalConfig")
)
if mibBuilder.loadTexts:
    clagAggHashDistGlobalGroup.setStatus("current")

clagAggChannelIfMinLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 11)
)
clagAggChannelIfMinLinkGroup.setObjects(
    ("CISCO-LAG-MIB", "clagAggChannelIfMinLink")
)
if mibBuilder.loadTexts:
    clagAggChannelIfMinLinkGroup.setStatus("current")

clagAggPortListInterfaceIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 12)
)
clagAggPortListInterfaceIndexGroup.setObjects(
    ("CISCO-LAG-MIB", "clagAggPortListInterfaceIndexList")
)
if mibBuilder.loadTexts:
    clagAggPortListInterfaceIndexGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clagMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 1)
)
if mibBuilder.loadTexts:
    clagMIBCompliance.setStatus(
        "deprecated"
    )

clagMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 2)
)
if mibBuilder.loadTexts:
    clagMIBCompliance2.setStatus(
        "deprecated"
    )

clagMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 3)
)
if mibBuilder.loadTexts:
    clagMIBCompliance3.setStatus(
        "deprecated"
    )

clagMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 4)
)
if mibBuilder.loadTexts:
    clagMIBCompliance4.setStatus(
        "deprecated"
    )

clagMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 5)
)
if mibBuilder.loadTexts:
    clagMIBCompliance5.setStatus(
        "deprecated"
    )

clagMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 6)
)
if mibBuilder.loadTexts:
    clagMIBCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LAG-MIB",
    **{"ClagDistributionProtocol": ClagDistributionProtocol,
       "ClagDistributionAddressMode": ClagDistributionAddressMode,
       "ClagDistributionMplsProtocol": ClagDistributionMplsProtocol,
       "ClagAggregationProtocol": ClagAggregationProtocol,
       "ClagPortAdminStatus": ClagPortAdminStatus,
       "ciscoLagMIB": ciscoLagMIB,
       "clagMIBObjects": clagMIBObjects,
       "clagGlobalConfigObjects": clagGlobalConfigObjects,
       "clagAggDistributionProtocol": clagAggDistributionProtocol,
       "clagAggDistributionAddressMode": clagAggDistributionAddressMode,
       "clagAggDistributionMplsProtocol": clagAggDistributionMplsProtocol,
       "clagAggMaxAggregators": clagAggMaxAggregators,
       "clagAggHashDistMethodGlobalConfig": clagAggHashDistMethodGlobalConfig,
       "clagAgg": clagAgg,
       "clagAggProtocolTable": clagAggProtocolTable,
       "clagAggProtocolEntry": clagAggProtocolEntry,
       "clagAggProtocolType": clagAggProtocolType,
       "clagAggPort": clagAggPort,
       "clagAggPortTable": clagAggPortTable,
       "clagAggPortEntry": clagAggPortEntry,
       "clagAggPortAdminStatus": clagAggPortAdminStatus,
       "clagAggPortRate": clagAggPortRate,
       "clagAggPortList": clagAggPortList,
       "clagAggPortListTable": clagAggPortListTable,
       "clagAggPortListEntry": clagAggPortListEntry,
       "clagAggPortListPorts": clagAggPortListPorts,
       "clagAggPortListInterfaceIndexList": clagAggPortListInterfaceIndexList,
       "clagAggChannelIntf": clagAggChannelIntf,
       "clagAggChannelIfTable": clagAggChannelIfTable,
       "clagAggChannelIfEntry": clagAggChannelIfEntry,
       "clagAggChannelIfFastSwitchOver": clagAggChannelIfFastSwitchOver,
       "clagAggChannelIfMaxBundle": clagAggChannelIfMaxBundle,
       "clagAggChannelIfMinLink": clagAggChannelIfMinLink,
       "clagAggChannelIfHashDistAdminMethod": clagAggChannelIfHashDistAdminMethod,
       "clagAggChannelIfHashDistOperMethod": clagAggChannelIfHashDistOperMethod,
       "clagMIBNotifications": clagMIBNotifications,
       "clagMIBConformance": clagMIBConformance,
       "clagMIBCompliances": clagMIBCompliances,
       "clagMIBCompliance": clagMIBCompliance,
       "clagMIBCompliance2": clagMIBCompliance2,
       "clagMIBCompliance3": clagMIBCompliance3,
       "clagMIBCompliance4": clagMIBCompliance4,
       "clagMIBCompliance5": clagMIBCompliance5,
       "clagMIBCompliance6": clagMIBCompliance6,
       "clagMIBGroups": clagMIBGroups,
       "clagAggProtocolGroup": clagAggProtocolGroup,
       "clagAggPortGroup": clagAggPortGroup,
       "clagAggDistributionGroup": clagAggDistributionGroup,
       "clagAggDistributionMplsGroup": clagAggDistributionMplsGroup,
       "clagAggPortListGroup": clagAggPortListGroup,
       "clagAggMaxAggregatorsGroup": clagAggMaxAggregatorsGroup,
       "clagAggRateGroup": clagAggRateGroup,
       "clagAggChannelIfLacpGroup": clagAggChannelIfLacpGroup,
       "clagAggChannelIfHashDistMethodGroup": clagAggChannelIfHashDistMethodGroup,
       "clagAggHashDistGlobalGroup": clagAggHashDistGlobalGroup,
       "clagAggChannelIfMinLinkGroup": clagAggChannelIfMinLinkGroup,
       "clagAggPortListInterfaceIndexGroup": clagAggPortListInterfaceIndexGroup}
)
