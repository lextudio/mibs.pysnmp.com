# SNMP MIB module (Console-Monitoring-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Console-Monitoring-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:49 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniAppMon_ObjectIdentity = ObjectIdentity
sniAppMon = _SniAppMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23)
)
_AppConsMon_ObjectIdentity = ObjectIdentity
appConsMon = _AppConsMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4)
)
_ConsMonGlobalData_ObjectIdentity = ObjectIdentity
consMonGlobalData = _ConsMonGlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 1)
)
_ConsMonVersion_Type = DisplayString
_ConsMonVersion_Object = MibScalar
consMonVersion = _ConsMonVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 1, 1),
    _ConsMonVersion_Type()
)
consMonVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonVersion.setStatus("mandatory")
_ConsMonMsgFilter_Type = DisplayString
_ConsMonMsgFilter_Object = MibScalar
consMonMsgFilter = _ConsMonMsgFilter_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 1, 2),
    _ConsMonMsgFilter_Type()
)
consMonMsgFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consMonMsgFilter.setStatus("mandatory")
_ConsMonNegMsgFilter_Type = DisplayString
_ConsMonNegMsgFilter_Object = MibScalar
consMonNegMsgFilter = _ConsMonNegMsgFilter_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 1, 3),
    _ConsMonNegMsgFilter_Type()
)
consMonNegMsgFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonNegMsgFilter.setStatus("mandatory")
_ConsMonBS2Group_ObjectIdentity = ObjectIdentity
consMonBS2Group = _ConsMonBS2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2)
)
_ConsMonCmdFreeIndex_Type = Integer32
_ConsMonCmdFreeIndex_Object = MibScalar
consMonCmdFreeIndex = _ConsMonCmdFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 1),
    _ConsMonCmdFreeIndex_Type()
)
consMonCmdFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonCmdFreeIndex.setStatus("mandatory")
_ConsMonCmdTabNum_Type = Integer32
_ConsMonCmdTabNum_Object = MibScalar
consMonCmdTabNum = _ConsMonCmdTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 2),
    _ConsMonCmdTabNum_Type()
)
consMonCmdTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonCmdTabNum.setStatus("mandatory")
_ConsMonCmdTable_Object = MibTable
consMonCmdTable = _ConsMonCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 3)
)
if mibBuilder.loadTexts:
    consMonCmdTable.setStatus("mandatory")
_ConsMonCmdEntry_Object = MibTableRow
consMonCmdEntry = _ConsMonCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 3, 1)
)
consMonCmdEntry.setIndexNames(
    (0, "Console-Monitoring-MIB", "consMonCmdIndex"),
)
if mibBuilder.loadTexts:
    consMonCmdEntry.setStatus("mandatory")
_ConsMonCmdIndex_Type = Integer32
_ConsMonCmdIndex_Object = MibTableColumn
consMonCmdIndex = _ConsMonCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 3, 1, 1),
    _ConsMonCmdIndex_Type()
)
consMonCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonCmdIndex.setStatus("mandatory")
_ConsMonCmd_Type = DisplayString
_ConsMonCmd_Object = MibTableColumn
consMonCmd = _ConsMonCmd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 3, 1, 2),
    _ConsMonCmd_Type()
)
consMonCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consMonCmd.setStatus("mandatory")


class _ConsMonCmdResult_Type(Integer32):
    """Custom type consMonCmdResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("error", 4),
          ("executing", 2),
          ("none", 1),
          ("ok", 3),
          ("waiting", 5))
    )


_ConsMonCmdResult_Type.__name__ = "Integer32"
_ConsMonCmdResult_Object = MibTableColumn
consMonCmdResult = _ConsMonCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 3, 1, 3),
    _ConsMonCmdResult_Type()
)
consMonCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonCmdResult.setStatus("mandatory")
_ConsMonCmdMainRetco_Type = DisplayString
_ConsMonCmdMainRetco_Object = MibTableColumn
consMonCmdMainRetco = _ConsMonCmdMainRetco_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 3, 1, 4),
    _ConsMonCmdMainRetco_Type()
)
consMonCmdMainRetco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonCmdMainRetco.setStatus("mandatory")
_ConsMonOutTable_Object = MibTable
consMonOutTable = _ConsMonOutTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 4)
)
if mibBuilder.loadTexts:
    consMonOutTable.setStatus("mandatory")
_ConsMonOutEntry_Object = MibTableRow
consMonOutEntry = _ConsMonOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 4, 1)
)
consMonOutEntry.setIndexNames(
    (0, "Console-Monitoring-MIB", "consMonOutCmdIndex"),
    (0, "Console-Monitoring-MIB", "consMonOutLineNo"),
)
if mibBuilder.loadTexts:
    consMonOutEntry.setStatus("mandatory")
_ConsMonOutCmdIndex_Type = Integer32
_ConsMonOutCmdIndex_Object = MibTableColumn
consMonOutCmdIndex = _ConsMonOutCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 4, 1, 1),
    _ConsMonOutCmdIndex_Type()
)
consMonOutCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonOutCmdIndex.setStatus("mandatory")
_ConsMonOutLineNo_Type = Integer32
_ConsMonOutLineNo_Object = MibTableColumn
consMonOutLineNo = _ConsMonOutLineNo_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 4, 1, 2),
    _ConsMonOutLineNo_Type()
)
consMonOutLineNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonOutLineNo.setStatus("mandatory")
_ConsMonOutContents_Type = DisplayString
_ConsMonOutContents_Object = MibTableColumn
consMonOutContents = _ConsMonOutContents_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 4, 1, 3),
    _ConsMonOutContents_Type()
)
consMonOutContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consMonOutContents.setStatus("mandatory")
_ConsMonBS2Ans_Type = DisplayString
_ConsMonBS2Ans_Object = MibScalar
consMonBS2Ans = _ConsMonBS2Ans_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 23, 4, 2, 5),
    _ConsMonBS2Ans_Type()
)
consMonBS2Ans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consMonBS2Ans.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Console-Monitoring-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniAppMon": sniAppMon,
       "appConsMon": appConsMon,
       "consMonGlobalData": consMonGlobalData,
       "consMonVersion": consMonVersion,
       "consMonMsgFilter": consMonMsgFilter,
       "consMonNegMsgFilter": consMonNegMsgFilter,
       "consMonBS2Group": consMonBS2Group,
       "consMonCmdFreeIndex": consMonCmdFreeIndex,
       "consMonCmdTabNum": consMonCmdTabNum,
       "consMonCmdTable": consMonCmdTable,
       "consMonCmdEntry": consMonCmdEntry,
       "consMonCmdIndex": consMonCmdIndex,
       "consMonCmd": consMonCmd,
       "consMonCmdResult": consMonCmdResult,
       "consMonCmdMainRetco": consMonCmdMainRetco,
       "consMonOutTable": consMonOutTable,
       "consMonOutEntry": consMonOutEntry,
       "consMonOutCmdIndex": consMonOutCmdIndex,
       "consMonOutLineNo": consMonOutLineNo,
       "consMonOutContents": consMonOutContents,
       "consMonBS2Ans": consMonBS2Ans}
)
