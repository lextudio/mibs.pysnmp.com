# SNMP MIB module (TPLINK-ROUTEMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-ROUTEMAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:36 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkRouteMapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76)
)
tplinkRouteMapMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



class TPRouteMapMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TplinkRouteMapMIBObjects_ObjectIdentity = ObjectIdentity
tplinkRouteMapMIBObjects = _TplinkRouteMapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1)
)
_TpIpPrefixConfig_ObjectIdentity = ObjectIdentity
tpIpPrefixConfig = _TpIpPrefixConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1)
)
_TpIpPrefixConfigTable_Object = MibTable
tpIpPrefixConfigTable = _TpIpPrefixConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpIpPrefixConfigTable.setStatus("current")
_TpIpPrefixConfigEntry_Object = MibTableRow
tpIpPrefixConfigEntry = _TpIpPrefixConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1, 1, 1)
)
tpIpPrefixConfigEntry.setIndexNames(
    (0, "TPLINK-ROUTEMAP-MIB", "tpIpPrefixName"),
    (0, "TPLINK-ROUTEMAP-MIB", "tpIpPrefixSeq"),
)
if mibBuilder.loadTexts:
    tpIpPrefixConfigEntry.setStatus("current")


class _TpIpPrefixName_Type(OctetString):
    """Custom type tpIpPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TpIpPrefixName_Type.__name__ = "OctetString"
_TpIpPrefixName_Object = MibTableColumn
tpIpPrefixName = _TpIpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1, 1, 1, 1),
    _TpIpPrefixName_Type()
)
tpIpPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpPrefixName.setStatus("current")
_TpIpPrefixMode_Type = TPRouteMapMode
_TpIpPrefixMode_Object = MibTableColumn
tpIpPrefixMode = _TpIpPrefixMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1, 1, 1, 2),
    _TpIpPrefixMode_Type()
)
tpIpPrefixMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpPrefixMode.setStatus("current")
_TpIpPrefixSeq_Type = Integer32
_TpIpPrefixSeq_Object = MibTableColumn
tpIpPrefixSeq = _TpIpPrefixSeq_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1, 1, 1, 3),
    _TpIpPrefixSeq_Type()
)
tpIpPrefixSeq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpPrefixSeq.setStatus("current")


class _TpNetwork_Type(OctetString):
    """Custom type tpNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_TpNetwork_Type.__name__ = "OctetString"
_TpNetwork_Object = MibTableColumn
tpNetwork = _TpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1, 1, 1, 4),
    _TpNetwork_Type()
)
tpNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpNetwork.setStatus("current")
_TpMaskGe_Type = Integer32
_TpMaskGe_Object = MibTableColumn
tpMaskGe = _TpMaskGe_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1, 1, 1, 5),
    _TpMaskGe_Type()
)
tpMaskGe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMaskGe.setStatus("current")
_TpMaskLe_Type = Integer32
_TpMaskLe_Object = MibTableColumn
tpMaskLe = _TpMaskLe_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1, 1, 1, 6),
    _TpMaskLe_Type()
)
tpMaskLe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMaskLe.setStatus("current")
_TpIpPrefixItemStatus_Type = TPRowStatus
_TpIpPrefixItemStatus_Object = MibTableColumn
tpIpPrefixItemStatus = _TpIpPrefixItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 1, 1, 1, 7),
    _TpIpPrefixItemStatus_Type()
)
tpIpPrefixItemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpIpPrefixItemStatus.setStatus("current")
_TpRouteMapConfig_ObjectIdentity = ObjectIdentity
tpRouteMapConfig = _TpRouteMapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2)
)
_TpRouteMapConfigTable_Object = MibTable
tpRouteMapConfigTable = _TpRouteMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpRouteMapConfigTable.setStatus("current")
_TpRouteMapConfigEntry_Object = MibTableRow
tpRouteMapConfigEntry = _TpRouteMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 1, 1)
)
tpRouteMapConfigEntry.setIndexNames(
    (0, "TPLINK-ROUTEMAP-MIB", "tpRouteMapName"),
    (0, "TPLINK-ROUTEMAP-MIB", "tpRuleId"),
)
if mibBuilder.loadTexts:
    tpRouteMapConfigEntry.setStatus("current")


