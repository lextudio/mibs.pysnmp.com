# SNMP MIB module (ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:35 2024
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

(BridgeId,
 dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysSpanningTreeDiagnosticMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29)
)
etsysSpanningTreeDiagnosticMIB.setRevisions(
        ("2006-10-04 19:49",
         "2005-01-24 15:46",
         "2004-06-07 19:20",
         "2003-01-15 19:18",
         "2002-11-21 19:01",
         "2002-11-18 21:36",
         "2002-10-10 21:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysStpPortRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 4),
          ("backUp", 5),
          ("designated", 3),
          ("disabled", 1),
          ("master", 6),
          ("root", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysStpDiagObjects_ObjectIdentity = ObjectIdentity
etsysStpDiagObjects = _EtsysStpDiagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1)
)
_EtsysStpDiagNotifications_ObjectIdentity = ObjectIdentity
etsysStpDiagNotifications = _EtsysStpDiagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 0)
)
_EtsysStpDiagControl_ObjectIdentity = ObjectIdentity
etsysStpDiagControl = _EtsysStpDiagControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 1)
)


class _EtsysStpDiagCounterReset_Type(Integer32):
    """Custom type etsysStpDiagCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("reset", 2))
    )


_EtsysStpDiagCounterReset_Type.__name__ = "Integer32"
_EtsysStpDiagCounterReset_Object = MibScalar
etsysStpDiagCounterReset = _EtsysStpDiagCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 1, 1),
    _EtsysStpDiagCounterReset_Type()
)
etsysStpDiagCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysStpDiagCounterReset.setStatus("current")
_EtsysStpDiagCounterResetElapsedTime_Type = Unsigned32
_EtsysStpDiagCounterResetElapsedTime_Object = MibScalar
etsysStpDiagCounterResetElapsedTime = _EtsysStpDiagCounterResetElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 1, 2),
    _EtsysStpDiagCounterResetElapsedTime_Type()
)
etsysStpDiagCounterResetElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCounterResetElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysStpDiagCounterResetElapsedTime.setUnits("seconds")
_EtsysStpDiagCounterResetDateAndTime_Type = DateAndTime
_EtsysStpDiagCounterResetDateAndTime_Object = MibScalar
etsysStpDiagCounterResetDateAndTime = _EtsysStpDiagCounterResetDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 1, 3),
    _EtsysStpDiagCounterResetDateAndTime_Type()
)
etsysStpDiagCounterResetDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCounterResetDateAndTime.setStatus("current")
_EtsysStpDiagCommon_ObjectIdentity = ObjectIdentity
etsysStpDiagCommon = _EtsysStpDiagCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2)
)
_EtsysStpDiagTopChanges_Type = Counter32
_EtsysStpDiagTopChanges_Object = MibScalar
etsysStpDiagTopChanges = _EtsysStpDiagTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 1),
    _EtsysStpDiagTopChanges_Type()
)
etsysStpDiagTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagTopChanges.setStatus("current")
_EtsysStpDiagCommonInvalidBpdu_Type = Counter32
_EtsysStpDiagCommonInvalidBpdu_Object = MibScalar
etsysStpDiagCommonInvalidBpdu = _EtsysStpDiagCommonInvalidBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 2),
    _EtsysStpDiagCommonInvalidBpdu_Type()
)
etsysStpDiagCommonInvalidBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonInvalidBpdu.setStatus("current")
_EtsysStpDiagCommonStpCfgBpduRx_Type = Counter32
_EtsysStpDiagCommonStpCfgBpduRx_Object = MibScalar
etsysStpDiagCommonStpCfgBpduRx = _EtsysStpDiagCommonStpCfgBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 3),
    _EtsysStpDiagCommonStpCfgBpduRx_Type()
)
etsysStpDiagCommonStpCfgBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonStpCfgBpduRx.setStatus("current")
_EtsysStpDiagCommonStpCfgBpduTx_Type = Counter32
_EtsysStpDiagCommonStpCfgBpduTx_Object = MibScalar
etsysStpDiagCommonStpCfgBpduTx = _EtsysStpDiagCommonStpCfgBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 4),
    _EtsysStpDiagCommonStpCfgBpduTx_Type()
)
etsysStpDiagCommonStpCfgBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonStpCfgBpduTx.setStatus("current")
_EtsysStpDiagCommonStpTcnBpduRx_Type = Counter32
_EtsysStpDiagCommonStpTcnBpduRx_Object = MibScalar
etsysStpDiagCommonStpTcnBpduRx = _EtsysStpDiagCommonStpTcnBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 5),
    _EtsysStpDiagCommonStpTcnBpduRx_Type()
)
etsysStpDiagCommonStpTcnBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonStpTcnBpduRx.setStatus("current")
_EtsysStpDiagCommonStpTcnBpduTx_Type = Counter32
_EtsysStpDiagCommonStpTcnBpduTx_Object = MibScalar
etsysStpDiagCommonStpTcnBpduTx = _EtsysStpDiagCommonStpTcnBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 6),
    _EtsysStpDiagCommonStpTcnBpduTx_Type()
)
etsysStpDiagCommonStpTcnBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonStpTcnBpduTx.setStatus("current")
_EtsysStpDiagCommonRstBpduRx_Type = Counter32
_EtsysStpDiagCommonRstBpduRx_Object = MibScalar
etsysStpDiagCommonRstBpduRx = _EtsysStpDiagCommonRstBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 7),
    _EtsysStpDiagCommonRstBpduRx_Type()
)
etsysStpDiagCommonRstBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonRstBpduRx.setStatus("current")
_EtsysStpDiagCommonRstBpduTx_Type = Counter32
_EtsysStpDiagCommonRstBpduTx_Object = MibScalar
etsysStpDiagCommonRstBpduTx = _EtsysStpDiagCommonRstBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 8),
    _EtsysStpDiagCommonRstBpduTx_Type()
)
etsysStpDiagCommonRstBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonRstBpduTx.setStatus("current")
_EtsysStpDiagCommonRstTcRx_Type = Counter32
_EtsysStpDiagCommonRstTcRx_Object = MibScalar
etsysStpDiagCommonRstTcRx = _EtsysStpDiagCommonRstTcRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 9),
    _EtsysStpDiagCommonRstTcRx_Type()
)
etsysStpDiagCommonRstTcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonRstTcRx.setStatus("current")
_EtsysStpDiagCommonRstTcTx_Type = Counter32
_EtsysStpDiagCommonRstTcTx_Object = MibScalar
etsysStpDiagCommonRstTcTx = _EtsysStpDiagCommonRstTcTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 10),
    _EtsysStpDiagCommonRstTcTx_Type()
)
etsysStpDiagCommonRstTcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonRstTcTx.setStatus("current")
_EtsysStpDiagCommonMstBpduRx_Type = Counter32
_EtsysStpDiagCommonMstBpduRx_Object = MibScalar
etsysStpDiagCommonMstBpduRx = _EtsysStpDiagCommonMstBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 11),
    _EtsysStpDiagCommonMstBpduRx_Type()
)
etsysStpDiagCommonMstBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonMstBpduRx.setStatus("current")
_EtsysStpDiagCommonMstBpduTx_Type = Counter32
_EtsysStpDiagCommonMstBpduTx_Object = MibScalar
etsysStpDiagCommonMstBpduTx = _EtsysStpDiagCommonMstBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 12),
    _EtsysStpDiagCommonMstBpduTx_Type()
)
etsysStpDiagCommonMstBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonMstBpduTx.setStatus("current")
_EtsysStpDiagCommonMstCistTcRx_Type = Counter32
_EtsysStpDiagCommonMstCistTcRx_Object = MibScalar
etsysStpDiagCommonMstCistTcRx = _EtsysStpDiagCommonMstCistTcRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 13),
    _EtsysStpDiagCommonMstCistTcRx_Type()
)
etsysStpDiagCommonMstCistTcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonMstCistTcRx.setStatus("current")
_EtsysStpDiagCommonMstCistTcTx_Type = Counter32
_EtsysStpDiagCommonMstCistTcTx_Object = MibScalar
etsysStpDiagCommonMstCistTcTx = _EtsysStpDiagCommonMstCistTcTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 14),
    _EtsysStpDiagCommonMstCistTcTx_Type()
)
etsysStpDiagCommonMstCistTcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonMstCistTcTx.setStatus("current")
_EtsysStpDiagCommonStpCfgBpduRxTcFlagSet_Type = Counter32
_EtsysStpDiagCommonStpCfgBpduRxTcFlagSet_Object = MibScalar
etsysStpDiagCommonStpCfgBpduRxTcFlagSet = _EtsysStpDiagCommonStpCfgBpduRxTcFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 15),
    _EtsysStpDiagCommonStpCfgBpduRxTcFlagSet_Type()
)
etsysStpDiagCommonStpCfgBpduRxTcFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonStpCfgBpduRxTcFlagSet.setStatus("current")
_EtsysStpDiagCommonStpCfgBpduTxTcFlagSet_Type = Counter32
_EtsysStpDiagCommonStpCfgBpduTxTcFlagSet_Object = MibScalar
etsysStpDiagCommonStpCfgBpduTxTcFlagSet = _EtsysStpDiagCommonStpCfgBpduTxTcFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 16),
    _EtsysStpDiagCommonStpCfgBpduTxTcFlagSet_Type()
)
etsysStpDiagCommonStpCfgBpduTxTcFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonStpCfgBpduTxTcFlagSet.setStatus("current")
_EtsysStpDiagCommonDisputedBpdu_Type = Counter32
_EtsysStpDiagCommonDisputedBpdu_Object = MibScalar
etsysStpDiagCommonDisputedBpdu = _EtsysStpDiagCommonDisputedBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 17),
    _EtsysStpDiagCommonDisputedBpdu_Type()
)
etsysStpDiagCommonDisputedBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCommonDisputedBpdu.setStatus("current")
_EtsysStpDiagMessageExpiration_Type = Counter32
_EtsysStpDiagMessageExpiration_Object = MibScalar
etsysStpDiagMessageExpiration = _EtsysStpDiagMessageExpiration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 2, 28),
    _EtsysStpDiagMessageExpiration_Type()
)
etsysStpDiagMessageExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMessageExpiration.setStatus("current")
_EtsysStpDiagCistPort_ObjectIdentity = ObjectIdentity
etsysStpDiagCistPort = _EtsysStpDiagCistPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3)
)
_EtsysStpDiagCistPortTable_Object = MibTable
etsysStpDiagCistPortTable = _EtsysStpDiagCistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysStpDiagCistPortTable.setStatus("current")
_EtsysStpDiagCistPortEntry_Object = MibTableRow
etsysStpDiagCistPortEntry = _EtsysStpDiagCistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1)
)
etsysStpDiagCistPortEntry.setIndexNames(
    (0, "ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortNumber"),
)
if mibBuilder.loadTexts:
    etsysStpDiagCistPortEntry.setStatus("current")
_EtsysStpDiagCistPortNumber_Type = InterfaceIndex
_EtsysStpDiagCistPortNumber_Object = MibTableColumn
etsysStpDiagCistPortNumber = _EtsysStpDiagCistPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 1),
    _EtsysStpDiagCistPortNumber_Type()
)
etsysStpDiagCistPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortNumber.setStatus("current")
_EtsysStpDiagCistPortRole_Type = EtsysStpPortRole
_EtsysStpDiagCistPortRole_Object = MibTableColumn
etsysStpDiagCistPortRole = _EtsysStpDiagCistPortRole_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 2),
    _EtsysStpDiagCistPortRole_Type()
)
etsysStpDiagCistPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortRole.setStatus("current")
_EtsysStpDiagCistPortInvalidBpdu_Type = Counter32
_EtsysStpDiagCistPortInvalidBpdu_Object = MibTableColumn
etsysStpDiagCistPortInvalidBpdu = _EtsysStpDiagCistPortInvalidBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 3),
    _EtsysStpDiagCistPortInvalidBpdu_Type()
)
etsysStpDiagCistPortInvalidBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortInvalidBpdu.setStatus("current")
_EtsysStpDiagCistPortStpCfgBpduRx_Type = Counter32
_EtsysStpDiagCistPortStpCfgBpduRx_Object = MibTableColumn
etsysStpDiagCistPortStpCfgBpduRx = _EtsysStpDiagCistPortStpCfgBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 4),
    _EtsysStpDiagCistPortStpCfgBpduRx_Type()
)
etsysStpDiagCistPortStpCfgBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortStpCfgBpduRx.setStatus("current")
_EtsysStpDiagCistPortStpCfgBpduTx_Type = Counter32
_EtsysStpDiagCistPortStpCfgBpduTx_Object = MibTableColumn
etsysStpDiagCistPortStpCfgBpduTx = _EtsysStpDiagCistPortStpCfgBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 5),
    _EtsysStpDiagCistPortStpCfgBpduTx_Type()
)
etsysStpDiagCistPortStpCfgBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortStpCfgBpduTx.setStatus("current")
_EtsysStpDiagCistPortStpTcnBpduRx_Type = Counter32
_EtsysStpDiagCistPortStpTcnBpduRx_Object = MibTableColumn
etsysStpDiagCistPortStpTcnBpduRx = _EtsysStpDiagCistPortStpTcnBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 6),
    _EtsysStpDiagCistPortStpTcnBpduRx_Type()
)
etsysStpDiagCistPortStpTcnBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortStpTcnBpduRx.setStatus("current")
_EtsysStpDiagCistPortStpTcnBpduTx_Type = Counter32
_EtsysStpDiagCistPortStpTcnBpduTx_Object = MibTableColumn
etsysStpDiagCistPortStpTcnBpduTx = _EtsysStpDiagCistPortStpTcnBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 7),
    _EtsysStpDiagCistPortStpTcnBpduTx_Type()
)
etsysStpDiagCistPortStpTcnBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortStpTcnBpduTx.setStatus("current")
_EtsysStpDiagCistPortRstBpduRx_Type = Counter32
_EtsysStpDiagCistPortRstBpduRx_Object = MibTableColumn
etsysStpDiagCistPortRstBpduRx = _EtsysStpDiagCistPortRstBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 8),
    _EtsysStpDiagCistPortRstBpduRx_Type()
)
etsysStpDiagCistPortRstBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortRstBpduRx.setStatus("current")
_EtsysStpDiagCistPortRstBpduTx_Type = Counter32
_EtsysStpDiagCistPortRstBpduTx_Object = MibTableColumn
etsysStpDiagCistPortRstBpduTx = _EtsysStpDiagCistPortRstBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 9),
    _EtsysStpDiagCistPortRstBpduTx_Type()
)
etsysStpDiagCistPortRstBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortRstBpduTx.setStatus("current")
_EtsysStpDiagCistPortRstTcRx_Type = Counter32
_EtsysStpDiagCistPortRstTcRx_Object = MibTableColumn
etsysStpDiagCistPortRstTcRx = _EtsysStpDiagCistPortRstTcRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 10),
    _EtsysStpDiagCistPortRstTcRx_Type()
)
etsysStpDiagCistPortRstTcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortRstTcRx.setStatus("current")
_EtsysStpDiagCistPortRstTcTx_Type = Counter32
_EtsysStpDiagCistPortRstTcTx_Object = MibTableColumn
etsysStpDiagCistPortRstTcTx = _EtsysStpDiagCistPortRstTcTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 11),
    _EtsysStpDiagCistPortRstTcTx_Type()
)
etsysStpDiagCistPortRstTcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortRstTcTx.setStatus("current")
_EtsysStpDiagCistPortMstBpduRx_Type = Counter32
_EtsysStpDiagCistPortMstBpduRx_Object = MibTableColumn
etsysStpDiagCistPortMstBpduRx = _EtsysStpDiagCistPortMstBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 12),
    _EtsysStpDiagCistPortMstBpduRx_Type()
)
etsysStpDiagCistPortMstBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortMstBpduRx.setStatus("current")
_EtsysStpDiagCistPortMstBpduTx_Type = Counter32
_EtsysStpDiagCistPortMstBpduTx_Object = MibTableColumn
etsysStpDiagCistPortMstBpduTx = _EtsysStpDiagCistPortMstBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 13),
    _EtsysStpDiagCistPortMstBpduTx_Type()
)
etsysStpDiagCistPortMstBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortMstBpduTx.setStatus("current")
_EtsysStpDiagCistPortMstCistTcRx_Type = Counter32
_EtsysStpDiagCistPortMstCistTcRx_Object = MibTableColumn
etsysStpDiagCistPortMstCistTcRx = _EtsysStpDiagCistPortMstCistTcRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 14),
    _EtsysStpDiagCistPortMstCistTcRx_Type()
)
etsysStpDiagCistPortMstCistTcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortMstCistTcRx.setStatus("current")
_EtsysStpDiagCistPortMstCistTcTx_Type = Counter32
_EtsysStpDiagCistPortMstCistTcTx_Object = MibTableColumn
etsysStpDiagCistPortMstCistTcTx = _EtsysStpDiagCistPortMstCistTcTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 15),
    _EtsysStpDiagCistPortMstCistTcTx_Type()
)
etsysStpDiagCistPortMstCistTcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortMstCistTcTx.setStatus("current")
_EtsysStpDiagCistPortExpiration_Type = Counter32
_EtsysStpDiagCistPortExpiration_Object = MibTableColumn
etsysStpDiagCistPortExpiration = _EtsysStpDiagCistPortExpiration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 16),
    _EtsysStpDiagCistPortExpiration_Type()
)
etsysStpDiagCistPortExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortExpiration.setStatus("current")
_EtsysStpDiagCistPortStpCfgBpduRxTcFlagSet_Type = Counter32
_EtsysStpDiagCistPortStpCfgBpduRxTcFlagSet_Object = MibTableColumn
etsysStpDiagCistPortStpCfgBpduRxTcFlagSet = _EtsysStpDiagCistPortStpCfgBpduRxTcFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 17),
    _EtsysStpDiagCistPortStpCfgBpduRxTcFlagSet_Type()
)
etsysStpDiagCistPortStpCfgBpduRxTcFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortStpCfgBpduRxTcFlagSet.setStatus("current")
_EtsysStpDiagCistPortStpCfgBpduTxTcFlagSet_Type = Counter32
_EtsysStpDiagCistPortStpCfgBpduTxTcFlagSet_Object = MibTableColumn
etsysStpDiagCistPortStpCfgBpduTxTcFlagSet = _EtsysStpDiagCistPortStpCfgBpduTxTcFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 18),
    _EtsysStpDiagCistPortStpCfgBpduTxTcFlagSet_Type()
)
etsysStpDiagCistPortStpCfgBpduTxTcFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortStpCfgBpduTxTcFlagSet.setStatus("current")
_EtsysStpDiagCistPortDisputedBpdu_Type = Counter32
_EtsysStpDiagCistPortDisputedBpdu_Object = MibTableColumn
etsysStpDiagCistPortDisputedBpdu = _EtsysStpDiagCistPortDisputedBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 1, 1, 19),
    _EtsysStpDiagCistPortDisputedBpdu_Type()
)
etsysStpDiagCistPortDisputedBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistPortDisputedBpdu.setStatus("current")
_EtsysStpDiagCistBridgePortTable_Object = MibTable
etsysStpDiagCistBridgePortTable = _EtsysStpDiagCistBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2)
)
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortTable.setStatus("current")
_EtsysStpDiagCistBridgePortEntry_Object = MibTableRow
etsysStpDiagCistBridgePortEntry = _EtsysStpDiagCistBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortEntry.setStatus("current")
_EtsysStpDiagCistBridgePortRole_Type = EtsysStpPortRole
_EtsysStpDiagCistBridgePortRole_Object = MibTableColumn
etsysStpDiagCistBridgePortRole = _EtsysStpDiagCistBridgePortRole_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 2),
    _EtsysStpDiagCistBridgePortRole_Type()
)
etsysStpDiagCistBridgePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortRole.setStatus("current")
_EtsysStpDiagCistBridgePortInvalidBpdu_Type = Counter32
_EtsysStpDiagCistBridgePortInvalidBpdu_Object = MibTableColumn
etsysStpDiagCistBridgePortInvalidBpdu = _EtsysStpDiagCistBridgePortInvalidBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 3),
    _EtsysStpDiagCistBridgePortInvalidBpdu_Type()
)
etsysStpDiagCistBridgePortInvalidBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortInvalidBpdu.setStatus("current")
_EtsysStpDiagCistBridgePortStpCfgBpduRx_Type = Counter32
_EtsysStpDiagCistBridgePortStpCfgBpduRx_Object = MibTableColumn
etsysStpDiagCistBridgePortStpCfgBpduRx = _EtsysStpDiagCistBridgePortStpCfgBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 4),
    _EtsysStpDiagCistBridgePortStpCfgBpduRx_Type()
)
etsysStpDiagCistBridgePortStpCfgBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortStpCfgBpduRx.setStatus("current")
_EtsysStpDiagCistBridgePortStpCfgBpduTx_Type = Counter32
_EtsysStpDiagCistBridgePortStpCfgBpduTx_Object = MibTableColumn
etsysStpDiagCistBridgePortStpCfgBpduTx = _EtsysStpDiagCistBridgePortStpCfgBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 5),
    _EtsysStpDiagCistBridgePortStpCfgBpduTx_Type()
)
etsysStpDiagCistBridgePortStpCfgBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortStpCfgBpduTx.setStatus("current")
_EtsysStpDiagCistBridgePortStpTcnBpduRx_Type = Counter32
_EtsysStpDiagCistBridgePortStpTcnBpduRx_Object = MibTableColumn
etsysStpDiagCistBridgePortStpTcnBpduRx = _EtsysStpDiagCistBridgePortStpTcnBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 6),
    _EtsysStpDiagCistBridgePortStpTcnBpduRx_Type()
)
etsysStpDiagCistBridgePortStpTcnBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortStpTcnBpduRx.setStatus("current")
_EtsysStpDiagCistBridgePortStpTcnBpduTx_Type = Counter32
_EtsysStpDiagCistBridgePortStpTcnBpduTx_Object = MibTableColumn
etsysStpDiagCistBridgePortStpTcnBpduTx = _EtsysStpDiagCistBridgePortStpTcnBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 7),
    _EtsysStpDiagCistBridgePortStpTcnBpduTx_Type()
)
etsysStpDiagCistBridgePortStpTcnBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortStpTcnBpduTx.setStatus("current")
_EtsysStpDiagCistBridgePortRstBpduRx_Type = Counter32
_EtsysStpDiagCistBridgePortRstBpduRx_Object = MibTableColumn
etsysStpDiagCistBridgePortRstBpduRx = _EtsysStpDiagCistBridgePortRstBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 8),
    _EtsysStpDiagCistBridgePortRstBpduRx_Type()
)
etsysStpDiagCistBridgePortRstBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortRstBpduRx.setStatus("current")
_EtsysStpDiagCistBridgePortRstBpduTx_Type = Counter32
_EtsysStpDiagCistBridgePortRstBpduTx_Object = MibTableColumn
etsysStpDiagCistBridgePortRstBpduTx = _EtsysStpDiagCistBridgePortRstBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 9),
    _EtsysStpDiagCistBridgePortRstBpduTx_Type()
)
etsysStpDiagCistBridgePortRstBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortRstBpduTx.setStatus("current")
_EtsysStpDiagCistBridgePortRstTcRx_Type = Counter32
_EtsysStpDiagCistBridgePortRstTcRx_Object = MibTableColumn
etsysStpDiagCistBridgePortRstTcRx = _EtsysStpDiagCistBridgePortRstTcRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 10),
    _EtsysStpDiagCistBridgePortRstTcRx_Type()
)
etsysStpDiagCistBridgePortRstTcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortRstTcRx.setStatus("current")
_EtsysStpDiagCistBridgePortRstTcTx_Type = Counter32
_EtsysStpDiagCistBridgePortRstTcTx_Object = MibTableColumn
etsysStpDiagCistBridgePortRstTcTx = _EtsysStpDiagCistBridgePortRstTcTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 11),
    _EtsysStpDiagCistBridgePortRstTcTx_Type()
)
etsysStpDiagCistBridgePortRstTcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortRstTcTx.setStatus("current")
_EtsysStpDiagCistBridgePortMstBpduRx_Type = Counter32
_EtsysStpDiagCistBridgePortMstBpduRx_Object = MibTableColumn
etsysStpDiagCistBridgePortMstBpduRx = _EtsysStpDiagCistBridgePortMstBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 12),
    _EtsysStpDiagCistBridgePortMstBpduRx_Type()
)
etsysStpDiagCistBridgePortMstBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortMstBpduRx.setStatus("current")
_EtsysStpDiagCistBridgePortMstBpduTx_Type = Counter32
_EtsysStpDiagCistBridgePortMstBpduTx_Object = MibTableColumn
etsysStpDiagCistBridgePortMstBpduTx = _EtsysStpDiagCistBridgePortMstBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 13),
    _EtsysStpDiagCistBridgePortMstBpduTx_Type()
)
etsysStpDiagCistBridgePortMstBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortMstBpduTx.setStatus("current")
_EtsysStpDiagCistBridgePortMstCistTcRx_Type = Counter32
_EtsysStpDiagCistBridgePortMstCistTcRx_Object = MibTableColumn
etsysStpDiagCistBridgePortMstCistTcRx = _EtsysStpDiagCistBridgePortMstCistTcRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 14),
    _EtsysStpDiagCistBridgePortMstCistTcRx_Type()
)
etsysStpDiagCistBridgePortMstCistTcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortMstCistTcRx.setStatus("current")
_EtsysStpDiagCistBridgePortMstCistTcTx_Type = Counter32
_EtsysStpDiagCistBridgePortMstCistTcTx_Object = MibTableColumn
etsysStpDiagCistBridgePortMstCistTcTx = _EtsysStpDiagCistBridgePortMstCistTcTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 15),
    _EtsysStpDiagCistBridgePortMstCistTcTx_Type()
)
etsysStpDiagCistBridgePortMstCistTcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortMstCistTcTx.setStatus("current")
_EtsysStpDiagCistBridgePortExpiration_Type = Counter32
_EtsysStpDiagCistBridgePortExpiration_Object = MibTableColumn
etsysStpDiagCistBridgePortExpiration = _EtsysStpDiagCistBridgePortExpiration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 16),
    _EtsysStpDiagCistBridgePortExpiration_Type()
)
etsysStpDiagCistBridgePortExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortExpiration.setStatus("current")
_EtsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet_Type = Counter32
_EtsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet_Object = MibTableColumn
etsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet = _EtsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 17),
    _EtsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet_Type()
)
etsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet.setStatus("current")
_EtsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet_Type = Counter32
_EtsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet_Object = MibTableColumn
etsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet = _EtsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 18),
    _EtsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet_Type()
)
etsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet.setStatus("current")
_EtsysStpDiagCistBridgePortDisputedBpdu_Type = Counter32
_EtsysStpDiagCistBridgePortDisputedBpdu_Object = MibTableColumn
etsysStpDiagCistBridgePortDisputedBpdu = _EtsysStpDiagCistBridgePortDisputedBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 3, 2, 1, 19),
    _EtsysStpDiagCistBridgePortDisputedBpdu_Type()
)
etsysStpDiagCistBridgePortDisputedBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagCistBridgePortDisputedBpdu.setStatus("current")
_EtsysStpDiagMsti_ObjectIdentity = ObjectIdentity
etsysStpDiagMsti = _EtsysStpDiagMsti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4)
)
_EtsysStpDiagMstiTable_Object = MibTable
etsysStpDiagMstiTable = _EtsysStpDiagMstiTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysStpDiagMstiTable.setStatus("current")
_EtsysStpDiagMstiEntry_Object = MibTableRow
etsysStpDiagMstiEntry = _EtsysStpDiagMstiEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4, 1, 1)
)
etsysStpDiagMstiEntry.setIndexNames(
    (0, "ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiId"),
)
if mibBuilder.loadTexts:
    etsysStpDiagMstiEntry.setStatus("current")


class _EtsysStpDiagMstiId_Type(Unsigned32):
    """Custom type etsysStpDiagMstiId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EtsysStpDiagMstiId_Type.__name__ = "Unsigned32"
