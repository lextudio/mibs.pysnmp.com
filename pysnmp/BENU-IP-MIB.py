# SNMP MIB module (BENU-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:55 2024
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

(benuPlatform,) = mibBuilder.importSymbols(
    "BENU-PLATFORM-MIB",
    "benuPlatform")

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


# MODULE-IDENTITY

bIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6)
)
bIPMIB.setRevisions(
        ("2014-12-17 00:00",
         "2013-11-28 00:00",
         "2013-05-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BIPNotifObjects_ObjectIdentity = ObjectIdentity
bIPNotifObjects = _BIPNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 0)
)
if mibBuilder.loadTexts:
    bIPNotifObjects.setStatus("current")
_BIPMIBObjects_ObjectIdentity = ObjectIdentity
bIPMIBObjects = _BIPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1)
)
if mibBuilder.loadTexts:
    bIPMIBObjects.setStatus("current")
_BIPPortTable_Object = MibTable
bIPPortTable = _BIPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    bIPPortTable.setStatus("current")
_BIPPortEntry_Object = MibTableRow
bIPPortEntry = _BIPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1)
)
bIPPortEntry.setIndexNames(
    (0, "BENU-IP-MIB", "bIPPortIndex"),
)
if mibBuilder.loadTexts:
    bIPPortEntry.setStatus("current")
