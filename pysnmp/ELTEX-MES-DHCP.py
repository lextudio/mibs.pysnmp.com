# SNMP MIB module (ELTEX-MES-DHCP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-DHCP
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:36 2024
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

(eltMesDhcp,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesDhcp")

(rlDhcpSrvConfParamsEntry,) = mibBuilder.importSymbols(
    "RADLAN-DHCP-MIB",
    "rlDhcpSrvConfParamsEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EltDhcpRelayOption82PolicyType(Integer32, TextualConvention):
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
        *(("drop", 2),
          ("keep", 3),
          ("replace", 1))
    )



class EltDhcpRelayOption82SuboptionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("custom", 2),
          ("tr101", 1))
    )



class EltDhcpRelayOption82CombinationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bin", 5),
          ("pv", 3),
          ("spv", 4),
          ("sv", 2))
    )



class EltDhcpRelayOption82DelimiterType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("comma", 3),
          ("dot", 2),
          ("hash", 5),
          ("semicolon", 4),
          ("slash", 6),
          ("space", 7),
          ("tr101", 1))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesDhcpRelay_ObjectIdentity = ObjectIdentity
eltMesDhcpRelay = _EltMesDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1)
)
_EltMesDhcpRelayOption82_ObjectIdentity = ObjectIdentity
eltMesDhcpRelayOption82 = _EltMesDhcpRelayOption82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1)
)
_EltDhcpRelayOption82Policy_Type = EltDhcpRelayOption82PolicyType
_EltDhcpRelayOption82Policy_Object = MibScalar
eltDhcpRelayOption82Policy = _EltDhcpRelayOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 1),
    _EltDhcpRelayOption82Policy_Type()
)
eltDhcpRelayOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDhcpRelayOption82Policy.setStatus("current")
_EltDhcpRelayOption82IfPolicyTable_Object = MibTable
eltDhcpRelayOption82IfPolicyTable = _EltDhcpRelayOption82IfPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltDhcpRelayOption82IfPolicyTable.setStatus("current")
_EltDhcpRelayOption82IfPolicyEntry_Object = MibTableRow
eltDhcpRelayOption82IfPolicyEntry = _EltDhcpRelayOption82IfPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2, 1)
)
eltDhcpRelayOption82IfPolicyEntry.setIndexNames(
    (0, "ELTEX-MES-DHCP", "eltDhcpRelayOption82IfIndex"),
)
if mibBuilder.loadTexts:
    eltDhcpRelayOption82IfPolicyEntry.setStatus("current")
_EltDhcpRelayOption82IfIndex_Type = Integer32
_EltDhcpRelayOption82IfIndex_Object = MibTableColumn
eltDhcpRelayOption82IfIndex = _EltDhcpRelayOption82IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2, 1, 1),
    _EltDhcpRelayOption82IfIndex_Type()
)
eltDhcpRelayOption82IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltDhcpRelayOption82IfIndex.setStatus("current")


class _EltDhcpRelayOption82IfPolicy_Type(Integer32):
    """Custom type eltDhcpRelayOption82IfPolicy based on Integer32"""
    defaultValue = 4

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
        *(("drop", 2),
          ("global", 4),
          ("keep", 3),
          ("replace", 1))
    )


_EltDhcpRelayOption82IfPolicy_Type.__name__ = "Integer32"
_EltDhcpRelayOption82IfPolicy_Object = MibTableColumn
eltDhcpRelayOption82IfPolicy = _EltDhcpRelayOption82IfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2, 1, 2),
    _EltDhcpRelayOption82IfPolicy_Type()
)
eltDhcpRelayOption82IfPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDhcpRelayOption82IfPolicy.setStatus("current")


class _EltDhcpRelayOption82AccessNodeIdentifier_Type(DisplayString):
    """Custom type eltDhcpRelayOption82AccessNodeIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_EltDhcpRelayOption82AccessNodeIdentifier_Type.__name__ = "DisplayString"
_EltDhcpRelayOption82AccessNodeIdentifier_Object = MibScalar
eltDhcpRelayOption82AccessNodeIdentifier = _EltDhcpRelayOption82AccessNodeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 3),
    _EltDhcpRelayOption82AccessNodeIdentifier_Type()
)
eltDhcpRelayOption82AccessNodeIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDhcpRelayOption82AccessNodeIdentifier.setStatus("current")
_EltDhcpRelayOption82CircuitIdSuboptionsCombination_Type = EltDhcpRelayOption82CombinationType
_EltDhcpRelayOption82CircuitIdSuboptionsCombination_Object = MibScalar
eltDhcpRelayOption82CircuitIdSuboptionsCombination = _EltDhcpRelayOption82CircuitIdSuboptionsCombination_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 4),
    _EltDhcpRelayOption82CircuitIdSuboptionsCombination_Type()
)
eltDhcpRelayOption82CircuitIdSuboptionsCombination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDhcpRelayOption82CircuitIdSuboptionsCombination.setStatus("current")
_EltDhcpRelayOption82CircuitIdSuboptionsDelimeter_Type = EltDhcpRelayOption82DelimiterType
_EltDhcpRelayOption82CircuitIdSuboptionsDelimeter_Object = MibScalar
eltDhcpRelayOption82CircuitIdSuboptionsDelimeter = _EltDhcpRelayOption82CircuitIdSuboptionsDelimeter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 5),
    _EltDhcpRelayOption82CircuitIdSuboptionsDelimeter_Type()
)
eltDhcpRelayOption82CircuitIdSuboptionsDelimeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDhcpRelayOption82CircuitIdSuboptionsDelimeter.setStatus("current")
_EltDhcpRelayOption82SuboptionType_Type = EltDhcpRelayOption82SuboptionType
_EltDhcpRelayOption82SuboptionType_Object = MibScalar
eltDhcpRelayOption82SuboptionType = _EltDhcpRelayOption82SuboptionType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 6),
    _EltDhcpRelayOption82SuboptionType_Type()
)
eltDhcpRelayOption82SuboptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDhcpRelayOption82SuboptionType.setStatus("current")


class _EltDhcpRelayOption82RemoteIdentifier_Type(DisplayString):
    """Custom type eltDhcpRelayOption82RemoteIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_EltDhcpRelayOption82RemoteIdentifier_Type.__name__ = "DisplayString"