class _TpRouteMapName_Type(OctetString):
    """Custom type tpRouteMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TpRouteMapName_Type.__name__ = "OctetString"
_TpRouteMapName_Object = MibTableColumn
tpRouteMapName = _TpRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 1, 1, 1),
    _TpRouteMapName_Type()
)
tpRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRouteMapName.setStatus("current")
_TpConfigMode_Type = TPRouteMapMode
_TpConfigMode_Object = MibTableColumn
tpConfigMode = _TpConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 1, 1, 2),
    _TpConfigMode_Type()
)
tpConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpConfigMode.setStatus("current")
_TpRuleId_Type = Integer32
_TpRuleId_Object = MibTableColumn
tpRuleId = _TpRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 1, 1, 3),
    _TpRuleId_Type()
)
tpRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRuleId.setStatus("current")
_TpConfigItemStatus_Type = TPRowStatus
_TpConfigItemStatus_Object = MibTableColumn
tpConfigItemStatus = _TpConfigItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 1, 1, 4),
    _TpConfigItemStatus_Type()
)
tpConfigItemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpConfigItemStatus.setStatus("current")
_TpRouteMapMatchConfigTable_Object = MibTable
tpRouteMapMatchConfigTable = _TpRouteMapMatchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tpRouteMapMatchConfigTable.setStatus("current")
_TpRouteMapMatchConfigEntry_Object = MibTableRow
tpRouteMapMatchConfigEntry = _TpRouteMapMatchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1)
)
tpRouteMapMatchConfigEntry.setIndexNames(
    (0, "TPLINK-ROUTEMAP-MIB", "tpRouteMapName"),
    (0, "TPLINK-ROUTEMAP-MIB", "tpRuleId"),
)
if mibBuilder.loadTexts:
    tpRouteMapMatchConfigEntry.setStatus("current")
_TpMatchMode_Type = TPRouteMapMode
_TpMatchMode_Object = MibTableColumn
tpMatchMode = _TpMatchMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1, 1),
    _TpMatchMode_Type()
)
tpMatchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMatchMode.setStatus("current")


class _TpSIPAcl_Type(OctetString):
    """Custom type tpSIPAcl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TpSIPAcl_Type.__name__ = "OctetString"
_TpSIPAcl_Object = MibTableColumn
tpSIPAcl = _TpSIPAcl_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1, 2),
    _TpSIPAcl_Type()
)
tpSIPAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSIPAcl.setStatus("current")


class _TpSIPPrefixList_Type(OctetString):
    """Custom type tpSIPPrefixList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TpSIPPrefixList_Type.__name__ = "OctetString"
_TpSIPPrefixList_Object = MibTableColumn
tpSIPPrefixList = _TpSIPPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1, 3),
    _TpSIPPrefixList_Type()
)
tpSIPPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSIPPrefixList.setStatus("current")


class _TpDIPAcl_Type(OctetString):
    """Custom type tpDIPAcl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TpDIPAcl_Type.__name__ = "OctetString"
_TpDIPAcl_Object = MibTableColumn
tpDIPAcl = _TpDIPAcl_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1, 4),
    _TpDIPAcl_Type()
)
tpDIPAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDIPAcl.setStatus("current")


class _TpDIPPrefixList_Type(OctetString):
    """Custom type tpDIPPrefixList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TpDIPPrefixList_Type.__name__ = "OctetString"
_TpDIPPrefixList_Object = MibTableColumn
tpDIPPrefixList = _TpDIPPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1, 5),
    _TpDIPPrefixList_Type()
)
tpDIPPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpDIPPrefixList.setStatus("current")


class _TpNXPAcl_Type(OctetString):
    """Custom type tpNXPAcl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TpNXPAcl_Type.__name__ = "OctetString"