_EtsysStpDiagMstiId_Object = MibTableColumn
etsysStpDiagMstiId = _EtsysStpDiagMstiId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4, 1, 1, 1),
    _EtsysStpDiagMstiId_Type()
)
etsysStpDiagMstiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiId.setStatus("current")
_EtsysStpDiagMstiTopChanges_Type = Counter32
_EtsysStpDiagMstiTopChanges_Object = MibTableColumn
etsysStpDiagMstiTopChanges = _EtsysStpDiagMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4, 1, 1, 2),
    _EtsysStpDiagMstiTopChanges_Type()
)
etsysStpDiagMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiTopChanges.setStatus("current")
_EtsysStpDiagMstiConfigMsgRx_Type = Counter32
_EtsysStpDiagMstiConfigMsgRx_Object = MibTableColumn
etsysStpDiagMstiConfigMsgRx = _EtsysStpDiagMstiConfigMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4, 1, 1, 3),
    _EtsysStpDiagMstiConfigMsgRx_Type()
)
etsysStpDiagMstiConfigMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiConfigMsgRx.setStatus("current")
_EtsysStpDiagMstiConfigMsgTx_Type = Counter32
_EtsysStpDiagMstiConfigMsgTx_Object = MibTableColumn
etsysStpDiagMstiConfigMsgTx = _EtsysStpDiagMstiConfigMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4, 1, 1, 4),
    _EtsysStpDiagMstiConfigMsgTx_Type()
)
etsysStpDiagMstiConfigMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiConfigMsgTx.setStatus("current")
_EtsysStpDiagMstiTcRx_Type = Counter32
_EtsysStpDiagMstiTcRx_Object = MibTableColumn
etsysStpDiagMstiTcRx = _EtsysStpDiagMstiTcRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4, 1, 1, 5),
    _EtsysStpDiagMstiTcRx_Type()
)
etsysStpDiagMstiTcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiTcRx.setStatus("current")
_EtsysStpDiagMstiTcTx_Type = Counter32
_EtsysStpDiagMstiTcTx_Object = MibTableColumn
etsysStpDiagMstiTcTx = _EtsysStpDiagMstiTcTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4, 1, 1, 6),
    _EtsysStpDiagMstiTcTx_Type()
)
etsysStpDiagMstiTcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiTcTx.setStatus("current")
_EtsysStpDiagMstiDisputedBpdu_Type = Counter32
_EtsysStpDiagMstiDisputedBpdu_Object = MibTableColumn
etsysStpDiagMstiDisputedBpdu = _EtsysStpDiagMstiDisputedBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 4, 1, 1, 7),
    _EtsysStpDiagMstiDisputedBpdu_Type()
)
etsysStpDiagMstiDisputedBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiDisputedBpdu.setStatus("current")
_EtsysStpDiagMstiPort_ObjectIdentity = ObjectIdentity
etsysStpDiagMstiPort = _EtsysStpDiagMstiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5)
)
_EtsysStpDiagMstiPortTable_Object = MibTable
etsysStpDiagMstiPortTable = _EtsysStpDiagMstiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1)
)
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortTable.setStatus("current")
_EtsysStpDiagMstiPortEntry_Object = MibTableRow
etsysStpDiagMstiPortEntry = _EtsysStpDiagMstiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1, 1)
)
etsysStpDiagMstiPortEntry.setIndexNames(
    (0, "ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortMstiId"),
    (0, "ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortNumber"),
)
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortEntry.setStatus("current")


