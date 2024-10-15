# SNMP MIB module (WWP-LEOS-TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-TWAMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:14 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosTwampMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40)
)
wwpLeosTwampMIB.setRevisions(
        ("2008-08-08 08:00",
         "2008-02-15 08:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosTwampMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosTwampMIBObjects = _WwpLeosTwampMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1)
)
_WwpLeosTwamp_ObjectIdentity = ObjectIdentity
wwpLeosTwamp = _WwpLeosTwamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1)
)
_WwpLeosTwampModule_ObjectIdentity = ObjectIdentity
wwpLeosTwampModule = _WwpLeosTwampModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1)
)


class _WwpLeosTwampPort_Type(Integer32):
    """Custom type wwpLeosTwampPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_WwpLeosTwampPort_Type.__name__ = "Integer32"
_WwpLeosTwampPort_Object = MibScalar
wwpLeosTwampPort = _WwpLeosTwampPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 1),
    _WwpLeosTwampPort_Type()
)
wwpLeosTwampPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampPort.setStatus("current")


class _WwpLeosTwampEnable_Type(Integer32):
    """Custom type wwpLeosTwampEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WwpLeosTwampEnable_Type.__name__ = "Integer32"
_WwpLeosTwampEnable_Object = MibScalar
wwpLeosTwampEnable = _WwpLeosTwampEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 2),
    _WwpLeosTwampEnable_Type()
)
wwpLeosTwampEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampEnable.setStatus("current")
_WwpLeosTwampPortEnableTable_Object = MibTable
wwpLeosTwampPortEnableTable = _WwpLeosTwampPortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosTwampPortEnableTable.setStatus("current")
_WwpLeosTwampPortEnableEntry_Object = MibTableRow
wwpLeosTwampPortEnableEntry = _WwpLeosTwampPortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 3, 1)
)
wwpLeosTwampPortEnableEntry.setIndexNames(
    (0, "WWP-LEOS-TWAMP-MIB", "wwpLeosTwampPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosTwampPortEnableEntry.setStatus("current")


class _WwpLeosTwampPortId_Type(Integer32):
    """Custom type wwpLeosTwampPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_WwpLeosTwampPortId_Type.__name__ = "Integer32"
_WwpLeosTwampPortId_Object = MibTableColumn
wwpLeosTwampPortId = _WwpLeosTwampPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 3, 1, 1),
    _WwpLeosTwampPortId_Type()
)
wwpLeosTwampPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampPortId.setStatus("current")


class _WwpLeosTwampPortEnableState_Type(Integer32):
    """Custom type wwpLeosTwampPortEnableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WwpLeosTwampPortEnableState_Type.__name__ = "Integer32"
_WwpLeosTwampPortEnableState_Object = MibTableColumn
wwpLeosTwampPortEnableState = _WwpLeosTwampPortEnableState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 3, 1, 2),
    _WwpLeosTwampPortEnableState_Type()
)
wwpLeosTwampPortEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampPortEnableState.setStatus("current")


class _WwpLeosTwampClientEnable_Type(Integer32):
    """Custom type wwpLeosTwampClientEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WwpLeosTwampClientEnable_Type.__name__ = "Integer32"
_WwpLeosTwampClientEnable_Object = MibScalar
wwpLeosTwampClientEnable = _WwpLeosTwampClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 4),
    _WwpLeosTwampClientEnable_Type()
)
wwpLeosTwampClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientEnable.setStatus("current")


class _WwpLeosTwampServerEnable_Type(Integer32):
    """Custom type wwpLeosTwampServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WwpLeosTwampServerEnable_Type.__name__ = "Integer32"
_WwpLeosTwampServerEnable_Object = MibScalar
wwpLeosTwampServerEnable = _WwpLeosTwampServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 5),
    _WwpLeosTwampServerEnable_Type()
)
wwpLeosTwampServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampServerEnable.setStatus("current")


class _WwpLeosTwampLightEnable_Type(Integer32):
    """Custom type wwpLeosTwampLightEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WwpLeosTwampLightEnable_Type.__name__ = "Integer32"
_WwpLeosTwampLightEnable_Object = MibScalar
wwpLeosTwampLightEnable = _WwpLeosTwampLightEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 6),
    _WwpLeosTwampLightEnable_Type()
)
wwpLeosTwampLightEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampLightEnable.setStatus("current")
_WwpLeosTwampServerSessionsTable_Object = MibTable
wwpLeosTwampServerSessionsTable = _WwpLeosTwampServerSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wwpLeosTwampServerSessionsTable.setStatus("current")
_WwpLeosTwampServerSessionEntry_Object = MibTableRow
wwpLeosTwampServerSessionEntry = _WwpLeosTwampServerSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 7, 1)
)
wwpLeosTwampServerSessionEntry.setIndexNames(
    (0, "WWP-LEOS-TWAMP-MIB", "wwpLeosTwampServerSessionId"),
)
if mibBuilder.loadTexts:
    wwpLeosTwampServerSessionEntry.setStatus("current")


class _WwpLeosTwampServerSessionId_Type(Integer32):
    """Custom type wwpLeosTwampServerSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WwpLeosTwampServerSessionId_Type.__name__ = "Integer32"
_WwpLeosTwampServerSessionId_Object = MibTableColumn
wwpLeosTwampServerSessionId = _WwpLeosTwampServerSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 7, 1, 1),
    _WwpLeosTwampServerSessionId_Type()
)
wwpLeosTwampServerSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerSessionId.setStatus("current")


