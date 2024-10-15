# SNMP MIB module (RUCKUS-ADAPTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-ADAPTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:36 2024
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

(ruckusCommonAdapterModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonAdapterModule")

(RuckusSSID,
 RuckusdB) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusSSID",
    "RuckusdB")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusAdapterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusAdapterObjects_ObjectIdentity = ObjectIdentity
ruckusAdapterObjects = _RuckusAdapterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1)
)
_RuckusAdapterInfo_ObjectIdentity = ObjectIdentity
ruckusAdapterInfo = _RuckusAdapterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1)
)
_RuckusAdapterTable_Object = MibTable
ruckusAdapterTable = _RuckusAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusAdapterTable.setStatus("current")
_RuckusAdapterEntry_Object = MibTableRow
ruckusAdapterEntry = _RuckusAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 1, 1)
)
ruckusAdapterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-ADAPTER-MIB", "ruckusAdapterMacAddress"),
)
if mibBuilder.loadTexts:
    ruckusAdapterEntry.setStatus("current")
_RuckusAdapterMacAddress_Type = MacAddress
_RuckusAdapterMacAddress_Object = MibTableColumn
ruckusAdapterMacAddress = _RuckusAdapterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 1, 1, 1),
    _RuckusAdapterMacAddress_Type()
)
ruckusAdapterMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAdapterMacAddress.setStatus("current")


class _RuckusAdapterReboot_Type(TruthValue):
    """Custom type ruckusAdapterReboot based on TruthValue"""


_RuckusAdapterReboot_Object = MibTableColumn
ruckusAdapterReboot = _RuckusAdapterReboot_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 1, 1, 2),
    _RuckusAdapterReboot_Type()
)
ruckusAdapterReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusAdapterReboot.setStatus("current")
_RuckusAdapterInfoTable_Object = MibTable
ruckusAdapterInfoTable = _RuckusAdapterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusAdapterInfoTable.setStatus("current")
_RuckusAdapterInfoEntry_Object = MibTableRow
ruckusAdapterInfoEntry = _RuckusAdapterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 2, 1)
)
ruckusAdapterInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-ADAPTER-MIB", "ruckusAdapterInfoMacAddr"),
)
if mibBuilder.loadTexts:
    ruckusAdapterInfoEntry.setStatus("current")
_RuckusAdapterInfoMacAddr_Type = MacAddress
_RuckusAdapterInfoMacAddr_Object = MibTableColumn
ruckusAdapterInfoMacAddr = _RuckusAdapterInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 2, 1, 1),
    _RuckusAdapterInfoMacAddr_Type()
)
ruckusAdapterInfoMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAdapterInfoMacAddr.setStatus("current")
_RuckusAdapterInfoSSID_Type = RuckusSSID
_RuckusAdapterInfoSSID_Object = MibTableColumn
ruckusAdapterInfoSSID = _RuckusAdapterInfoSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 2, 1, 2),
    _RuckusAdapterInfoSSID_Type()
)
ruckusAdapterInfoSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterInfoSSID.setStatus("current")
_RuckusAdapterInfoBSSID_Type = MacAddress
_RuckusAdapterInfoBSSID_Object = MibTableColumn
ruckusAdapterInfoBSSID = _RuckusAdapterInfoBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 2, 1, 3),
    _RuckusAdapterInfoBSSID_Type()
)
ruckusAdapterInfoBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterInfoBSSID.setStatus("current")
_RuckusAdapterRssi_Type = RuckusdB
_RuckusAdapterRssi_Object = MibTableColumn
ruckusAdapterRssi = _RuckusAdapterRssi_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 2, 1, 4),
    _RuckusAdapterRssi_Type()
)
ruckusAdapterRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterRssi.setStatus("current")
_RuckusAdapterStatTable_Object = MibTable
ruckusAdapterStatTable = _RuckusAdapterStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruckusAdapterStatTable.setStatus("current")
_RuckusAdapterStatEntry_Object = MibTableRow
ruckusAdapterStatEntry = _RuckusAdapterStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1)
)
ruckusAdapterStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-ADAPTER-MIB", "ruckusAdapterStatMacAddr"),
)
if mibBuilder.loadTexts:
    ruckusAdapterStatEntry.setStatus("current")