class _EtsysStpDiagMstiPortMstiId_Type(Unsigned32):
    """Custom type etsysStpDiagMstiPortMstiId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EtsysStpDiagMstiPortMstiId_Type.__name__ = "Unsigned32"
_EtsysStpDiagMstiPortMstiId_Object = MibTableColumn
etsysStpDiagMstiPortMstiId = _EtsysStpDiagMstiPortMstiId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1, 1, 1),
    _EtsysStpDiagMstiPortMstiId_Type()
)
etsysStpDiagMstiPortMstiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortMstiId.setStatus("current")
_EtsysStpDiagMstiPortNumber_Type = InterfaceIndex
_EtsysStpDiagMstiPortNumber_Object = MibTableColumn
etsysStpDiagMstiPortNumber = _EtsysStpDiagMstiPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1, 1, 2),
    _EtsysStpDiagMstiPortNumber_Type()
)
etsysStpDiagMstiPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortNumber.setStatus("current")
_EtsysStpDiagMstiPortTopChanges_Type = Counter32
_EtsysStpDiagMstiPortTopChanges_Object = MibTableColumn
etsysStpDiagMstiPortTopChanges = _EtsysStpDiagMstiPortTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1, 1, 3),
    _EtsysStpDiagMstiPortTopChanges_Type()
)
etsysStpDiagMstiPortTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortTopChanges.setStatus("deprecated")
_EtsysStpDiagMstiPortConfigMsgRx_Type = Counter32
_EtsysStpDiagMstiPortConfigMsgRx_Object = MibTableColumn
etsysStpDiagMstiPortConfigMsgRx = _EtsysStpDiagMstiPortConfigMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1, 1, 4),
    _EtsysStpDiagMstiPortConfigMsgRx_Type()
)
etsysStpDiagMstiPortConfigMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortConfigMsgRx.setStatus("current")
_EtsysStpDiagMstiPortConfigMsgTx_Type = Counter32
_EtsysStpDiagMstiPortConfigMsgTx_Object = MibTableColumn
etsysStpDiagMstiPortConfigMsgTx = _EtsysStpDiagMstiPortConfigMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1, 1, 5),
    _EtsysStpDiagMstiPortConfigMsgTx_Type()
)
etsysStpDiagMstiPortConfigMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortConfigMsgTx.setStatus("current")
_EtsysStpDiagMstiPortTcRx_Type = Counter32
_EtsysStpDiagMstiPortTcRx_Object = MibTableColumn
etsysStpDiagMstiPortTcRx = _EtsysStpDiagMstiPortTcRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1, 1, 6),
    _EtsysStpDiagMstiPortTcRx_Type()
)
etsysStpDiagMstiPortTcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortTcRx.setStatus("current")
_EtsysStpDiagMstiPortTcTx_Type = Counter32
_EtsysStpDiagMstiPortTcTx_Object = MibTableColumn
etsysStpDiagMstiPortTcTx = _EtsysStpDiagMstiPortTcTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1, 1, 7),
    _EtsysStpDiagMstiPortTcTx_Type()
)
etsysStpDiagMstiPortTcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortTcTx.setStatus("current")
_EtsysStpDiagMstiPortDisputedBpdu_Type = Counter32
_EtsysStpDiagMstiPortDisputedBpdu_Object = MibTableColumn
etsysStpDiagMstiPortDisputedBpdu = _EtsysStpDiagMstiPortDisputedBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 1, 1, 8),
    _EtsysStpDiagMstiPortDisputedBpdu_Type()
)
etsysStpDiagMstiPortDisputedBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiPortDisputedBpdu.setStatus("current")
_EtsysStpDiagMstiBridgePortTable_Object = MibTable
etsysStpDiagMstiBridgePortTable = _EtsysStpDiagMstiBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 2)
)
if mibBuilder.loadTexts:
    etsysStpDiagMstiBridgePortTable.setStatus("current")
_EtsysStpDiagMstiBridgePortEntry_Object = MibTableRow
etsysStpDiagMstiBridgePortEntry = _EtsysStpDiagMstiBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 2, 1)
)
etsysStpDiagMstiBridgePortEntry.setIndexNames(
    (0, "ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortMstiId"),
    (0, "BRIDGE-MIB", "dot1dStpPort"),
)
if mibBuilder.loadTexts:
    etsysStpDiagMstiBridgePortEntry.setStatus("current")


class _EtsysStpDiagMstiBridgePortMstiId_Type(Unsigned32):
    """Custom type etsysStpDiagMstiBridgePortMstiId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EtsysStpDiagMstiBridgePortMstiId_Type.__name__ = "Unsigned32"