class _WwpLeosTwampServerSessionState_Type(Integer32):
    """Custom type wwpLeosTwampServerSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("accept", 3),
          ("error", 6),
          ("greet", 1),
          ("listen", 0),
          ("start", 2),
          ("stop", 5),
          ("test", 4))
    )


_WwpLeosTwampServerSessionState_Type.__name__ = "Integer32"
_WwpLeosTwampServerSessionState_Object = MibTableColumn
wwpLeosTwampServerSessionState = _WwpLeosTwampServerSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 7, 1, 2),
    _WwpLeosTwampServerSessionState_Type()
)
wwpLeosTwampServerSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerSessionState.setStatus("current")


class _WwpLeosTwampServerSessionPort_Type(Integer32):
    """Custom type wwpLeosTwampServerSessionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTwampServerSessionPort_Type.__name__ = "Integer32"
_WwpLeosTwampServerSessionPort_Object = MibTableColumn
wwpLeosTwampServerSessionPort = _WwpLeosTwampServerSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 7, 1, 3),
    _WwpLeosTwampServerSessionPort_Type()
)
wwpLeosTwampServerSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerSessionPort.setStatus("current")
_WwpLeosTwampServerSessionHost_Type = IpAddress
_WwpLeosTwampServerSessionHost_Object = MibTableColumn
wwpLeosTwampServerSessionHost = _WwpLeosTwampServerSessionHost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 7, 1, 4),
    _WwpLeosTwampServerSessionHost_Type()
)
wwpLeosTwampServerSessionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerSessionHost.setStatus("current")
_WwpLeosTwampServerSessionNumPkts_Type = Integer32
_WwpLeosTwampServerSessionNumPkts_Object = MibTableColumn
wwpLeosTwampServerSessionNumPkts = _WwpLeosTwampServerSessionNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 7, 1, 5),
    _WwpLeosTwampServerSessionNumPkts_Type()
)
wwpLeosTwampServerSessionNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerSessionNumPkts.setStatus("current")
_WwpLeosTwampServerSessionSeqNum_Type = Integer32
_WwpLeosTwampServerSessionSeqNum_Object = MibTableColumn
wwpLeosTwampServerSessionSeqNum = _WwpLeosTwampServerSessionSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 7, 1, 6),
    _WwpLeosTwampServerSessionSeqNum_Type()
)
wwpLeosTwampServerSessionSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerSessionSeqNum.setStatus("current")


class _WwpLeosTwampServerSessionHwAssist_Type(Integer32):
    """Custom type wwpLeosTwampServerSessionHwAssist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_WwpLeosTwampServerSessionHwAssist_Type.__name__ = "Integer32"
_WwpLeosTwampServerSessionHwAssist_Object = MibTableColumn
wwpLeosTwampServerSessionHwAssist = _WwpLeosTwampServerSessionHwAssist_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 7, 1, 7),
    _WwpLeosTwampServerSessionHwAssist_Type()
)
wwpLeosTwampServerSessionHwAssist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerSessionHwAssist.setStatus("current")


class _WwpLeosTwampTimeout_Type(Integer32):
    """Custom type wwpLeosTwampTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_WwpLeosTwampTimeout_Type.__name__ = "Integer32"
_WwpLeosTwampTimeout_Object = MibScalar
wwpLeosTwampTimeout = _WwpLeosTwampTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 8),
    _WwpLeosTwampTimeout_Type()
)
wwpLeosTwampTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampTimeout.setStatus("current")
_WwpLeosTwampClientSessionsTable_Object = MibTable
wwpLeosTwampClientSessionsTable = _WwpLeosTwampClientSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionsTable.setStatus("current")
_WwpLeosTwampClientSessionEntry_Object = MibTableRow
wwpLeosTwampClientSessionEntry = _WwpLeosTwampClientSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1)
)
wwpLeosTwampClientSessionEntry.setIndexNames(
    (0, "WWP-LEOS-TWAMP-MIB", "wwpLeosTwampClientSessionId"),
)
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionEntry.setStatus("current")


class _WwpLeosTwampClientSessionId_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WwpLeosTwampClientSessionId_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionId_Object = MibTableColumn
wwpLeosTwampClientSessionId = _WwpLeosTwampClientSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 1),
    _WwpLeosTwampClientSessionId_Type()
)
wwpLeosTwampClientSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionId.setStatus("current")


class _WwpLeosTwampClientSessionStatus_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionStatus based on Integer32"""
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
        *(("active", 1),
          ("clear", 3),
          ("clearStats", 6),
          ("createAndGo", 2),
          ("startTest", 4),
          ("stopTest", 5))
    )


_WwpLeosTwampClientSessionStatus_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionStatus_Object = MibTableColumn
wwpLeosTwampClientSessionStatus = _WwpLeosTwampClientSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 2),
    _WwpLeosTwampClientSessionStatus_Type()
)
wwpLeosTwampClientSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatus.setStatus("current")


class _WwpLeosTwampClientSessionName_Type(DisplayString):
    """Custom type wwpLeosTwampClientSessionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_WwpLeosTwampClientSessionName_Type.__name__ = "DisplayString"
_WwpLeosTwampClientSessionName_Object = MibTableColumn
wwpLeosTwampClientSessionName = _WwpLeosTwampClientSessionName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 3),
    _WwpLeosTwampClientSessionName_Type()
)
wwpLeosTwampClientSessionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionName.setStatus("current")
_WwpLeosTwampClientSessionHost_Type = IpAddress
_WwpLeosTwampClientSessionHost_Object = MibTableColumn
wwpLeosTwampClientSessionHost = _WwpLeosTwampClientSessionHost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 4),
    _WwpLeosTwampClientSessionHost_Type()
)
wwpLeosTwampClientSessionHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionHost.setStatus("current")


class _WwpLeosTwampClientSessionState_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("error", 7),
          ("greeting", 1),
          ("idle", 0),
          ("serverStart", 2),
          ("sessionSetup", 3),
          ("sessionStart", 4),
          ("stop", 6),
          ("testing", 5))
    )


