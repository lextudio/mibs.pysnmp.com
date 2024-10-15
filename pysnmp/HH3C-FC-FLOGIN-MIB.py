# SNMP MIB module (HH3C-FC-FLOGIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FC-FLOGIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:15 2024
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

(Hh3cFcAddressId,
 Hh3cFcBbCredit,
 Hh3cFcClassOfServices,
 Hh3cFcNameId,
 Hh3cFcRxMTU) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcAddressId",
    "Hh3cFcBbCredit",
    "Hh3cFcClassOfServices",
    "Hh3cFcNameId",
    "Hh3cFcRxMTU")

(hh3cSan,
 hh3cVsanIndex) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan",
    "hh3cVsanIndex")

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

hh3cFcFLogin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3)
)
hh3cFcFLogin.setRevisions(
        ("2013-02-27 11:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFcFLoginMibObjects_ObjectIdentity = ObjectIdentity
hh3cFcFLoginMibObjects = _Hh3cFcFLoginMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1)
)
_Hh3cFcFLoginTable_Object = MibTable
hh3cFcFLoginTable = _Hh3cFcFLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFcFLoginTable.setStatus("current")
_Hh3cFcFLoginEntry_Object = MibTableRow
hh3cFcFLoginEntry = _Hh3cFcFLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1)
)
hh3cFcFLoginEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "HH3C-FC-FLOGIN-MIB", "hh3cFcFLoginIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcFLoginEntry.setStatus("current")
_Hh3cFcFLoginIndex_Type = Hh3cFcAddressId
_Hh3cFcFLoginIndex_Object = MibTableColumn
hh3cFcFLoginIndex = _Hh3cFcFLoginIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 1),
    _Hh3cFcFLoginIndex_Type()
)
hh3cFcFLoginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcFLoginIndex.setStatus("current")
_Hh3cFcFLoginPortNodeWWN_Type = Hh3cFcNameId
_Hh3cFcFLoginPortNodeWWN_Object = MibTableColumn
hh3cFcFLoginPortNodeWWN = _Hh3cFcFLoginPortNodeWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 2),
    _Hh3cFcFLoginPortNodeWWN_Type()
)
hh3cFcFLoginPortNodeWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginPortNodeWWN.setStatus("current")
_Hh3cFcFLoginPortWWN_Type = Hh3cFcNameId
_Hh3cFcFLoginPortWWN_Object = MibTableColumn
hh3cFcFLoginPortWWN = _Hh3cFcFLoginPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 3),
    _Hh3cFcFLoginPortWWN_Type()
)
hh3cFcFLoginPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginPortWWN.setStatus("current")
_Hh3cFcFLoginPortFcId_Type = Hh3cFcAddressId
_Hh3cFcFLoginPortFcId_Object = MibTableColumn
hh3cFcFLoginPortFcId = _Hh3cFcFLoginPortFcId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 4),
    _Hh3cFcFLoginPortFcId_Type()
)
hh3cFcFLoginPortFcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginPortFcId.setStatus("current")
_Hh3cFcFLoginRxBbCredit_Type = Hh3cFcBbCredit
_Hh3cFcFLoginRxBbCredit_Object = MibTableColumn
hh3cFcFLoginRxBbCredit = _Hh3cFcFLoginRxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 5),
    _Hh3cFcFLoginRxBbCredit_Type()
)
hh3cFcFLoginRxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginRxBbCredit.setStatus("current")
_Hh3cFcFLoginTxBbCredit_Type = Hh3cFcBbCredit
_Hh3cFcFLoginTxBbCredit_Object = MibTableColumn
hh3cFcFLoginTxBbCredit = _Hh3cFcFLoginTxBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 6),
    _Hh3cFcFLoginTxBbCredit_Type()
)
hh3cFcFLoginTxBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginTxBbCredit.setStatus("current")
_Hh3cFcFLoginClass2RxMTU_Type = Hh3cFcRxMTU
_Hh3cFcFLoginClass2RxMTU_Object = MibTableColumn
hh3cFcFLoginClass2RxMTU = _Hh3cFcFLoginClass2RxMTU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 7),
    _Hh3cFcFLoginClass2RxMTU_Type()
)
hh3cFcFLoginClass2RxMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginClass2RxMTU.setStatus("current")
_Hh3cFcFLoginClass3RxMTU_Type = Hh3cFcRxMTU
_Hh3cFcFLoginClass3RxMTU_Object = MibTableColumn
hh3cFcFLoginClass3RxMTU = _Hh3cFcFLoginClass3RxMTU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 8),
    _Hh3cFcFLoginClass3RxMTU_Type()
)
hh3cFcFLoginClass3RxMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginClass3RxMTU.setStatus("current")
_Hh3cFcFLoginSuppClassRequested_Type = Hh3cFcClassOfServices
_Hh3cFcFLoginSuppClassRequested_Object = MibTableColumn
hh3cFcFLoginSuppClassRequested = _Hh3cFcFLoginSuppClassRequested_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 9),
    _Hh3cFcFLoginSuppClassRequested_Type()
)
hh3cFcFLoginSuppClassRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginSuppClassRequested.setStatus("current")
_Hh3cFcFLoginClass2ReqAgreed_Type = TruthValue
_Hh3cFcFLoginClass2ReqAgreed_Object = MibTableColumn
hh3cFcFLoginClass2ReqAgreed = _Hh3cFcFLoginClass2ReqAgreed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 10),
    _Hh3cFcFLoginClass2ReqAgreed_Type()
)
hh3cFcFLoginClass2ReqAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginClass2ReqAgreed.setStatus("current")
_Hh3cFcFLoginClass3ReqAgreed_Type = TruthValue
_Hh3cFcFLoginClass3ReqAgreed_Object = MibTableColumn
hh3cFcFLoginClass3ReqAgreed = _Hh3cFcFLoginClass3ReqAgreed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 3, 1, 1, 1, 11),
    _Hh3cFcFLoginClass3ReqAgreed_Type()
)
hh3cFcFLoginClass3ReqAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcFLoginClass3ReqAgreed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FC-FLOGIN-MIB",
    **{"hh3cFcFLogin": hh3cFcFLogin,
       "hh3cFcFLoginMibObjects": hh3cFcFLoginMibObjects,
       "hh3cFcFLoginTable": hh3cFcFLoginTable,
       "hh3cFcFLoginEntry": hh3cFcFLoginEntry,
       "hh3cFcFLoginIndex": hh3cFcFLoginIndex,
       "hh3cFcFLoginPortNodeWWN": hh3cFcFLoginPortNodeWWN,
       "hh3cFcFLoginPortWWN": hh3cFcFLoginPortWWN,
       "hh3cFcFLoginPortFcId": hh3cFcFLoginPortFcId,
       "hh3cFcFLoginRxBbCredit": hh3cFcFLoginRxBbCredit,
       "hh3cFcFLoginTxBbCredit": hh3cFcFLoginTxBbCredit,
       "hh3cFcFLoginClass2RxMTU": hh3cFcFLoginClass2RxMTU,
       "hh3cFcFLoginClass3RxMTU": hh3cFcFLoginClass3RxMTU,
       "hh3cFcFLoginSuppClassRequested": hh3cFcFLoginSuppClassRequested,
       "hh3cFcFLoginClass2ReqAgreed": hh3cFcFLoginClass2ReqAgreed,
       "hh3cFcFLoginClass3ReqAgreed": hh3cFcFLoginClass3ReqAgreed}
)
