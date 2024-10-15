# SNMP MIB module (CISCO-REPEATER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-REPEATER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:29 2024
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

(rptrPortEntry,) = mibBuilder.importSymbols(
    "SNMP-REPEATER-MIB",
    "rptrPortEntry")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoRptrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 22)
)
ciscoRptrMIB.setRevisions(
        ("1995-12-05 00:00",
         "1995-10-17 00:00",
         "1995-03-09 00:00",
         "1994-10-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoRptrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRptrMIBObjects = _CiscoRptrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1)
)
_CiscoRptrPortTable_Object = MibTable
ciscoRptrPortTable = _CiscoRptrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRptrPortTable.setStatus("current")
_CiscoRptrPortEntry_Object = MibTableRow
ciscoRptrPortEntry = _CiscoRptrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRptrPortEntry.setStatus("current")


class _CiscoRptrPortMDIStatus_Type(Integer32):
    """Custom type ciscoRptrPortMDIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossover", 2),
          ("normal", 1),
          ("notSwitchable", 3))
    )


_CiscoRptrPortMDIStatus_Type.__name__ = "Integer32"
_CiscoRptrPortMDIStatus_Object = MibTableColumn
ciscoRptrPortMDIStatus = _CiscoRptrPortMDIStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 1),
    _CiscoRptrPortMDIStatus_Type()
)
ciscoRptrPortMDIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoRptrPortMDIStatus.setStatus("current")


class _CiscoRptrPortLinkTestEnabled_Type(TruthValue):
    """Custom type ciscoRptrPortLinkTestEnabled based on TruthValue"""


_CiscoRptrPortLinkTestEnabled_Object = MibTableColumn
ciscoRptrPortLinkTestEnabled = _CiscoRptrPortLinkTestEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 2),
    _CiscoRptrPortLinkTestEnabled_Type()
)
ciscoRptrPortLinkTestEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoRptrPortLinkTestEnabled.setStatus("current")
_CiscoRptrPortLinkTestFailed_Type = TruthValue
_CiscoRptrPortLinkTestFailed_Object = MibTableColumn
ciscoRptrPortLinkTestFailed = _CiscoRptrPortLinkTestFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 3),
    _CiscoRptrPortLinkTestFailed_Type()
)
ciscoRptrPortLinkTestFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoRptrPortLinkTestFailed.setStatus("current")


class _CiscoRptrPortAutoPolarityEnabled_Type(TruthValue):
    """Custom type ciscoRptrPortAutoPolarityEnabled based on TruthValue"""


_CiscoRptrPortAutoPolarityEnabled_Object = MibTableColumn
ciscoRptrPortAutoPolarityEnabled = _CiscoRptrPortAutoPolarityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 4),
    _CiscoRptrPortAutoPolarityEnabled_Type()
)
ciscoRptrPortAutoPolarityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoRptrPortAutoPolarityEnabled.setStatus("current")
_CiscoRptrPortAutoPolarityCorrected_Type = TruthValue
_CiscoRptrPortAutoPolarityCorrected_Object = MibTableColumn
ciscoRptrPortAutoPolarityCorrected = _CiscoRptrPortAutoPolarityCorrected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 5),
    _CiscoRptrPortAutoPolarityCorrected_Type()
)
ciscoRptrPortAutoPolarityCorrected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoRptrPortAutoPolarityCorrected.setStatus("current")


class _CiscoRptrPortSrcAddrCtrl_Type(TruthValue):
    """Custom type ciscoRptrPortSrcAddrCtrl based on TruthValue"""


_CiscoRptrPortSrcAddrCtrl_Object = MibTableColumn
ciscoRptrPortSrcAddrCtrl = _CiscoRptrPortSrcAddrCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 6),
    _CiscoRptrPortSrcAddrCtrl_Type()
)
ciscoRptrPortSrcAddrCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoRptrPortSrcAddrCtrl.setStatus("current")


class _CiscoRptrPortAllowedSrcAddr_Type(OctetString):
    """Custom type ciscoRptrPortAllowedSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_CiscoRptrPortAllowedSrcAddr_Type.__name__ = "OctetString"
_CiscoRptrPortAllowedSrcAddr_Object = MibTableColumn
ciscoRptrPortAllowedSrcAddr = _CiscoRptrPortAllowedSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 7),
    _CiscoRptrPortAllowedSrcAddr_Type()
)
ciscoRptrPortAllowedSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoRptrPortAllowedSrcAddr.setStatus("current")


