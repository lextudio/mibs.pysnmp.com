# SNMP MIB module (HPN-ICF-FC-FLOGIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FC-FLOGIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:15 2024
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

(HpnicfFcAddressId,
 HpnicfFcBbCredit,
 HpnicfFcClassOfServices,
 HpnicfFcNameId,
 HpnicfFcRxMTU) = mibBuilder.importSymbols(
    "HPN-ICF-FC-TC-MIB",
    "HpnicfFcAddressId",
    "HpnicfFcBbCredit",
    "HpnicfFcClassOfServices",
    "HpnicfFcNameId",
    "HpnicfFcRxMTU")

(hpnicfSan,
 hpnicfVsanIndex) = mibBuilder.importSymbols(
    "HPN-ICF-VSAN-MIB",
    "hpnicfSan",
    "hpnicfVsanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfFcFLogin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3)
)
hpnicfFcFLogin.setRevisions(
        ("2013-02-27 11:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfFcFLoginMibObjects_ObjectIdentity = ObjectIdentity
hpnicfFcFLoginMibObjects = _HpnicfFcFLoginMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1)
)
_HpnicfFcFLoginTable_Object = MibTable
hpnicfFcFLoginTable = _HpnicfFcFLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcFLoginTable.setStatus("current")
_HpnicfFcFLoginEntry_Object = MibTableRow
hpnicfFcFLoginEntry = _HpnicfFcFLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1)
)
hpnicfFcFLoginEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"),
    (0, "HPN-ICF-FC-FLOGIN-MIB", "hpnicfFcFLoginIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcFLoginEntry.setStatus("current")
_HpnicfFcFLoginIndex_Type = HpnicfFcAddressId
_HpnicfFcFLoginIndex_Object = MibTableColumn
hpnicfFcFLoginIndex = _HpnicfFcFLoginIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 1),
    _HpnicfFcFLoginIndex_Type()
)
hpnicfFcFLoginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcFLoginIndex.setStatus("current")
_HpnicfFcFLoginPortNodeWWN_Type = HpnicfFcNameId
_HpnicfFcFLoginPortNodeWWN_Object = MibTableColumn
hpnicfFcFLoginPortNodeWWN = _HpnicfFcFLoginPortNodeWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 2),
    _HpnicfFcFLoginPortNodeWWN_Type()
)
hpnicfFcFLoginPortNodeWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginPortNodeWWN.setStatus("current")
_HpnicfFcFLoginPortWWN_Type = HpnicfFcNameId
_HpnicfFcFLoginPortWWN_Object = MibTableColumn
hpnicfFcFLoginPortWWN = _HpnicfFcFLoginPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 3),
    _HpnicfFcFLoginPortWWN_Type()
)
hpnicfFcFLoginPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginPortWWN.setStatus("current")
_HpnicfFcFLoginPortFcId_Type = HpnicfFcAddressId
_HpnicfFcFLoginPortFcId_Object = MibTableColumn
hpnicfFcFLoginPortFcId = _HpnicfFcFLoginPortFcId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 4),
    _HpnicfFcFLoginPortFcId_Type()
)
hpnicfFcFLoginPortFcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginPortFcId.setStatus("current")
_HpnicfFcFLoginRxBbCredit_Type = HpnicfFcBbCredit
_HpnicfFcFLoginRxBbCredit_Object = MibTableColumn
hpnicfFcFLoginRxBbCredit = _HpnicfFcFLoginRxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 5),
    _HpnicfFcFLoginRxBbCredit_Type()
)
hpnicfFcFLoginRxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginRxBbCredit.setStatus("current")
_HpnicfFcFLoginTxBbCredit_Type = HpnicfFcBbCredit
_HpnicfFcFLoginTxBbCredit_Object = MibTableColumn
hpnicfFcFLoginTxBbCredit = _HpnicfFcFLoginTxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 6),
    _HpnicfFcFLoginTxBbCredit_Type()
)
hpnicfFcFLoginTxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginTxBbCredit.setStatus("current")
_HpnicfFcFLoginClass2RxMTU_Type = HpnicfFcRxMTU
_HpnicfFcFLoginClass2RxMTU_Object = MibTableColumn
hpnicfFcFLoginClass2RxMTU = _HpnicfFcFLoginClass2RxMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 7),
    _HpnicfFcFLoginClass2RxMTU_Type()
)
hpnicfFcFLoginClass2RxMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginClass2RxMTU.setStatus("current")
_HpnicfFcFLoginClass3RxMTU_Type = HpnicfFcRxMTU
_HpnicfFcFLoginClass3RxMTU_Object = MibTableColumn
hpnicfFcFLoginClass3RxMTU = _HpnicfFcFLoginClass3RxMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 8),
    _HpnicfFcFLoginClass3RxMTU_Type()
)
hpnicfFcFLoginClass3RxMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginClass3RxMTU.setStatus("current")
_HpnicfFcFLoginSuppClassRequested_Type = HpnicfFcClassOfServices
_HpnicfFcFLoginSuppClassRequested_Object = MibTableColumn
hpnicfFcFLoginSuppClassRequested = _HpnicfFcFLoginSuppClassRequested_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 9),
    _HpnicfFcFLoginSuppClassRequested_Type()
)
hpnicfFcFLoginSuppClassRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginSuppClassRequested.setStatus("current")
_HpnicfFcFLoginClass2ReqAgreed_Type = TruthValue
_HpnicfFcFLoginClass2ReqAgreed_Object = MibTableColumn
hpnicfFcFLoginClass2ReqAgreed = _HpnicfFcFLoginClass2ReqAgreed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 10),
    _HpnicfFcFLoginClass2ReqAgreed_Type()
)
hpnicfFcFLoginClass2ReqAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginClass2ReqAgreed.setStatus("current")
_HpnicfFcFLoginClass3ReqAgreed_Type = TruthValue
_HpnicfFcFLoginClass3ReqAgreed_Object = MibTableColumn
hpnicfFcFLoginClass3ReqAgreed = _HpnicfFcFLoginClass3ReqAgreed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 3, 1, 1, 1, 11),
    _HpnicfFcFLoginClass3ReqAgreed_Type()
)
hpnicfFcFLoginClass3ReqAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcFLoginClass3ReqAgreed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FC-FLOGIN-MIB",
    **{"hpnicfFcFLogin": hpnicfFcFLogin,
       "hpnicfFcFLoginMibObjects": hpnicfFcFLoginMibObjects,
       "hpnicfFcFLoginTable": hpnicfFcFLoginTable,
       "hpnicfFcFLoginEntry": hpnicfFcFLoginEntry,
       "hpnicfFcFLoginIndex": hpnicfFcFLoginIndex,
       "hpnicfFcFLoginPortNodeWWN": hpnicfFcFLoginPortNodeWWN,
       "hpnicfFcFLoginPortWWN": hpnicfFcFLoginPortWWN,
       "hpnicfFcFLoginPortFcId": hpnicfFcFLoginPortFcId,
       "hpnicfFcFLoginRxBbCredit": hpnicfFcFLoginRxBbCredit,
       "hpnicfFcFLoginTxBbCredit": hpnicfFcFLoginTxBbCredit,
       "hpnicfFcFLoginClass2RxMTU": hpnicfFcFLoginClass2RxMTU,
       "hpnicfFcFLoginClass3RxMTU": hpnicfFcFLoginClass3RxMTU,
       "hpnicfFcFLoginSuppClassRequested": hpnicfFcFLoginSuppClassRequested,
       "hpnicfFcFLoginClass2ReqAgreed": hpnicfFcFLoginClass2ReqAgreed,
       "hpnicfFcFLoginClass3ReqAgreed": hpnicfFcFLoginClass3ReqAgreed}
)
