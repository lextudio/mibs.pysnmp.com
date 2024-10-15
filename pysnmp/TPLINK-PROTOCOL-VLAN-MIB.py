# SNMP MIB module (TPLINK-PROTOCOL-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-PROTOCOL-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:33 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

tplinkProtocolVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16)
)
tplinkProtocolVlanMIB.setRevisions(
        ("2009-08-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkProtocolVlanMIBObjects_ObjectIdentity = ObjectIdentity
tplinkProtocolVlanMIBObjects = _TplinkProtocolVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1)
)
_ProtocolTemplate_ObjectIdentity = ObjectIdentity
protocolTemplate = _ProtocolTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 1)
)
_ProtocolTemplateTable_Object = MibTable
protocolTemplateTable = _ProtocolTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    protocolTemplateTable.setStatus("current")
_TemplateEntry_Object = MibTableRow
templateEntry = _TemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 1, 1, 1)
)
templateEntry.setIndexNames(
    (0, "TPLINK-PROTOCOL-VLAN-MIB", "templateProtocolName"),
)
if mibBuilder.loadTexts:
    templateEntry.setStatus("current")


class _TemplateProtocolName_Type(OctetString):
    """Custom type templateProtocolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TemplateProtocolName_Type.__name__ = "OctetString"
_TemplateProtocolName_Object = MibTableColumn
templateProtocolName = _TemplateProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 1, 1, 1, 1),
    _TemplateProtocolName_Type()
)
templateProtocolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    templateProtocolName.setStatus("current")


class _TemplateEtherType_Type(OctetString):
    """Custom type templateEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TemplateEtherType_Type.__name__ = "OctetString"
_TemplateEtherType_Object = MibTableColumn
templateEtherType = _TemplateEtherType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 1, 1, 1, 2),
    _TemplateEtherType_Type()
)
templateEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    templateEtherType.setStatus("current")


class _TemplateFrameType_Type(Integer32):
    """Custom type templateFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet8023", 0),
          ("ethernetII", 1),
          ("llc", 3),
          ("snap", 2))
    )


_TemplateFrameType_Type.__name__ = "Integer32"
_TemplateFrameType_Object = MibTableColumn
templateFrameType = _TemplateFrameType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 1, 1, 1, 3),
    _TemplateFrameType_Type()
)
templateFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    templateFrameType.setStatus("current")
_TemplateStatus_Type = TPRowStatus
_TemplateStatus_Object = MibTableColumn
templateStatus = _TemplateStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 1, 1, 1, 4),
    _TemplateStatus_Type()
)
templateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    templateStatus.setStatus("current")
_ProtocolGroup_ObjectIdentity = ObjectIdentity
protocolGroup = _ProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 2)
)
_ProtocolGroupTable_Object = MibTable
protocolGroupTable = _ProtocolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    protocolGroupTable.setStatus("current")
_ProtocolVlanEntry_Object = MibTableRow
protocolVlanEntry = _ProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 2, 1, 1)
)
protocolVlanEntry.setIndexNames(
    (0, "TPLINK-PROTOCOL-VLAN-MIB", "protocolName"),
)
if mibBuilder.loadTexts:
    protocolVlanEntry.setStatus("current")


class _ProtocolName_Type(OctetString):
    """Custom type protocolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProtocolName_Type.__name__ = "OctetString"
_ProtocolName_Object = MibTableColumn
protocolName = _ProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 2, 1, 1, 1),
    _ProtocolName_Type()
)
protocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolName.setStatus("current")


class _ProtocolVlanId_Type(Integer32):
    """Custom type protocolVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ProtocolVlanId_Type.__name__ = "Integer32"
_ProtocolVlanId_Object = MibTableColumn
protocolVlanId = _ProtocolVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 2, 1, 1, 2),
    _ProtocolVlanId_Type()
)
protocolVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolVlanId.setStatus("current")
_ProtocolPortMember_Type = OctetString
_ProtocolPortMember_Object = MibTableColumn
protocolPortMember = _ProtocolPortMember_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 2, 1, 1, 3),
    _ProtocolPortMember_Type()
)
protocolPortMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolPortMember.setStatus("current")
_ProtocolVlanStatus_Type = TPRowStatus
_ProtocolVlanStatus_Object = MibTableColumn
protocolVlanStatus = _ProtocolVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 1, 2, 1, 1, 4),
    _ProtocolVlanStatus_Type()
)
protocolVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolVlanStatus.setStatus("current")
_TplinkProtocolVlanNotifications_ObjectIdentity = ObjectIdentity
tplinkProtocolVlanNotifications = _TplinkProtocolVlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 16, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PROTOCOL-VLAN-MIB",
    **{"tplinkProtocolVlanMIB": tplinkProtocolVlanMIB,
       "tplinkProtocolVlanMIBObjects": tplinkProtocolVlanMIBObjects,
       "protocolTemplate": protocolTemplate,
       "protocolTemplateTable": protocolTemplateTable,
       "templateEntry": templateEntry,
       "templateProtocolName": templateProtocolName,
       "templateEtherType": templateEtherType,
       "templateFrameType": templateFrameType,
       "templateStatus": templateStatus,
       "protocolGroup": protocolGroup,
       "protocolGroupTable": protocolGroupTable,
       "protocolVlanEntry": protocolVlanEntry,
       "protocolName": protocolName,
       "protocolVlanId": protocolVlanId,
       "protocolPortMember": protocolPortMember,
       "protocolVlanStatus": protocolVlanStatus,
       "tplinkProtocolVlanNotifications": tplinkProtocolVlanNotifications}
)
