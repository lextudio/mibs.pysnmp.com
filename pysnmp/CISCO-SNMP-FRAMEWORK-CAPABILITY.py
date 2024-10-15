# SNMP MIB module (CISCO-SNMP-FRAMEWORK-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SNMP-FRAMEWORK-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:31 2024
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

(ciscoAgentCapability,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoAgentCapability")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSnmpFrameworkCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 315)
)
ciscoSnmpFrameworkCapability.setRevisions(
        ("2007-11-12 00:00",
         "2006-05-27 00:00",
         "2003-09-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cSnmpFrameworkCapCatOSV05R0401 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 315, 1)
)
if mibBuilder.loadTexts:
    cSnmpFrameworkCapCatOSV05R0401.setProductRelease("Cisco CatOS 5.4(1).")
if mibBuilder.loadTexts:
    cSnmpFrameworkCapCatOSV05R0401.setStatus(
        "current"
    )

cSnmpFrameworkCapACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 315, 2)
)
if mibBuilder.loadTexts:
    cSnmpFrameworkCapACSWV03R000.setProductRelease("""\
ACSW (Application Control Software) 3.0
                          for Application Control Engine (ACE) 
                          Service Module.""")
if mibBuilder.loadTexts:
    cSnmpFrameworkCapACSWV03R000.setStatus(
        "current"
    )

cSnmpFrameworkCapc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 315, 3)
)
if mibBuilder.loadTexts:
    cSnmpFrameworkCapc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                         for ACE 4710 Application Control Engine 
                         Appliance""")
if mibBuilder.loadTexts:
    cSnmpFrameworkCapc4710aceVA1R700.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNMP-FRAMEWORK-CAPABILITY",
    **{"ciscoSnmpFrameworkCapability": ciscoSnmpFrameworkCapability,
       "cSnmpFrameworkCapCatOSV05R0401": cSnmpFrameworkCapCatOSV05R0401,
       "cSnmpFrameworkCapACSWV03R000": cSnmpFrameworkCapACSWV03R000,
       "cSnmpFrameworkCapc4710aceVA1R700": cSnmpFrameworkCapc4710aceVA1R700}
)
