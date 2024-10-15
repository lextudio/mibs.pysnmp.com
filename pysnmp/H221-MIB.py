# SNMP MIB module (H221-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H221-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:35 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

h221MIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 221, 2)
)
h221MIB.setRevisions(
        ("1998-05-25 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H221Stats_ObjectIdentity = ObjectIdentity
h221Stats = _H221Stats_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 1)
)
_H221InFrames_Type = Counter32
_H221InFrames_Object = MibScalar
h221InFrames = _H221InFrames_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1),
    _H221InFrames_Type()
)
h221InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221InFrames.setStatus("current")
_H221OutFrames_Type = Counter32
_H221OutFrames_Object = MibScalar
h221OutFrames = _H221OutFrames_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 2),
    _H221OutFrames_Type()
)
h221OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221OutFrames.setStatus("current")
_H221InFrameErrs_Type = Counter32
_H221InFrameErrs_Object = MibScalar
h221InFrameErrs = _H221InFrameErrs_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 3),
    _H221InFrameErrs_Type()
)
h221InFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221InFrameErrs.setStatus("current")
_H221FrameAlignmentErrs_Type = Counter32
_H221FrameAlignmentErrs_Object = MibScalar
h221FrameAlignmentErrs = _H221FrameAlignmentErrs_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 4),
    _H221FrameAlignmentErrs_Type()
)
h221FrameAlignmentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221FrameAlignmentErrs.setStatus("current")
_H221MultiFrameAlignmentErrs_Type = Counter32
_H221MultiFrameAlignmentErrs_Object = MibScalar
h221MultiFrameAlignmentErrs = _H221MultiFrameAlignmentErrs_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 5),
    _H221MultiFrameAlignmentErrs_Type()
)
h221MultiFrameAlignmentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221MultiFrameAlignmentErrs.setStatus("current")
_H221ErrorPerformance_Type = Counter32
_H221ErrorPerformance_Object = MibScalar
h221ErrorPerformance = _H221ErrorPerformance_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 6),
    _H221ErrorPerformance_Type()
)
h221ErrorPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221ErrorPerformance.setStatus("current")
_H221BASErrs_Type = Counter32
_H221BASErrs_Object = MibScalar
h221BASErrs = _H221BASErrs_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 7),
    _H221BASErrs_Type()
)
h221BASErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221BASErrs.setStatus("current")
_H221Events_ObjectIdentity = ObjectIdentity
h221Events = _H221Events_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 2)
)
_H221StatsMIBConfs_ObjectIdentity = ObjectIdentity
h221StatsMIBConfs = _H221StatsMIBConfs_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 3)
)
_H221StatsMIBGroups_ObjectIdentity = ObjectIdentity
h221StatsMIBGroups = _H221StatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 3, 1)
)
_H221StatsMIBCompl_ObjectIdentity = ObjectIdentity
h221StatsMIBCompl = _H221StatsMIBCompl_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 3, 2)
)

# Managed Objects groups

h221StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 1)
)
h221StatsGroup.setObjects(
      *(("H221-MIB", "h221InFrames"),
        ("H221-MIB", "h221OutFrames"),
        ("H221-MIB", "h221InFrameErrs"),
        ("H221-MIB", "h221FrameAlignmentErrs"),
        ("H221-MIB", "h221MultiFrameAlignmentErrs"),
        ("H221-MIB", "h221ErrorPerformance"),
        ("H221-MIB", "h221BASErrs"))
)
if mibBuilder.loadTexts:
    h221StatsGroup.setStatus("current")


# Notification objects

h221TooManyErrors = NotificationType(
    (1, 3, 6, 1, 3, 221, 2, 2, 1)
)
h221TooManyErrors.setObjects(
    ("H221-MIB", "h221ErrorPerformance")
)
if mibBuilder.loadTexts:
    h221TooManyErrors.setStatus(
        "current"
    )


# Notifications groups

h221EventsGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 2)
)
h221EventsGroup.setObjects(
    ("H221-MIB", "h221TooManyErrors")
)
if mibBuilder.loadTexts:
    h221EventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h221StatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 221, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    h221StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H221-MIB",
    **{"h221MIB": h221MIB,
       "h221Stats": h221Stats,
       "h221InFrames": h221InFrames,
       "h221OutFrames": h221OutFrames,
       "h221InFrameErrs": h221InFrameErrs,
       "h221FrameAlignmentErrs": h221FrameAlignmentErrs,
       "h221MultiFrameAlignmentErrs": h221MultiFrameAlignmentErrs,
       "h221ErrorPerformance": h221ErrorPerformance,
       "h221BASErrs": h221BASErrs,
       "h221Events": h221Events,
       "h221TooManyErrors": h221TooManyErrors,
       "h221StatsMIBConfs": h221StatsMIBConfs,
       "h221StatsMIBGroups": h221StatsMIBGroups,
       "h221StatsGroup": h221StatsGroup,
       "h221EventsGroup": h221EventsGroup,
       "h221StatsMIBCompl": h221StatsMIBCompl,
       "h221StatsCompliance": h221StatsCompliance}
)