class _CiscoRptrPortAllowedSrcAddrStatus_Type(Integer32):
    """Custom type ciscoRptrPortAllowedSrcAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowedSrcAddrConfig", 1),
          ("allowedSrcAddrLearn", 2),
          ("allowedSrcAddrUndefined", 3))
    )


_CiscoRptrPortAllowedSrcAddrStatus_Type.__name__ = "Integer32"
_CiscoRptrPortAllowedSrcAddrStatus_Object = MibTableColumn
ciscoRptrPortAllowedSrcAddrStatus = _CiscoRptrPortAllowedSrcAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 8),
    _CiscoRptrPortAllowedSrcAddrStatus_Type()
)
ciscoRptrPortAllowedSrcAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoRptrPortAllowedSrcAddrStatus.setStatus("current")


class _CiscoRptrPortLastIllegalSrcAddr_Type(OctetString):
    """Custom type ciscoRptrPortLastIllegalSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_CiscoRptrPortLastIllegalSrcAddr_Type.__name__ = "OctetString"
_CiscoRptrPortLastIllegalSrcAddr_Object = MibTableColumn
ciscoRptrPortLastIllegalSrcAddr = _CiscoRptrPortLastIllegalSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 9),
    _CiscoRptrPortLastIllegalSrcAddr_Type()
)
ciscoRptrPortLastIllegalSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoRptrPortLastIllegalSrcAddr.setStatus("current")


class _CiscoRptrPortIllegalAddrTrapAcked_Type(Integer32):
    """Custom type ciscoRptrPortIllegalAddrTrapAcked based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acked", 1),
          ("no-acked-no-sending", 3),
          ("no-acked-sending", 2))
    )


_CiscoRptrPortIllegalAddrTrapAcked_Type.__name__ = "Integer32"
_CiscoRptrPortIllegalAddrTrapAcked_Object = MibTableColumn
ciscoRptrPortIllegalAddrTrapAcked = _CiscoRptrPortIllegalAddrTrapAcked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 10),
    _CiscoRptrPortIllegalAddrTrapAcked_Type()
)
ciscoRptrPortIllegalAddrTrapAcked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoRptrPortIllegalAddrTrapAcked.setStatus("current")


class _CiscoRptrPortIllegalAddrTrapEnabled_Type(TruthValue):
    """Custom type ciscoRptrPortIllegalAddrTrapEnabled based on TruthValue"""


_CiscoRptrPortIllegalAddrTrapEnabled_Object = MibTableColumn
ciscoRptrPortIllegalAddrTrapEnabled = _CiscoRptrPortIllegalAddrTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 11),
    _CiscoRptrPortIllegalAddrTrapEnabled_Type()
)
ciscoRptrPortIllegalAddrTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoRptrPortIllegalAddrTrapEnabled.setStatus("current")
_CiscoRptrPortIllegalAddrFirstHeard_Type = TimeStamp
_CiscoRptrPortIllegalAddrFirstHeard_Object = MibTableColumn
ciscoRptrPortIllegalAddrFirstHeard = _CiscoRptrPortIllegalAddrFirstHeard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 12),
    _CiscoRptrPortIllegalAddrFirstHeard_Type()
)
ciscoRptrPortIllegalAddrFirstHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoRptrPortIllegalAddrFirstHeard.setStatus("current")
_CiscoRptrPortIllegalAddrLastHeard_Type = TimeStamp
_CiscoRptrPortIllegalAddrLastHeard_Object = MibTableColumn
ciscoRptrPortIllegalAddrLastHeard = _CiscoRptrPortIllegalAddrLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 13),
    _CiscoRptrPortIllegalAddrLastHeard_Type()
)
ciscoRptrPortIllegalAddrLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoRptrPortIllegalAddrLastHeard.setStatus("current")
_CiscoRptrPortLastIllegalAddrCount_Type = Gauge32
_CiscoRptrPortLastIllegalAddrCount_Object = MibTableColumn
ciscoRptrPortLastIllegalAddrCount = _CiscoRptrPortLastIllegalAddrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 14),
    _CiscoRptrPortLastIllegalAddrCount_Type()
)
ciscoRptrPortLastIllegalAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoRptrPortLastIllegalAddrCount.setStatus("current")
_CiscoRptrPortIllegalAddrTotalCount_Type = Counter32
_CiscoRptrPortIllegalAddrTotalCount_Object = MibTableColumn
ciscoRptrPortIllegalAddrTotalCount = _CiscoRptrPortIllegalAddrTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 1, 1, 15),
    _CiscoRptrPortIllegalAddrTotalCount_Type()
)
ciscoRptrPortIllegalAddrTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoRptrPortIllegalAddrTotalCount.setStatus("current")
_CiscoRptrMIBglobal_ObjectIdentity = ObjectIdentity
ciscoRptrMIBglobal = _CiscoRptrMIBglobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 2)
)


class _CiscoRptrTrapAlgorithm_Type(Integer32):
    """Custom type ciscoRptrTrapAlgorithm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decay", 2),
          ("once", 1))
    )


