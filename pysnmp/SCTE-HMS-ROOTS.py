# SNMP MIB module (SCTE-HMS-ROOTS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCTE-HMS-ROOTS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:07 2024
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

(scteHmsTree,) = mibBuilder.importSymbols(
    "SCTE-ROOT",
    "scteHmsTree")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PropertyIdent_ObjectIdentity = ObjectIdentity
propertyIdent = _PropertyIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 1)
)
_AlarmsIdent_ObjectIdentity = ObjectIdentity
alarmsIdent = _AlarmsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 2)
)
_CommonIdent_ObjectIdentity = ObjectIdentity
commonIdent = _CommonIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 3)
)
_PsIdent_ObjectIdentity = ObjectIdentity
psIdent = _PsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 4)
)
_FnIdent_ObjectIdentity = ObjectIdentity
fnIdent = _FnIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5)
)
_GenIdent_ObjectIdentity = ObjectIdentity
genIdent = _GenIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 6)
)
_TransponderInterfaceBusIdent_ObjectIdentity = ObjectIdentity
transponderInterfaceBusIdent = _TransponderInterfaceBusIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7)
)
_DownloadIdent_ObjectIdentity = ObjectIdentity
downloadIdent = _DownloadIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8)
)
_OaIdent_ObjectIdentity = ObjectIdentity
oaIdent = _OaIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 9)
)
_RfAmplifierIdent_ObjectIdentity = ObjectIdentity
rfAmplifierIdent = _RfAmplifierIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 10)
)
_InsidePlantIdent_ObjectIdentity = ObjectIdentity
insidePlantIdent = _InsidePlantIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-ROOTS",
    **{"propertyIdent": propertyIdent,
       "alarmsIdent": alarmsIdent,
       "commonIdent": commonIdent,
       "psIdent": psIdent,
       "fnIdent": fnIdent,
       "genIdent": genIdent,
       "transponderInterfaceBusIdent": transponderInterfaceBusIdent,
       "downloadIdent": downloadIdent,
       "oaIdent": oaIdent,
       "rfAmplifierIdent": rfAmplifierIdent,
       "insidePlantIdent": insidePlantIdent}
)