_EtsysStpDiagMstiBridgePortMstiId_Object = MibTableColumn
etsysStpDiagMstiBridgePortMstiId = _EtsysStpDiagMstiBridgePortMstiId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 2, 1, 1),
    _EtsysStpDiagMstiBridgePortMstiId_Type()
)
etsysStpDiagMstiBridgePortMstiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiBridgePortMstiId.setStatus("current")
_EtsysStpDiagMstiBridgePortRole_Type = EtsysStpPortRole
_EtsysStpDiagMstiBridgePortRole_Object = MibTableColumn
etsysStpDiagMstiBridgePortRole = _EtsysStpDiagMstiBridgePortRole_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 2, 1, 3),
    _EtsysStpDiagMstiBridgePortRole_Type()
)
etsysStpDiagMstiBridgePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiBridgePortRole.setStatus("current")
_EtsysStpDiagMstiBridgePortConfigMsgRx_Type = Counter32
_EtsysStpDiagMstiBridgePortConfigMsgRx_Object = MibTableColumn
etsysStpDiagMstiBridgePortConfigMsgRx = _EtsysStpDiagMstiBridgePortConfigMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 2, 1, 4),
    _EtsysStpDiagMstiBridgePortConfigMsgRx_Type()
)
etsysStpDiagMstiBridgePortConfigMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiBridgePortConfigMsgRx.setStatus("current")
_EtsysStpDiagMstiBridgePortConfigMsgTx_Type = Counter32
_EtsysStpDiagMstiBridgePortConfigMsgTx_Object = MibTableColumn
etsysStpDiagMstiBridgePortConfigMsgTx = _EtsysStpDiagMstiBridgePortConfigMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 2, 1, 5),
    _EtsysStpDiagMstiBridgePortConfigMsgTx_Type()
)
etsysStpDiagMstiBridgePortConfigMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiBridgePortConfigMsgTx.setStatus("current")
_EtsysStpDiagMstiBridgePortTcRx_Type = Counter32
_EtsysStpDiagMstiBridgePortTcRx_Object = MibTableColumn
etsysStpDiagMstiBridgePortTcRx = _EtsysStpDiagMstiBridgePortTcRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 2, 1, 6),
    _EtsysStpDiagMstiBridgePortTcRx_Type()
)
etsysStpDiagMstiBridgePortTcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiBridgePortTcRx.setStatus("current")
_EtsysStpDiagMstiBridgePortTcTx_Type = Counter32
_EtsysStpDiagMstiBridgePortTcTx_Object = MibTableColumn
etsysStpDiagMstiBridgePortTcTx = _EtsysStpDiagMstiBridgePortTcTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 2, 1, 7),
    _EtsysStpDiagMstiBridgePortTcTx_Type()
)
etsysStpDiagMstiBridgePortTcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiBridgePortTcTx.setStatus("current")
_EtsysStpDiagMstiBridgePortDisputedBpdu_Type = Counter32
_EtsysStpDiagMstiBridgePortDisputedBpdu_Object = MibTableColumn
etsysStpDiagMstiBridgePortDisputedBpdu = _EtsysStpDiagMstiBridgePortDisputedBpdu_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 5, 2, 1, 8),
    _EtsysStpDiagMstiBridgePortDisputedBpdu_Type()
)
etsysStpDiagMstiBridgePortDisputedBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagMstiBridgePortDisputedBpdu.setStatus("current")
_EtsysStpDiagRootHistory_ObjectIdentity = ObjectIdentity
etsysStpDiagRootHistory = _EtsysStpDiagRootHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 6)
)
_EtsysStpDiagRootHistoryTable_Object = MibTable
etsysStpDiagRootHistoryTable = _EtsysStpDiagRootHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 6, 1)
)
if mibBuilder.loadTexts:
    etsysStpDiagRootHistoryTable.setStatus("current")
