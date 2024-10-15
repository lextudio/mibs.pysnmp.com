# SNMP MIB module (HPN-ICF-VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-VOICE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:12 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfVoiceVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9)
)
hpnicfVoiceVlan.setRevisions(
        ("2009-05-15 00:00",
         "2002-07-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HpnicfvoiceVlanOuiTable_Object = MibTable
hpnicfvoiceVlanOuiTable = _HpnicfvoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 1)
)
if mibBuilder.loadTexts:
    hpnicfvoiceVlanOuiTable.setStatus("current")
_HpnicfvoiceVlanOuiEntry_Object = MibTableRow
hpnicfvoiceVlanOuiEntry = _HpnicfvoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 1, 1)
)
hpnicfvoiceVlanOuiEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-VLAN-MIB", "hpnicfVoiceVlanOuiAddress"),
)
if mibBuilder.loadTexts:
    hpnicfvoiceVlanOuiEntry.setStatus("current")
_HpnicfVoiceVlanOuiAddress_Type = MacAddress
_HpnicfVoiceVlanOuiAddress_Object = MibTableColumn
hpnicfVoiceVlanOuiAddress = _HpnicfVoiceVlanOuiAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 1, 1, 1),
    _HpnicfVoiceVlanOuiAddress_Type()
)
hpnicfVoiceVlanOuiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanOuiAddress.setStatus("current")
_HpnicfVoiceVlanOuiMask_Type = MacAddress
_HpnicfVoiceVlanOuiMask_Object = MibTableColumn
hpnicfVoiceVlanOuiMask = _HpnicfVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 1, 1, 2),
    _HpnicfVoiceVlanOuiMask_Type()
)
hpnicfVoiceVlanOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanOuiMask.setStatus("current")


class _HpnicfVoiceVlanOuiDescription_Type(OctetString):
    """Custom type hpnicfVoiceVlanOuiDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HpnicfVoiceVlanOuiDescription_Type.__name__ = "OctetString"
_HpnicfVoiceVlanOuiDescription_Object = MibTableColumn
hpnicfVoiceVlanOuiDescription = _HpnicfVoiceVlanOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 1, 1, 3),
    _HpnicfVoiceVlanOuiDescription_Type()
)
hpnicfVoiceVlanOuiDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanOuiDescription.setStatus("current")
_HpnicfVoiceVlanOuiRowStatus_Type = RowStatus
_HpnicfVoiceVlanOuiRowStatus_Object = MibTableColumn
hpnicfVoiceVlanOuiRowStatus = _HpnicfVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 1, 1, 4),
    _HpnicfVoiceVlanOuiRowStatus_Type()
)
hpnicfVoiceVlanOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanOuiRowStatus.setStatus("current")
_HpnicfVoiceVlanEnabledId_Type = Integer32
_HpnicfVoiceVlanEnabledId_Object = MibScalar
hpnicfVoiceVlanEnabledId = _HpnicfVoiceVlanEnabledId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 2),
    _HpnicfVoiceVlanEnabledId_Type()
)
hpnicfVoiceVlanEnabledId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanEnabledId.setStatus("current")
_HpnicfVoiceVlanPortEnableList_Type = PortList
_HpnicfVoiceVlanPortEnableList_Object = MibScalar
hpnicfVoiceVlanPortEnableList = _HpnicfVoiceVlanPortEnableList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 3),
    _HpnicfVoiceVlanPortEnableList_Type()
)
hpnicfVoiceVlanPortEnableList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanPortEnableList.setStatus("current")


class _HpnicfVoiceVlanAgingTime_Type(Integer32):
    """Custom type hpnicfVoiceVlanAgingTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 43200),
    )


_HpnicfVoiceVlanAgingTime_Type.__name__ = "Integer32"
_HpnicfVoiceVlanAgingTime_Object = MibScalar
hpnicfVoiceVlanAgingTime = _HpnicfVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 4),
    _HpnicfVoiceVlanAgingTime_Type()
)
hpnicfVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanAgingTime.setStatus("current")


class _HpnicfVoiceVlanConfigState_Type(Integer32):
    """Custom type hpnicfVoiceVlanConfigState based on Integer32"""
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


_HpnicfVoiceVlanConfigState_Type.__name__ = "Integer32"
_HpnicfVoiceVlanConfigState_Object = MibScalar
hpnicfVoiceVlanConfigState = _HpnicfVoiceVlanConfigState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 5),
    _HpnicfVoiceVlanConfigState_Type()
)
hpnicfVoiceVlanConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanConfigState.setStatus("current")


class _HpnicfVoiceVlanSecurityState_Type(Integer32):
    """Custom type hpnicfVoiceVlanSecurityState based on Integer32"""
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


