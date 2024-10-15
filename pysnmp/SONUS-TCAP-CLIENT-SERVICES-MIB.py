# SNMP MIB module (SONUS-TCAP-CLIENT-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-TCAP-CLIENT-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:13 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")

(PointCode,
 SonusName) = mibBuilder.importSymbols(
    "SONUS-TC",
    "PointCode",
    "SonusName")


# MODULE-IDENTITY

sonusTcapClientServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4)
)
sonusTcapClientServicesMIB.setRevisions(
        ("2000-10-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusTcapClientServicesMIBObjects_ObjectIdentity = ObjectIdentity
sonusTcapClientServicesMIBObjects = _SonusTcapClientServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1)
)
_SonusScpAdmn_ObjectIdentity = ObjectIdentity
sonusScpAdmn = _SonusScpAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1)
)
_SonusScpAdmnNextIndex_Type = Integer32
_SonusScpAdmnNextIndex_Object = MibScalar
sonusScpAdmnNextIndex = _SonusScpAdmnNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 1),
    _SonusScpAdmnNextIndex_Type()
)
sonusScpAdmnNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusScpAdmnNextIndex.setStatus("obsolete")
_SonusScpAdmnTable_Object = MibTable
sonusScpAdmnTable = _SonusScpAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusScpAdmnTable.setStatus("obsolete")
_SonusScpAdmnEntry_Object = MibTableRow
sonusScpAdmnEntry = _SonusScpAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1)
)
sonusScpAdmnEntry.setIndexNames(
    (0, "SONUS-TCAP-CLIENT-SERVICES-MIB", "sonusScpAdmnIndex"),
)
if mibBuilder.loadTexts:
    sonusScpAdmnEntry.setStatus("obsolete")
_SonusScpAdmnIndex_Type = Integer32
_SonusScpAdmnIndex_Object = MibTableColumn
sonusScpAdmnIndex = _SonusScpAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 1),
    _SonusScpAdmnIndex_Type()
)
sonusScpAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusScpAdmnIndex.setStatus("obsolete")
_SonusScpAdmnName_Type = SonusName
_SonusScpAdmnName_Object = MibTableColumn
sonusScpAdmnName = _SonusScpAdmnName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 2),
    _SonusScpAdmnName_Type()
)
sonusScpAdmnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnName.setStatus("obsolete")


class _SonusScpAdmnCarrier_Type(DisplayString):
    """Custom type sonusScpAdmnCarrier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SonusScpAdmnCarrier_Type.__name__ = "DisplayString"
_SonusScpAdmnCarrier_Object = MibTableColumn
sonusScpAdmnCarrier = _SonusScpAdmnCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 3),
    _SonusScpAdmnCarrier_Type()
)
sonusScpAdmnCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnCarrier.setStatus("obsolete")


class _SonusScpAdmnNode_Type(DisplayString):
    """Custom type sonusScpAdmnNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_SonusScpAdmnNode_Type.__name__ = "DisplayString"
_SonusScpAdmnNode_Object = MibTableColumn
sonusScpAdmnNode = _SonusScpAdmnNode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 4),
    _SonusScpAdmnNode_Type()
)
sonusScpAdmnNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnNode.setStatus("obsolete")
_SonusScpAdmnPc_Type = PointCode
_SonusScpAdmnPc_Object = MibTableColumn
sonusScpAdmnPc = _SonusScpAdmnPc_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 5),
    _SonusScpAdmnPc_Type()
)
sonusScpAdmnPc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnPc.setStatus("obsolete")
_SonusScpAdmnSsn_Type = Integer32
_SonusScpAdmnSsn_Object = MibTableColumn
sonusScpAdmnSsn = _SonusScpAdmnSsn_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 6),
    _SonusScpAdmnSsn_Type()
)
sonusScpAdmnSsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnSsn.setStatus("obsolete")
_SonusScpAdmnTimeout_Type = Integer32
_SonusScpAdmnTimeout_Object = MibTableColumn
sonusScpAdmnTimeout = _SonusScpAdmnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 7),
    _SonusScpAdmnTimeout_Type()
)
sonusScpAdmnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnTimeout.setStatus("obsolete")


class _SonusScpAdmnType_Type(Integer32):
    """Custom type sonusScpAdmnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("authen", 4),
          ("credit", 3),
          ("lnp", 2),
          ("tollfree", 1))
    )


_SonusScpAdmnType_Type.__name__ = "Integer32"
_SonusScpAdmnType_Object = MibTableColumn
sonusScpAdmnType = _SonusScpAdmnType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 8),
    _SonusScpAdmnType_Type()
)
sonusScpAdmnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnType.setStatus("obsolete")


class _SonusScpAdmnProtocol_Type(Integer32):
    """Custom type sonusScpAdmnProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ain", 2),
          ("inap", 3),
          ("none", 1))
    )