_WwpLeosTwampClientSessionState_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionState_Object = MibTableColumn
wwpLeosTwampClientSessionState = _WwpLeosTwampClientSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 5),
    _WwpLeosTwampClientSessionState_Type()
)
wwpLeosTwampClientSessionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionState.setStatus("current")


class _WwpLeosTwampClientSessionCommPort_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionCommPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTwampClientSessionCommPort_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionCommPort_Object = MibTableColumn
wwpLeosTwampClientSessionCommPort = _WwpLeosTwampClientSessionCommPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 6),
    _WwpLeosTwampClientSessionCommPort_Type()
)
wwpLeosTwampClientSessionCommPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionCommPort.setStatus("current")


class _WwpLeosTwampClientSessionCosPolicy_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionCosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 1),
          ("ipPrec", 2))
    )


_WwpLeosTwampClientSessionCosPolicy_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionCosPolicy_Object = MibTableColumn
wwpLeosTwampClientSessionCosPolicy = _WwpLeosTwampClientSessionCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 7),
    _WwpLeosTwampClientSessionCosPolicy_Type()
)
wwpLeosTwampClientSessionCosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionCosPolicy.setStatus("current")


class _WwpLeosTwampClientSessionDscp_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WwpLeosTwampClientSessionDscp_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionDscp_Object = MibTableColumn
wwpLeosTwampClientSessionDscp = _WwpLeosTwampClientSessionDscp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 8),
    _WwpLeosTwampClientSessionDscp_Type()
)
wwpLeosTwampClientSessionDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionDscp.setStatus("current")


class _WwpLeosTwampClientSessionIpPrec_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionIpPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTwampClientSessionIpPrec_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionIpPrec_Object = MibTableColumn
wwpLeosTwampClientSessionIpPrec = _WwpLeosTwampClientSessionIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 9),
    _WwpLeosTwampClientSessionIpPrec_Type()
)
wwpLeosTwampClientSessionIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionIpPrec.setStatus("current")


class _WwpLeosTwampClientSessionType_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("poisson", 2))
    )


_WwpLeosTwampClientSessionType_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionType_Object = MibTableColumn
wwpLeosTwampClientSessionType = _WwpLeosTwampClientSessionType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 10),
    _WwpLeosTwampClientSessionType_Type()
)
wwpLeosTwampClientSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionType.setStatus("current")


class _WwpLeosTwampClientSessionPktSize_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_WwpLeosTwampClientSessionPktSize_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionPktSize_Object = MibTableColumn
wwpLeosTwampClientSessionPktSize = _WwpLeosTwampClientSessionPktSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 11),
    _WwpLeosTwampClientSessionPktSize_Type()
)
wwpLeosTwampClientSessionPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionPktSize.setStatus("current")


class _WwpLeosTwampClientSessionRepeat_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionRepeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTwampClientSessionRepeat_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionRepeat_Object = MibTableColumn
wwpLeosTwampClientSessionRepeat = _WwpLeosTwampClientSessionRepeat_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 12),
    _WwpLeosTwampClientSessionRepeat_Type()
)
wwpLeosTwampClientSessionRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionRepeat.setStatus("current")
_WwpLeosTwampClientSessionSeqNum_Type = Integer32
_WwpLeosTwampClientSessionSeqNum_Object = MibTableColumn
wwpLeosTwampClientSessionSeqNum = _WwpLeosTwampClientSessionSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 13),
    _WwpLeosTwampClientSessionSeqNum_Type()
)
wwpLeosTwampClientSessionSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionSeqNum.setStatus("current")
_WwpLeosTwampClientSessionNumPkts_Type = Integer32
_WwpLeosTwampClientSessionNumPkts_Object = MibTableColumn
wwpLeosTwampClientSessionNumPkts = _WwpLeosTwampClientSessionNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 14),
    _WwpLeosTwampClientSessionNumPkts_Type()
)
wwpLeosTwampClientSessionNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionNumPkts.setStatus("current")


class _WwpLeosTwampClientSessionRxHw_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionRxHw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_WwpLeosTwampClientSessionRxHw_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionRxHw_Object = MibTableColumn
wwpLeosTwampClientSessionRxHw = _WwpLeosTwampClientSessionRxHw_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 15),
    _WwpLeosTwampClientSessionRxHw_Type()
)
wwpLeosTwampClientSessionRxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionRxHw.setStatus("current")


class _WwpLeosTwampClientSessionTxHw_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionTxHw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_WwpLeosTwampClientSessionTxHw_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionTxHw_Object = MibTableColumn
wwpLeosTwampClientSessionTxHw = _WwpLeosTwampClientSessionTxHw_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 16),
    _WwpLeosTwampClientSessionTxHw_Type()
)
wwpLeosTwampClientSessionTxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionTxHw.setStatus("current")


