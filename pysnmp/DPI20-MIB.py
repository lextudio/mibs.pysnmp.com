# SNMP MIB module (DPI20-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DPI20-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:20 2024
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

dpi20MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2, 1)
)
dpi20MIB.setRevisions(
        ("1996-09-30 00:00",
         "1996-05-01 00:00",
         "1995-05-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmDPI_ObjectIdentity = ObjectIdentity
ibmDPI = _IbmDPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2)
)
_DpiPort_ObjectIdentity = ObjectIdentity
dpiPort = _DpiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 1)
)


class _DpiPortForTCP_Type(Integer32):
    """Custom type dpiPortForTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpiPortForTCP_Type.__name__ = "Integer32"
_DpiPortForTCP_Object = MibScalar
dpiPortForTCP = _DpiPortForTCP_Object(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 1),
    _DpiPortForTCP_Type()
)
dpiPortForTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiPortForTCP.setStatus("current")


class _DpiPortForUDP_Type(Integer32):
    """Custom type dpiPortForUDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpiPortForUDP_Type.__name__ = "Integer32"
_DpiPortForUDP_Object = MibScalar
dpiPortForUDP = _DpiPortForUDP_Object(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 2),
    _DpiPortForUDP_Type()
)
dpiPortForUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiPortForUDP.setStatus("current")
_DpiPathNameForUnixStream_Type = DisplayString
_DpiPathNameForUnixStream_Object = MibScalar
dpiPathNameForUnixStream = _DpiPathNameForUnixStream_Object(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 1, 3),
    _DpiPathNameForUnixStream_Type()
)
dpiPathNameForUnixStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpiPathNameForUnixStream.setStatus("current")
_DpiMIBConformance_ObjectIdentity = ObjectIdentity
dpiMIBConformance = _DpiMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 2)
)
_DpiMIBCompliances_ObjectIdentity = ObjectIdentity
dpiMIBCompliances = _DpiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 1)
)
_DpiMIBGroups_ObjectIdentity = ObjectIdentity
dpiMIBGroups = _DpiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 2)
)

# Managed Objects groups

dpiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 2, 1)
)
dpiGroup.setObjects(
      *(("DPI20-MIB", "dpiPortForTCP"),
        ("DPI20-MIB", "dpiPortForUDP"))
)
if mibBuilder.loadTexts:
    dpiGroup.setStatus("current")

dpiGroupUnix = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 2, 2)
)
dpiGroupUnix.setObjects(
    ("DPI20-MIB", "dpiPathNameForUnixStream")
)
if mibBuilder.loadTexts:
    dpiGroupUnix.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dpiMIBCompliance.setStatus(
        "current"
    )

dpiMIBComplianceUnix = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    dpiMIBComplianceUnix.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPI20-MIB",
    **{"ibm": ibm,
       "ibmDPI": ibmDPI,
       "dpi20MIB": dpi20MIB,
       "dpiPort": dpiPort,
       "dpiPortForTCP": dpiPortForTCP,
       "dpiPortForUDP": dpiPortForUDP,
       "dpiPathNameForUnixStream": dpiPathNameForUnixStream,
       "dpiMIBConformance": dpiMIBConformance,
       "dpiMIBCompliances": dpiMIBCompliances,
       "dpiMIBCompliance": dpiMIBCompliance,
       "dpiMIBComplianceUnix": dpiMIBComplianceUnix,
       "dpiMIBGroups": dpiMIBGroups,
       "dpiGroup": dpiGroup,
       "dpiGroupUnix": dpiGroupUnix}
)