_EtsysStpDiagRootHistoryEntry_Object = MibTableRow
etsysStpDiagRootHistoryEntry = _EtsysStpDiagRootHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 6, 1, 1)
)
etsysStpDiagRootHistoryEntry.setIndexNames(
    (0, "ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagRootHistoryStpID"),
    (0, "ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagRootHistoryIndex"),
)
if mibBuilder.loadTexts:
    etsysStpDiagRootHistoryEntry.setStatus("current")


class _EtsysStpDiagRootHistoryStpID_Type(Unsigned32):
    """Custom type etsysStpDiagRootHistoryStpID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_EtsysStpDiagRootHistoryStpID_Type.__name__ = "Unsigned32"
_EtsysStpDiagRootHistoryStpID_Object = MibTableColumn
etsysStpDiagRootHistoryStpID = _EtsysStpDiagRootHistoryStpID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 6, 1, 1, 1),
    _EtsysStpDiagRootHistoryStpID_Type()
)
etsysStpDiagRootHistoryStpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagRootHistoryStpID.setStatus("current")


class _EtsysStpDiagRootHistoryIndex_Type(Unsigned32):
    """Custom type etsysStpDiagRootHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EtsysStpDiagRootHistoryIndex_Type.__name__ = "Unsigned32"
_EtsysStpDiagRootHistoryIndex_Object = MibTableColumn
etsysStpDiagRootHistoryIndex = _EtsysStpDiagRootHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 6, 1, 1, 2),
    _EtsysStpDiagRootHistoryIndex_Type()
)
etsysStpDiagRootHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagRootHistoryIndex.setStatus("current")
_EtsysStpDiagRootHistoryBridgeID_Type = BridgeId
_EtsysStpDiagRootHistoryBridgeID_Object = MibTableColumn
etsysStpDiagRootHistoryBridgeID = _EtsysStpDiagRootHistoryBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 6, 1, 1, 3),
    _EtsysStpDiagRootHistoryBridgeID_Type()
)
etsysStpDiagRootHistoryBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagRootHistoryBridgeID.setStatus("current")
_EtsysStpDiagRootHistoryDateAndTime_Type = DateAndTime
_EtsysStpDiagRootHistoryDateAndTime_Object = MibTableColumn
etsysStpDiagRootHistoryDateAndTime = _EtsysStpDiagRootHistoryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 6, 1, 1, 4),
    _EtsysStpDiagRootHistoryDateAndTime_Type()
)
etsysStpDiagRootHistoryDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStpDiagRootHistoryDateAndTime.setStatus("current")
_EtsysStpDiagTrapConfig_ObjectIdentity = ObjectIdentity
etsysStpDiagTrapConfig = _EtsysStpDiagTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 7)
)