_HpnicfVoiceVlanSecurityState_Type.__name__ = "Integer32"
_HpnicfVoiceVlanSecurityState_Object = MibScalar
hpnicfVoiceVlanSecurityState = _HpnicfVoiceVlanSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 6),
    _HpnicfVoiceVlanSecurityState_Type()
)
hpnicfVoiceVlanSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanSecurityState.setStatus("current")
_HpnicfvoiceVlanPortTable_Object = MibTable
hpnicfvoiceVlanPortTable = _HpnicfvoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 7)
)
if mibBuilder.loadTexts:
    hpnicfvoiceVlanPortTable.setStatus("current")
_HpnicfvoiceVlanPortEntry_Object = MibTableRow
hpnicfvoiceVlanPortEntry = _HpnicfvoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 7, 1)
)
hpnicfvoiceVlanPortEntry.setIndexNames(
    (0, "HPN-ICF-VOICE-VLAN-MIB", "hpnicfVoiceVlanPortifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfvoiceVlanPortEntry.setStatus("current")


class _HpnicfVoiceVlanPortifIndex_Type(Integer32):
    """Custom type hpnicfVoiceVlanPortifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfVoiceVlanPortifIndex_Type.__name__ = "Integer32"
_HpnicfVoiceVlanPortifIndex_Object = MibTableColumn
hpnicfVoiceVlanPortifIndex = _HpnicfVoiceVlanPortifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 7, 1, 1),
    _HpnicfVoiceVlanPortifIndex_Type()
)
hpnicfVoiceVlanPortifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanPortifIndex.setStatus("current")


class _HpnicfVoiceVlanPortMode_Type(Integer32):
    """Custom type hpnicfVoiceVlanPortMode based on Integer32"""
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


_HpnicfVoiceVlanPortMode_Type.__name__ = "Integer32"
_HpnicfVoiceVlanPortMode_Object = MibTableColumn
hpnicfVoiceVlanPortMode = _HpnicfVoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 7, 1, 2),
    _HpnicfVoiceVlanPortMode_Type()
)
hpnicfVoiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanPortMode.setStatus("current")
_HpnicfVoiceVlanPortLegacy_Type = TruthValue
_HpnicfVoiceVlanPortLegacy_Object = MibTableColumn
hpnicfVoiceVlanPortLegacy = _HpnicfVoiceVlanPortLegacy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 7, 1, 3),
    _HpnicfVoiceVlanPortLegacy_Type()
)
hpnicfVoiceVlanPortLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanPortLegacy.setStatus("current")
_HpnicfVoiceVlanPortQosTrust_Type = TruthValue
_HpnicfVoiceVlanPortQosTrust_Object = MibTableColumn
hpnicfVoiceVlanPortQosTrust = _HpnicfVoiceVlanPortQosTrust_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 9, 7, 1, 4),
    _HpnicfVoiceVlanPortQosTrust_Type()
)
hpnicfVoiceVlanPortQosTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceVlanPortQosTrust.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VOICE-VLAN-MIB",
    **{"PortList": PortList,
       "hpnicfVoiceVlan": hpnicfVoiceVlan,
       "hpnicfvoiceVlanOuiTable": hpnicfvoiceVlanOuiTable,
       "hpnicfvoiceVlanOuiEntry": hpnicfvoiceVlanOuiEntry,
       "hpnicfVoiceVlanOuiAddress": hpnicfVoiceVlanOuiAddress,
       "hpnicfVoiceVlanOuiMask": hpnicfVoiceVlanOuiMask,
       "hpnicfVoiceVlanOuiDescription": hpnicfVoiceVlanOuiDescription,
       "hpnicfVoiceVlanOuiRowStatus": hpnicfVoiceVlanOuiRowStatus,
       "hpnicfVoiceVlanEnabledId": hpnicfVoiceVlanEnabledId,
       "hpnicfVoiceVlanPortEnableList": hpnicfVoiceVlanPortEnableList,
       "hpnicfVoiceVlanAgingTime": hpnicfVoiceVlanAgingTime,
       "hpnicfVoiceVlanConfigState": hpnicfVoiceVlanConfigState,
       "hpnicfVoiceVlanSecurityState": hpnicfVoiceVlanSecurityState,
       "hpnicfvoiceVlanPortTable": hpnicfvoiceVlanPortTable,
       "hpnicfvoiceVlanPortEntry": hpnicfvoiceVlanPortEntry,
       "hpnicfVoiceVlanPortifIndex": hpnicfVoiceVlanPortifIndex,
       "hpnicfVoiceVlanPortMode": hpnicfVoiceVlanPortMode,
       "hpnicfVoiceVlanPortLegacy": hpnicfVoiceVlanPortLegacy,
       "hpnicfVoiceVlanPortQosTrust": hpnicfVoiceVlanPortQosTrust}
)