_BIPPortIndex_Type = Unsigned32
_BIPPortIndex_Object = MibTableColumn
bIPPortIndex = _BIPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 1),
    _BIPPortIndex_Type()
)
bIPPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bIPPortIndex.setStatus("current")
_BIPPortInterfaceName_Type = DisplayString
_BIPPortInterfaceName_Object = MibTableColumn
bIPPortInterfaceName = _BIPPortInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 2),
    _BIPPortInterfaceName_Type()
)
bIPPortInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortInterfaceName.setStatus("current")
_BIPPortTxBytesInFrameWoErr_Type = Counter64
_BIPPortTxBytesInFrameWoErr_Object = MibTableColumn
bIPPortTxBytesInFrameWoErr = _BIPPortTxBytesInFrameWoErr_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 3),
    _BIPPortTxBytesInFrameWoErr_Type()
)
bIPPortTxBytesInFrameWoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTxBytesInFrameWoErr.setStatus("current")
_BIPPortTxFramesWoErrExclPausFrame_Type = Counter64
_BIPPortTxFramesWoErrExclPausFrame_Object = MibTableColumn
bIPPortTxFramesWoErrExclPausFrame = _BIPPortTxFramesWoErrExclPausFrame_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 4),
    _BIPPortTxFramesWoErrExclPausFrame_Type()
)
bIPPortTxFramesWoErrExclPausFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTxFramesWoErrExclPausFrame.setStatus("deprecated")
_BIPPortTxBcastFrames_Type = Counter64
_BIPPortTxBcastFrames_Object = MibTableColumn
bIPPortTxBcastFrames = _BIPPortTxBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 5),
    _BIPPortTxBcastFrames_Type()
)
bIPPortTxBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTxBcastFrames.setStatus("current")
_BIPPortTxL2McastFrames_Type = Counter64
_BIPPortTxL2McastFrames_Object = MibTableColumn
bIPPortTxL2McastFrames = _BIPPortTxL2McastFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 6),
    _BIPPortTxL2McastFrames_Type()
)
bIPPortTxL2McastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTxL2McastFrames.setStatus("current")
_BIPPortTxPausFrame_Type = Counter64
_BIPPortTxPausFrame_Object = MibTableColumn
bIPPortTxPausFrame = _BIPPortTxPausFrame_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 7),
    _BIPPortTxPausFrame_Type()
)
bIPPortTxPausFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTxPausFrame.setStatus("current")
_BIPPortTx64byteFrames_Type = Counter64
_BIPPortTx64byteFrames_Object = MibTableColumn
bIPPortTx64byteFrames = _BIPPortTx64byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 8),
    _BIPPortTx64byteFrames_Type()
)
bIPPortTx64byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTx64byteFrames.setStatus("current")
_BIPPortTx65to127byteFrames_Type = Counter64
_BIPPortTx65to127byteFrames_Object = MibTableColumn
bIPPortTx65to127byteFrames = _BIPPortTx65to127byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 9),
    _BIPPortTx65to127byteFrames_Type()
)
bIPPortTx65to127byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTx65to127byteFrames.setStatus("current")
_BIPPortTx128to255byteFrames_Type = Counter64
_BIPPortTx128to255byteFrames_Object = MibTableColumn
bIPPortTx128to255byteFrames = _BIPPortTx128to255byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 10),
    _BIPPortTx128to255byteFrames_Type()
)
bIPPortTx128to255byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTx128to255byteFrames.setStatus("current")
_BIPPortTx256to511byteFrames_Type = Counter64
_BIPPortTx256to511byteFrames_Object = MibTableColumn
bIPPortTx256to511byteFrames = _BIPPortTx256to511byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 11),
    _BIPPortTx256to511byteFrames_Type()
)
bIPPortTx256to511byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTx256to511byteFrames.setStatus("current")
_BIPPortTx512to1023byteFrames_Type = Counter64
_BIPPortTx512to1023byteFrames_Object = MibTableColumn
bIPPortTx512to1023byteFrames = _BIPPortTx512to1023byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 12),
    _BIPPortTx512to1023byteFrames_Type()
)
bIPPortTx512to1023byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTx512to1023byteFrames.setStatus("current")
_BIPPortTx1024to1518byteFrames_Type = Counter64
_BIPPortTx1024to1518byteFrames_Object = MibTableColumn
bIPPortTx1024to1518byteFrames = _BIPPortTx1024to1518byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 13),
    _BIPPortTx1024to1518byteFrames_Type()
)
bIPPortTx1024to1518byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTx1024to1518byteFrames.setStatus("current")
_BIPPortTx1519to1522byteFrames_Type = Counter64
_BIPPortTx1519to1522byteFrames_Object = MibTableColumn
bIPPortTx1519to1522byteFrames = _BIPPortTx1519to1522byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 14),
    _BIPPortTx1519to1522byteFrames_Type()
)
bIPPortTx1519to1522byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTx1519to1522byteFrames.setStatus("current")
_BIPPortTx1523toMaxByteFrames_Type = Counter64
_BIPPortTx1523toMaxByteFrames_Object = MibTableColumn
bIPPortTx1523toMaxByteFrames = _BIPPortTx1523toMaxByteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 15),
    _BIPPortTx1523toMaxByteFrames_Type()
)
bIPPortTx1523toMaxByteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTx1523toMaxByteFrames.setStatus("current")
_BIPPortTx17to63byteFrames_Type = Counter64
_BIPPortTx17to63byteFrames_Object = MibTableColumn
bIPPortTx17to63byteFrames = _BIPPortTx17to63byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 16),
    _BIPPortTx17to63byteFrames_Type()
)
bIPPortTx17to63byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTx17to63byteFrames.setStatus("current")
_BIPPortTxBadFcsFrames_Type = Counter64
_BIPPortTxBadFcsFrames_Object = MibTableColumn
bIPPortTxBadFcsFrames = _BIPPortTxBadFcsFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 17),
    _BIPPortTxBadFcsFrames_Type()
)
bIPPortTxBadFcsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortTxBadFcsFrames.setStatus("current")
_BIPPortRxBytesInFrameWoErr_Type = Counter64
_BIPPortRxBytesInFrameWoErr_Object = MibTableColumn
bIPPortRxBytesInFrameWoErr = _BIPPortRxBytesInFrameWoErr_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 18),
    _BIPPortRxBytesInFrameWoErr_Type()
)
bIPPortRxBytesInFrameWoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxBytesInFrameWoErr.setStatus("current")
_BIPPortRxBcastFrames_Type = Counter64
_BIPPortRxBcastFrames_Object = MibTableColumn
bIPPortRxBcastFrames = _BIPPortRxBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 19),
    _BIPPortRxBcastFrames_Type()
)
bIPPortRxBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxBcastFrames.setStatus("current")
_BIPPortRxL2McastFrames_Type = Counter64
_BIPPortRxL2McastFrames_Object = MibTableColumn
bIPPortRxL2McastFrames = _BIPPortRxL2McastFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 20),
    _BIPPortRxL2McastFrames_Type()
)
bIPPortRxL2McastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxL2McastFrames.setStatus("current")
_BIPPortRxPausFrames_Type = Counter64
_BIPPortRxPausFrames_Object = MibTableColumn
bIPPortRxPausFrames = _BIPPortRxPausFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 21),
    _BIPPortRxPausFrames_Type()
)
bIPPortRxPausFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxPausFrames.setStatus("current")
_BIPPortRx64byteFrames_Type = Counter64
_BIPPortRx64byteFrames_Object = MibTableColumn
bIPPortRx64byteFrames = _BIPPortRx64byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 22),
    _BIPPortRx64byteFrames_Type()
)
bIPPortRx64byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRx64byteFrames.setStatus("current")
_BIPPortRx65to127byteFrames_Type = Counter64
_BIPPortRx65to127byteFrames_Object = MibTableColumn
bIPPortRx65to127byteFrames = _BIPPortRx65to127byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 23),
    _BIPPortRx65to127byteFrames_Type()
)
bIPPortRx65to127byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRx65to127byteFrames.setStatus("current")
_BIPPortRx128to255byteFrames_Type = Counter64
_BIPPortRx128to255byteFrames_Object = MibTableColumn
bIPPortRx128to255byteFrames = _BIPPortRx128to255byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 24),
    _BIPPortRx128to255byteFrames_Type()
)
bIPPortRx128to255byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRx128to255byteFrames.setStatus("current")
_BIPPortRx256to511byteFrames_Type = Counter64
_BIPPortRx256to511byteFrames_Object = MibTableColumn
bIPPortRx256to511byteFrames = _BIPPortRx256to511byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 25),
    _BIPPortRx256to511byteFrames_Type()
)
bIPPortRx256to511byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRx256to511byteFrames.setStatus("current")
_BIPPortRx512to1023byteFrames_Type = Counter64
_BIPPortRx512to1023byteFrames_Object = MibTableColumn
bIPPortRx512to1023byteFrames = _BIPPortRx512to1023byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 26),
    _BIPPortRx512to1023byteFrames_Type()
)
bIPPortRx512to1023byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRx512to1023byteFrames.setStatus("current")
_BIPPortRx1024to1518byteFrames_Type = Counter64
_BIPPortRx1024to1518byteFrames_Object = MibTableColumn
bIPPortRx1024to1518byteFrames = _BIPPortRx1024to1518byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 27),
    _BIPPortRx1024to1518byteFrames_Type()
)
bIPPortRx1024to1518byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRx1024to1518byteFrames.setStatus("current")
_BIPPortRx1519to1522byteFrames_Type = Counter64
_BIPPortRx1519to1522byteFrames_Object = MibTableColumn
bIPPortRx1519to1522byteFrames = _BIPPortRx1519to1522byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 28),
    _BIPPortRx1519to1522byteFrames_Type()
)
bIPPortRx1519to1522byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRx1519to1522byteFrames.setStatus("current")
_BIPPortRx1523to10368byteFrames_Type = Counter64
_BIPPortRx1523to10368byteFrames_Object = MibTableColumn
bIPPortRx1523to10368byteFrames = _BIPPortRx1523to10368byteFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 29),
    _BIPPortRx1523to10368byteFrames_Type()
)
bIPPortRx1523to10368byteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRx1523to10368byteFrames.setStatus("current")
_BIPPortRxShortFrames_Type = Counter64
_BIPPortRxShortFrames_Object = MibTableColumn
bIPPortRxShortFrames = _BIPPortRxShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 30),
    _BIPPortRxShortFrames_Type()
)
bIPPortRxShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxShortFrames.setStatus("current")
_BIPPortRxJabberFrames_Type = Counter64
_BIPPortRxJabberFrames_Object = MibTableColumn
bIPPortRxJabberFrames = _BIPPortRxJabberFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 31),
    _BIPPortRxJabberFrames_Type()
)
bIPPortRxJabberFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxJabberFrames.setStatus("current")
_BIPPortRxOvrSzFrames_Type = Counter64
_BIPPortRxOvrSzFrames_Object = MibTableColumn
bIPPortRxOvrSzFrames = _BIPPortRxOvrSzFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 32),
    _BIPPortRxOvrSzFrames_Type()
)
bIPPortRxOvrSzFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxOvrSzFrames.setStatus("current")
_BIPPortRxLenFldErrFrames_Type = Counter64
_BIPPortRxLenFldErrFrames_Object = MibTableColumn
bIPPortRxLenFldErrFrames = _BIPPortRxLenFldErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 33),
    _BIPPortRxLenFldErrFrames_Type()
)
bIPPortRxLenFldErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxLenFldErrFrames.setStatus("current")
_BIPPortRxSymbErrs_Type = Counter64
_BIPPortRxSymbErrs_Object = MibTableColumn
bIPPortRxSymbErrs = _BIPPortRxSymbErrs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 34),
    _BIPPortRxSymbErrs_Type()
)
bIPPortRxSymbErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxSymbErrs.setStatus("current")
_BIPPortRxIntrPktJunk_Type = Counter64
_BIPPortRxIntrPktJunk_Object = MibTableColumn
bIPPortRxIntrPktJunk = _BIPPortRxIntrPktJunk_Object(
    (1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 35),
    _BIPPortRxIntrPktJunk_Type()
)
bIPPortRxIntrPktJunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bIPPortRxIntrPktJunk.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-IP-MIB",
    **{"bIPMIB": bIPMIB,
       "bIPNotifObjects": bIPNotifObjects,
       "bIPMIBObjects": bIPMIBObjects,
       "bIPPortTable": bIPPortTable,
       "bIPPortEntry": bIPPortEntry,
       "bIPPortIndex": bIPPortIndex,
       "bIPPortInterfaceName": bIPPortInterfaceName,
       "bIPPortTxBytesInFrameWoErr": bIPPortTxBytesInFrameWoErr,
       "bIPPortTxFramesWoErrExclPausFrame": bIPPortTxFramesWoErrExclPausFrame,
       "bIPPortTxBcastFrames": bIPPortTxBcastFrames,
       "bIPPortTxL2McastFrames": bIPPortTxL2McastFrames,
       "bIPPortTxPausFrame": bIPPortTxPausFrame,
       "bIPPortTx64byteFrames": bIPPortTx64byteFrames,
       "bIPPortTx65to127byteFrames": bIPPortTx65to127byteFrames,
       "bIPPortTx128to255byteFrames": bIPPortTx128to255byteFrames,
       "bIPPortTx256to511byteFrames": bIPPortTx256to511byteFrames,
       "bIPPortTx512to1023byteFrames": bIPPortTx512to1023byteFrames,
       "bIPPortTx1024to1518byteFrames": bIPPortTx1024to1518byteFrames,
       "bIPPortTx1519to1522byteFrames": bIPPortTx1519to1522byteFrames,
       "bIPPortTx1523toMaxByteFrames": bIPPortTx1523toMaxByteFrames,
       "bIPPortTx17to63byteFrames": bIPPortTx17to63byteFrames,
       "bIPPortTxBadFcsFrames": bIPPortTxBadFcsFrames,
       "bIPPortRxBytesInFrameWoErr": bIPPortRxBytesInFrameWoErr,
       "bIPPortRxBcastFrames": bIPPortRxBcastFrames,
       "bIPPortRxL2McastFrames": bIPPortRxL2McastFrames,
       "bIPPortRxPausFrames": bIPPortRxPausFrames,
       "bIPPortRx64byteFrames": bIPPortRx64byteFrames,
       "bIPPortRx65to127byteFrames": bIPPortRx65to127byteFrames,
       "bIPPortRx128to255byteFrames": bIPPortRx128to255byteFrames,
       "bIPPortRx256to511byteFrames": bIPPortRx256to511byteFrames,
       "bIPPortRx512to1023byteFrames": bIPPortRx512to1023byteFrames,
       "bIPPortRx1024to1518byteFrames": bIPPortRx1024to1518byteFrames,
       "bIPPortRx1519to1522byteFrames": bIPPortRx1519to1522byteFrames,
       "bIPPortRx1523to10368byteFrames": bIPPortRx1523to10368byteFrames,
       "bIPPortRxShortFrames": bIPPortRxShortFrames,
       "bIPPortRxJabberFrames": bIPPortRxJabberFrames,
       "bIPPortRxOvrSzFrames": bIPPortRxOvrSzFrames,
       "bIPPortRxLenFldErrFrames": bIPPortRxLenFldErrFrames,
       "bIPPortRxSymbErrs": bIPPortRxSymbErrs,
       "bIPPortRxIntrPktJunk": bIPPortRxIntrPktJunk}
)
