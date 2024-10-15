# SNMP MIB module (CISCO-BULK-FILE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BULK-FILE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:25 2024
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

ciscoBulkFileCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 188)
)
ciscoBulkFileCapability.setRevisions(
        ("2006-02-06 00:00",
         "2003-11-13 00:00",
         "2002-02-17 00:00",
         "2000-12-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoBulkFileCapabilityV1R0 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 188, 1)
)
if mibBuilder.loadTexts:
    ciscoBulkFileCapabilityV1R0.setProductRelease("Cisco IOS mc 1.0")
if mibBuilder.loadTexts:
    ciscoBulkFileCapabilityV1R0.setStatus(
        "current"
    )

ciscoBulkFileCapabilityV2R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 188, 2)
)
if mibBuilder.loadTexts:
    ciscoBulkFileCapabilityV2R00.setProductRelease("""\
MGX8850 Release 2.00,
                          BPX SES Release 1.00.""")
if mibBuilder.loadTexts:
    ciscoBulkFileCapabilityV2R00.setStatus(
        "current"
    )

ciscoBulkFileCapabilityV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 188, 3)
)
if mibBuilder.loadTexts:
    ciscoBulkFileCapabilityV3R00.setProductRelease("""\
MGX8850 Release 3.00,
                          BPX SES Release 3.00,
                          VXSM  Release 5.0.0.""")
if mibBuilder.loadTexts:
    ciscoBulkFileCapabilityV3R00.setStatus(
        "current"
    )

ciscoBulkFileCapCRS1V2R0 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 188, 4)
)
if mibBuilder.loadTexts:
    ciscoBulkFileCapCRS1V2R0.setProductRelease("Cisco IOS XR 2.0 for CRS-1")
if mibBuilder.loadTexts:
    ciscoBulkFileCapCRS1V2R0.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BULK-FILE-CAPABILITY",
    **{"ciscoBulkFileCapability": ciscoBulkFileCapability,
       "ciscoBulkFileCapabilityV1R0": ciscoBulkFileCapabilityV1R0,
       "ciscoBulkFileCapabilityV2R00": ciscoBulkFileCapabilityV2R00,
       "ciscoBulkFileCapabilityV3R00": ciscoBulkFileCapabilityV3R00,
       "ciscoBulkFileCapCRS1V2R0": ciscoBulkFileCapCRS1V2R0}
)