_RuckusAdapterStatMacAddr_Type = MacAddress
_RuckusAdapterStatMacAddr_Object = MibTableColumn
ruckusAdapterStatMacAddr = _RuckusAdapterStatMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 1),
    _RuckusAdapterStatMacAddr_Type()
)
ruckusAdapterStatMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusAdapterStatMacAddr.setStatus("current")
_RuckusAdapterStatRxDataFrames_Type = Counter32
_RuckusAdapterStatRxDataFrames_Object = MibTableColumn
ruckusAdapterStatRxDataFrames = _RuckusAdapterStatRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 2),
    _RuckusAdapterStatRxDataFrames_Type()
)
ruckusAdapterStatRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxDataFrames.setStatus("current")
_RuckusAdapterStatRxMgmtFrames_Type = Counter32
_RuckusAdapterStatRxMgmtFrames_Object = MibTableColumn
ruckusAdapterStatRxMgmtFrames = _RuckusAdapterStatRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 3),
    _RuckusAdapterStatRxMgmtFrames_Type()
)
ruckusAdapterStatRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxMgmtFrames.setStatus("current")
_RuckusAdapterStatRxCtrlFrames_Type = Counter32
_RuckusAdapterStatRxCtrlFrames_Object = MibTableColumn
ruckusAdapterStatRxCtrlFrames = _RuckusAdapterStatRxCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 4),
    _RuckusAdapterStatRxCtrlFrames_Type()
)
ruckusAdapterStatRxCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxCtrlFrames.setStatus("current")
_RuckusAdapterStatRxUcastFrames_Type = Counter32
_RuckusAdapterStatRxUcastFrames_Object = MibTableColumn
ruckusAdapterStatRxUcastFrames = _RuckusAdapterStatRxUcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 5),
    _RuckusAdapterStatRxUcastFrames_Type()
)
ruckusAdapterStatRxUcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxUcastFrames.setStatus("current")
_RuckusAdapterStatRxMcastFrames_Type = Counter32
_RuckusAdapterStatRxMcastFrames_Object = MibTableColumn
ruckusAdapterStatRxMcastFrames = _RuckusAdapterStatRxMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 6),
    _RuckusAdapterStatRxMcastFrames_Type()
)
ruckusAdapterStatRxMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxMcastFrames.setStatus("current")
_RuckusAdapterStatRxBytes_Type = Counter32
_RuckusAdapterStatRxBytes_Object = MibTableColumn
ruckusAdapterStatRxBytes = _RuckusAdapterStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 7),
    _RuckusAdapterStatRxBytes_Type()
)
ruckusAdapterStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxBytes.setStatus("current")
_RuckusAdapterStatRxDup_Type = Counter32
_RuckusAdapterStatRxDup_Object = MibTableColumn
ruckusAdapterStatRxDup = _RuckusAdapterStatRxDup_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 8),
    _RuckusAdapterStatRxDup_Type()
)
ruckusAdapterStatRxDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxDup.setStatus("current")
_RuckusAdapterStatRxNoPrivacy_Type = Counter32
_RuckusAdapterStatRxNoPrivacy_Object = MibTableColumn
ruckusAdapterStatRxNoPrivacy = _RuckusAdapterStatRxNoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 9),
    _RuckusAdapterStatRxNoPrivacy_Type()
)
ruckusAdapterStatRxNoPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxNoPrivacy.setStatus("current")
_RuckusAdapterStatRxWEPFail_Type = Counter32
_RuckusAdapterStatRxWEPFail_Object = MibTableColumn
ruckusAdapterStatRxWEPFail = _RuckusAdapterStatRxWEPFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 10),
    _RuckusAdapterStatRxWEPFail_Type()
)
ruckusAdapterStatRxWEPFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxWEPFail.setStatus("current")
_RuckusAdapterStatRxDemicFail_Type = Counter32
_RuckusAdapterStatRxDemicFail_Object = MibTableColumn
ruckusAdapterStatRxDemicFail = _RuckusAdapterStatRxDemicFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 11),
    _RuckusAdapterStatRxDemicFail_Type()
)
ruckusAdapterStatRxDemicFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxDemicFail.setStatus("current")
_RuckusAdapterStatRxDecap_Type = Counter32
_RuckusAdapterStatRxDecap_Object = MibTableColumn
ruckusAdapterStatRxDecap = _RuckusAdapterStatRxDecap_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 12),
    _RuckusAdapterStatRxDecap_Type()
)
ruckusAdapterStatRxDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxDecap.setStatus("current")
_RuckusAdapterStatRxDeFrag_Type = Counter32
_RuckusAdapterStatRxDeFrag_Object = MibTableColumn
ruckusAdapterStatRxDeFrag = _RuckusAdapterStatRxDeFrag_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 13),
    _RuckusAdapterStatRxDeFrag_Type()
)
ruckusAdapterStatRxDeFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxDeFrag.setStatus("current")
_RuckusAdapterStatRxDisAssoc_Type = Counter32
_RuckusAdapterStatRxDisAssoc_Object = MibTableColumn
ruckusAdapterStatRxDisAssoc = _RuckusAdapterStatRxDisAssoc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 14),
    _RuckusAdapterStatRxDisAssoc_Type()
)
ruckusAdapterStatRxDisAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxDisAssoc.setStatus("current")
_RuckusAdapterStatRxDeAuth_Type = Counter32
_RuckusAdapterStatRxDeAuth_Object = MibTableColumn
ruckusAdapterStatRxDeAuth = _RuckusAdapterStatRxDeAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 15),
    _RuckusAdapterStatRxDeAuth_Type()
)
ruckusAdapterStatRxDeAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxDeAuth.setStatus("current")
_RuckusAdapterStatRxUnAuth_Type = Counter32
_RuckusAdapterStatRxUnAuth_Object = MibTableColumn
ruckusAdapterStatRxUnAuth = _RuckusAdapterStatRxUnAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 16),
    _RuckusAdapterStatRxUnAuth_Type()
)
ruckusAdapterStatRxUnAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxUnAuth.setStatus("current")
_RuckusAdapterStatRxUnEncrypted_Type = Counter32
_RuckusAdapterStatRxUnEncrypted_Object = MibTableColumn
ruckusAdapterStatRxUnEncrypted = _RuckusAdapterStatRxUnEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 17),
    _RuckusAdapterStatRxUnEncrypted_Type()
)
ruckusAdapterStatRxUnEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxUnEncrypted.setStatus("current")
_RuckusAdapterStatRxBeacons_Type = Counter32
_RuckusAdapterStatRxBeacons_Object = MibTableColumn
ruckusAdapterStatRxBeacons = _RuckusAdapterStatRxBeacons_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 18),
    _RuckusAdapterStatRxBeacons_Type()
)
ruckusAdapterStatRxBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatRxBeacons.setStatus("current")
_RuckusAdapterStatTxDataFrames_Type = Counter32
_RuckusAdapterStatTxDataFrames_Object = MibTableColumn
ruckusAdapterStatTxDataFrames = _RuckusAdapterStatTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 19),
    _RuckusAdapterStatTxDataFrames_Type()
)
ruckusAdapterStatTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxDataFrames.setStatus("current")
_RuckusAdapterStatTxMgmtFrames_Type = Counter32
_RuckusAdapterStatTxMgmtFrames_Object = MibTableColumn
ruckusAdapterStatTxMgmtFrames = _RuckusAdapterStatTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 20),
    _RuckusAdapterStatTxMgmtFrames_Type()
)
ruckusAdapterStatTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxMgmtFrames.setStatus("current")
_RuckusAdapterStatTxUcastFrames_Type = Counter32
_RuckusAdapterStatTxUcastFrames_Object = MibTableColumn
ruckusAdapterStatTxUcastFrames = _RuckusAdapterStatTxUcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 21),
    _RuckusAdapterStatTxUcastFrames_Type()
)
ruckusAdapterStatTxUcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxUcastFrames.setStatus("current")
_RuckusAdapterStatTxMcastFrames_Type = Counter32
_RuckusAdapterStatTxMcastFrames_Object = MibTableColumn
ruckusAdapterStatTxMcastFrames = _RuckusAdapterStatTxMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 22),
    _RuckusAdapterStatTxMcastFrames_Type()
)
ruckusAdapterStatTxMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxMcastFrames.setStatus("current")
_RuckusAdapterStatTxBytes_Type = Counter32
_RuckusAdapterStatTxBytes_Object = MibTableColumn
ruckusAdapterStatTxBytes = _RuckusAdapterStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 23),
    _RuckusAdapterStatTxBytes_Type()
)
ruckusAdapterStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxBytes.setStatus("current")
_RuckusAdapterStatTxAssoc_Type = Counter32
_RuckusAdapterStatTxAssoc_Object = MibTableColumn
ruckusAdapterStatTxAssoc = _RuckusAdapterStatTxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 24),
    _RuckusAdapterStatTxAssoc_Type()
)
ruckusAdapterStatTxAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxAssoc.setStatus("current")
_RuckusAdapterStatTxAssocFail_Type = Counter32
_RuckusAdapterStatTxAssocFail_Object = MibTableColumn
ruckusAdapterStatTxAssocFail = _RuckusAdapterStatTxAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 25),
    _RuckusAdapterStatTxAssocFail_Type()
)
ruckusAdapterStatTxAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxAssocFail.setStatus("current")
_RuckusAdapterStatTxAuth_Type = Counter32
_RuckusAdapterStatTxAuth_Object = MibTableColumn
ruckusAdapterStatTxAuth = _RuckusAdapterStatTxAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 26),
    _RuckusAdapterStatTxAuth_Type()
)
ruckusAdapterStatTxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxAuth.setStatus("current")
_RuckusAdapterStatTxAuthFail_Type = Counter32
_RuckusAdapterStatTxAuthFail_Object = MibTableColumn
ruckusAdapterStatTxAuthFail = _RuckusAdapterStatTxAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 27),
    _RuckusAdapterStatTxAuthFail_Type()
)
ruckusAdapterStatTxAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxAuthFail.setStatus("current")
_RuckusAdapterStatTxDeAuth_Type = Counter32
_RuckusAdapterStatTxDeAuth_Object = MibTableColumn
ruckusAdapterStatTxDeAuth = _RuckusAdapterStatTxDeAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 28),
    _RuckusAdapterStatTxDeAuth_Type()
)
ruckusAdapterStatTxDeAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxDeAuth.setStatus("current")
_RuckusAdapterStatTxDisAssoc_Type = Counter32
_RuckusAdapterStatTxDisAssoc_Object = MibTableColumn
ruckusAdapterStatTxDisAssoc = _RuckusAdapterStatTxDisAssoc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 29),
    _RuckusAdapterStatTxDisAssoc_Type()
)
ruckusAdapterStatTxDisAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxDisAssoc.setStatus("current")
_RuckusAdapterStatTxProbeReq_Type = Counter32
_RuckusAdapterStatTxProbeReq_Object = MibTableColumn
ruckusAdapterStatTxProbeReq = _RuckusAdapterStatTxProbeReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 30),
    _RuckusAdapterStatTxProbeReq_Type()
)
ruckusAdapterStatTxProbeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxProbeReq.setStatus("current")
_RuckusAdapterStatTxProbeResp_Type = Counter32
_RuckusAdapterStatTxProbeResp_Object = MibTableColumn
ruckusAdapterStatTxProbeResp = _RuckusAdapterStatTxProbeResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 1, 1, 3, 1, 31),
    _RuckusAdapterStatTxProbeResp_Type()
)
ruckusAdapterStatTxProbeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusAdapterStatTxProbeResp.setStatus("current")
_RuckusAdapterEvents_ObjectIdentity = ObjectIdentity
ruckusAdapterEvents = _RuckusAdapterEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 9, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ADAPTER-MIB",
    **{"ruckusAdapterMIB": ruckusAdapterMIB,
       "ruckusAdapterObjects": ruckusAdapterObjects,
       "ruckusAdapterInfo": ruckusAdapterInfo,
       "ruckusAdapterTable": ruckusAdapterTable,
       "ruckusAdapterEntry": ruckusAdapterEntry,
       "ruckusAdapterMacAddress": ruckusAdapterMacAddress,
       "ruckusAdapterReboot": ruckusAdapterReboot,
       "ruckusAdapterInfoTable": ruckusAdapterInfoTable,
       "ruckusAdapterInfoEntry": ruckusAdapterInfoEntry,
       "ruckusAdapterInfoMacAddr": ruckusAdapterInfoMacAddr,
       "ruckusAdapterInfoSSID": ruckusAdapterInfoSSID,
       "ruckusAdapterInfoBSSID": ruckusAdapterInfoBSSID,
       "ruckusAdapterRssi": ruckusAdapterRssi,
       "ruckusAdapterStatTable": ruckusAdapterStatTable,
       "ruckusAdapterStatEntry": ruckusAdapterStatEntry,
       "ruckusAdapterStatMacAddr": ruckusAdapterStatMacAddr,
       "ruckusAdapterStatRxDataFrames": ruckusAdapterStatRxDataFrames,
       "ruckusAdapterStatRxMgmtFrames": ruckusAdapterStatRxMgmtFrames,
       "ruckusAdapterStatRxCtrlFrames": ruckusAdapterStatRxCtrlFrames,
       "ruckusAdapterStatRxUcastFrames": ruckusAdapterStatRxUcastFrames,
       "ruckusAdapterStatRxMcastFrames": ruckusAdapterStatRxMcastFrames,
       "ruckusAdapterStatRxBytes": ruckusAdapterStatRxBytes,
       "ruckusAdapterStatRxDup": ruckusAdapterStatRxDup,
       "ruckusAdapterStatRxNoPrivacy": ruckusAdapterStatRxNoPrivacy,
       "ruckusAdapterStatRxWEPFail": ruckusAdapterStatRxWEPFail,
       "ruckusAdapterStatRxDemicFail": ruckusAdapterStatRxDemicFail,
       "ruckusAdapterStatRxDecap": ruckusAdapterStatRxDecap,
       "ruckusAdapterStatRxDeFrag": ruckusAdapterStatRxDeFrag,
       "ruckusAdapterStatRxDisAssoc": ruckusAdapterStatRxDisAssoc,
       "ruckusAdapterStatRxDeAuth": ruckusAdapterStatRxDeAuth,
       "ruckusAdapterStatRxUnAuth": ruckusAdapterStatRxUnAuth,
       "ruckusAdapterStatRxUnEncrypted": ruckusAdapterStatRxUnEncrypted,
       "ruckusAdapterStatRxBeacons": ruckusAdapterStatRxBeacons,
       "ruckusAdapterStatTxDataFrames": ruckusAdapterStatTxDataFrames,
       "ruckusAdapterStatTxMgmtFrames": ruckusAdapterStatTxMgmtFrames,
       "ruckusAdapterStatTxUcastFrames": ruckusAdapterStatTxUcastFrames,
       "ruckusAdapterStatTxMcastFrames": ruckusAdapterStatTxMcastFrames,
       "ruckusAdapterStatTxBytes": ruckusAdapterStatTxBytes,
       "ruckusAdapterStatTxAssoc": ruckusAdapterStatTxAssoc,
       "ruckusAdapterStatTxAssocFail": ruckusAdapterStatTxAssocFail,
       "ruckusAdapterStatTxAuth": ruckusAdapterStatTxAuth,
       "ruckusAdapterStatTxAuthFail": ruckusAdapterStatTxAuthFail,
       "ruckusAdapterStatTxDeAuth": ruckusAdapterStatTxDeAuth,
       "ruckusAdapterStatTxDisAssoc": ruckusAdapterStatTxDisAssoc,
       "ruckusAdapterStatTxProbeReq": ruckusAdapterStatTxProbeReq,
       "ruckusAdapterStatTxProbeResp": ruckusAdapterStatTxProbeResp,
       "ruckusAdapterEvents": ruckusAdapterEvents}
)
