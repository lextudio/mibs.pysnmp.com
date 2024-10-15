# SNMP MIB module (RBN-EPSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-EPSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:08 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

rbnEpsuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47)
)
rbnEpsuMIB.setRevisions(
        ("2009-09-23 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnEpsuNotifcationGroup_ObjectIdentity = ObjectIdentity
rbnEpsuNotifcationGroup = _RbnEpsuNotifcationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 0)
)
_RbnEpsuStatMIBObjects_ObjectIdentity = ObjectIdentity
rbnEpsuStatMIBObjects = _RbnEpsuStatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1)
)
_RbnEpsuS1uGtp_ObjectIdentity = ObjectIdentity
rbnEpsuS1uGtp = _RbnEpsuS1uGtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1)
)
_RbnEpsuS1uDlPktsSent_Type = Counter64
_RbnEpsuS1uDlPktsSent_Object = MibScalar
rbnEpsuS1uDlPktsSent = _RbnEpsuS1uDlPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 1),
    _RbnEpsuS1uDlPktsSent_Type()
)
rbnEpsuS1uDlPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlPktsSent.setUnits("Packets")
_RbnEpsuS1uDlOctetsSent_Type = Counter64
_RbnEpsuS1uDlOctetsSent_Object = MibScalar
rbnEpsuS1uDlOctetsSent = _RbnEpsuS1uDlOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 2),
    _RbnEpsuS1uDlOctetsSent_Type()
)
rbnEpsuS1uDlOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlOctetsSent.setUnits("Octets")
_RbnEpsuS1uDlPktsDropped_Type = Counter64
_RbnEpsuS1uDlPktsDropped_Object = MibScalar
rbnEpsuS1uDlPktsDropped = _RbnEpsuS1uDlPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 3),
    _RbnEpsuS1uDlPktsDropped_Type()
)
rbnEpsuS1uDlPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlPktsDropped.setUnits("Packets")
_RbnEpsuS1uDlPolicingPktsDropped_Type = Counter64
_RbnEpsuS1uDlPolicingPktsDropped_Object = MibScalar
rbnEpsuS1uDlPolicingPktsDropped = _RbnEpsuS1uDlPolicingPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 4),
    _RbnEpsuS1uDlPolicingPktsDropped_Type()
)
rbnEpsuS1uDlPolicingPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlPolicingPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlPolicingPktsDropped.setUnits("Packets")
_RbnEpsuS1uDlUeIdlePktsDropped_Type = Counter64
_RbnEpsuS1uDlUeIdlePktsDropped_Object = MibScalar
rbnEpsuS1uDlUeIdlePktsDropped = _RbnEpsuS1uDlUeIdlePktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 5),
    _RbnEpsuS1uDlUeIdlePktsDropped_Type()
)
rbnEpsuS1uDlUeIdlePktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlUeIdlePktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uDlUeIdlePktsDropped.setUnits("Packets")
_RbnEpsuS1uUlPktsRcvd_Type = Counter64
_RbnEpsuS1uUlPktsRcvd_Object = MibScalar
rbnEpsuS1uUlPktsRcvd = _RbnEpsuS1uUlPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 6),
    _RbnEpsuS1uUlPktsRcvd_Type()
)
rbnEpsuS1uUlPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlPktsRcvd.setUnits("Packets")
_RbnEpsuS1uUlOctetsRcvd_Type = Counter64
_RbnEpsuS1uUlOctetsRcvd_Object = MibScalar
rbnEpsuS1uUlOctetsRcvd = _RbnEpsuS1uUlOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 7),
    _RbnEpsuS1uUlOctetsRcvd_Type()
)
rbnEpsuS1uUlOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlOctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlOctetsRcvd.setUnits("Octets")
_RbnEpsuS1uUlPktsDiscarded_Type = Counter64
_RbnEpsuS1uUlPktsDiscarded_Object = MibScalar
rbnEpsuS1uUlPktsDiscarded = _RbnEpsuS1uUlPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 8),
    _RbnEpsuS1uUlPktsDiscarded_Type()
)
rbnEpsuS1uUlPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlPktsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlPktsDiscarded.setUnits("Packets")
_RbnEpsuS1uUlBearerPktsDiscarded_Type = Counter64
_RbnEpsuS1uUlBearerPktsDiscarded_Object = MibScalar
rbnEpsuS1uUlBearerPktsDiscarded = _RbnEpsuS1uUlBearerPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 9),
    _RbnEpsuS1uUlBearerPktsDiscarded_Type()
)
rbnEpsuS1uUlBearerPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlBearerPktsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlBearerPktsDiscarded.setUnits("Packets")
_RbnEpsuS1uUlPolicingPktsDiscarded_Type = Counter64
_RbnEpsuS1uUlPolicingPktsDiscarded_Object = MibScalar
rbnEpsuS1uUlPolicingPktsDiscarded = _RbnEpsuS1uUlPolicingPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 1, 10),
    _RbnEpsuS1uUlPolicingPktsDiscarded_Type()
)
rbnEpsuS1uUlPolicingPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlPolicingPktsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS1uUlPolicingPktsDiscarded.setUnits("Packets")
_RbnEpsuSgwGtp_ObjectIdentity = ObjectIdentity
rbnEpsuSgwGtp = _RbnEpsuSgwGtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2)
)
_RbnEpsuS5S8GtpDlPktsRcvd_Type = Counter64
_RbnEpsuS5S8GtpDlPktsRcvd_Object = MibScalar
rbnEpsuS5S8GtpDlPktsRcvd = _RbnEpsuS5S8GtpDlPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 1),
    _RbnEpsuS5S8GtpDlPktsRcvd_Type()
)
rbnEpsuS5S8GtpDlPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPktsRcvd.setUnits("Packets")
_RbnEpsuS5S8GtpDlOctetsRcvd_Type = Counter64
_RbnEpsuS5S8GtpDlOctetsRcvd_Object = MibScalar
rbnEpsuS5S8GtpDlOctetsRcvd = _RbnEpsuS5S8GtpDlOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 2),
    _RbnEpsuS5S8GtpDlOctetsRcvd_Type()
)
rbnEpsuS5S8GtpDlOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlOctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlOctetsRcvd.setUnits("Octets")
_RbnEpsuS5S8GtpDlPktsDiscarded_Type = Counter64
_RbnEpsuS5S8GtpDlPktsDiscarded_Object = MibScalar
rbnEpsuS5S8GtpDlPktsDiscarded = _RbnEpsuS5S8GtpDlPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 3),
    _RbnEpsuS5S8GtpDlPktsDiscarded_Type()
)
rbnEpsuS5S8GtpDlPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPktsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPktsDiscarded.setUnits("Packets")
_RbnEpsuS5S8GtpUlPktsSent_Type = Counter64
_RbnEpsuS5S8GtpUlPktsSent_Object = MibScalar
rbnEpsuS5S8GtpUlPktsSent = _RbnEpsuS5S8GtpUlPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 4),
    _RbnEpsuS5S8GtpUlPktsSent_Type()
)
rbnEpsuS5S8GtpUlPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPktsSent.setUnits("Packets")
_RbnEpsuS5S8GtpUlOctetsSent_Type = Counter64
_RbnEpsuS5S8GtpUlOctetsSent_Object = MibScalar
rbnEpsuS5S8GtpUlOctetsSent = _RbnEpsuS5S8GtpUlOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 5),
    _RbnEpsuS5S8GtpUlOctetsSent_Type()
)
rbnEpsuS5S8GtpUlOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlOctetsSent.setUnits("Octets")
_RbnEpsuS5S8GtpUlPktsDropped_Type = Counter64
_RbnEpsuS5S8GtpUlPktsDropped_Object = MibScalar
rbnEpsuS5S8GtpUlPktsDropped = _RbnEpsuS5S8GtpUlPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 2, 6),
    _RbnEpsuS5S8GtpUlPktsDropped_Type()
)
rbnEpsuS5S8GtpUlPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPktsDropped.setUnits("Packets")
_RbnEpsuPgwGtp_ObjectIdentity = ObjectIdentity
rbnEpsuPgwGtp = _RbnEpsuPgwGtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3)
)
_RbnEpsuS5S8GtpDlPktsSent_Type = Counter64
_RbnEpsuS5S8GtpDlPktsSent_Object = MibScalar
rbnEpsuS5S8GtpDlPktsSent = _RbnEpsuS5S8GtpDlPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 1),
    _RbnEpsuS5S8GtpDlPktsSent_Type()
)
rbnEpsuS5S8GtpDlPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPktsSent.setUnits("Packets")
_RbnEpsuS5S8GtpDlOctetsSent_Type = Counter64
_RbnEpsuS5S8GtpDlOctetsSent_Object = MibScalar
rbnEpsuS5S8GtpDlOctetsSent = _RbnEpsuS5S8GtpDlOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 2),
    _RbnEpsuS5S8GtpDlOctetsSent_Type()
)
rbnEpsuS5S8GtpDlOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlOctetsSent.setUnits("Octets")
_RbnEpsuS5S8GtpDlPktsDropped_Type = Counter64
_RbnEpsuS5S8GtpDlPktsDropped_Object = MibScalar
rbnEpsuS5S8GtpDlPktsDropped = _RbnEpsuS5S8GtpDlPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 3),
    _RbnEpsuS5S8GtpDlPktsDropped_Type()
)
rbnEpsuS5S8GtpDlPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPktsDropped.setUnits("Packets")
_RbnEpsuS5S8GtpDlPolicingPktsDropped_Type = Counter64
_RbnEpsuS5S8GtpDlPolicingPktsDropped_Object = MibScalar
rbnEpsuS5S8GtpDlPolicingPktsDropped = _RbnEpsuS5S8GtpDlPolicingPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 4),
    _RbnEpsuS5S8GtpDlPolicingPktsDropped_Type()
)
rbnEpsuS5S8GtpDlPolicingPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPolicingPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpDlPolicingPktsDropped.setUnits("Packets")
_RbnEpsuS5S8GtpUlPktsRcvd_Type = Counter64
_RbnEpsuS5S8GtpUlPktsRcvd_Object = MibScalar
rbnEpsuS5S8GtpUlPktsRcvd = _RbnEpsuS5S8GtpUlPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 5),
    _RbnEpsuS5S8GtpUlPktsRcvd_Type()
)
rbnEpsuS5S8GtpUlPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPktsRcvd.setUnits("Packets")
_RbnEpsuS5S8GtpUlOctetsRcvd_Type = Counter64
_RbnEpsuS5S8GtpUlOctetsRcvd_Object = MibScalar
rbnEpsuS5S8GtpUlOctetsRcvd = _RbnEpsuS5S8GtpUlOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 6),
    _RbnEpsuS5S8GtpUlOctetsRcvd_Type()
)
rbnEpsuS5S8GtpUlOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlOctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlOctetsRcvd.setUnits("Octets")
_RbnEpsuS5S8GtpUlPktsDiscarded_Type = Counter64
_RbnEpsuS5S8GtpUlPktsDiscarded_Object = MibScalar
rbnEpsuS5S8GtpUlPktsDiscarded = _RbnEpsuS5S8GtpUlPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 7),
    _RbnEpsuS5S8GtpUlPktsDiscarded_Type()
)
rbnEpsuS5S8GtpUlPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPktsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPktsDiscarded.setUnits("Packets")
_RbnEpsuS5S8GtpUlBearerPktsDiscarded_Type = Counter64
_RbnEpsuS5S8GtpUlBearerPktsDiscarded_Object = MibScalar
rbnEpsuS5S8GtpUlBearerPktsDiscarded = _RbnEpsuS5S8GtpUlBearerPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 8),
    _RbnEpsuS5S8GtpUlBearerPktsDiscarded_Type()
)
rbnEpsuS5S8GtpUlBearerPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlBearerPktsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlBearerPktsDiscarded.setUnits("Packets")
_RbnEpsuS5S8GtpUlPolicingPktsDiscarded_Type = Counter64
_RbnEpsuS5S8GtpUlPolicingPktsDiscarded_Object = MibScalar
rbnEpsuS5S8GtpUlPolicingPktsDiscarded = _RbnEpsuS5S8GtpUlPolicingPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 3, 9),
    _RbnEpsuS5S8GtpUlPolicingPktsDiscarded_Type()
)
rbnEpsuS5S8GtpUlPolicingPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPolicingPktsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuS5S8GtpUlPolicingPktsDiscarded.setUnits("Packets")
_RbnEpsuSgi_ObjectIdentity = ObjectIdentity
rbnEpsuSgi = _RbnEpsuSgi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4)
)
_RbnEpsuSgiDlPktsRcvd_Type = Counter64
_RbnEpsuSgiDlPktsRcvd_Object = MibScalar
rbnEpsuSgiDlPktsRcvd = _RbnEpsuSgiDlPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 1),
    _RbnEpsuSgiDlPktsRcvd_Type()
)
rbnEpsuSgiDlPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlPktsRcvd.setUnits("Packets")
_RbnEpsuSgiDlOctetsRcvd_Type = Counter64
_RbnEpsuSgiDlOctetsRcvd_Object = MibScalar
rbnEpsuSgiDlOctetsRcvd = _RbnEpsuSgiDlOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 2),
    _RbnEpsuSgiDlOctetsRcvd_Type()
)
rbnEpsuSgiDlOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlOctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlOctetsRcvd.setUnits("Octets")
_RbnEpsuSgiDlV6PktsRcvd_Type = Counter64
_RbnEpsuSgiDlV6PktsRcvd_Object = MibScalar
rbnEpsuSgiDlV6PktsRcvd = _RbnEpsuSgiDlV6PktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 3),
    _RbnEpsuSgiDlV6PktsRcvd_Type()
)
rbnEpsuSgiDlV6PktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlV6PktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlV6PktsRcvd.setUnits("Packets")
_RbnEpsuSgiDlV6OctetsRcvd_Type = Counter64
_RbnEpsuSgiDlV6OctetsRcvd_Object = MibScalar
rbnEpsuSgiDlV6OctetsRcvd = _RbnEpsuSgiDlV6OctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 4),
    _RbnEpsuSgiDlV6OctetsRcvd_Type()
)
rbnEpsuSgiDlV6OctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlV6OctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlV6OctetsRcvd.setUnits("Octets")
_RbnEpsuSgiDlPktsDiscarded_Type = Counter64
_RbnEpsuSgiDlPktsDiscarded_Object = MibScalar
rbnEpsuSgiDlPktsDiscarded = _RbnEpsuSgiDlPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 5),
    _RbnEpsuSgiDlPktsDiscarded_Type()
)
rbnEpsuSgiDlPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlPktsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiDlPktsDiscarded.setUnits("Packets")
_RbnEpsuSgiUlPktsSent_Type = Counter64
_RbnEpsuSgiUlPktsSent_Object = MibScalar
rbnEpsuSgiUlPktsSent = _RbnEpsuSgiUlPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 6),
    _RbnEpsuSgiUlPktsSent_Type()
)
rbnEpsuSgiUlPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlPktsSent.setUnits("Packets")
_RbnEpsuSgiUlOctetsSent_Type = Counter64
_RbnEpsuSgiUlOctetsSent_Object = MibScalar
rbnEpsuSgiUlOctetsSent = _RbnEpsuSgiUlOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 7),
    _RbnEpsuSgiUlOctetsSent_Type()
)
rbnEpsuSgiUlOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlOctetsSent.setUnits("Octets")
_RbnEpsuSgiUlV6PktsSent_Type = Counter64
_RbnEpsuSgiUlV6PktsSent_Object = MibScalar
rbnEpsuSgiUlV6PktsSent = _RbnEpsuSgiUlV6PktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 8),
    _RbnEpsuSgiUlV6PktsSent_Type()
)
rbnEpsuSgiUlV6PktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlV6PktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlV6PktsSent.setUnits("Packets")
_RbnEpsuSgiUlV6OctetsSent_Type = Counter64
_RbnEpsuSgiUlV6OctetsSent_Object = MibScalar
rbnEpsuSgiUlV6OctetsSent = _RbnEpsuSgiUlV6OctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 9),
    _RbnEpsuSgiUlV6OctetsSent_Type()
)
rbnEpsuSgiUlV6OctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlV6OctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlV6OctetsSent.setUnits("Octets")
_RbnEpsuSgiUlPktsDropped_Type = Counter64
_RbnEpsuSgiUlPktsDropped_Object = MibScalar
rbnEpsuSgiUlPktsDropped = _RbnEpsuSgiUlPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 4, 10),
    _RbnEpsuSgiUlPktsDropped_Type()
)
rbnEpsuSgiUlPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiUlPktsDropped.setUnits("Packets")
_RbnEpsuSgiApn_ObjectIdentity = ObjectIdentity
rbnEpsuSgiApn = _RbnEpsuSgiApn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5)
)
_RbnEpsuSgiApnStatsTable_Object = MibTable
rbnEpsuSgiApnStatsTable = _RbnEpsuSgiApnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rbnEpsuSgiApnStatsTable.setStatus("current")
_RbnEpsuSgiApnStatsEntry_Object = MibTableRow
rbnEpsuSgiApnStatsEntry = _RbnEpsuSgiApnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1)
)
rbnEpsuSgiApnStatsEntry.setIndexNames(
    (0, "RBN-EPSU-MIB", "rbnEpsuSgiApnIndex"),
)
if mibBuilder.loadTexts:
    rbnEpsuSgiApnStatsEntry.setStatus("current")