class _WwpLeosTwampClientSessionDot1dpri_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionDot1dpri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTwampClientSessionDot1dpri_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionDot1dpri_Object = MibTableColumn
wwpLeosTwampClientSessionDot1dpri = _WwpLeosTwampClientSessionDot1dpri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 9, 1, 17),
    _WwpLeosTwampClientSessionDot1dpri_Type()
)
wwpLeosTwampClientSessionDot1dpri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionDot1dpri.setStatus("current")
_WwpLeosTwampClientSessionsStatisticsTable_Object = MibTable
wwpLeosTwampClientSessionsStatisticsTable = _WwpLeosTwampClientSessionsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionsStatisticsTable.setStatus("current")
_WwpLeosTwampClientSessionStatisticsEntry_Object = MibTableRow
wwpLeosTwampClientSessionStatisticsEntry = _WwpLeosTwampClientSessionStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1)
)
wwpLeosTwampClientSessionStatisticsEntry.setIndexNames(
    (0, "WWP-LEOS-TWAMP-MIB", "wwpLeosTwampClientSessionStatsIndex"),
    (0, "WWP-LEOS-TWAMP-MIB", "wwpLeosTwampClientStatsRecordIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatisticsEntry.setStatus("current")


class _WwpLeosTwampClientSessionStatsIndex_Type(Integer32):
    """Custom type wwpLeosTwampClientSessionStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WwpLeosTwampClientSessionStatsIndex_Type.__name__ = "Integer32"
_WwpLeosTwampClientSessionStatsIndex_Object = MibTableColumn
wwpLeosTwampClientSessionStatsIndex = _WwpLeosTwampClientSessionStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 1),
    _WwpLeosTwampClientSessionStatsIndex_Type()
)
wwpLeosTwampClientSessionStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsIndex.setStatus("current")


class _WwpLeosTwampClientStatsRecordIndex_Type(Integer32):
    """Custom type wwpLeosTwampClientStatsRecordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WwpLeosTwampClientStatsRecordIndex_Type.__name__ = "Integer32"
_WwpLeosTwampClientStatsRecordIndex_Object = MibTableColumn
wwpLeosTwampClientStatsRecordIndex = _WwpLeosTwampClientStatsRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 2),
    _WwpLeosTwampClientStatsRecordIndex_Type()
)
wwpLeosTwampClientStatsRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTwampClientStatsRecordIndex.setStatus("current")


