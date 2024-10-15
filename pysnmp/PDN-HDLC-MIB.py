# SNMP MIB module (PDN-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:41 2024
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

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

pdnHdlcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26)
)
pdnHdlcMIB.setRevisions(
        ("2004-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnHdlcNotifications_ObjectIdentity = ObjectIdentity
pdnHdlcNotifications = _PdnHdlcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 0)
)
_PdnHdlcObjects_ObjectIdentity = ObjectIdentity
pdnHdlcObjects = _PdnHdlcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1)
)
_PdnHdlcStatsTotalTable_Object = MibTable
pdnHdlcStatsTotalTable = _PdnHdlcStatsTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1)
)
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalTable.setStatus("current")
_PdnHdlcStatsTotalEntry_Object = MibTableRow
pdnHdlcStatsTotalEntry = _PdnHdlcStatsTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1)
)
pdnHdlcStatsTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalEntry.setStatus("current")
_PdnHdlcStatsTotalRxGood_Type = Counter32
_PdnHdlcStatsTotalRxGood_Object = MibTableColumn
pdnHdlcStatsTotalRxGood = _PdnHdlcStatsTotalRxGood_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1, 1),
    _PdnHdlcStatsTotalRxGood_Type()
)
pdnHdlcStatsTotalRxGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalRxGood.setStatus("current")
_PdnHdlcStatsTotalRxCRCErrors_Type = Counter32
_PdnHdlcStatsTotalRxCRCErrors_Object = MibTableColumn
pdnHdlcStatsTotalRxCRCErrors = _PdnHdlcStatsTotalRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1, 2),
    _PdnHdlcStatsTotalRxCRCErrors_Type()
)
pdnHdlcStatsTotalRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalRxCRCErrors.setStatus("current")
_PdnHdlcStatsTotalRxAborts_Type = Counter32
_PdnHdlcStatsTotalRxAborts_Object = MibTableColumn
pdnHdlcStatsTotalRxAborts = _PdnHdlcStatsTotalRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1, 3),
    _PdnHdlcStatsTotalRxAborts_Type()
)
pdnHdlcStatsTotalRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalRxAborts.setStatus("current")
_PdnHdlcStatsTotalRxBadAddress_Type = Counter32
_PdnHdlcStatsTotalRxBadAddress_Object = MibTableColumn
pdnHdlcStatsTotalRxBadAddress = _PdnHdlcStatsTotalRxBadAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1, 4),
    _PdnHdlcStatsTotalRxBadAddress_Type()
)
pdnHdlcStatsTotalRxBadAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalRxBadAddress.setStatus("current")
_PdnHdlcStatsTotalRxNoBufAvail_Type = Counter32
_PdnHdlcStatsTotalRxNoBufAvail_Object = MibTableColumn
pdnHdlcStatsTotalRxNoBufAvail = _PdnHdlcStatsTotalRxNoBufAvail_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1, 5),
    _PdnHdlcStatsTotalRxNoBufAvail_Type()
)
pdnHdlcStatsTotalRxNoBufAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalRxNoBufAvail.setStatus("current")
_PdnHdlcStatsTotalReceiverOverrun_Type = Counter32
_PdnHdlcStatsTotalReceiverOverrun_Object = MibTableColumn
pdnHdlcStatsTotalReceiverOverrun = _PdnHdlcStatsTotalReceiverOverrun_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1, 6),
    _PdnHdlcStatsTotalReceiverOverrun_Type()
)
pdnHdlcStatsTotalReceiverOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalReceiverOverrun.setStatus("current")
_PdnHdlcStatsTotalRxMaxSizeExceeded_Type = Counter32
_PdnHdlcStatsTotalRxMaxSizeExceeded_Object = MibTableColumn
pdnHdlcStatsTotalRxMaxSizeExceeded = _PdnHdlcStatsTotalRxMaxSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1, 7),
    _PdnHdlcStatsTotalRxMaxSizeExceeded_Type()
)
pdnHdlcStatsTotalRxMaxSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalRxMaxSizeExceeded.setStatus("current")
_PdnHdlcStatsTotalTx_Type = Counter32
_PdnHdlcStatsTotalTx_Object = MibTableColumn
pdnHdlcStatsTotalTx = _PdnHdlcStatsTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1, 8),
    _PdnHdlcStatsTotalTx_Type()
)
pdnHdlcStatsTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalTx.setStatus("current")
_PdnHdlcStatsTotalTxBufUnderrun_Type = Counter32
_PdnHdlcStatsTotalTxBufUnderrun_Object = MibTableColumn
pdnHdlcStatsTotalTxBufUnderrun = _PdnHdlcStatsTotalTxBufUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 1, 1, 1, 9),
    _PdnHdlcStatsTotalTxBufUnderrun_Type()
)
pdnHdlcStatsTotalTxBufUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalTxBufUnderrun.setStatus("current")
_PdnHdlcAFNs_ObjectIdentity = ObjectIdentity
pdnHdlcAFNs = _PdnHdlcAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 2)
)
_PdnHdlcConformance_ObjectIdentity = ObjectIdentity
pdnHdlcConformance = _PdnHdlcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 3)
)
_PdnHdlcCompliances_ObjectIdentity = ObjectIdentity
pdnHdlcCompliances = _PdnHdlcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 3, 1)
)
_PdnHdlcGroups_ObjectIdentity = ObjectIdentity
pdnHdlcGroups = _PdnHdlcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 3, 2)
)
_PdnHdlcObjGroups_ObjectIdentity = ObjectIdentity
pdnHdlcObjGroups = _PdnHdlcObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 3, 2, 1)
)
_PdnHdlcAfnGroups_ObjectIdentity = ObjectIdentity
pdnHdlcAfnGroups = _PdnHdlcAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 3, 2, 2)
)
_PdnHdlcNtfyGroups_ObjectIdentity = ObjectIdentity
pdnHdlcNtfyGroups = _PdnHdlcNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 3, 2, 3)
)

