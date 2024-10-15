# SNMP MIB module (HH3C-VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VOICE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:19 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cVoiceVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9)
)
hh3cVoiceVlan.setRevisions(
        ("2009-05-15 00:00",
         "2002-07-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Hh3cvoiceVlanOuiTable_Object = MibTable
hh3cvoiceVlanOuiTable = _Hh3cvoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 1)
)
if mibBuilder.loadTexts:
    hh3cvoiceVlanOuiTable.setStatus("current")
_Hh3cvoiceVlanOuiEntry_Object = MibTableRow
hh3cvoiceVlanOuiEntry = _Hh3cvoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 1, 1)
)
hh3cvoiceVlanOuiEntry.setIndexNames(
    (0, "HH3C-VOICE-VLAN-MIB", "hh3cVoiceVlanOuiAddress"),
)
if mibBuilder.loadTexts:
    hh3cvoiceVlanOuiEntry.setStatus("current")
_Hh3cVoiceVlanOuiAddress_Type = MacAddress
_Hh3cVoiceVlanOuiAddress_Object = MibTableColumn
hh3cVoiceVlanOuiAddress = _Hh3cVoiceVlanOuiAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 1, 1, 1),
    _Hh3cVoiceVlanOuiAddress_Type()
)
hh3cVoiceVlanOuiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVoiceVlanOuiAddress.setStatus("current")
_Hh3cVoiceVlanOuiMask_Type = MacAddress
_Hh3cVoiceVlanOuiMask_Object = MibTableColumn
hh3cVoiceVlanOuiMask = _Hh3cVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 1, 1, 2),
    _Hh3cVoiceVlanOuiMask_Type()
)
hh3cVoiceVlanOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanOuiMask.setStatus("current")


class _Hh3cVoiceVlanOuiDescription_Type(OctetString):
    """Custom type hh3cVoiceVlanOuiDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Hh3cVoiceVlanOuiDescription_Type.__name__ = "OctetString"
_Hh3cVoiceVlanOuiDescription_Object = MibTableColumn
hh3cVoiceVlanOuiDescription = _Hh3cVoiceVlanOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 1, 1, 3),
    _Hh3cVoiceVlanOuiDescription_Type()
)
hh3cVoiceVlanOuiDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanOuiDescription.setStatus("current")
_Hh3cVoiceVlanOuiRowStatus_Type = RowStatus
_Hh3cVoiceVlanOuiRowStatus_Object = MibTableColumn
hh3cVoiceVlanOuiRowStatus = _Hh3cVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 1, 1, 4),
    _Hh3cVoiceVlanOuiRowStatus_Type()
)
hh3cVoiceVlanOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVoiceVlanOuiRowStatus.setStatus("current")
_Hh3cVoiceVlanEnabledId_Type = Integer32
_Hh3cVoiceVlanEnabledId_Object = MibScalar
hh3cVoiceVlanEnabledId = _Hh3cVoiceVlanEnabledId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 2),
    _Hh3cVoiceVlanEnabledId_Type()
)
hh3cVoiceVlanEnabledId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanEnabledId.setStatus("current")
_Hh3cVoiceVlanPortEnableList_Type = PortList
_Hh3cVoiceVlanPortEnableList_Object = MibScalar
hh3cVoiceVlanPortEnableList = _Hh3cVoiceVlanPortEnableList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 3),
    _Hh3cVoiceVlanPortEnableList_Type()
)
hh3cVoiceVlanPortEnableList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanPortEnableList.setStatus("current")


class _Hh3cVoiceVlanAgingTime_Type(Integer32):
    """Custom type hh3cVoiceVlanAgingTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 43200),
    )


_Hh3cVoiceVlanAgingTime_Type.__name__ = "Integer32"
_Hh3cVoiceVlanAgingTime_Object = MibScalar
hh3cVoiceVlanAgingTime = _Hh3cVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 4),
    _Hh3cVoiceVlanAgingTime_Type()
)
hh3cVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanAgingTime.setStatus("current")


class _Hh3cVoiceVlanConfigState_Type(Integer32):
    """Custom type hh3cVoiceVlanConfigState based on Integer32"""
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


_Hh3cVoiceVlanConfigState_Type.__name__ = "Integer32"
_Hh3cVoiceVlanConfigState_Object = MibScalar
hh3cVoiceVlanConfigState = _Hh3cVoiceVlanConfigState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 5),
    _Hh3cVoiceVlanConfigState_Type()
)
hh3cVoiceVlanConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanConfigState.setStatus("current")


class _Hh3cVoiceVlanSecurityState_Type(Integer32):
    """Custom type hh3cVoiceVlanSecurityState based on Integer32"""
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