_TpNXPAcl_Object = MibTableColumn
tpNXPAcl = _TpNXPAcl_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1, 6),
    _TpNXPAcl_Type()
)
tpNXPAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpNXPAcl.setStatus("current")


class _TpNXPPrefixList_Type(OctetString):
    """Custom type tpNXPPrefixList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TpNXPPrefixList_Type.__name__ = "OctetString"
_TpNXPPrefixList_Object = MibTableColumn
tpNXPPrefixList = _TpNXPPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1, 7),
    _TpNXPPrefixList_Type()
)
tpNXPPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpNXPPrefixList.setStatus("current")
_TpMatchMetric_Type = Integer32
_TpMatchMetric_Object = MibTableColumn
tpMatchMetric = _TpMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1, 8),
    _TpMatchMetric_Type()
)
tpMatchMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMatchMetric.setStatus("current")
_TpMatchItemStatus_Type = TPRowStatus
_TpMatchItemStatus_Object = MibTableColumn
tpMatchItemStatus = _TpMatchItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 2, 1, 9),
    _TpMatchItemStatus_Type()
)
tpMatchItemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMatchItemStatus.setStatus("current")
_TpRouteMapSetConfigTable_Object = MibTable
tpRouteMapSetConfigTable = _TpRouteMapSetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tpRouteMapSetConfigTable.setStatus("current")
_TpRouteMapSetConfigEntry_Object = MibTableRow
tpRouteMapSetConfigEntry = _TpRouteMapSetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 3, 1)
)
tpRouteMapSetConfigEntry.setIndexNames(
    (0, "TPLINK-ROUTEMAP-MIB", "tpRouteMapName"),
    (0, "TPLINK-ROUTEMAP-MIB", "tpRuleId"),
)
if mibBuilder.loadTexts:
    tpRouteMapSetConfigEntry.setStatus("current")
_TpSetMode_Type = TPRouteMapMode
_TpSetMode_Object = MibTableColumn
tpSetMode = _TpSetMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 3, 1, 1),
    _TpSetMode_Type()
)
tpSetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSetMode.setStatus("current")
_TpSetMetric_Type = Integer32
_TpSetMetric_Object = MibTableColumn
tpSetMetric = _TpSetMetric_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 3, 1, 2),
    _TpSetMetric_Type()
)
tpSetMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSetMetric.setStatus("current")
_TpSetNexthop_Type = IpAddress
_TpSetNexthop_Object = MibTableColumn
tpSetNexthop = _TpSetNexthop_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 3, 1, 3),
    _TpSetNexthop_Type()
)
tpSetNexthop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSetNexthop.setStatus("current")
_TpSetItemStatus_Type = TPRowStatus
_TpSetItemStatus_Object = MibTableColumn
tpSetItemStatus = _TpSetItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 2, 3, 1, 4),
    _TpSetItemStatus_Type()
)
tpSetItemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpSetItemStatus.setStatus("current")
_TpRouteMapBindConfig_ObjectIdentity = ObjectIdentity
tpRouteMapBindConfig = _TpRouteMapBindConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 3)
)
_TpRouteMapBindConfigTable_Object = MibTable
tpRouteMapBindConfigTable = _TpRouteMapBindConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpRouteMapBindConfigTable.setStatus("current")
_TpRouteMapBindConfigEntry_Object = MibTableRow
tpRouteMapBindConfigEntry = _TpRouteMapBindConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 3, 1, 1)
)
tpRouteMapBindConfigEntry.setIndexNames(
    (0, "TPLINK-ROUTEMAP-MIB", "tpRouteMapBindName"),
    (0, "TPLINK-ROUTEMAP-MIB", "tpBindVid"),
)
if mibBuilder.loadTexts:
    tpRouteMapBindConfigEntry.setStatus("current")


class _TpRouteMapBindName_Type(OctetString):
    """Custom type tpRouteMapBindName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TpRouteMapBindName_Type.__name__ = "OctetString"
