"""SNMP MIB module (AISYSCFG-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISYSCFG-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 10:13:11 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance")

(Counter32,
 Gauge32,
 iso,
 ModuleIdentity,
 TimeTicks,
 IpAddress,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 Unsigned32,
 MibIdentifier,
 Integer32,
 ObjectIdentity,
 Bits,
 Counter64,
 enterprises) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "Gauge32",
    "iso",
    "ModuleIdentity",
    "TimeTicks",
    "IpAddress",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "Unsigned32",
    "MibIdentifier",
    "Integer32",
    "ObjectIdentity",
    "Bits",
    "Counter64",
    "enterprises")

(TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString")


# MODULE-IDENTITY

aiSysCfg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32)
)
aiSysCfg.setLastUpdated("0104301700Z")
if mibBuilder.loadTexts:
    aiSysCfg.setOrganization("""\
Applied Innovation Inc.
""")
aiSysCfg.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSysCfg.setDescription("""\
MIB module for system parameters.
""")

aiSysCfgSoftware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 1)
)
aiSysCfgSoftware.setLastUpdated("0104301700Z")
if mibBuilder.loadTexts:
    aiSysCfgSoftware.setOrganization("""\
Applied Innovation Inc.
""")
aiSysCfgSoftware.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSysCfgSoftware.setDescription("""\
MIB module to describe software images. Any software/firmware
image/load/package should be describable by entries in aiSCSoftwareTable. The
set of (name, type, version, date) should uniquely identify any image loaded on
an AI box.
""")

aiSysCfgTime = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 2)
)
aiSysCfgTime.setLastUpdated("0104301700Z")
if mibBuilder.loadTexts:
    aiSysCfgTime.setOrganization("""\
Applied Innovation Inc.
""")
aiSysCfgTime.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSysCfgTime.setDescription("""\
MIB module for timekeeping.
""")

aiSysCfgPower = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 3)
)
aiSysCfgPower.setLastUpdated("0104301700Z")
if mibBuilder.loadTexts:
    aiSysCfgPower.setOrganization("""\
Applied Innovation Inc.
""")
aiSysCfgPower.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSysCfgPower.setDescription("""\
MIB module for Power Supplies.
""")

aiSysCfgFan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 4)
)
aiSysCfgFan.setLastUpdated("0104301700Z")
if mibBuilder.loadTexts:
    aiSysCfgFan.setOrganization("""\
Applied Innovation Inc.
""")
aiSysCfgFan.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSysCfgFan.setDescription("""\
MIB module for fans.
""")

aiSysCfgTemp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 32, 5)
)
aiSysCfgTemp.setLastUpdated("0104301700Z")
if mibBuilder.loadTexts:
    aiSysCfgTemp.setOrganization("""\
Applied Innovation Inc.
""")
aiSysCfgTemp.setContactInfo("""\
 Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation
Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email:
snmp@aiinet.com
""")
if mibBuilder.loadTexts:
    aiSysCfgTemp.setDescription("""\
MIB module for Temperature Probes.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISYSCFG-MIB",
    **{"aii": aii,
       "aiSysCfg": aiSysCfg,
       "aiSysCfgSoftware": aiSysCfgSoftware,
       "aiSysCfgTime": aiSysCfgTime,
       "aiSysCfgPower": aiSysCfgPower,
       "aiSysCfgFan": aiSysCfgFan,
       "aiSysCfgTemp": aiSysCfgTemp}
)