_Hh3cVoiceVlanSecurityState_Type.__name__ = "Integer32"
_Hh3cVoiceVlanSecurityState_Object = MibScalar
hh3cVoiceVlanSecurityState = _Hh3cVoiceVlanSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 6),
    _Hh3cVoiceVlanSecurityState_Type()
)
hh3cVoiceVlanSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanSecurityState.setStatus("current")
_Hh3cvoiceVlanPortTable_Object = MibTable
hh3cvoiceVlanPortTable = _Hh3cvoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 7)
)
if mibBuilder.loadTexts:
    hh3cvoiceVlanPortTable.setStatus("current")
_Hh3cvoiceVlanPortEntry_Object = MibTableRow
hh3cvoiceVlanPortEntry = _Hh3cvoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 7, 1)
)
hh3cvoiceVlanPortEntry.setIndexNames(
    (0, "HH3C-VOICE-VLAN-MIB", "hh3cVoiceVlanPortifIndex"),
)
if mibBuilder.loadTexts:
    hh3cvoiceVlanPortEntry.setStatus("current")


class _Hh3cVoiceVlanPortifIndex_Type(Integer32):
    """Custom type hh3cVoiceVlanPortifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVoiceVlanPortifIndex_Type.__name__ = "Integer32"
_Hh3cVoiceVlanPortifIndex_Object = MibTableColumn
hh3cVoiceVlanPortifIndex = _Hh3cVoiceVlanPortifIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 7, 1, 1),
    _Hh3cVoiceVlanPortifIndex_Type()
)
hh3cVoiceVlanPortifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVoiceVlanPortifIndex.setStatus("current")


class _Hh3cVoiceVlanPortMode_Type(Integer32):
    """Custom type hh3cVoiceVlanPortMode based on Integer32"""
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


_Hh3cVoiceVlanPortMode_Type.__name__ = "Integer32"
_Hh3cVoiceVlanPortMode_Object = MibTableColumn
hh3cVoiceVlanPortMode = _Hh3cVoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 7, 1, 2),
    _Hh3cVoiceVlanPortMode_Type()
)
hh3cVoiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanPortMode.setStatus("current")
_Hh3cVoiceVlanPortLegacy_Type = TruthValue
_Hh3cVoiceVlanPortLegacy_Object = MibTableColumn
hh3cVoiceVlanPortLegacy = _Hh3cVoiceVlanPortLegacy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 7, 1, 3),
    _Hh3cVoiceVlanPortLegacy_Type()
)
hh3cVoiceVlanPortLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanPortLegacy.setStatus("current")
_Hh3cVoiceVlanPortQosTrust_Type = TruthValue
_Hh3cVoiceVlanPortQosTrust_Object = MibTableColumn
hh3cVoiceVlanPortQosTrust = _Hh3cVoiceVlanPortQosTrust_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 9, 7, 1, 4),
    _Hh3cVoiceVlanPortQosTrust_Type()
)
hh3cVoiceVlanPortQosTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceVlanPortQosTrust.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VOICE-VLAN-MIB",
    **{"PortList": PortList,
       "hh3cVoiceVlan": hh3cVoiceVlan,
       "hh3cvoiceVlanOuiTable": hh3cvoiceVlanOuiTable,
       "hh3cvoiceVlanOuiEntry": hh3cvoiceVlanOuiEntry,
       "hh3cVoiceVlanOuiAddress": hh3cVoiceVlanOuiAddress,
       "hh3cVoiceVlanOuiMask": hh3cVoiceVlanOuiMask,
       "hh3cVoiceVlanOuiDescription": hh3cVoiceVlanOuiDescription,
       "hh3cVoiceVlanOuiRowStatus": hh3cVoiceVlanOuiRowStatus,
       "hh3cVoiceVlanEnabledId": hh3cVoiceVlanEnabledId,
       "hh3cVoiceVlanPortEnableList": hh3cVoiceVlanPortEnableList,
       "hh3cVoiceVlanAgingTime": hh3cVoiceVlanAgingTime,
       "hh3cVoiceVlanConfigState": hh3cVoiceVlanConfigState,
       "hh3cVoiceVlanSecurityState": hh3cVoiceVlanSecurityState,
       "hh3cvoiceVlanPortTable": hh3cvoiceVlanPortTable,
       "hh3cvoiceVlanPortEntry": hh3cvoiceVlanPortEntry,
       "hh3cVoiceVlanPortifIndex": hh3cVoiceVlanPortifIndex,
       "hh3cVoiceVlanPortMode": hh3cVoiceVlanPortMode,
       "hh3cVoiceVlanPortLegacy": hh3cVoiceVlanPortLegacy,
       "hh3cVoiceVlanPortQosTrust": hh3cVoiceVlanPortQosTrust}
)