class _WwpLeosTwampClientSessionStatsName_Type(DisplayString):
    """Custom type wwpLeosTwampClientSessionStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_WwpLeosTwampClientSessionStatsName_Type.__name__ = "DisplayString"
_WwpLeosTwampClientSessionStatsName_Object = MibTableColumn
wwpLeosTwampClientSessionStatsName = _WwpLeosTwampClientSessionStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 3),
    _WwpLeosTwampClientSessionStatsName_Type()
)
wwpLeosTwampClientSessionStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsName.setStatus("current")
_WwpLeosTwampClientSessionTimestamp_Type = Unsigned32
_WwpLeosTwampClientSessionTimestamp_Object = MibTableColumn
wwpLeosTwampClientSessionTimestamp = _WwpLeosTwampClientSessionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 4),
    _WwpLeosTwampClientSessionTimestamp_Type()
)
wwpLeosTwampClientSessionTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionTimestamp.setStatus("current")
_WwpLeosTwampClientSessionStatsPktTx_Type = Unsigned32
_WwpLeosTwampClientSessionStatsPktTx_Object = MibTableColumn
wwpLeosTwampClientSessionStatsPktTx = _WwpLeosTwampClientSessionStatsPktTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 5),
    _WwpLeosTwampClientSessionStatsPktTx_Type()
)
wwpLeosTwampClientSessionStatsPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsPktTx.setStatus("current")
_WwpLeosTwampClientSessionStatsPktRx_Type = Unsigned32
_WwpLeosTwampClientSessionStatsPktRx_Object = MibTableColumn
wwpLeosTwampClientSessionStatsPktRx = _WwpLeosTwampClientSessionStatsPktRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 6),
    _WwpLeosTwampClientSessionStatsPktRx_Type()
)
wwpLeosTwampClientSessionStatsPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsPktRx.setStatus("current")
_WwpLeosTwampClientSessionStatsPktOL_Type = Unsigned32
_WwpLeosTwampClientSessionStatsPktOL_Object = MibTableColumn
wwpLeosTwampClientSessionStatsPktOL = _WwpLeosTwampClientSessionStatsPktOL_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 7),
    _WwpLeosTwampClientSessionStatsPktOL_Type()
)
wwpLeosTwampClientSessionStatsPktOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsPktOL.setStatus("current")
_WwpLeosTwampClientSessionStatsPktRL_Type = Unsigned32
_WwpLeosTwampClientSessionStatsPktRL_Object = MibTableColumn
wwpLeosTwampClientSessionStatsPktRL = _WwpLeosTwampClientSessionStatsPktRL_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 8),
    _WwpLeosTwampClientSessionStatsPktRL_Type()
)
wwpLeosTwampClientSessionStatsPktRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsPktRL.setStatus("current")
_WwpLeosTwampClientSessionStatsRTMin_Type = Unsigned32
_WwpLeosTwampClientSessionStatsRTMin_Object = MibTableColumn
wwpLeosTwampClientSessionStatsRTMin = _WwpLeosTwampClientSessionStatsRTMin_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 9),
    _WwpLeosTwampClientSessionStatsRTMin_Type()
)
wwpLeosTwampClientSessionStatsRTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsRTMin.setStatus("current")
_WwpLeosTwampClientSessionStatsRTMax_Type = Unsigned32
_WwpLeosTwampClientSessionStatsRTMax_Object = MibTableColumn
wwpLeosTwampClientSessionStatsRTMax = _WwpLeosTwampClientSessionStatsRTMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 10),
    _WwpLeosTwampClientSessionStatsRTMax_Type()
)
wwpLeosTwampClientSessionStatsRTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsRTMax.setStatus("current")
_WwpLeosTwampClientSessionStatsRTMean_Type = Unsigned32
_WwpLeosTwampClientSessionStatsRTMean_Object = MibTableColumn
wwpLeosTwampClientSessionStatsRTMean = _WwpLeosTwampClientSessionStatsRTMean_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 11),
    _WwpLeosTwampClientSessionStatsRTMean_Type()
)
wwpLeosTwampClientSessionStatsRTMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsRTMean.setStatus("current")
_WwpLeosTwampClientSessionStatsRTStdDev_Type = Unsigned32
_WwpLeosTwampClientSessionStatsRTStdDev_Object = MibTableColumn
wwpLeosTwampClientSessionStatsRTStdDev = _WwpLeosTwampClientSessionStatsRTStdDev_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 12),
    _WwpLeosTwampClientSessionStatsRTStdDev_Type()
)
wwpLeosTwampClientSessionStatsRTStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsRTStdDev.setStatus("current")
_WwpLeosTwampClientSessionStatsRT95th_Type = Unsigned32
_WwpLeosTwampClientSessionStatsRT95th_Object = MibTableColumn
wwpLeosTwampClientSessionStatsRT95th = _WwpLeosTwampClientSessionStatsRT95th_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 13),
    _WwpLeosTwampClientSessionStatsRT95th_Type()
)
wwpLeosTwampClientSessionStatsRT95th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsRT95th.setStatus("current")
_WwpLeosTwampClientSessionStatsRT99pt9th_Type = Unsigned32
_WwpLeosTwampClientSessionStatsRT99pt9th_Object = MibTableColumn
wwpLeosTwampClientSessionStatsRT99pt9th = _WwpLeosTwampClientSessionStatsRT99pt9th_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 14),
    _WwpLeosTwampClientSessionStatsRT99pt9th_Type()
)
wwpLeosTwampClientSessionStatsRT99pt9th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsRT99pt9th.setStatus("current")
_WwpLeosTwampClientSessionStatsOWOMin_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWOMin_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWOMin = _WwpLeosTwampClientSessionStatsOWOMin_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 15),
    _WwpLeosTwampClientSessionStatsOWOMin_Type()
)
wwpLeosTwampClientSessionStatsOWOMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWOMin.setStatus("current")
_WwpLeosTwampClientSessionStatsOWOMax_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWOMax_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWOMax = _WwpLeosTwampClientSessionStatsOWOMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 16),
    _WwpLeosTwampClientSessionStatsOWOMax_Type()
)
wwpLeosTwampClientSessionStatsOWOMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWOMax.setStatus("current")
_WwpLeosTwampClientSessionStatsOWOMean_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWOMean_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWOMean = _WwpLeosTwampClientSessionStatsOWOMean_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 17),
    _WwpLeosTwampClientSessionStatsOWOMean_Type()
)
wwpLeosTwampClientSessionStatsOWOMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWOMean.setStatus("current")
_WwpLeosTwampClientSessionStatsOWOStdDev_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWOStdDev_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWOStdDev = _WwpLeosTwampClientSessionStatsOWOStdDev_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 18),
    _WwpLeosTwampClientSessionStatsOWOStdDev_Type()
)
wwpLeosTwampClientSessionStatsOWOStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWOStdDev.setStatus("current")
_WwpLeosTwampClientSessionStatsOWO95th_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWO95th_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWO95th = _WwpLeosTwampClientSessionStatsOWO95th_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 19),
    _WwpLeosTwampClientSessionStatsOWO95th_Type()
)
wwpLeosTwampClientSessionStatsOWO95th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWO95th.setStatus("current")
_WwpLeosTwampClientSessionStatsOWO99pt9th_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWO99pt9th_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWO99pt9th = _WwpLeosTwampClientSessionStatsOWO99pt9th_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 20),
    _WwpLeosTwampClientSessionStatsOWO99pt9th_Type()
)
wwpLeosTwampClientSessionStatsOWO99pt9th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWO99pt9th.setStatus("current")
_WwpLeosTwampClientSessionStatsOWBMin_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWBMin_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWBMin = _WwpLeosTwampClientSessionStatsOWBMin_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 21),
    _WwpLeosTwampClientSessionStatsOWBMin_Type()
)
wwpLeosTwampClientSessionStatsOWBMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWBMin.setStatus("current")
_WwpLeosTwampClientSessionStatsOWBMax_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWBMax_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWBMax = _WwpLeosTwampClientSessionStatsOWBMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 22),
    _WwpLeosTwampClientSessionStatsOWBMax_Type()
)
wwpLeosTwampClientSessionStatsOWBMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWBMax.setStatus("current")
_WwpLeosTwampClientSessionStatsOWBMean_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWBMean_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWBMean = _WwpLeosTwampClientSessionStatsOWBMean_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 23),
    _WwpLeosTwampClientSessionStatsOWBMean_Type()
)
wwpLeosTwampClientSessionStatsOWBMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWBMean.setStatus("current")
_WwpLeosTwampClientSessionStatsOWBStdDev_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWBStdDev_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWBStdDev = _WwpLeosTwampClientSessionStatsOWBStdDev_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 24),
    _WwpLeosTwampClientSessionStatsOWBStdDev_Type()
)
wwpLeosTwampClientSessionStatsOWBStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWBStdDev.setStatus("current")
_WwpLeosTwampClientSessionStatsOWB95th_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWB95th_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWB95th = _WwpLeosTwampClientSessionStatsOWB95th_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 25),
    _WwpLeosTwampClientSessionStatsOWB95th_Type()
)
wwpLeosTwampClientSessionStatsOWB95th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWB95th.setStatus("current")
_WwpLeosTwampClientSessionStatsOWB99pt9th_Type = Unsigned32
_WwpLeosTwampClientSessionStatsOWB99pt9th_Object = MibTableColumn
wwpLeosTwampClientSessionStatsOWB99pt9th = _WwpLeosTwampClientSessionStatsOWB99pt9th_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 26),
    _WwpLeosTwampClientSessionStatsOWB99pt9th_Type()
)
wwpLeosTwampClientSessionStatsOWB99pt9th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsOWB99pt9th.setStatus("current")
_WwpLeosTwampClientSessionStatsTPMin_Type = Unsigned32
_WwpLeosTwampClientSessionStatsTPMin_Object = MibTableColumn
wwpLeosTwampClientSessionStatsTPMin = _WwpLeosTwampClientSessionStatsTPMin_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 27),
    _WwpLeosTwampClientSessionStatsTPMin_Type()
)
wwpLeosTwampClientSessionStatsTPMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsTPMin.setStatus("current")
_WwpLeosTwampClientSessionStatsTPMax_Type = Unsigned32
_WwpLeosTwampClientSessionStatsTPMax_Object = MibTableColumn
wwpLeosTwampClientSessionStatsTPMax = _WwpLeosTwampClientSessionStatsTPMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 28),
    _WwpLeosTwampClientSessionStatsTPMax_Type()
)
wwpLeosTwampClientSessionStatsTPMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsTPMax.setStatus("current")
_WwpLeosTwampClientSessionStatsTPMean_Type = Unsigned32
_WwpLeosTwampClientSessionStatsTPMean_Object = MibTableColumn
wwpLeosTwampClientSessionStatsTPMean = _WwpLeosTwampClientSessionStatsTPMean_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 29),
    _WwpLeosTwampClientSessionStatsTPMean_Type()
)
wwpLeosTwampClientSessionStatsTPMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsTPMean.setStatus("current")
_WwpLeosTwampClientSessionStatsTPStdDev_Type = Unsigned32
_WwpLeosTwampClientSessionStatsTPStdDev_Object = MibTableColumn
wwpLeosTwampClientSessionStatsTPStdDev = _WwpLeosTwampClientSessionStatsTPStdDev_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 30),
    _WwpLeosTwampClientSessionStatsTPStdDev_Type()
)
wwpLeosTwampClientSessionStatsTPStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsTPStdDev.setStatus("current")
_WwpLeosTwampClientSessionStatsTP95th_Type = Unsigned32
_WwpLeosTwampClientSessionStatsTP95th_Object = MibTableColumn
wwpLeosTwampClientSessionStatsTP95th = _WwpLeosTwampClientSessionStatsTP95th_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 31),
    _WwpLeosTwampClientSessionStatsTP95th_Type()
)
wwpLeosTwampClientSessionStatsTP95th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsTP95th.setStatus("current")
_WwpLeosTwampClientSessionStatsTP99pt9th_Type = Unsigned32
_WwpLeosTwampClientSessionStatsTP99pt9th_Object = MibTableColumn
wwpLeosTwampClientSessionStatsTP99pt9th = _WwpLeosTwampClientSessionStatsTP99pt9th_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 11, 1, 32),
    _WwpLeosTwampClientSessionStatsTP99pt9th_Type()
)
wwpLeosTwampClientSessionStatsTP99pt9th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampClientSessionStatsTP99pt9th.setStatus("current")


class _WwpLeosTwampClientDscp_Type(Integer32):
    """Custom type wwpLeosTwampClientDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WwpLeosTwampClientDscp_Type.__name__ = "Integer32"