class _EtsysStpDiagDisputedBpduTrapThreshold_Type(Unsigned32):
    """Custom type etsysStpDiagDisputedBpduTrapThreshold based on Unsigned32"""
    defaultValue = 0


_EtsysStpDiagDisputedBpduTrapThreshold_Object = MibScalar
etsysStpDiagDisputedBpduTrapThreshold = _EtsysStpDiagDisputedBpduTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 7, 1),
    _EtsysStpDiagDisputedBpduTrapThreshold_Type()
)
etsysStpDiagDisputedBpduTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysStpDiagDisputedBpduTrapThreshold.setStatus("current")
_EtsysStpDiagConformance_ObjectIdentity = ObjectIdentity
etsysStpDiagConformance = _EtsysStpDiagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2)
)
_EtsysStpDiagGroups_ObjectIdentity = ObjectIdentity
etsysStpDiagGroups = _EtsysStpDiagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1)
)
_EtsysStpDiagCompliances_ObjectIdentity = ObjectIdentity
etsysStpDiagCompliances = _EtsysStpDiagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 2)
)
dot1dStpPortEntry.registerAugmentions(
    ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB",
     "etsysStpDiagCistBridgePortEntry")
)
etsysStpDiagCistBridgePortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups

etsysStpDiagDot1dGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1, 1)
)
etsysStpDiagDot1dGroup.setObjects(
      *(("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCounterReset"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCounterResetElapsedTime"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCounterResetDateAndTime"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagTopChanges"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonInvalidBpdu"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonStpCfgBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonStpCfgBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonStpTcnBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonStpTcnBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonStpCfgBpduRxTcFlagSet"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonStpCfgBpduTxTcFlagSet"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonDisputedBpdu"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMessageExpiration"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortNumber"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortRole"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortInvalidBpdu"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortStpCfgBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortStpCfgBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortStpTcnBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortStpTcnBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortStpCfgBpduRxTcFlagSet"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortStpCfgBpduTxTcFlagSet"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortDisputedBpdu"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortExpiration"))
)
if mibBuilder.loadTexts:
    etsysStpDiagDot1dGroup.setStatus("current")

etsysStpDiagDot1wGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1, 2)
)
etsysStpDiagDot1wGroup.setObjects(
      *(("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonRstBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonRstBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonRstTcRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonRstTcTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortRstBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortRstBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortRstTcRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortRstTcTx"))
)
if mibBuilder.loadTexts:
    etsysStpDiagDot1wGroup.setStatus("current")

etsysStpDiagDot1sGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1, 3)
)
etsysStpDiagDot1sGroup.setObjects(
      *(("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonMstBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonMstBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonMstCistTcRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCommonMstCistTcTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortMstBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortMstBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortMstCistTcRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistPortMstCistTcTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortMstBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortMstBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortMstCistTcRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortMstCistTcTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiId"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiTopChanges"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiConfigMsgRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiConfigMsgTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiTcRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiTcTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiDisputedBpdu"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortMstiId"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortNumber"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortTopChanges"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortConfigMsgRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortConfigMsgTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortTcRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortTcTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiPortDisputedBpdu"))
)
if mibBuilder.loadTexts:
    etsysStpDiagDot1sGroup.setStatus("current")

etsysStpDiagHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1, 4)
)
etsysStpDiagHistoryGroup.setObjects(
      *(("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagRootHistoryStpID"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagRootHistoryIndex"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagRootHistoryBridgeID"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagRootHistoryDateAndTime"))
)
if mibBuilder.loadTexts:
    etsysStpDiagHistoryGroup.setStatus("current")

etsysStpDiagDot1dBridgePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1, 5)
)
etsysStpDiagDot1dBridgePortGroup.setObjects(
      *(("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortRole"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortInvalidBpdu"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortStpCfgBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortStpCfgBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortStpTcnBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortStpTcnBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortDisputedBpdu"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortExpiration"))
)
if mibBuilder.loadTexts:
    etsysStpDiagDot1dBridgePortGroup.setStatus("current")

etsysStpDiagDot1wBridgePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1, 6)
)
etsysStpDiagDot1wBridgePortGroup.setObjects(
      *(("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortRstBpduRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortRstBpduTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortRstTcRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortRstTcTx"))
)
if mibBuilder.loadTexts:
    etsysStpDiagDot1wBridgePortGroup.setStatus("current")

etsysStpDiagDot1sBridgePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1, 7)
)
etsysStpDiagDot1sBridgePortGroup.setObjects(
      *(("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortMstiId"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortRole"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortConfigMsgRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortConfigMsgTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortTcRx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortTcTx"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortDisputedBpdu"))
)
if mibBuilder.loadTexts:
    etsysStpDiagDot1sBridgePortGroup.setStatus("current")

etsysStpDiagTrapConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1, 8)
)
etsysStpDiagTrapConfigGroup.setObjects(
    ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagDisputedBpduTrapThreshold")
)
if mibBuilder.loadTexts:
    etsysStpDiagTrapConfigGroup.setStatus("current")


# Notification objects

etsysStpDiagCistDisputedBpduThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 0, 1)
)
etsysStpDiagCistDisputedBpduThresholdExceeded.setObjects(
      *(("BRIDGE-MIB", "dot1dStpPort"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistBridgePortDisputedBpdu"))
)
if mibBuilder.loadTexts:
    etsysStpDiagCistDisputedBpduThresholdExceeded.setStatus(
        "current"
    )

etsysStpDiagMstiDisputedBpduThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 1, 0, 2)
)
etsysStpDiagMstiDisputedBpduThresholdExceeded.setObjects(
      *(("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortMstiId"),
        ("BRIDGE-MIB", "dot1dStpPort"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiBridgePortDisputedBpdu"))
)
if mibBuilder.loadTexts:
    etsysStpDiagMstiDisputedBpduThresholdExceeded.setStatus(
        "current"
    )


# Notifications groups

etsysStpDiagNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 1, 9)
)
etsysStpDiagNotificationGroup.setObjects(
      *(("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagCistDisputedBpduThresholdExceeded"),
        ("ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB", "etsysStpDiagMstiDisputedBpduThresholdExceeded"))
)
if mibBuilder.loadTexts:
    etsysStpDiagNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysStpDiagCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 29, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysStpDiagCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-SPANNING-TREE-DIAGNOSTIC-MIB",
    **{"EtsysStpPortRole": EtsysStpPortRole,
       "etsysSpanningTreeDiagnosticMIB": etsysSpanningTreeDiagnosticMIB,
       "etsysStpDiagObjects": etsysStpDiagObjects,
       "etsysStpDiagNotifications": etsysStpDiagNotifications,
       "etsysStpDiagCistDisputedBpduThresholdExceeded": etsysStpDiagCistDisputedBpduThresholdExceeded,
       "etsysStpDiagMstiDisputedBpduThresholdExceeded": etsysStpDiagMstiDisputedBpduThresholdExceeded,
       "etsysStpDiagControl": etsysStpDiagControl,
       "etsysStpDiagCounterReset": etsysStpDiagCounterReset,
       "etsysStpDiagCounterResetElapsedTime": etsysStpDiagCounterResetElapsedTime,
       "etsysStpDiagCounterResetDateAndTime": etsysStpDiagCounterResetDateAndTime,
       "etsysStpDiagCommon": etsysStpDiagCommon,
       "etsysStpDiagTopChanges": etsysStpDiagTopChanges,
       "etsysStpDiagCommonInvalidBpdu": etsysStpDiagCommonInvalidBpdu,
       "etsysStpDiagCommonStpCfgBpduRx": etsysStpDiagCommonStpCfgBpduRx,
       "etsysStpDiagCommonStpCfgBpduTx": etsysStpDiagCommonStpCfgBpduTx,
       "etsysStpDiagCommonStpTcnBpduRx": etsysStpDiagCommonStpTcnBpduRx,
       "etsysStpDiagCommonStpTcnBpduTx": etsysStpDiagCommonStpTcnBpduTx,
       "etsysStpDiagCommonRstBpduRx": etsysStpDiagCommonRstBpduRx,
       "etsysStpDiagCommonRstBpduTx": etsysStpDiagCommonRstBpduTx,
       "etsysStpDiagCommonRstTcRx": etsysStpDiagCommonRstTcRx,
       "etsysStpDiagCommonRstTcTx": etsysStpDiagCommonRstTcTx,
       "etsysStpDiagCommonMstBpduRx": etsysStpDiagCommonMstBpduRx,
       "etsysStpDiagCommonMstBpduTx": etsysStpDiagCommonMstBpduTx,
       "etsysStpDiagCommonMstCistTcRx": etsysStpDiagCommonMstCistTcRx,
       "etsysStpDiagCommonMstCistTcTx": etsysStpDiagCommonMstCistTcTx,
       "etsysStpDiagCommonStpCfgBpduRxTcFlagSet": etsysStpDiagCommonStpCfgBpduRxTcFlagSet,
       "etsysStpDiagCommonStpCfgBpduTxTcFlagSet": etsysStpDiagCommonStpCfgBpduTxTcFlagSet,
       "etsysStpDiagCommonDisputedBpdu": etsysStpDiagCommonDisputedBpdu,
       "etsysStpDiagMessageExpiration": etsysStpDiagMessageExpiration,
       "etsysStpDiagCistPort": etsysStpDiagCistPort,
       "etsysStpDiagCistPortTable": etsysStpDiagCistPortTable,
       "etsysStpDiagCistPortEntry": etsysStpDiagCistPortEntry,
       "etsysStpDiagCistPortNumber": etsysStpDiagCistPortNumber,
       "etsysStpDiagCistPortRole": etsysStpDiagCistPortRole,
       "etsysStpDiagCistPortInvalidBpdu": etsysStpDiagCistPortInvalidBpdu,
       "etsysStpDiagCistPortStpCfgBpduRx": etsysStpDiagCistPortStpCfgBpduRx,
       "etsysStpDiagCistPortStpCfgBpduTx": etsysStpDiagCistPortStpCfgBpduTx,
       "etsysStpDiagCistPortStpTcnBpduRx": etsysStpDiagCistPortStpTcnBpduRx,
       "etsysStpDiagCistPortStpTcnBpduTx": etsysStpDiagCistPortStpTcnBpduTx,
       "etsysStpDiagCistPortRstBpduRx": etsysStpDiagCistPortRstBpduRx,
       "etsysStpDiagCistPortRstBpduTx": etsysStpDiagCistPortRstBpduTx,
       "etsysStpDiagCistPortRstTcRx": etsysStpDiagCistPortRstTcRx,
       "etsysStpDiagCistPortRstTcTx": etsysStpDiagCistPortRstTcTx,
       "etsysStpDiagCistPortMstBpduRx": etsysStpDiagCistPortMstBpduRx,
       "etsysStpDiagCistPortMstBpduTx": etsysStpDiagCistPortMstBpduTx,
       "etsysStpDiagCistPortMstCistTcRx": etsysStpDiagCistPortMstCistTcRx,
       "etsysStpDiagCistPortMstCistTcTx": etsysStpDiagCistPortMstCistTcTx,
       "etsysStpDiagCistPortExpiration": etsysStpDiagCistPortExpiration,
       "etsysStpDiagCistPortStpCfgBpduRxTcFlagSet": etsysStpDiagCistPortStpCfgBpduRxTcFlagSet,
       "etsysStpDiagCistPortStpCfgBpduTxTcFlagSet": etsysStpDiagCistPortStpCfgBpduTxTcFlagSet,
       "etsysStpDiagCistPortDisputedBpdu": etsysStpDiagCistPortDisputedBpdu,
       "etsysStpDiagCistBridgePortTable": etsysStpDiagCistBridgePortTable,
       "etsysStpDiagCistBridgePortEntry": etsysStpDiagCistBridgePortEntry,
       "etsysStpDiagCistBridgePortRole": etsysStpDiagCistBridgePortRole,
       "etsysStpDiagCistBridgePortInvalidBpdu": etsysStpDiagCistBridgePortInvalidBpdu,
       "etsysStpDiagCistBridgePortStpCfgBpduRx": etsysStpDiagCistBridgePortStpCfgBpduRx,
       "etsysStpDiagCistBridgePortStpCfgBpduTx": etsysStpDiagCistBridgePortStpCfgBpduTx,
       "etsysStpDiagCistBridgePortStpTcnBpduRx": etsysStpDiagCistBridgePortStpTcnBpduRx,
       "etsysStpDiagCistBridgePortStpTcnBpduTx": etsysStpDiagCistBridgePortStpTcnBpduTx,
       "etsysStpDiagCistBridgePortRstBpduRx": etsysStpDiagCistBridgePortRstBpduRx,
       "etsysStpDiagCistBridgePortRstBpduTx": etsysStpDiagCistBridgePortRstBpduTx,
       "etsysStpDiagCistBridgePortRstTcRx": etsysStpDiagCistBridgePortRstTcRx,
       "etsysStpDiagCistBridgePortRstTcTx": etsysStpDiagCistBridgePortRstTcTx,
       "etsysStpDiagCistBridgePortMstBpduRx": etsysStpDiagCistBridgePortMstBpduRx,
       "etsysStpDiagCistBridgePortMstBpduTx": etsysStpDiagCistBridgePortMstBpduTx,
       "etsysStpDiagCistBridgePortMstCistTcRx": etsysStpDiagCistBridgePortMstCistTcRx,
       "etsysStpDiagCistBridgePortMstCistTcTx": etsysStpDiagCistBridgePortMstCistTcTx,
       "etsysStpDiagCistBridgePortExpiration": etsysStpDiagCistBridgePortExpiration,
       "etsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet": etsysStpDiagCistBridgePortStpCfgBpduRxTcFlagSet,
       "etsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet": etsysStpDiagCistBridgePortStpCfgBpduTxTcFlagSet,
       "etsysStpDiagCistBridgePortDisputedBpdu": etsysStpDiagCistBridgePortDisputedBpdu,
       "etsysStpDiagMsti": etsysStpDiagMsti,
       "etsysStpDiagMstiTable": etsysStpDiagMstiTable,
       "etsysStpDiagMstiEntry": etsysStpDiagMstiEntry,
       "etsysStpDiagMstiId": etsysStpDiagMstiId,
       "etsysStpDiagMstiTopChanges": etsysStpDiagMstiTopChanges,
       "etsysStpDiagMstiConfigMsgRx": etsysStpDiagMstiConfigMsgRx,
       "etsysStpDiagMstiConfigMsgTx": etsysStpDiagMstiConfigMsgTx,
       "etsysStpDiagMstiTcRx": etsysStpDiagMstiTcRx,
       "etsysStpDiagMstiTcTx": etsysStpDiagMstiTcTx,
       "etsysStpDiagMstiDisputedBpdu": etsysStpDiagMstiDisputedBpdu,
       "etsysStpDiagMstiPort": etsysStpDiagMstiPort,
       "etsysStpDiagMstiPortTable": etsysStpDiagMstiPortTable,
       "etsysStpDiagMstiPortEntry": etsysStpDiagMstiPortEntry,
       "etsysStpDiagMstiPortMstiId": etsysStpDiagMstiPortMstiId,
       "etsysStpDiagMstiPortNumber": etsysStpDiagMstiPortNumber,
       "etsysStpDiagMstiPortTopChanges": etsysStpDiagMstiPortTopChanges,
       "etsysStpDiagMstiPortConfigMsgRx": etsysStpDiagMstiPortConfigMsgRx,
       "etsysStpDiagMstiPortConfigMsgTx": etsysStpDiagMstiPortConfigMsgTx,
       "etsysStpDiagMstiPortTcRx": etsysStpDiagMstiPortTcRx,
       "etsysStpDiagMstiPortTcTx": etsysStpDiagMstiPortTcTx,
       "etsysStpDiagMstiPortDisputedBpdu": etsysStpDiagMstiPortDisputedBpdu,
       "etsysStpDiagMstiBridgePortTable": etsysStpDiagMstiBridgePortTable,
       "etsysStpDiagMstiBridgePortEntry": etsysStpDiagMstiBridgePortEntry,
       "etsysStpDiagMstiBridgePortMstiId": etsysStpDiagMstiBridgePortMstiId,
       "etsysStpDiagMstiBridgePortRole": etsysStpDiagMstiBridgePortRole,
       "etsysStpDiagMstiBridgePortConfigMsgRx": etsysStpDiagMstiBridgePortConfigMsgRx,
       "etsysStpDiagMstiBridgePortConfigMsgTx": etsysStpDiagMstiBridgePortConfigMsgTx,
       "etsysStpDiagMstiBridgePortTcRx": etsysStpDiagMstiBridgePortTcRx,
       "etsysStpDiagMstiBridgePortTcTx": etsysStpDiagMstiBridgePortTcTx,
       "etsysStpDiagMstiBridgePortDisputedBpdu": etsysStpDiagMstiBridgePortDisputedBpdu,
       "etsysStpDiagRootHistory": etsysStpDiagRootHistory,
       "etsysStpDiagRootHistoryTable": etsysStpDiagRootHistoryTable,
       "etsysStpDiagRootHistoryEntry": etsysStpDiagRootHistoryEntry,
       "etsysStpDiagRootHistoryStpID": etsysStpDiagRootHistoryStpID,
       "etsysStpDiagRootHistoryIndex": etsysStpDiagRootHistoryIndex,
       "etsysStpDiagRootHistoryBridgeID": etsysStpDiagRootHistoryBridgeID,
       "etsysStpDiagRootHistoryDateAndTime": etsysStpDiagRootHistoryDateAndTime,
       "etsysStpDiagTrapConfig": etsysStpDiagTrapConfig,
       "etsysStpDiagDisputedBpduTrapThreshold": etsysStpDiagDisputedBpduTrapThreshold,
       "etsysStpDiagConformance": etsysStpDiagConformance,
       "etsysStpDiagGroups": etsysStpDiagGroups,
       "etsysStpDiagDot1dGroup": etsysStpDiagDot1dGroup,
       "etsysStpDiagDot1wGroup": etsysStpDiagDot1wGroup,
       "etsysStpDiagDot1sGroup": etsysStpDiagDot1sGroup,
       "etsysStpDiagHistoryGroup": etsysStpDiagHistoryGroup,
       "etsysStpDiagDot1dBridgePortGroup": etsysStpDiagDot1dBridgePortGroup,
       "etsysStpDiagDot1wBridgePortGroup": etsysStpDiagDot1wBridgePortGroup,
       "etsysStpDiagDot1sBridgePortGroup": etsysStpDiagDot1sBridgePortGroup,
       "etsysStpDiagTrapConfigGroup": etsysStpDiagTrapConfigGroup,
       "etsysStpDiagNotificationGroup": etsysStpDiagNotificationGroup,
       "etsysStpDiagCompliances": etsysStpDiagCompliances,
       "etsysStpDiagCompliance": etsysStpDiagCompliance}
)
