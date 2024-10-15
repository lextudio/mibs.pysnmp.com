# SNMP MIB module (CISCO-WAN-RPM-CONN-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-RPM-CONN-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:14 2024
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

(cwAtmChanCnfgEntry,) = mibBuilder.importSymbols(
    "CISCO-WAN-ATM-CONN-MIB",
    "cwAtmChanCnfgEntry")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoWanRpmConnExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 9)
)
ciscoWanRpmConnExtMIB.setRevisions(
        ("2002-05-21 00:00",
         "2002-03-18 00:00",
         "1999-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwRpmConnExtMIBObjects_ObjectIdentity = ObjectIdentity
cwRpmConnExtMIBObjects = _CwRpmConnExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1)
)
_CwRpmConnExt_ObjectIdentity = ObjectIdentity
cwRpmConnExt = _CwRpmConnExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1)
)
_CwRpmChanExtTable_Object = MibTable
cwRpmChanExtTable = _CwRpmChanExtTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwRpmChanExtTable.setStatus("current")
_CwRpmChanExtEntry_Object = MibTableRow
cwRpmChanExtEntry = _CwRpmChanExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwRpmChanExtEntry.setStatus("current")


class _CwrChanSubInterface_Type(Unsigned32):
    """Custom type cwrChanSubInterface based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwrChanSubInterface_Type.__name__ = "Unsigned32"
_CwrChanSubInterface_Object = MibTableColumn
cwrChanSubInterface = _CwrChanSubInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 1),
    _CwrChanSubInterface_Type()
)
cwrChanSubInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrChanSubInterface.setStatus("current")


class _CwrChanVcd_Type(Unsigned32):
    """Custom type cwrChanVcd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwrChanVcd_Type.__name__ = "Unsigned32"
_CwrChanVcd_Object = MibTableColumn
cwrChanVcd = _CwrChanVcd_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 2),
    _CwrChanVcd_Type()
)
cwrChanVcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwrChanVcd.setStatus("current")


class _CwrChanAalEncapType_Type(Integer32):
    """Custom type cwrChanAalEncapType based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("aal5ciscoPPP", 1),
          ("aal5muxAPOLLO", 2),
          ("aal5muxAPPLETALK", 3),
          ("aal5muxDECNET", 4),
          ("aal5muxIP", 5),
          ("aal5muxIPX", 6),
          ("aal5muxPPP", 7),
          ("aal5muxVINES", 8),
          ("aal5muxXNS", 9),
          ("aal5nlpid", 10),
          ("aal5snap", 11),
          ("ilmi", 12),
          ("qsaal", 13))
    )


_CwrChanAalEncapType_Type.__name__ = "Integer32"
_CwrChanAalEncapType_Object = MibTableColumn
cwrChanAalEncapType = _CwrChanAalEncapType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 3),
    _CwrChanAalEncapType_Type()
)
cwrChanAalEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrChanAalEncapType.setStatus("current")


class _CwrChanVirtualTemplate_Type(Unsigned32):
    """Custom type cwrChanVirtualTemplate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CwrChanVirtualTemplate_Type.__name__ = "Unsigned32"
_CwrChanVirtualTemplate_Object = MibTableColumn
cwrChanVirtualTemplate = _CwrChanVirtualTemplate_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 4),
    _CwrChanVirtualTemplate_Type()
)
cwrChanVirtualTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrChanVirtualTemplate.setStatus("current")


class _CwrChanInArpInterval_Type(Unsigned32):
    """Custom type cwrChanInArpInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CwrChanInArpInterval_Type.__name__ = "Unsigned32"
_CwrChanInArpInterval_Object = MibTableColumn
cwrChanInArpInterval = _CwrChanInArpInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 5),
    _CwrChanInArpInterval_Type()
)
cwrChanInArpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrChanInArpInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwrChanInArpInterval.setUnits("minutes")


class _CwrChanOamLoopbkTxInterval_Type(Unsigned32):
    """Custom type cwrChanOamLoopbkTxInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CwrChanOamLoopbkTxInterval_Type.__name__ = "Unsigned32"
_CwrChanOamLoopbkTxInterval_Object = MibTableColumn
cwrChanOamLoopbkTxInterval = _CwrChanOamLoopbkTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 6),
    _CwrChanOamLoopbkTxInterval_Type()
)
cwrChanOamLoopbkTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrChanOamLoopbkTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwrChanOamLoopbkTxInterval.setUnits("seconds")


class _CwrChanOamManage_Type(TruthValue):
    """Custom type cwrChanOamManage based on TruthValue"""


_CwrChanOamManage_Object = MibTableColumn
cwrChanOamManage = _CwrChanOamManage_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 7),
    _CwrChanOamManage_Type()
)
cwrChanOamManage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrChanOamManage.setStatus("current")


