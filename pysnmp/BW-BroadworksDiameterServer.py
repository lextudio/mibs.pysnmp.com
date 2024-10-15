# SNMP MIB module (BW-BroadworksDiameterServer) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-BroadworksDiameterServer
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:01 2024
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

broadsoft = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6431)
)
broadsoft.setRevisions(
        ("2006-01-26 00:01",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadworks_ObjectIdentity = ObjectIdentity
broadworks = _Broadworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1)
)
_DiameterFrontNode_ObjectIdentity = ObjectIdentity
diameterFrontNode = _DiameterFrontNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10)
)
_ProtocolsModule_ObjectIdentity = ObjectIdentity
protocolsModule = _ProtocolsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1)
)
_DsBaseProtocolStats_ObjectIdentity = ObjectIdentity
dsBaseProtocolStats = _DsBaseProtocolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1)
)
_BwDiameterFrontNodeRequestsOut_Type = Counter32
_BwDiameterFrontNodeRequestsOut_Object = MibScalar
bwDiameterFrontNodeRequestsOut = _BwDiameterFrontNodeRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 1),
    _BwDiameterFrontNodeRequestsOut_Type()
)
bwDiameterFrontNodeRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeRequestsOut.setStatus("current")
_BwDiameterFrontNodeRequestsIn_Type = Counter32
_BwDiameterFrontNodeRequestsIn_Object = MibScalar
bwDiameterFrontNodeRequestsIn = _BwDiameterFrontNodeRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 2),
    _BwDiameterFrontNodeRequestsIn_Type()
)
bwDiameterFrontNodeRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeRequestsIn.setStatus("current")
_BwDiameterFrontNodeResponsesOut_Type = Counter32
_BwDiameterFrontNodeResponsesOut_Object = MibScalar
bwDiameterFrontNodeResponsesOut = _BwDiameterFrontNodeResponsesOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 3),
    _BwDiameterFrontNodeResponsesOut_Type()
)
bwDiameterFrontNodeResponsesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeResponsesOut.setStatus("current")
_BwDiameterFrontNodeResponsesIn_Type = Counter32
_BwDiameterFrontNodeResponsesIn_Object = MibScalar
bwDiameterFrontNodeResponsesIn = _BwDiameterFrontNodeResponsesIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 4),
    _BwDiameterFrontNodeResponsesIn_Type()
)
bwDiameterFrontNodeResponsesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeResponsesIn.setStatus("current")
_BwDiameterFrontNodeDWRsOut_Type = Counter32
_BwDiameterFrontNodeDWRsOut_Object = MibScalar
bwDiameterFrontNodeDWRsOut = _BwDiameterFrontNodeDWRsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 5),
    _BwDiameterFrontNodeDWRsOut_Type()
)
bwDiameterFrontNodeDWRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeDWRsOut.setStatus("current")
_BwDiameterFrontNodeDWRsIn_Type = Counter32
_BwDiameterFrontNodeDWRsIn_Object = MibScalar
bwDiameterFrontNodeDWRsIn = _BwDiameterFrontNodeDWRsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 6),
    _BwDiameterFrontNodeDWRsIn_Type()
)
bwDiameterFrontNodeDWRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeDWRsIn.setStatus("current")
_BwDiameterFrontNodeDWAsOut_Type = Counter32
_BwDiameterFrontNodeDWAsOut_Object = MibScalar
bwDiameterFrontNodeDWAsOut = _BwDiameterFrontNodeDWAsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 7),
    _BwDiameterFrontNodeDWAsOut_Type()
)
bwDiameterFrontNodeDWAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeDWAsOut.setStatus("current")
_BwDiameterFrontNodeDWAsIn_Type = Counter32
_BwDiameterFrontNodeDWAsIn_Object = MibScalar
bwDiameterFrontNodeDWAsIn = _BwDiameterFrontNodeDWAsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 8),
    _BwDiameterFrontNodeDWAsIn_Type()
)
bwDiameterFrontNodeDWAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeDWAsIn.setStatus("current")
_BwDiameterFrontNodeCERsOut_Type = Counter32
_BwDiameterFrontNodeCERsOut_Object = MibScalar
bwDiameterFrontNodeCERsOut = _BwDiameterFrontNodeCERsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 9),
    _BwDiameterFrontNodeCERsOut_Type()
)
bwDiameterFrontNodeCERsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeCERsOut.setStatus("current")
_BwDiameterFrontNodeCERsIn_Type = Counter32
_BwDiameterFrontNodeCERsIn_Object = MibScalar
bwDiameterFrontNodeCERsIn = _BwDiameterFrontNodeCERsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 10),
    _BwDiameterFrontNodeCERsIn_Type()
)
bwDiameterFrontNodeCERsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeCERsIn.setStatus("current")
_BwDiameterFrontNodeCEAsOut_Type = Counter32
_BwDiameterFrontNodeCEAsOut_Object = MibScalar
bwDiameterFrontNodeCEAsOut = _BwDiameterFrontNodeCEAsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 11),
    _BwDiameterFrontNodeCEAsOut_Type()
)
bwDiameterFrontNodeCEAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeCEAsOut.setStatus("current")
_BwDiameterFrontNodeCEAsIn_Type = Counter32
_BwDiameterFrontNodeCEAsIn_Object = MibScalar
bwDiameterFrontNodeCEAsIn = _BwDiameterFrontNodeCEAsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 12),
    _BwDiameterFrontNodeCEAsIn_Type()
)
bwDiameterFrontNodeCEAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeCEAsIn.setStatus("current")
_BwDiameterFrontNodeDPRsOut_Type = Counter32
_BwDiameterFrontNodeDPRsOut_Object = MibScalar
bwDiameterFrontNodeDPRsOut = _BwDiameterFrontNodeDPRsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 13),
    _BwDiameterFrontNodeDPRsOut_Type()
)
bwDiameterFrontNodeDPRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeDPRsOut.setStatus("current")
_BwDiameterFrontNodeDPRsIn_Type = Counter32
_BwDiameterFrontNodeDPRsIn_Object = MibScalar
bwDiameterFrontNodeDPRsIn = _BwDiameterFrontNodeDPRsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 14),
    _BwDiameterFrontNodeDPRsIn_Type()
)
bwDiameterFrontNodeDPRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeDPRsIn.setStatus("current")
_BwDiameterFrontNodeDPAsOut_Type = Counter32
_BwDiameterFrontNodeDPAsOut_Object = MibScalar
bwDiameterFrontNodeDPAsOut = _BwDiameterFrontNodeDPAsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 15),
    _BwDiameterFrontNodeDPAsOut_Type()
)
bwDiameterFrontNodeDPAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeDPAsOut.setStatus("current")
_BwDiameterFrontNodeDPAsIn_Type = Counter32
_BwDiameterFrontNodeDPAsIn_Object = MibScalar
bwDiameterFrontNodeDPAsIn = _BwDiameterFrontNodeDPAsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 16),
    _BwDiameterFrontNodeDPAsIn_Type()
)
bwDiameterFrontNodeDPAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeDPAsIn.setStatus("current")
_BwDiameterFrontNodeSTRsOut_Type = Counter32
_BwDiameterFrontNodeSTRsOut_Object = MibScalar
bwDiameterFrontNodeSTRsOut = _BwDiameterFrontNodeSTRsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 17),
    _BwDiameterFrontNodeSTRsOut_Type()
)
bwDiameterFrontNodeSTRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeSTRsOut.setStatus("current")
_BwDiameterFrontNodeSTRsIn_Type = Counter32
_BwDiameterFrontNodeSTRsIn_Object = MibScalar
bwDiameterFrontNodeSTRsIn = _BwDiameterFrontNodeSTRsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 18),
    _BwDiameterFrontNodeSTRsIn_Type()
)
bwDiameterFrontNodeSTRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeSTRsIn.setStatus("current")
_BwDiameterFrontNodeSTAsOut_Type = Counter32
_BwDiameterFrontNodeSTAsOut_Object = MibScalar
bwDiameterFrontNodeSTAsOut = _BwDiameterFrontNodeSTAsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 19),
    _BwDiameterFrontNodeSTAsOut_Type()
)
bwDiameterFrontNodeSTAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeSTAsOut.setStatus("current")
_BwDiameterFrontNodeSTAsIn_Type = Counter32
_BwDiameterFrontNodeSTAsIn_Object = MibScalar
bwDiameterFrontNodeSTAsIn = _BwDiameterFrontNodeSTAsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 20),
    _BwDiameterFrontNodeSTAsIn_Type()
)
bwDiameterFrontNodeSTAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeSTAsIn.setStatus("current")
_BwDiameterFrontNodeASRsOut_Type = Counter32
_BwDiameterFrontNodeASRsOut_Object = MibScalar
bwDiameterFrontNodeASRsOut = _BwDiameterFrontNodeASRsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 21),
    _BwDiameterFrontNodeASRsOut_Type()
)
bwDiameterFrontNodeASRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeASRsOut.setStatus("current")
_BwDiameterFrontNodeASRsIn_Type = Counter32
_BwDiameterFrontNodeASRsIn_Object = MibScalar
bwDiameterFrontNodeASRsIn = _BwDiameterFrontNodeASRsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 22),
    _BwDiameterFrontNodeASRsIn_Type()
)
bwDiameterFrontNodeASRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeASRsIn.setStatus("current")
_BwDiameterFrontNodeASAsOut_Type = Counter32
_BwDiameterFrontNodeASAsOut_Object = MibScalar
bwDiameterFrontNodeASAsOut = _BwDiameterFrontNodeASAsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 23),
    _BwDiameterFrontNodeASAsOut_Type()
)
bwDiameterFrontNodeASAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeASAsOut.setStatus("current")
_BwDiameterFrontNodeASAsIn_Type = Counter32
_BwDiameterFrontNodeASAsIn_Object = MibScalar
bwDiameterFrontNodeASAsIn = _BwDiameterFrontNodeASAsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 1, 1, 24),
    _BwDiameterFrontNodeASAsIn_Type()
)
bwDiameterFrontNodeASAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeASAsIn.setStatus("current")
_ManagementModule_ObjectIdentity = ObjectIdentity
managementModule = _ManagementModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 2)
)
_BwDiameterFrontNodeResetAllCounters_Type = Counter32
_BwDiameterFrontNodeResetAllCounters_Object = MibScalar
bwDiameterFrontNodeResetAllCounters = _BwDiameterFrontNodeResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 10, 2, 1),
    _BwDiameterFrontNodeResetAllCounters_Type()
)
bwDiameterFrontNodeResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwDiameterFrontNodeResetAllCounters.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-BroadworksDiameterServer",
    **{"broadsoft": broadsoft,
       "broadworks": broadworks,
       "diameterFrontNode": diameterFrontNode,
       "protocolsModule": protocolsModule,
       "dsBaseProtocolStats": dsBaseProtocolStats,
       "bwDiameterFrontNodeRequestsOut": bwDiameterFrontNodeRequestsOut,
       "bwDiameterFrontNodeRequestsIn": bwDiameterFrontNodeRequestsIn,
       "bwDiameterFrontNodeResponsesOut": bwDiameterFrontNodeResponsesOut,
       "bwDiameterFrontNodeResponsesIn": bwDiameterFrontNodeResponsesIn,
       "bwDiameterFrontNodeDWRsOut": bwDiameterFrontNodeDWRsOut,
       "bwDiameterFrontNodeDWRsIn": bwDiameterFrontNodeDWRsIn,
       "bwDiameterFrontNodeDWAsOut": bwDiameterFrontNodeDWAsOut,
       "bwDiameterFrontNodeDWAsIn": bwDiameterFrontNodeDWAsIn,
       "bwDiameterFrontNodeCERsOut": bwDiameterFrontNodeCERsOut,
       "bwDiameterFrontNodeCERsIn": bwDiameterFrontNodeCERsIn,
       "bwDiameterFrontNodeCEAsOut": bwDiameterFrontNodeCEAsOut,
       "bwDiameterFrontNodeCEAsIn": bwDiameterFrontNodeCEAsIn,
       "bwDiameterFrontNodeDPRsOut": bwDiameterFrontNodeDPRsOut,
       "bwDiameterFrontNodeDPRsIn": bwDiameterFrontNodeDPRsIn,
       "bwDiameterFrontNodeDPAsOut": bwDiameterFrontNodeDPAsOut,
       "bwDiameterFrontNodeDPAsIn": bwDiameterFrontNodeDPAsIn,
       "bwDiameterFrontNodeSTRsOut": bwDiameterFrontNodeSTRsOut,
       "bwDiameterFrontNodeSTRsIn": bwDiameterFrontNodeSTRsIn,
       "bwDiameterFrontNodeSTAsOut": bwDiameterFrontNodeSTAsOut,
       "bwDiameterFrontNodeSTAsIn": bwDiameterFrontNodeSTAsIn,
       "bwDiameterFrontNodeASRsOut": bwDiameterFrontNodeASRsOut,
       "bwDiameterFrontNodeASRsIn": bwDiameterFrontNodeASRsIn,
       "bwDiameterFrontNodeASAsOut": bwDiameterFrontNodeASAsOut,
       "bwDiameterFrontNodeASAsIn": bwDiameterFrontNodeASAsIn,
       "managementModule": managementModule,
       "bwDiameterFrontNodeResetAllCounters": bwDiameterFrontNodeResetAllCounters}
)