_WwpLeosTwampClientDscp_Object = MibScalar
wwpLeosTwampClientDscp = _WwpLeosTwampClientDscp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 12),
    _WwpLeosTwampClientDscp_Type()
)
wwpLeosTwampClientDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientDscp.setStatus("current")


class _WwpLeosTwampServerDscp_Type(Integer32):
    """Custom type wwpLeosTwampServerDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WwpLeosTwampServerDscp_Type.__name__ = "Integer32"
_WwpLeosTwampServerDscp_Object = MibScalar
wwpLeosTwampServerDscp = _WwpLeosTwampServerDscp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 13),
    _WwpLeosTwampServerDscp_Type()
)
wwpLeosTwampServerDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampServerDscp.setStatus("current")


class _WwpLeosTwampClientHwAssist_Type(Integer32):
    """Custom type wwpLeosTwampClientHwAssist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTwampClientHwAssist_Type.__name__ = "Integer32"
_WwpLeosTwampClientHwAssist_Object = MibScalar
wwpLeosTwampClientHwAssist = _WwpLeosTwampClientHwAssist_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 14),
    _WwpLeosTwampClientHwAssist_Type()
)
wwpLeosTwampClientHwAssist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampClientHwAssist.setStatus("current")


class _WwpLeosTwampServerHwAssist_Type(Integer32):
    """Custom type wwpLeosTwampServerHwAssist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTwampServerHwAssist_Type.__name__ = "Integer32"
_WwpLeosTwampServerHwAssist_Object = MibScalar
wwpLeosTwampServerHwAssist = _WwpLeosTwampServerHwAssist_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 15),
    _WwpLeosTwampServerHwAssist_Type()
)
wwpLeosTwampServerHwAssist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTwampServerHwAssist.setStatus("current")
_WwpLeosTwampServerCtrlSessionsTable_Object = MibTable
wwpLeosTwampServerCtrlSessionsTable = _WwpLeosTwampServerCtrlSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    wwpLeosTwampServerCtrlSessionsTable.setStatus("current")
_WwpLeosTwampServerCtrlSessionEntry_Object = MibTableRow
wwpLeosTwampServerCtrlSessionEntry = _WwpLeosTwampServerCtrlSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 16, 1)
)
wwpLeosTwampServerCtrlSessionEntry.setIndexNames(
    (0, "WWP-LEOS-TWAMP-MIB", "wwpLeosTwampServerCtrlSessionId"),
)
if mibBuilder.loadTexts:
    wwpLeosTwampServerCtrlSessionEntry.setStatus("current")


class _WwpLeosTwampServerCtrlSessionId_Type(Integer32):
    """Custom type wwpLeosTwampServerCtrlSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WwpLeosTwampServerCtrlSessionId_Type.__name__ = "Integer32"
_WwpLeosTwampServerCtrlSessionId_Object = MibTableColumn
wwpLeosTwampServerCtrlSessionId = _WwpLeosTwampServerCtrlSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 16, 1, 1),
    _WwpLeosTwampServerCtrlSessionId_Type()
)
wwpLeosTwampServerCtrlSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerCtrlSessionId.setStatus("current")


