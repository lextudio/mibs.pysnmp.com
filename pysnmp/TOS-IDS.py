# SNMP MIB module (TOS-IDS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TOS-IDS
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:36 2024
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
 Gauge,
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
 Opaque,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge",
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
    "Opaque",
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

(tosMib,) = mibBuilder.importSymbols(
    "TOS-SMI",
    "tosMib")


# MODULE-IDENTITY

tosIDS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11)
)
tosIDS.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IdsTotal_Type = Counter32
_IdsTotal_Object = MibScalar
idsTotal = _IdsTotal_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 1),
    _IdsTotal_Type()
)
idsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsTotal.setStatus("current")
_IdsIpoption_Type = Counter32
_IdsIpoption_Object = MibScalar
idsIpoption = _IdsIpoption_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 2),
    _IdsIpoption_Type()
)
idsIpoption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsIpoption.setStatus("current")
_IdsIpprotocol_Type = Counter32
_IdsIpprotocol_Object = MibScalar
idsIpprotocol = _IdsIpprotocol_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 3),
    _IdsIpprotocol_Type()
)
idsIpprotocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsIpprotocol.setStatus("current")
_IdsPort_Type = Counter32
_IdsPort_Object = MibScalar
idsPort = _IdsPort_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 4),
    _IdsPort_Type()
)
idsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsPort.setStatus("current")
_IdsTcpscan_Type = Counter32
_IdsTcpscan_Object = MibScalar
idsTcpscan = _IdsTcpscan_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 5),
    _IdsTcpscan_Type()
)
idsTcpscan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsTcpscan.setStatus("current")
_IdsWinnuke_Type = Counter32
_IdsWinnuke_Object = MibScalar
idsWinnuke = _IdsWinnuke_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 6),
    _IdsWinnuke_Type()
)
idsWinnuke.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsWinnuke.setStatus("current")
_IdsIcmpContent_Type = Counter32
_IdsIcmpContent_Object = MibScalar
idsIcmpContent = _IdsIcmpContent_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 7),
    _IdsIcmpContent_Type()
)
idsIcmpContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsIcmpContent.setStatus("current")
_IdsSmurf_Type = Counter32
_IdsSmurf_Object = MibScalar
idsSmurf = _IdsSmurf_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 8),
    _IdsSmurf_Type()
)
idsSmurf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsSmurf.setStatus("current")
_IdsLand_Type = Counter32
_IdsLand_Object = MibScalar
idsLand = _IdsLand_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 9),
    _IdsLand_Type()
)
idsLand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsLand.setStatus("current")
_IdsPingofdeath_Type = Counter32
_IdsPingofdeath_Object = MibScalar
idsPingofdeath = _IdsPingofdeath_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 10),
    _IdsPingofdeath_Type()
)
idsPingofdeath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsPingofdeath.setStatus("current")
_IdsTeardrop_Type = Counter32
_IdsTeardrop_Object = MibScalar
idsTeardrop = _IdsTeardrop_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 11),
    _IdsTeardrop_Type()
)
idsTeardrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsTeardrop.setStatus("current")
_IdsTarga3_Type = Counter32
_IdsTarga3_Object = MibScalar
idsTarga3 = _IdsTarga3_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 12),
    _IdsTarga3_Type()
)
idsTarga3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsTarga3.setStatus("current")
_IdsIpspoof_Type = Counter32
_IdsIpspoof_Object = MibScalar
idsIpspoof = _IdsIpspoof_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 13),
    _IdsIpspoof_Type()
)
idsIpspoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsIpspoof.setStatus("current")
_IdsPortscan_Type = Counter32
_IdsPortscan_Object = MibScalar
idsPortscan = _IdsPortscan_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 14),
    _IdsPortscan_Type()
)
idsPortscan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsPortscan.setStatus("current")
_IdsSynflood_Type = Counter32
_IdsSynflood_Object = MibScalar
idsSynflood = _IdsSynflood_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 15),
    _IdsSynflood_Type()
)
idsSynflood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsSynflood.setStatus("current")
_IdsUdpflood_Type = Counter32
_IdsUdpflood_Object = MibScalar
idsUdpflood = _IdsUdpflood_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 16),
    _IdsUdpflood_Type()
)
idsUdpflood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsUdpflood.setStatus("current")
_IdsIcmpflood_Type = Counter32
_IdsIcmpflood_Object = MibScalar
idsIcmpflood = _IdsIcmpflood_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 17),
    _IdsIcmpflood_Type()
)
idsIcmpflood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsIcmpflood.setStatus("current")
_IdsIpsweep_Type = Counter32
_IdsIpsweep_Object = MibScalar
idsIpsweep = _IdsIpsweep_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 11, 18),
    _IdsIpsweep_Type()
)
idsIpsweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsIpsweep.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOS-IDS",
    **{"tosIDS": tosIDS,
       "idsTotal": idsTotal,
       "idsIpoption": idsIpoption,
       "idsIpprotocol": idsIpprotocol,
       "idsPort": idsPort,
       "idsTcpscan": idsTcpscan,
       "idsWinnuke": idsWinnuke,
       "idsIcmpContent": idsIcmpContent,
       "idsSmurf": idsSmurf,
       "idsLand": idsLand,
       "idsPingofdeath": idsPingofdeath,
       "idsTeardrop": idsTeardrop,
       "idsTarga3": idsTarga3,
       "idsIpspoof": idsIpspoof,
       "idsPortscan": idsPortscan,
       "idsSynflood": idsSynflood,
       "idsUdpflood": idsUdpflood,
       "idsIcmpflood": idsIcmpflood,
       "idsIpsweep": idsIpsweep}
)
