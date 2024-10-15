# SNMP MIB module (A3COM-HUAWEI-VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-VOICE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:27 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cVoiceVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9)
)
h3cVoiceVlan.setRevisions(
        ("2009-05-15 00:00",
         "2002-07-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_H3cvoiceVlanOuiTable_Object = MibTable
h3cvoiceVlanOuiTable = _H3cvoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 1)
)
if mibBuilder.loadTexts:
    h3cvoiceVlanOuiTable.setStatus("current")
_H3cvoiceVlanOuiEntry_Object = MibTableRow
h3cvoiceVlanOuiEntry = _H3cvoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 1, 1)
)
h3cvoiceVlanOuiEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOICE-VLAN-MIB", "h3cVoiceVlanOuiAddress"),
)
if mibBuilder.loadTexts:
    h3cvoiceVlanOuiEntry.setStatus("current")
_H3cVoiceVlanOuiAddress_Type = MacAddress
_H3cVoiceVlanOuiAddress_Object = MibTableColumn
h3cVoiceVlanOuiAddress = _H3cVoiceVlanOuiAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 1, 1, 1),
    _H3cVoiceVlanOuiAddress_Type()
)
h3cVoiceVlanOuiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVoiceVlanOuiAddress.setStatus("current")
_H3cVoiceVlanOuiMask_Type = MacAddress
_H3cVoiceVlanOuiMask_Object = MibTableColumn
h3cVoiceVlanOuiMask = _H3cVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 1, 1, 2),
    _H3cVoiceVlanOuiMask_Type()
)
h3cVoiceVlanOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanOuiMask.setStatus("current")


class _H3cVoiceVlanOuiDescription_Type(OctetString):
    """Custom type h3cVoiceVlanOuiDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_H3cVoiceVlanOuiDescription_Type.__name__ = "OctetString"
_H3cVoiceVlanOuiDescription_Object = MibTableColumn
h3cVoiceVlanOuiDescription = _H3cVoiceVlanOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 1, 1, 3),
    _H3cVoiceVlanOuiDescription_Type()
)
h3cVoiceVlanOuiDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanOuiDescription.setStatus("current")
_H3cVoiceVlanOuiRowStatus_Type = RowStatus
_H3cVoiceVlanOuiRowStatus_Object = MibTableColumn
h3cVoiceVlanOuiRowStatus = _H3cVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 1, 1, 4),
    _H3cVoiceVlanOuiRowStatus_Type()
)
h3cVoiceVlanOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoiceVlanOuiRowStatus.setStatus("current")
_H3cVoiceVlanEnabledId_Type = Integer32
_H3cVoiceVlanEnabledId_Object = MibScalar
h3cVoiceVlanEnabledId = _H3cVoiceVlanEnabledId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 2),
    _H3cVoiceVlanEnabledId_Type()
)
h3cVoiceVlanEnabledId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanEnabledId.setStatus("current")
_H3cVoiceVlanPortEnableList_Type = PortList
_H3cVoiceVlanPortEnableList_Object = MibScalar
h3cVoiceVlanPortEnableList = _H3cVoiceVlanPortEnableList_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 3),
    _H3cVoiceVlanPortEnableList_Type()
)
h3cVoiceVlanPortEnableList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanPortEnableList.setStatus("current")


class _H3cVoiceVlanAgingTime_Type(Integer32):
    """Custom type h3cVoiceVlanAgingTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 43200),
    )


_H3cVoiceVlanAgingTime_Type.__name__ = "Integer32"
_H3cVoiceVlanAgingTime_Object = MibScalar
h3cVoiceVlanAgingTime = _H3cVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 4),
    _H3cVoiceVlanAgingTime_Type()
)
h3cVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanAgingTime.setStatus("current")


class _H3cVoiceVlanConfigState_Type(Integer32):
    """Custom type h3cVoiceVlanConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_H3cVoiceVlanConfigState_Type.__name__ = "Integer32"
_H3cVoiceVlanConfigState_Object = MibScalar
h3cVoiceVlanConfigState = _H3cVoiceVlanConfigState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 5),
    _H3cVoiceVlanConfigState_Type()
)
h3cVoiceVlanConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanConfigState.setStatus("current")


class _H3cVoiceVlanSecurityState_Type(Integer32):
    """Custom type h3cVoiceVlanSecurityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("security", 1))
    )