_EltDhcpRelayOption82RemoteIdentifier_Object = MibScalar
eltDhcpRelayOption82RemoteIdentifier = _EltDhcpRelayOption82RemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 7),
    _EltDhcpRelayOption82RemoteIdentifier_Type()
)
eltDhcpRelayOption82RemoteIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDhcpRelayOption82RemoteIdentifier.setStatus("current")
_EltDhcpRelayBroadcastEnable_Type = TruthValue
_EltDhcpRelayBroadcastEnable_Object = MibScalar
eltDhcpRelayBroadcastEnable = _EltDhcpRelayBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 2),
    _EltDhcpRelayBroadcastEnable_Type()
)
eltDhcpRelayBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDhcpRelayBroadcastEnable.setStatus("current")
_EltMesDhcpSrv_ObjectIdentity = ObjectIdentity
eltMesDhcpSrv = _EltMesDhcpSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2)
)
_EltDhcpSrvConfParamsTable_Object = MibTable
eltDhcpSrvConfParamsTable = _EltDhcpSrvConfParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2, 1)
)
if mibBuilder.loadTexts:
    eltDhcpSrvConfParamsTable.setStatus("current")
_EltDhcpSrvConfParamsEntry_Object = MibTableRow
eltDhcpSrvConfParamsEntry = _EltDhcpSrvConfParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltDhcpSrvConfParamsEntry.setStatus("current")
_EltDhcpSrvConfParamsTftpSrvList_Type = DisplayString
_EltDhcpSrvConfParamsTftpSrvList_Object = MibTableColumn
eltDhcpSrvConfParamsTftpSrvList = _EltDhcpSrvConfParamsTftpSrvList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2, 1, 1, 1),
    _EltDhcpSrvConfParamsTftpSrvList_Type()
)
eltDhcpSrvConfParamsTftpSrvList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltDhcpSrvConfParamsTftpSrvList.setStatus("current")
rlDhcpSrvConfParamsEntry.registerAugmentions(
    ("ELTEX-MES-DHCP",
     "eltDhcpSrvConfParamsEntry")
)
eltDhcpSrvConfParamsEntry.setIndexNames(*rlDhcpSrvConfParamsEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-DHCP",
    **{"EltDhcpRelayOption82PolicyType": EltDhcpRelayOption82PolicyType,
       "EltDhcpRelayOption82SuboptionType": EltDhcpRelayOption82SuboptionType,
       "EltDhcpRelayOption82CombinationType": EltDhcpRelayOption82CombinationType,
       "EltDhcpRelayOption82DelimiterType": EltDhcpRelayOption82DelimiterType,
       "eltMesDhcpRelay": eltMesDhcpRelay,
       "eltMesDhcpRelayOption82": eltMesDhcpRelayOption82,
       "eltDhcpRelayOption82Policy": eltDhcpRelayOption82Policy,
       "eltDhcpRelayOption82IfPolicyTable": eltDhcpRelayOption82IfPolicyTable,
       "eltDhcpRelayOption82IfPolicyEntry": eltDhcpRelayOption82IfPolicyEntry,
       "eltDhcpRelayOption82IfIndex": eltDhcpRelayOption82IfIndex,
       "eltDhcpRelayOption82IfPolicy": eltDhcpRelayOption82IfPolicy,
       "eltDhcpRelayOption82AccessNodeIdentifier": eltDhcpRelayOption82AccessNodeIdentifier,
       "eltDhcpRelayOption82CircuitIdSuboptionsCombination": eltDhcpRelayOption82CircuitIdSuboptionsCombination,
       "eltDhcpRelayOption82CircuitIdSuboptionsDelimeter": eltDhcpRelayOption82CircuitIdSuboptionsDelimeter,
       "eltDhcpRelayOption82SuboptionType": eltDhcpRelayOption82SuboptionType,
       "eltDhcpRelayOption82RemoteIdentifier": eltDhcpRelayOption82RemoteIdentifier,
       "eltDhcpRelayBroadcastEnable": eltDhcpRelayBroadcastEnable,
       "eltMesDhcpSrv": eltMesDhcpSrv,
       "eltDhcpSrvConfParamsTable": eltDhcpSrvConfParamsTable,
       "eltDhcpSrvConfParamsEntry": eltDhcpSrvConfParamsEntry,
       "eltDhcpSrvConfParamsTftpSrvList": eltDhcpSrvConfParamsTftpSrvList}
)
