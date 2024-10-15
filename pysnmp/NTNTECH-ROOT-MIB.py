# SNMP MIB module (NTNTECH-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTNTECH-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:42 2024
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

ntntechRootMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8059)
)
ntntechRootMIB.setRevisions(
        ("1902-08-28 11:57",
         "1902-10-22 02:00",
         "1904-10-11 01:01",
         "1904-11-17 10:09")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtnIpAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:2x:3x:4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class NtnDefaultGateway(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:2x:3x:4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class NtnSubnetMask(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:2x:3x:4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class NtnDisplayString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class NtnMacAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class NtnTimeTicks(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class NtnCounter32(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class NtnGauge32(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class NtnTruthValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )



# MIB Managed Objects in the order of their OIDs

_NtntechNamingTree_ObjectIdentity = ObjectIdentity
ntntechNamingTree = _NtntechNamingTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1)
)
_NtntechChassis_ObjectIdentity = ObjectIdentity
ntntechChassis = _NtntechChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1)
)
_NtntechChassisConfigurationMIB_ObjectIdentity = ObjectIdentity
ntntechChassisConfigurationMIB = _NtntechChassisConfigurationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 1)
)
_NtntechChassisStatusMIB_ObjectIdentity = ObjectIdentity
ntntechChassisStatusMIB = _NtntechChassisStatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 1, 2)
)
_NtntechInterfaceModule_ObjectIdentity = ObjectIdentity
ntntechInterfaceModule = _NtntechInterfaceModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2)
)
_NtntechInterfaceModuleConfigurationMIB_ObjectIdentity = ObjectIdentity
ntntechInterfaceModuleConfigurationMIB = _NtntechInterfaceModuleConfigurationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 1)
)
_NtntechInterfaceModuleStatusMIB_ObjectIdentity = ObjectIdentity
ntntechInterfaceModuleStatusMIB = _NtntechInterfaceModuleStatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 2)
)
_NtntechQoSMIB_ObjectIdentity = ObjectIdentity
ntntechQoSMIB = _NtntechQoSMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 2, 3)
)
_NtntechNMSTraps_ObjectIdentity = ObjectIdentity
ntntechNMSTraps = _NtntechNMSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3)
)
_NtntechNMSTrapsMIB_ObjectIdentity = ObjectIdentity
ntntechNMSTrapsMIB = _NtntechNMSTrapsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 1)
)
_NtntechSystemObjects_ObjectIdentity = ObjectIdentity
ntntechSystemObjects = _NtntechSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 4)
)
_NtntechSystemObjectsIdentifierMIB_ObjectIdentity = ObjectIdentity
ntntechSystemObjectsIdentifierMIB = _NtntechSystemObjectsIdentifierMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8059, 1, 4, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTNTECH-ROOT-MIB",
    **{"NtnIpAddress": NtnIpAddress,
       "NtnDefaultGateway": NtnDefaultGateway,
       "NtnSubnetMask": NtnSubnetMask,
       "NtnDisplayString": NtnDisplayString,
       "NtnMacAddress": NtnMacAddress,
       "NtnTimeTicks": NtnTimeTicks,
       "NtnCounter32": NtnCounter32,
       "NtnGauge32": NtnGauge32,
       "NtnTruthValue": NtnTruthValue,
       "ntntechRootMIB": ntntechRootMIB,
       "ntntechNamingTree": ntntechNamingTree,
       "ntntechChassis": ntntechChassis,
       "ntntechChassisConfigurationMIB": ntntechChassisConfigurationMIB,
       "ntntechChassisStatusMIB": ntntechChassisStatusMIB,
       "ntntechInterfaceModule": ntntechInterfaceModule,
       "ntntechInterfaceModuleConfigurationMIB": ntntechInterfaceModuleConfigurationMIB,
       "ntntechInterfaceModuleStatusMIB": ntntechInterfaceModuleStatusMIB,
       "ntntechQoSMIB": ntntechQoSMIB,
       "ntntechNMSTraps": ntntechNMSTraps,
       "ntntechNMSTrapsMIB": ntntechNMSTrapsMIB,
       "ntntechSystemObjects": ntntechSystemObjects,
       "ntntechSystemObjectsIdentifierMIB": ntntechSystemObjectsIdentifierMIB}
)