class _WwpLeosTwampServerCtrlSessionState_Type(Integer32):
    """Custom type wwpLeosTwampServerCtrlSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("accept", 3),
          ("error", 6),
          ("greet", 1),
          ("listen", 0),
          ("start", 2),
          ("stop", 5),
          ("test", 4))
    )


_WwpLeosTwampServerCtrlSessionState_Type.__name__ = "Integer32"
_WwpLeosTwampServerCtrlSessionState_Object = MibTableColumn
wwpLeosTwampServerCtrlSessionState = _WwpLeosTwampServerCtrlSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 16, 1, 2),
    _WwpLeosTwampServerCtrlSessionState_Type()
)
wwpLeosTwampServerCtrlSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerCtrlSessionState.setStatus("current")


class _WwpLeosTwampServerCtrlSessionPort_Type(Integer32):
    """Custom type wwpLeosTwampServerCtrlSessionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTwampServerCtrlSessionPort_Type.__name__ = "Integer32"
_WwpLeosTwampServerCtrlSessionPort_Object = MibTableColumn
wwpLeosTwampServerCtrlSessionPort = _WwpLeosTwampServerCtrlSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 16, 1, 3),
    _WwpLeosTwampServerCtrlSessionPort_Type()
)
wwpLeosTwampServerCtrlSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerCtrlSessionPort.setStatus("current")
_WwpLeosTwampServerCtrlSessionHost_Type = IpAddress
_WwpLeosTwampServerCtrlSessionHost_Object = MibTableColumn
wwpLeosTwampServerCtrlSessionHost = _WwpLeosTwampServerCtrlSessionHost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 16, 1, 4),
    _WwpLeosTwampServerCtrlSessionHost_Type()
)
wwpLeosTwampServerCtrlSessionHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerCtrlSessionHost.setStatus("current")
_WwpLeosTwampServerCtrlSessionTestMap_Type = Unsigned32
_WwpLeosTwampServerCtrlSessionTestMap_Object = MibTableColumn
wwpLeosTwampServerCtrlSessionTestMap = _WwpLeosTwampServerCtrlSessionTestMap_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 40, 1, 1, 1, 16, 1, 5),
    _WwpLeosTwampServerCtrlSessionTestMap_Type()
)
wwpLeosTwampServerCtrlSessionTestMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTwampServerCtrlSessionTestMap.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-TWAMP-MIB",
    **{"wwpLeosTwampMIB": wwpLeosTwampMIB,
       "wwpLeosTwampMIBObjects": wwpLeosTwampMIBObjects,
       "wwpLeosTwamp": wwpLeosTwamp,
       "wwpLeosTwampModule": wwpLeosTwampModule,
       "wwpLeosTwampPort": wwpLeosTwampPort,
       "wwpLeosTwampEnable": wwpLeosTwampEnable,
       "wwpLeosTwampPortEnableTable": wwpLeosTwampPortEnableTable,
       "wwpLeosTwampPortEnableEntry": wwpLeosTwampPortEnableEntry,
       "wwpLeosTwampPortId": wwpLeosTwampPortId,
       "wwpLeosTwampPortEnableState": wwpLeosTwampPortEnableState,
       "wwpLeosTwampClientEnable": wwpLeosTwampClientEnable,
       "wwpLeosTwampServerEnable": wwpLeosTwampServerEnable,
       "wwpLeosTwampLightEnable": wwpLeosTwampLightEnable,
       "wwpLeosTwampServerSessionsTable": wwpLeosTwampServerSessionsTable,
       "wwpLeosTwampServerSessionEntry": wwpLeosTwampServerSessionEntry,
       "wwpLeosTwampServerSessionId": wwpLeosTwampServerSessionId,
       "wwpLeosTwampServerSessionState": wwpLeosTwampServerSessionState,
       "wwpLeosTwampServerSessionPort": wwpLeosTwampServerSessionPort,
       "wwpLeosTwampServerSessionHost": wwpLeosTwampServerSessionHost,
       "wwpLeosTwampServerSessionNumPkts": wwpLeosTwampServerSessionNumPkts,
       "wwpLeosTwampServerSessionSeqNum": wwpLeosTwampServerSessionSeqNum,
       "wwpLeosTwampServerSessionHwAssist": wwpLeosTwampServerSessionHwAssist,
       "wwpLeosTwampTimeout": wwpLeosTwampTimeout,
       "wwpLeosTwampClientSessionsTable": wwpLeosTwampClientSessionsTable,
       "wwpLeosTwampClientSessionEntry": wwpLeosTwampClientSessionEntry,
       "wwpLeosTwampClientSessionId": wwpLeosTwampClientSessionId,
       "wwpLeosTwampClientSessionStatus": wwpLeosTwampClientSessionStatus,
       "wwpLeosTwampClientSessionName": wwpLeosTwampClientSessionName,
       "wwpLeosTwampClientSessionHost": wwpLeosTwampClientSessionHost,
       "wwpLeosTwampClientSessionState": wwpLeosTwampClientSessionState,
       "wwpLeosTwampClientSessionCommPort": wwpLeosTwampClientSessionCommPort,
       "wwpLeosTwampClientSessionCosPolicy": wwpLeosTwampClientSessionCosPolicy,
       "wwpLeosTwampClientSessionDscp": wwpLeosTwampClientSessionDscp,
       "wwpLeosTwampClientSessionIpPrec": wwpLeosTwampClientSessionIpPrec,
       "wwpLeosTwampClientSessionType": wwpLeosTwampClientSessionType,
       "wwpLeosTwampClientSessionPktSize": wwpLeosTwampClientSessionPktSize,
       "wwpLeosTwampClientSessionRepeat": wwpLeosTwampClientSessionRepeat,
       "wwpLeosTwampClientSessionSeqNum": wwpLeosTwampClientSessionSeqNum,
       "wwpLeosTwampClientSessionNumPkts": wwpLeosTwampClientSessionNumPkts,
       "wwpLeosTwampClientSessionRxHw": wwpLeosTwampClientSessionRxHw,
       "wwpLeosTwampClientSessionTxHw": wwpLeosTwampClientSessionTxHw,
       "wwpLeosTwampClientSessionDot1dpri": wwpLeosTwampClientSessionDot1dpri,
       "wwpLeosTwampClientSessionsStatisticsTable": wwpLeosTwampClientSessionsStatisticsTable,
       "wwpLeosTwampClientSessionStatisticsEntry": wwpLeosTwampClientSessionStatisticsEntry,
       "wwpLeosTwampClientSessionStatsIndex": wwpLeosTwampClientSessionStatsIndex,
       "wwpLeosTwampClientStatsRecordIndex": wwpLeosTwampClientStatsRecordIndex,
       "wwpLeosTwampClientSessionStatsName": wwpLeosTwampClientSessionStatsName,
       "wwpLeosTwampClientSessionTimestamp": wwpLeosTwampClientSessionTimestamp,
       "wwpLeosTwampClientSessionStatsPktTx": wwpLeosTwampClientSessionStatsPktTx,
       "wwpLeosTwampClientSessionStatsPktRx": wwpLeosTwampClientSessionStatsPktRx,
       "wwpLeosTwampClientSessionStatsPktOL": wwpLeosTwampClientSessionStatsPktOL,
       "wwpLeosTwampClientSessionStatsPktRL": wwpLeosTwampClientSessionStatsPktRL,
       "wwpLeosTwampClientSessionStatsRTMin": wwpLeosTwampClientSessionStatsRTMin,
       "wwpLeosTwampClientSessionStatsRTMax": wwpLeosTwampClientSessionStatsRTMax,
       "wwpLeosTwampClientSessionStatsRTMean": wwpLeosTwampClientSessionStatsRTMean,
       "wwpLeosTwampClientSessionStatsRTStdDev": wwpLeosTwampClientSessionStatsRTStdDev,
       "wwpLeosTwampClientSessionStatsRT95th": wwpLeosTwampClientSessionStatsRT95th,
       "wwpLeosTwampClientSessionStatsRT99pt9th": wwpLeosTwampClientSessionStatsRT99pt9th,
       "wwpLeosTwampClientSessionStatsOWOMin": wwpLeosTwampClientSessionStatsOWOMin,
       "wwpLeosTwampClientSessionStatsOWOMax": wwpLeosTwampClientSessionStatsOWOMax,
       "wwpLeosTwampClientSessionStatsOWOMean": wwpLeosTwampClientSessionStatsOWOMean,
       "wwpLeosTwampClientSessionStatsOWOStdDev": wwpLeosTwampClientSessionStatsOWOStdDev,
       "wwpLeosTwampClientSessionStatsOWO95th": wwpLeosTwampClientSessionStatsOWO95th,
       "wwpLeosTwampClientSessionStatsOWO99pt9th": wwpLeosTwampClientSessionStatsOWO99pt9th,
       "wwpLeosTwampClientSessionStatsOWBMin": wwpLeosTwampClientSessionStatsOWBMin,
       "wwpLeosTwampClientSessionStatsOWBMax": wwpLeosTwampClientSessionStatsOWBMax,
       "wwpLeosTwampClientSessionStatsOWBMean": wwpLeosTwampClientSessionStatsOWBMean,
       "wwpLeosTwampClientSessionStatsOWBStdDev": wwpLeosTwampClientSessionStatsOWBStdDev,
       "wwpLeosTwampClientSessionStatsOWB95th": wwpLeosTwampClientSessionStatsOWB95th,
       "wwpLeosTwampClientSessionStatsOWB99pt9th": wwpLeosTwampClientSessionStatsOWB99pt9th,
       "wwpLeosTwampClientSessionStatsTPMin": wwpLeosTwampClientSessionStatsTPMin,
       "wwpLeosTwampClientSessionStatsTPMax": wwpLeosTwampClientSessionStatsTPMax,
       "wwpLeosTwampClientSessionStatsTPMean": wwpLeosTwampClientSessionStatsTPMean,
       "wwpLeosTwampClientSessionStatsTPStdDev": wwpLeosTwampClientSessionStatsTPStdDev,
       "wwpLeosTwampClientSessionStatsTP95th": wwpLeosTwampClientSessionStatsTP95th,
       "wwpLeosTwampClientSessionStatsTP99pt9th": wwpLeosTwampClientSessionStatsTP99pt9th,
       "wwpLeosTwampClientDscp": wwpLeosTwampClientDscp,
       "wwpLeosTwampServerDscp": wwpLeosTwampServerDscp,
       "wwpLeosTwampClientHwAssist": wwpLeosTwampClientHwAssist,
       "wwpLeosTwampServerHwAssist": wwpLeosTwampServerHwAssist,
       "wwpLeosTwampServerCtrlSessionsTable": wwpLeosTwampServerCtrlSessionsTable,
       "wwpLeosTwampServerCtrlSessionEntry": wwpLeosTwampServerCtrlSessionEntry,
       "wwpLeosTwampServerCtrlSessionId": wwpLeosTwampServerCtrlSessionId,
       "wwpLeosTwampServerCtrlSessionState": wwpLeosTwampServerCtrlSessionState,
       "wwpLeosTwampServerCtrlSessionPort": wwpLeosTwampServerCtrlSessionPort,
       "wwpLeosTwampServerCtrlSessionHost": wwpLeosTwampServerCtrlSessionHost,
       "wwpLeosTwampServerCtrlSessionTestMap": wwpLeosTwampServerCtrlSessionTestMap}
)
