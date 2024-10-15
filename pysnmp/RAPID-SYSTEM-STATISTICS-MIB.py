# SNMP MIB module (RAPID-SYSTEM-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPID-SYSTEM-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:41 2024
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

(rapidstream,) = mibBuilder.importSymbols(
    "RAPID-MIB",
    "rapidstream")

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

rsInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6)
)
rsInfoModule.setRevisions(
        ("2001-05-16 12:00",
         "2002-11-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsSystemStatisticsMIB_ObjectIdentity = ObjectIdentity
rsSystemStatisticsMIB = _RsSystemStatisticsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3)
)
if mibBuilder.loadTexts:
    rsSystemStatisticsMIB.setStatus("current")
_RsSystemCpuUtil_Type = Counter64
_RsSystemCpuUtil_Object = MibScalar
rsSystemCpuUtil = _RsSystemCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 4),
    _RsSystemCpuUtil_Type()
)
rsSystemCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemCpuUtil.setStatus("current")
_RsSystemTotalSendBytes_Type = Counter64
_RsSystemTotalSendBytes_Object = MibScalar
rsSystemTotalSendBytes = _RsSystemTotalSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 8),
    _RsSystemTotalSendBytes_Type()
)
rsSystemTotalSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemTotalSendBytes.setStatus("current")
_RsSystemTotalRecvBytes_Type = Counter64
_RsSystemTotalRecvBytes_Object = MibScalar
rsSystemTotalRecvBytes = _RsSystemTotalRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 9),
    _RsSystemTotalRecvBytes_Type()
)
rsSystemTotalRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemTotalRecvBytes.setStatus("current")
_RsSystemTotalSendPackets_Type = Counter64
_RsSystemTotalSendPackets_Object = MibScalar
rsSystemTotalSendPackets = _RsSystemTotalSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 10),
    _RsSystemTotalSendPackets_Type()
)
rsSystemTotalSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemTotalSendPackets.setStatus("current")
_RsSystemTotalRecvPackets_Type = Counter64
_RsSystemTotalRecvPackets_Object = MibScalar
rsSystemTotalRecvPackets = _RsSystemTotalRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 11),
    _RsSystemTotalRecvPackets_Type()
)
rsSystemTotalRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemTotalRecvPackets.setStatus("current")
_RsSystemStreamReqTotal_Type = Counter64
_RsSystemStreamReqTotal_Object = MibScalar
rsSystemStreamReqTotal = _RsSystemStreamReqTotal_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 30),
    _RsSystemStreamReqTotal_Type()
)
rsSystemStreamReqTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemStreamReqTotal.setStatus("current")
_RsSystemStreamReqDrop_Type = Counter64
_RsSystemStreamReqDrop_Object = MibScalar
rsSystemStreamReqDrop = _RsSystemStreamReqDrop_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 34),
    _RsSystemStreamReqDrop_Type()
)
rsSystemStreamReqDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemStreamReqDrop.setStatus("current")
_RsSystemCpuUtil1_Type = Counter64
_RsSystemCpuUtil1_Object = MibScalar
rsSystemCpuUtil1 = _RsSystemCpuUtil1_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 77),
    _RsSystemCpuUtil1_Type()
)
rsSystemCpuUtil1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemCpuUtil1.setStatus("current")
_RsSystemCpuUtil5_Type = Counter64
_RsSystemCpuUtil5_Object = MibScalar
rsSystemCpuUtil5 = _RsSystemCpuUtil5_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 78),
    _RsSystemCpuUtil5_Type()
)
rsSystemCpuUtil5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemCpuUtil5.setStatus("current")
_RsSystemCpuUtil15_Type = Counter64
_RsSystemCpuUtil15_Object = MibScalar
rsSystemCpuUtil15 = _RsSystemCpuUtil15_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 3, 79),
    _RsSystemCpuUtil15_Type()
)
rsSystemCpuUtil15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemCpuUtil15.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPID-SYSTEM-STATISTICS-MIB",
    **{"rsInfoModule": rsInfoModule,
       "rsSystemStatisticsMIB": rsSystemStatisticsMIB,
       "rsSystemCpuUtil": rsSystemCpuUtil,
       "rsSystemTotalSendBytes": rsSystemTotalSendBytes,
       "rsSystemTotalRecvBytes": rsSystemTotalRecvBytes,
       "rsSystemTotalSendPackets": rsSystemTotalSendPackets,
       "rsSystemTotalRecvPackets": rsSystemTotalRecvPackets,
       "rsSystemStreamReqTotal": rsSystemStreamReqTotal,
       "rsSystemStreamReqDrop": rsSystemStreamReqDrop,
       "rsSystemCpuUtil1": rsSystemCpuUtil1,
       "rsSystemCpuUtil5": rsSystemCpuUtil5,
       "rsSystemCpuUtil15": rsSystemCpuUtil15}
)