_TpRouteMapBindName_Object = MibTableColumn
tpRouteMapBindName = _TpRouteMapBindName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 3, 1, 1, 1),
    _TpRouteMapBindName_Type()
)
tpRouteMapBindName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRouteMapBindName.setStatus("current")
_TpBindVid_Type = Integer32
_TpBindVid_Object = MibTableColumn
tpBindVid = _TpBindVid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 3, 1, 1, 2),
    _TpBindVid_Type()
)
tpBindVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpBindVid.setStatus("current")
_TpBindItemStatus_Type = TPRowStatus
_TpBindItemStatus_Object = MibTableColumn
tpBindItemStatus = _TpBindItemStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 1, 3, 1, 1, 3),
    _TpBindItemStatus_Type()
)
tpBindItemStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpBindItemStatus.setStatus("current")
_TplinkRouteMapNotifications_ObjectIdentity = ObjectIdentity
tplinkRouteMapNotifications = _TplinkRouteMapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 76, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ROUTEMAP-MIB",
    **{"MacAddress": MacAddress,
       "TPRouteMapMode": TPRouteMapMode,
       "tplinkRouteMapMIB": tplinkRouteMapMIB,
       "tplinkRouteMapMIBObjects": tplinkRouteMapMIBObjects,
       "tpIpPrefixConfig": tpIpPrefixConfig,
       "tpIpPrefixConfigTable": tpIpPrefixConfigTable,
       "tpIpPrefixConfigEntry": tpIpPrefixConfigEntry,
       "tpIpPrefixName": tpIpPrefixName,
       "tpIpPrefixMode": tpIpPrefixMode,
       "tpIpPrefixSeq": tpIpPrefixSeq,
       "tpNetwork": tpNetwork,
       "tpMaskGe": tpMaskGe,
       "tpMaskLe": tpMaskLe,
       "tpIpPrefixItemStatus": tpIpPrefixItemStatus,
       "tpRouteMapConfig": tpRouteMapConfig,
       "tpRouteMapConfigTable": tpRouteMapConfigTable,
       "tpRouteMapConfigEntry": tpRouteMapConfigEntry,
       "tpRouteMapName": tpRouteMapName,
       "tpConfigMode": tpConfigMode,
       "tpRuleId": tpRuleId,
       "tpConfigItemStatus": tpConfigItemStatus,
       "tpRouteMapMatchConfigTable": tpRouteMapMatchConfigTable,
       "tpRouteMapMatchConfigEntry": tpRouteMapMatchConfigEntry,
       "tpMatchMode": tpMatchMode,
       "tpSIPAcl": tpSIPAcl,
       "tpSIPPrefixList": tpSIPPrefixList,
       "tpDIPAcl": tpDIPAcl,
       "tpDIPPrefixList": tpDIPPrefixList,
       "tpNXPAcl": tpNXPAcl,
       "tpNXPPrefixList": tpNXPPrefixList,
       "tpMatchMetric": tpMatchMetric,
       "tpMatchItemStatus": tpMatchItemStatus,
       "tpRouteMapSetConfigTable": tpRouteMapSetConfigTable,
       "tpRouteMapSetConfigEntry": tpRouteMapSetConfigEntry,
       "tpSetMode": tpSetMode,
       "tpSetMetric": tpSetMetric,
       "tpSetNexthop": tpSetNexthop,
       "tpSetItemStatus": tpSetItemStatus,
       "tpRouteMapBindConfig": tpRouteMapBindConfig,
       "tpRouteMapBindConfigTable": tpRouteMapBindConfigTable,
       "tpRouteMapBindConfigEntry": tpRouteMapBindConfigEntry,
       "tpRouteMapBindName": tpRouteMapBindName,
       "tpBindVid": tpBindVid,
       "tpBindItemStatus": tpBindItemStatus,
       "tplinkRouteMapNotifications": tplinkRouteMapNotifications}
)