_H3cVoiceVlanSecurityState_Type.__name__ = "Integer32"
_H3cVoiceVlanSecurityState_Object = MibScalar
h3cVoiceVlanSecurityState = _H3cVoiceVlanSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 6),
    _H3cVoiceVlanSecurityState_Type()
)
h3cVoiceVlanSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanSecurityState.setStatus("current")
_H3cvoiceVlanPortTable_Object = MibTable
h3cvoiceVlanPortTable = _H3cvoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 7)
)
if mibBuilder.loadTexts:
    h3cvoiceVlanPortTable.setStatus("current")
_H3cvoiceVlanPortEntry_Object = MibTableRow
h3cvoiceVlanPortEntry = _H3cvoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 7, 1)
)
h3cvoiceVlanPortEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VOICE-VLAN-MIB", "h3cVoiceVlanPortifIndex"),
)
if mibBuilder.loadTexts:
    h3cvoiceVlanPortEntry.setStatus("current")


class _H3cVoiceVlanPortifIndex_Type(Integer32):
    """Custom type h3cVoiceVlanPortifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoiceVlanPortifIndex_Type.__name__ = "Integer32"
_H3cVoiceVlanPortifIndex_Object = MibTableColumn
h3cVoiceVlanPortifIndex = _H3cVoiceVlanPortifIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 7, 1, 1),
    _H3cVoiceVlanPortifIndex_Type()
)
h3cVoiceVlanPortifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoiceVlanPortifIndex.setStatus("current")


class _H3cVoiceVlanPortMode_Type(Integer32):
    """Custom type h3cVoiceVlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_H3cVoiceVlanPortMode_Type.__name__ = "Integer32"
_H3cVoiceVlanPortMode_Object = MibTableColumn
h3cVoiceVlanPortMode = _H3cVoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 7, 1, 2),
    _H3cVoiceVlanPortMode_Type()
)
h3cVoiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanPortMode.setStatus("current")
_H3cVoiceVlanPortLegacy_Type = TruthValue
_H3cVoiceVlanPortLegacy_Object = MibTableColumn
h3cVoiceVlanPortLegacy = _H3cVoiceVlanPortLegacy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 7, 1, 3),
    _H3cVoiceVlanPortLegacy_Type()
)
h3cVoiceVlanPortLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanPortLegacy.setStatus("current")
_H3cVoiceVlanPortQosTrust_Type = TruthValue
_H3cVoiceVlanPortQosTrust_Object = MibTableColumn
h3cVoiceVlanPortQosTrust = _H3cVoiceVlanPortQosTrust_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 9, 7, 1, 4),
    _H3cVoiceVlanPortQosTrust_Type()
)
h3cVoiceVlanPortQosTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceVlanPortQosTrust.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VOICE-VLAN-MIB",
    **{"PortList": PortList,
       "h3cVoiceVlan": h3cVoiceVlan,
       "h3cvoiceVlanOuiTable": h3cvoiceVlanOuiTable,
       "h3cvoiceVlanOuiEntry": h3cvoiceVlanOuiEntry,
       "h3cVoiceVlanOuiAddress": h3cVoiceVlanOuiAddress,
       "h3cVoiceVlanOuiMask": h3cVoiceVlanOuiMask,
       "h3cVoiceVlanOuiDescription": h3cVoiceVlanOuiDescription,
       "h3cVoiceVlanOuiRowStatus": h3cVoiceVlanOuiRowStatus,
       "h3cVoiceVlanEnabledId": h3cVoiceVlanEnabledId,
       "h3cVoiceVlanPortEnableList": h3cVoiceVlanPortEnableList,
       "h3cVoiceVlanAgingTime": h3cVoiceVlanAgingTime,
       "h3cVoiceVlanConfigState": h3cVoiceVlanConfigState,
       "h3cVoiceVlanSecurityState": h3cVoiceVlanSecurityState,
       "h3cvoiceVlanPortTable": h3cvoiceVlanPortTable,
       "h3cvoiceVlanPortEntry": h3cvoiceVlanPortEntry,
       "h3cVoiceVlanPortifIndex": h3cVoiceVlanPortifIndex,
       "h3cVoiceVlanPortMode": h3cVoiceVlanPortMode,
       "h3cVoiceVlanPortLegacy": h3cVoiceVlanPortLegacy,
       "h3cVoiceVlanPortQosTrust": h3cVoiceVlanPortQosTrust}
)