class _CwrChanOamRetryUpCount_Type(Unsigned32):
    """Custom type cwrChanOamRetryUpCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CwrChanOamRetryUpCount_Type.__name__ = "Unsigned32"
_CwrChanOamRetryUpCount_Object = MibTableColumn
cwrChanOamRetryUpCount = _CwrChanOamRetryUpCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 8),
    _CwrChanOamRetryUpCount_Type()
)
cwrChanOamRetryUpCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrChanOamRetryUpCount.setStatus("current")


class _CwrChanOamRetryDownCount_Type(Unsigned32):
    """Custom type cwrChanOamRetryDownCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CwrChanOamRetryDownCount_Type.__name__ = "Unsigned32"
_CwrChanOamRetryDownCount_Object = MibTableColumn
cwrChanOamRetryDownCount = _CwrChanOamRetryDownCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 9),
    _CwrChanOamRetryDownCount_Type()
)
cwrChanOamRetryDownCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrChanOamRetryDownCount.setStatus("current")


class _CwrChanOamRetryInterval_Type(Unsigned32):
    """Custom type cwrChanOamRetryInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CwrChanOamRetryInterval_Type.__name__ = "Unsigned32"
_CwrChanOamRetryInterval_Object = MibTableColumn
cwrChanOamRetryInterval = _CwrChanOamRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 1, 1, 1, 1, 10),
    _CwrChanOamRetryInterval_Type()
)
cwrChanOamRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwrChanOamRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwrChanOamRetryInterval.setUnits("seconds")
_CiscoWanRpmConnExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanRpmConnExtMIBConformance = _CiscoWanRpmConnExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 2)
)
_CiscoWanRpmConnExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanRpmConnExtMIBCompliances = _CiscoWanRpmConnExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 2, 1)
)
_CiscoWanRpmConnExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanRpmConnExtMIBGroups = _CiscoWanRpmConnExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 2, 2)
)
cwAtmChanCnfgEntry.registerAugmentions(
    ("CISCO-WAN-RPM-CONN-EXT-MIB",
     "cwRpmChanExtEntry")
)
cwRpmChanExtEntry.setIndexNames(*cwAtmChanCnfgEntry.getIndexNames())

# Managed Objects groups

ciscoWanRpmConnExtMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 2, 2, 1)
)
ciscoWanRpmConnExtMIBGroup.setObjects(
      *(("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanSubInterface"),
        ("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanVcd"),
        ("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanAalEncapType"),
        ("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanVirtualTemplate"),
        ("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanInArpInterval"),
        ("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanOamLoopbkTxInterval"),
        ("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanOamManage"),
        ("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanOamRetryUpCount"),
        ("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanOamRetryDownCount"),
        ("CISCO-WAN-RPM-CONN-EXT-MIB", "cwrChanOamRetryInterval"))
)
if mibBuilder.loadTexts:
    ciscoWanRpmConnExtMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanRpmConnExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanRpmConnExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-RPM-CONN-EXT-MIB",
    **{"ciscoWanRpmConnExtMIB": ciscoWanRpmConnExtMIB,
       "cwRpmConnExtMIBObjects": cwRpmConnExtMIBObjects,
       "cwRpmConnExt": cwRpmConnExt,
       "cwRpmChanExtTable": cwRpmChanExtTable,
       "cwRpmChanExtEntry": cwRpmChanExtEntry,
       "cwrChanSubInterface": cwrChanSubInterface,
       "cwrChanVcd": cwrChanVcd,
       "cwrChanAalEncapType": cwrChanAalEncapType,
       "cwrChanVirtualTemplate": cwrChanVirtualTemplate,
       "cwrChanInArpInterval": cwrChanInArpInterval,
       "cwrChanOamLoopbkTxInterval": cwrChanOamLoopbkTxInterval,
       "cwrChanOamManage": cwrChanOamManage,
       "cwrChanOamRetryUpCount": cwrChanOamRetryUpCount,
       "cwrChanOamRetryDownCount": cwrChanOamRetryDownCount,
       "cwrChanOamRetryInterval": cwrChanOamRetryInterval,
       "ciscoWanRpmConnExtMIBConformance": ciscoWanRpmConnExtMIBConformance,
       "ciscoWanRpmConnExtMIBCompliances": ciscoWanRpmConnExtMIBCompliances,
       "ciscoWanRpmConnExtMIBCompliance": ciscoWanRpmConnExtMIBCompliance,
       "ciscoWanRpmConnExtMIBGroups": ciscoWanRpmConnExtMIBGroups,
       "ciscoWanRpmConnExtMIBGroup": ciscoWanRpmConnExtMIBGroup}
)