class _RbnEpsuSgiApnIndex_Type(Unsigned32):
    """Custom type rbnEpsuSgiApnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnEpsuSgiApnIndex_Type.__name__ = "Unsigned32"
_RbnEpsuSgiApnIndex_Object = MibTableColumn
rbnEpsuSgiApnIndex = _RbnEpsuSgiApnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 1),
    _RbnEpsuSgiApnIndex_Type()
)
rbnEpsuSgiApnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnIndex.setStatus("current")


class _RbnEpsuSgiApnName_Type(SnmpAdminString):
    """Custom type rbnEpsuSgiApnName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RbnEpsuSgiApnName_Type.__name__ = "SnmpAdminString"
_RbnEpsuSgiApnName_Object = MibTableColumn
rbnEpsuSgiApnName = _RbnEpsuSgiApnName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 2),
    _RbnEpsuSgiApnName_Type()
)
rbnEpsuSgiApnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnName.setStatus("current")
_RbnEpsuSgiApnDlPktsRcvd_Type = Counter64
_RbnEpsuSgiApnDlPktsRcvd_Object = MibTableColumn
rbnEpsuSgiApnDlPktsRcvd = _RbnEpsuSgiApnDlPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 3),
    _RbnEpsuSgiApnDlPktsRcvd_Type()
)
rbnEpsuSgiApnDlPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlPktsRcvd.setUnits("Packets")
_RbnEpsuSgiApnDlOctetsRcvd_Type = Counter64
_RbnEpsuSgiApnDlOctetsRcvd_Object = MibTableColumn
rbnEpsuSgiApnDlOctetsRcvd = _RbnEpsuSgiApnDlOctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 4),
    _RbnEpsuSgiApnDlOctetsRcvd_Type()
)
rbnEpsuSgiApnDlOctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlOctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlOctetsRcvd.setUnits("Octets")
_RbnEpsuSgiApnDlPktsDiscarded_Type = Counter64
_RbnEpsuSgiApnDlPktsDiscarded_Object = MibTableColumn
rbnEpsuSgiApnDlPktsDiscarded = _RbnEpsuSgiApnDlPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 5),
    _RbnEpsuSgiApnDlPktsDiscarded_Type()
)
rbnEpsuSgiApnDlPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlPktsDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlPktsDiscarded.setUnits("Packets")
_RbnEpsuSgiApnUlPktsSent_Type = Counter64
_RbnEpsuSgiApnUlPktsSent_Object = MibTableColumn
rbnEpsuSgiApnUlPktsSent = _RbnEpsuSgiApnUlPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 6),
    _RbnEpsuSgiApnUlPktsSent_Type()
)
rbnEpsuSgiApnUlPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlPktsSent.setUnits("Packets")
_RbnEpsuSgiApnUlOctetsSent_Type = Counter64
_RbnEpsuSgiApnUlOctetsSent_Object = MibTableColumn
rbnEpsuSgiApnUlOctetsSent = _RbnEpsuSgiApnUlOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 7),
    _RbnEpsuSgiApnUlOctetsSent_Type()
)
rbnEpsuSgiApnUlOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlOctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlOctetsSent.setUnits("Octets")
_RbnEpsuSgiApnUlPktsDropped_Type = Counter64
_RbnEpsuSgiApnUlPktsDropped_Object = MibTableColumn
rbnEpsuSgiApnUlPktsDropped = _RbnEpsuSgiApnUlPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 8),
    _RbnEpsuSgiApnUlPktsDropped_Type()
)
rbnEpsuSgiApnUlPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlPktsDropped.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlPktsDropped.setUnits("Packets")
_RbnEpsuSgiApnDlV6PktsRcvd_Type = Counter64
_RbnEpsuSgiApnDlV6PktsRcvd_Object = MibTableColumn
rbnEpsuSgiApnDlV6PktsRcvd = _RbnEpsuSgiApnDlV6PktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 9),
    _RbnEpsuSgiApnDlV6PktsRcvd_Type()
)
rbnEpsuSgiApnDlV6PktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlV6PktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlV6PktsRcvd.setUnits("Packets")
_RbnEpsuSgiApnDlV6OctetsRcvd_Type = Counter64
_RbnEpsuSgiApnDlV6OctetsRcvd_Object = MibTableColumn
rbnEpsuSgiApnDlV6OctetsRcvd = _RbnEpsuSgiApnDlV6OctetsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 10),
    _RbnEpsuSgiApnDlV6OctetsRcvd_Type()
)
rbnEpsuSgiApnDlV6OctetsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlV6OctetsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnDlV6OctetsRcvd.setUnits("Octets")
_RbnEpsuSgiApnUlV6PktsSent_Type = Counter64
_RbnEpsuSgiApnUlV6PktsSent_Object = MibTableColumn
rbnEpsuSgiApnUlV6PktsSent = _RbnEpsuSgiApnUlV6PktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 11),
    _RbnEpsuSgiApnUlV6PktsSent_Type()
)
rbnEpsuSgiApnUlV6PktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlV6PktsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlV6PktsSent.setUnits("Packets")
_RbnEpsuSgiApnUlV6OctetsSent_Type = Counter64
_RbnEpsuSgiApnUlV6OctetsSent_Object = MibTableColumn
rbnEpsuSgiApnUlV6OctetsSent = _RbnEpsuSgiApnUlV6OctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 1, 5, 1, 1, 12),
    _RbnEpsuSgiApnUlV6OctetsSent_Type()
)
rbnEpsuSgiApnUlV6OctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlV6OctetsSent.setStatus("current")
if mibBuilder.loadTexts:
    rbnEpsuSgiApnUlV6OctetsSent.setUnits("Octets")