_CiscoRptrTrapAlgorithm_Type.__name__ = "Integer32"
_CiscoRptrTrapAlgorithm_Object = MibScalar
ciscoRptrTrapAlgorithm = _CiscoRptrTrapAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 1, 2, 1),
    _CiscoRptrTrapAlgorithm_Type()
)
ciscoRptrTrapAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoRptrTrapAlgorithm.setStatus("current")
_CiscoRptrMIBConformance_ObjectIdentity = ObjectIdentity
ciscoRptrMIBConformance = _CiscoRptrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 2)
)
_CiscoRptrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoRptrMIBCompliances = _CiscoRptrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 1)
)
_CiscoRptrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoRptrMIBGroups = _CiscoRptrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 2)
)
_CiscoRptrMIBTrapPrefix_ObjectIdentity = ObjectIdentity
ciscoRptrMIBTrapPrefix = _CiscoRptrMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 3)
)
_CiscoRptrMIBTraps_ObjectIdentity = ObjectIdentity
ciscoRptrMIBTraps = _CiscoRptrMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 3, 0)
)
rptrPortEntry.registerAugmentions(
    ("CISCO-REPEATER-MIB",
     "ciscoRptrPortEntry")
)
ciscoRptrPortEntry.setIndexNames(*rptrPortEntry.getIndexNames())

# Managed Objects groups

ciscoRptrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 2, 1)
)
ciscoRptrMIBGroup.setObjects(
      *(("CISCO-REPEATER-MIB", "ciscoRptrPortMDIStatus"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortLinkTestEnabled"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortLinkTestFailed"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortAutoPolarityEnabled"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortAutoPolarityCorrected"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortSrcAddrCtrl"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortAllowedSrcAddr"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortAllowedSrcAddrStatus"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortLastIllegalSrcAddr"))
)
if mibBuilder.loadTexts:
    ciscoRptrMIBGroup.setStatus("obsolete")

ciscoRptrMIBPortGroupV11R01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 2, 2)
)
ciscoRptrMIBPortGroupV11R01.setObjects(
      *(("CISCO-REPEATER-MIB", "ciscoRptrPortMDIStatus"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortLinkTestEnabled"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortLinkTestFailed"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortAutoPolarityEnabled"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortAutoPolarityCorrected"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortSrcAddrCtrl"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortAllowedSrcAddr"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortAllowedSrcAddrStatus"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortLastIllegalSrcAddr"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortIllegalAddrTrapAcked"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortIllegalAddrTrapEnabled"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortIllegalAddrFirstHeard"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortIllegalAddrLastHeard"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortLastIllegalAddrCount"),
        ("CISCO-REPEATER-MIB", "ciscoRptrPortIllegalAddrTotalCount"))
)
if mibBuilder.loadTexts:
    ciscoRptrMIBPortGroupV11R01.setStatus("current")

ciscoRptrMIBGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 2, 3)
)
ciscoRptrMIBGlobalsGroup.setObjects(
    ("CISCO-REPEATER-MIB", "ciscoRptrTrapAlgorithm")
)
if mibBuilder.loadTexts:
    ciscoRptrMIBGlobalsGroup.setStatus("current")


