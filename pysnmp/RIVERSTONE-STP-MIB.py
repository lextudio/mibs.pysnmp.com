# SNMP MIB module (RIVERSTONE-STP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIVERSTONE-STP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:56 2024
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

(dot1dBasePortEntry,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePortEntry")

(riverstoneMibs,) = mibBuilder.importSymbols(
    "RSTONE-SMI-MIB",
    "riverstoneMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsStpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12)
)
rsStpMib.setRevisions(
        ("2000-07-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RSStpProtocolVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fastSTP", 4),
          ("ieee802", 2),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RsStpGlobals_ObjectIdentity = ObjectIdentity
rsStpGlobals = _RsStpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 1)
)
if mibBuilder.loadTexts:
    rsStpGlobals.setStatus("current")
_RsStpStatus_Type = TruthValue
_RsStpStatus_Object = MibScalar
rsStpStatus = _RsStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 1, 1),
    _RsStpStatus_Type()
)
rsStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpStatus.setStatus("current")
_RsStpProtocol_Type = RSStpProtocolVersion
_RsStpProtocol_Object = MibScalar
rsStpProtocol = _RsStpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 1, 2),
    _RsStpProtocol_Type()
)
rsStpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpProtocol.setStatus("current")
_RsStpProtocolsSupported_Type = Integer32
_RsStpProtocolsSupported_Object = MibScalar
rsStpProtocolsSupported = _RsStpProtocolsSupported_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 1, 3),
    _RsStpProtocolsSupported_Type()
)
rsStpProtocolsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpProtocolsSupported.setStatus("current")
_RsStpLastSetErrorReason_Type = SnmpAdminString
_RsStpLastSetErrorReason_Object = MibScalar
rsStpLastSetErrorReason = _RsStpLastSetErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 1, 4),
    _RsStpLastSetErrorReason_Type()
)
rsStpLastSetErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpLastSetErrorReason.setStatus("current")
_RsStpPortsLevel_ObjectIdentity = ObjectIdentity
rsStpPortsLevel = _RsStpPortsLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 2)
)
if mibBuilder.loadTexts:
    rsStpPortsLevel.setStatus("current")
_RsStpLastChanged_Type = TimeTicks
_RsStpLastChanged_Object = MibScalar
rsStpLastChanged = _RsStpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 2, 1),
    _RsStpLastChanged_Type()
)
rsStpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpLastChanged.setStatus("current")
_RsStpBaseTable_Object = MibTable
rsStpBaseTable = _RsStpBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 2, 2)
)
if mibBuilder.loadTexts:
    rsStpBaseTable.setStatus("current")
_RsStpBaseEntry_Object = MibTableRow
rsStpBaseEntry = _RsStpBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rsStpBaseEntry.setStatus("current")
_RsStpBaseEnableProtocol_Type = TruthValue
_RsStpBaseEnableProtocol_Object = MibTableColumn
rsStpBaseEnableProtocol = _RsStpBaseEnableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 2, 2, 1, 1),
    _RsStpBaseEnableProtocol_Type()
)
rsStpBaseEnableProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpBaseEnableProtocol.setStatus("current")
_RsStpBaseBlockBpdu_Type = TruthValue
_RsStpBaseBlockBpdu_Object = MibTableColumn
rsStpBaseBlockBpdu = _RsStpBaseBlockBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 2, 2, 1, 2),
    _RsStpBaseBlockBpdu_Type()
)
rsStpBaseBlockBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsStpBaseBlockBpdu.setStatus("current")
_RsStpBaseBpduSends_Type = Counter32
_RsStpBaseBpduSends_Object = MibTableColumn
rsStpBaseBpduSends = _RsStpBaseBpduSends_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 2, 2, 1, 3),
    _RsStpBaseBpduSends_Type()
)
rsStpBaseBpduSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpBaseBpduSends.setStatus("current")
_RsStpBaseBpduReceives_Type = Counter32
_RsStpBaseBpduReceives_Object = MibTableColumn
rsStpBaseBpduReceives = _RsStpBaseBpduReceives_Object(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 2, 2, 1, 4),
    _RsStpBaseBpduReceives_Type()
)
rsStpBaseBpduReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsStpBaseBpduReceives.setStatus("current")
_RsStpConformance_ObjectIdentity = ObjectIdentity
rsStpConformance = _RsStpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 10)
)
_RsStpGroups_ObjectIdentity = ObjectIdentity
rsStpGroups = _RsStpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 10, 1)
)
_RsStpCompliances_ObjectIdentity = ObjectIdentity
rsStpCompliances = _RsStpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 10, 2)
)
dot1dBasePortEntry.registerAugmentions(
    ("RIVERSTONE-STP-MIB",
     "rsStpBaseEntry")
)
rsStpBaseEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups

rsStpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 10, 1, 1)
)
rsStpBaseGroup.setObjects(
      *(("RIVERSTONE-STP-MIB", "rsStpStatus"),
        ("RIVERSTONE-STP-MIB", "rsStpLastChanged"),
        ("RIVERSTONE-STP-MIB", "rsStpBaseEnableProtocol"),
        ("RIVERSTONE-STP-MIB", "rsStpBaseBlockBpdu"),
        ("RIVERSTONE-STP-MIB", "rsStpBaseBpduSends"),
        ("RIVERSTONE-STP-MIB", "rsStpBaseBpduReceives"),
        ("RIVERSTONE-STP-MIB", "rsStpProtocol"),
        ("RIVERSTONE-STP-MIB", "rsStpProtocolsSupported"),
        ("RIVERSTONE-STP-MIB", "rsStpLastSetErrorReason"))
)
if mibBuilder.loadTexts:
    rsStpBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsStpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5567, 2, 12, 10, 2, 1)
)
if mibBuilder.loadTexts:
    rsStpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIVERSTONE-STP-MIB",
    **{"RSStpProtocolVersion": RSStpProtocolVersion,
       "rsStpMib": rsStpMib,
       "rsStpGlobals": rsStpGlobals,
       "rsStpStatus": rsStpStatus,
       "rsStpProtocol": rsStpProtocol,
       "rsStpProtocolsSupported": rsStpProtocolsSupported,
       "rsStpLastSetErrorReason": rsStpLastSetErrorReason,
       "rsStpPortsLevel": rsStpPortsLevel,
       "rsStpLastChanged": rsStpLastChanged,
       "rsStpBaseTable": rsStpBaseTable,
       "rsStpBaseEntry": rsStpBaseEntry,
       "rsStpBaseEnableProtocol": rsStpBaseEnableProtocol,
       "rsStpBaseBlockBpdu": rsStpBaseBlockBpdu,
       "rsStpBaseBpduSends": rsStpBaseBpduSends,
       "rsStpBaseBpduReceives": rsStpBaseBpduReceives,
       "rsStpConformance": rsStpConformance,
       "rsStpGroups": rsStpGroups,
       "rsStpBaseGroup": rsStpBaseGroup,
       "rsStpCompliances": rsStpCompliances,
       "rsStpMibCompliance": rsStpMibCompliance}
)