_RbnEpsuMIBConformance_ObjectIdentity = ObjectIdentity
rbnEpsuMIBConformance = _RbnEpsuMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 2)
)
_RbnEpsuMIBGroups_ObjectIdentity = ObjectIdentity
rbnEpsuMIBGroups = _RbnEpsuMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1)
)
_RbnEpsuMIBCompliances_ObjectIdentity = ObjectIdentity
rbnEpsuMIBCompliances = _RbnEpsuMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 2)
)

# Managed Objects groups

rbnEpsuS1uGtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 1)
)
rbnEpsuS1uGtpGroup.setObjects(
      *(("RBN-EPSU-MIB", "rbnEpsuS1uDlPktsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuS1uDlOctetsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuS1uDlPktsDropped"),
        ("RBN-EPSU-MIB", "rbnEpsuS1uDlPolicingPktsDropped"),
        ("RBN-EPSU-MIB", "rbnEpsuS1uDlUeIdlePktsDropped"),
        ("RBN-EPSU-MIB", "rbnEpsuS1uUlPktsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuS1uUlOctetsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuS1uUlPktsDiscarded"),
        ("RBN-EPSU-MIB", "rbnEpsuS1uUlBearerPktsDiscarded"),
        ("RBN-EPSU-MIB", "rbnEpsuS1uUlPolicingPktsDiscarded"))
)
if mibBuilder.loadTexts:
    rbnEpsuS1uGtpGroup.setStatus("current")

rbnEpsuSgwGtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 2)
)
rbnEpsuSgwGtpGroup.setObjects(
      *(("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPktsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlOctetsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPktsDiscarded"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPktsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlOctetsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPktsDropped"))
)
if mibBuilder.loadTexts:
    rbnEpsuSgwGtpGroup.setStatus("current")

rbnEpsuPgwGtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 3)
)
rbnEpsuPgwGtpGroup.setObjects(
      *(("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPktsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlOctetsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPktsDropped"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpDlPolicingPktsDropped"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPktsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlOctetsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPktsDiscarded"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlBearerPktsDiscarded"),
        ("RBN-EPSU-MIB", "rbnEpsuS5S8GtpUlPolicingPktsDiscarded"))
)
if mibBuilder.loadTexts:
    rbnEpsuPgwGtpGroup.setStatus("current")

rbnEpsuSgiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 4)
)
rbnEpsuSgiGroup.setObjects(
      *(("RBN-EPSU-MIB", "rbnEpsuSgiDlPktsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiDlOctetsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiDlV6PktsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiDlV6OctetsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiDlPktsDiscarded"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiUlPktsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiUlOctetsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiUlPktsDropped"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiUlV6PktsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiUlV6OctetsSent"))
)
if mibBuilder.loadTexts:
    rbnEpsuSgiGroup.setStatus("current")

rbnEspuSgiApnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 1, 5)
)
rbnEspuSgiApnGroup.setObjects(
      *(("RBN-EPSU-MIB", "rbnEpsuSgiApnName"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlPktsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlOctetsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlV6PktsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlV6OctetsRcvd"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnDlPktsDiscarded"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlPktsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlOctetsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlV6PktsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlV6OctetsSent"),
        ("RBN-EPSU-MIB", "rbnEpsuSgiApnUlPktsDropped"))
)
if mibBuilder.loadTexts:
    rbnEspuSgiApnGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnEpsuMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 47, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnEpsuMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-EPSU-MIB",
    **{"rbnEpsuMIB": rbnEpsuMIB,
       "rbnEpsuNotifcationGroup": rbnEpsuNotifcationGroup,
       "rbnEpsuStatMIBObjects": rbnEpsuStatMIBObjects,
       "rbnEpsuS1uGtp": rbnEpsuS1uGtp,
       "rbnEpsuS1uDlPktsSent": rbnEpsuS1uDlPktsSent,
       "rbnEpsuS1uDlOctetsSent": rbnEpsuS1uDlOctetsSent,
       "rbnEpsuS1uDlPktsDropped": rbnEpsuS1uDlPktsDropped,
       "rbnEpsuS1uDlPolicingPktsDropped": rbnEpsuS1uDlPolicingPktsDropped,
       "rbnEpsuS1uDlUeIdlePktsDropped": rbnEpsuS1uDlUeIdlePktsDropped,
       "rbnEpsuS1uUlPktsRcvd": rbnEpsuS1uUlPktsRcvd,
       "rbnEpsuS1uUlOctetsRcvd": rbnEpsuS1uUlOctetsRcvd,
       "rbnEpsuS1uUlPktsDiscarded": rbnEpsuS1uUlPktsDiscarded,
       "rbnEpsuS1uUlBearerPktsDiscarded": rbnEpsuS1uUlBearerPktsDiscarded,
       "rbnEpsuS1uUlPolicingPktsDiscarded": rbnEpsuS1uUlPolicingPktsDiscarded,
       "rbnEpsuSgwGtp": rbnEpsuSgwGtp,
       "rbnEpsuS5S8GtpDlPktsRcvd": rbnEpsuS5S8GtpDlPktsRcvd,
       "rbnEpsuS5S8GtpDlOctetsRcvd": rbnEpsuS5S8GtpDlOctetsRcvd,
       "rbnEpsuS5S8GtpDlPktsDiscarded": rbnEpsuS5S8GtpDlPktsDiscarded,
       "rbnEpsuS5S8GtpUlPktsSent": rbnEpsuS5S8GtpUlPktsSent,
       "rbnEpsuS5S8GtpUlOctetsSent": rbnEpsuS5S8GtpUlOctetsSent,
       "rbnEpsuS5S8GtpUlPktsDropped": rbnEpsuS5S8GtpUlPktsDropped,
       "rbnEpsuPgwGtp": rbnEpsuPgwGtp,
       "rbnEpsuS5S8GtpDlPktsSent": rbnEpsuS5S8GtpDlPktsSent,
       "rbnEpsuS5S8GtpDlOctetsSent": rbnEpsuS5S8GtpDlOctetsSent,
       "rbnEpsuS5S8GtpDlPktsDropped": rbnEpsuS5S8GtpDlPktsDropped,
       "rbnEpsuS5S8GtpDlPolicingPktsDropped": rbnEpsuS5S8GtpDlPolicingPktsDropped,
       "rbnEpsuS5S8GtpUlPktsRcvd": rbnEpsuS5S8GtpUlPktsRcvd,
       "rbnEpsuS5S8GtpUlOctetsRcvd": rbnEpsuS5S8GtpUlOctetsRcvd,
       "rbnEpsuS5S8GtpUlPktsDiscarded": rbnEpsuS5S8GtpUlPktsDiscarded,
       "rbnEpsuS5S8GtpUlBearerPktsDiscarded": rbnEpsuS5S8GtpUlBearerPktsDiscarded,
       "rbnEpsuS5S8GtpUlPolicingPktsDiscarded": rbnEpsuS5S8GtpUlPolicingPktsDiscarded,
       "rbnEpsuSgi": rbnEpsuSgi,
       "rbnEpsuSgiDlPktsRcvd": rbnEpsuSgiDlPktsRcvd,
       "rbnEpsuSgiDlOctetsRcvd": rbnEpsuSgiDlOctetsRcvd,
       "rbnEpsuSgiDlV6PktsRcvd": rbnEpsuSgiDlV6PktsRcvd,
       "rbnEpsuSgiDlV6OctetsRcvd": rbnEpsuSgiDlV6OctetsRcvd,
       "rbnEpsuSgiDlPktsDiscarded": rbnEpsuSgiDlPktsDiscarded,
       "rbnEpsuSgiUlPktsSent": rbnEpsuSgiUlPktsSent,
       "rbnEpsuSgiUlOctetsSent": rbnEpsuSgiUlOctetsSent,
       "rbnEpsuSgiUlV6PktsSent": rbnEpsuSgiUlV6PktsSent,
       "rbnEpsuSgiUlV6OctetsSent": rbnEpsuSgiUlV6OctetsSent,
       "rbnEpsuSgiUlPktsDropped": rbnEpsuSgiUlPktsDropped,
       "rbnEpsuSgiApn": rbnEpsuSgiApn,
       "rbnEpsuSgiApnStatsTable": rbnEpsuSgiApnStatsTable,
       "rbnEpsuSgiApnStatsEntry": rbnEpsuSgiApnStatsEntry,
       "rbnEpsuSgiApnIndex": rbnEpsuSgiApnIndex,
       "rbnEpsuSgiApnName": rbnEpsuSgiApnName,
       "rbnEpsuSgiApnDlPktsRcvd": rbnEpsuSgiApnDlPktsRcvd,
       "rbnEpsuSgiApnDlOctetsRcvd": rbnEpsuSgiApnDlOctetsRcvd,
       "rbnEpsuSgiApnDlPktsDiscarded": rbnEpsuSgiApnDlPktsDiscarded,
       "rbnEpsuSgiApnUlPktsSent": rbnEpsuSgiApnUlPktsSent,
       "rbnEpsuSgiApnUlOctetsSent": rbnEpsuSgiApnUlOctetsSent,
       "rbnEpsuSgiApnUlPktsDropped": rbnEpsuSgiApnUlPktsDropped,
       "rbnEpsuSgiApnDlV6PktsRcvd": rbnEpsuSgiApnDlV6PktsRcvd,
       "rbnEpsuSgiApnDlV6OctetsRcvd": rbnEpsuSgiApnDlV6OctetsRcvd,
       "rbnEpsuSgiApnUlV6PktsSent": rbnEpsuSgiApnUlV6PktsSent,
       "rbnEpsuSgiApnUlV6OctetsSent": rbnEpsuSgiApnUlV6OctetsSent,
       "rbnEpsuMIBConformance": rbnEpsuMIBConformance,
       "rbnEpsuMIBGroups": rbnEpsuMIBGroups,
       "rbnEpsuS1uGtpGroup": rbnEpsuS1uGtpGroup,
       "rbnEpsuSgwGtpGroup": rbnEpsuSgwGtpGroup,
       "rbnEpsuPgwGtpGroup": rbnEpsuPgwGtpGroup,
       "rbnEpsuSgiGroup": rbnEpsuSgiGroup,
       "rbnEspuSgiApnGroup": rbnEspuSgiApnGroup,
       "rbnEpsuMIBCompliances": rbnEpsuMIBCompliances,
       "rbnEpsuMIBCompliance": rbnEpsuMIBCompliance}
)