# Notification objects

ciscoRptrIllegalSrcAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 3, 0, 1)
)
ciscoRptrIllegalSrcAddrTrap.setObjects(
    ("CISCO-REPEATER-MIB", "ciscoRptrPortLastIllegalSrcAddr")
)
if mibBuilder.loadTexts:
    ciscoRptrIllegalSrcAddrTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoRptrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRptrMIBCompliance.setStatus(
        "obsolete"
    )

ciscoRptrMIBComplianceV11R01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 22, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoRptrMIBComplianceV11R01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-REPEATER-MIB",
    **{"ciscoRptrMIB": ciscoRptrMIB,
       "ciscoRptrMIBObjects": ciscoRptrMIBObjects,
       "ciscoRptrPortTable": ciscoRptrPortTable,
       "ciscoRptrPortEntry": ciscoRptrPortEntry,
       "ciscoRptrPortMDIStatus": ciscoRptrPortMDIStatus,
       "ciscoRptrPortLinkTestEnabled": ciscoRptrPortLinkTestEnabled,
       "ciscoRptrPortLinkTestFailed": ciscoRptrPortLinkTestFailed,
       "ciscoRptrPortAutoPolarityEnabled": ciscoRptrPortAutoPolarityEnabled,
       "ciscoRptrPortAutoPolarityCorrected": ciscoRptrPortAutoPolarityCorrected,
       "ciscoRptrPortSrcAddrCtrl": ciscoRptrPortSrcAddrCtrl,
       "ciscoRptrPortAllowedSrcAddr": ciscoRptrPortAllowedSrcAddr,
       "ciscoRptrPortAllowedSrcAddrStatus": ciscoRptrPortAllowedSrcAddrStatus,
       "ciscoRptrPortLastIllegalSrcAddr": ciscoRptrPortLastIllegalSrcAddr,
       "ciscoRptrPortIllegalAddrTrapAcked": ciscoRptrPortIllegalAddrTrapAcked,
       "ciscoRptrPortIllegalAddrTrapEnabled": ciscoRptrPortIllegalAddrTrapEnabled,
       "ciscoRptrPortIllegalAddrFirstHeard": ciscoRptrPortIllegalAddrFirstHeard,
       "ciscoRptrPortIllegalAddrLastHeard": ciscoRptrPortIllegalAddrLastHeard,
       "ciscoRptrPortLastIllegalAddrCount": ciscoRptrPortLastIllegalAddrCount,
       "ciscoRptrPortIllegalAddrTotalCount": ciscoRptrPortIllegalAddrTotalCount,
       "ciscoRptrMIBglobal": ciscoRptrMIBglobal,
       "ciscoRptrTrapAlgorithm": ciscoRptrTrapAlgorithm,
       "ciscoRptrMIBConformance": ciscoRptrMIBConformance,
       "ciscoRptrMIBCompliances": ciscoRptrMIBCompliances,
       "ciscoRptrMIBCompliance": ciscoRptrMIBCompliance,
       "ciscoRptrMIBComplianceV11R01": ciscoRptrMIBComplianceV11R01,
       "ciscoRptrMIBGroups": ciscoRptrMIBGroups,
       "ciscoRptrMIBGroup": ciscoRptrMIBGroup,
       "ciscoRptrMIBPortGroupV11R01": ciscoRptrMIBPortGroupV11R01,
       "ciscoRptrMIBGlobalsGroup": ciscoRptrMIBGlobalsGroup,
       "ciscoRptrMIBTrapPrefix": ciscoRptrMIBTrapPrefix,
       "ciscoRptrMIBTraps": ciscoRptrMIBTraps,
       "ciscoRptrIllegalSrcAddrTrap": ciscoRptrIllegalSrcAddrTrap}
)