# Managed Objects groups

pdnHdlcStatsTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 3, 2, 1, 1)
)
pdnHdlcStatsTotalGroup.setObjects(
      *(("PDN-HDLC-MIB", "pdnHdlcStatsTotalRxGood"),
        ("PDN-HDLC-MIB", "pdnHdlcStatsTotalRxCRCErrors"),
        ("PDN-HDLC-MIB", "pdnHdlcStatsTotalRxAborts"),
        ("PDN-HDLC-MIB", "pdnHdlcStatsTotalRxBadAddress"),
        ("PDN-HDLC-MIB", "pdnHdlcStatsTotalRxNoBufAvail"),
        ("PDN-HDLC-MIB", "pdnHdlcStatsTotalReceiverOverrun"),
        ("PDN-HDLC-MIB", "pdnHdlcStatsTotalRxMaxSizeExceeded"),
        ("PDN-HDLC-MIB", "pdnHdlcStatsTotalTx"),
        ("PDN-HDLC-MIB", "pdnHdlcStatsTotalTxBufUnderrun"))
)
if mibBuilder.loadTexts:
    pdnHdlcStatsTotalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnHdlcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 26, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnHdlcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-HDLC-MIB",
    **{"pdnHdlcMIB": pdnHdlcMIB,
       "pdnHdlcNotifications": pdnHdlcNotifications,
       "pdnHdlcObjects": pdnHdlcObjects,
       "pdnHdlcStatsTotalTable": pdnHdlcStatsTotalTable,
       "pdnHdlcStatsTotalEntry": pdnHdlcStatsTotalEntry,
       "pdnHdlcStatsTotalRxGood": pdnHdlcStatsTotalRxGood,
       "pdnHdlcStatsTotalRxCRCErrors": pdnHdlcStatsTotalRxCRCErrors,
       "pdnHdlcStatsTotalRxAborts": pdnHdlcStatsTotalRxAborts,
       "pdnHdlcStatsTotalRxBadAddress": pdnHdlcStatsTotalRxBadAddress,
       "pdnHdlcStatsTotalRxNoBufAvail": pdnHdlcStatsTotalRxNoBufAvail,
       "pdnHdlcStatsTotalReceiverOverrun": pdnHdlcStatsTotalReceiverOverrun,
       "pdnHdlcStatsTotalRxMaxSizeExceeded": pdnHdlcStatsTotalRxMaxSizeExceeded,
       "pdnHdlcStatsTotalTx": pdnHdlcStatsTotalTx,
       "pdnHdlcStatsTotalTxBufUnderrun": pdnHdlcStatsTotalTxBufUnderrun,
       "pdnHdlcAFNs": pdnHdlcAFNs,
       "pdnHdlcConformance": pdnHdlcConformance,
       "pdnHdlcCompliances": pdnHdlcCompliances,
       "pdnHdlcCompliance": pdnHdlcCompliance,
       "pdnHdlcGroups": pdnHdlcGroups,
       "pdnHdlcObjGroups": pdnHdlcObjGroups,
       "pdnHdlcStatsTotalGroup": pdnHdlcStatsTotalGroup,
       "pdnHdlcAfnGroups": pdnHdlcAfnGroups,
       "pdnHdlcNtfyGroups": pdnHdlcNtfyGroups}
)