_SonusScpAdmnProtocol_Type.__name__ = "Integer32"
_SonusScpAdmnProtocol_Object = MibTableColumn
sonusScpAdmnProtocol = _SonusScpAdmnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 9),
    _SonusScpAdmnProtocol_Type()
)
sonusScpAdmnProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnProtocol.setStatus("obsolete")


class _SonusScpAdmnState_Type(Integer32):
    """Custom type sonusScpAdmnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusScpAdmnState_Type.__name__ = "Integer32"
_SonusScpAdmnState_Object = MibTableColumn
sonusScpAdmnState = _SonusScpAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 10),
    _SonusScpAdmnState_Type()
)
sonusScpAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnState.setStatus("obsolete")
_SonusScpAdmnRowStatus_Type = RowStatus
_SonusScpAdmnRowStatus_Object = MibTableColumn
sonusScpAdmnRowStatus = _SonusScpAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 11),
    _SonusScpAdmnRowStatus_Type()
)
sonusScpAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusScpAdmnRowStatus.setStatus("obsolete")
_SonusScpStatTable_Object = MibTable
sonusScpStatTable = _SonusScpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    sonusScpStatTable.setStatus("obsolete")
_SonusScpStatEntry_Object = MibTableRow
sonusScpStatEntry = _SonusScpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2, 1)
)
sonusScpStatEntry.setIndexNames(
    (0, "SONUS-TCAP-CLIENT-SERVICES-MIB", "sonusScpStatIndex"),
)
if mibBuilder.loadTexts:
    sonusScpStatEntry.setStatus("obsolete")
_SonusScpStatIndex_Type = Integer32
_SonusScpStatIndex_Object = MibTableColumn
sonusScpStatIndex = _SonusScpStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2, 1, 1),
    _SonusScpStatIndex_Type()
)
sonusScpStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusScpStatIndex.setStatus("obsolete")
_SonusScpStatQueryNum_Type = Integer32
_SonusScpStatQueryNum_Object = MibTableColumn
sonusScpStatQueryNum = _SonusScpStatQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2, 1, 2),
    _SonusScpStatQueryNum_Type()
)
sonusScpStatQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusScpStatQueryNum.setStatus("obsolete")
_SonusScpStatQueryFailed_Type = Integer32
_SonusScpStatQueryFailed_Object = MibTableColumn
sonusScpStatQueryFailed = _SonusScpStatQueryFailed_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2, 1, 3),
    _SonusScpStatQueryFailed_Type()
)
sonusScpStatQueryFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusScpStatQueryFailed.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-TCAP-CLIENT-SERVICES-MIB",
    **{"sonusTcapClientServicesMIB": sonusTcapClientServicesMIB,
       "sonusTcapClientServicesMIBObjects": sonusTcapClientServicesMIBObjects,
       "sonusScpAdmn": sonusScpAdmn,
       "sonusScpAdmnNextIndex": sonusScpAdmnNextIndex,
       "sonusScpAdmnTable": sonusScpAdmnTable,
       "sonusScpAdmnEntry": sonusScpAdmnEntry,
       "sonusScpAdmnIndex": sonusScpAdmnIndex,
       "sonusScpAdmnName": sonusScpAdmnName,
       "sonusScpAdmnCarrier": sonusScpAdmnCarrier,
       "sonusScpAdmnNode": sonusScpAdmnNode,
       "sonusScpAdmnPc": sonusScpAdmnPc,
       "sonusScpAdmnSsn": sonusScpAdmnSsn,
       "sonusScpAdmnTimeout": sonusScpAdmnTimeout,
       "sonusScpAdmnType": sonusScpAdmnType,
       "sonusScpAdmnProtocol": sonusScpAdmnProtocol,
       "sonusScpAdmnState": sonusScpAdmnState,
       "sonusScpAdmnRowStatus": sonusScpAdmnRowStatus,
       "sonusScpStatTable": sonusScpStatTable,
       "sonusScpStatEntry": sonusScpStatEntry,
       "sonusScpStatIndex": sonusScpStatIndex,
       "sonusScpStatQueryNum": sonusScpStatQueryNum,
       "sonusScpStatQueryFailed": sonusScpStatQueryFailed}
)
